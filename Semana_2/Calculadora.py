class calculadora:

  #Atributo
  botones=True
  print("Botones = ",botones)
  color=input(str("color "))
  forma=input(str("Forma "))
  marca=input(str("Marca "))
  modelo=input(str("Modelo "))
  funciones=input(str("Funciones "))
  tcalculadora=input(str("Tipo de calculadora "))
  fdealim=input(str("Fuente de alimentacion "))
  Tpantalla=input(str("Tipo de pantalla "))

  #Metodos
  def __init__(self):
    print("\nconstructor calculadora")
  
  def sumar(self):
    print("Sumar")

  def restar(self):
    print("Restar")
  
  def dividir(self):
    print("Dividir")

  def multiplicar(self):
    print("Multiplicar")

  def RC(self):
    print("Raiz cuadrada")

objeto_cal=calculadora()
objeto_cal.sumar()
objeto_cal.restar()
objeto_cal.dividir()
objeto_cal.multiplicar()
objeto_cal.RC()