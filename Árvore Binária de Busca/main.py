import os
import sys
import time
from BinarySearchTree import BinarySearchTree  # Importa a classe BinarySearchTree
import argparse

# Adiciona o caminho do diretório pai ao sys.path para permitir a importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils')))

from utils import clear_terminal

# Verifica se o usuário possui os pacotes necessários para executar o programa
try:
    import graphviz
except ImportError:
    print("Instalando o pacote graphviz...")
    os.system("pip install graphviz")
    import graphviz
    
try:
    import rich.console as console
    import rich.table as table
except ImportError:
    print("Instalando o pacote rich...")
    os.system("pip install rich")
    import rich.console as console
    import rich.table as table


# Argumentos para o programa relacionados à exibição da árvore
"""
    python main.py --print-terminal -> Exibe a árvore no terminal
    python main.py --print-graphical -> Exibe a árvore graficamente
    python main.py --print-terminal --print-graphical -> Exibe a árvore no terminal e graficamente
"""
parser = argparse.ArgumentParser(description="Construa uma árvore binária de busca a partir de um arquivo de entrada.")
parser.add_argument('--print-terminal', action='store_true', help="Imprime a árvore no terminal.")
parser.add_argument('--print-graphical', action='store_true', help="Visualiza a árvore graficamente.")
parser.add_argument('--write-result-archive', action='store_true', help="Escreve os resultados em um arquivo.")
args = parser.parse_args()

PRINT_TREE_TERMINAL = args.print_terminal
PRINT_TREE_GRAPHICAL = args.print_graphical
WRITE_RESULT_ARCHIVE = args.write_result_archive

if __name__ == '__main__':
    
    clear_terminal()
    
    console = console.Console()

    # Percorre a pasta "Entradas Árvores/Construir" e cria um menu de opções usando o os
    # para o usuário escolher o arquivo de entrada
    options = os.listdir("../Entradas Árvores/Construir")
    options = [f for f in options if f.endswith('.txt')]
    options.sort(key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    options.append("Sair")

    # Cria um menu de opções para o usuário escolher o arquivo de entrada
    console.print("Selecione o arquivo de entrada para construir a árvore binária de busca:")
    for i, op in enumerate(options):
        console.print(f"[bold red]{i+1}[/bold red] - {op}")

    # Pega a opção escolhida pelo usuário
    option = console.input("Opção: ")
    option = int(option)
    
    clear_terminal()

    # Verifica se a opção escolhida é válida
    if option < 1 or option > len(options):
        console.print("Opção inválida!")
    else:
        if option == len(options):
            console.print("Saindo...")
        else:
            # Lê o arquivo de entrada
            with open(f"../Entradas Árvores/Construir/{options[option-1]}", 'r') as file:
                lines = file.readlines()
                # Processa cada linha separadamente
                numbers = []
                for line in lines:
                    try:
                        numbers.extend(map(int, line.strip().split()))
                    except ValueError:
                        continue  # Ignora linhas com caracteres inválidos

            # Constrói a árvore binária de busca
            bst_tree = BinarySearchTree()  # Cria uma instância da árvore binária de busca
            start_time = time.time()  # Inicia a contagem do tempo

            for number in numbers:
                bst_tree.insert(number)  # Insere os números na árvore

            end_time = time.time()  # Finaliza a contagem do tempo
            total_time = end_time - start_time  # Calcula o tempo total

            # Exibe os resultados em uma tabela
            result_table = table.Table(title="Resultados da Construção da Árvore Binária de Busca")
            result_table.add_column("Descrição", justify="left", style="cyan")
            result_table.add_column("Valor", justify="right", style="green")

            result_table.add_row("Quantidade de comparações", str(bst_tree.comparison_count))
            result_table.add_row("Tempo total de construção (s)", f"{total_time:.6f}")

            console.print(result_table)
            
            # Lê o arquivo de consulta
            with open(f"../Entradas Árvores/Consultar/{options[option-1]}", 'r') as file:
                lines = file.readlines()
                # Processa cada linha separadamente
                query_numbers = []
                for line in lines:
                    try:
                        query_numbers.extend(map(int, line.strip().split()))
                    except ValueError:
                        continue  # Ignora linhas com caracteres inválidos

            # Realiza as consultas
            query_comparison_count = 0  # Contador de comparações durante as consultas
            start_query_time = time.time()  # Inicia a contagem do tempo de consulta

            for number in query_numbers:
                # Busca o número na árvore e incrementa o contador de comparações
                query_comparison_count += bst_tree.search(number)

            end_query_time = time.time()  # Finaliza a contagem do tempo de consulta
            total_query_time = end_query_time - start_query_time  # Calcula o tempo total de consulta

            # Exibe os resultados da consulta em uma tabela
            query_table = table.Table(title="Resultados da Consulta na Árvore Binária de Busca")
            query_table.add_column("Descrição", justify="left", style="cyan")
            query_table.add_column("Valor", justify="right", style="green")

            query_table.add_row("Quantidade de comparações", str(query_comparison_count))
            query_table.add_row("Tempo total de consulta (s)", f"{total_query_time:.6f}")
            query_table.add_row("[green]Hits (acertos)[/green]", f"[green]{bst_tree.hits}[/green]")  # Exibe o número de acertos
            query_table.add_row("[red]Misses (erros)[/red]", str(bst_tree.misses))  # Exibe o número de erros

            console.print(query_table)
            
            # Exibe a árvore binária de busca (opcional para grandes árvores)
            if PRINT_TREE_TERMINAL:
                bst_tree.print_tree(bst_tree.root)
            
            if PRINT_TREE_GRAPHICAL:
                bst_tree.visualize_tree()
                
            if WRITE_RESULT_ARCHIVE:

                # Verifica se o arquivo de saída já existe, se sim, remove
                if os.path.exists(f"../Saídas Árvores/Construir/{options[option-1]}_Arvore_Binaria_de_Busca.txt"):
                    os.remove(f"../Saídas Árvores/Construir/{options[option-1]}_Arvore_Binaria_de_Busca.txt")
                    
                with open(f"../Saídas Árvores/Construir/{options[option-1]}_Arvore_Binaria_de_Busca.txt", 'w') as file:
                    file.write(f"Quantidade de comparações: {bst_tree.comparison_count}\n")
                    file.write(f"Tempo total de construção (s): {total_time:.6f}\n")
                    
                with open(f"../Saídas Árvores/Consultar/{options[option-1]}_Arvore_Binaria_de_Busca.txt", 'w') as file:
                    file.write(f"Quantidade de comparações: {query_comparison_count}\n")
                    file.write(f"Tempo total de consulta (s): {total_query_time:.6f}\n")
                    file.write(f"Hits (acertos): {bst_tree.hits}\n")
                    file.write(f"Misses (erros): {bst_tree.misses}\n")