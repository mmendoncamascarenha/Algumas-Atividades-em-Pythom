salario = float(input("Digite o seu salario: "))
aumento = 0
novo_salario = 0

if salario <=280:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print(f"Reajuste de 20% sálario antigo {salario} aumento {aumento} e novo salário {novo_salario}")


