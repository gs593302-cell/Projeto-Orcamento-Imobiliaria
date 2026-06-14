from imovel import Imovel
import csv

print("=== ORÇAMENTO IMOBILIÁRIA R.M ===")

tipo = input("Tipo do imóvel (apartamento/casa/estudio): ").lower()

quartos = 1

if tipo != "estudio":
    quartos = int(input("Quantidade de quartos (1 ou 2): "))

garagem = False

if tipo != "estudio":
    resp = input("Possui garagem? (s/n): ").lower()
    garagem = resp == "s"

criancas = True

if tipo == "apartamento":
    resp = input("Possui crianças? (s/n): ").lower()
    criancas = resp == "s"

imovel = Imovel(tipo, quartos, garagem, criancas)

valor_aluguel = imovel.calcular_aluguel()

parcelas = int(input("Parcelar contrato em até 5 vezes: "))

while parcelas < 1 or parcelas > 5:
    parcelas = int(input("Digite um valor entre 1 e 5: "))

valor_contrato = 2000
valor_parcela = valor_contrato / parcelas

print("\n===== ORÇAMENTO =====")
print(f"Valor do aluguel: R$ {valor_aluguel:.2f}")
print(f"Valor do contrato: R$ {valor_contrato:.2f}")
print(f"{parcelas}x de R$ {valor_parcela:.2f}")

with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    escritor.writerow(["Mes", "Valor"])

    for mes in range(1, 13):
        escritor.writerow([mes, valor_aluguel])

print("\nArquivo CSV gerado com sucesso!")