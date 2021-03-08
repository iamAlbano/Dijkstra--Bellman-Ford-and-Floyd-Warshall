from random import randint, randrange

# This function works properly but it has a high cost

def grafoAleatorio(numVert, numArestas, pesoMin, pesoMax):

    grafo = []
    i = 0
    j = 0

    maxArestas = (numVert*(numVert-1))

    if numArestas > maxArestas:
        print("Não foi possivel gerar o grafo!")
        print("O número de arestas especifícado excede o limite para a quantidade de vértices informado")
        return

    while i < numVert:
        grafo.append([])
        i += 1
    i = 0

    while i < numVert:
        j = 0
        while j < numVert:
            if j != i:
                grafo[i].append((j,randint(pesoMin, pesoMax)))
            j += 1
        i += 1

    remover = maxArestas - numArestas   #quantidade de arestas a serem removidas
    i = 0

    while i < remover:

        vert = randint(0, -1 + numVert)
        aresta = randint(0, -1 + numVert)

        try:
            del(grafo[vert][aresta])
            i +=1
        except:
            continue


    return grafo




# The code below has a better cost but it doesn't  make the nodes in a correct sequence


def gerarGrafo(numArestas, numVert, pesoMin, pesoMax):

    i = 0
    j = 0
    grafo = []
    arestasDisponiveis = numArestas

    while i < numVert:

        grafo.append([])

        if i == numVert-1:
            totalArestas = arestasDisponiveis
        else:
            totalArestas = randint(0, -1 + numVert)  #total de arestas do vértice atual
            arestasDisponiveis -= totalArestas

        auxVert = [i]

        while j < totalArestas:

            while True:


                vertAtual = randint(0, numVert-1)  #gera um vertice aleatório para interligar ao atual

                if len(auxVert) == numVert:
                    break

                if vertAtual not in auxVert: #apenas sai do laço se o vertice aleatório for diferente do vertice atual
                    break
            auxVert.append(vertAtual)

            grafo[i].append((vertAtual, randint(pesoMin, pesoMax)))
            sorted(grafo[i])

            j += 1

        auxVert.clear()
        i += 1
        j = 0


    return grafo





