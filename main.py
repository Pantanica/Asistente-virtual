import tkinter as tk
from PIL import Image, ImageTk

class InterfazPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Asistente Virtual de Recomendación")
        master.geometry("600x400")

        self.label_bienvenida = tk.Label(master, text="¡Bienvenido al Asistente Virtual de Recomendación!", font=("Helvetica", 20), pady=20)
        self.label_bienvenida.pack()

        self.frame_botones = tk.Frame(master)
        self.frame_botones.pack()

        # Cargar imágenes
        self.imagen_actividades_individuales = Image.open("actividades_individuales.png")
        self.imagen_actividades_individuales = self.imagen_actividades_individuales.resize((100, 100), Image.ANTIALIAS)
        self.imagen_actividades_individuales = ImageTk.PhotoImage(self.imagen_actividades_individuales)

        self.imagen_actividades_grupales = Image.open("actividades_grupales.png")
        self.imagen_actividades_grupales = self.imagen_actividades_grupales.resize((100, 100), Image.ANTIALIAS)
        self.imagen_actividades_grupales = ImageTk.PhotoImage(self.imagen_actividades_grupales)

        # Botones con imágenes
        self.button_actividades_individuales = tk.Button(self.frame_botones, image=self.imagen_actividades_individuales, text="Actividades Individuales", compound="top", font=("Helvetica", 14), command=self.mostrar_actividades_individuales)
        self.button_actividades_individuales.grid(row=0, column=0, padx=20, pady=20)

        self.button_actividades_grupales = tk.Button(self.frame_botones, image=self.imagen_actividades_grupales, text="Actividades Grupales", compound="top", font=("Helvetica", 14), command=self.mostrar_actividades_grupales)
        self.button_actividades_grupales.grid(row=0, column=1, padx=20, pady=20)

        self.button_salir = tk.Button(master, text="Salir", font=("Helvetica", 14), command=master.quit)
        self.button_salir.pack(pady=20)

    def mostrar_actividades_individuales(self):
        # Aquí puedes implementar la lógica para mostrar actividades individuales
        print("Mostrar actividades individuales")

    def mostrar_actividades_grupales(self):
        # Aquí puedes implementar la lógica para mostrar actividades grupales
        print("Mostrar actividades grupales")

root = tk.Tk()
mi_interfaz = InterfazPrincipal(root)
root.mainloop()
