'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação 
que cada estado teve dentro do valor total mensal da distribuidora.'''

class Estado():
    total = 0
    def __init__(self, uf, valor):
        self.uf = uf
        self.valor = valor
        Estado.total += valor
    

    def __str__(self):
        return f'{self.uf.upper()}: {self.valor / Estado.total * 100:.2f}%'
    
sp = Estado('sp', 67836.43)
rj = Estado('rj', 36678.66)
mg = Estado('mg', 29229.88)
es = Estado('es', 27165.48)
outros = Estado('outros', 19879.53)


print(sp)
print(rj)
print(mg)
print(es)
print(outros)