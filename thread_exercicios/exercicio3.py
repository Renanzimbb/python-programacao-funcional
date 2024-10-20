import time
from threading import Thread

def calcular_cubo (numero, tempo_espera):
    print(f'Iniciando calculo do cubo de {numero}')
    time.sleep(tempo_espera)
    print(f"O Cubo de {numero} é {numero * 3}")

def calcular_quadrado (numero,tempo_espera):
    print(f'Iniciando calculo do quadrado de {numero}')
    time.sleep(tempo_espera)
    print(f"O quadrado de {numero} é {numero * 2}")


t1 = Thread(target=calcular_cubo,args=(5,3))
t2 = Thread(target=calcular_quadrado, args=(5,2))
t1.start()
t2.start()

t1.join()
t2.join()

print('Execução foi concluída')