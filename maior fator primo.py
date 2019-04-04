###################################################################################
#Maior Fator Primo de N
#Vinícius Rabello Rodrigues
#DRE:119056899
#Curso: Matemática Aplicada
###################################################################################

import math

print('Use a Função MaiorFatorPrimo(n), para que o programa calcule o maior fator primo de n')

def MaiorFatorPrimo(n):

    MaiorPrimo = -1
    while n % 2 == 0:
        MaiorPrimo = 2
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            MaiorPrimo = i
            n = n/i

    if n > 2:
        MaiorPrimo = n

    return int(MaiorPrimo)
