import tkinter
import math
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:

A) Al presionar el botón 'Agregar' se debera cargar el precio iva incluido en la lista correspondiente, 
   segun se trate de un articulo con IVA del 21% o del 10.5%.

   La condicion del articulo frente al IVA es indicada mediante una lista desplegable.

** Flotantes positivos

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar los articulos, sus precios sin iva y su posicion en la lista (por terminal)

¡¡IMPORTANTE!!

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR.

C) Al precionar el boton Informar 
    0- Valor y posicion frente al IVA del o los Articulo/s sin IVA mas caro/s
    1- Valor y posicion frente al IVA del o los Articulo/s mas barato IVA incluido
    2- Precio promedio sin IVA
    3- Precio promedio con IVA
    4- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio sin IVA
    5- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio sin IVA
    6- Valor y posicion frente al IVA del o los Articulo/s que son mas caros que el promedio con IVA
    7- Valor y posicion frente al IVA del o los Articulo/s que son mas baratos que el promedio con IVA
    8- Valor y posicion frente al IVA del o los Articulo/s cuyo valor se repite en la lista que integra
    9- Valor y posicion frente al IVA del o los Articulo/s cuyo valor NO se repite en la lista que integra

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")

        self.txt_precio_articulo = customtkinter.CTkEntry(master=self, placeholder_text="Precio")
        self.txt_precio_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_iva = customtkinter.CTkComboBox(master=self, values=["10.5","21"])
        self.combobox_iva.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_precios_21 = []
        self.lista_precio_105 = []


    def btn_agregar_on_click(self):
        iva_value = self.combobox_iva.get()
        value = self.txt_precio_articulo.get()

        if value is not None and value.isnumeric() is True and value > 0:
            alert(title = "Success", message = "Agregado")
            if iva_value == "21":
                self.lista_precios_21.append(float(value))
            else:
                self.lista_precio_105.append(float(value))

        else:
            alert(title = "ERROR", message = "ERROR - Ingrese un numero valido.")
        pass
        
    # Ultimo numero de DNI: 5
    def btn_mostrar_on_click(self):
        value_iva_21 = ""
        value_iva_10 = ""
        final_message = ""
        counter = 0

        for elemento in self.lista_precios_21:
            counter += 1
            value_iva_21 += f'Articulo {counter}: ${elemento}\n'
        if len(value_iva_21) > 0:
            final_message += "Objetos con IVA 21% (precio sin IVA):\n" + value_iva_21
        
        counter = 0

        for elemento in self.lista_precio_105:
            counter += 1
            value_iva_10 += f'Articulo {counter}: ${elemento}\n'
        if len(value_iva_10) > 0:
            final_message += "Objetos con IVA 10.5% (precio sin IVA):\n" + value_iva_10
        
        if final_message == "":
            final_message = "No hay nada que mostrar"

        alert(title="Mostrar", message=final_message)
        pass


    def btn_informar_on_click(self):
        promedio1 = 0
        counter_promedio1 = 0
        promedio2 = 0
        counter_promedio2 = 0
        counter = 0
        final_message = ""

        for elemento in self.lista_precio_105:
            promedio1 += elemento / 1.105
            counter_promedio1 += 1

        for elemento in self.lista_precios_21:
            promedio2 += elemento / 1.21
            counter_promedio2 += 1
        
        if counter_promedio1 != 0:
            promedio1 = promedio1 / counter_promedio1

            final_message += f'Promedio de articulos SIN IVA para IVA 10.5%: ${promedio1}\n'
            articulos_mayores = ""
            articulos_menores = ""
            for elemento in self.lista_precio_105:
                counter += 1
                if elemento > promedio1:                    
                    articulos_mayores += f'Articulo {counter}: ${elemento}\n'
                else:
                    articulos_menores += f'Articulo {counter}: ${elemento}\n'

            if articulos_mayores != "":
                final_message += "Elementos cuyo valor con IVA es MAYOR al promedio:\n" + articulos_mayores
            if articulos_menores != "":
                final_message += "Elementos cuyo valor con IVA es MENOR al promedio:\n" + articulos_menores
            

        if counter_promedio2 != 0:
            promedio2 = promedio2 / counter_promedio2
            
            counter = 0
            final_message += f'\n\n--------\n\nPromedio de articulos SIN IVA para IVA 21%: ${promedio2}\n'
            articulos_mayores = ""
            articulos_menores = ""
            for elemento in self.lista_precios_21:
                counter += 1
                if elemento > promedio2:                    
                    articulos_mayores += f'Articulo {counter}: ${elemento}\n'
                else:
                    articulos_menores += f'Articulo {counter}: ${elemento}\n'
            if articulos_mayores != "":
                final_message += "Elementos cuyo valor con IVA es MAYOR al promedio:\n" + articulos_mayores
            if articulos_menores != "":
                final_message += "Elementos cuyo valor con IVA es MENOR al promedio:\n" + articulos_menores
        
        alert(title="Informe", message=final_message)

        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()    