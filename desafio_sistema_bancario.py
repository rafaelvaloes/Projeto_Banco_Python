
saldo = 500
valor_limite_saque = 500
extrato = []
numero_saques = 0
QTD_LIMITE_SAQUES = 3


menu = """
--------------------------------
    Selecione a Opção Desejada:
    [1] - Saque
    [2] - Deposito
    [3] - Extrato
    [0] - Sair
--------------------------------
    => """

print("Bem vindo ao Nosso Banco!")
while True:

    opcao = int(input(menu))

    if opcao == 1:
        print("\nVoce selecionou a opção Saque.")
        valor_saque = float(input("\nDigite quanto quer Sacar: "))
        
        if valor_saque < saldo:

            if numero_saques < QTD_LIMITE_SAQUES:

                if valor_saque > 0 and valor_saque == round(valor_saque, 2):

                    if valor_saque < valor_limite_saque:
                        saldo -= valor_saque
                        numero_saques += 1
                        print(f"\nTransação Realizada: Foram sacados R${valor_saque:.2f}.")
                        extrato.append(f"Saque realizado: R${valor_saque:.2f}.")
                    else:
                        print(f"\nTransação não realizada: O valor limite para saques é de R$500,00.\n")
                
                else:
                    print("\nTransação não realizada: Valor Invalido.")

            else:
                print("\nTransação não realizada: Foi excedida a quatidade diária de saques.")

        else:
            print("\nTransação não realizada: O Valor Selecionado é maior que seu Saldo.")
    
    elif opcao == 2:
        print("\nVoce selecionou a opção Deposito.")
        valor_deposito= float(input("\nDigite quanto quer Depositar: "))
        
        if valor_deposito > 0 and valor_deposito == round(valor_deposito, 2):

            saldo += valor_deposito
            print(f"\nTransação Realizada: Foram depositados R${valor_deposito:.2f}.")
            extrato.append(f"Deposito realizado: R${valor_deposito:.2f}.")
        
        else:
            print("\nTransação não realizada: Valor Invalido.")

    elif opcao == 3:
        print("\nMostrando Extrato:")

        for operacao in extrato:
            print(operacao)

        print(f"\nSeu saldo atual é de R${saldo:.2f}.")

    elif opcao == 0:
        print("Obrigado por usar o nosso Banco!")
        break

    else:
        print("Opcao invalida, digite um numero de nosso menu: ")