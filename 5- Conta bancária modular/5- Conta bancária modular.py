def func_saque(*, saque, conta, extrato, contsaque):
    if contsaque != 0:
        if saque > conta:
            print("\nVocê não pode sacar mais do que tem.")
        elif saque > 500:
            print("\nVocê não pode sacar mais que R$500,00.")
        else:
            conta -= saque
            contsaque -= 1
            extrato += f"Saque no valor de R${saque:.2f}\n"
            print("\nSaque realizado.")
    else:
        print("\nVocê já excedeu o limite de saques diário.")
    return conta, extrato


def func_deposito(valor, conta, extrato, /):
    if valor > 0:
        conta += valor
        extrato += f"Depósito no valor de R${valor:.2f}\n"
        print("\nDepósito realizado.")
    else:
        print("\nO valor digitado é inválido.")
    return conta, extrato


def func_extrato(conta, /, *,extrato):
    print("\n================ EXTRATO ================")
    print(extrato)
    print(f"\nO valor atual da conta é R${conta}.")
    print("=========================================")
    
    
def func_usuario(usuarios):
    cpf = int(input("\nInforme o CPF (apenas números): "))
    usuario = func_filusuario(cpf, usuarios)
    if usuario:
        print("\nJá existe um usuário cadastrado com esse CPF.")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nUsuário criado.")
    
    
def func_filusuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def func_novaconta(numero_conta, cpf, usuarios):
    agencia = "0001"
    usuario = func_filusuario(cpf, usuarios)
    if usuario:
        print("\nConta criada.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\nNão é possível criar conta de um usuário inexistente.")
    
    
def func_listconta(contas):
    for cont in contas:
        linha = f"\nAgência: {cont['agencia']}\nC/C: {cont['numero_conta']}\nTitular: {cont['usuario']['nome']}"
        print(linha)      
 
        
def func_menu():
    menu = int(input("\n================= MENU! =================\n\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Nova conta\n[5] Listar contas\n[6] Novo usuário\n[0] Sair\n\nDigite aqui: "))
    print("\n=========================================")
    return menu


def main():
    conta = 0
    extrato = ""
    contsaque = 3
    usuarios = []
    contas = []
    numero_conta = 1
    while True:
        op = func_menu()
        if op == 1:
            valor = float(input("\nInforme o valor do depósito: "))
            conta, extrato = func_deposito(valor, conta, extrato)
        elif op == 2:
            saque = float(input("\nQuanto você deseja sacar? Lembre-se,\nvocê só pode fazer 3 saques diários\ncom o valor máximo de R$500,00\nDigite aqui: "))
            conta, extrato = func_saque(saque=saque, conta=conta, extrato=extrato, contsaque=contsaque)
        elif op == 3:
            func_extrato(conta, extrato=extrato)
        elif op == 4:
            cpf = int(input("\nDigite seu CPF (apenas números): "))
            cont = func_novaconta(numero_conta, cpf, usuarios)
            numero_conta += 1
            if cont:
                contas.append(cont)
        elif op == 5:
            func_listconta(contas)
        elif op == 6:
            func_usuario(usuarios)
        elif op == 0:
            break
        else:
            print("\nO valor digitado não é válido.")
            

main()
