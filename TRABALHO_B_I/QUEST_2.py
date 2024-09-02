print ("------- Bem vindo a loja de marmitas do Luís Filipe -------")
print ("-------------------------cardápio--------------------------")
print ("-----------------------------------------------------------")
print ("--| Tamanho | Bife Acebolado (BA) | Filé de Frango (FF) |--")
print ("--|    P    |      R$ 16,00       |       R$ 15,00      |--")
print ("--|    M    |      R$ 18,00       |       R$ 17,00      |--")
print ("--|    G    |      R$ 22,00       |       R$ 21,00      |--")
print ("-----------------------------------------------------------")
BA = "Bife Acebolado"
FF = "File de Frango"
total = 0 
while True:
    saborPedido = input("Entre com o sabor desejado (BA/FF): ").upper()
    while saborPedido != "BA" and saborPedido != "FF":
        print("Sabor inválido. Tente novamente\n")
        saborPedido = input("Entre com o sabor desejado (BA/FF): ").upper()
        saborPedido = saborPedido
    tamanhoPedido = input("Entre com o tamanho desejado (P/M/G): ").upper()
    while tamanhoPedido != "P" and tamanhoPedido != "M" and tamanhoPedido != "G":
        print("Tamanho inválido. Tente novamente\n")
        tamanhoPedido = input("Entre com o tamanho desejado (P/M/G): ").upper()
        tamanhoPedido = tamanhoPedido
    if saborPedido == "BA" and tamanhoPedido == "P":
        print ("Você pediu Bife Acebolado tamanho P: R$ 16,00\n")
        total += 16.00
    elif saborPedido == "BA" and tamanhoPedido == "M":
        print ("Você pediu Bife Acebolado tamanho M: R$ 18,00\n")
        total += 18.00
    elif saborPedido == "BA" and tamanhoPedido == "G":
        print ("Você pediu Bife Acebolado tamanho G: R$ 22,00\n")
        total += 22.00
    elif saborPedido == "FF" and tamanhoPedido == "P":
        print ("Você pediu Filé de Frango tamanho P: R$ 15,00\n")
        total += 15.00
    elif saborPedido == "FF" and tamanhoPedido == "M":
        print ("Você pediu Filé de Frango tamanho M: R$ 17,00\n")
        total += 17.00
    elif saborPedido == "FF" and tamanhoPedido == "G":
        print ("Você pediu Filé de Frango tamanho G: R$ 21,00\n")
        total += 21.00
    pedido = input ("Deseja pedir mais alguma coisa ? (S/N): ").upper()
    if pedido == "N":
        print(f"O valor total a ser pago: R${total}")
        break
    else:
        continue
