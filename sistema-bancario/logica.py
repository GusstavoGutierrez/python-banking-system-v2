from datetime import datetime

LIMITE_SAQUES_DIARIOS = 3 
LIMITE_TRANSACOES_DIA = 10
AGENCIA = "0001"

usuarios = []
contas = []

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario = filtrar_usuario(cpf)
    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta_usuario(usuario):
    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA,
        "numero": numero_conta,
        "usuario": usuario,
        "saldo": 0.0,
        "extrato": "",
        "numero_saques_diarios": 0,
        "data_ultima_transacao": None,
        "transacoes_hoje": 0,          
        "limite_por_saque": 500.0      
    }
    contas.append(conta)
    print(f"\nConta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}")

def listar_contas_usuario(usuario):
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == usuario["cpf"]]
    if not contas_usuario:
        print("\nUsuário não possui contas.")
        return
    for conta in contas_usuario:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']} | Titular: {conta['usuario']['nome']}")

def selecionar_conta_usuario(usuario):
    contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == usuario["cpf"]]
    if not contas_usuario:
        print("\nUsuário não possui contas. Crie uma conta primeiro!")
        return None
    print("\nContas disponíveis:")
    for conta in contas_usuario:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']}")
    try:
        numero = int(input("Digite o número da conta para logar: "))
    except ValueError:
        print("Número inválido.")
        return None
    for conta in contas_usuario:
        if conta["numero"] == numero:
            print(f"\nConta {numero} logada com sucesso!")
            return conta
    print("Conta não encontrada.")
    return None

def deposito(saldo, extrato, /):
    try:
        valor_str = input("Informe o valor do depósito: ").replace(",", ".")
        valor = float(valor_str)
    except ValueError:
        print("\nOperação falhou! Valor inválido. Tente novamente.")
        return saldo, extrato, False

    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora} - Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
        return saldo, extrato, True
    else:
        print("\nOperação falhou! O valor informado é inválido (deve ser maior que zero).")
        return saldo, extrato, False

def saque(*, saldo, extrato, limite_valor_saque, numero_saques_feitos_hoje, limite_diario_saques):
    try:
        valor_str = input("Informe o valor do saque: ").replace(",", ".")
        valor = float(valor_str)
    except ValueError:
        print("\nOperação falhou! Valor inválido. Tente novamente.")
        return saldo, extrato, numero_saques_feitos_hoje, False

    excedeu_saldo = valor > saldo
    excedeu_limite_por_transacao = valor > limite_valor_saque
    excedeu_limite_saques_diarios = numero_saques_feitos_hoje >= limite_diario_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques_feitos_hoje, False
    elif excedeu_limite_por_transacao:
        print(f"\nOperação falhou! O valor do saque (R$ {valor:.2f}) excede o limite por transação (R$ {limite_valor_saque:.2f}).")
        return saldo, extrato, numero_saques_feitos_hoje, False
    elif excedeu_limite_saques_diarios:
        print(f"\nOperação falhou! Número máximo de saques diários ({limite_diario_saques}) excedido.")
        return saldo, extrato, numero_saques_feitos_hoje, False
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
        numero_saques_feitos_hoje += 1
        print("\nSaque realizado com sucesso!")
        return saldo, extrato, numero_saques_feitos_hoje, True
    else:
        print("\nOperação falhou! O valor informado é inválido (deve ser maior que zero).")
        return saldo, extrato, numero_saques_feitos_hoje, False

def exibir_extrato(saldo, /, *, extrato, usuario=None, conta=None):
    print("\n================ EXTRATO ================\n")
    if usuario and conta:
        print(f"Usuário: {usuario['nome']} | Conta: {conta['numero']}")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================\n")

def sair():
    print("\nObrigado por utilizar nosso sistema bancário!")

def resetar_contadores_diarios(data_ultima_transacao, transacoes_hoje, numero_saques_diarios):
    hoje = datetime.now().date()
    if data_ultima_transacao is None or data_ultima_transacao != hoje:
        return hoje, 0, 0
    return data_ultima_transacao, transacoes_hoje, numero_saques_diarios

