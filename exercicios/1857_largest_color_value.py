"""
Solução para o problema "Largest Color Value in a Directed Graph?" (LeetCode 1857)
Verifica se o grafo é um DAG e, se for, retorna o valor máximo da cor dentre os caminhos válidos.
"""

class Solution(object):
    """
    Utiliza ordenação topológica com fila dos graus dos vértices para encontrar o maior valor de cor em caminhos válidos.
    Retorna -1 se houver ciclo.
    """

    def largestPathValue(self, colors, edges):
        n = len(colors)
        from collections import deque

        # Construção do grafo
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Inicialização da fila
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        # Matriz de contagem de cores para cada vértice
        color_count = [[0] * 26 for _ in range(n)]

        # Inicialização de cada vértice com sua própria cor
        for i in range(n):
            color_idx = ord(colors[i]) - ord("a")
            color_count[i][color_idx] = 1

        processed_nodes = 0
        max_color_value = 0

        # Laço para processamento em ordem topológica
        while queue:
            current = queue.popleft()  # Remove o próximo vértice (FIFO)
            processed_nodes += 1

            # Laço para atualização do valor máximo da cor
            for c in range(26):
                max_color_value = max(max_color_value, color_count[current][c])

            # Laço para processar todos os vizinhos
            for neighbor in graph[current]:
                neighbor_color_idx = ord(colors[neighbor]) - ord("a")
                # Laço para atualizar os contadores de cores 
                for c in range(26):
                    if c == neighbor_color_idx:
                        color_count[neighbor][c] = max(color_count[neighbor][c], color_count[current][c] + 1)
                    else:
                        color_count[neighbor][c] = max(color_count[neighbor][c], color_count[current][c])

                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Verificação de ciclo se não tiver processado todos os vértices
        if processed_nodes != n:
            return -1

        return max_color_value