Descrição
Você está desenvolvendo um sistema que integra com uma API de dados transacionais, onde as datas são fornecidas no formato "DD-MM-YYYY". Sua tarefa é processar essa lista de datas e transformá-las para o formato internacional "YYYY/MM/DD".

Entrada
A entrada deve receber uma string contendo datas separadas por ponto e vírgula: "DD-MM-YYYY;DD-MM-YYYY;...". Cada data é uma string.

Saída
Deverá retornar uma lista de strings contendo as datas no formato "YYYY/MM/DD".

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
01-01-2020;02-02-2021	['2020/01/01', '2021/02/02']
15-05-1999;23-11-2003	['1999/05/15', '2003/11/23']
31-12-2022	['2022/12/31']
