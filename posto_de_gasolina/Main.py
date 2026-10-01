from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento

etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")


carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")

camionete = Veiculo("Camionete", "ABC-1284")
suv = Veiculo("SUV", "ABC-1122")
esportivo = Veiculo("Esportivo", "ABC-1004")
caminhao = Veiculo("Caminhao", "ABC-1200")
compacto = Veiculo("Compacto", "ABC-1300")


abastecimento1 = Abastecimento(carro, etanol, 50)
abastecimento2 = Abastecimento(moto, gasolina, 25)
abastecimento3 = Abastecimento(van, diesel, 200)

abastecimento4 = Abastecimento(camionete, gasolina, 200)
abastecimento5 = Abastecimento(suv, gasolina, 250)
abastecimento6 = Abastecimento(esportivo, gasolina, 180)
abastecimento7 = Abastecimento(caminhao, diesel, 500)
abastecimento8 = Abastecimento(compacto, etanol, 50)


abastecimentos = [
    abastecimento1,
    abastecimento2,
    abastecimento3,
    abastecimento4,
    abastecimento5,
    abastecimento6,
    abastecimento7,
    abastecimento8
]


print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()


total_etanol = 0
total_gasolina = 0
total_diesel = 0

for abastecimento in abastecimentos:

    if abastecimento.combustivel.nome == "Etanol":
        total_etanol += abastecimento.valor

    elif abastecimento.combustivel.nome == "Gasolina":
        total_gasolina += abastecimento.valor

    elif abastecimento.combustivel.nome == "Diesel":
        total_diesel += abastecimento.valor


total_dia = total_etanol + total_gasolina + total_diesel


with open("recibo_posto.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("========== POSTO DE GASOLINA ==========\n")

    for abastecimento in abastecimentos:

        arquivo.write(
            f"{abastecimento.veiculo.modelo} - "
            f"{abastecimento.veiculo.placa}\n"
        )

        arquivo.write(
            f"Combustível: "
            f"{abastecimento.combustivel.nome}\n"
        )

        arquivo.write(
            f"Valor: R$ {abastecimento.valor:.2f}\n\n"
        )

    arquivo.write("========================================\n")
    arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
    arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
    arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
    arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")


with open("recibo_posto.txt", "r", encoding="utf-8") as arquivo:

    texto = arquivo.read()

    print("\n========== CONTEÚDO DO RECIBO ==========\n")
    print(texto)

    posicao_etanol = texto.find("Etanol:")
    fim_linha = texto.find("\n", posicao_etanol)

    etanol_texto = texto[
        posicao_etanol + len("Etanol:"):fim_linha
    ].strip()

    posicao_gasolina = texto.find("Gasolina:")
    fim_linha = texto.find("\n", posicao_gasolina)

    gasolina_texto = texto[
        posicao_gasolina + len("Gasolina:"):fim_linha
    ].strip()

    posicao_diesel = texto.find("Diesel:")
    fim_linha = texto.find("\n", posicao_diesel)

    diesel_texto = texto[
        posicao_diesel + len("Diesel:"):fim_linha
    ].strip()

    posicao_total_dia = texto.find("TOTAL DO DIA:")
    fim_linha = texto.find("\n", posicao_total_dia)

    total_dia_texto = texto[
        posicao_total_dia + len("TOTAL DO DIA:"):fim_linha
    ].strip()


print("========== TOTAIS ENCONTRADOS NO TXT ==========")

print(f"Total ganho Etanol: {etanol_texto}")
print(f"Total ganho Gasolina: {gasolina_texto}")
print(f"Total ganho Diesel: {diesel_texto}")
print(f"Total ganho no dia: {total_dia_texto}")
