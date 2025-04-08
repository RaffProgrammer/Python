produto = float(input("Digite o valor do produto: "))

# Leitura da forma de pagamento
print("Escolha a forma de pagamento:")
print("1 - À Vista em Dinheiro ou Pix")
print("2 - À Vista no cartão de crédito")
print("3 - Parcelado no cartão em duas vezes")
print("4 - Parcelado no cartão em três vezes ou mais")
codigo_pagamento = int(input("Digite o código da forma de pagamento: "))

# Cálculo do valor a ser pago conforme a forma de pagamento
if codigo_pagamento == 1:
    # 15% de desconto
    valor_final = produto * 0.85
    print(f"Valor final a pagar: R${valor_final:.2f} (15% de desconto)")
elif codigo_pagamento == 2:
    # 10% de desconto
    valor_final = produto * 0.90
    print(f"Valor final a pagar: R${valor_final:.2f} (10% de desconto)")
elif codigo_pagamento == 3:
    # Parcelado em 2 vezes, preço normal
    valor_final = produto
    print(f"Valor final a pagar: R${valor_final:.2f} (parcelado em 2 vezes, preço normal)")
elif codigo_pagamento == 4:
    # Parcelado em 3 ou mais vezes, com 10% de juros
    valor_final = produto * 1.10
    print(f"Valor final a pagar: R${valor_final:.2f} (10% de juros)")
else:
    print("Código de pagamento inválido!")
