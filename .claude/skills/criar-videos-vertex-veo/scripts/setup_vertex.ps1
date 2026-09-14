param(
  [Parameter(Mandatory=$true)][string]$Project   # ID do projeto Google Cloud (ex: project-2b35e859-...)
)
# Instala o Google Cloud SDK (se preciso), faz login no navegador, define o projeto e liga a API do Vertex.
# O login é do usuário (abre o navegador). O Claude nunca vê a senha.
$ErrorActionPreference = "Stop"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$base = "$env:LOCALAPPDATA\GoogleCloudSDK"
$gcloud = "$base\google-cloud-sdk\bin\gcloud.cmd"

if (-not (Test-Path $gcloud)) {
  Write-Host "Instalando o Google Cloud SDK..."
  New-Item -ItemType Directory -Force -Path $base | Out-Null
  $zip = Join-Path $base "gcloud.zip"
  $ProgressPreference = "SilentlyContinue"
  Invoke-WebRequest -Uri "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-windows-x86_64-bundled-python.zip" -OutFile $zip
  Expand-Archive -Path $zip -DestinationPath $base -Force
  & "$base\google-cloud-sdk\install.bat" --quiet --path-update true --usage-reporting false | Out-Null
}
if (-not (Test-Path $gcloud)) { throw "Falha ao instalar o gcloud." }

# Login (abre o navegador para o usuário). Se já estiver logado, não força.
$accounts = & $gcloud auth list --filter=status:ACTIVE --format="value(account)" 2>$null
if (-not $accounts) {
  Write-Host "Abrindo o navegador para login. Escolha a conta Google com os créditos do Vertex..."
  & $gcloud auth login --quiet
}

& $gcloud config set project $Project 2>$null | Out-Null
Write-Host "Ligando a API do Vertex AI (pode levar ~1 min)..."
& $gcloud services enable aiplatform.googleapis.com 2>$null | Out-Null

$tok = (& $gcloud auth print-access-token 2>$null)
if ($tok -and $tok.Length -gt 30) { Write-Host "SETUP_OK projeto=$Project" }
else { Write-Host "SETUP_FALHOU: não consegui obter token. Refaça o login." }
