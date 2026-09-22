# Creality Hi no Bambu Studio

Os cinco presets desta pasta já foram instalados nas pastas de usuário do Bambu Studio
(`%APPDATA%\BambuStudio\user\default` e `...\user\721047249`). Basta **reiniciar o Bambu Studio**:
a impressora "Creality Hi 0.4 nozzle" aparece na lista de impressoras (aba Preparar → Impressora),
com os processos "0.20mm Standard @Creality Hi 0.4 nozzle" e "Tea Holder - PLA branco @Creality Hi
0.4 nozzle" e os filamentos "Generic PLA @Creality Hi 0.4 nozzle" e "Hyper PLA @Creality Hi 0.4 nozzle".

Se por algum motivo não aparecerem: Arquivo → Importar → Importar configurações, e selecione os
`.json` desta pasta (máquina primeiro, depois processos e filamentos).

## Como foi feito

O Bambu Studio não tem a Creality Hi no pacote de fabricantes (18 modelos Creality, o mais novo é
o K1C) e a pasta de programa não permite gravação. Por isso a Hi entra como preset de usuário que
**herda do "Creality K1 Max 0.4 nozzle"** (Klipper, CoreXY, mesmas macros START_PRINT/END_PRINT)
e sobrescreve tudo que é da Hi, copiado dos perfis oficiais do Creality Print 7.2:

- mesa 260 × 260 × 300 mm, bico 0,4, estrutura CoreXY, G-code Klipper
- limites: 300 mm/s, aceleração 12.000 (20.000 em deslocamento), jerk 12, Z 20 mm/s
- retração 0,8 mm a 40 mm/s, z-hop 0,4, wipe ligado, retração ao trocar de camada
- G-code de início/fim/troca de camada/pausa/troca de filamento da Hi, na íntegra
- processo 0,20 mm da Hi (velocidades, acelerações, larguras de linha) e o processo do Tea Holder
- Generic PLA (220/60 °C, ventoinha 100%, fluxo 0,98, 12 mm³/s) e Hyper PLA (fluxo 0,97, 23 mm³/s)
- envio pela rede: host `http://192.168.100.142:7125/` (Moonraker, compatível com OctoPrint)

Por herdar do K1 Max, a etiqueta de **modelo** que o Bambu mostra é "Creality K1 Max"; a
impressora, o processo e os filamentos levam o nome "Creality Hi" e os valores são da Hi.

Os G-codes de filamento do Creality Print usam sintaxe que o interpretador do Bambu não aceita;
ficaram os da base do Bambu (só M104/M140 padrão). Nada muda no resultado.

## Validação

Os presets, achatados, fatiaram o Tea Holder pela linha de comando do Bambu Studio: 413 camadas,
9h35m, 348,5 g, START_PRINT a 220/60 °C, limites e ajustes conferidos no bloco de configuração
do G-code. (A estimativa do Bambu é um pouco mais alta que a do Creality Print — 9h18m — porque
os dois estimam tempo de forma diferente; o G-code para a impressão real é o do Creality Print.)
