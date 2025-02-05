from Node import Node
import rich.console as console
import networkx as nx
import matplotlib.pyplot as plt

class BinarySearchTree:
    def __init__(self):
        
        # Inicializa a raiz da árvore como None (árvore vazia).
        self.root = None

        # Contadores para comparações, hits e misses.
        self.comparison_count = 0  # Conta o número de comparações durante inserções.
        self.hits = 0  # Conta o número de acertos durante buscas.
        self.misses = 0  # Conta o número de erros durante buscas.

    def insert(self, key):
        """
        Insere um novo nó com a chave fornecida na árvore.
        """
        
        new_node = Node(key) 
        parent = None  # Inicializa o nó pai como None.
        current = self.root  # Começa a busca pela raiz da árvore.

        # Encontra a posição correta para inserir o novo nó.
        while current is not None:
            parent = current  # Atualiza o nó pai para o nó atual.
            self.comparison_count += 1  # Incrementa o contador de comparações.

            # Decide se deve ir para a subárvore esquerda ou direita.
            if key < current.key:
                current = current.left  # Vai para a esquerda se a chave for menor.
            else:
                current = current.right  # Vai para a direita se a chave for maior ou igual.

        # Define o pai do novo nó.
        new_node.parent = parent

        # Se a árvore estava vazia, o novo nó é a raiz.
        if parent is None:
            self.root = new_node
        # Se a chave for menor que a chave do pai, insere à esquerda.
        elif key < parent.key:
            parent.left = new_node
        # Caso contrário, insere à direita.
        else:
            parent.right = new_node

    def search(self, key):
        """
        Busca um nó com a chave fornecida e retorna o número de comparações feitas.
        Incrementa os contadores de hits e misses.
        """
        current = self.root  # Começa a busca pela raiz da árvore.
        comparisons = 0  # Contador de comparações.

        # Percorre a árvore até encontrar o nó ou chegar a um nó folha.
        while current is not None:
            comparisons += 1  # Incrementa o contador de comparações.
            if key == current.key:
                self.hits += 1  # Incrementa o contador de acertos.
                return comparisons  # Retorna o número de comparações.
            elif key < current.key:
                current = current.left  # Vai para a esquerda se a chave for menor.
            else:
                current = current.right  # Vai para a direita se a chave for maior.

        self.misses += 1  # Incrementa o contador de erros.
        
        return comparisons  # Retorna o número de comparações, mesmo se o nó não for encontrado.

    def inorder_traversal(self, node):
        """
        Percorre a árvore em ordem (in-order traversal).
        """
        
        if node is not None:
            # Percorre a subárvore esquerda.
            self.inorder_traversal(node.left)

            # Visita o nó atual (imprime a chave).
            print(node.key)

            # Percorre a subárvore direita.
            self.inorder_traversal(node.right)

    def print_tree(self, node, indent="", last=True):
        """
        Exibe a árvore no terminal de forma hierárquica.
        """
        if node is not None:
            # Imprime a indentação atual.
            print(indent, end="")

            # Verifica se este é o último nó no nível atual.
            if last:
                print("└── ", end="")  # Usa "└──" para o último nó.
                indent += "    "  # Adiciona espaços para a próxima linha.
            else:
                print("├── ", end="")  # Usa "├──" para nós intermediários.
                indent += "│   "  # Adiciona uma barra vertical para a próxima linha.

            # Imprime a chave do nó atual.
            print(node.key)

            # Percorre a subárvore esquerda.
            self.print_tree(node.left, indent, False)

            # Percorre a subárvore direita.
            self.print_tree(node.right, indent, True)

    def visualize_tree(self):
        """
        Gera uma visualização gráfica da árvore usando matplotlib e networkx.
        """
        G = nx.DiGraph()  # Cria um grafo direcionado para representar a árvore.
        self._add_nodes_edges(self.root, G)  # Adiciona nós e arestas ao grafo.

        # Define a posição dos nós para desenhar a árvore.
        pos = self._hierarchy_pos(G, self.root.key if self.root else None)

        # Desenha a árvore.
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10, font_color='white', edge_color='black', arrows=False)
        plt.show()  # Exibe o gráfico.

    def _add_nodes_edges(self, node, G):
        """
        Adiciona nós e arestas ao grafo.
        """
        if node is not None:
            # Adiciona o nó ao grafo.
            G.add_node(node.key)

            # Adiciona uma aresta para o filho esquerdo, se existir.
            if node.left is not None:
                G.add_edge(node.key, node.left.key)
                self._add_nodes_edges(node.left, G)  # Recursão para o filho esquerdo.

            # Adiciona uma aresta para o filho direito, se existir.
            if node.right is not None:
                G.add_edge(node.key, node.right.key)
                self._add_nodes_edges(node.right, G)  # Recursão para o filho direito.

    def _hierarchy_pos(self, G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        Define a posição dos nós para desenhar a árvore hierarquicamente.
        """
        if root is None:
            return {}  # Retorna um dicionário vazio se a árvore estiver vazia.

        # Define a posição do nó raiz.
        pos = {root: (xcenter, vert_loc)}

        # Obtém os vizinhos (filhos) do nó raiz.
        neighbors = list(G.neighbors(root))

        # Se houver vizinhos, calcula a posição de cada um.
        if len(neighbors) != 0:
            dx = width / 2  # Largura do espaço para cada subárvore.
            nextx = xcenter - width / 2  # Posição inicial no eixo x.

            # Percorre os vizinhos e calcula suas posições.
            for neighbor in neighbors:
                if neighbor < root:  # Nó à esquerda (menor que o nó atual).
                    pos.update(self._hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx))
                else:  # Nó à direita (maior que o nó atual).
                    pos.update(self._hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx + dx))
                nextx += dx

        # Retorna o dicionário de posições.
        return pos