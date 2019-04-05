###################################################################################
#Soma dos Múltiplos de X e Y
#Vinícius Rabello Rodrigues
#DRE:119056899
#Curso: Matemática Aplicada
###################################################################################

print('\no programa irá calcular a soma dos multiplos menores que n de x ou y\n(multiplos em comum só serão adicionados uma vez)')

x = int(input('\ninsira x: '))
y = int(input('\ninsira y: '))
n = int(input('\ninsira n: '))
lx = []
ly = []
l = []
s = 0
i = 0

while (i < n):
    if i % x == 0:
        lx.append(i)
    if i % y == 0:
        ly.append(i)
    if i % x == 0 and i % y == 0:
        l.append(i)
    i += 1

s = sum(lx) + sum (ly) - sum (l)
print(s)
        
