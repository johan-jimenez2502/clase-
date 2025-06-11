import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import json

# ---------------- Configuracion ----------------
CARPETA_USUARIOS = "usuarios_lamigaja"

if not os.path.exists(CARPETA_USUARIOS):
    os.makedirs(CARPETA_USUARIOS)

# ---------------- Funciones ----------------

def registrar():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    rol = rol_seleccionado.get()

    if not usuario or not contrasena or rol == "Seleccione un rol":
        messagebox.showwarning("Campos vacíos", "Completa todos los campos.")
        return

    ruta_archivo = os.path.join(CARPETA_USUARIOS, f"{usuario}.json")

    if os.path.exists(ruta_archivo):
        messagebox.showwarning("Error", "¡Este usuario ya está registrado!")
    else:
        datos = {
            "usuario": usuario,
            "contrasena": contrasena,
            "rol": rol
        }
        with open(ruta_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
        messagebox.showinfo("Registro exitoso", f"Usuario '{usuario}' registrado como {rol}.")
        limpiar_campos()

def iniciar_sesion():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()

    if not usuario or not contrasena:
        messagebox.showwarning("Campos vacíos", "Debes llenar todos los campos.")
        return

    ruta_archivo = os.path.join(CARPETA_USUARIOS, f"{usuario}.json")

    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as archivo:
            datos = json.load(archivo)
        if datos["contrasena"] == contrasena:
            rol = datos["rol"]
            messagebox.showinfo("Bienvenido", f"¡Hola {usuario}!\nRol: {rol.capitalize()}")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
    else:
        messagebox.showerror("Error", "Usuario no registrado.")

def limpiar_campos():
    entry_usuario.delete(0, tk.END)
    entry_contrasena.delete(0, tk.END)
    rol_seleccionado.set("Seleccione un rol")

# ---------------- Interfaz gráfica ----------------

ventana = tk.Tk()
ventana.title("La Migaja - Login")
ventana.geometry("400x500")
ventana.config(bg="#FFF9F0")  # Color de fondo claro tipo panadería

# Cargar logo (usa una imagen llamada 'logo.png' en la misma carpeta)
try:
    imagen = Image.open("logo.png")
    imagen = imagen.resize((120, 120))
    logo = ImageTk.PhotoImage(imagen)
    tk.Label(ventana, image=logo, bg="#FFF9F0").pack(pady=10)
except:
    tk.Label(ventana, text="La Migaja", font=("Arial", 18, "bold"), bg="#FFF9F0", fg="#9C4F20").pack(pady=10)

# Campos
tk.Label(ventana, text="Usuario:", bg="#FFF9F0", font=("Arial", 12)).pack(pady=5)
entry_usuario = tk.Entry(ventana, font=("Arial", 12))
entry_usuario.pack()

tk.Label(ventana, text="Contraseña:", bg="#FFF9F0", font=("Arial", 12)).pack(pady=5)
entry_contrasena = tk.Entry(ventana, show="*", font=("Arial", 12))
entry_contrasena.pack()

tk.Label(ventana, text="Rol:", bg="#FFF9F0", font=("Arial", 12)).pack(pady=5)
rol_seleccionado = tk.StringVar(ventana)
rol_seleccionado.set("Seleccione un rol")
opciones_rol = ["cliente", "mesero", "cocinero"]
tk.OptionMenu(ventana, rol_seleccionado, *opciones_rol).pack()

# Botones
def estilo_boton(boton):
    boton.config(font=("Arial", 12), bg="#D9A066", fg="white", activebackground="#BF8430", cursor="hand2", width=15)

btn_registrar = tk.Button(ventana, text="Registrarse", command=registrar)
estilo_boton(btn_registrar)
btn_registrar.pack(pady=10)

btn_login = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion)
estilo_boton(btn_login)
btn_login.pack()

# Ejecutar
ventana.mainloop()
