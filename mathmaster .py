import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
import pygame 
colores = {   
    'primario': '#6a0dad',
    'secundario': '#8a2be2',
    'terciario': '#9370db',
    'cuaternario': '#ba55d3',
    'quinto': '#D496A7',
    'sexto': '#e6e6fa',
    'séptimo': '#f0e6f6',
    'gris_claro': '#e6e6e6',
    'madera': '#d0a94a'
}
def reproducir_audio(ruta_audio): 
    pygame.mixer.init()
    pygame.mixer.music.load(ruta_audio)
    pygame.mixer.music.play(-1)  
def aplicar_degradado(color_inicial, color_final):
    for i in range(256):
        r = int(color_inicial[1:3], 16) + (int(color_final[1:3], 16) - int(color_inicial[1:3], 16)) * i // 255
        g = int(color_inicial[3:5], 16) + (int(color_final[3:5], 16) - int(color_inicial[3:5], 16)) * i // 255
        b = int(color_inicial[5:7], 16) + (int(color_final[5:7], 16) - int(color_inicial[5:7], 16)) * i // 255
        color = "#{:02x}{:02x}{:02x}".format(r, g, b)
        root.config(bg=color)
def aplicar_estilo(widget, color_fondo='primario', color_texto='white'):
    widget.config(font=("Helvetica", 12), bg=colores[color_fondo], fg=color_texto, padx=10, pady=5, relief="flat", borderwidth=2)
def aplicar_estilo_entrada(widget):
    widget.config(font=("Helvetica", 12), bg=colores['gris_claro'], fg=colores['primario'], borderwidth=2, relief="solid")

from tkinter import PhotoImage, Label
from PIL import Image, ImageTk
import tkinter as tk

def mostrar_pagina_principal():
    aplicar_degradado(colores['primario'], colores['secundario'])
    for widget in root.winfo_children():
        widget.destroy()
    root.title("MathMaster")

    imagen_fondo = Image.open("im.jpg")  
    imagen_fondo = imagen_fondo.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)
    imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    etiqueta_fondo = Label(root, image=imagen_fondo_tk)
    etiqueta_fondo.image = imagen_fondo_tk  
    etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)  

    marco = tk.Frame(root, bg=colores['secundario']) 
    marco.pack(fill=tk.BOTH, expand=True)

    etiqueta_bienvenida = tk.Label(marco, text="¡Bienvenido a MathMaster!", font=("Helvetica", 40, "bold"), fg='black', bg=colores['secundario'])
    etiqueta_bienvenida.pack(pady=20)

    imagen_bienvenida = Image.open("icono.png")
    imagen_bienvenida = imagen_bienvenida.resize((100, 100)) 
    imagen_bienvenida = ImageTk.PhotoImage(imagen_bienvenida)

    etiqueta_imagen = Label(marco, image=imagen_bienvenida, bg=colores['secundario'])
    etiqueta_imagen.image = imagen_bienvenida 
    etiqueta_imagen.pack(pady=10)

    etiqueta_temas = tk.Label(marco, text="¿Qué te gustaría aprender hoy?", font=("Helvetica", 20), fg='black', bg=colores['secundario'])
    etiqueta_temas.pack(pady=20)

    boton_temas = tk.Button(marco, text="Temas", command=mostrar_temas)
    aplicar_estilo(boton_temas, color_fondo='cuaternario', color_texto='black')
    boton_temas.pack(pady=10)

    boton_examenes = tk.Button(marco, text="Exámenes", command=mostrar_examenes)
    aplicar_estilo(boton_examenes, color_fondo='cuaternario', color_texto='black')
    boton_examenes.pack(pady=10)

    boton_salir = tk.Button(marco, text="Salir", command=root.quit)
    aplicar_estilo(boton_salir, color_fondo='cuaternario', color_texto='black')
    boton_salir.pack(pady=20)

    reproducir_audio("La 5ta Sinfonía de Beethoven como nunca la habías visto.mp3")  


