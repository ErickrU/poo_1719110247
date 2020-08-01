class FutbolistaClase:
  
  #atributos
  nacionalidad_variable=        input(str("Nacionalidad "))
  raza_variable=                input(str("Raza "))
  edad_variable=                input(str("Edad "))
  posicion_variable=            input(str("posicion "))
  ndegolesrecord_variable=      input(str("Numero de goles Record "))

  #metodos
  def __init__(self):
    pass

  def entrenarMetodo(self):
    print("Entrenar")

  def partorMetodo(self):
    print("Participar en torneos")

class FutbolistaAmateurClase(FutbolistaClase):

  #atributos
  desempeno_variable=                   input(str("Desempeno "))
  Equipoparaelquejuega_variable=        input(str("Equipo para el equipo que juega "))
  ndejugador_variable=                  input(str("Numero de jugador "))
  liga_variable=                        input(str("Liga "))
  partidos_variable=                    input(str("Partidos jugados")) 

  #metodos
  def __init__(self):
    pass

  def zigzagearMetodo(self):
    print("Zigzaguear")

  def patearMetodo(self):
    print("Patear")

  def entrenarMetodo(self):
    print("Entrenar amateur")

  def partorMetodo(self):
    print("Participar en torneos amateur")

obj_fut = FutbolistaAmateurClase()
print("")
obj_fut.entrenarMetodo()
obj_fut.partorMetodo()
obj_fut.zigzagearMetodo()
obj_fut.patearMetodo()