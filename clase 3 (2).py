class Person:
    def __init__(self, name,age, ced,tel):
        self._name=name
        self._age=age
        self._ced=ced
        self._tel=tel
        
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
            
    def get_ced(self):
        return self._ced
    def set_ced(self, new_ced):
        if isinstance(new_ced,int) & new_ced > 0 & new_ced < 120:
            self._ced=new_ced
    
    def get_tel(self):
        return self._tel
    def set_tel(self, new_tel):
        if isinstance(new_tel,int) & new_tel > 0 & new_tel < 120:
            self._tel=new_tel
    
    def __str__(self):
        return 'Person[' + str(self._name) +'] is ' + 'Age [' + str(self._age)+'] is ' + 'ID [' + str(self._ced)+'] is ' + ' Phone['+str(self._tel)

