def mutiplica_por(multiplicador):
    return lambda multiplicando: multiplicando * multiplicador

multiplicar_por_10 = mutiplica_por(10)

print((multiplicar_por_10(1)))
print((multiplicar_por_10(2)))


multiplicar_por_10 = mutiplica_por(5)

print((multiplicar_por_10(1)))
print((multiplicar_por_10(2)))
