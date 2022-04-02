import random

class Pila: 
    def __init__(lista): 
        lista.elements = []

    def print_list(lista):
        return (f"Los elementos de la pila son: {lista.elements[-1]}\n")
    
    def push(lista, datos): 
        lista.elements.append(datos) 
        return datos

    def size(lista):
        return (f"La pila tiene una tamaño de {len(lista.elements)} elementos en este momento\n")
    
    def pop_1(lista):
        return lista.elements.pop()
        
    def peek(lista):
        return lista.elements[-1]
      
    def is_empty(lista):
        return len(lista.elements) == 0

class Cola: 
    def __init__(lista): 
        lista.elements = []

    def print_list(lista):
        return (f"Los elementos de la cola son: {lista.elements}\n")
    
    def enqueue(lista, datos): 
        lista.elements.append(datos) 
        return datos

    def size(lista):
        return (f"La cola tiene una tamaño de {len(lista.elements)} elementos en este momento\n")
    
    def dequeue(lista):
        return lista.elements.pop(0)
        
    def rear(lista):
        return lista.elements[-1]
    
    def front(lista):
        return lista.elements[0]

    def is_empty(lista):
        return len(lista.elements) == 0

if __name__ == '__main__':
    pila = Pila()
    cola = Cola()

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
            7. Eliminar elementos de la pila
            8. Buscar un número y borrar los que no son iguales hasta que lo encuentre
            9. Salir
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
                if pila.is_empty() == True:
                    print("La lista esta vacia")
                else: 
                    print(f"El elemento del frente de la pila es {pila.peek()}")
                    pila.pop_1()
                    print(f"El elemento superior ha sido eliminado\n")
            elif choose_2 == 5:
                ## printing the topmost element of the pila
                print(f"El elemento superior de la pila es {pila.peek()}\n")
            elif choose_2 == 6:
                ## checking is_empty method
                if pila.is_empty() == True:
                    print("La pila esta vacia\n")
                else:
                    print(pila.print_list())
            elif choose_2 == 7:
                ## Creating the empty pila
                while pila.is_empty() == False:
                    print(f"Se ha eliminado el elemento {pila.peek()} de la pila...\n")
                    pila.pop_1()
                    if pila.is_empty() == True:
                        print("Se han eliminado todos los elementos de la pila o ya estaba vacia")
                    
            elif choose_2 == 8:
                number_1 = int(input("Escriba el número a buscar\n"))
                erased_nums = []
                for num in range(numbers):
                    if number_1 == pila.peek():
                        print(f"Usted ha elegido: {number_1} y el elemento superior de la pila es: {pila.peek()}")
                        break
                    else:
                        print(f"Usted ha elegido: {number_1} y el elemento superior de la pila es: {pila.peek()}")
                        print(f"El número al frente de la cola {pila.peek()} se ha eliminado ya que no es igual al elegido")
                        erased_nums.append(pila.peek())
                        pila.pop_1()
                print(f"Los números eliminados son: {erased_nums}")
                
            elif choose_2 == 9:
                break
    elif choose == 2:
        while True:
            choose_2 = int(input("""Elija una de las siguientes opciones
            1. Crear cola vacia
            2. Consultar el tamaño de la cola
            3. Añadir elementos a la cola
            4. Consultar y Retirar el elemento del frente de la cola de la pila
            5. Consultar el elemento en el frente de la cola
            6. Consultar si la cola esta vacia o no
            7. Consultar el elemento del final de la cola
            8. Insertar un elemento al final de la cola
            9. Eliminar elementos de la cola
            10. Buscar un número y borrar los que no son iguales hasta que lo encuentre
            11. Salir
            """))
            if choose_2 == 1:
                ## Creating the empty pila
                print("Se ha creado una cola vacia\n")
                cola.__init__()
            elif choose_2 == 2:
                ## Show the size of the pila
                print(cola.size())
            elif choose_2 == 3:
                ## pushing the elements with a cycle for
                numbers = int(input("¿Cuantos números desea agregar a la cola?\n"))
                print(f"Se agregaron los numeros del 0 al {numbers-1}\n")
                for i in range(numbers):
                    cola.enqueue(i)
            elif choose_2 == 4:
                ## popping and reading the topmost element
                print(f"El elemento del frente de la cola es {cola.front()}")
                cola.dequeue()
                print(f"El elemento del frente ha sido eliminado\n")
            elif choose_2 == 5:
                ## printing the topmost element of the pila
                print(f"El elemento del frente de la lista es {cola.front()}\n")
            elif choose_2 == 6:
                ## checking is_empty method
                if cola.is_empty() == True:
                    print("La pila esta vacia\n")
                else:
                    print(cola.print_list())
            elif choose_2 == 7:
                print(f"El elemento del final de la lista es {cola.rear()}\n")
            elif choose_2 == 8:
                number_3 = int(input("¿Cuantos números desea agregar a la cola?\n"))
                print(f"Se agregaron los numeros del 0 al {number_3-1}\n")
                for i in range(number_3):
                    cola.enqueue(i)
            elif choose_2 == 9:
                ## Creating the empty pila
                while cola.is_empty() == False:
                    print(f"Se ha eliminado el elemento {cola.front()} de la lista...\n")
                    cola.enqueue()
                    if cola.is_empty() == True:
                        print("Se han eliminado todos los elementos de la pila.")
            elif choose_2 == 10:
                number_1 = int(input("Escriba el número a buscar\n"))
                erased_nums = []
                for num in range(numbers):
                    if number_1 == cola.front():
                        print(f"Usted ha elegido: {number_1} y el elemento del frente de la cola es: {cola.front()}")
                        break
                    else:
                        print(f"Usted ha elegido: {number_1} y el elemento del frente de la cola es: {cola.front()}")
                        print(f"El número al frente de la cola {cola.front()} se ha eliminado ya que no es igual al elegido")
                        erased_nums.append(cola.front())
                        cola.dequeue()
                print(f"Los números eliminados son: {erased_nums}")
                
            elif choose_2 == 11:
                break
    elif choose == 3:
        print("has elegido salir del programa, hasta pronto.\n")
        break
    else:
        print("opción invalida, por favor ingrese una opción valida.\n")
        

 
