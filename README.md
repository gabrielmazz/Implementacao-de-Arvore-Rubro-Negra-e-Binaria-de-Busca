# <p align="center">Árvore Binária de Busca e Árvore Red-Black</p>

<h3 align="center">Trabalho de Projeto e Análise de Algoritmos</h3>

<p align="center">
    <img src="https://img.shields.io/badge/Árvore-Binária%20de%20Busca-informational?logo=&style=for-the-badge&logoColor=333333&color=007db3&labelColor=333333" alt="">
    <img src="https://img.shields.io/badge/Árvore-Red%20Black-informational?logo=&style=for-the-badge&logoColor=333333&color=b3002d&labelColor=333333">
    <img src="https://img.shields.io/badge/UNIOESTE-2025-informational?logo=&style=for-the-badge&logoColor=333333&color=dbdf07&labelColor=333333" alt="">
    <img src="https://img.shields.io/badge/Pyrhon-3.10+-informational?logo=python&style=for-the-badge&logoColor=ffffff&color=8807df&labelColor=333333" alt="">
</p>

<h3 align="center">Ciências da Computação - Universidade Estadual do Oeste do Paraná (UNIOESTE)</h4>

<br>

<h4 align="center">Desenvolvido por:</h4>
<p align="center">
  <a href="https://github.com/gabrielmazz">Gabriel Mazzuco</a>,
  <a href="#">Marco Damo</a>,
  <a href="#">Maria Eduarda Crema Carlos</a> e
  <a href="#">Igor Kaiser Gris</a>
</p>

<br>

<h3 align="center">Introdução</h3>

<p align="">
    Este trabalho tem como objetivo a implementação de uma Árvore Binária de Busca e uma Árvore Red-Black, com as operações de inserção e posteriormente de consulta. O objetivo é comparar o desempenho das duas estruturas de dados em relação ao tempo de execução e a quantidade de comparações tanto na inserção quanto na consulta, tendo uma análise crítica dos resultados obtidos.
</p>

<br>

<h3 align="center">Entrada dos Dados</h3>

<p align="">
    A entrada dos dados será feita através de um arquivo de texto, onde a primeira linha conterá um número inteiro N, que representa a quantidade de elementos a serem inseridos na árvore. 
</p>

```python
    10 20 30 45 5 8 9 15 17 27 7 4 2 1 3 6 12 11 13 14 80 43 20 2 15
```

<p align="">
    Dentro da pasta <code>Entradas Árvores</code> existem duas pastas, uma para <code>Construir</code> e outra para <code>Consultar</code>. Dentro de cada uma dessas pastas existem arquivos de texto com os valores distintos, indo de um range de 50 a 250000 elementos, todos sendo disponibilizados pelo professor da disciplina.
</p>

<h4 align="center">Criação de uma ambiente de testes</h4>

<p align="">
    Dentro da pasta <code>Utils</code>, na raiz do projeto, existe um arquivo chamado <code>create_inputs.py</code>, que é responsável por gerar arquivos de entrada para testes tando para consulta e construção de árvores. Outro arquivo é o <code>create_inputs_seq.py</code>, que é responsável por gerar arquivos de entrada sequenciais, mas apenas para a construção de árvores. Para executar esses arquivos, basta seguir os comandos abaixo. Vale ressaltar que os arquivos possuem parametros que são passados no comando de execução
</p>

```bash
    python3 create_inputs.py AMOUNT RANGE
    python3 create_inputs_seq.py AMOUNT RANGE
```

<p align="">
    Onde <code>AMOUNT</code> é a quantidade de elementos a serem gerados e <code>RANGE</code> é o range de valores que os elementos podem ter.
</p>

<h3 align="center">🌳 Árvore Binária de Busca</h3>

<p align="">
    A árvore binária de busca é uma estrutura de dados que organiza os elementos de forma hierárquica, onde cada nó possui no máximo dois filhos, sendo um à esquerda e outro à direita. A árvore binária de busca possui a propriedade de que, para cada nó, todos os elementos à esquerda são menores que o nó e todos os elementos à direita são maiores que o nó.
</p>

<h4 align="center">Implementação</h4>

<p align="">
    A implementação da árvore binária de busca é feita com base numa classe chamada <code>Node.py</code>, que é responsável por criar um nó da árvore
</p>

