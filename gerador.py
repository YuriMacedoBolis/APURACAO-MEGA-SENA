import csv
import random
import sys

def gerar_aposta():
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    qtd_numeros = random.randint(1, 20)
    numeros = random.sample(range(1, 61), qtd_numeros)
    return [id_aposta] + sorted(numeros)

def main():
    # Lê o parâmetro passado no terminal (ex: python gerador.py 10). Se não informado, gera 5 por padrão.
    qtd_linhas = int(sys.argv[1]) if len(sys.argv) > 1 else 5

    with open('apostas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        linhas_geradas = 0
        while linhas_geradas < qtd_linhas:
            aposta = gerar_aposta()
            if 6 <= (len(aposta) - 1) <= 15:
                writer.writerow(aposta)
                linhas_geradas += 1

if __name__ == "__main__":
    main()