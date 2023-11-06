# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
numero = [ ]
for n in range (0, 7):
    ADN = int(input("Digite o ADN: "))
    if ADN <=2005:
        print("maioridade")
    else:
        print("nao atingiu")