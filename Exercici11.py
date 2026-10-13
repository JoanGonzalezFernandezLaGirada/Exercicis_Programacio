#Veamos un ejemplo (e11):
'''for n1 in range(3):
 for n2 in range(5):
  print("n1 = " + str(n1) + ", n2 = " + str(n2))'''

#El programa imprime en orden los elementos de la lista 1 (del 0 al 2) y dentro de ella los de la lista 2 (del 0 al 4).
#Con el bucle WHILE:
'''n1 = 0
while n1<3:
 n2 = 0
 while n2<5:
  print("n1 = " + str(n1) + ", n2 = " + str(n2))
 n2 = n2 + 1
 n1 = n1 + 1'''

#Si lo hacemos mezclando los dos tipos de bucles tenemos:
n1 = 0
while n1<3:
 for n2 in range(5):
  print("n1 = " + str(n1) + ", n2 = " + str(n2))
 n1 = n1 + 1
