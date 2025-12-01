"""
Este archivo contendrá las preguntas y las funciones necesarias para el juego, donde se elegirán 5 preguntas aleatorias
de los bancos de preguntas
"""

import random

preguntas_facil = {
    1: {"pregunta": "¿Cuál es la capital de España?",
        "opciones": {
            "a": "Barcelona",
            "b": "Madrid",
            "c": "Valencia",
            "d": "Sevilla"
        },
        "respuesta": "b"
    },
    2: {"pregunta": "¿Cuánto es 7x8?", 
        "opciones": {
            "a": "32",
            "b": "99",
            "c": "12",
            "d": "56",
            },
        "respuesta": "d"
    },
    3: {"pregunta": "¿Cuál es el color de los limones?", 
        "opciones": {
            "a": "Verde",
            "b": "Rojo",
            "c": "Amarillo",
            "d": "Azul"
        },
        "respuesta": "c"
    },
    4: {"pregunta": "¿Qué animal hace 'guau'?", 
        "opciones": {
            "a": "Gato",
            "b": "Oveja",
            "c": "Perro",
            "d": "Mamút"
        },
        "respuesta": "c"
    },
    5: {"pregunta": "¿De qué color es el pasto?", 
        "opciones": {
            "a": "Verde",
            "b": "Rojo",
            "c": "Amarillo",
            "d": "Azul"
        },
        "respuesta": "a"
    },
    6: {"pregunta": "¿Qué hacemos cuando tenemos hambre?", 
        "opciones": {
            "a": "Cantar",
            "b": "Comer",
            "c": "Beber",
            "d": "Dormir"
        },
        "respuesta": "b"
    },
    7: {"pregunta": "¿Qué número viene después del 1?", 
        "opciones": {
            "a": "2",
            "b": "8",
            "c": "1 (?)",
            "d": "4"
        },
        "respuesta": "a"
    },
    8: {"pregunta": "¿Con qué parte del cuerpo vemos?", 
        "opciones": {
            "a": "Brazos",
            "b": "Ojos",
            "c": "Dedos",
            "d": "Pelo"
        },
        "respuesta": "b"
    },
    9: {"pregunta": "¿Cuál es la raíz cuadrada de 25?", 
        "opciones": {
            "a": "3",
            "b": "25",
            "c": "2",
            "d": "5"
        },
        "respuesta": "d"
    },
    10: {"pregunta": "¿Para que sirve la fórmula E=mc²?, lo siento mala suerte", 
        "opciones": {
            "a": "Para calcular la velocidad máxima de un objeto",
            "b": "Para medir la intensidad de un campo magnético",
            "c": "Para determinar la fuerza necesaria para mover un objeto",
            "d": "Para relacionar masa y energía según la teoría de la relatividad"
        },
        "respuesta": "d"
    },
}

preguntas_media = {
    1: {"pregunta": "¿Cuál es el río más largo del mundo?", 
        "opciones": {
            "a": "Amazonas",
            "b": "Nilo",
            "c": "Yangtsé",
        "d": "Misisipi"
        },
        "respuesta": "b"
    },
    2: {"pregunta": "¿Qué gas necesitamos para respirar?", 
        "opciones": {
            "a": "Dióxido de carbono",
            "b": "Oxígeno",
            "c": "Hidrógeno",
            "d": "Nitrógeno"
        },
        "respuesta": "b"
    },
    3: {"pregunta": "¿Cuál es el animal terrestre más rápido?", 
        "opciones": {
            "a": "León",
            "b": "Gacela",
            "c": "Guepardo",
            "d": "Tigre"
        },
        "respuesta": "c"
    },
    4: {"pregunta": "¿Quién escribió 'Don Quijote de la Mancha'?", 
        "opciones": {
            "a": "Federico García Lorca",
            "b": "Lope de Vega",
            "c": "Gustavo Adolfo Bécquer",
            "d": "Miguel de Cervantes"
        },
        "respuesta": "d"
    },
    5: {"pregunta": "¿Cuál es el país con más población del mundo?", 
        "opciones": {
            "a": "China",
            "b": "India",
            "c": "Estados Unidos",
            "d": "Indonesia"
        },
        "respuesta": "a"
    },
    6: {"pregunta": "¿Cuál es la fórmula química del agua?", 
        "opciones": {
            "a": "CO₂",
            "b": "H₂O",
            "c": "O₂",
            "d": "NaCl"
        },
        "respuesta": "b"
    },
    7: {"pregunta": "¿En qué continente se encuentra Argentina?", 
        "opciones": {
            "a": "Europa",
            "b": "África",
            "c": "América del Sur",
            "d": "Asia"
        },
        "respuesta": "c"
    },
    8: {"pregunta": "¿Qué instrumento mide la presión atmosférica?", 
        "opciones": {
            "a": "Termómetro",
            "b": "Higrómetro",
            "c": "Anemómetro",
            "d": "Barómetro"
        },
        "respuesta": "d"
    },
    9: {"pregunta": "¿Qué planeta es el más grande del sistema solar?", 
        "opciones": {
            "a": "Júpiter",
            "b": "Saturno",
            "c": "Urano",
            "d": "Neptuno"
        },
        "respuesta": "a"
    },
    10: {"pregunta": "¿Cuál es el océano que está al este de África?", 
        "opciones": {
            "a": "Atlántico",
            "b": "Índico",
            "c": "Pacífico",
            "d": "Ártico"
        },
        "respuesta": "b"
    }
}

