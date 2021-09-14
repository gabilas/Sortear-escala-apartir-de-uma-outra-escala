# Sortear-escala-apartir-de-uma-outra-escala
Programa criado para a @Energisa SE, para criar uma escala de apresentação do DDS (Diálogo Diário de Segurança) baseado na escala de horário de seus colaboradores.

## To Do

- [X] Receber a escala de horários dos colaboradores a partir de um arquivo txt;
- [X] Escrever e salvar a escala do DDS em um outro arquivo txt;
- [X] Executável do programa.

## Instruções de uso

- Instalar o python 3 ou baixar o Executável (Encontra-se na pasta 'dist');
- Ter um arquivo txt com nome 'ESCALA_COD';
- No txt com a escala dos colaboradores inserir os seguintes dados (e tendo um espaço vazio entre eles):
   * A quantidade de dias no mês;
   * Os colaboradores no turno da manha (separados por '|');
   * Os colaboradores no turno da tarde (separados por '|');
   * Os colaboradores no turno da noite (separados por '|');
- Ter um outro arquivo txt com nome 'ESCALA_DDS';
- Aguardar o programa montar a escala, quando toda escala tiver sido montada, o arquivo será salvo e o programa encerrado.



**Exemplo:**

- Entrada 'ESCALA_COD'

=====================================================================================
```
30

DP6XA1|DP6XA1|DCO3AR|3CORU|ZC9UR|ZPF9A8|4PF5A8|4PDEA8|ETKDA1|DTKXA1|DTX1V|DCOR3|3COUAR|ZC93AR|ZPFS98|4PF5S8|4PS5A8|ETK15|ETK1X|ETKXA1|VCO3AR|3COUAR|ZC9UAR|ZSF9A8|4FS85|EFP85|ETKQ61|QTK6A1|VTK6A1|VCO3AR

4TF5E8|ETFVB8|VTLXB1|VTK1X|VKO13|3COUBR|ZCU9BR|ZCF9BR|4PF5S8|4PF5E8|EPK8F|VTK1X|VTX6Q1|VTOQB1|3COQBR|ZCU9QR|ZC9QBR|4FP8S|6PF85|QKPF68|QTKX61|VTKQB1|VTKO31|3OUVR|ZC9RU|ZCSR9|4PF5S8|4PF5E8|EPFQB8|QTK6B1

ZS9|4S5|4E5|DE6|DXT|VX6|V3O|U3O|ZU9|ZS9|4S5|4E5|DKE|6KX|VX6|V3O|U3O|ZU9|ZS9|4S5|4E5|EX6|Q6X|QX6|V3O|U3O|ZU9|ZS9|4S5|4E5
```
=====================================================================================

- Saída 'ESCALA_DDS'

=====================================================================================
```
Data: 1
Operador da manhã: RUBENS
Operador da tarde: LUCAS
Operador da noite: ANDRÉ

=======================================

Data: 2
Operador da manhã: NEILSON
Operador da tarde: MACIEL
Operador da noite: DANIEL

=======================================

Data: 3
Operador da manhã: SAMUEL
Operador da tarde: ORLEAN
Operador da noite: ADISSON

=======================================

Data: 4
Operador da manhã: MARCO ANTONIO
Operador da tarde: CRISTIAN
Operador da noite: MACIEL

=======================================

Data: 5
Operador da manhã: RONALD
Operador da tarde: CRISTIAN
Operador da noite: JOÃO PAULO

=======================================

Data: 6
Operador da manhã: FÁBIO
Operador da tarde: AISLAN
Operador da noite: NEILSON

=======================================

Data: 7
Operador da manhã: ADISSON
Operador da tarde: JANISON
Operador da noite: ROBSON

=======================================

Data: 8
Operador da manhã: DANIEL
Operador da tarde: AISLAN
Operador da noite: CESAR

=======================================

Data: 9
Operador da manhã: BRUNO DIAS
Operador da tarde: GABRIEL
Operador da noite: JANISON

=======================================

Data: 10
Operador da manhã: SAMUEL
Operador da tarde: DANIEL
Operador da noite: RONALD

=======================================

Data: 11
Operador da manhã: NEILSON
Operador da tarde: CRISTIAN
Operador da noite: ANDRÉ

=======================================

Data: 12
Operador da manhã: BRUNO DIAS
Operador da tarde: NEILSON
Operador da noite: DANIEL

=======================================

Data: 13
Operador da manhã: REGIVAN
Operador da tarde: NEILSON
Operador da noite: MACIEL

=======================================

Data: 14
Operador da manhã: RONALD
Operador da tarde: SÉRGIO
Operador da noite: RUBENS

=======================================

Data: 15
Operador da manhã: FÁBIO
Operador da tarde: CESAR
Operador da noite: RUBENS

=======================================

Data: 16
Operador da manhã: GABRIEL
Operador da tarde: REGIVAN
Operador da noite: CESAR

=======================================

Data: 17
Operador da manhã: ADISSON
Operador da tarde: RONALD
Operador da noite: ROBSON

=======================================

Data: 18
Operador da manhã: MACIEL
Operador da tarde: GABRIEL
Operador da noite: RONALD

=======================================

Data: 19
Operador da manhã: CRISTIAN
Operador da tarde: LUCAS
Operador da noite: JANISON

=======================================

Data: 20
Operador da manhã: ORLEAN
Operador da tarde: GABRIEL
Operador da noite: ANDRÉ

=======================================

Data: 21
Operador da manhã: EVERTON
Operador da tarde: JOÃO PAULO
Operador da noite: DANIEL

=======================================

Data: 22
Operador da manhã: ROBSON
Operador da tarde: ORLEAN
Operador da noite: NEILSON

=======================================

Data: 23
Operador da manhã: MARCO ANTONIO
Operador da tarde: JOÃO PAULO
Operador da noite: NEILSON

=======================================

Data: 24
Operador da manhã: SAMUEL
Operador da tarde: REGIVAN
Operador da noite: SÉRGIO

=======================================

Data: 25
Operador da manhã: LUCAS
Operador da tarde: REGIVAN
Operador da noite: CESAR

=======================================

Data: 26
Operador da manhã: ADISSON
Operador da tarde: MARCO ANTONIO
Operador da noite: REGIVAN

=======================================

Data: 27
Operador da manhã: CRISTIAN
Operador da tarde: LUCAS
Operador da noite: REGIVAN

=======================================

Data: 28
Operador da manhã: SÉRGIO
Operador da tarde: MACIEL
Operador da noite: RONALD

=======================================

Data: 29
Operador da manhã: SAMUEL
Operador da tarde: FÁBIO
Operador da noite: ADISSON

=======================================

Data: 30
Operador da manhã: ROBSON
Operador da tarde: SÉRGIO
Operador da noite: DANIEL

=======================================
```
=====================================================================================

