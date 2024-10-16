import sys
import random
from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
def min_max_vet(vet):
    max_value = vet[0]
    min_value = vet[0]
    pos_max = 0
    pos_min = 0
    comp = 0  # Inicializa o contador de comparações

    for i in range(1, len(vet)):
        comp += 1  # Conta a comparação
        if max_value < vet[i]:
            max_value = vet[i]
            pos_max = i
        elif min_value > vet[i]:
            min_value = vet[i]
            pos_min = i

    return pos_max, pos_min, comp  # Retorna as posições e a contagem de comparações

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':
    v = []

    random.seed(int(datetime.now().strftime('%H%M%S')))

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 20

    for i in range(n):
        v.append(random.randint(0, 1000))

    posMax, posMin, total_comp = min_max_vet(v)  # Retorna a posição do maior  e menor numero e o número de comparações

    print(f"[ ", end='')
    for i in range(n - 1):
        if i == posMax:
            print(f"\033[1;92m", end='') 
        elif i == posMin:
            print(f"\033[1;91m", end='')  # Destaca o menor número
        else:
            print(f"\033[1;37m", end='')

        print(f"{v[i]}\033[1;37m, ", end='')

    if n - 1 == posMax:
        print(f"\033[1;92m", end='')
    elif n - 1 == posMin:
        print(f"\033[1;91m", end='')
    else:
        print(f"\033[1;37m", end='')

    print(f"{v[n - 1]}\033[1;37m]")

    print(f"Maior elemento da sequência = {v[posMax]}")
    print(f"Menor elemento da sequência = {v[posMin]}")
    print(f"Número de comparações feitas: {total_comp}")  # Exibe o total de comparações