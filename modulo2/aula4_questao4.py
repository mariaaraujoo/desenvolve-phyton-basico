valor = int(input("Digite um valor inteiro em reais: "))

notas = [100, 50, 20, 10, 5, 2, 1]

quantidade_notas = {}

for nota in notas:
    quantidade_notas[nota] = valor // nota
    valor %= nota

for nota in notas:
    print(f"{quantidade_notas[nota]} nota(s) de R${nota},00")