def mostrar_temas():
    for widget in root.winfo_children():
        if widget.winfo_ismapped():  
            widget.destroy()

    root.title("Temas")
    aplicar_degradado(colores['primario'], colores['secundario'])  

    etiqueta_temas = tk.Label(root, text="Selecciona la Unidad que deseas trabajar hoy :)", font=("Helvetica", 16, "bold"), bg=colores['secundario'], fg='black')
    etiqueta_temas.pack(pady=20, padx=20, anchor="center")

    frame_izquierdo = tk.Frame(root, bg=colores['secundario'])
    frame_izquierdo.pack(side="left", fill="both", expand=True, padx=20, pady=10)

    frame_derecho = tk.Frame(root, bg=colores['secundario'])
    frame_derecho.pack(side="right", fill="both", expand=True, padx=20, pady=10)

    periodos_unidades = {
        "Periodo 1": ["Unidad 1", "Unidad 2"],
        "Periodo 2": ["Unidad 3", "Unidad 4"],
        "Periodo 3": ["Unidad 5", "Unidad 6"],
        "Periodo 4": ["Unidad 7", "Unidad 8"]
    }

    for periodo in ["Periodo 1", "Periodo 2"]:
        etiqueta_periodo = tk.Label(frame_izquierdo, text=periodo, font=("Helvetica", 14, "bold"), bg=colores['secundario'], fg='black')
        etiqueta_periodo.pack(pady=10, anchor="center")  # Centrar etiqueta

        for unidad in periodos_unidades[periodo]:
            boton_unidad = tk.Button(frame_izquierdo, text=unidad, command=lambda u=unidad: mostrar_clases(u))
            aplicar_estilo(boton_unidad, color_fondo='quinto', color_texto='black')
            boton_unidad.pack(pady=5, padx=20, anchor="center")  # Centrar botón

        if periodo == "Periodo 1":
            tk.Label(frame_izquierdo, bg=colores['secundario']).pack(pady=20)  # Espacio entre periodos 1 y 2

  
    for periodo in ["Periodo 3", "Periodo 4"]:
        etiqueta_periodo = tk.Label(frame_derecho, text=periodo, font=("Helvetica", 14, "bold"), bg=colores['secundario'], fg='black')
        etiqueta_periodo.pack(pady=10, anchor="center")  # Centrar etiqueta

        for unidad in periodos_unidades[periodo]:
            boton_unidad = tk.Button(frame_derecho, text=unidad, command=lambda u=unidad: mostrar_clases(u))
            aplicar_estilo(boton_unidad, color_fondo='quinto', color_texto='black')
            boton_unidad.pack(pady=5, padx=20, anchor="center")  # Centrar botón

        # Añadir un espacio adicional entre los periodos
        if periodo == "Periodo 3":
            tk.Label(frame_derecho, bg=colores['secundario']).pack(pady=20)  # Espacio entre periodos 3 y 4

    
    boton_volver = tk.Button(root, text="Volver a la Página Principal", command=mostrar_pagina_principal)
    aplicar_estilo(boton_volver, color_fondo='quinto', color_texto='black')
    boton_volver.pack(side="bottom", pady=20, padx=20, anchor="center")  # Colocar el botón al final

#clases
def mostrar_clases(unidad):
    for widget in root.winfo_children():
        widget.destroy()
    root.title(f"Clases de {unidad}")
    titulo = tk.Label(root, text=f"Clases de {unidad}", font=('Helvetica', 18, 'bold'), bg=colores['secundario'], fg='black')
    titulo.pack(pady=20)

    aplicar_degradado(colores['primario'], colores['secundario'])  # Cambia estos colores para el fondo degradado
    
    clases_por_unidad = {
        "Unidad 1": ["Clase 1.1: Operaciones con raíces cuadradas (Repaso)", 
                     "Clase 1.2: Operaciones combinadas con raíces cuadradas (Repaso)", 
                     "Clase 1.3: Racionalización con denominador √a",
                     "Clase 1.4: Racionalización con denominador binomio",
                     "Clase 1.5: Los números neperiano y áureo",
                     "Clase 1.6: Definición de los números reales: la recta numérica",
                     "Clase 1.7: Definición de los números reales: números decimales",],

        "Unidad 2": ["Clase 1.1: Definición de monomio, polinomio y grado",
                     "Clase 1.2: Productos de binomio por binomio, parte 1",
                     "Clase 1.3: Productos de binomio por binomio, parte 2",
                     "Clase 1.4 Productos de la forma (ax + b)(cx + d)",
                     "Clase 1.5 Cubo de un binomio, parte 1",
                     "Clase 1.6 Cubo de un binomio, parte 2)",
                     "Clase 1.7 Combinaciones de productos notables",
                     ],
      
    }
    clases = clases_por_unidad.get(unidad, [])
    for clase in clases:
        boton_clase = tk.Button(root, text=clase, command=lambda c=clase: mostrar_contenido_clase(c, unidad))
        aplicar_estilo(boton_clase, color_fondo='quinto', color_texto='black')
        boton_clase.pack(pady=10)
    boton_volver = tk.Button(root, text="Volver a las Unidades", command=mostrar_temas)
    aplicar_estilo(boton_volver, color_fondo='quinto', color_texto='black')
    boton_volver.pack(pady=20)

