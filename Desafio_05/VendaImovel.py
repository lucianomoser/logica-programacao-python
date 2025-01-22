nome_vendedor = input("Digite o nome do vendedor: ")
valor_imovel = float(input("Digite o valor do Imóvel: "))
commisao_venda = 0
if valor_imovel >= 50000.00:
    commisao_venda = valor_imovel * 0.2
elif valor_imovel >= 30000.00:
    commisao_venda = valor_imovel * 0.15
elif valor_imovel < 30000.00:
    commisao_venda = valor_imovel * 0.1
else:
    print("Valor digitado não está formatado corretamente.")

print("Nome do vendedor: ", nome_vendedor)
print(f"Valor do Imóvel: {valor_imovel:.2f}")
print(f"Valor da comissão do vendedor: {commisao_venda:.2f}")




