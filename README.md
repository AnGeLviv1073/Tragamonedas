Descripción
Este es un juego de tragamonedas sencillo desarrollado en Python utilizando el marco de trabajo tkinter para la interfaz gráfica. El juego sigue el patrón de diseño Model-View-Controller (MVC), que separa la lógica del juego, la interfaz de usuario y el controlador que gestiona las interacciones del usuario.

Funcionalidad
El jugador tiene un saldo inicial de $100.

El jugador puede realizar apuestas de $10 por cada giro de los rodillos.

Al girar los rodillos, el juego genera aleatoriamente tres símbolos, y el jugador recibe un premio basado en los símbolos que aparecen.

Símbolos: cherry, lemon, bell, diamond y star.

Premio mayor: Si los tres símbolos coinciden, el jugador gana 10 veces su apuesta.

Premio menor: Si hay dos símbolos coincidentes, el jugador gana 2 veces su apuesta.

Sin premio: Si no hay símbolos coincidentes, el jugador no gana nada.

El objetivo es mantener el saldo positivo y disfrutar del juego.

Requisitos
Python 3.x

Biblioteca tkinter (por defecto en Python)

Biblioteca PIL (Python Imaging Library) para manejar imágenes. Puedes instalarla usando pip install Pillow.

Estructura del Proyecto
bash
Copiar
Editar
/SlotMachineGame
    /images
        cherry.png
        diamond.png
        lemon.png
        star.png
        bell.png
    /slot_model.py        # Lógica del juego (Modelo)
    /slot_view.py         # Interfaz gráfica (Vista)
    /slot_controller.py   # Controlador de la aplicación (Controlador)
    main.py               # Punto de entrada del programa
    README.md             # Este archivo
Cómo usar
Instala los requisitos: Asegúrate de tener Python 3.x y la biblioteca Pillow instalada. Puedes instalarla utilizando el siguiente comando:

bash
Copiar
Editar
pip install Pillow
Preparar las imágenes: Coloca las imágenes PNG (cherry.png, diamond.png, lemon.png, star.png, bell.png) en la carpeta images/.

Ejecutar el juego: Simplemente ejecuta el archivo main.py para iniciar el juego:

bash
Copiar
Editar
python main.py
Interacción con el juego:

El saldo inicial es de $100.

Puedes hacer clic en el botón SPIN para girar los rodillos.

Los rodillos mostrarán imágenes de los símbolos y el saldo se actualizará en función de los resultados del giro.

Explicación del código
El código está organizado utilizando el patrón Modelo-Vista-Controlador (MVC):

Modelo (slot_model.py):

Define la clase SlotMachine que maneja la lógica del juego.

Genera resultados aleatorios para los rodillos y calcula las ganancias según los símbolos que coinciden.

Lleva el control del saldo y la apuesta.

Vista (slot_view.py):

Utiliza tkinter para crear una interfaz gráfica.

Muestra las imágenes de los rodillos y el saldo actual.

Actualiza la interfaz con los resultados del juego.

Controlador (slot_controller.py):

Gestiona las interacciones entre la vista y el modelo.

Se encarga de manejar el evento de hacer clic en el botón SPIN y de realizar el giro de los rodillos.

Inicia un hilo para que el proceso de giro no bloquee la interfaz de usuario.
