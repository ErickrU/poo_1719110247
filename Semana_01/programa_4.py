class coche:

  def __init__(self):
    print("constructor de coche")

  def acelerar(self):
    print("acelerar")

  def frenar(self):
    print("frenar")

class cocherojo(coche):

  def __init__(self):
    print("Constructor coche rojo")  

objeto0 = coche()
objeto0.acelerar()
objeto0.frenar()

objeto1 = cocherojo()
objeto1.acelerar()
objeto1.frenar()