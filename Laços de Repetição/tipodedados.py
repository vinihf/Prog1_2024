dado = 1

match dado:
    case str(dado):
        print("É string")
    case int(dado):
        print("É int")
    case float(dado):
        print("É float")
    case _:
        print("Tipo não reconhecido.")

