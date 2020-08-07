class excepciones:#clase
  def __init__(self):#constructor
    pass
  def solicitud(self):#unica clase
    import math#libreria
    numeros=[]#lista de los numeros
    c=0#contador
    cuantos=int(input('Cuantos numeros desea evaluar: '))#numero de numeros a evaluar
    for i in range (cuantos):#cadena para leer cada numero
      c+=1#contador
      print('Cual es el valor del numero',c)
      valor=int(input(' '))
      numeros.append(valor)
    r='s'#para repetir
    while r == 's':
      print('\nRecuerda que una lista empiza desde el indice 0')
      indice=int(input('dame un indice '))#para ver que numero se va trabajar
      try:#por si no aparece en la lista
        num=(numeros[indice])
      except:#el por que
        print('\n\n******************************************\nEl indice no esta en la lista o no es un valor valido\n******************************************\nEn su lugar se tomara el ultimo indice valido\n******************************************\n\n') 
        print('El numero es: ',num)
      if r == 's':#para cada operacion necesaria
        try:#por si el valor no es un numero o algo sale mal
          if num%2 == 0:#resultado de la division
            print ('\n',num,' es un numero par')
          else:#si no lo es pues obvio impar
            print ('\n',num,' es un numero impar')
        except TypeError:#explicacion
          print('El valor no es un numero')
      if r == 's':
        try:
            r0=math.sqrt(num)#raiz cuadrada
            print('\nLa raiz de',num,'cuadrada es:',r0)
        except ValueError:#xplicaion para el usuario
          print('\n',num,'no es un numero')
      if r == 's':
        try:#por si falla
          r1= num ** 3#raiz al cubo
          print('\n',num,'elevado al cubo es',r1)
        except TypeError:#explicacion 
          print('\n',num,'no es un numero')
      r=str(input('\nanalizar otro numero s/n : '))#para repetir 
obj=excepciones()#para crear el objeto
obj.solicitud()