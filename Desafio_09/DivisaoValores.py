primero_valor_informado = float(input('Digite o primeiro valor da divisão (Dividendo): '))
while True:
    segundo_valor_informado = float(input("Digite o segundo valor da divisão (Divisor): "))
    if segundo_valor_informado == 0:
        input("Informe outro valor, Divisor não pode ser 0: ")
    else:
        break
resultadoDivisao = primero_valor_informado / segundo_valor_informado
print(f"O resultado da divisão {resultadoDivisao:.2f}")


