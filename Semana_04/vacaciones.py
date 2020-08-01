class VacacionesClase:
  
  #atributos
  lugar_variable=                input(str("Lugar "))
  duracion_variable=             input(str("Duracion "))
  numerodeacompanates_variable=  input(str("Numero de acompantes "))
  costo_variable=                input(str("Costo "))

  #metodos
  def __init__(self):
    pass

  def relajarMetodo(self):
    print("Relajar")

  def descansarMetodo(self):
    print("Descansar")

class VacacionesDeTrabajoClase(VacacionesClase):

  #atributos
  empresa_variable=              input(str("Empresa que paga las vaciones"))
  motivo_variable=               input(str("Motivo de las vaciones de trabajo"))


  #metodos
  def __init__(self):
    pass

  def propositoMetodo(self):
    print("Conseguir la reunion")

  def relajarMetodo(self):
    print("Relajar en vacaciones de trabajo")

  def descansarMetodo(self):
    print("Descansar en vacaciones de trabajo ")

obj_vaca = VacacionesDeTrabajoClase()
print("")
obj_vaca.relajarMetodo()
obj_vaca.descansarMetodo()
obj_vaca.propositoMetodo()