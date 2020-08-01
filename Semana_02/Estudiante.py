class estudiante:

  #atributos
  destudia=input(str("Donde estudia? "))
  matricula=input(str("Matricula "))
  calificaciones=input(str("Calificaciones "))
  edad=input(str("edad "))
  escolaridad=input(str("Escolaridad "))
  sexo=input(str("Sexo "))
  conducta=input(str("Conducta "))
  tiradematerias=input(str("Tira de materias "))
  nombre=input(str("Nombre "))
  nacionalidad=input(str("Nacionalidad "))

  #metodos
  def __init__(self):
    print("\nConstructor estudiante")

  def aprobar(self):
    print("Aprobar")

  def estudiar(self):
    print("Estudiar")

  def comprender(self):
    print("Comprender")

  def resolver(self):
    print("Resolver")

  def aprender(self):
    print("Aprender")

objeto_estudiante=estudiante()
objeto_estudiante.aprobar()
objeto_estudiante.estudiar()
objeto_estudiante.comprender()
objeto_estudiante.resolver()
objeto_estudiante.aprender()