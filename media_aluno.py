media = float(input("Digite a nota média do aluno: "))

if media >= 6:
    print(f"Aluno com média {media} está Aprovado")
elif media <= 4:
    print(f"O aluno com média {media} está Reprovado")
else:
    print(f"Aluno como media {media} está em Recuperação")