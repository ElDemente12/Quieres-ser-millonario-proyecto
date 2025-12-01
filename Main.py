"""
Bienvenido a "¿Quieres ser millonario?", un supuesto proyecto califible para la asignatura de 'Python'.
Este proyecto está hecho por Esteban Linares Abad. Este archivo será el archivo Main, dónde solo estará lo principal y 
necesario para que este proyecto corra.
"""
import OpcionesMenu

try:
    while True:
        OpcionesMenu.mostrar_menu()
        OpcionesMenu.leer_opcion_menu()
except KeyboardInterrupt:
    print("\nLo siento pero si sales corriendo no te podras llevar ningún premio, ¡que lástima!")
