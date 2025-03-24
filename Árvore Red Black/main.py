import os
import sys
import time
from RedBlackTree import RedBlackTree
import argparse

# Adiciona o caminho do diretório pai ao sys.path para permitir a importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Utils')))

#from Utils.utils import clear_terminal

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
parser = argparse.ArgumentParser(description="Construa uma árvore rubro-negra a partir de um arquivo de entrada.")
parser.add_argument('--print-terminal', action='store_true', help="Imprime a árvore no terminal.")
parser.add_argument('--print-graphical', action='store_true', help="Visualiza a árvore graficamente.")
parser.add_argument('--write-result-archive', action='store_true', help="Escreve os resultados em um arquivo.")
parser.add_argument('--all_inputs', action='store_true', help="Executa o programa para todos os arquivos de entrada.")
args = parser.parse_args()

PRINT_TREE_TERMINAL = args.print_terminal
PRINT_TREE_GRAPHICAL = args.print_graphical
WRITE_RESULT_ARCHIVE = args.write_result_archive

def process_file(input_file, console):
    # Lê o arquivo de entrada
    with open(f"../Entradas Árvores/Construir/{input_file}", 'r') as file:
        lines = file.readlines()
        # Processa cada linha separadamente
        numbers = []
        for line in lines:
            try:
                numbers.extend(map(int, line.strip().split()))
            except ValueError:
                continue  # Ignora linhas com caracteres inválidos

    # Constrói a árvore rubro-negra
    rb_tree = RedBlackTree()
    start_time = time.time()  # Inicia a contagem do tempo

    for number in numbers:
        rb_tree.insert(number)

    end_time = time.time()  # Finaliza a contagem do tempo
    total_time = end_time - start_time  # Calcula o tempo total

    # Exibe os resultados em uma tabela
    result_table = table.Table(title=f"Resultados da Construção da Árvore Rubro-Negra - {input_file}")
    result_table.add_column("Descrição", justify="left", style="cyan")
    result_table.add_column("Valor", justify="right", style="green")

    result_table.add_row("Quantidade de comparações", str(rb_tree.comparison_count))
    result_table.add_row("Tempo total de construção (s)", f"{total_time:.6f}")

    console.print(result_table)
    
    # Lê o arquivo de consulta
    with open(f"../Entradas Árvores/Consultar/{input_file}", 'r') as file:
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
        query_comparison_count += rb_tree.search(number)

    end_query_time = time.time()  # Finaliza a contagem do tempo de consulta
    total_query_time = end_query_time - start_query_time  # Calcula o tempo total de consulta

    # Exibe os resultados da consulta em uma tabela
    query_table = table.Table(title=f"Resultados da Consulta na Árvore Rubro-Negra - {input_file}")
    query_table.add_column("Descrição", justify="left", style="cyan")
    query_table.add_column("Valor", justify="right", style="green")

    query_table.add_row("Quantidade de comparações", str(query_comparison_count))
    query_table.add_row("Tempo total de consulta (s)", f"{total_query_time:.6f}")
    query_table.add_row("[green]Hits (acertos)[/green]", str(rb_tree.hits))  # Exibe o número de acertos
    query_table.add_row("[red]Misses (erros)[/red]", str(rb_tree.misses))  # Exibe o número de erros

    console.print(query_table)
    
    # Exibe a árvore rubro-negra (opcional para grandes árvores)
    if PRINT_TREE_TERMINAL:
        rb_tree.print_tree(rb_tree.root)
    
    if PRINT_TREE_GRAPHICAL:
        rb_tree.visualize_tree()
        
    if WRITE_RESULT_ARCHIVE:
        
        # Verifica se o arquivo de saída já existe, se sim, remove
        if os.path.exists(f"../Saídas Árvores/Construir/{input_file}_Arvore_Rubro-Negra.txt"):
            os.remove(f"../Saídas Árvores/Construir/{input_file}_Arvore_Rubro-Negra.txt")
        
        with open(f"../Saídas Árvores/Construir/{input_file}_Arvore_Rubro-Negra.txt", 'w') as file:
            file.write(f"Quantidade de comparações: {rb_tree.comparison_count}\n")
            file.write(f"Tempo total de construção (s): {total_time:.6f}\n")
        
        with open(f"../Saídas Árvores/Consultar/{input_file}_Arvore_Rubro-Negra.txt", 'w') as file:
            file.write(f"Quantidade de comparações: {query_comparison_count}\n")
            file.write(f"Tempo total de consulta (s): {total_query_time:.6f}\n")
            file.write(f"Hits (acertos): {rb_tree.hits}\n")
            file.write(f"Misses (erros): {rb_tree.misses}\n")

if __name__ == '__main__':
    
    console = console.Console()

    if args.all_inputs:
        # Percorre todos os arquivos de entrada na pasta "Entradas Árvores/Construir"
        input_files = os.listdir("../Entradas Árvores/Construir")
        input_files = [f for f in input_files if f.endswith('.txt')]
        input_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))

        for input_file in input_files:
            console.print(f"Processando arquivo: {input_file}")
            process_file(input_file, console)
            console.print("\n" + "="*50 + "\n")  # Separador entre os arquivos
    else:
        # Percorre a pasta "Entradas Árvores/Construir" e cria um menu de opções usando o os
        # para o usuário escolher o arquivo de entrada
        options = os.listdir("../Entradas Árvores/Construir")
        options = [f for f in options if f.endswith('.txt')]
        options.sort(key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
        options.append("Sair")

        # Cria um menu de opções para o usuário escolher o arquivo de entrada
        console.print("Selecione o arquivo de entrada para construir a árvore rubro-negra:")
        for i, op in enumerate(options):
            console.print(f"[bold red]{i+1}[/bold red] - {op}")

        # Pega a opção escolhida pelo usuário
        option = console.input("Opção: ")
        option = int(option)
        
        #clear_terminal()

        # Verifica se a opção escolhida é válida
        if option < 1 or option > len(options):
            console.print("Opção inválida!")
        else:
            if option == len(options):
                console.print("Saindo...")
            else:
                process_file(options[option-1], console)