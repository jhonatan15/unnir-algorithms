class Pila: 
    def __init__(lista): 
        lista.elements = []

    def print_list(lista):
        return (f"Los elementos de la pila son: {lista.elements}")
    
    def push(lista, datos): 
        lista.elements.append(datos) 
        return datos 
    
    def size(lista):
        return (f"La pila tiene una tamaño de {len(lista.elements)} elementos en este momento")
    
    def pop(lista): 
        print(f"El elemento superior de la lista es {lista.elements[-1]}")
        print(f"El elemento superior ha sido eliminado")
        return lista.elements.pop() 
        
    def peek(lista):
        return (f"El elemento superior de la lista es {lista.elements[-1]}")
        
    def is_empty(lista):
        return len(lista.elements) == 0

if __name__ == '__main__':
    pila = Pila()

start = True  
while start == True:
    print("""\nBienvenido al programa
Elija una de las siguientes opciones""")
    choose = int(input("""
    1. TDA Pila
    2. TDA Cola
    3. Salir
    """))
    if choose == 1:
        while True:
            choose_2 = int(input("""Elija una de las siguientes opciones
            1. Crear pila vacia
            2. Consultar el tamaño de la pila
            3. Añadir elementos a la pila
            4. Consultar y Retirar el elemento superior de la pila
            5. Consultar el elemento superior de la pila sin retirarlo
            6. Consultar si la pila tiene o no elementos
            7. Eliminar elementos la pila
            8. Salir
            """))
            if choose_2 == 1:
                ## Creating the empty pila
                print("Se ha creado una lista vacia\n")
                pila.__init__()
            elif choose_2 == 2:
                ## Show the size of the pila
                print(pila.size())
            elif choose_2 == 3:
                ## pushing the elements with a cycle for
                numbers = int(input("¿Cuantos números desea agregar a la pila?\n"))
                print(f"Se agregaron los numeros del 0 al {numbers-1}\n")
                for i in range(numbers):
                    pila.push(i)
            elif choose_2 == 4:
                ## popping and reading the topmost element
                pila.pop()
            elif choose_2 == 5:
                ## printing the topmost element of the pila
                print(pila.peek())
            elif choose_2 == 6:
                ## checking is_empty method
                if pila.is_empty() == True:
                    print("La pila esta vacia\n")
                else:
                    print(pila.print_list())
            elif choose_2 == 7:
                ## Creating the empty pila
                pila.__init__()
                print("Se han elimiado los elementos de la pila\n")
            elif choose_2 == 8:
                break
    elif choose == 2:
        print("Has ingresado a la opción 2\n")
    elif choose == 3:
        print("has elegido salir del programa, hasta pronto.\n")
        break
    else:
        print("opción invalida, por favor ingrese una opción valida.\n")
        
