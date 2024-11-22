# upper -> converte para caracteres maiúsculos
# lower -> converte para caracteres minúsculos 
genero = (input("Digite a letra F ou M :"))

if genero == 'M':
    print(f"A letra digitada {genero}  é masculino")
elif genero == 'F':
    print(f"A letra digitada {genero} é feminino")
else: 
    print("genero inválido")