# Función para animar texto (sin cambios)
def animar_texto(etiqueta, texto, indice=0, delay=100):
    if indice <= len(texto):
        etiqueta.config(text=texto[:indice])
        indice += 1
        etiqueta.after(delay, animar_texto, etiqueta, texto, indice)

def mostrar_contenido_clase(clase, unidad="Unidad 1"):
    for widget in root.winfo_children():
        widget.destroy()

    if clase == "Clase 1.1: Operaciones con raíces cuadradas (Repaso)":
        teoria = "Teoría:\n\nLa raíz cuadrada es una operación matemática\nque se realiza sobre un número para conocer qué\notro número, multiplicado por sí mismo, da como\nresultado el número original"
        demostracion = "Demostración:\n\na) √6 x 10\n= √ (2×3) x (2 × 5)\n= 121×3×5\n=2√3x5\n= 2√15\nPor lo tanto, √6 x 10 = 2 √15\n Demostración 2:\n\nb) √12+ √75\nSe simplifican las raíces cuadradas\n√12 = √22x3\n= 2√3\n√75 = √3x5 =513\nse efectúa la suma de términos semejantes:\n√12+ √75 = 2√3+5√3 = 7√3"
        conclusion = "Conclusión:\n\nse efectúa la resta de términos semejantes: \n√18-√50 = 3√2-5√2= -212\nUn número b es raíz cuadrada de un número \na si al elevar al cuadrado el número b se obtiene\n el número a, es decir b2 = a."
        practica_1 = "Práctica 1:\nResuelve: √9 × √10 = ?"
        practica_2 = "Práctica 2:\nResuelve: √5 + √5 = ?"
        respuestas_posibles_1 = ["√60", "3√10", "10"]
        respuestas_posibles_2 = ["2√10", "2√5", "√8"]
        respuesta_correcta_1 = "3√10"
        respuesta_correcta_2 = "2√5"
        
    elif clase == "Clase 1.2: Operaciones combinadas con raíces cuadradas (Repaso)":
        teoria = "Teoría:\n\nLas operaciones combinadas con raíces cuadradas \ninvolucran la aplicación simultánea de varias operaciones \nmatemáticas, como suma, resta, multiplicación y división, \nen expresiones que contienen raíces cuadradas. Para resolver \nestas expresiones, es importante seguir el orden de operaciones\n(paréntesis, exponentes, multiplicación y división, suma y resta), \nasí como aplicar correctamente las propiedades de los radicales,\ncomo la simplificación de raíces y la racionalización de denominadores. "
        demostracion = "Demostración:\n\na) √2(√6 + √10)\n=√2 × 6+12 × 10\n=- √12+120\n=-12x3+12x5\n=-213+215.\nPor lo tanto, √(√ √10)-23+25\nAplicando la propiedad distributiva,\nse puede hacer la descomposición prima de una sola vez,\n\nb) (√2 + √15)\n(√2+15) √5-6) =√2 × 15 - √2 × √6 + √15 × 15-V15x15 Efectuando el producto,\n=-125-2√√√352\nrealizando la descomposición prima,\n=-10-2√3+513-310\nPor lo tanto, (√√5) (√5-6) =-2√30+3√3."
        conclusion = "Conclusión:\n\nEn las operaciones combinadas con radicales se realizan los siguientes pasos:\n1. Se efectúan las multiplicaciones y divisiones.\n2. Se simplifican las raíces cuadradas.\n3. Se efectúan las sumas y restas de raíces semejantes."
        practica_1 = "Práctica 1:\nEfectúa las siguientes operaciones:\nRecuerda la propiedad distributiva y los productos notables:\n\na)√2(√14+ √5)="
        practica_2 = "Práctica 2:\nb)√6(√3-√8)="
        respuestas_posibles_1 = ["2√5+√9", "2√3+√9", "2√5+√10"]
        respuestas_posibles_2 = ["2√2-2√3", "4√2-4√3", "4√7-4√9"]
        respuesta_correcta_1 = "2√5+√10"
        respuesta_correcta_2 = "4√2-4√3"
        
    elif clase == "Clase 1.3: Racionalización con denominador √a":
        teoria = "Teoría:\n\nLa racionalización es una técnica matemática\nutilizada para simplificar fracciones que contienen\nradicales en el denominador. Cuando encontramos\nuna fracción con una raíz cuadrada, es común que\ndeseemos racionalizar esta fracción, es decir,\neliminar la raíz del denominador para facilitar\nsu manipulación y comprensión."
        demostracion = "Demostración:\n\nLa racionalización elimina radicales del\n denominador multiplicando la fracción \n por el conjugado del denominador. \n Al hacerlo, los radicales se cancelan \n gracias a la propiedad de la diferencia \n de cuadrados, dejando un denominador \n racional y simplificando la expresión."
        conclusion = "Conclusión:\n\n La racionalización elimina radicales del \n denominador multiplicando la fracción \n por el conjugado del denominador. \n Al hacerlo, los radicales se cancelan \n gracias a la propiedad de la diferencia \n de cuadrados, dejando un denominador \n racional y simplificando la expresión."
        practica_1 = "Práctica 1:\na)3/√6="
        practica_2 = "Práctica 2:\nb)2/√20="
        respuestas_posibles_1 = ["√5/8", "2√/9", "√6/2"]
        respuestas_posibles_2 = ["2/√3", "√5/5", "4/4√"]
        respuesta_correcta_1 = "√6/2"
        respuesta_correcta_2 = "√5/5"
    
    frame_contenido = tk.Frame(root, bg=colores['secundario'])
    frame_contenido.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    etiqueta_titulo_clase = tk.Label(root, text=clase, font=("Helvetica", 24, "bold"), bg=colores['secundario'], fg='black')
    etiqueta_titulo_clase.grid(row=0, column=0, padx=10, pady=20, sticky="n")
    
    etiqueta_teoria = tk.Label(frame_contenido, text="", wraplength=300, justify="left", font=("Helvetica", 14), bg=colores['secundario'], fg='black')
    etiqueta_teoria.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    animar_texto(etiqueta_teoria, teoria)

    etiqueta_demostracion = tk.Label(frame_contenido, text="", wraplength=300, justify="left", font=("Helvetica", 14), bg=colores['secundario'], fg='black')
    etiqueta_demostracion.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    animar_texto(etiqueta_demostracion, demostracion)

    etiqueta_conclusion = tk.Label(frame_contenido, text="", wraplength=300, justify="left", font=("Helvetica", 14), bg=colores['secundario'], fg='black')
    etiqueta_conclusion.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
    animar_texto(etiqueta_conclusion, conclusion)

    frame_practica = tk.Frame(frame_contenido, bg=colores['secundario'])
    frame_practica.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

    etiqueta_practica_1 = tk.Label(frame_practica, text="", wraplength=300, justify="left", font=("Helvetica", 14), bg=colores['secundario'], fg='black')
    etiqueta_practica_1.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
    animar_texto(etiqueta_practica_1, practica_1)

    combo_respuesta_1 = ttk.Combobox(frame_practica, values=respuestas_posibles_1)
    combo_respuesta_1.grid(row=1, column=0, padx=10, pady=5)

    def verificar_practica_1():
        respuesta_1 = combo_respuesta_1.get().strip()
        if respuesta_1 == respuesta_correcta_1:
            resultado_1 = "¡Correcto!"
        else:
            resultado_1 = "Incorrecto, inténtalo de nuevo."
        etiqueta_resultado_1.config(text=resultado_1)

    boton_verificar_1 = tk.Button(frame_practica, text="Verificar práctica 1", command=verificar_practica_1, font=("Arial", 12), bg=colores['quinto'], fg='black')
    boton_verificar_1.grid(row=2, column=0, padx=10, pady=5)

    etiqueta_resultado_1 = tk.Label(frame_practica, text="", font=("Arial", 12), bg=colores['secundario'])
    etiqueta_resultado_1.grid(row=3, column=0, padx=10, pady=5)

    # Práctica 2
    etiqueta_practica_2 = tk.Label(frame_practica, text="", wraplength=300, justify="left", font=("Helvetica", 14), bg=colores['secundario'], fg='black')
    etiqueta_practica_2.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")
    animar_texto(etiqueta_practica_2, practica_2)

    combo_respuesta_2 = ttk.Combobox(frame_practica, values=respuestas_posibles_2)
    combo_respuesta_2.grid(row=5, column=0, padx=10, pady=5)

    def verificar_practica_2():
        respuesta_2 = combo_respuesta_2.get().strip()
        if respuesta_2 == respuesta_correcta_2:
            resultado_2 = "¡Correcto!"
        else:
            resultado_2 = "Incorrecto, inténtalo de nuevo."
        etiqueta_resultado_2.config(text=resultado_2)

    boton_verificar_2 = tk.Button(frame_practica, text="Verificar práctica 2", command=verificar_practica_2, font=("Arial", 12), bg=colores['quinto'], fg='black')
    boton_verificar_2.grid(row=6, column=0, padx=10, pady=5)

    etiqueta_resultado_2 = tk.Label(frame_practica, text="", font=("Arial", 12), bg=colores['secundario'])
    etiqueta_resultado_2.grid(row=7, column=0, padx=10, pady=5)

    boton_volver = tk.Button(root, text="Volver a las Clases", command=lambda: mostrar_clases(unidad), font=("Arial", 16, "bold"), bg=colores['quinto'], fg='black')
    boton_volver.grid(row=1, column=0, pady=20, padx=10, sticky="s")


