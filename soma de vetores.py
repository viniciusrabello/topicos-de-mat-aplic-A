###################################################################################
#Soma de Vetores de N Coordenadas
#Vinicius Rabello Rodrigues
#DRE:119056899
#Curso: Matematica Aplicada
###################################################################################




print('o programa ira somar dois vetores, v1 e v2, onde: ')
print('v1 = (x1, x2, x3,..., xn) e v2 = (y1 y2, y3,..., yn)')
print('e vetor3 = (x1 + y1, x2 + y2, x3 + y3,..., xn + yn)')

n = int(input('insira o numero de dimensoes dos seus vetores: '))
numdim = n
i = 1
o = 1
vetor1 = []
vetor2 = []
vetor3 = []

while len(vetor1) < numdim:
    cord = int(input('insira x{}: '.format(i)))
    vetor1.append(cord)
    i += 1

while len(vetor2) < numdim:
    cord = int(input('insira y{}: '.format(o)))
    vetor2.append(cord)
    o += 1

if len(vetor1) and len(vetor2) == numdim:
    print('vetor1 = {}'.format(vetor1))
    print('vetor2 = {}'.format(vetor2))

vetor3 = [vetor1[p] + vetor2[p] for p in range (numdim)]
print('vetor3 = {}'.format(vetor3))

