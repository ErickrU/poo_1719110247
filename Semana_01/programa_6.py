class encapsulacion:

  variable_1=1   #public 
  _variable_2=2  #protected
  __variable_3=3 #private


  def __init__(self):
    print(self.variable_1)
    print(self._variable_2)
    print(self.__variable_3)     

objeto1 = encapsulacion()
print(objeto1.variable_1)
print(objeto1._variable_2)
print(objeto1.__variable_3)