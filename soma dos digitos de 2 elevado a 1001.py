###################################################################################
#Soma dos Dígitos de 2 elevado à 1001
#Vinícius Rabello Rodrigues
#DRE:119056899
#Curso: Matemática Aplicada
###################################################################################

print('o programa ir� calcular a soma dos digitos de n')
x = int(input('insira x, onde n = 2**x: '))
n = 2**x
ultimodigito = 0
s = 0

while n != 0:
    ultimodigito = n % 10
    s += ultimodigito
    n = int(n/10)

    if n == 0:
        print(s)
    
