import random
import os
import argparse

# Gerador de entradas para criar as árvores binárias de busca
# Exemplo: 40 54 34 42 17 61 98 13 14 35 39 8 37 31 86 92 15 27 59 28

parser = argparse.ArgumentParser(description="Gerador de entradas para criar as árvores binárias de busca.")
parser.add_argument('--amount', type=int, help="Número de números em cada arquivo.")
parser.add_argument('--range', type=int, help="Range de números de 1 a RANGE.")
args = parser.parse_args()

AMOUNT = args.amount
RANGE = args.range

# Cria o arquivo de entrada para contruir a árvore 
with open(f"../Entradas Árvores/Construir/entrada_{AMOUNT}.txt", 'w') as file:
    numbers = random.sample(range(1, RANGE), AMOUNT)
    file.write(' '.join(map(str, numbers)))
    
# Cria o arquivo de entrada para consultar a árvore
with open(f"../Entradas Árvores/Consultar/entrada_{AMOUNT}.txt", 'w') as file:
    numbers = random.sample(range(1, RANGE), AMOUNT)
    file.write(' '.join(map(str, numbers)))