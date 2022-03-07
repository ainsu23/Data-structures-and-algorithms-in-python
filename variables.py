# Variables se crean con un igual
nombre = "Andrés Felipe Insuasty Chamorro"
edad = 31
masculino = True

# Existen 2 tipos de variables: Primitivas y containers
# Para conocer el tipo de variable usar función type()
print(type(edad))
print(type(masculino))
## Primitivas: Enteros, decimal, boolean, strings, none
### Existen varios métodos o funciones asociadas al tipo string.
#### nombre_variable.lower() o
#### introducir variables en texto con {}, parecido a glue:
print(nombre.lower())
print("hola, mi nombre es: {}. Mi edad es: {}".format(nombre, edad))

## Containers: Listas, tuplas, diccionarios.
### Listas se crean con corchetes [], métodos asociados: lista.append ,
### lista.remove, lista.insert , lista.pop, lista.copy
frutas = ["fresa", "mango", "pera", "manzana"]
print("Frutas: {}".format(frutas))

### Tuplas: Colección de valores ordenadas, similar a una lista. Sin embargo,
### las tuplas no puede ser modificadas después de su creación, es decir, no es
### posbile adicionar, eliminar, o modificar un valor en tuplas. A este tipo de
### estructura de datos se le llaman inmutables. Una tupla es una lista inmutable.
### Se crean con ()
frutas_tuplas = ("fresa", "mango", "pera", "manzana")

### Diccionarios: Colección de items desordenados. Cada item almacenado en un
### diccionario tiene un key and value se crean con {}. Muy parecido a como
### se almacenan las listas en formatos JSON.
comida = {
        "frutas" : frutas,
        "carne" : ["cerdo", "pollo"]
        }
print(comida)
