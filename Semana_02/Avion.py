class avion:

  #Atributos
  color=input(str("color "))
  modelo=input(str("Modelo "))
  manu=input(str("Empresa de manofacturacion "))
  Tdecombusticle=input(str("Tipo de combustible "))
  vcrucero=input(str("Velocidad crucero "))
  tdealerones=input(str("Tipo de alerones "))
  ndpropulsores=input(str("numero de propulsores "))
  tipodemotor=input(str("Tipo de motor "))
  pesodelavion=input(str("peso del avion "))
  amx=input(str("Altitud maxima soportada por el avion "))

  #Metodos
  def __init__(self):
    print("\nConstructor avion")

  def volar(self):
    print("volar")

  def transportar(self):
    print("Transportar")

  def aterrizar(self):
    print("Aterrizar")

  def despegar(self):
    print("Despegar")

  def repostar(self):
    print("Repostar")

objeto_avion=avion()
objeto_avion.volar()
objeto_avion.transportar()
objeto_avion.aterrizar()
objeto_avion.despegar()
objeto_avion.repostar()