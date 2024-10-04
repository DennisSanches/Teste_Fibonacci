import json


# Função 1: Cálculo da variável SOMA
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K

    print(f"Resultado da variável SOMA: {SOMA}")


# Função 2: Verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci():
    numero = int(input("Informe um número: "))
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero or a == numero:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")


# Função 3: Faturamento diário: menor, maior e dias acima da média
def calcular_faturamento():
    dados_faturamento = """
    {
        "faturamento_diario": [200, 150, 0, 0, 230, 0, 0, 400, 120, 0, 300, 180, 250, 0, 100, 340, 0, 200]
    }
    """
    dados = json.loads(dados_faturamento)
    faturamento = [dia for dia in dados['faturamento_diario'] if dia > 0]  # Ignorando dias sem faturamento

    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    dias_acima_media = len([dia for dia in faturamento if dia > media_mensal])

    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")


# Função 4: Percentual de faturamento por estado
def calcular_percentual_faturamento():
    faturamento_estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    faturamento_total = sum(faturamento_estados.values())

    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"Estado: {estado} - Percentual: {percentual:.2f}%")


# Função 5: Inverter uma string
def inverter_string():
    string = input("Informe uma string: ")
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    print(f"String invertida: {invertida}")


# Menu de opções
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Cálculo da variável SOMA")
        print("2. Verificar se um número pertence à sequência de Fibonacci")
        print("3. Calcular menor, maior faturamento e dias acima da média")
        print("4. Calcular percentual de faturamento por estado")
        print("5. Inverter uma string")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            calcular_soma()
        elif opcao == '2':
            pertence_fibonacci()
        elif opcao == '3':
            calcular_faturamento()
        elif opcao == '4':
            calcular_percentual_faturamento()
        elif opcao == '5':
            inverter_string()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


# Executar o menu
if __name__ == "__main__":
    menu()
