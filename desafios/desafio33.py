print("| COMPRANDO PRODUTO DA LISTA |")
print("-"*40)

produtos = ["Xbox","Controle","Shampoo","Frango Frito","Banana","Sorvete"]
print("Selecione um dos produtos que for te apresentado!")
print("Resposta se deseja comprar com 'sim' ou 'não'!")
for i in produtos:
    print(f"Produto: {i}")
    resposta = input("Digite aqui: ")

    if resposta.lower() == "sim":
        print(f"Você comprou o produto {i}!")
        break

if resposta != "sim":
    print("Você não escolheu nenhum dos produtos disponíveis!")

print("Tenha um ótimo dia")