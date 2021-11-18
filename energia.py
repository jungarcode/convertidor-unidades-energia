from tkinter import *
from tkinter import ttk
#from ttkthemes import themed_tk

root = Tk()
root.title("Convertidor Unidades Energia")
root.geometry("460x440+427+100")
#root.themed_tk.ThemedTk(theme="itft1")
root.resizable(False,False)
root.config(bg="#9699F0")

unidades = [
    "julios(j)",
    "kilovatios hora(KWh)",
    "Electrovoltio(eV)",
    "Uni.Term.Britanica(BTU)",
    "Toneladas Petroleo(TOE)",
    "Toneladas Carbon(TCE)", 
]
conversiones = [
    1,
    2.778*10 ** -7,
    6.242*10**18,
    0.000947817,
    0.00000000002388,
    0.00000000003
]

def converter():
    try:
        op1 = menu1.get()
        op2 = menu2.get()
        entrada = float(entri1.get())

        pos_op1 = unidades.index(op1)
        pos_op2 = unidades.index(op2)
        
       
        # Conversion de j a todas las demas unidades
        
        if op1 == unidades[0] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        if op1 == unidades[0] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[0] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[0] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[0] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[0] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op1] * conversiones[pos_op2])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
            
        # conversiones de kwh a demas unidades
        
        elif  op1 == unidades[1] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[1] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[1] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[1] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[1] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[1] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
            
        # convertir de eV a demas unidades  
        
        elif  op1 == unidades[2] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[2] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[2] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[2] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[2] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[2] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        
        # convertir de BTU a demas unidades  
        
        elif  op1 == unidades[3] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[3] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[3] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[3] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[3] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[3] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
            
        # convertir de TOE a demas unidades  
        
        elif  op1 == unidades[4] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[4] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[4] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[4] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[4] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[4] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        
         # convertir de TOE a demas unidades  
        
        elif  op1 == unidades[5] and op2 == unidades[0]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[5] and op2 == unidades[1]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[5] and op2 == unidades[2]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[5] and op2 == unidades[3]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[5] and op2 == unidades[4]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
        elif  op1 == unidades[5] and op2 == unidades[5]:
            conv_j_kwh = entrada * (conversiones[pos_op2] / conversiones[pos_op1])
            resultado['text'] = str (format(conv_j_kwh,'.1E'))
              
    except ValueError:
        resultado['text'] = "solo numeros"

def limpiar():
    entri1.delete(0,END)
    resultado["text"]=""

labelframe = LabelFrame(root,text="Energia",bg="#162215",font=("Arial",20,"bold"),bd=5,fg="#03C000")
labelframe.grid(column=0,row=0,padx=10,pady=10,ipady=10)

entri1 = Entry(labelframe,width=15,font=("Calibri",14,"bold"),justify=CENTER)
entri1.grid(column=0,row=0,padx=5,pady=5,ipady=10,ipadx=10)
entri1.insert(0, "Valor a Convertir")
entri1.configure(state=DISABLED)
entri1.focus()
def click(event):
    entri1.configure(state=NORMAL)
    entri1.delete(0,END)
entri1.bind("<Double-Button-1>",click)

resultado = Label(labelframe,text="Conversion",bg="#E0E0E0",font=("Calibri",20))
resultado.grid(column=1,row=0,padx=5,pady=5,ipady=10,ipadx=15)

menu1 = ttk.Combobox(labelframe,values=unidades,justify= "center")
menu1.grid(column=0,row=1,padx=10,pady=10,ipady=5)
menu1.current(0)

menu2 = ttk.Combobox(labelframe,values=unidades,justify= "center")
menu2.grid(column=1,row=1,padx=10,pady=10,ipady=5)
menu2.current(1)

button1 = Button(labelframe,text="Limpiar",bg="#03C000")
button1.grid(column=0,row=2,padx=10,pady=10)

button2 = Button(labelframe,text="Convertir",command=converter,bg="#03C000")
button2.grid(column=1,row=2,padx=10,pady=10)

root.mainloop()