# Tempo Estimado de Entrega
nomeRestaurante = input()
tempoEstimadoEntrega = int(input())
print(f"\nO restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos.")

# Calcular o Preço Final de um Pedido
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())
valorTotalDosHamburgueres = valorHamburguer * quantidadeHamburguer
valorTotalDasBebidas = valorBebida * quantidadeBebida
precoTotalDoPedido = valorTotalDosHamburgueres + valorTotalDasBebidas
trocoNecessario = valorPago - precoTotalDoPedido
print(f"O preço final do pedido é R$ {precoTotalDoPedido:.2f}. Seu troco é R$ {trocoNecessario:.2f}.")

# Ganhe uma Sobremesa Especial!
valorPedido = int(input())
if valorPedido >= 50:
  print("Parabens, você ganhou uma sobremesa gratis!")
else:
  print("Que pena, você nao ganhou nenhum brinde especial.")

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
