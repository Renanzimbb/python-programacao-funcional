#Alguns metodos para somar valores com programacao Python Programacao Funcional(nao altera lista original)


#sem alterar variável total como o funcional3
def sum(numeros):
    if not numeros:
        return 0
    primeiro = numeros[0]
    resto = numeros[1:]
    return primeiro + sum(resto)

print(sum([2,4,6,8,10]))

#segundo exemplo
print('\nSegundo exemplo:')
lista = ['Ferrari']
nova_lista = lista + ['Porsche']
print(nova_lista)

#terceiro exemplo
#operator(biblioteca) é interessante para exemplificar algums funções, operações em python
#ajuda quando você usa lista como parâmetros
print('\nTerceiro exemplo:')
import operator
#função operator.add que soma valores
print(operator.add(10,20))

#quarto  exemplo
print('\nQuarto exemplo')
from functools import reduce
#reduc(function, list)
#reduce recebe função e lista
print(reduce(operator.add,[10,20]))
print(reduce(operator.concat,['Aprendendo reduce!']))