valor_hora_aula = float(input("Digite o valor da hora aula: R$"))
numero_aulas = int(input("Digite o número de aulas lecionadas no mês: "))
percentual_inss = float(input("Digite o percentual de desconto do INSS: "))

salario_bruto = valor_hora_aula * numero_aulas

desconto_inss = salario_bruto * (percentual_inss / 100)

salario_liquido = salario_bruto - desconto_inss

# Correção na impressão das variáveis
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Desconto do INSS: R${desconto_inss:.2f}")
print(f"Salário Líquido: R${salario_liquido:.2f}")
