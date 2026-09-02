import csv
import random

def gerar_aposta():
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    qtd_numeros = random.randint(1, 20)
    numeros = random.sample(range(1, 61), qtd_numeros)
    return [id_aposta] + sorted(numeros)

def main():
    with open('apostas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        linhas_geradas = 0
        while linhas_geradas < 5:
            aposta = gerar_aposta()
            # Regra Mega-Sena: Aceita apenas entre 6 e 15 números (descontando o ID)
            if 6 <= (len(aposta) - 1) <= 15:
                writer.writerow(aposta)
                linhas_geradas += 1

if __name__ == "__main__":
    main()