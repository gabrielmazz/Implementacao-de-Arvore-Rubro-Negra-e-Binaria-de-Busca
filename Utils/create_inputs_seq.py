import random
import os
import argparse

# Gerador de entradas para criar as árvores binárias de busca, neste arquivo ele cria uma sequencia de 1 a AMOUNT
# Tendo uma diferença que aleatoriza os números de 1 a RANGE para a consulta
# Exemplo: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ...

parser = argparse.ArgumentParser(description="Gerador de entradas para criar as árvores binárias de busca.")
parser.add_argument('amount', type=int, help="Número de números em cada arquivo.")
parser.add_argument('range', type=int, help="Range de números de 1 a RANGE.")
args = parser.parse_args()

AMOUNT = args.amount
RANGE = args.range

# Cria o arquivo de entrada para contruir a árvore
with open(f"../Entradas Árvores/Construir/entrada_{AMOUNT}.txt", 'w') as file:
    numbers = range(1, AMOUNT+1)
    file.write(' '.join(map(str, numbers)))
    
# Cria o arquivo de entrada para consultar a árvore
with open(f"../Entradas Árvores/Consultar/entrada_{AMOUNT}.txt", 'w') as file:
    numbers = random.sample(range(1, RANGE), AMOUNT)
    file.write(' '.join(map(str, numbers)))