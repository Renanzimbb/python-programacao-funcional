import time
from threading import Thread

def funcao(tempo_espera, nome_tarefa):
    print(f"Iniciando a tarefa {nome_tarefa}")
    time.sleep(tempo_espera)
    print(f"Concluindo a tarefa {nome_tarefa}")

thread = Thread(target=funcao, args=(3,'A'))
thread2 = Thread(target=funcao, args=(2, 'B'))
thread.start()
thread2.start()

print('\nAguardando a execução das threads')
thread.join()
thread2.join()
print('A execução foi concluída')