# Funciones para mostrar cada examen
def mostrar_examen(examen_numero):
    for widget in root.winfo_children():
        widget.destroy()
    root.title(f"Examen {examen_numero}")
    aplicar_degradado(colores['primario'], colores['secundario'])

    etiqueta_examen = tk.Label(root, text=f"Contenido del Examen {examen_numero}", font=("Arial", 16, "bold"), bg=colores['secundario'], fg='black')
    etiqueta_examen.pack(pady=20)

    frame_ejercicios = tk.Frame(root, bg=colores['secundario'])
    frame_ejercicios.pack(pady=10)

    ejercicios = [
       "1. Resuelve: √9 × √10 =",
            "2. Resuelve: √2(√14+ √5)=",
            "3. Resuelve: 3/√15",
            "4. Resuelve: Calcula una aproximación \ndel número (e)\nusando la expresión\n(1 + 1/n)^n para n = 10000.",
            "5. Resuelve: =∣ 7/10∣=",
    ]
    for i, ejercicio in enumerate(ejercicios):
        etiqueta_ejercicio = tk.Label(frame_ejercicios, text=ejercicio, font=("Arial", 12), bg=colores['secundario'], fg='black')
        etiqueta_ejercicio.grid(row=i, column=0, padx=10, pady=5, sticky='w') 

        respuestas = ["10", "11", "12", "13", "14", "15", "16", "17"]  
        combo_respuestas = ttk.Combobox(frame_ejercicios, values=respuestas)
        combo_respuestas.grid(row=i, column=1, padx=10, pady=5) 

        boton_verificar = tk.Button(frame_ejercicios, text="Verificar Respuesta", command=lambda idx=i: verificar_respuesta(combo_respuestas.get(), respuestas_correctas[idx]))
        aplicar_estilo(boton_verificar, color_fondo='quinto', color_texto='black')
        boton_verificar.grid(row=i, column=2, padx=10, pady=5) 

    boton_volver = tk.Button(root, text="Volver a Exámenes", command=mostrar_examenes)
    aplicar_estilo(boton_volver, color_fondo='quinto', color_texto='black')
    boton_volver.pack(pady=20)

