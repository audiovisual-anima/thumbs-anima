# Tea Holder — revisão de parâmetros para Creality Hi Combo, PLA branco

Arquivo de origem: `POINY POINYD.3mf` — projeto do **Bambu Studio 1.10** configurado para
**Bambu Lab A1**. Nada nele servia à Creality Hi sem revisão: impressora, mesa, velocidades,
retração, G-code de início/fim e perfil de filamento eram todos da A1.

## O que é a peça

Caixa "BOX" de **222,2 × 111,1 × 82,5 mm**, 6 compartimentos iguais de 69,8 × 50,8 mm em grade
3 × 2. Malha estanque, 8.226 triângulos. Medidas que decidiram os parâmetros:

| | |
|---|---|
| Paredes (externas e divisórias) | **3,2 mm** — uniformes |
| Fundo | **6,4 mm** maciço |
| Base de contato com a mesa | 246 cm² |
| Balanços acima de 45° | 0,4 cm² (nada) · sem tetos internos · sem pontes |
| Orientação | como veio: boca para cima, fundo na mesa |

Conclusão: **sem suporte**, sem brim, e as paredes de 3,2 mm podem sair **maciças** só com
voltas de parede, sem preenchimento dentro delas.

## Arquivos

| Arquivo | Uso |
|---|---|
| `Tea-Holder-Creality-Hi-PLA-branco.3mf` | **Projeto do Creality Print** — abrir, conferir, fatiar, enviar |
| `Tea-Holder-Creality-Hi-PLA-branco.gcode` | **Já fatiado pelo Creality Print 7.2** com este projeto — pode ir direto para a Hi (USB ou envio pelo app) |
| `Tea-Holder-limpo.stl` | geometria limpa, centrada, apoiada em z = 0 |
| `preset-processo-Tea-Holder-Creality-Hi.json` | o preset de processo, para importar no Creality Print se quiser reaproveitar em outra peça |

## Parâmetros: original → ajustado

| Parâmetro | Original (Bambu A1) | Creality Hi, PLA branco | Por quê |
|---|---|---|---|
| Impressora | Bambu Lab A1 0.4 | **Creality Hi 0.4 nozzle** | perfil de sistema do Creality Print 7.2 (260 × 260 × 300, Klipper, z-hop 0,4, retração 0,8) |
| Processo | 0.20mm Standard @BBL A1 | **0.20mm Standard @Creality Hi 0.4** + ajustes abaixo | velocidades, acelerações e sequência da Hi |
| Filamento | Generic PLA @BBL A1 | **Generic PLA @Creality Hi 0.4** — 220 °C / mesa 60 °C / ventoinha 100% / fluxo 0,98 / 12 mm³/s | perfil conservador, seguro para qualquer PLA branco |
| Mesa | Textured PEI Plate (65 °C) | **Textured PEI Plate (60 °C)** | chapa PEI texturizada da Hi |
| Camada | 0,20 mm | **0,20 mm** | 413 camadas; boa relação acabamento/tempo |
| Paredes | 2 | **4, gerador Arachne** | 3,2 mm ÷ 0,42 = 7,6 linhas: o Arachne ajusta a largura e fecha a parede maciça, sem gap fill; o clássico deixaria uma fresta |
| Camadas de fundo / topo | 3 / 5 | **4 / 5** | fundo de 6,4 mm firme embaixo; topo fecha os pisos dos compartimentos |
| Preenchimento | 15% gyroid | **20% grade** | só existe dentro do fundo; grade é mais rígida no plano |
| Ironing | não | **top** (30 mm/s, 10%, 0,15) | piso dos 6 compartimentos e a borda saem alisados — é o que se vê ao abrir |
| Brim | automático | **nenhum** + **saia de 1 volta** a 3 mm | 246 cm² em PEI a 60 °C, impressora fechada: adesão sobra; brim só marcaria a borda. A saia escorva o bico |
| Costura | alinhada | **alinhada** | fica sempre no mesmo canto da caixa |
| Suporte | não | **não** | não há balanço |
| Pé de elefante | 0,075 | **0,15** | valor do perfil da Hi; compensa o esmagamento da 1ª camada numa base de 222 mm |
| Parede externa precisa | — | **sim** | contorno externo com fluxo compensado, arestas mais fiéis |
| Ventoinha | 80% máx | **100%** | perfil de PLA da Hi; PLA branco aceita bem resfriamento total |
| Cor | branco | **branco (#FFFFFF)** | |

Resultado no fatiador: **413 camadas · 9h 18m · 345 g de PLA** (~R$ 38 de filamento a R$ 110/kg).

## Como usar

**Caminho 1 — abrir no Creality Print (recomendado):** abra o `.3mf`. Se o Creality Print
perguntar, confirme impressora *Creality Hi 0.4 nozzle*, filamento *Generic PLA* e mesa
*Textured PEI Plate*. Fatie e envie. Se o seu PLA branco for **Creality Hyper PLA**, troque o
filamento para *Hyper PLA @Creality Hi 0.4 nozzle*: mesmas temperaturas, mas ele permite 23 mm³/s
e a impressão cai para perto de 6 h.

**Caminho 2 — G-code direto:** o `.gcode` já foi gerado pelo Creality Print 7.2 a partir deste
projeto. Copie para o pendrive ou envie pelo app. É a rota mais segura: nada é recalculado.

Antes de imprimir: chapa limpa com álcool isopropílico (base grande, PLA branco marca dedo),
CFS com PLA branco no slot 1, e nivelamento automático da Hi ativo.

## Já na impressora

O G-code foi enviado à Creality Hi (`192.168.100.142`, hostname `Creality Hi-6701`) pela API
Moonraker (porta 7125) — 11.965.245 bytes, íntegro. A impressão **não foi iniciada**: no momento
do envio o CFS constava como desconectado e o sensor do caminho direto detectava um filamento.
Confira que é o PLA branco e inicie pela tela da impressora ou pelo Fluidd (`:4408`).

## Creality Hi no Bambu Studio

Cinco presets de usuário instalados na pasta de usuário do Bambu Studio (`AppData\Roaming\BambuStudio\user`,
pasta `default` e a da sua conta): impressora *Creality Hi 0.4 nozzle*, processos *0.20mm Standard* e
*Tea Holder – PLA branco*, filamentos *Generic PLA* e *Hyper PLA*, todos `@Creality Hi 0.4 nozzle`.
Reinicie o Bambu Studio. Detalhes e cópia dos arquivos em `Bambu-Studio-presets/`.

## Validação

- Perfis lidos do próprio Creality Print 7.2 instalado (`resources/profiles/Creality`), com a
  herança resolvida — são os mesmos que o programa usa.
- O projeto `.3mf` foi **aberto e fatiado pela linha de comando do Creality Print 7.2**: passou
  na checagem de versão, aplicou todos os parâmetros (conferidos no bloco de configuração do
  G-code: 4 paredes Arachne, ironing presente, saia presente, brim ausente, branco, 220/60 °C,
  mesa PEI texturizada) e gerou os 413 layers.
- O G-code entregue é exatamente o que essa fatiação produziu.

## Se quiser mais acabamento

Camada de **0,16 mm** (perfil *0.16mm Standard @Creality Hi 0.4*) suaviza as linhas nas
paredes de 82 mm ao custo de ~25% a mais de tempo (~11h40). Basta trocar o processo no
Creality Print e manter os mesmos ajustes — o preset `.json` da pasta serve de base.
