lista = [1, 2, 3, 4, 5]

def triplica_itens(iterable):
    lista_aux = []

    for x in iterable:
        lista_aux.append(x*3)
    return lista_aux


def main():
    print(triplica_itens(lista))

if __name__ == '__main__':
    main()
