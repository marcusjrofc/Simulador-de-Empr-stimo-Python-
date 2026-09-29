from datetime import datetime, timedelta

def calcular_idade(data_nascimento_str):

    data_nasc = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    hoje = datetime.now()

    idade = (hoje - data_nasc).days / 365.25
    return idade

def simular_emprestimo():
    tentativas = 0
    limite_tentativas = 3

    print("=== SIMULADOR DE EMPRÉSTIMO ===")

    while tentativas < limite_tentativas:
        try:

            nome = input("\nDigite seu nome: ").strip()
            if len(nome) < 5:
                print("❌ Nome inválido (mínimo 5 caracteres).")
                tentativas += 1
                continue


            cpf = input("Digite seu CPF (apenas números): ").strip()
            if len(cpf) != 11 or not cpf.isdigit():
                print("❌ CPF inválido (deve conter exatamente 11 números).")
                tentativas += 1
                continue


            data_nasc = input("Digite sua data de nascimento (DD/MM/AAAA): ").strip()
            idade = calcular_idade(data_nasc)
            print(f"-> Idade calculada: {idade:.1f} anos")


            valor_emprestimo = float(input("Digite o valor do empréstimo (R$): "))
            if valor_emprestimo <= 0:
                print("❌ Valor do empréstimo inválido.")
                tentativas += 1
                continue


            taxa_juros = float(input("Digite a taxa de juros (%): "))
            if taxa_juros <= 0:
                print("❌ Taxa de juros inválida.")
                tentativas += 1
                continue


            qtd_parcelas = int(input("Digite a quantidade de parcelas: "))
            if qtd_parcelas <= 0:
                print("❌ Número de parcelas inválido.")
                tentativas += 1
                continue


            taxa_decimal = taxa_juros / 100
            valor_juros = valor_emprestimo * taxa_decimal
            montante_total = valor_emprestimo + valor_juros
            valor_parcela = montante_total / qtd_parcelas


            print("\n" + "="*30)
            print(f"Montante Total: R$ {montante_total:.2f}")
            print("="*30)

            hoje = datetime.now()
            for i in range(1, qtd_parcelas + 1):
                data_vencimento = hoje + timedelta(days=30 * i)
                data_formatada = data_vencimento.strftime("%d/%m/%Y")
                print(f"Parcela {i}: R$ {valor_parcela:.2f} - Vencimento: {data_formatada}")


            break

        except ValueError:
            print("❌ Entrada inválida! Verifique se digitou números nos campos corretos.")
            tentativas += 1

        if tentativas >= limite_tentativas:
            print("\n🚨 Você atingiu o limite de tentativas. Tente novamente mais tarde!")


simular_emprestimo()