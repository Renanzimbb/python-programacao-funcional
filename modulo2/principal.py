from threading import Thread
from multiprocessing import Process

def funcao_a(name):
    print(name)

def main():
    t = Thread(target=funcao_a, args=("Minha Thred",))
    t.start()

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()
if __name__ == '__main__':
    main()

    

