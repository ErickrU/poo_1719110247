class Cajeroautomatico_Clase:
  
  #atributos
  ubicacion_variable=          input(str("Lugar "))
  compania_variable=           input(str("compania "))
  saldo_variable=              input(str("Saldo "))
  color_variable=              input(str("Color "))
  material_variable=           input(str("Material "))

  #metodos
  def __init__(self):
    pass

  def retirarMetodo(self):
    print("Retirar dinero")

  def consultarMetodo(self):
    print("Consultar saldo")

class Practicaja_Clase(Cajeroautomatico_Clase):

  #atributos
  operaciones_variable=        input(str("operaciones "))
  numerodebotones_variable=    input(str("Numero de botones "))
  pantallatactil_variable=True
  print("Pantalla Tactil = ",pantallatactil_variable)
  tipodecajero_variable=       input(str("Tipo de cajero "))
  camaradeseguridad_variable=True
  print("Camara de seguridad = ",camaradeseguridad_variable)

  #metodos
  def __init__(self):
    pass

  def transferenciabancariaMetodo(self):
    print("Realizar una tranferencia bancaria")

  def pagarservicioMetodo(self):
    print("Pagar servicio")

obj_caj = Practicaja_Clase()
print("")
obj_caj.retirarMetodo()
obj_caj.consultarMetodo()
obj_caj.transferenciabancariaMetodo()
obj_caj.pagarservicioMetodo()