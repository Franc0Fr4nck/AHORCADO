from tkinter import *
from tkinter.messagebox import showinfo

def verificar_credenciales():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()

    with open('usuarios.txt', 'r') as archivo:
        usuarios = archivo.readlines()

    for linea in usuarios:
        datos = linea.strip().split(',')
        if len(datos) == 2 and datos[0] == usuario and datos[1] == contraseña:
            showinfo("Éxito", "Inicio de sesión exitoso")
            raiz.destroy()  # Cierra la ventana actual para abrir el juego
            abrir_juego()
            return

    showinfo("Error", "Usuario o contraseña incorrectos")

def abrir_juego():
    import main  # Aquí se importa la lógica del juego, asegúrate de tenerlo en el mismo directorio

# Ventana principal del login
raiz = Tk()
raiz.geometry('400x300')
raiz.title('Login')

Label(raiz, text="Usuario:", font=('Verdana', 14)).pack(pady=10)
entrada_usuario = Entry(raiz, font=('Verdana', 14))
entrada_usuario.pack()

Label(raiz, text="Contraseña:", font=('Verdana', 14)).pack(pady=10)
entrada_contraseña = Entry(raiz, font=('Verdana', 14), show="*")
entrada_contraseña.pack()

boton_login = Button(raiz, text="Iniciar sesión", font=('Verdana', 14), command=verificar_credenciales)
boton_login.pack(pady=20)

raiz.mainloop()

