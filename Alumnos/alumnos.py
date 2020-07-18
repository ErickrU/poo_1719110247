class alumnos():
  def __init__(self):
    pass
  '''este codigo solo funciona con una funcion la primera lista alu se encarga de recibir losd atos de los alumnos para posteriormente crear una lista de listas con la lista aluf en esta lista se queda almacenado dos valores los cuales son el nombre y el año de nacimiento para calcular la edad del individuo se se usa un for de la lista aluf en el cual line apor linea lee el año en el que nacio hace la operacion que es restar el año en el que estamos menos en el que nacio despues de eso todo eso se pone en una lista para almacenar la informacion llamada resuelto'''
  def act(self):
    repetir='s'
    alu=[]
    aluf=[]
    resuelto=[]
    while repetir == 's' :
      nm=input('\nNombre ')
      alu.append(nm)
      nac=int(input('Año de nacimiento '))
      alu.append(nac)
      g=input('Grupo ')
      aluf.append(alu)
      alu=[]
      repetir = str(input("\n¿Desea tomar el dato de otro alumno s/n?: "))
      if repetir == 'n' or repetir == 'N':
        print('\n             Fin captura de datos\n')
    for i in aluf:
      i2=2020-(i[1])
      resuelto.append('\nEstudiante: ')
      resuelto.append(i[0])
      resuelto.append('\nEdad: ')
      resuelto.append(i2)
      resuelto.append('\n')
    print(*resuelto)
obj = alumnos()
obj.act()