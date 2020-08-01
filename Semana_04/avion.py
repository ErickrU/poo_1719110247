class AvionClase:
  
  #atributos 
  modelo_variable=input(str("Modelo "))
  tipodemotor_varible=input(str("Tipo de motor "))
  velocidaddecrucero_variable=input(str("Velocidad crucero "))
  color_variable=input(str("color "))
  altitudmaximasoportada_variable=input(str("Altitud maxima soportada por el avion "))

  #metodos 
  def __init__(self):
    pass

  def aterrizarMetodo(self):
    print("Aterrizar")

  def despegarMetodo(self):
    print("Despegar")

class AvionComercialClase(AvionClase):

  #atributos
  tipodealerones_variable=input(str("Tipo de alerones "))
  numerodepropulsores_variable=input(str("numero de propulsores "))
  pesodelavion_variable=input(str("peso del avion "))
  manu_variable=input(str("Empresa de manofacturacion "))
  Tdecombustible_variable=input(str("Tipo de combustible "))

  #metodos 
  def __init__(self):
    pass

  def volarMetodo(self):
    print("volar")

  def repostarMetodo(self):
    print("repostar")

  def aterrizarMetodo(self):
    print("Aterrizar el avion comercial")

  def despegarMetodo(self):
    print("Despegar el avion comercial")


objeto_av = AvionComercialClase()
print("")
objeto_av.aterrizarMetodo()
objeto_av.volarMetodo()
objeto_av.despegarMetodo()
objeto_av.repostarMetodo()
































