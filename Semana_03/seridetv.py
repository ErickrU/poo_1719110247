class SeriedeTVClase:
  
  #atributo
  genero_variable=              input(str("Genero "))
  duracion_variable=            input(str("Duracion "))
  prodcutora_variable=          input(str("Productora "))
  idioma_variable=              input(str("Idioma "))
  lgdegrabacion_variable=       input(str("Lugar de grabacion "))

  #metodo
  def __init__(self):
    pass

  def relajarMetodo(self):
    print("Relajar")

  def entretenerMetodo(self):
    print("Entretener")

class SeriedeTVMAClase(SeriedeTVClase):

  #atributo
  director_variable=            input(str("Director "))
  actores_variable=             input(str("Actores "))
  critica_variable=             input(str("Critica "))
  emisor_variable=              input(str("Emisor "))
  calidad_variable=             input(str("Calidad "))

  #metodo
  def __init__(self):
    pass

  def informarMetodo(self):
    print("Informar")

  def aburrirMetodo(self):
    print("Aburir")

obj_tv = SeriedeTVMAClase()
print("")
obj_tv.relajarMetodo()
obj_tv.entretenerMetodo()
obj_tv.informarMetodo()
obj_tv.aburrirMetodo()
