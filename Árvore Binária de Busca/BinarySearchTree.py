from Node import Node
import rich.console as console
import networkx as nx
import matplotlib.pyplot as plt

class BinarySearchTree:
    def __init__(self):
        # Inicializa a raiz da árvore como None (árvore vazia).
        self.root = None

        # Contadores para comparações, hits e misses.
        self.comparison_count = 0
        self.hits = 0
        self.misses = 0

    def insert(self, key):
        """
        Insere um novo nó com a chave fornecida na árvore.
        """
        new_node = Node(key)  # Cria um novo nó.
        parent = None
        current = self.root

        # Encontra a posição correta para inserir o novo nó.
        while current is not None:
            parent = current
            self.comparison_count += 1  # Conta a comparação.
            if key < current.key:
                current = current.left
            else:
                current = current.right

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
        current = self.root
        comparisons = 0  # Contador de comparações.

        while current is not None:
            comparisons += 1
            if key == current.key:
                self.hits += 1  # Incrementa o contador de acertos.
                return comparisons
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        self.misses += 1  # Incrementa o contador de erros.
        return comparisons

    def inorder_traversal(self, node):
        """
        Percorre a árvore em ordem (in-order traversal).
        """
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def print_tree(self, node, indent="", last=True):
        """
        Exibe a árvore no terminal de forma hierárquica.
        """
        if node is not None:
            print(indent, end="")
            if last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "│   "

            print(node.key)
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

    def visualize_tree(self):
        """
        Gera uma visualização gráfica da árvore usando matplotlib e networkx.
        """
        G = nx.DiGraph()  # Grafo direcionado.
        self._add_nodes_edges(self.root, G)

        # Define a posição dos nós para desenhar a árvore.
        pos = self._hierarchy_pos(G, self.root.key if self.root else None)

        # Desenha a árvore.
        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10, font_color='white', edge_color='black', arrows=False)
        plt.show()

    def _add_nodes_edges(self, node, G):
        """
        Adiciona nós e arestas ao grafo.
        """
        if node is not None:
            G.add_node(node.key)
            if node.left is not None:
                G.add_edge(node.key, node.left.key)
                self._add_nodes_edges(node.left, G)
            if node.right is not None:
                G.add_edge(node.key, node.right.key)
                self._add_nodes_edges(node.right, G)

    def _hierarchy_pos(self, G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        Define a posição dos nós para desenhar a árvore hierarquicamente.
        """
        if root is None:
            return {}

        pos = {root: (xcenter, vert_loc)}
        neighbors = list(G.neighbors(root))

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

        return pos