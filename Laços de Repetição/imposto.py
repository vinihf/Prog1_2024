price = float(input("Informe o valor do produto:"))

match price:
    case price if price <=50.0:
        print(f'O preço é de ${price:2.2f}, isento de imposto')
    case price if price >50.0:
        new_price = price+(price*0.6)
        print(f'O preço é de ${new_price:2.2f}, com 60% de imposto')
    case _:
        print("Valor impossível de verificar.")