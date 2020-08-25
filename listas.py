# Concatenar
a=[1,2]
b=[7,8]
a + b --> [1,2,7,8]

# Aumenta la misma lista:
a=[1,7]
a * 2 —> [1,7,1,7]

# Añadir elemento al final de la lista:
a=[1]
a.append(7)=[1,7]

# Eliminar elemento al final de la lista:
a=[1,7]
b=a.pop()
a=[1]

# Eliminar elemento por su posicion:
a=[3,7,9]
b=a.pop(1) #posicion 2
a=[3,9]

# Elimina el elemento por su valor
a=[4, 6, 8]
a.remove(6)
a=[4, 8]

# Ordenar lista de menor a mayor
a=[3,8,1]
a.sort() —> [1,3,8]

# sorted() # no existe ese atributo

# Creacion de listas en un rango determinado
 a=(list(range(0,10,2))) ·#--> Crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]

# Valor del tamaño de la lista
a=[0,2,4,6,8]
len(a)=5