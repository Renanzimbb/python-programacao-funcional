#A função map é utilizada para aplicar uma determinada função em cada elemento de um iterável (lista, tupla, dicionários etc.), retornando um novo iterável com os valores modificados.
#A função map é pura e de ordem superior, pois depende apenas de seus parâmetros e recebe uma função como parâmetro. A sua sintaxe é a seguinte:
#map(função, iterável1, iterável2...)

lista = [1, 2 , 3]

def triplica(item):
    return item * 3

def main():
    nova_lista = map(lambda item: item*3, lista)
   # print(list(nova_lista))

x = lambda a,b: a+[a[-1]+a[-2]+b]
y=[-1,0]
for i in range(7):
    y = x(y,i)
    print(y)

if __name__ == '__main__':
    main()