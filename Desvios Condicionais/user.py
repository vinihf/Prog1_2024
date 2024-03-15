user = input("Informe o user:")
password = input("Informe a password:")
if user == "admin" or password == "123":
    print("Usuário autorizado.")
else:
    print("Usuário não autorizado. Senha incorreta.")