"""
Solução para o problema "Is Graph Bipartite?" (LeetCode 785)
Verifica se um grafo não direcionado é bipartido.
"""

class Solution(object):
    """
    Utiliza BFS com auxilio de um vetor de cores, marcando os dois conjuntos para determinar se o grafo é bipartido.
    """

    def isBipartite(self, grafo):
        n = len(grafo)
        color = [-1] * n
        from collections import deque

        # Laço para percorrer todos os vértices
        for i in range(n):
            if color[i] == -1:
                # Inicialização da BFS a partir do vértice i
                queue = deque([i])
                color[i] = 0
                while queue:
                    u = queue.popleft()  # Remove o próximo vértice (FIFO)
                    # Laço para verificar e colorir os vizinhos
                    for v in grafo[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False
        return True