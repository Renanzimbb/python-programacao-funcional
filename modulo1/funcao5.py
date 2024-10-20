def mutiplica_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador
    return multi

multiplicar_por_10 = mutiplica_por(10)

print((multiplicar_por_10(1)))
print((multiplicar_por_10(2)))


multiplicar_por_10 = mutiplica_por(5)

print((multiplicar_por_10(1)))
print((multiplicar_por_10(2)))
