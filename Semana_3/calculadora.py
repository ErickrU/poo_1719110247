class Calculadora_Clase:
  
  #atributo
  botones_variable=True
  print("Botones = ",botones_variable)
  color_variable=              input(str("color "))
  forma_variable=              input(str("Forma "))
  marca_variable=              input(str("Marca "))
  modelo_variable=             input(str("Modelo "))

  #metodos
  def __init__(self):
    pass

  def sumarMetodo(self):
    print("Sumar")

  def restarMetodo(self):
    print("Restar")

class Calculadoracientifica_Clase(Calculadora_Clase):

  #atributos
  funciones_variable=              input(str("Funciones "))
  fuentedealimentacion_variable=   input(str("Fuente de alimentacion "))
  Tipodeantalla_variable=          input(str("Tipo de pantalla "))

  #metodos
  def __init__(self):
    pass

  def porcentajesMetodo(self):
    print("Porcentajes")

  def conversionesMetodo(self):
    print("Conversiones")

obj_cal = Calculadoracientifica_Clase()
print("")
obj_cal.sumarMetodo()
obj_cal.restarMetodo()
obj_cal.porcentajesMetodo()
obj_cal.conversionesMetodo()