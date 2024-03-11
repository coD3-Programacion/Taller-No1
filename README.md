# Taller-No1

## Grupo: CoD3

### Integrantes:

David Alejandro Sotelo Pinzón

David Santiago Hoyos Mateus

Diego Garcés Torres

### 1. Realice el quiz *Python Beginner Quiz* (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).

[![Captura-de-pantalla-2024-03-04-114632.png](https://i.postimg.cc/yNCSjz06/Captura-de-pantalla-2024-03-04-114632.png)](https://postimg.cc/9D1MXKxs)

### 2. Realice un programa que lea tres números reales y determine cuál es el mayor.

```python
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
```
#### Explicación de la solución

*primeramente se especifica el tipo de variable en las 3 variables (enteros), y despues se piden los 3 números. El siguiente paso fue con 3 condicionales evaluar cual número de los 3 era el mayor utilizando tambien 
operadores lógicos y por último tener en cuenta el caso en el que los 3 números sean iguales.

### 3. Realice un programa que lea un número enteros y determine si es par o impar.

```python

```

#### Explicación de la solución

### 4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

```python

```

#### Explicación de la solución

### 5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

```python

#Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número

n=int
m=int
r=int

n = int(input("Escriba el primer número "))
m = int(input("Escriba el segundo número "))
r = int(input("Escriba el tercer número "))

x=n+m

if x>r:
    print("La suma de los 2 primeros números es mayor al tercer número")

elif x<r:
    print("La suma de los 2 primeros números es menor al tercer número")

else:
    print("La suma de los 2 primeros números es igual al tercer número")
```
#### Explicación de la solución

*Se especifica el tipo de variables y se piden al usuario los 3 números, despues se crea una nueva variable llamada "x" la cual es la suma de los 2 primeros números y despues con 3 condicionales y con operadores lógicos se clasifica en una de las 3 situaciones (si la suma de los 2 primeros es mayor, menor o igual al tercer número)

#### Diagrama de flujo

```mermaid
flowchart TD;
  A[Pedir 3 números] -->B
  B[X = primer número + segundo número] --> C{Si X > tercer número}
  C --SI--> D[la suma de los 2 primeros números es mayor al tercero]
  C --NO--> E{Si X < tercer número}
  E --SI--> F[la suma de los 2 primeros números es menor al tercero]
  E --NO--> G[la suma de los 2 primeros números es igual al tercer número]
  D --> H(Fin)
  F --> H(Fin)
  G --> H(Fin)


```

### 6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

```python

```

#### Explicación de la solución

#### Diagrama de flujo

### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python

```

#### Explicación de la solución

### 8. Escriba un programa al que se le ingrese la frecuencia de una onda en *hz* y como salida arroje en que parte del espectro electromagnético se encuentra.

```python

```

#### Explicación de la solución

### 9. Escriba un programa que reciba el nombre en minúsculas de un país de **America** y retorne la ciudad capital, si el país no pertenece al continente debe arrojar *país no identificado*.

```python

```

#### Explicación de la solución

### 10. Escriba un programa que dada una distancia calcule:
+ El tiempo que le tomaría a la luz recorrer la distancia.
+ El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
+ El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
+ El tiempo que le tomaría a Bolt recorrer la distancia.

```python

```

#### Explicación de la solución


#### Diagrama de flujo
