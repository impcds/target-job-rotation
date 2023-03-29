"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""

import json # biblioteca responsavel por ler o arquivo json


# lendo os dados do arquivo de texto e criando um objeto json
with open("dados.json", "r") as f:
    dados = json.load(f)

# declarando variaveis
maior = float('-inf')
menor = float('inf')
totalFaturado, diasComFaturamento, diasAcimaDaMedia = 0, 0, 0

# fazendo um laço pelos dados para achar o maior e o menor valor e fazer a soma total
for dado in dados:
    if dado['valor'] == 0:
        continue

    diasComFaturamento += 1
    totalFaturado += dado['valor']

    if dado['valor'] < menor:
        menor = dado['valor']
    elif dado['valor'] > maior:
        maior = dado['valor']

# calculo da media
media = totalFaturado / diasComFaturamento

# verificando quantos dias teve faturamento acima da media
for dado in dados:
    if dado['valor'] > media:
        diasAcimaDaMedia += 1

# printando o resultado
print(f'''
    O menor faturamento em um dia foi: {menor}
    O maior faturamento em um dia foi: {maior}
    Número de dias com faturamento acima da média: {diasAcimaDaMedia} 
''')

