lista = [1, 2, 3, 4, 5]

nova_lista = map(lambda item: item * 3, lista)

def main():
    print(list(nova_lista))

if __name__ == "__main__":
    main()