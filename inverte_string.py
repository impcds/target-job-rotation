"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

frase = input('Digite uma frase: ')

saida = ''

for letra in range(1, len(frase) + 1):

    saida += frase[-letra]


print(saida)