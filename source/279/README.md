# #279 — Troca do casal de apresentadores

Arquivos-fonte para regenerar as thumbs do episódio #279 (Os bastidores do filme de Guido Schaffer).

- `modelo-base-279.png` — modelo original 1920x1080 (base, com o casal antigo).
- `casal-apresentadores-recorte.png` — recorte PNG do casal novo (transparente).
- `compose.py` — compõe o casal novo sobre o modelo, removendo o casal antigo,
  preservando a borda verde e recolocando os textos POR CIMA (nada sobreposto).
  Uso: `py compose.py <escala> <xoff> <ytop> <label> [grid]`

Variações entregues (em `../review/279/`):
- A (fiel ao modelo)  = escala 0.50 / xoff -40 / ytop 250
- B (casal inteiro)   = escala 0.485 / xoff 25 / ytop 255
- C (casal maior)     = escala 0.58 / xoff -35 / ytop 240

Observacao: feito localmente com Pillow porque o MCP do Canva estava desconectado.
Subtitulo do modelo veio truncado no original ("...E S / CASTELO").
