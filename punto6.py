x = input("ingrese una letra para determinar si es vocal o consonante: ")
if ord(x) == 65 or ord(x) == 69 or ord(x) == 73 or ord(x) == 79 or ord(x) == 85 or ord(x) == 97 or ord(x) == 101 or ord(x) == 105 or ord(x) == 111 or ord(x) == 117:
    print(x, " es una vocal")
elif ord(x) <= 64 or ord(x) >= 123:
    print(x, " es un simbolo")
else:
    print(x, " es una consonante")
    