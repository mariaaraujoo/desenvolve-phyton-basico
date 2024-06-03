juros = 1.01
saldo = 500.0

saldo *= juros  # mês 1
saldo *= juros  # mês 2
saldo *= juros  # mês 3

print("Após 3 meses meu novo saldo é")
print(saldo)