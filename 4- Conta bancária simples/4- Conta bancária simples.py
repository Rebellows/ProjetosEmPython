conta = 0
contsaque = 3
extrato = ""
while True:
    a = int(input("\nO que deseja fazer?\n[1] Depositar\n[2] Sacar\n[3] Extrato\n[0]Cancelar\nDigite aqui: "))
    if a == 1:
        valor = float(input("\nQual o valor deseja depositar? "))
        if valor < 100:
            print("\nO valor deve ser no mínimo R$100,00")

        else:
            conta += valor
            extrato += f"Depósito no valor de R${valor:.2f}\n"

    elif a == 2:
        if contsaque != 0:
            saque = float(input("\nQuanto você deseja sacar? Lembre-se,\nvocê só pode fazer 3 saques diários\ncom o valor máximo de R$500,00\nDigite aqui: "))
            if saque > conta:
                print("\nVocê não pode sacar mais do que tem.")
            elif saque > 500:
                print("\nVocê não pode sacar mais que R$500,00")
            else:
                conta -= saque
                contsaque -= 1
                extrato += f"Saque no valor de R${saque:.2f}\n"
        else:
            print("\nVocê já fez o limite máximo de saques diários.")
    elif a == 3:
        print("|------------------------------|\n|-----------Extrato:-----------|\n|------------------------------|\n")
        print(extrato)
        print(f"\nO valor atual da conta é R${conta}")
        print("|------------------------------|")
    elif a == 4:
        break
    else:
        print("\nOperação inválida, favor inserir o valor desejado novamente.")
