nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

nome = input("Digite o nome do aluno: ")

if media >= 7:
    status = "Aprovado"
else:
    status = "Reprovado"

print("Aluno:", nome)
print("Média:", media)
print("Status:", status)
