param(
  [Parameter(Mandatory=$true)][string]$Project,                       # ID do projeto Google Cloud
  [Parameter(Mandatory=$true)][string]$Manifest,                      # caminho do JSON (id, scene/image, hook, line)
  [Parameter(Mandatory=$true)][string]$ImagesDir,                     # pasta com as imagens da personagem
  [Parameter(Mandatory=$true)][string]$OutDir,                        # pasta de saída dos .mp4
  [string]$SpeakerDesc = "a person",                                  # descrição curta da personagem (qualquer nicho)
  [string]$Language = "Brazilian Portuguese",                         # idioma falado no vídeo
  [string]$Model = "veo-3.0-fast-generate-001",
  [int]$Duration = 8,
  [string]$Location = "us-central1"
)
# Gera vídeos 9:16 com áudio no Veo (Vertex AI) por image-to-video: cada imagem vira o 1º quadro.
# Usa curl.exe (PowerShell IRM dá erro TLS/417). Escreve status incremental em OutDir\run_status.txt.
$ErrorActionPreference = "Continue"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$gcloud = "$env:LOCALAPPDATA\GoogleCloudSDK\google-cloud-sdk\bin\gcloud.cmd"
$utf8 = New-Object Text.UTF8Encoding($false)
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$status = Join-Path $OutDir "run_status.txt"
function Log($m){ "$(Get-Date -Format HH:mm:ss)  $m" | Out-File $status -Append -Encoding utf8 }
function Token { (& $gcloud auth print-access-token).Trim() }
"" | Out-File $status -Encoding utf8; Log "INICIO"

$data = Get-Content $Manifest -Raw -Encoding UTF8 | ConvertFrom-Json
$videos = @(if ($data.videos) { $data.videos } else { $data })   # aceita {videos:[...]} ou [...]; força lista (corrige 1 item só)

# pré-carrega imagens em base64 (resolve por campo 'image' ou por 'scene' -> *scene*.png)
$imgCache = @{}
function Get-ImgB64($item) {
  $file = $null
  if ($item.image) { $file = Join-Path $ImagesDir $item.image }
  elseif ($item.scene) { $file = (Get-ChildItem $ImagesDir -Filter "*$($item.scene)*" | Select-Object -First 1).FullName }
  if (-not $file -or -not (Test-Path $file)) { return $null }
  if (-not $imgCache.ContainsKey($file)) { $imgCache[$file] = [Convert]::ToBase64String([IO.File]::ReadAllBytes($file)) }
  return $imgCache[$file]
}

$base = "https://$Location-aiplatform.googleapis.com/v1/projects/$Project/locations/$Location/publishers/google/models/$Model"
$token = Token

# SUBMIT
foreach ($v in $videos) {
  $b64 = Get-ImgB64 $v
  if (-not $b64) { Add-Member -InputObject $v -NotePropertyName st -NotePropertyValue "sem_imagem" -Force; Log "SEM IMAGEM $($v.id)"; continue }
  $desc = if ($v.speaker) { $v.speaker } else { $SpeakerDesc }
  if ($v.prompt) { $prompt = $v.prompt }  # se o item trouxer um prompt completo, usa ele
  else { $prompt = "$desc looks directly into the camera and speaks in warm, natural $Language with clear, correct pronunciation, saying: '$($v.line)' Subtle natural facial movement and lip sync, gentle ambient sound, candid documentary style, vertical 9:16." }
  $body = @{ instances=@(@{ prompt=$prompt; image=@{ bytesBase64Encoded=$b64; mimeType="image/png" } }); parameters=@{ aspectRatio="9:16"; sampleCount=1; durationSeconds=$Duration; generateAudio=$true } } | ConvertTo-Json -Depth 8
  $bf = Join-Path $env:TEMP ("vbody_"+$v.id+".json"); [IO.File]::WriteAllText($bf,$body,$utf8)
  $op=$null
  for ($t=1;$t -le 5;$t++){ $r=& curl.exe -s -X POST "${base}:predictLongRunning" -H "Authorization: Bearer $token" -H "Content-Type: application/json; charset=utf-8" -H "Expect:" --data "@$bf"; $jr=$null; try{$jr=$r|ConvertFrom-Json}catch{}; if($jr.name){$op=$jr.name;break}; Start-Sleep 10; $token=Token }
  Add-Member -InputObject $v -NotePropertyName op -NotePropertyValue $op -Force
  Add-Member -InputObject $v -NotePropertyName st -NotePropertyValue $(if($op){"submitted"}else{"submit_failed"}) -Force
  Log "SUBMIT $($v.id) $(if($op){'OK'}else{'FALHOU'})"
}
Log "SUBMIT COMPLETO"

# POLL + DOWNLOAD
$deadline=(Get-Date).AddMinutes(45)
do {
  $token=Token
  foreach ($v in ($videos | Where-Object { $_.st -eq "submitted" })) {
    $ob=(@{operationName=$v.op}|ConvertTo-Json); $obf=Join-Path $env:TEMP ("vob_"+$v.id+".json"); [IO.File]::WriteAllText($obf,$ob,$utf8)
    $r=& curl.exe -s -X POST "${base}:fetchPredictOperation" -H "Authorization: Bearer $token" -H "Content-Type: application/json" -H "Expect:" --data "@$obf"
    $j=$null; try{$j=$r|ConvertFrom-Json}catch{}
    if ($j.done) {
      if ($j.response.videos) {
        $name = if ($v.scene) { "$($v.id)_$($v.scene).mp4" } else { "$($v.id).mp4" }
        $out = Join-Path $OutDir $name
        [IO.File]::WriteAllBytes($out, [Convert]::FromBase64String($j.response.videos[0].bytesBase64Encoded))
        $v.st="done"; Log "DONE $($v.id) -> $name"
      } else { $v.st="filtered"; Log "FILTERED $($v.id) rai=$($j.response.raiMediaFilteredCount)" }
    }
  }
  $done=@($videos | Where-Object { $_.st -in @("done","filtered","submit_failed","sem_imagem") }).Count
  Log "PROGRESSO $done/$($videos.Count)"
  if ($done -ge $videos.Count) { break }
  Start-Sleep 20
} while ((Get-Date) -lt $deadline)

$videos | ConvertTo-Json -Depth 8 | Out-File (Join-Path $OutDir "results.json") -Encoding utf8
$ok=@($videos|?{$_.st -eq "done"}).Count
Log "FIM prontos=$ok de $($videos.Count)"
