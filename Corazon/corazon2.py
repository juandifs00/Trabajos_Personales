import turtle
import time

# define la función que dibuja la figura del corazón


def draw_heart(size):
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('pink', 'pink')
    turtle.pensize(6)
    turtle.speed(10)

    turtle.left(45)
    turtle.forward(size)
    turtle.circle(size / 2, 180)
    turtle.right(90)
    turtle.circle(size / 2, 180)
    turtle.forward(size)
    turtle.end_fill()

# define la función que muestra un mensaje


def show_message(message):
    turtle.penup()
    turtle.setpos(-450, -30)
    turtle.color('blue')
    turtle.write(message, font=("Comic Sans MS", 18, "bold"))


turtle.setup(930, 650)

# lista de mensajes a mostrar
messages = [
    "Lo siento por como te he hecho sentir, pero mi problema es que",
    "no sé cómo expresarme muchas veces.",
    "Intento aprender y mejorar, y sé que he cometido muchos errores",
    "y estoy muy agradecido porque a pesar de todo, aún me perdonas",
    "Agradezco tu paciencia y comprensión.",
    "No quiero seguir hiriendote, no quiero seguir fallándote ni haciente sentir mal,",
    "de verdad que quiero demostrarte que te amo y que te respeto porque",
    "quiero que vuelvas a querer todo conmigo,",
    "sino que muchas veces creo que doy 2 pasos adelante y como 5 atrás,",
    "y pienso que es porque quiero",
    "solucionar todo lo malo que he hecho",
    "en lugar de simplemente dejarme llevar y disfrutar del momento.",
    "Espero no cometer más errores porque desde que estoy contigo,",
    "estoy con una mujer maravillosa y que tengo que valorarte por lo que eres",
    "y por como has sido conmigo.",
    "Solo que quiero hacer las cosas bien contigo pero muchas veces...",
    "no me salen como las planeo y me frustro por eso.",
    "De verdad que no sé por qué te he fallado tantas veces,",
    "nunca había hecho llorar tanto a una mujer y me siento fatal por eso.",
    "No te voy a prometer nada ni te voy a decir nada que no sepas ya,",
    "sólo que pondré todo de mi para no volver a tropezarme con la misma piedra",
    "y que espero que me des el chance de mejorar y por lo menos de darte",
    "la mejor impresión de mi.",
    "Eres importante para mí y quiero hacerte feliz.",
    "Es lo que al menos quiero lograr y espero que me lo permitas."
]

# loop para repetir la animación indefinidamente
while True:
    turtle.clear()  # borra todo el dibujo anterior
    draw_heart(200)  # dibuja la figura del corazón

    # muestra los mensajes
    for message in messages:
        show_message(message)
        # espera 4 segundos antes de mostrar el siguiente mensaje
        time.sleep(4)
        turtle.clear()  # borra el mensaje antes de mostrar el siguiente
        draw_heart(200)  # dibuja la figura del corazón

     # espera 15 segundos antes de finalizar el programa
    time.sleep(5)
    break  # sale del bucle while y finaliza el programa
