# Identificando Pedidos Veganos
numPedidos = int(input())
i = 0

pedido = ""

while i != numPedidos:
    prato = input()
    calorias = int(input())
    ehVegano = input()
    i += 1
    if ehVegano == 'n':
        pedido += f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias\n"
    elif ehVegano == 's':
        pedido += f"\nPedido {i}: {prato} (Vegano) - {calorias} calorias"
    else:
        print("Pedido inválido.")

print(pedido)