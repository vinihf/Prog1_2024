dev_lang = input("Informe qual é a linguagem de Programação:")

match dev_lang:
    case "Java" | "PHP" | "Python" | "Javascript":
        print("Esta linguagem é estudada no curso de ADS")
    case _:
        print("Aprender sempre é possível.")