# Alumno: Mauricio Nápoles Navarro


# 1) ¿Cuáles son los dos valores del tipo de datos booleano? ¿Cómo se escriben?

# Existen dos tipos de valores booleanos 'sí' y 'no' en python los identificamos como 'True' y 'False'.


# 2)  ¿Cuáles son los tres operadores booleanos?

# En python existen 3 operadores booleanos, los identificamos cómo: AND, OR & NOT.


# 3) Escriba una rutina que genere todas las tablas de verdad de cada operador booleano 
# (es decir, cada combinación posible de valores booleanos para cada  operador). 
# A continuación se muestra un ejemplo para el operador or.

booleanos = [False, True]

# Tabla de verdad de OR

print('x\ty\tx or y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x or y)

# Tabla de verdad de AND

print('x\ty\tx and y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x and y)

#Tabla de verdad de NOT

print('x\ty\tx not y')
print('-'*22)
for x in booleanos:
    for y in booleanos:
        print(x, y, x not y)


# 4) ¿Cuáles son los seis operadores de comparación? 

# Los operadores de comparación en python son: 
x != y     # x no es igual a y
x > y      # x es mayor que y
x < y      # x es menor que y
x >= y     # x es mayor o igual que y
x <= y     # x es menor o igual que y


# 5) ¿Cuál es la diferencia entre el operador igual y el operador de asignación?

# La diferencia entre estos operadores es que el primero, el operador igual se escribe como '==', el nos sirve para comparar dos 
# objetos en nuestro código, ejemplo: 

print (4==4)

# Con esto estoy pidiendo que se compare y me diga si 4 es igual a 4.

# En el caso del operador de asignación, se escribe cómo '=' y nos sirve para asignar un nombre a algún objeto y hacerlo una variable,
# ejemplo: 

Variable1 = ('Hola', 'Adios')

#Lo que hice fue declarar la variable 'Variable1' y asignarle el valor de una cadena que contiene las palabras 'Hola' y 'Adiós'.


# 6) Una condición normalmente la usamos despues de poner, ya sea un 'if', 'while' o 'for'. La condición sirve para denortar que es lo 
# que queremos hacer después de la palabra reservada que hayamos escrito anteriormente, ejemplo: 

if (4>1):    # En este caso, (4<1) es nuestra condición para ejecutar el if que acabamos de poner.
	print ('Es verdad')

# 7) ¿Qué puede hacer si su programa está atascado en un bucle infinito?

#La solución más rápida a este problema sería presionar la combinación de teclas 'ctl + c', lo cuál detiene el proceso. Sin embargo, 
#Una forma más precisa de acabar con esto, en linux, es abriendo una terminal y presionando la combinación de 'k + ID del proceso'.


# 8) ¿Cuál es la diferencia entre romper y continuar?

# La instrucción romper, la cual se escribe 'break', sirve para interrumpir un loop que haya sido generado por un for que hayamos puesto 
# antes, ejemplo:

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Loop roto")
        break
    i += 1

# El punto aquí, es que nuestro loop se romperá cuando la variable i sea igual a 4.

# La instrucción continuar, se escribe 'continue', funciona en un bucle poniendo una condición, la declaración se saltará dicha condición y 
# continuara con el bucle. Ejemplo: 

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

# Lo que hacemos es, de una colección de números, saltarnos 1 y 4 e imprimir los demás. 

# Estas declaraciones sólo sirven para los bucles. 


# 9) ¿Cuál es la diferencia entre rango (10), rango (0, 10) y rango (0, 10, 1) en un bucle for? 

# Los rangos sirven para limitar las iteraciones que va a tener nuestro bucle. 

# range(10) toma 10 iteraciones consecutivas que, en este caso sería desde 0 hasta 9.

# range(0, 10) toma iteraciones consecutivas desde 0 y hasta 9, la diferencia con el primero es que podemos definir el rango y ponerlo, 
# por ejemplo de 1 a 10 poniendo range(1,11).

#range(0,10,1) toma iteraciones desde 0 y hasta 9 saltando de una en una cada iteración, la diferencia sería que podemos modificar el 
#salto poniendo por ejemplo range(0, 13, 2) y así haría iteraciones de 0 hasta 12 saltando de dos en dos. 


# 10) Escribe un programa que calcule los primeros n números usando un bucle for

s = 0
n = int(input("Dame un número  "))

for i in range (1, n+1):
	s = s+i
print("La suma de tu número es", s)

# 10.1) Luego escribe un programa equivalente que imprima los números del 1 al 10 usando un bucle while. 

suma = 0 
i = 0 

while i<11:
    suma = suma + i
    print(suma)
    i = i + 1


# 11) Escribe un programa que calcule los primeros N términos de la serie de fibonacci.

print("Calculo hasta el termino que quieras de la sucesión de Fibonacci")
print()

n = int(input("¿Hasta qué término quieres ver? Tu respuesta: "))
print()

a, b = 0,1

for i in range(n):
    print(a, end='\t')
    a,b = b, a+b


# 12) Escribe un programa que calcule el factorial de un número N.

n = int(input("Dame un número y cualculo su factorial. Tu respuesta: "))

m = 1

for i in range(n):
    m = m * (i+1)
    
print("Su factorial es:", m)
