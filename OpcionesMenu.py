"""
Este archivo será para poder usar las opciones del menú, dependiendo de la opción use el usuario, se lanzará una parte
u otra del juego
"""
import Instrucciones
import Excepciones
import Juego

"""
El menú que se mostrará al iniciar el juego
"""
def mostrar_menu():
    print("====================\n" + 
        "Bienvenido a... ¿QUIERES SER MILLONARIO?\n" +
        "====================")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Salir")
    
"""
Funcionamiento del menú elegir opciones, será el método que se mostrará en el main
"""
def leer_opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                Juego.jugar()
                return
            elif opcion == 2:
                Instrucciones.mostrar_instrucciones()
            elif opcion == 3:
                exit()
            else:
                raise Excepciones.OpcionMenuInvalida()
                
        except Excepciones.OpcionMenuInvalida:
            print("La opción del menú no existe, intentelo de nuevo")
        except ValueError:
            print("Has introducido algo distinto a un núemro, intentelo de nuevo")