valores = [10,20,30]

def altera_valores(lista):
    nova_lista = list(lista)
    nova_lista[1] = nova_lista[1] + 2
    return nova_lista

print("Nova lista: ", altera_valores(valores))
print("Nova lista: ", altera_valores(valores))