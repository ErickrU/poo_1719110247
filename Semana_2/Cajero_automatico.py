class cajeroautomatico:

  #atributos
  Ub=input(str("Lugar "))
  compania=input(str("compania "))
  saldo=input(str("Saldo "))
  operaciones=input(str("operaciones "))
  color=input(str("Color "))
  material=input(str("Material "))
  ndebotones=input(str("Numero de botones "))
  pantallatactil=True
  tipodecajero=input(str("Tipo de cajero "))
  camaradeseguridad=True

  #metodos
  def __init__(self):
    print("\nConstructor Cajero automatico")

  def rdp(self):
    print("Realizar depositos")

  def rd(self):
    print("Retirar dinero")

  def pgsv(self):
    print("Pagar servicios")

  def Adqs(self):
    print("Adquiere servicos")

  def sbm(self):
    print("Saber mi saldo")

objeto_cajero=cajeroautomatico()
objeto_cajero.rdp()
objeto_cajero.rd()
objeto_cajero.pgsv()
objeto_cajero.Adqs()
objeto_cajero.sbm()