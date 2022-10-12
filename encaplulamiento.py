
class Person:
    def __init__(self, name, age, ci, celu):
        self._name=name
        self._age=age
        self._ci=ci
        self._celu=celu
        
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if isinstance(new_name,int) & new_name > 0 & new_name < 120:
            self._name=new_name        
        
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        if isinstance(new_age,int) & new_age > 0 & new_age < 120:
            self._age=new_age
            
    def get_ci(self):
        return self._ci
    def set_ci(self, new_ci):
        if isinstance(new_ci,int) & new_ci > 0 & new_ced < 11:
            self._ci=new_ci
    
    def get_celu(self):
        return self._celu
    def set_celu(self, new_celu):
        if isinstance(new_celu,int) & new_celu > 0 & new_celu < 11:
            self._celu=new_celu
    
    def __str__(self):
        return 'Ciudadano[' + str(self._name) +'] es ' + 'Edad [' + str(self._age)+'] es ' + 'C.I [' + str(self._ci)+'] es ' + ' Celular['+str(self._celu) +'] es'
        
Patricio=Person("Patricio Haro", "25", "1720184314", "0988701423")
print("Nombre:", Patricio._name)
print("Edad:", Patricio._age)
print("C.I:", Patricio._ci)
print("Celular:", Patricio._celu)