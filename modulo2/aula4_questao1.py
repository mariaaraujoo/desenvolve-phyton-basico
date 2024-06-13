#Ler a largura do terreno (inteiro)
largura = int(input("Digite a largura do terreno em metros: "))
#Ler o comprimento do terreno (inteiro)
comprimento = int(input("Digite o comprimento do terreno em metros: "))
#Ler o preço por metro quadrado do terreno (ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado em reais: "))

#Calcular a área do terreno em metros quadrados
area_m2 = comprimento * largura
#Calcular o custo total do terreno
preco_total = preco_m2 * area_m2

#Imprimir o resultado 
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")