preguntas_dificil = {
    1: {"pregunta": "¿Cuál es el elemento químico con símbolo 'Au'?", 
        "opciones": {
            "a": "Oro",
            "b": "Plata",
            "c": "Cobre",
            "d": "Mercurio"
        },
        "respuesta": "a"
    },
    2: {"pregunta": "¿En qué año comenzó la Primera Guerra Mundial?", 
        "opciones": {
            "a": "1939",
            "b": "1914",
            "c": "1920",
            "d": "1905"
        },
        "respuesta": "b"
    },
    3: {"pregunta": "¿Quién pintó 'La noche estrellada'?", 
        "opciones": {
            "a": "Picasso",
            "b": "Dalí",
            "c": "Vincent van Gogh",
            "d": "Monet"
        },
        "respuesta": "c"
    },
    4: {"pregunta": "¿Cuál es la capital de Mongolia?", 
        "opciones": {
            "a": "Astaná",
            "b": "Biskek",
            "c": "Dusambé",
            "d": "Ulán Bator"
        },
        "respuesta": "d"
    },
    5: {"pregunta": "¿Qué teoría desarrolló Albert Einstein en 1915?", 
        "opciones": {
            "a": "Teoría de la relatividad general",
            "b": "Teoría cuántica",
            "c": "Teoría de cuerdas",
            "d": "Teoría heliocéntrica"
        },"respuesta": "a"
    },
    6: {"pregunta": "¿Cuál es el número primo más grande menor a 100?", 
            "opciones": {
            "a": "89",
            "b": "97",
            "c": "83",
            "d": "79"
        },
        "respuesta": "b"
    },
    7: {"pregunta": "¿Cuál es la velocidad de la luz en el vacío (aproximada en km/s)?", 
        "opciones": {
            "a": "150 000 km/s",
            "b": "200 000 km/s",
            "c": "300 000 km/s",
            "d": "1 000 000 km/s"
        },
        "respuesta": "c"
    },
    8: {"pregunta": "¿Qué país tiene el mayor número de islas en el mundo?", 
        "opciones": {
            "a": "Noruega",
            "b": "Filipinas",
            "c": "Indonesia",
            "d": "Suecia"
        },
        "respuesta": "d"
    },
    9: {"pregunta": "¿Qué matemático es conocido por el teorema de Fermat?", 
        "opciones": {
            "a": "Pierre de Fermat",
            "b": "Euler",
            "c": "Gauss",
            "d": "Descartes"
        },
        "respuesta": "a"
    },
    10: {"pregunta": "¿Cuál es el libro más antiguo de la Biblia?", 
        "opciones": {
            "a": "Génesis",
            "b": "Job",
            "c": "Éxodo",
            "d": "Proverbios"
        },"respuesta": "b"
    }
}

def obtener_pregunta_por_numero():
    preguntas_juego = []

    faciles = random.sample(list(preguntas_facil.values()), 5)
    medias = random.sample(list(preguntas_media.values()), 5)
    dificiles = random.sample(list(preguntas_dificil.values()), 5)
    
    preguntas_juego.extend(faciles)
    preguntas_juego.extend(medias)
    preguntas_juego.extend(dificiles)
    
    return preguntas_juego

preguntas = obtener_pregunta_por_numero()

def mostrar_pregunta(pregunta, numero_pregunta):
    print(f"\nPregunta {numero_pregunta}: {pregunta['pregunta']}")
    for clave, opcion in pregunta['opciones'].items():
        print(f"{clave}) {opcion}")