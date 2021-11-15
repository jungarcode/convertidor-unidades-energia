from tkinter import *
from tkinter import ttk
#from ttkthemes import themed_tk

root = Tk()
root.title("Convertidor Unidades Energia")
root.geometry("440x400")
#root.themed_tk.ThemedTk(theme="itft1")
root.resizable(False,False)
root.config(bg="blue2")

unidades = [
    "julios (j)",
    "kilovatios hora (KWh)",
    "Electrovoltio (eV)",
    "Unid. Term.Britanica (BTU)",
    "Toneladas Petroleo (TOE)",
    "Toneladas Carbon (TCE)", 
]

labelframe = LabelFrame(root,text="Convertir",bg="cyan2",font=("Arial"),bd=5)
labelframe.grid(column=0,row=0,padx=10,pady=10)

entri1 = Entry(labelframe,width=15)
entri1.grid(column=0,row=0,padx=5,pady=5,ipady=10,ipadx=10)
entri1.insert(0, "Valor a Convertir")
entri1.configure(state=DISABLED)
entri1.focus()
def click(event):
    entri1.configure(state=NORMAL)
    entri1.delete(0,END)
entri1.bind("<Button-1>",click)
entri2 = Entry(labelframe,width=15)
entri2.grid(column=1,row=0,padx=5,pady=5,ipady=10,ipadx=10)
entri2.insert(0, "Valor Convertido")
entri2.configure(state=DISABLED)
def click(event):
    pass
entri2.bind("<Button-1>",click)
menu1 = ttk.Combobox(labelframe,values=unidades,justify= "center")
menu1.grid(column=0,row=1,padx=10,pady=10)
menu1.current(0)

menu2 = ttk.Combobox(labelframe,values=unidades,justify= "center")
menu2.grid(column=1,row=1,padx=10,pady=10)
menu2.current(1)

button1 = ttk.Button(labelframe,text="Limpiar")
button1.grid(column=0,row=2,padx=10,pady=10)

button2 = ttk.Button(labelframe,text="Convertir")
button2.grid(column=1,row=2,padx=10,pady=10)

root.mainloop()