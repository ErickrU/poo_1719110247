class TemperaturasClase:
    def __init__(self):
      pass
    '''esta funcion tiene como proposito ecribir sobre el docuemnto temperaturas txt las temperaturas en grados centrigados y fahrenheit por medio de la funcion open y .write'''
    def escribirMetodo(self,temperaturas):
      file = open(temperaturas, 'a')
      repetir = 's' 
      fecha=input('fecha (con fomato DD MM AAAA): ')
      file.write('fecha: '+str(fecha)+'\n')
      while repetir == 's' or repetir == 'S' :    
        tempC_Variable =float(input('\nTemperatura en grados centigrados: '))
        convertidotemp_Variable =(tempC_Variable * 1.800)+32.00
        file.write('Grados centigrados: '+str(tempC_Variable)+'\nFahrenheit: '+str(convertidotemp_Variable)+'\n')      
        repetir = str(input("\n¿Desea leer otra temperatura s/n?: "))
        if repetir == 'n' or repetir == 'N':
          print('\n             Fin captura de temperaturas\n')
      file.close()
    '''este metodo tiene como proposito leer el archivo de texto para poder calcular el promedio de las temperaturas escritas en grados centigrados y fahrenheit para ello use la funcion .replace de igual manera solo dejo disponibles los numero por linea asi que lo que hago es guardar todo los datos en una tupla llmada lis la cual guarda los datos de la varible line en el for despues de ello con la funcion map puedo convertir los datos str a float despues de ellouso un for para poder intercambiar entre listas es decir el primer if guarda y suma los datos de las lineas iniciando desde 0 y el segundo if hace lo mismo pero iniciando con la linea 1 y lo que hace es alternar entre un if y otro acto seguido las sumas de las temperaturas son divididas para obtener la el numero de temperaturas totales en el que se debe dividr para obtener el promedio que se almacena la varible rpomedioc/f para luego ser impreso por otra parde cre un par de arreglos que se encontran como arreglo y arreglo2 se van a encagr de guardar la indo para el promedio general y el promedio de la temperatura mas alte dentro de todos los dias '''  
    def leerMetodo(self,temperaturas):
      file = open (temperaturas, 'r')
      arreglo=[]
      arreglo2=[]
      lisC=[]
      lisF=[]
      sumaC=0
      sumaF=0
      c=0
      for line in file:
        arreglo2.append(line)
        arreglo2 = list(map(str, arreglo2))
        if line[0] == 'F':
          line=line.replace('Fahrenheit: ','').replace('Grados centigrados: ','').replace('\n','')
          arreglo.append(line)
          arreglo = list(map(float, arreglo))
          c+=1
        elif line[0] == 'G':
          line=line.replace('Fahrenheit: ','').replace('Grados centigrados: ','').replace('\n','')
          arreglo.append(line)
          arreglo = list(map(float, arreglo))
          c+=1
      z=c/2
      f=0
      for y in arreglo:
        if f == 0:
          lisC.append(float(y))
          f+=1
        elif f == 1:
          lisF.append(float(y))
          f-=1
      for x in lisC:
        sumaC += x
      for y in lisF:
        sumaF +=y  
      promedioC=sumaC/z
      promedioF=sumaF/z
      mayorC=max(lisC)
      mayorF=max(lisF)
      print('El promedio de la temperatura en grados centigrados fue: ',promedioC,'°')
      print('El promedio de la temperatura en fahrenheit fue: ',promedioF,'°')
      print('La temperatura mas alta en grados centigrados fue: ',mayorC,'y en fahrenheit: ',mayorF,'En el dia ',arreglo2[0])
      file.close() 
obj=TemperaturasClase()
obj.escribirMetodo('temperaturas.txt')
obj.leerMetodo('temperaturas.txt')