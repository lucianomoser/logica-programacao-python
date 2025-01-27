
novoCalculo = "S"
while novoCalculo == "S" or novoCalculo == "s":

    primeiraNota = float(input("Digite a primeira nota: "))
    segundaNota = float(input("Digite a segunda nota: "))

    mediaNota = (primeiraNota + segundaNota) / 2

    if mediaNota >=7:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")
    print(f"Media do Aluno: {mediaNota:.2f}")
    novoCalculo = input("Deseja calcular a nova media (S = Sim ou N = Não)?")








