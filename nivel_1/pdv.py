
compras = []

print("=== Sistema de PDV com Descontos ===")
print("Digite 0 no valor da compra a qualquer momento para encerrar.\n")

while True:

    valor_compra = float(input("Digite o valor da compra (R$): "))
    while valor_compra < 0:
        print("Aviso: O valor da compra não pode ser negativo. Tente novamente.")
        valor_compra = float(input("Digite o valor da compra (R$): "))


    if valor_compra == 0:
        break

    idade = int(input("Digite a idade do cliente: "))
    while idade < 0:
        print("Aviso: A idade não pode ser negativa. Tente novamente.")
        idade = int(input("Digite a idade do cliente: "))

    # Desconto por idade (20% se idade >= 65)
    valor_apos_idade = valor_compra
    if idade >= 65:
        valor_apos_idade = valor_compra * 0.80

    # Desconto por valor (10% extra sobre o valor já com desconto de idade, se > 100)
    valor_final = valor_apos_idade
    if valor_apos_idade > 100:
        valor_final = valor_apos_idade * 0.90

    desconto = valor_compra - valor_final

    print(f"Valor final: R$ {valor_final:.2f}\n")

    compras.append({
        "original": valor_compra,
        "desconto": desconto,
        "final": valor_final
    })

# Resumo Final do Dia
total_bruto = 0.0
total_descontos = 0.0
total_final = 0.0

for compra in compras:
    total_bruto = total_bruto + compra["original"]
    total_descontos = total_descontos + compra["desconto"]
    total_final = total_final + compra["final"]

print("\n================ RESUMO DO DIA ================")
print(f"Quantidade de compras registradas: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
print("===============================================")

