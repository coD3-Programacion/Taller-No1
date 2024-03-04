n=int
m=int
r=int

n = int(input("Escriba el primer número "))
m = int(input("Escriba el segundo número "))
r = int(input("Escriba el tercer número "))

if n>m>r or n>r>m:
    print("El número mayor es " + str(n))

elif m>n>r or m>r>n:
    print("El número mayor es " + str(m))

elif r>m>n or r>n>m:
    print("El número mayor es " + str(r))

else:
    print("Los números son iguales")