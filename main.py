from tkinter import *
root = Tk()

pregunta = Label(root, text='¿Qué deporte te gusta más?').grid(row=0)
respuesta = StringVar(value=" ")

def reset_option():
    print('A tomar por culo')
    respuesta.set(None)


def option_select(value):
    value = 'Tu respuesta es ' + value
    respuesta_label = Label(root, text=value).grid(row=4)
    
opcion1 = Radiobutton(root, text='Muay Thai', value='Muay Thai', variable = respuesta, command=lambda : option_select(respuesta.get())).grid(row=1, sticky=W)
opcion2 = Radiobutton(root, text='Karate', value='Karate', variable = respuesta, command=lambda : option_select(respuesta.get())).grid(row=2, sticky=W)
opcion2 = Radiobutton(root, text='Boxeo', value='Boxeo', variable = respuesta, command=lambda : option_select(respuesta.get())).grid(row=3, sticky=W)


reset_button = Button(root, text = 'Resetear', command=reset_option).grid(row=5)


root.mainloop()