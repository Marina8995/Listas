#Declarar lista

miLista=["Maria", "Pepe", "Marta", "Antonio"]

#El primer elemeno de la lista es el 0, no el 1
#Imprimir lista
print(miLista[:])

#Imprimir un elemento
print(miLista[2])
print(miLista[3])

#En negativo empieza a contar desde el final de la lista. En este caso desde el 1, no el 0
print(miLista[-3])

#Para acceder a una porción de la lista
print(miLista[0:3])
#El 0 está incluido, el 3 no

#Si no ponemos nada al principio o al final:
print(miLista[:3])
print(miLista[2:])

#Agregar elemento al final de la lista
miLista.append("Sandra")
print(miLista[:])

#Agregar elemento según posición en la lista
miLista.insert(2,"Sandra")
print(miLista[:])

#Agregar más de un elemento a la lista

miLista.extend(["Sandra", "Ana", "Lucía"])
print(miLista[:])

#Para saber en qué índice está un elemento de la lista
print(miLista.index("Antonio"))

#Para saber si un elemento se encuentra en la lista
print("Pepe" in miLista)
print("Julia" in miLista)

#Eliminar un elemento de la lista
miLista.remove("Ana")
print(miLista[:])

#Eliminar el último elemento de la lista
miLista.pop()
print(miLista[:])

#Concatenar listas (suma)
miLista=["Maria", 5, True, 78.35]
miLista2=["Sandra", "Lucía"]
miLista3=miLista+miLista2

print(miLista3[:])

#El operador * para repetición
miLista=["Maria", 5, True, 78.35] * 3

print(miLista[:])