# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:23:54 2022

@author: lab
"""

"""Encapsulamiento: metodos getter and setter"""
class Person:
    def __init__(self, name , age):
        self._name= name # para coregir error poner ""
        self._age= age
        
    def get_age(self):
        return self._age
    
    def set_age(self,new_age):
        if isinstance(new_age, int) & new_age > 0 & new_age < 120:
            self._age= new_age 
            
    def get_name (self):
        return self._name
    
    def __str__(self):
        return 'Person[' + str(self._name)+'] in' + str (self._age)
    


    



