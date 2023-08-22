# Gerenciamento de Pedidos de Comida Online
def main():
    n = int(input())
    i = 0
    total = 0
 
    while i != n:
        i += 1
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
    choice = input()
    if choice == '10%':
        total = total - (total * 10/100)
        print(f"Valor total: {total:.2f}")
    elif choice == '20%':
        total = total - (total * 20/100)
        print(f"Valor total: {total:.2f}")

 
main()