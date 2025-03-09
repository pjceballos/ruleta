import random

def mostrar_bienvenida():
    print("¡Bienvenido al juego de Ruleta Francesa!")
    print("Comienzas con 5 monedas.")
    print("Gana más monedas adivinando el número correcto.")
    print("Si pierdes todas tus monedas, el juego termina.")
    print("¡Buena suerte!")

def mostrar_menu():
    print("\nOpciones:")
    print("1. Apostar a un número (paga 35 a 1)")
    print("2. Apostar a rojo o negro (paga 1 a 1)")
    print("3. Apostar a par o impar (paga 1 a 1)")
    print("4. Salir")

def girar_ruleta():
    return random.randint(0, 36)

def es_rojo(numero):
    rojos = [
        1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
    ]
    return numero in rojos

def obtener_pregunta():
    preguntas = [
        {
            "pregunta": "¿Qué es la estadística?",
            "opciones": ["a) El estudio de los astros", "b) La recolección, organización, análisis e interpretación de datos", "c) Un método para resolver ecuaciones", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "La estadística se divide en:",
            "opciones": ["a) Estadística experimental y descriptiva", "b) Estadística descriptiva e inferencial", "c) Estadística teórica y práctica", "d) Estadística clásica y moderna"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuál de los siguientes es un ejemplo de dato cualitativo?",
            "opciones": ["a) La temperatura del día", "b) La altura de una persona", "c) El color de ojos de una persona", "d) El peso de una caja"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "Un parámetro es:",
            "opciones": ["a) Una medida calculada con datos muestrales", "b) Una medida calculada con datos poblacionales", "c) Un tipo de variable", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuál de los siguientes NO es un tipo de variable cuantitativa?",
            "opciones": ["a) Discreta", "b) Continua", "c) Nominal", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "La moda de un conjunto de datos es:",
            "opciones": ["a) El número que más se repite", "b) El valor promedio", "c) El valor central en un conjunto ordenado", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "Si en un grupo de estudiantes las edades son: 12, 14, 15, 14, 14, 13 y 12, ¿cuál es la moda?",
            "opciones": ["a) 12", "b) 14", "c) 13", "d) 15"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cómo se calcula la media aritmética?",
            "opciones": ["a) Sumando los valores y dividiendo entre la cantidad de valores", "b) Restando el valor menor del mayor", "c) Multiplicando todos los valores", "d) Dividiendo el valor máximo entre el mínimo"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Cuál de las siguientes afirmaciones sobre la mediana es verdadera?",
            "opciones": ["a) Es el promedio de los valores extremos", "b) No se ve afectada por valores atípicos", "c) Siempre es igual a la media", "d) Es el valor que más se repite"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si los datos son: 3, 7, 10, 15, 18, 21, 25, ¿cuál es la mediana?",
            "opciones": ["a) 10", "b) 15", "c) 18", "d) 7"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "La desviación estándar mide:",
            "opciones": ["a) La tendencia central de los datos", "b) La dispersión de los datos respecto a la media", "c) La correlación entre variables", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si la varianza es 25, ¿cuál es la desviación estándar?",
            "opciones": ["a) 5", "b) 10", "c) 25", "d) 50"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Qué indica un coeficiente de variación alto?",
            "opciones": ["a) Menor dispersión relativa", "b) Mayor dispersión relativa", "c) No tiene significado", "d) Igualdad de valores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cómo se calcula el rango?",
            "opciones": ["a) Promediando todos los valores", "b) Restando el valor mínimo al valor máximo", "c) Sumando todos los valores", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si la media es 50 y la desviación estándar es 5, ¿cuál es el coeficiente de variación?",
            "opciones": ["a) 5%", "b) 10%", "c) 50%", "d) 25%"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué es la probabilidad?",
            "opciones": ["a) La posibilidad de que ocurra un evento", "b) El resultado de un experimento", "c) Un número siempre mayor que 1", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "Un evento imposible tiene una probabilidad de:",
            "opciones": ["a) 0", "b) 1", "c) 0.5", "d) -1"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Cuál de estos valores puede representar una probabilidad?",
            "opciones": ["a) -0.2", "b) 1.5", "c) 0.75", "d) 1.8"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "Si lanzamos un dado de seis caras, ¿cuál es la probabilidad de obtener un número par?",
            "opciones": ["a) 1/3", "b) 1/2", "c) 2/3", "d) 5/6"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "La probabilidad de obtener 'cara' en una moneda justa es:",
            "opciones": ["a) 0.25", "b) 0.50", "c) 0.75", "d) 1.00"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuál de las siguientes es una distribución de probabilidad discreta?",
            "opciones": ["a) Normal", "b) Binomial", "c) Exponencial", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "La distribución normal es:",
            "opciones": ["a) Simétrica", "b) Asimétrica", "c) Discreta", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "En una distribución binomial, el número de ensayos es:",
            "opciones": ["a) Variable", "b) Fijo", "c) Infinito", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué representa la media en una distribución normal estándar?",
            "opciones": ["a) 0", "b) 1", "c) 50", "d) Depende de los datos"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "La distribución de Poisson se usa para modelar:",
            "opciones": ["a) Datos normales", "b) Eventos raros en un intervalo", "c) Probabilidades simétricas", "d) Ninguna de las anteriores"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Qué es la probabilidad?",
            "opciones": ["a) La cantidad de veces que ocurre un evento.", "b) La posibilidad de que ocurra un evento.", "c) El número total de eventos en un experimento.", "d) La suma de todos los eventos posibles."],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si un evento tiene una probabilidad de 1, significa que:",
            "opciones": ["a) Nunca ocurrirá.", "b) Es muy poco probable que ocurra.", "c) Ocurrirá siempre.", "d) No se puede calcular su probabilidad."],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es la probabilidad de sacar un número impar al lanzar un dado de seis caras?",
            "opciones": ["a) 3/6", "b) 2/6", "c) 1/6", "d) 4/6"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "Si lanzamos una moneda, ¿cuál es la probabilidad de que salga cara?",
            "opciones": ["a) 100%", "b) 50%", "c) 25%", "d) 75%"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Un evento imposible tiene una probabilidad de:",
            "opciones": ["a) 0", "b) 1", "c) 0.5", "d) 10"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "¿Cuál es el espacio muestral al lanzar una moneda dos veces?",
            "opciones": ["a) {C, S}", "b) {CC, CS, SC, SS}", "c) {1, 2, 3, 4}", "d) {Cara, Sello}"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si en una bolsa hay 4 canicas rojas y 6 verdes, ¿cuál es el total de eventos posibles al sacar una canica?",
            "opciones": ["a) 6", "b) 4", "c) 10", "d) 2"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Qué significa que dos eventos sean mutuamente excluyentes?",
            "opciones": ["a) Que pueden ocurrir al mismo tiempo.", "b) Que nunca pueden ocurrir juntos.", "c) Que son el mismo evento.", "d) Que tienen la misma probabilidad."],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si un evento tiene probabilidad 0.25, significa que:",
            "opciones": ["a) Ocurrirá el 100% de las veces.", "b) Ocurrirá el 25% de las veces.", "c) Nunca ocurrirá.", "d) Ocurrirá la mitad de las veces."],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "¿Cuál es la probabilidad de sacar un número par al lanzar un dado de seis caras?",
            "opciones": ["a) 2/6", "b) 1/6", "c) 3/6", "d) 4/6"],
            "respuesta_correcta": "c"
        },
        {
            "pregunta": "¿Cuál es la probabilidad de sacar un rey en una baraja de 52 cartas?",
            "opciones": ["a) 1/52", "b) 4/52", "c) 13/52", "d) 26/52"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si en una urna hay 7 bolas rojas, 5 azules y 8 verdes, ¿cuál es la probabilidad de sacar una roja?",
            "opciones": ["a) 7/20", "b) 5/20", "c) 8/20", "d) 7/15"],
            "respuesta_correcta": "a"
        },
        {
            "pregunta": "Si sacamos una carta de una baraja española (40 cartas), ¿cuál es la probabilidad de que sea un as?",
            "opciones": ["a) 4/40", "b) 1/10", "c) 2/40", "d) 4/10"],
            "respuesta_correcta": "b"
        },
        {
            "pregunta": "Si se lanza un dado dos veces, ¿cuál es la probabilidad de obtener un 3 en ambas tiradas?",
            "opciones": ["a) 1/6", "b) 1/36", "c) 1/12", "d) 1/18"],
            "respuesta_correcta": "b"
        }
    ]
    return random.choice(preguntas)

def preguntar_probabilidad():
    pregunta = obtener_pregunta()
    print("\nPregunta de Probabilidad:")
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)
    
    respuesta = input("Elige la opción correcta (a, b, c, o d): ")
    return respuesta.lower() == pregunta["respuesta_correcta"]

def main():
    monedas = 5
    mostrar_bienvenida()

    while True:
        if monedas > 0:
            mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion == "1":
                numero_elegido = int(input("Elige un número entre 0 y 36: "))
                apuesta = int(input(f"¿Cuántas monedas quieres apostar? (Tienes {monedas} monedas): "))
                if apuesta > monedas:
                    print("No tienes suficientes monedas para esa apuesta.")
                    continue
                
                numero_ganador = girar_ruleta()
                print(f"El número ganador es: {numero_ganador}")
                if numero_elegido == numero_ganador:
                    ganancias = apuesta * 35
                    monedas += ganancias
                    print(f"¡Felicidades! Ganaste {ganancias} monedas.")
                else:
                    monedas -= apuesta
                    print("Lo siento, perdiste la apuesta.")

            elif opcion == "2":
                color_elegido = input("Elige un color (rojo/negro): ").lower()
                apuesta = int(input(f"¿Cuántas monedas quieres apostar? (Tienes {monedas} monedas): "))
                if apuesta > monedas:
                    print("No tienes suficientes monedas para esa apuesta.")
                    continue
                
                numero_ganador = girar_ruleta()
                color_ganador = "rojo" if es_rojo(numero_ganador) else "negro"
                print(f"El número ganador es: {numero_ganador} ({color_ganador})")
                if color_elegido == color_ganador:
                    ganancias = apuesta
                    monedas += ganancias
                    print(f"¡Felicidades! Ganaste {ganancias} monedas.")
                else:
                    monedas -= apuesta
                    print("Lo siento, perdiste la apuesta.")

            elif opcion == "3":
                paridad_elegida = input("Elige par o impar: ").lower()
                apuesta = int(input(f"¿Cuántas monedas quieres apostar? (Tienes {monedas} monedas): "))
                if apuesta > monedas:
                    print("No tienes suficientes monedas para esa apuesta.")
                    continue
                
                numero_ganador = girar_ruleta()
                paridad_ganadora = "par" if numero_ganador % 2 == 0 else "impar"
                print(f"El número ganador es: {numero_ganador} ({paridad_ganadora})")
                if paridad_elegida == paridad_ganadora:
                    ganancias = apuesta
                    monedas += ganancias
                    print(f"¡Felicidades! Ganaste {ganancias} monedas.")
                else:
                    monedas -= apuesta
                    print("Lo siento, perdiste la apuesta.")

            elif opcion == "4":
                print("Gracias por jugar. ¡Hasta la próxima!")
                break

            else:
                print("Opción no válida. Por favor, elige una opción del menú.")

            print(f"Te quedan {monedas} monedas.")
        
        else:
            print("Te has quedado sin monedas.")
            if preguntar_probabilidad():
                monedas = 1
                print("¡Respuesta correcta! Obtienes 1 moneda para seguir jugando.")
            else:
                print("Respuesta incorrecta. El juego ha terminado.")
                break

if __name__ == "__main__":
    main()