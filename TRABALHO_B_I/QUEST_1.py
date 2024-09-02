print("Bem vindo a loja do Luís Filipe Pereira Francisco.")
""" recebendo variaveis """
valorDoPedido = float(input("Entre com o valor do pedido:R$ "))
quantidadeParcelas = float(input("Entre com a quantidade de parcelas: "))
valorDaParcela = float
"""Area dos calculos percentuais"""
if quantidadeParcelas < 4 :
    valorDaParcela=valorDoPedido*(1+(0/100))/quantidadeParcelas
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    valorDaParcela=valorDoPedido*(1+4/100)/quantidadeParcelas
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    valorDaParcela=valorDoPedido*(1+8/100)/quantidadeParcelas
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    valorDaParcela=valorDoPedido*(1+16/100)/quantidadeParcelas
else:
    valorDaParcela=valorDoPedido*(1+32/100)/quantidadeParcelas
"""Saídas"""
print(f"O valor das parcelas é de:{valorDaParcela:.2f}")
print(f"O valor total tarcelado é de: {valorDaParcela*quantidadeParcelas:.2f}")