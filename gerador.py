import csv
import random

def gerar_aposta():
    # Gera um ID alfanumérico na primeira posição
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    # Sorteia uma quantidade aleatória de números
    qtd_numeros = random.randint(1, 20)
    numeros = random.sample(range(1, 61), qtd_numeros)
    return [id_aposta] + sorted(numeros)

def main():
    with open('apostas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for _ in range(5):
            writer.writerow(gerar_aposta())

if __name__ == "__main__":
    main()