# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 09:24:43 2022

@author: lab
"""

#creando la clase, loos metodos y los atributos
class Computador:
    def __init__(self): #metodo constructor 
        self.procesador="Intel"# pbblico 
        # self._procesador="Intel"#privado 
    def almacenamiento(self,cantidad_datos):
        print("El estado del almacenamiento es:", cantidad_datos)
        
 # crear objetos definiendo variables 
       
compu_carlos_v= Computador()
# compu_carlos_u= Computador()
# compu_angelo= Computador()
print("Computadora Carlos V:",compu_carlos_v.procesador)
compu_carlos_v.almacenamiento("50 Gb")
compu_carlos_v.almacenamiento("40 Gb")
compu_carlos_v.almacenamiento("30 Gb")