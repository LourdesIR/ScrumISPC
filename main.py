## Ecuaciones basicas
arr= []

##Ejercicio sumar 3 parametros (la siguiente funcion permite sumar 3 parametros y mas)
def suma(arr):
    suma = 0
    for num in arr:
        suma += num
    print(suma)

# Solo numeros
def ingresar_numeros():
   try:
    n = int(input('Ingrese un numero o ingrese "0" (cero) para salir: '))
    while n != 0:
        arr.insert(0,n)
        n = int(input('Ingrese un numero o ingrese "0" (cero) para salir: '))
    print(arr)
   except:
    print('Solo se permiten numeros, la suma de los numeros es: ')


ingresar_numeros()
suma(arr)