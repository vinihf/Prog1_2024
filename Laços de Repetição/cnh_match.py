from datetime import date

ano = int(input("Informe seu ano de nascimento:"))
idade = date.today().year - ano
match idade:
    case idade if idade>=18:
        print("Pode ter CNH")
    case _:
        print("Não pode ter CNH")