respuestas_correctas = ["12", "7", "16", "4", "27", "15", "18", "4"]

def verificar_respuesta(respuesta_seleccionada, respuesta_correcta):
    if respuesta_seleccionada == respuesta_correcta:
        messagebox.showinfo("Resultado", "¡Correcto!")
    else:
        messagebox.showerror("Resultado", "Incorrecto. Inténtalo de nuevo.")

def mostrar_examenes():
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Exámenes")
    aplicar_degradado(colores['primario'], colores['secundario'])  
    
    etiqueta_examenes = tk.Label(root, text="Aquí puedes realizar exámenes para practicar.", font=("Arial", 16, "bold"), bg=colores['secundario'], fg='black')
    etiqueta_examenes.pack(pady=20)

    for i in range(1, 5):
        boton_examen = tk.Button(root, text=f"Examen {i}", command=lambda num=i: mostrar_examen(num))
        aplicar_estilo(boton_examen, color_fondo='quinto', color_texto='black')
        boton_examen.pack(pady=5)

    boton_volver = tk.Button(root, text="Volver a la Página Principal", command=mostrar_pagina_principal)
    aplicar_estilo(boton_volver, color_fondo='quinto', color_texto='black')
    boton_volver.pack(pady=20)

# Ventana principal
root = tk.Tk()
root.geometry("700x500")
mostrar_pagina_principal()
root.mainloop()