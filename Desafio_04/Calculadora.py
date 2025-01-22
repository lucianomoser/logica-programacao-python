

print("Escolha a opção:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = int(input("Digite o número da operação desejada (1/2/3/4): "))

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

def escolherOpcao(numeroEscolhido):
    match numeroEscolhido:
        case 1:
            resultado = numero1 + numero2
        case 2:
            resultado = numero1 - numero2
        case 3:
            resultado = numero1 * numero2
        case 4:
            resultado = numero1 / numero2
        case _:
            return print("Não possui a opção digitada.")
    return resultado

print("Resultado:", escolherOpcao(escolha))





