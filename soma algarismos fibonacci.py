###################################################################################
#Soma dos Algarismos �mpares de Fibonacci
#Vin�cius Rabello Rodrigues
#DRE:119056899
#Curso: Matem�tica Aplicada
###################################################################################

n = input()
x = 1
y = 2
s = 0

while True: 

    if x % 2 != 0:
        s += x
    if y % 2 != 0:
        s += y
    x = x + y
    y = y + x
    if x > n or y > n:
        break

print(s)
        
