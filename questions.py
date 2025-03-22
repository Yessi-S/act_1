import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Inicializo el contador de puntos
points=0

# Creación de una lista con 3 preguntas, respuestas asociadas y sus respuestas correctas para evitar el uso de indices
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
# Se usan tres variables para acceder a cada pregunta, respuesta y respuesta correcta
for question, options,correct_option in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(options):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # verifico si es un numero y por circuito corto: si no lo es pasa directamente al else.
        # uso len(options) para conocer la cantidad de respuestas posibles debtro de la pregunta aleatoria seleccionada
        if user_answer.isdigit() and 1<= int(user_answer) <=len(options):
             user_answer=int(user_answer)-1
        else:
             print("Respuesta no válida")
             sys.exit(1)
        # Se verifica si la respuesta es correcta
        if user_answer == correct_option:
            points+=1
            print("¡Correcto!")
            break
        else:
            points-=0.5          
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(options[correct_option])
    # Se imprime un blanco al final de la pregunta
    print()
print(f"Su puntaje final: {points} puntos")