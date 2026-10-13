#Veamos el primer ejemplo (e9_1):
lista = [1,2,3,4,5,6,7,8,9]
for n in lista:
 print(n)

#también podemos hacerlo con cadenas de texto:
lista = ["ordenador", "teclado", "raton"]
for n in lista:
 print(n)


#Y trabajando con la instrucción range, podremos trabajar con rangos de números: (e9_2)
for n in range(10):
 print(n)
# o de otra manera:
for Numero in range(1,11,1):
 print(Numero)


#Donde (1,11,1) A B C También podemos trabajar con variables, (e9_3)
n=int(input("Número: "))
for x in range(n, n*2):
 print(x)
