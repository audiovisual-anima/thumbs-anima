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

## Caixa para 6 porta-copos

Caixa com tampa no formato do logo. Tudo deriva do contorno do porta-copos com 2 mm
de deslocamento uniforme (0,5 de folga + 1,5 de parede), o que preserva o formato.

| | |
|---|---|
| Externo | **94,0 × 102,8 × 33,0 mm** (largura pedida; 102 não fecha — o porta-copos tem 98,84) |
| Interno | 91,0 × 99,8 mm · 24,4 mm livres para os 6 (24,0) |
| Parede / fundo | 1,5 / 1,6 mm |
| Tampa | placa 3,0 + aba interna 4,0 (0,2 de folga), flush com a caixa |
| Logo na tampa | branco embutido 0,8 mm, escalado ao contorno da tampa |
| Acabamento | chanfro 0,6 no pé e no topo; V de 0,4 + 0,4 na junta; tampa impressa virada para a placa |

Arquivos:

- `Anima-Caixa-A1-base.3mf` — base verde, 1 cor. **Validada**: 30,8 g, 52 min.
- `Anima-Caixa-A1-tampa-2cores.3mf` — tampa com logo branco (filamento 2). Exige AMS.
  Geometria validada com 1 filamento: 22,9 g, 41 min.
- `Anima-Caixa-A1-completa-2cores.3mf` — base + tampa numa mesa. Exige AMS. 53,6 g, 1h24.
- STLs: `Anima-Caixa-1-base-verde`, `Anima-Caixa-2-tampa-verde`, `Anima-Caixa-3-tampa-logo-branco`.

Encaixe: a aba tem 0,2 mm de folga radial — justo, como pedido. Se sair apertado
demais na sua impressora, o ajuste é escalar só a **tampa** em 99,5% no XY.

## Se quiser mudar o tamanho

4 mm é a altura pedida e funciona bem. Abaixo de 3 mm a peça fica flexível e
perde a cara de porta-copos. Para escalar, escale **só em X e Y** e mantenha os
4 mm de Z — senão o rebaixo do logo sai raso demais ou fundo demais.
