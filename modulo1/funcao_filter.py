#É utilizada para filtrar elementos de um iterável (lista, tupla, dicionários etc.). O filtro é realizado utilizando uma função, que deve ser capaz de retornar true ou false (verdadeiro ou falso) para cada elemento do iterável.
#Todo elemento que for avaliado como true será incluído em um novo iterável retornado pela função filter,
# que é pura e de alta ordem, pois depende apenas dos parâmetros e recebe uma função como parâmetro. A sua sintaxe é a seguinte:

#filter(função, iterável)


# script funcao_filter.py
lista = [1, 2, 3, 4, 5]


def impar(item):
    return item % 2 != 0


def main():
    nova_lista = filter(impar, lista)
    print(list(nova_lista))


if __name__ == "__main__":
    main()