menu = """

    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [4] Sair

    => """
    
saldo = 0
limite = 500
extrato = []
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
limite_de_saque = 0
saque = 0
while True:
    opcao = input(menu)
    
    if opcao == "1":
        print("Deposito")
        deposito =float(input('digite o valor do deposito: '))
        saldo += deposito
        print(f'Seu saldo atual é de {saldo}')
        extrato.append(f"Depósito no valor de R${saldo}")
    elif opcao == "2":
        saque =float(input('digite o valor do saque: '))
        if saque <= 500:
            saldo -= saque
            numero_de_saques += 1
            limite_de_saque = LIMITE_DE_SAQUES - numero_de_saques
            extrato.append(f"Saque no valor de R${saque}")
            saque += saque
        if saque >= 500:
            print('O valor excede o maximo estabelecido [R$500]')
        if saque >= 1500:
            print('Voce excedeu o limite de saque diarip, tente vamente amanhã!')
        elif numero_de_saques <= 0:
            print('Todos os 3 saques diarios foram gastos.')
    elif opcao == "3":
        print("\nextrato")
        for l in extrato:
            print(l)
        
    elif opcao == "4":
        print("encerrando programa...")
        break
    elif limite_de_saque <= 0: 
        print