class serie_de_tv:

  #atributo
  genero=input(str("Genero "))
  duracion=input(str("Duracion "))
  prodcutora=input(str("Productora "))
  idioma=input(str("Idioma "))
  lgdegrabacion=input(str("Lugar de grabacion "))
  director=input(str("Director "))
  actores=input(str("Actores "))
  critica=input(str("Critica "))
  emisor=input(str("Emisor "))
  calidad=input(str("Calidad "))

  #metodo
  def __init__(self):
    print("\nConstructor Serie de television")

  def relajar(self):
    print("Relajar")

  def entretener(self):
    print("Entretener")

  def informar(self):
    print("Informar")

  def aburri(self):
    print("Aburir")

objeto_serie=serie_de_tv()
objeto_serie.relajar()
objeto_serie.entretener()
objeto_serie.informar()
objeto_serie.aburri()