from tkinter import *
from random import randint
from tkinter.messagebox import showinfo

letrasUsadas = []
intentos = 7
letrasAcertadas = 0

def colocarLetras():
    x = 50
    y = 150
    contador = 0
    Label(canvas, text='Letras sin usar').place(x=50, y=100)
    for i in range(26):
        contador += 1
        letrasLabel[i].place(x=x, y=y)
        x += 30
        if contador == 5:
            y += 35
            contador = 0
            x = 50

def probarLetraFuncion():
    global intentos, letrasAcertadas

    letra = letraObtenida.get().lower()

    if letra and letra not in letrasUsadas:  
        letrasUsadas.append(letra)

        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    guiones[i].config(text=letra)
                    letrasAcertadas += 1

            if letrasAcertadas == len(palabra):
                showinfo(title='¡Ganaste!', message='¡Felicidades, completaste el juego!')
                raiz.quit()  

        else:
            intentos -= 1
            canvas.itemconfig(imagen_id, image=imagenes[intentos-1])
            if intentos == 0:
                showinfo(title='Perdiste', message='Se acabaron los intentos. ¡Intenta de nuevo!')
                raiz.quit()  

        letrasLabel[ord(letra) - 97].config(text='')  
    else:
        showinfo("Advertencia", "Esa letra ya fue utilizada.")  

    letraObtenida.set("")  

def verificar_login():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    with open('usuarios.txt', 'r') as archivo:
        usuarios = archivo.readlines()

    for linea in usuarios:
        datos = linea.strip().split(',')
        if len(datos) == 2 and datos[0] == usuario and datos[1] == contraseña:
            showinfo("Éxito", "Inicio de sesión exitoso")
            ventana_login.destroy()
            iniciar_juego()
            return

    showinfo("Error", "Usuario o contraseña incorrectos")

def iniciar_juego():
    global palabra, raiz, canvas, letraObtenida, letrasLabel, guiones, imagen_id, imagenes

    raiz = Tk()
    archivo = open('palabras.txt', 'r')
    conjuntoPalabras = list(archivo.read().split('\n'))
    palabra = conjuntoPalabras[randint(0, len(conjuntoPalabras) - 1)].lower()

    letraObtenida = StringVar()

    raiz.config(width=1000, height=600, bg='blue', relief='groove', bd=10)
    raiz.geometry('1000x600')
    canvas = Canvas(raiz, width=100, height=600)
    canvas.pack(expand=True, fill='both')
    imagenes = [
        PhotoImage(file='1.png'),
        PhotoImage(file='2.png'),
        PhotoImage(file='3.png'),
        PhotoImage(file='4.png'),
        PhotoImage(file='5.png'),
        PhotoImage(file='6.png'),
        PhotoImage(file='7.png'),
    ]
    imagen_id = canvas.create_image(750, 300, image=imagenes[6])
    Label(canvas, text='Introduce la letra', font=('Verdana', 24)).grid(row=0, column=0, padx=10, pady=10)
    letra = Entry(canvas, width=1, font=('Verdana', 24), textvariable=letraObtenida)
    letra.grid(row=0, column=1, padx=10, pady=10)

    probarletra = Button(canvas, text='Probar', bg='Gray', command=probarLetraFuncion)
    probarletra.grid(row=1, column=0, pady=10)

    letrasLabel = [Label(canvas, text=chr(j + 97), font=('Verdana', 20)) for j in range(26)]
    colocarLetras()

    guiones = [Label(canvas, text='_', font=('Verdana', 30)) for _ in palabra]
    inicialX = 200
    for i in range(len(palabra)):
        guiones[i].place(x=inicialX, y=400)
        inicialX += 50

    raiz.mainloop()

# Ventana de login
ventana_login = Tk()
ventana_login.geometry('400x300')
ventana_login.title('Login')

Label(ventana_login, text="Usuario:", font=('Verdana', 14)).pack(pady=10)
entrada_usuario = Entry(ventana_login, font=('Verdana', 14))
entrada_usuario.pack()

Label(ventana_login, text="Contraseña:", font=('Verdana', 14)).pack(pady=10)
entrada_contraseña = Entry(ventana_login, font=('Verdana', 14), show="*")
entrada_contraseña.pack()

boton_login = Button(ventana_login, text="Iniciar sesión", font=('Verdana', 14), command=verificar_login)
boton_login.pack(pady=20)

ventana_login.mainloop()
