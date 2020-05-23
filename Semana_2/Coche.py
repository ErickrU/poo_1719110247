class coche:

  #atributos
  color=input(str("Cual es el color? "))
  modelo=input(str("Cual es el modelo? "))
  ndellantas=input(str("Numero de llantas "))
  ndepuertas=input(str("Numero de puertas "))
  tipodecombustible=input(str("Tipo de compustible "))
  tipodemotor=input(str("Tipo de motor "))
  tienequemacocos=False
  print("Tiene quemacocos = ",tienequemacocos)
  empresadefacturado=input(str("Empresa de facturacion "))
  escaladeseguridad=input(str("Escala de seguridad "))
  tipodefreno=input(str("Tipo de freno "))

  #metodos
  def __init__(self):
    print("\nConstructor coche")

  def acelerar(self):
    print("Acelerar")

  def frenar(self):
    print("Frenar")

  def apagar(self):
    print("Apagar")

  def encender(self):
    print("Encender")

  def repostar(self):
    print("Repostar")

objeto_coche=coche()
objeto_coche.acelerar()
objeto_coche.frenar()
objeto_coche.apagar()
objeto_coche.encender()
objeto_coche.repostar()