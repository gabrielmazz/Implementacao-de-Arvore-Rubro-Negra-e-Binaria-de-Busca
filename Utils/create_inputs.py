import random
import os
import argparse

# Gerador de entradas para criar as árvores binárias de busca
# Exemplo: 40 54 34 42 17 61 98 13 14 35 39 8 37 31 86 92 15 27 59 28

parser = argparse.ArgumentParser(description="Gerador de entradas para criar as árvores binárias de busca.")
parser.add_argument('--amount', type=int, help="Número de números em cada arquivo.")
parser.add_argument('--range', type=int, help="Range de números de 1 a RANGE.")
parser.add_argument('--name', type=str, help="Nome do arquivo de saída.")
args = parser.parse_args()

AMOUNT = args.amount
RANGE = args.range

# Cria o arquivo de entrada para contruir a árvore 

# Verifica se o argumento de nome do arquivo foi passado
if args.name:
    with open(f"../Entradas Árvores/Construir/{args.name}.txt", 'w') as file:
        numbers = random.sample(range(1, RANGE), AMOUNT)
        file.write(' '.join(map(str, numbers)))
        
    with open(f"../Entradas Árvores/Consultar/{args.name}.txt", 'w') as file:
        numbers = random.sample(range(1, RANGE), AMOUNT)
        file.write(' '.join(map(str, numbers)))
else:
    with open(f"../Entradas Árvores/Construir/entrada_{AMOUNT}.txt", 'w') as file:
        numbers = random.sample(range(1, RANGE), AMOUNT)
        file.write(' '.join(map(str, numbers)))
        
    with open(f"../Entradas Árvores/Consultar/entrada_{AMOUNT}.txt", 'w') as file:
        numbers = random.sample(range(1, RANGE), AMOUNT)
        file.write(' '.join(map(str, numbers)))
    