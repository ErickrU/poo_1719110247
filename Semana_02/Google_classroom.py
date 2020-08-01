class googleclassroom:

  #atributos
  credenciales=input(str("Credenciales "))
  formato=input(str("Formato "))
  diseno=input(str("Diseno "))
  materias=input(str("Materias "))
  apartados=input(str("Apartados "))
  calendario=input(str("Calendario "))
  calificaciones=input(str("Calificaciones "))
  estado=input(str("Estado "))
  version=input(str("version "))

  #metodos
  def __init__(self):
    print("\nContructor googleclassroom")

  def eng(self):
    print("Entregar tareas")

  def rcbt(self):
    print("Recibir tareas")

  def retro(self):
    print("Retroalimentar la clase")

  def cali(self):
    print("Cailificar tareas")

  def comp(self):
    print("Compartir informacion")

objeto_google=googleclassroom()
objeto_google.eng()
objeto_google.rcbt()
objeto_google.retro()
objeto_google.cali()
objeto_google.comp()