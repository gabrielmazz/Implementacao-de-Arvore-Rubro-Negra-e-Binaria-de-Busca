from Node import Node
import rich.console as console
import networkx as nx
import matplotlib.pyplot as plt

class RedBlackTree:
    
    def __init__(self):
        
        # Cria um nó especial chamado NIL, que representa os nós folha da árvore rubro-negra.
        # O NIL é sempre preto (color='BLACK') e não contém nenhum valor (key=None).
        self.NIL = Node(None, color='BLACK')

        # Inicializa a raiz da árvore como o nó NIL.
        # No início, a árvore está vazia, então a raiz aponta para o NIL.
        self.root = self.NIL

        # Inicializa um contador de comparações.
        # Esse contador será usado para contar quantas comparações são feitas durante a inserção de elementos na árvore.
        self.comparison_count = 0
        
        # Inicializa o console para exibir mensagens no terminal.
        self.console = console.Console()
        
        # Contadores para hits e misses durante a busca.
        self.hits = 0 
        self.misses = 0

    def insert(self, key):
        # Cria um novo nó com a chave fornecida.
        # Por padrão, o novo nó é vermelho (color='RED').
        new_node = Node(key)

        # Define os filhos esquerdo e direito do novo nó como NIL.
        # NIL representa os nós folha na árvore rubro-negra.
        new_node.left = self.NIL
        new_node.right = self.NIL

        # Inicializa as variáveis para percorrer a árvore.
        # `parent` será o nó pai do novo nó.
        # `current` começa na raiz da árvore.
        parent = None
        current = self.root

        # Encontrar a posição correta para inserir o novo nó.
        # Percorre a árvore até encontrar um nó folha (NIL).
        while current != self.NIL:
            parent = current  # Atualiza o nó pai para o nó atual.

            # Incrementa o contador de comparações.
            # Cada comparação entre chaves é contabilizada.
            self.comparison_count += 1

            # Decide se deve ir para a subárvore esquerda ou direita.
            if new_node.key < current.key:
                current = current.left  # Vai para a esquerda se a chave for menor.
            else:
                current = current.right  # Vai para a direita se a chave for maior ou igual.

        # Define o pai do novo nó como o nó encontrado no loop acima.
        new_node.parent = parent

        # Se o pai for None, a árvore estava vazia, e o novo nó será a raiz.
        if parent is None:
            self.root = new_node
        # Se a chave do novo nó for menor que a chave do pai, insere à esquerda.
        elif new_node.key < parent.key:
            parent.left = new_node
        # Caso contrário, insere à direita.
        else:
            parent.right = new_node

        # Define a cor do novo nó como vermelho.
        # Na árvore rubro-negra, novos nós são sempre inseridos como vermelhos.
        new_node.color = 'RED'

        # Chama a função _fix_insert para corrigir possíveis violações das propriedades da árvore rubro-negra.
        # Isso garante que a árvore permaneça balanceada após a inserção.
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        
        # Enquanto o pai do nó existir e for vermelho, pode haver violações das propriedades da árvore rubro-negra.
        while node.parent and node.parent.color == 'RED':
            
            # Verifica se o pai do nó é o filho esquerdo do avô.
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right  # O tio é o filho direito do avô.

                # Caso 1: O tio é vermelho.
                if uncle.color == 'RED':
                    # Faz a recoloração:
                    # - Pai e tio ficam pretos.
                    # - Avô fica vermelho.
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'

                    # Move o nó para o avô, pois a violação pode ter subido na árvore.
                    node = node.parent.parent
                else:
                    # Caso 2: O tio é preto e o nó é o filho direito do pai.
                    if node == node.parent.right:
                        
                        # Faz uma rotação à esquerda no pai para transformar no Caso 3.
                        node = node.parent
                        self._left_rotate(node)

                    # Caso 3: O tio é preto e o nó é o filho esquerdo do pai.
                    # Faz a recoloração e uma rotação à direita no avô.
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._right_rotate(node.parent.parent)
            else:
                # O pai do nó é o filho direito do avô (caso simétrico ao anterior).
                uncle = node.parent.parent.left  # O tio é o filho esquerdo do avô.

                # Caso 1: O tio é vermelho.
                if uncle.color == 'RED':
                    # Faz a recoloração:
                    # - Pai e tio ficam pretos.
                    # - Avô fica vermelho.
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'

                    # Move o nó para o avô, pois a violação pode ter subido na árvore.
                    node = node.parent.parent
                else:
                    # Caso 2: O tio é preto e o nó é o filho esquerdo do pai.
                    if node == node.parent.left:
                        # Faz uma rotação à direita no pai para transformar no Caso 3.
                        node = node.parent
                        self._right_rotate(node)

                    # Caso 3: O tio é preto e o nó é o filho direito do pai.
                    # Faz a recoloração e uma rotação à esquerda no avô.
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self._left_rotate(node.parent.parent)

            # Se o nó atual for a raiz, sai do loop.
            if node == self.root:
                break

        # Garante que a raiz da árvore seja sempre preta.
        self.root.color = 'BLACK'

    def _left_rotate(self, x):
        
        # Antes da rotação à esquerda:
        # x
        #  \
        #   y
        #  /
        # z
        
        # Depois da rotação à esquerda:
        #   y 
        #  /
        # x
        #  \
        #   z
        
        # y é o filho direito de x.
        y = x.right

        # O filho esquerdo de y se torna o filho direito de x.
        x.right = y.left

        # Se o filho esquerdo de y não for NIL, atualiza seu pai para x.
        if y.left != self.NIL:
            y.left.parent = x

        # O pai de y agora é o pai de x.
        y.parent = x.parent

        # Se x era a raiz da árvore, y se torna a nova raiz.
        if x.parent is None:
            self.root = y
        # Se x era o filho esquerdo de seu pai, y se torna o novo filho esquerdo.
        elif x == x.parent.left:
            x.parent.left = y
        # Caso contrário, y se torna o novo filho direito.
        else:
            x.parent.right = y

        # x se torna o filho esquerdo de y.
        y.left = x

        # O pai de x agora é y.
        x.parent = y

    def _right_rotate(self, y):
        
        # Antes da rotação à direita:
        #   y
        #  /
        # x
        #  \
        #   z
        
        # Depois da rotação à direita:
        # x
        #  \
        #   y
        #  /
        # z
            
        # x é o filho esquerdo de y.
        x = y.left

        # O filho direito de x se torna o filho esquerdo de y.
        y.left = x.right

        # Se o filho direito de x não for NIL, atualiza seu pai para y.
        if x.right != self.NIL:
            x.right.parent = y

        # O pai de x agora é o pai de y.
        x.parent = y.parent

        # Se y era a raiz da árvore, x se torna a nova raiz.
        if y.parent is None:
            self.root = x
        # Se y era o filho direito de seu pai, x se torna o novo filho direito.
        elif y == y.parent.right:
            y.parent.right = x
        # Caso contrário, x se torna o novo filho esquerdo.
        else:
            y.parent.left = x

        # y se torna o filho direito de x.
        x.right = y

        # O pai de y agora é x.
        y.parent = x

    def search(self, key):
        """
        Busca um nó com a chave fornecida e retorna o número de comparações feitas.
        Incrementa os contadores de hits e misses.
        """
        current = self.root
        comparisons = 0  # Contador de comparações

        while current != self.NIL:
            comparisons += 1
            if key == current.key:
                self.hits += 1  # Incrementa o contador de acertos
                return comparisons  # Retorna o número de comparações
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        self.misses += 1  # Incrementa o contador de erros
        return comparisons  # Retorna o número de comparações, mesmo se o nó não for encontrado

    def inorder_traversal(self, node):
        
        # Verifica se o nó atual não é NIL (nó folha).
        if node != self.NIL:
            
            # Percorre a subárvore esquerda.
            self.inorder_traversal(node.left)

            # Imprime a chave e a cor do nó atual.
            print(node.key, node.color)

            # Percorre a subárvore direita.
            self.inorder_traversal(node.right)

    def print_tree(self, node, indent="", last=True):
                
        """
        Função para imprimir a árvore de forma visual dentro do console, usando a indentação para representar a hierarquia.
        
        Exemplo de árvore rubro-negra impressa no console:
        
        └── 40 (BLACK)
            ├── 17 (RED)
            │   ├── 13 (BLACK)
            │   │   └── 14 (RED)
            │   └── 34 (BLACK)
            │       └── 35 (RED)
            └── 54 (RED)
                ├── 42 (BLACK)
                └── 61 (BLACK)
                    └── 98 (RED)
        """
        
        # Verifica se o nó atual não é NIL (nó folha).
        if node != self.NIL:
            
            # Imprime a indentação atual.
            self.console.print(indent, end="")

            # Verifica se este é o último nó no nível atual.
            if last:
                self.console.print("└── ", end="")  # Usa "└──" para o último nó.
                indent += "    "       # Adiciona espaços para a próxima linha.
            else:
                self.console.print("├── ", end="")  # Usa "├──" para nós intermediários.
                indent += "│   "       # Adiciona uma barra vertical para a próxima linha.

            # Imprime a chave e a cor do nó atual.
            self.console.print(f"[{'red' if node.color == 'RED' else 'black'}]{node.key} ({node.color})[/]", style="red" if node.color == 'RED' else "black")

            # Percorre a subárvore esquerda.
            self.print_tree(node.left, indent, False)

            # Percorre a subárvore direita.
            self.print_tree(node.right, indent, True)
    
    def visualize_tree(self):
        """
        Gera uma visualização gráfica da árvore rubro-negra usando matplotlib, networkx, não sendo recomendado para
        árvores muito grandes, pois a visualização pode ficar confusa.
        """
        # Cria um grafo direcionado para representar a árvore.
        G = nx.DiGraph()

        # Adiciona nós e arestas ao grafo.
        self._add_nodes_edges(self.root, G)

        # Define a posição dos nós para desenhar a árvore.
        pos = self._hierarchy_pos(G, self.root.key)

        # Obtém as cores dos nós (vermelho ou preto).
        node_colors = [G.nodes[node]['color'] for node in G.nodes]

        # Configura o gráfico.
        plt.figure(figsize=(10, 6))

        # Desenha a árvore.
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color=node_colors, font_size=10, font_color='white', edge_color='black', arrows=False)

        # Exibe o gráfico.
        plt.show()
    
    def _add_nodes_edges(self, node, G):
        """
        Adiciona nós e arestas ao grafo para desenhar a árvore rubro-negra, sendo uma função auxiliar para a função
        visualize_tree.
        """
        # Verifica se o nó atual não é NIL (nó folha).
        if node != self.NIL:
            # Adiciona o nó ao grafo com sua cor (vermelho ou preto).
            G.add_node(node.key, color='red' if node.color == 'RED' else 'black')

            # Adiciona uma aresta para o filho esquerdo, se existir.
            if node.left != self.NIL:
                G.add_edge(node.key, node.left.key)
                self._add_nodes_edges(node.left, G)

            # Adiciona uma aresta para o filho direito, se existir.
            if node.right != self.NIL:
                G.add_edge(node.key, node.right.key)
                self._add_nodes_edges(node.right, G)

    def _hierarchy_pos(self, G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
        """
        Define a posição dos nós para desenhar a árvore hierarquicamente.
        """
        # Define a posição do nó raiz.
        pos = {root: (xcenter, vert_loc)}

        # Obtém os vizinhos (filhos) do nó raiz.
        neighbors = list(G.neighbors(root))

        # Se houver vizinhos, calcula a posição de cada um.
        if len(neighbors) != 0:
            dx = width / 2  # Largura do espaço para cada subárvore.
            nextx = xcenter - width / 2 - dx / 2  # Posição inicial no eixo x.

            # Percorre os vizinhos e calcula suas posições.
            for neighbor in neighbors:
                nextx += dx
                pos.update(self._hierarchy_pos(G, neighbor, width=dx, vert_gap=vert_gap, vert_loc=vert_loc - vert_gap, xcenter=nextx))

        # Retorna o dicionário de posições.
        return pos