"""
Calculadora de Partidas Rankeadas
---------------------------------
Calcula o saldo de vitórias (vitórias - derrotas) de um jogador
e informa em qual nível/patente ele se encontra.
"""

# Nome do heroi
nome = input("Digite o nome do herói: ")


def calcular_nivel(vitorias):
    """Recebe a quantidade de vitórias e retorna o nível correspondente."""
    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:  # vitorias >= 101
        nivel = "Imortal"

    return nivel


def calcular_saldo(vitorias, derrotas):
    """Recebe vitórias e derrotas e retorna o saldo (vitórias - derrotas) e o nível."""
    saldo_vitorias = vitorias - derrotas
    nivel = calcular_nivel(vitorias)

    return saldo_vitorias, nivel


def exibir_resultado(saldo_vitorias, nivel):
    """Exibe a mensagem final formatada."""
    print(
        f"O Herói {nome}tem de saldo de {saldo_vitorias} está no nível de {nivel}")


def main():
    # Laço de repetição para permitir múltiplas consultas
    while True:
        try:
            vitorias = int(input("Digite a quantidade de vitórias: "))
            derrotas = int(input("Digite a quantidade de derrotas: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros.\n")
            continue

        if vitorias < 0 or derrotas < 0:
            print("Os valores não podem ser negativos.\n")
            continue

        saldo_vitorias, nivel = calcular_saldo(vitorias, derrotas)
        exibir_resultado(saldo_vitorias, nivel)

        continuar = input(
            "\nDeseja calcular novamente? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando a calculadora. Até a próxima!")
            break


if __name__ == "__main__":
    main()
