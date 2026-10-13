lista = ["ordenador","teclado","raton"]
print(lista)

lista = ["ordenador","teclado","raton"]
print(len(lista))
print(lista[0])
print(lista[1])
print(lista[2])


listaoriginal = ["ordenador","teclado","raton"]
listanueva = ["monitor","impresora","altavoces"]
listafinal = listaoriginal + listanueva
print(listafinal)


lista = ["ordenador","teclado","raton"]
print(lista)
lista = lista + ["mesa"]
print(lista)

lista = ["ordenador","teclado","raton"]
print(lista)
lista[0] = "monitor"
lista[1] = "impresora"
lista[2] = "altavoces"
print(lista)

lista = ["ordenador","teclado","raton"]
print(lista)
del lista[1]
print(lista)

lista = ["ordenador","teclado","raton", ["tarjeta de sonido" ,"micro" ,"altavoces"]]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[3][2])

tupla = ("ordenador","teclado","raton")
print(tupla)
print(len(tupla))
print(tupla[0])
print(tupla[1])
print(tupla[2])

mesestraducidos = {"Enero" : "January",
 "Febrero" : "February",
 "Marzo" : "March",
 "Abril" : "April",
 "Mayo" : "May",
 "Junio" : "June",
 "Julio" : "July",
 "Agosto" : "August",
 "Septiembre" : "September",
 "Octubre" : "October",
 "Noviembre" : "November",
 "Diciembre" : "December"}
print(mesestraducidos["Noviembre"])
print(mesestraducidos["Mayo"])