```python
class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
```
<p align="">
    Indo pro arquivo <code>BinarySearchTree.py</code>, é onde a árvore é implementada, onde suas operações são feitas, sendo umma árvore binária de busca simples, ela possui duas operações principais, a de inserção e a de consulta.
</p>

```python
    def insert(self, key):

        new_node = Node(key) 
        parent = None  
        current = self.root 

        while current is not None:
            parent = current  
            self.comparison_count += 1  

            if key < current.key:
                current = current.left 
            else:
                current = current.right 

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
```

```python
    def search(self, key):
        current = self.root 
        comparisons = 0 

        while current is not None:
            comparisons += 1 
            if key == current.key:
                self.hits += 1 
                return comparisons  
            elif key < current.key:
                current = current.left 
            else:
                current = current.right  

        self.misses += 1  
        
        return comparisons 
```

<h3 align="center">🔴 Árvore Red-Black</h3>

<p align="">
    A árvore Red-Black é uma árvore binária de busca balanceada, onde cada nó possui uma cor, que pode ser vermelha ou preta. A árvore Red-Black possui as seguintes propriedades:
</p>

<ul>
    <li>Cada nó é vermelho ou preto</li>
    <li>A raiz é preta</li>
    <li>Todos os nós folha são pretos</li>
    <li>Se um nó é vermelho, então seus filhos são pretos</li>
    <li>Para cada nó, todos os caminhos de nós até os nós folha contêm o mesmo número de nós pretos</li>
</ul>

<h4 align="center">Implementação</h4>

<p align="">
    A implementação da árvore Red-Black é feita tambem com base na classe chamada <code>Node.py</code>, que é responsável por criar um nó da árvore, que é a mesma utilizada na 
    árvore binária de busca. Indo pro arquivo <code>RedBlackTree.py</code>, é onde a árvore é implementada, onde suas operações são feitas, sendo uma árvore Red-Black, ela 
    possui duas operações principais, a de inserção e a de consulta, mas aqui a inserção é um pouco mais complexa devido a propriedade de balanceamento da árvore e sendo 
    a Red-Black, existem alguns casos que devem ser tratados.
</p>

```python
    def insert(self, key):
        new_node = Node(key, 'RED') 
        parent = None  
        current = self.root 

        while current is not None:
            parent = current  
            self.comparison_count += 1  

            if key < current.key:
                current = current.left 
            else:
                current = current.right 

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)
```

```python
    def fix_insert(self, node):
        while node != self.root and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    self.left_rotate(node.parent.parent)

        self.root.color = 'BLACK'
```

```python
    def search(self, key):
        current = self.root 
        comparisons = 0 

        while current is not None:
            comparisons += 1 
            if key == current.key:
                self.hits += 1 
                return comparisons  
            elif key < current.key:
                current = current.left 
            else:
                current = current.right  

        self.misses += 1  
        
        return comparisons 

```python
    def search(self, key):
        current = self.root 
        comparisons = 0 

        while current is not None:
            comparisons += 1 
            if key == current.key:
                self.hits += 1 
                return comparisons  
            elif key < current.key:
                current = current.left 
            else:
                current = current.right  

        self.misses += 1  
        
        return comparisons 
```

<h3 align="center">Execução</h3>

<p align="">
    Para executar o projeto, basta rodar o arquivo <code>main.py</code>, que dependendo de qual árvore você deseja testar, basta entrar na pasta
    referente a árvore e rodar o arquivo <code>main.py</code> que está dentro dela.
</p>

<p align="">
    Vale ressaltar que o projeto, possui alguns parametros que podem ser passados na execução, indicando se quer printar a árvore no terminal e
    também se quiser mostrar como ficou a árvore após a inserção de todos os elementos.
</p>

```bash
    python main.py --print-terminal -> Exibe a árvore no terminal
    python main.py --print-graphical -> Exibe a árvore graficamente
    python main.py --print-terminal --print-graphical -> Exibe a árvore no terminal e graficamente
```

<h3 align="center">Bibliotecas necessárias</h3>

<p align="">
    Para rodar o projeto, é necessário ter a biblioteca <code>matplotlib</code>, que é responsável por exibir a árvore graficamente, a biblioteca
    <code>networkx</code>, que é responsável por criar o grafo da árvore e a biblioteca <code>rich</code>, que é responsável pelos inputs e outputs
    no terminal.
</p>

<p align="">
    Para instalar as bibliotecas, basta rodar o comando abaixo.
</p>

```bash
    pip install -r requirements.txt
```

