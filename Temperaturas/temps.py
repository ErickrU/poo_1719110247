class TemperaturasClase:
    def __init__(self):
      pass
    '''esta funcion tiene como proposito ecribir sobre el docuemnto temperaturas txt las temperaturas en grados centrigados y fahrenheit por medio de la funcion open y .write'''
    def escribirMetodo(self,temperaturas):
      file = open(temperaturas, 'w')
      repetir = 's' 
      while repetir == 's' or repetir == 'S' :    
        tempC_Variable =float(input('\nTemperatura en grados centigrados: '))
        convertidotemp_Variable =(tempC_Variable * 1.800)+32.00
        file.write('La temperatura en grados centigrados es: '+str(tempC_Variable)+'\nLa temperatura en fahrenheit es: '+str(convertidotemp_Variable)+'\n')      
        repetir = str(input("\n¿Desea leer otra temperatura s/n?: "))
        if repetir == 'n' or repetir == 'N':
          print('\n             Fin captura de temperaturas\n')
      file.close()
    '''este metodo tiene como proposito leer el archivo de texto para poder calcular el promedio de las temperaturas escritas en grados centigrados y fahrenheit para ello use la funcion .replace de igual manera solo dejo disponibles los numero por linea asi que lo que hago es guardar todo los datos en una tupla llmada lis la cual guarda los datos de la varible line en el for despues de ello con la funcion map puedo convertir los datos str a float despues de ellouso un for para poder intercambiar entre listas es decir el primer if guarda y suma los datos de las lineas iniciando desde 0 y el segundo if hace lo mismo pero iniciando con la linea 1 y lo que hace es alternar entre un if y otro acto seguido las sumas de las temperaturas son divididas para obtener la el numero de temperaturas totales en el que se debe dividr para obtener el promedio que se almacena la varible rpomedioc/f para luego ser impreso'''
    def leerMetodo(self,temperaturas):
      lisC=0
      lisF=0
      lis=[]
      file = open (temperaturas, 'r')
      for line in file:
        line=line.replace('La temperatura en fahrenheit es: ','').replace('La temperatura en grados centigrados es: ','').replace('\n','')
        lis.append(line) 
        lis = list(map(float, lis))  
      z=int(len(lis))/2
      f=0
      for y in lis:
        if f == 0:
          lisC+=y
          f+=1
        elif f == 1:
          lisF+= y
          f-=1
      promedioC=lisC/z
      promedioF=lisF/z
      print('El promedio de la temperatura en grados centigrados fue: ',promedioC,'°')
      print('El promedio de la temperatura en fahrenheit fue: ',promedioF,'°')
      file.close() 
obj=TemperaturasClase()
obj.escribirMetodo('temperaturas.txt')
obj.leerMetodo('temperaturas.txt')