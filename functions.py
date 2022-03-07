# Creación de funciones: Para crear funciones se debe escribir
# def nombre_funcion(parametros):
## Importante mantener espacios
nombre = "Andrés Felipe Insuasty Chamorro"
def imprimir_nombre(nombre):
    print(nombre)
imprimir_nombre(nombre)

def filter_even(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    return result_list
print(filter_even([3,4,6]))
