"""
En este archivo se encontrarán los métodos y funciones necesarias para mostrar el cómo jugar si eres nuevo
"""

arrayInstrucciones = [
    "• Hay 15 preguntas",
    "• Se dividen por dificultad (1-5: fácil, 6-10: media, 11-15: difícil)",
    "• Se pueden plantar escribiendo P",
    "• Se debe responder con A, B, C o D",
    "• Si aciertas subes el premio",
    "• Si fallas pierdes y te quedas con el premio del último nivel seguro superado",
    "• Hay niveles seguros (pregunta 5 y 10)",
]

def mostrar_instrucciones():
    for instruccion in arrayInstrucciones:
        print(instruccion)