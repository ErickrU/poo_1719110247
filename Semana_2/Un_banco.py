class unbanco:

  #atrinutos
  empresa=input(str("Empresa "))
  ndesucursales=input(str("Numero de sucursales "))
  ndeclientes=input(str("Numero de clientes "))
  ndecajeros=input(str("Numero de cajeros "))
  ndeempleados=input(str("Numero de empleados "))
  rf=input(str("Registro federal "))
  ci=input(str("Conexion internacional "))
  seguridadfinanciera=input(str("Seguridad financiera "))
  extranjero=True

  #Metodos
  def __init__(self):
    print("\nconstructor un banco")

  def rdinero(self):
    print("Retirar dinero")

  def rdeposi(self):
    print("Realizar depositos")

  def rcheques(self):
    print("Realizar cheques")

  def ccuenta(self):
    print("Crar cuentas")

  def tb(self):
    print("Transferencias bancarias")

objeto_banco=unbanco()
objeto_banco.rdinero()
objeto_banco.rdeposi()
objeto_banco.rcheques()
objeto_banco.ccuenta()
objeto_banco.tb()