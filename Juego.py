import Preguntas
import Excepciones

premios = [
    100, 200, 300, 500, 1000,
    2000, 4000, 8000, 16000, 32000,
    64000, 125000, 250000, 500000, 1000000
]

def jugar():
    print("\n====================\n" + 
        "¡Comienza el juego!\n" +
        "====================")
    lista_preguntas = Preguntas.obtener_pregunta_por_numero()
    
    premio_actual = 0
    nivel_seguro = 0
    
    for i, pregunta in enumerate(lista_preguntas):
        numero_pregunta = i + 1
        Preguntas.mostrar_pregunta(pregunta, numero_pregunta)
        
        print(f"Premio por acertar: {premios[i]}€")
        print("Escribe la letra de tu respuesta o 'P' para plantarte.")
        
        while True:
            try:
                respuesta = input("Tu respuesta: ").lower().strip()
                
                if respuesta == 'p':
                    print(f"\n¡Te has plantado! Te llevas {premio_actual}€.")
                    return

                if respuesta not in ['a', 'b', 'c', 'd']:
                    raise Excepciones.RespuestaInvalida()
                
                # Comprobar respuesta
                if respuesta == pregunta['respuesta']:
                    premio_actual = premios[i]
                    print(f"\n¡Correcto! Has ganado {premio_actual}€.")
                    
                    # Actualizar nivel seguro
                    if numero_pregunta == 5:
                        nivel_seguro = 1000
                        print("¡Has alcanzado el primer nivel seguro (1.000€)!")
                    elif numero_pregunta == 10:
                        nivel_seguro = 32000
                        print("¡Has alcanzado el segundo nivel seguro (32.000€)!")
                    
                    if numero_pregunta == 15:
                        print("\n¡¡¡ENHORABUENA!!! ¡HAS GANADO EL MILLÓN DE EUROS!")
                        return
                    
                    break # Sale del while de input y va a la siguiente pregunta
                else:
                    print(f"\nIncorrecto. La respuesta correcta era '{pregunta['respuesta']}'.")
                    print(f"Te vas a casa con {nivel_seguro}€.")
                    return

            except Excepciones.RespuestaInvalida:
                print("Respuesta no válida. Por favor, introduce A, B, C, D o P.")
            except Exception as e:
                print(f"Ha ocurrido un error inesperado: {e}")
                return
