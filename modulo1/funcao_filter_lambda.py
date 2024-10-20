lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 !=1, lista)

print(list(nova_lista))
