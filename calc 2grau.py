###################################################################################
#Calculadora de Equação do Segundo Grau
#Vinícius Rabello Rodrigues
#DRE:119056899
#Curso: Matemática Aplicada
###################################################################################

import cmath

print('\no programa irá calcular as raizes de uma equação do segundo grau\n(ax**2 + bx + c = 0)com os coeficientes (a, b, c) escolhidos pelo usuário')
a = float(input('\ninsira a: '))
b = float(input('\ninsira b: '))
c = float(input('\ninsira c: '))

if a != 0:

    d = (b**2) - (4*a*c)
    x1 = (-b - cmath.sqrt(d))/(2*a)
    x2 = (-b + cmath.sqrt(d))/(2*a)

    if d > 0:

        print('a equação possui tais raízes reais e distintas:')
        print('x1 = {}'.format(x1))
        print('x2 = {}'.format(x2))

    if d == 0:

        print('a equação possui tais raízes reais e iguais:')
        print('x1 = {}'.format(x1))
        print('x2 = {}'.format(x2))

    if d < 0:

        print('a equação possui tais raízes complexas e distintas:')
        print('x1 = {}'.format(x1))
        print('x2 = {}'.format(x2))

else:

    print('\na não pode ser igual à zero')



