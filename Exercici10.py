#Este bucle está destinado a situaciones donde no sabemos cuántas veces se debe repetir un bucle. La sintaxis sería la siguiente (e10):
i = 0
while i<10:
 print(i)
 i = i + 1
#A= Primer número a imprimir
#B= Rango de números
#C= Intervalo entre números a imprimir

#Si hacemos que dependa de una variable de entrada:
continuar = True
while continuar:
 valor = int(input("Introduce un entero superior a 100: "))
 if valor>100:
  continuar = False
print("Programa acabado")