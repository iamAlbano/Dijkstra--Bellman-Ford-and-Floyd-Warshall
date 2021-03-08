from dijkstra import dijkstra, buscaMenor
from grafo import gerarGrafo, grafoAleatorio
from bellmanford import bellmanFord
from floydwarshall import floydWarshall
import timeit


if __name__ == '__main__':


     grafo1 = [[(1, 6), (2, 2)], [(2, 3), (3, 1), (4, 3)], [(1, 2), (3, 5)], [(4, 3)], []]
     grafo2 = [[(2,8),(1,5)],[(2,7),(3,7)],[(0,5),(3,9),(4,7)],[(1,6),(4,5)],[(2,5)]]
     grafo3 = [[(1,6),(2,2)], [(2,3),(3,1),(4,3)],[(1,2),(3,5)],[(4,3)],[]]
     grafo4 = [[(1,6),(2,2)],[(0,3),(2,7),(3,5)],[(1,2),(3,1)],[(2,4)]]
     grafo5 = [[(1,-1),(2,6)],[(2,4)],[(0,5),(1,3)]]

     grafo = grafoAleatorio(1000, 500000, 1, 5)

     print(grafo, "\n")

     inicio = timeit.default_timer()
     a, b = dijkstra(grafo, 0)
     fim = timeit.default_timer()



     print(a)
     print(b)

     print('Time of execution: %.3f ' % (fim - inicio))





















