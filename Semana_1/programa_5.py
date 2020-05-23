class transporteterrestre:

  def __init__(self):
    print("Constructor transporte terrestre")

  def acelerar(self):
    print("Acelerar")

class coche(transporteterrestre):

  def __init__(self):
    print("Constructor coche")

  def acelerar(self):
    print("Acelerar coche")

class bicicleta(transporteterrestre):

  def __init__(self):
    print("Constructor bicileta")

  def acelerar(self):
    print("Acelerar bicicleta")


objeto1 = transporteterrestre()
objeto1.acelerar()


objeto2 = coche()
objeto2.acelerar()

objeto3 = bicicleta()
objeto3.acelerar()