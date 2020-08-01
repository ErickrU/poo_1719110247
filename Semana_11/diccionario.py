class diccionarioClase:
  def __init__(self):
    pass
  def solicitar(self):
    '''Este programa solo tiene una funcion, ok iremos linea por linea en un principio encontramos la valible r nos ayuda a repetir el codigo acto seguido las listas que se encargaran de guardar la infonmacion del diccionario ya dentro del while tenemos los input para darle forma al diccionario la valiable diccionario o mejor dicho el diccionario en si cada linea de diccionario se agrega a una lista para hacer una lista de diccionario por que como ya se sabe si tuviera varias claves con el mismo nombre solo se toma el valor de la ultima clave en la segunda parte en la valible imprimir alamacenaremos el valor que se va mostarr de la seleccion del genero con con el input 'key' usamos el for para tomar cada una de las lista del diccionario y un if para filtrar las pelicas del genero que desea el usuario despues es agregada a la lista imprimir ya antes mecionada donde se pondran los dstos compeltos de las peliculas del genero solicitado y de no ser el caso se aplicara el else'''
    r='s'
    peliculas=[]
    peliculasv2=[]
    print('**************************************\n*        Datos de la pelicula        *\n**************************************')
    while r == 's':
      nombre =str(input('\nNombre '))
      genero=str(input('Genero '))
      año=int(input('Año '))
      diccionario={"Nombre":nombre ,'Genero':genero ,'Año de lanzamiento':año}
      peliculas.append(diccionario)
      peliculas.append('\n')
      peliculasv2.append(diccionario)
      r=str(input('\nleer otra pelicula s/n '))
    print('\n**************************************\n*            PELICULAS               *\n**************************************\n')
    print(*peliculas)
    imprimir=[]
    key=input('Genero de la pelicula que desea ver ')
    for xyz in peliculasv2:
      if key in xyz['Genero']:
        imprimir.append(xyz)
        imprimir.append('\n')
        xyz=[]
    print('Las peliculas del genero ',key,' son: \n')
    print(*imprimir)
obj=diccionarioClase()
obj.solicitar()