import ctypes
from tkinter import Tk, Button, font, Text, END, Label

# Loading the API
house_control_library = ctypes.CDLL('./house_control.dll')

armado_total = house_control_library.armado_total
armado_parcial = house_control_library.armado_parcial
desactivar = house_control_library.desactivar
anular_zona = house_control_library.armado_total
panico = house_control_library.panico
emergencia_medica = house_control_library.emergencia_medica

root = Tk()
root.title("Sistema controlador de Domicilio")

# Button styles
button_font = font.Font(size=11)
button_width = 16
button_height = 3
button_relief = "raised"
button_borderwidth = 4

# Defining functions return type
armado_total.restype = ctypes.c_char_p
armado_parcial.restype = ctypes.c_char_p
desactivar.restype = ctypes.c_char_p
panico.restype = ctypes.c_char_p
emergencia_medica.restype = ctypes.c_char_p


# Function for decoding the received text and updating the label
def update_output(text):
    text = text.decode("utf-8")
    output_label.config(text=f'Estado actual: {text}')

# Button commands to call C functions and update the UI
def call_armado_total():
    text = armado_total()

    update_output(text)

def call_armado_parcial():
    text = armado_parcial()  
    update_output(text)

def call_desactivar():
    text = desactivar()
    print(text)
    update_output(text)

def call_anular_zona():
    text = anular_zona()  
    update_output(text)

def call_panico():
    text = panico()  
    update_output(text)

def call_emergencia_medica():
    text = emergencia_medica()  
    update_output(text)


output_label = Label(root, text="", height=4, width=30, relief='flat', anchor='center', justify='center', font=('Arial', 14))
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


# Creating buttons and placing them in a grid
armado_total_btn = Button(root, text="Armado Total", command=call_armado_total,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)
armado_parcial_btn = Button(root, text="Armado Parcial", command=call_armado_parcial,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)
desactivar_btn = Button(root, text="Desactivar", command=call_desactivar,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)
anulzar_zona_btn = Button(root, text="Anular Zona", command=call_anular_zona,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)
panico_btn = Button(root, text="Panico", command=call_panico,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)
emergencia_medica_btn = Button(root, text="Emergencia Medica", command=call_emergencia_medica,
                 width=button_width, height=button_height, font=button_font,
                 relief=button_relief, bd=button_borderwidth)

armado_total_btn.grid(row=0, column=0, padx=10, pady=10)

armado_parcial_btn.grid(row=0, column=1, padx=10, pady=10)

desactivar_btn.grid(row=1, column=0, padx=10, pady=10)

anulzar_zona_btn.grid(row=1, column=1, padx=10, pady=10)

panico_btn.grid(row=2, column=0, padx=10, pady=10)

emergencia_medica_btn.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
