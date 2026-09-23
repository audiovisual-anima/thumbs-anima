# Marcadores de livro Anima — arquivos de impressão (Bambu A1 + AMS lite)

Dois marcadores de página de encaixe, a partir de `Marcador1.svg` (barras do logo) e
`Marcador2.svg` (palavra "anima"), montados sobre o clipe do marcador de referência
("Dia dos professores").

| | |
|---|---|
| Medidas | **40,0 × 190,0 × 2,0 mm** cada |
| Cores | corpo **branco** · balão **verde #00A859** embutido 0,6 mm · barras/letras brancas (vazios no verde) |
| Filamentos | 1 = branco, 2 = verde — Generic PLA @BBL A1, 220 °C / mesa 65 °C |
| Orientação | **face do logo na placa** (PEI texturizada): superfície lisa, sem linhas |
| Camada | 0,20 mm · 10 camadas · trocas de cor só nas 3 primeiras |
| Suporte · brim | nenhum · automático (não gera nada numa placa de 2 mm) |
| Estimativa | 109 min e 29,6 g para os dois (sem contar a purga das trocas) |

## Decisões de layout (confirmadas com você)

- Largura 40 mm com **logo proporcional**: o balão foi reduzido a 0,8× (40,0 × 43,9 mm) sem
  distorção; o corpo do clipe mantém a largura original de 37,8 mm e ganhou 8,3 mm de trecho
  reto (inserido a 75 mm do fundo, ponta arredondada intacta) para fechar 190 mm.
  Sobreposição balão/corpo mantida proporcional (12,2 mm).
- Canal do clipe: 2,6 mm, atravessa a peça — moldura + língua central, como na referência.
  A pedido, o recorte começa **2 mm abaixo da ponta do balão** (as pernas do canal foram
  estendidas 9,5 mm para cima; a ponta arredondada não mudou). Sobra uma ponte sólida de
  14,2 mm até o topo do corpo, escondida atrás do balão.
- **Marcador 2:** com a redução, os traços da palavra "anima" cairiam para ~0,75 mm; foram
  engrossados 0,2 mm (invisível a olho) e ficam em ~1,1 mm — duas a três linhas do bico 0,4.
- Como barras e letras são brancas iguais ao corpo, elas não são peças: são **vazios no verde**
  por onde o corpo aparece. Duas cores bastam.

## Arquivos

| Arquivo | Uso |
|---|---|
| `Marcadores-Anima-A1-2cores.3mf` | **Projeto do Bambu Studio** — os dois marcadores numa mesa, filamentos, processo e torre de purga definidos |
| `Marcador1-1-corpo-branco.stl` · `Marcador1-2-balao-verde.stl` | peças soltas, alinhadas entre si |
| `Marcador2-1-corpo-branco.stl` · `Marcador2-2-balao-verde.stl` | idem |

## Ajustes sobre o perfil *0.20mm Standard @BBL A1* (máxima qualidade em placa fina)

| Ajuste | Valor | Porquê |
|---|---|---|
| Gerador de paredes | **Arachne** | resolve os traços de 1,1 mm das letras sem gap fill |
| Paredes | 3 | borda firme do clipe de 2 mm |
| Largura da parede externa | **0,38 mm** | contorno das cores mais fiel |
| Largura da 1ª camada | **0,42 mm** (padrão 0,50) | a 1ª camada é a face do logo: linha fina preserva o detalhe |
| Velocidade da 1ª camada | **30 mm/s** | fronteiras de cor limpas |
| Pé de elefante | **0,10 mm** | menos esmagamento = as cores não "vazam" na 1ª camada |
| Ironing | **topo** | o "topo" impresso é o verso do marcador — sai liso também |
| Fundo / topo | 4 / 5 camadas | a peça de 10 camadas sai sólida |
| Torre de purga | 35 mm, em (208, 110) | fora das peças, 15 mm de folga; só 3 camadas de altura |

## No Bambu Studio

Abra o `.3mf`. Filamento 1 = PLA branco, filamento 2 = PLA verde: mapeie para os slots do AMS
lite. Fatie e envie. Se o Bambu perguntar sobre o preset modificado, mantenha o do projeto.

## Validação

Perfis reais do Bambu Studio 2.8 instalado. O projeto foi **fatiado pela linha de comando do
Bambu Studio** num gêmeo de um filamento (a CLI não fatia 2 filamentos na A1 — limitação dela,
não do arquivo): 2 objetos de 40,0 × 190,0 × 2,0 mm, apoiados em z = 0, 10 camadas, 109 min,
29,6 g, todos os ajustes conferidos no bloco de configuração do G-code. A troca de cor em si
fica para você conferir no preview antes de imprimir.
