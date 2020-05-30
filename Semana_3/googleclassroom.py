class GoogleClassroomClase:

  #atributos
  credenciales_variable=        input(str("Credenciales "))
  formato_variable=             input(str("Formato "))
  diseno_variable=              input(str("Diseno "))
  materias_variable=            input(str("Materias "))
  apartados_variable=           input(str("Apartados "))

  #metodos
  def __init__(self):
    pass  

  def entregartareasMetodo(self):
    print("Entregar tareas")

  def recibirtareasMetodo(self):
    print("Recibir tareas")

class GoogleClassroomMaestrosClase(GoogleClassroomClase):


  #atributos
  calendario_variable=          input(str("Calendario "))
  calificaciones_variabls=      input(str("Calificaciones "))
  estado_variable=              input(str("Estado "))
  version_variable=             input(str("version "))
  profesor=True
  print("Profesor", profesor)
  
  #metodos
  def __init__(self):
    pass

  def retroalimentacionMetodo(self):
    print("Retroalimentar la clase")

  def calificacionMetodo(self):
    print("Cailificar tareas")

obj_clase = GoogleClassroomMaestrosClase()
print("")
obj_clase.entregartareasMetodo()
obj_clase.recibirtareasMetodo()
obj_clase.retroalimentacionMetodo()
obj_clase.calificacionMetodo()