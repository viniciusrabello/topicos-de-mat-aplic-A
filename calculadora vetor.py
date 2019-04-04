while True:

    m = 0

    if m == 0:
        print('\nMenu de Opções')
        print('\n1-Soma de Dois Vetores(w = v + u)')
        print('\n2-Subtração de Dois Vetores(w = v - u)')
        print('\n3-Sair do Programa')
        m = int(input('\nDigite o número da opção desejada: '))


    if m == 1:

        print('\no programa ira somar dois vetores, v1 e v2, onde: ')
        print('\nv1 = (x1, x2, x3,..., xn) e v2 = (y1 y2, y3,..., yn)')
        print('\ne vetor3 = (x1 + y1, x2 + y2, x3 + y3,..., xn + yn)')

        n = int(input('\ninsira o numero de dimensoes dos seus vetores: '))
        numdim = n
        i = 1
        o = 1
        vetor1 = []
        vetor2 = []
        vetor3 = []

        while len(vetor1) < numdim:
            cord = int(input('\ninsira x{}: '.format(i)))
            vetor1.append(cord)
            i += 1

        while len(vetor2) < numdim:
            cord = int(input('\ninsira y{}: '.format(o)))
            vetor2.append(cord)
            o += 1

        if len(vetor1) and len(vetor2) == numdim:
            print('\nvetor1 = {}'.format(vetor1))
            print('\nvetor2 = {}'.format(vetor2))

        vetor3 = [vetor1[p] + vetor2[p] for p in range (numdim)]
        print('\nvetor3 = {}'.format(vetor3))
        m = 0

    if m == 2:

        print('\no programa ira subtrair dois vetores, v1 e v2, onde: ')
        print('\nv1 = (x1, x2, x3,..., xn) e v2 = (y1 y2, y3,..., yn)')
        print('\ne vetor3 = (x1 - y1, x2 - y2, x3 - y3,..., xn - yn)')

        n = int(input('\ninsira o numero de dimensoes dos seus vetores: '))
        numdim = n
        i = 1
        o = 1
        vetor1 = []
        vetor2 = []
        vetor3 = []

        while len(vetor1) < numdim:
            cord = int(input('\ninsira x{}: '.format(i)))
            vetor1.append(cord)
            i += 1

        while len(vetor2) < numdim:
            cord = int(input('\ninsira y{}: '.format(o)))
            vetor2.append(cord)
            o += 1

        if len(vetor1) and len(vetor2) == numdim:
            print('\nvetor1 = {}'.format(vetor1))
            print('\nvetor2 = {}'.format(vetor2))

        vetor3 = [vetor1[p] - vetor2[p] for p in range (numdim)]
        print('\nvetor3 = {}'.format(vetor3))
        m = 0
        

    if m == 3:
        exit()

    else:
        m = 0

        