def main():
    usuario_logado = None
    conta_logada = None

    MenuUSER = """
[n] Novo usuario
[l] Logar usuario
[s] Sair
=>"""

    menuCONTA = """
[c] Nova conta
[lc] Logar em conta
[l] Listar contas
[v] Voltar
=>"""

    menuACOES = """
[d] Depositar
[s] Sacar
[e] Extrato
[v] Voltar
=>"""

    while True:
        usuario_logado = None
        conta_logada = None
        opcao = input(MenuUSER).strip().lower()

        if opcao == "n":
            criar_usuario()
        elif opcao == "l":
            cpf = input("Informe o CPF do usuário: ").strip()
            usuario = filtrar_usuario(cpf)
            if usuario:
                usuario_logado = usuario
                print(f"\nUsuário {usuario['nome']} logado com sucesso!")
                while True:
                    conta_logada = None
                    op_conta = input(menuCONTA).strip().lower()
                    if op_conta == "c":
                        criar_conta_usuario(usuario_logado)
                    elif op_conta == "lc":
                        conta_logada = selecionar_conta_usuario(usuario_logado)
                        if conta_logada:
                            saldo_conta = conta_logada["saldo"]
                            extrato_conta = conta_logada["extrato"]
                            numero_saques_conta = conta_logada["numero_saques_diarios"]
                            data_ultima_transacao_conta = conta_logada["data_ultima_transacao"]
                            transacoes_hoje_conta = conta_logada["transacoes_hoje"]
                            limite_por_saque_conta = conta_logada["limite_por_saque"]

                            while True:
                                data_ultima_transacao_conta, transacoes_hoje_conta, numero_saques_conta = resetar_contadores_diarios(
                                    data_ultima_transacao_conta, transacoes_hoje_conta, numero_saques_conta
                                )
                                op_acao = input(menuACOES).strip().lower()

                                if op_acao == "d":
                                    if transacoes_hoje_conta >= LIMITE_TRANSACOES_DIA:
                                        print("\nLimite diário de transações atingido!")
                                        continue
                                    
                                    novo_saldo, novo_extrato, sucesso_deposito = deposito(saldo_conta, extrato_conta)
                                    if sucesso_deposito:
                                        saldo_conta = novo_saldo
                                        extrato_conta = novo_extrato
                                        transacoes_hoje_conta += 1
                                        data_ultima_transacao_conta = datetime.now().date()
                                elif op_acao == "s":
                                    if transacoes_hoje_conta >= LIMITE_TRANSACOES_DIA:
                                        print("\nLimite diário de transações atingido!")
                                        continue
                                    novo_saldo, novo_extrato, novo_numero_saques, sucesso_saque = saque(
                                        saldo=saldo_conta,
                                        extrato=extrato_conta,
                                        limite_valor_saque=limite_por_saque_conta,
                                        numero_saques_feitos_hoje=numero_saques_conta,
                                        limite_diario_saques=LIMITE_SAQUES_DIARIOS,
                                    )
                                    if sucesso_saque:
                                        saldo_conta = novo_saldo
                                        extrato_conta = novo_extrato
                                        numero_saques_conta = novo_numero_saques
                                        transacoes_hoje_conta += 1
                                        data_ultima_transacao_conta = datetime.now().date()
                                elif op_acao == "e":
                                    print(f"\nUsuário: {usuario_logado['nome']} | Conta: {conta_logada['numero']}")
                                    exibir_extrato(saldo_conta, extrato=extrato_conta)
                                elif op_acao == "v":
                                    conta_logada["saldo"] = saldo_conta
                                    conta_logada["extrato"] = extrato_conta
                                    conta_logada["numero_saques_diarios"] = numero_saques_conta
                                    conta_logada["data_ultima_transacao"] = data_ultima_transacao_conta
                                    conta_logada["transacoes_hoje"] = transacoes_hoje_conta
                                    break
                                else:
                                    print("\nOpção inválida.")
                    elif op_conta == "l":
                        listar_contas_usuario(usuario_logado)
                    elif op_conta == "v":
                        break
                    else:
                        print("\nOpção inválida.")
            else:
                print("\nUsuário não encontrado.")
        elif opcao == "s":
            sair()
            break
        else:
            print("\nOpção inválida.")
