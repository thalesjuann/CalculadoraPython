def calculadora():
    operacoes = {
        '1': ('Adição', lambda x, y: x + y),
        '2': ('Subtração', lambda x, y: x - y),
        '3': ('Multiplicação', lambda x, y: x * y),
        '4': ('Divisão', lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero')
    }

    def formatar_numero(num):
        return int(num) if num.is_integer() else num

    while True:
        print("\n=============================")
        print("  Bem-vindo à Calculadora!")
        print("=============================")
        print("Selecione uma operação:")
        for key, (name, _) in operacoes.items():
            print(f" {key}. {name}")
        print(" Q. Sair")
        print("=============================")

        escolha = input("Digite a opção (1/2/3/4/Q): ").upper()

        if escolha == 'Q':
            print("Saindo da calculadora. Até mais!")
            break
        elif escolha in operacoes:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                nome_operacao, operacao = operacoes[escolha]
                resultado = operacao(num1, num2)
                num1_formatado = formatar_numero(num1)
                num2_formatado = formatar_numero(num2)
                resultado_formatado = formatar_numero(resultado) if isinstance(resultado, (int, float)) else resultado
                print(f"\nResultado da {nome_operacao.lower()} entre {num1_formatado} e {num2_formatado} é: {resultado_formatado}")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
        else:
            print("Opção inválida. Por favor, tente novamente.")

        continuar = input("Deseja realizar outra operação? (S/N): ").upper()
        if continuar != 'S':
            print("Saindo da calculadora. Até mais!")
            break

if __name__ == "__main__":
    calculadora()