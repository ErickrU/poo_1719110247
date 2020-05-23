class futbolista:

  #atributos
  nacionalidad=input(str("Nacionalidad "))
  raza=input(str("Raza "))
  edad=input(str("Edad "))
  posicion=input(str("posicion "))
  ndegolesrecord=input(str("Numero de goles Record "))
  desempeno=input(str("Desempeno "))
  ndecontratos=input(str("Numero de contratos Historial "))
  Equipoparaelquejuega=input(str("Equipo para el equipo que juega "))
  ndejugador=input(str("Numero de jugador "))
  liga=input(str("Liga "))

  #Metodo
  def __init__(self):
    print("\nConstructor futbolista")

  def entrenar(self):
    print("Entrenar")

  def partor(self):
    print("Participar en torneos")

  def correr(self):
    print("Correr")

  def zigzagear(self):
    print("Zigzaguear")

  def patear(self):
    print("Patear")

objeto_futbolista=futbolista()
objeto_futbolista.entrenar()
objeto_futbolista.partor()
objeto_futbolista.correr()
objeto_futbolista.zigzagear()
objeto_futbolista.patear()