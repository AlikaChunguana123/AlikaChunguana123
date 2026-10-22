# Margin Call — "$176 mil/hora" (português)

`margincall2-portugues.mp4` — 59,5 s, 720×1280.

Mesmo formato do original: cabeçalho preto em cima, vídeo com tarja, legendas
centradas em baixo.

## Cabeçalho

| | |
|---|---|
| Linha laranja | *Margin Call (2011)* — Arial Itálico 22, espaço +0,5, x=64, base 285, cor #FFDE62 |
| Linha 1 | Despediram-no e pagaram |
| Linha 2 | $176 mil/hora para o ter de volta. |

Título em Arial 41, x=66, bases 336 e 390 — as mesmas do original.

## Legendas

35 legendas, com os tempos medidos no vídeo. Arial 39, espaço +0,5, centradas
em x=358. Uma linha → base 949; duas linhas → bases 930 e 968.

## Como foi feito

O tipo de letra foi identificado por IoU contra o original inglês: **Arial**
(0,689 contra 0,472 do Roboto). O cabeçalho estava sobre preto puro, por isso
foi simplesmente tapado e reescrito.

As legendas estavam gravadas na imagem. Em cada um dos 1784 fotogramas,
detectei-as como pixels claros junto ao contorno escuro, filtrei por
componentes do tamanho de letra (altura 7–95 px, largura ≤ 280) e apaguei-as
com `cv2.inpaint`. O filtro teve de aceitar blocos até 95 px de altura: quando
as duas linhas ficam juntas sobre um fundo claro — a camisa branca — fundem-se
num só componente, e um limite mais baixo deixava inglês por apagar.

`margincall2-legendas-pt.srt` tem as legendas em texto, caso queiras alterar
alguma frase.
