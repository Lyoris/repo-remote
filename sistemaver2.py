import os

# Estilo ANSI (cores)
AZUL = '\033[94m'
VERDE = '\033[92m'
AMARELO = '\033[93m'
VERMELHO = '\033[91m'
RESET = '\033[0m'

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def titulo(texto):
    print(f"\n{AZUL}{'='*40}\n{texto.center(40)}\n{'='*40}{RESET}")

def depositar(valor, /, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"{VERDE}Depósito: R${valor:.2f}{RESET}")
        print(f"{VERDE}Depósito realizado! Novo saldo: R${saldo:.2f}{RESET}")
    else:
        print(f"{VERMELHO}Valor inválido para depósito.{RESET}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print(f"{VERMELHO}Saldo insuficiente.{RESET}")
    elif valor > limite:
        print(f"{VERMELHO}Limite por saque excedido (máximo R${limite:.2f}).{RESET}")
    elif numero_saques >= limite_saques:
        print(f"{VERMELHO}Limite diário de saques atingido ({limite_saques} saques).{RESET}")
    elif valor <= 0:
        print(f"{VERMELHO}Valor inválido.{RESET}")
    else:
        saldo -= valor
        extrato.append(f"{VERMELHO}Saque: R${valor:.2f}{RESET}")
        numero_saques += 1
        print(f"{VERDE}Saque realizado! Novo saldo: R${saldo:.2f}{RESET}")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    titulo("EXTRATO")
    if extrato:
        for item in extrato:
            print(item)
    else:
        print(f"{AMARELO}Nenhuma movimentação registrada.{RESET}")
    print(f"\n{AZUL}Saldo atual: R${saldo:.2f}{RESET}")
    print(f"{AZUL}{'='*40}{RESET}")

def criar_usuario(usuarios):
    titulo("CRIAR USUÁRIO")
    cpf = input("CPF (somente números): ")
    if any(u["cpf"] == cpf for u in usuarios):
        print(f"{VERMELHO}Usuário com este CPF já existe.{RESET}")
        return usuarios
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (rua, nº - bairro - cidade/UF): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"{VERDE}Usuário criado com sucesso!{RESET}")
    return usuarios

def criar_conta(agencia, numero_conta, usuarios):
    titulo("CRIAR CONTA")
    cpf = input("CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)
    if usuario:
        print(f"{VERDE}Conta criada com sucesso!{RESET}")
        return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}
    else:
        print(f"{VERMELHO}Usuário não encontrado.{RESET}")
        return None

# Programa principal
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

menu = f"""
{AMARELO}========== MENU =========={RESET}
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Sair
{AMARELO}==========================={RESET}
=> """

while True:
    opcao = input(menu)
    
    if opcao == "1":
        limpar()
        titulo("DEPÓSITO")
        valor = float(input("Valor do depósito: R$"))
        saldo, extrato = depositar(valor, saldo, extrato)
        
    elif opcao == "2":
        limpar()
        titulo("SAQUE")
        valor = float(input("Valor do saque: R$"))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "3":
        limpar()
        exibir_extrato(saldo, extrato)

    elif opcao == "4":
        limpar()
        usuarios = criar_usuario(usuarios)

    elif opcao == "5":
        limpar()
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "6":
        limpar()
        print(f"{AZUL}Obrigado por usar nosso sistema!{RESET}")
        break

    else:
        print(f"{VERMELHO}Opção inválida. Tente novamente.{RESET}")