class UnBancoClase:
  
  #atrbutos
  empresa_variable=                       input(str("Empresa "))
  ndesucursales_variable=                 input(str("Numero de sucursales "))
  ndeclientes_variable=                   input(str("Numero de clientes "))
  ndecajeros_variable=                    input(str("Numero de cajeros "))
  ndeempleados_variable=                  input(str("Numero de empleados "))

  #metodos
  def __init__(self):
    pass

  def retirardineroMetodo(self):
    print("Retirar dinero")

  def realizardepositoMetodo(self):
    print("Realizar depositos")

class BancoLocalClase(UnBancoClase):

  #atributos
  registrofederal_variable=               input(str("Registro federal "))
  seguridadfinanciera_variable=           input(str("Seguridad financiera "))
  extranjero=False
  print("Extranjero = ",extranjero)

  #metodos
  def __init__(self):
    pass

  def realizarchequesMetodo(self):
    print("Realizar cheques")

  def crearcuentaMetodo(self):
    print("Crar cuentas")

  def retirardineroMetodo(self):
    print("Retirar dinero de un banco local")

  def realizardepositoMetodo(self):
    print("Realizar depositos de un banco lolcal")

obj_bl = BancoLocalClase()
print("")
obj_bl.retirardineroMetodo()
obj_bl.realizardepositoMetodo()
obj_bl.realizarchequesMetodo()
obj_bl.crearcuentaMetodo()