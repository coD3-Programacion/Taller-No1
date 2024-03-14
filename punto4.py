print("ingrese un numero para determinar si es multiplo de un segundo numero")
x : float = float(input("ingrese un numero: "))
y : float = float(input("ingrese un numero: "))
if x%y==0:
    print(x, " es multiplo de ", y)
else:
    print(x, " no es multiplo de ", y)
    