class EstudianteClase:
  
  #estudiante
  destudia_variable=             input(str("Donde estudia? "))
  matricula_variable=            input(str("Matricula "))
  calificaciones_variable=       input(str("Calificaciones "))
  edad_variable=                 input(str("edad "))
  sexo_variable=                 input(str("Sexo "))

  #atributos 
  def __init__(self):
    pass

  def estudiarMetodo(self):
    print("Estudiar")

  def comprenderMetodo(self):
    print("Comprender")

class EstudianteExtranjeroClase(EstudianteClase):

  #atributos
  conducta_variable=           input(str("Conducta "))
  tiradematerias_variable=     input(str("Tira de materias "))
  destudiav2_variable=         input(str("Dond estudia en el extranjero? "))
  nacionalidad_variable=       input(str("Nacionalidad "))
  periodo_variable=            input(str("Periodo que estudiara en el extranjero? "))

  #metodos
  def __init__(self):
    pass

  def aprenderMetodo(self):
    print("Aprender")

  def aprobarMetodo(self):
    print("Aprobar")

obj_estuextra = EstudianteExtranjeroClase()
print("")
obj_estuextra.estudiarMetodo()
obj_estuextra.comprenderMetodo()
obj_estuextra.aprenderMetodo()
obj_estuextra.aprobarMetodo()