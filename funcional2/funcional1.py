# como fazer - imperativo
numeros = [1, 2 ,3, 4, 5]
total = 0

for numero in numeros:
    total += numero
print('O total é ', total)

#segundo exemplo

print('\nsegundo exemplo')
if True:
    print('Tudo certo')
else:
    print('ops')


frutas = ['banana', 'maça', 'pera', 'morango', 'uva','tamarindo']

for c in range(-1,-5,-2):
    print(frutas[c])
print()

for c in range(len(frutas)):
    print(frutas[c])

print()
nome = {'Nome': 'Renan',
        'Idade': 34,
        'Escolaridade': 'Superior Incompleto',
        'Sexo': 'Masculino'}


for chave, valor in nome.items():
    print(f'{chave}: {valor}')

def numeros(*numeros):
    print(numeros)

numeros(11,22,33,44,55)

numeros2 = [11,22,44,55,66]

def desempacotar(a,b,c,d,e):
    print(a, b, c, d, e)
desempacotar(*numeros2)

y = 'RL Sites'
print('.'.join(y))

nomes = ['renan', 'joao', 'pedro', 'carlos']

for x in nomes:
    print(x)