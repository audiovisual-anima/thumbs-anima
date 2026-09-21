# Porta-copos Anima Podcast — arquivos de impressão 3D

Logo do Anima Podcast convertido em porta-copos, configurado para **Bambu Lab A1
(bico 0,4)** com **Generic PLA**.

| | |
|---|---|
| Medidas | **90,0 × 98,8 × 4,0 mm** |
| Altura de camada | 0,20 mm — **20 camadas** |
| Logo | rebaixado **0,8 mm** (4 camadas) |
| Material | Generic PLA, ~**22,5 g** |
| Tempo estimado | ~**41 min** |
| Mesa | Textured PEI Plate |
| Suportes | nenhum |

As medidas vêm do próprio SVG (90 mm de largura), então a proporção do logo está
preservada exatamente.

---

## Qual arquivo usar

### `Anima-PortaCopos-A1-1cor.3mf` — recomendado

Projeto completo do Bambu Studio: impressora, filamento, processo e posição na
mesa já definidos. **Abra e mande imprimir.**

O logo fica **rebaixado 0,8 mm** na face de cima, então ele aparece mesmo numa
impressão de cor única. Imprime com a face do logo para cima, sem suportes.

Este arquivo foi **fatiado e validado** na linha de comando do próprio Bambu
Studio: 20 camadas, 4,00 mm, 22,47 g, 41m03s.

### `Anima-PortaCopos-A1-2cores.3mf` — só se você tiver AMS lite

Mesma peça, mas o logo é uma **peça separada embutida** no verde (filamento 2),
e a peça é impressa **com o logo virado para a placa** — assim a face de
exibição sai lisa, com o acabamento da chapa.

Duas cores na mesma camada exigem AMS: o logo é cercado de verde em todas as
camadas em que aparece, então não dá para resolver com uma troca manual de
filamento. **Sem AMS, use o arquivo de 1 cor.**

> Ressalva honesta: este arquivo de 2 cores **não pôde ser validado aqui**. A CLI
> do Bambu Studio não fatia nenhum trabalho de 2 filamentos para a A1 — inclusive
> um arquivo gerado pelo próprio Bambu Studio passa a falhar assim que uma segunda
> cor é declarada. É limitação do modo headless, sem contexto de AMS, não do
> arquivo. Confira o preview no Bambu Studio antes de imprimir.

### STLs

`Anima-PortaCopos-1-corpo-verde.stl` e `Anima-PortaCopos-2-letras-brancas.stl` —
as duas peças soltas, para usar em qualquer outro fatiador. As duas são malhas
fechadas (watertight) e já vêm alinhadas entre si: é só carregar as duas juntas.

---

## Configuração aplicada

Parte do perfil de sistema **0.20mm Standard @BBL A1** com quatro ajustes, feitos
porque a peça é chata e larga:

| Ajuste | Sistema | Aqui | Porquê |
|---|---|---|---|
| Paredes | 2 | **3** | borda mais firme e limpa no contorno do balão |
| Camadas de baixo | 3 | **5** | face que encosta na mesa, sem transparência |
| Camadas de topo | 5 | **5** | fecha bem o fundo do rebaixo do logo |
| Preenchimento | 15% | **30%** | peça de 4 mm não pode soar oca |

Tudo o mais é o perfil de fábrica. Os ajustes ficam declarados no projeto, então
o Bambu Studio mostra o preset como modificado e você vê exatamente o que mudou.

## Conferências feitas no modelo

- Traços do logo com mais de 4 mm de espessura — folga enorme para o bico de 0,4.
- Menor vão entre as barras: **1,53 mm** (cabe 2 perímetros sem fundir).
- Malhas fechadas, normais coerentes, apoiadas em z = 0.
- G-code conferido camada a camada: 1ª camada sólida, miolo em grade, e os
  5 vazios das barras aparecendo nas camadas de topo.

## Se quiser mudar o tamanho

4 mm é a altura pedida e funciona bem. Abaixo de 3 mm a peça fica flexível e
perde a cara de porta-copos. Para escalar, escale **só em X e Y** e mantenha os
4 mm de Z — senão o rebaixo do logo sai raso demais ou fundo demais.
