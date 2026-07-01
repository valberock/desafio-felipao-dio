# ---------------------------------------------
# Script para ranquear um Herói com base no XP
# ---------------------------------------------

# Nome do herói
nome = "Aragorn"

# Recebe a quantidade de experiência (xp) como número inteiro
xp = int(input("Digite a quantidade de experiência (XP) do herói: "))

# Estrutura de decisão para definir o nível do herói
if xp < 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibe a mensagem final
print(f"O Herói de nome {nome} está no nível {nivel}")
