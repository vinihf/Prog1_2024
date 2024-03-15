x = 10
match x:
        case x if x > 0:
            print("O valor é positivo")
        case x if x < 0:
            print("O valor é negativo")
        case x if x == 0:
            print("O valor é zero")
        case _:
            print("O valor não é classificado dentro de qualquer intervalo")