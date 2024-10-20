# exemplo partial
import collections
import operator
from functools import partial
adiciona_um = partial(operator.add,1)

print(adiciona_um(5))

#segundo exemplo partial
print('\nSegundo exemplo')
import collections
from operator import  attrgetter
#tuple recebe uma lista como parâmetros
pessoa = collections.namedtuple('pessoa', 'nome idade')
pessoas = [pessoa('João', 40), pessoa('Ana', 20), pessoa('Renata', 25)]

#attrgetter especifíca por ordem você está ordenando
print(sorted(pessoas, key=attrgetter('nome')))
print(sorted(pessoas, key=attrgetter('idade')))

#terceiro exemplo
print('\nTerceiro exemplo')
from functools import partial
sort_nome = partial(sorted,key=attrgetter('nome'))
sort_idade = partial(sorted, key=attrgetter('idade'))

print(sort_nome(pessoas))
print(sort_idade(pessoas))