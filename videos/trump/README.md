# Trump — $900 milhões de dívida (português)

`trump-portugues.mp4` — 91,8 s, 1080×1920.

Fonte: *The Ellen DeGeneres Show*, entrevista a Donald Trump. No próprio
vídeo ele refere o programa *The Apprentice*, que estreou em 2004, por isso
a entrevista é de 2004 ou depois. Não consegui confirmar a data exacta numa
fonte fiável, por isso não a indico.

## O que foi feito

**1. Marca de água removida.** O "CHAD MONEY" era semi-transparente, por isso
não se detecta por cor nem por imobilidade. Isolei-o pela componente de alta
frequência mediana ao longo de 28 fotogramas — os contornos do logótipo são
constantes, o fundo não. Daí saiu o traçado exacto das letras, que preenchi e
apaguei com `removelogo`.

**2. Legendas inglesas removidas.** São brancas com sombra preta forte
(deslocamento 3,6 px). O detector por fotograma é: pixel claro que tem preto
na vizinhança, fechado, preenchido e filtrado por componentes de altura de
letra (20–100 px). Depois `cv2.inpaint` TELEA só na faixa das legendas.

**3. Letra identificada: Anton.** Comparei 30 tipos condensados/display por
IoU contra o original inglês. Anton deu 0,489 contra 0,383 do segundo
classificado (Big Shoulders Display) — uma diferença grande. Corpo 75,
espacejamento −1, centrado em x = 540, linhas de base 881 / 990 / 1097
(passo 108,5).

**4. 51 legendas em português**, com os tempos reais medidos no vídeo
(segmentação por assinatura de perfil de colunas). Cobrem 84,9 s dos 91,8 s.

**5. Título** em Anton corpo 80, nos primeiros 8,4 s, com fade.

Também aqui: `trump-legendas-pt.srt`, caso queiras editar as legendas.
