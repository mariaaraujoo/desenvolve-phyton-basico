#nome,preço e quantidade do produto 1
nome1 = str (input("Digite o nome do produto 1: "))
preço1= float(input("Digite o preço unitário do produto 1: "))
quantidade1 = int(input("Digite a quantidade do produto 1: "))

#nome,preço e quantidade do produto 2
nome2 = str(input("Digite o nome do produto 2: "))
preço2= float(input("Digite o preço unitário do produto 2: "))
quantidade2 = int(input("Digite a quantidade do produto 2: "))

#nome,preço e quantidade do produto 3
nome3 = str(input("Digite o nome do produto 3: "))
preço3= float(input("Digite o preço unitário do produto 3: "))
quantidade3 = int(input("Digite a quantidade do produto 3: "))

#cálculo do valor final da compra
valor_final = (preço1 * quantidade1) + (preço2 * quantidade2) + (preço3 * quantidade3)

#valor final da compra
print(f"Total: R${valor_final:,.2f}")
