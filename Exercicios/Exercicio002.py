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