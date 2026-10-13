#Prueba este programa (e8_1):
'''numero = int(input("Escribe un número del 1 al 10: "))
if numero>10:
 print("¡El numero que has escrito es mayor que 10!")
print("Has escrito el numero " + str(numero))'''

#En este otro ejemplo (e8_2) vamos a ver cuándo hay una primera alternativa:
'''Numero1 = int(input("Introduce el número 1:"))
Numero2 = int(input("Introduce el número 2:"))
if Numero1 == Numero2:
 print("Son iguales")
else:
 print("Son diferentes")'''

#En el tercer caso, tendremos más de una alternativa (e8_3):
numero1 = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
if numero1>numero2:
 print("¡El primer número es mayor que el segundo!")
elif numero1==numero2:
 print("¡Ambos número son iguales!")
else:
 print("¡El primer número es menor que el segundo!")