#PRUEBA: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.#
print("Hola mundo!")

#ejercicio2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.#
name=input("Ingrese su nombre: ")
print("hola, ", name)

#ejercicio3: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.#
name=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido ")
edad=input("Ingrese su edad ")
Residencia=input("Ingrese su lugar de residencia ")

print("Mi nombre es", name, "mi apellido es ",apellido, "tengo ",edad, "años y vivo en", Residencia)

#ejercicio4: Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.#
radio=float(input("Ingrese el radio de un circulo: "))
area=3.14*radio**2
perimetro=2*3.14*radio

print("El area del circulo es ", area, "y el perimetro es ", perimetro)

#ejercicio5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.#
segundos=int(input("Ingresar por favor la cantidad de segundos "))
if segundos>3600:
    horas=segundos//3600
    print("La cantidad de horas es:", horas)
else:
    print ("con los datos ingresados no se puede calcular una hora completa")

#ejercicio6:Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.#
numero=int(input("Por favor ingresar un numero "))

for i in range(1,11):
    print(numero, "x", i, "=", numero * i)
    
#ejercicio7:Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.#
num1=int(input("por favor ingresar un numero "))
num2=int(input("por favor ingresar un segundo numero "))

suma=num1+num2
division=num1/num2
multiplicacion=num1*num2
resta=num1-num2

print("la suma de ambos numeros es: ", suma)
print("la división de del primer numero por el segundo numero es: ", division)
print("la multiplicacion de ambos numeros es: ", multiplicacion)
print("la resta del primer numero menos el segundo es: ", resta)

#ejercicio8: Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.#
Peso=float(input("por favor ingrese su peso "))
Altura=float(input("por favor ingrese su altura "))

IMC=Peso/(Altura**2)

print("Su indice de Masa Corporal es:", IMC)

#ejercicio9: Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.#
TempC=float(input("Ingresar por favor qué temperatura hace en grados celsius "))
TempF=(TempC*1.8)+32

print("La temperatura ingresada en grados celsius al pasar a farenheit es: ", TempF)

#ejercicio10: Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.#
Num1=int(input("Por favor ingresar el primer numero "))
Num2=int(input("Por favor ingresar un segundo numero "))
Num3=int(input("Por favor ingresar un tercer numero "))

Promedio=(Num1+Num2+Num3)/3
print("El promedio de los tres numeros es: ", Promedio)
