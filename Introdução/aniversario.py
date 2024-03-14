import datetime

ano_nascimento = int(input("Informe o ano do seu nascimento:"))
idade = datetime.date.today().year - ano_nascimento
print(f'Você tem {idade} anos.')