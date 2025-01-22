incremento = 0
total = 0.0
totalComDesconto = 0.0
i = 1
nomes = []
precos = []
quantidadeUnitarias = []
totalProdutos = int(input("Quantos produtos você deseja registrar? "))


for i  in range(totalProdutos):
      i += 1
      nome = input("Nome do Produto: ")
      nomes.append(nome)

      quantidadeUnitaria = int(input("Quantidade de itens: "))
      quantidadeUnitarias.append(quantidadeUnitaria)

      preco = float(input("Preço Produto: "))
      precos.append(preco)

      total += preco * quantidadeUnitaria

      if i <= 10:
          desconto = 0
          totalComDesconto = total
      elif i >= 11 and i <= 20:
          desconto = 0.10
          valorDesconto = total * desconto
          totalComDesconto = total - valorDesconto
      elif totalProdutos >= 21 and totalProdutos <= 50:
          desconto = 0.20
          valorDesconto = total * desconto
          totalComDesconto = total - valorDesconto
      else:
          desconto = 0.25
          valorDesconto = total * desconto
          totalComDesconto = total - valorDesconto
print("Quantidade de itens: " , totalProdutos)
print(f"Total:  {total:2f}")
print(f"Total com desconto: {totalComDesconto:.2f}")


