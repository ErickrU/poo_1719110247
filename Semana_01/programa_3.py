class variablesGlobales:

  nombre = ""
  
  def __init__(self, nombre):
    self.nombre = nombre

  def getnombre(self):
    print(self.nombre)

objeto0 = variablesGlobales("Erick")
objeto0.getnombre()