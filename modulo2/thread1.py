import threading 
import time

def funcao():
    for i in range(3):
        print(i,'Executando a thread')
        time.sleep(1)

print('iniciando o programa\n')
t = threading.Thread(target=funcao).start()
print('\nFinalizando o programa!')