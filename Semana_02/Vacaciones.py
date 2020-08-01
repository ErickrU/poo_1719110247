class vacaciones:

  #atributos
  lugar=input(str("Lugar "))
  duracion=input(str("Duracion "))
  numerodeacompanates=input(str("Numero de acompantes "))
  costo=input(str("Costo "))

  #metodos
  def __init__(self):
    print("\nContructor Vacaciones")

  def relajar(self):
    print("Relajar")

  def descansar(self):
    print("Descansar")

  def desestresarse(self):
    print("Desestresarse")

objeto_vacaciones=vacaciones()
objeto_vacaciones.relajar()
objeto_vacaciones.descansar()
objeto_vacaciones.desestresarse()