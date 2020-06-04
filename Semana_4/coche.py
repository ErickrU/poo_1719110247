class CocheClase:
  
  #atributos
  tipodefreno_variable=              input(str("Tipo de freno "))
  modelo_variable=                   input(str("Cual es el modelo? "))
  numerodellantas_variable=          input(str("Numero de llantas "))
  numerodepuertas_variable=          input(str("Numero de puertas "))
  empresadefacturado_variable=       input(str("Empresa de facturacion "))

  #metodos
  def __init(self):
    pass

  def acelerarMetodo(self):
    print("Acelerar")

  def frenarMetodo(self):
    print("Frenar")

class CocheElectricoClase(CocheClase):

  #atributos
  color_variable=              input(str("Cual es el color? "))
  tipodebateria_variable=      input(str("Tipo de bateria "))
  tipodemotor_variable=        input(str("Tipo de motor "))
  tienequemacocos=False
  print("Tiene quemacocos = ",tienequemacocos)
  escaladeseguridad_variable=  input(str("Escala de seguridad "))

  #metodo
  def __init__(self):
    pass

  def cargarapidaMetodo(self):
    print("Carga super rapida")

  def conduccionasistidaMetodo(self):
    print("Conduccion asistida")

  def acelerarMetodo(self):
    print("Acelerar coche electrico")

  def frenarMetodo(self):
    print("Frenar coche electrico")

obj_elect = CocheElectricoClase()
print("")
obj_elect.acelerarMetodo()
obj_elect.frenarMetodo()
obj_elect.cargarapidaMetodo()
obj_elect.conduccionasistidaMetodo()