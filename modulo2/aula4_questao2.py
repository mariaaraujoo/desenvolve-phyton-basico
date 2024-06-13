#Ler a temperatura em Fahrenheit
temperatura_F = int(input("Digite a temperatura em Fahrenheit: "))

#Converter a temperatura em Fahrenheit para Celsius
temperatura_C = (temperatura_F - 32) * (5/9)

#Converter o valor em Celsius para inteiro
temperatura_C = int(temperatura_C)

#Resultado final da conversão
print(f"{temperatura_F} graus Fahrenheit são {temperatura_C} graus Celsius")