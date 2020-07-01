class TemperaturasClase:
    def __init__(self):
      pass 
    '''el metodo escribirMetodo se encarga de escribir en el documnetod de texto de igual manera se encarga de realizar las operaciones matematicas para convertir los grados centigrados a fahrenheit mediante dos variables que cambias de valor al entrar en un while donde confimamos seguir agregando temperaturas al documento de texto'''  
    def escribirMetodo(self,temperaturas):
      file = open(temperaturas, 'w')
      lisC=0
      lisF=0
      contador=0
      repetir = 's' 
      while repetir == 's' or repetir == 'S' :    
        tempC_Variable = float(input('\nTemperatura en grados centigrados: '))
        convertidotemp_Variable = (tempC_Variable * 1.800)+32.00
        file.write('La temperatura es grados centigrados es: '+str(tempC_Variable)+'c\nLa temperatura en fahrenheit es: '+str(convertidotemp_Variable)+'f\n\n')
        print('La infomracion fue guardada en el archivo de texto')
        repetir = str(input("\n¿Desea leer otra temperatura s/n?: "))
        contador +=1
        if repetir == 'n' or repetir == 'N':
          print('\n             Fin captura de temperaturas')
        lisC = (tempC_Variable + lisC)
        lisF = (convertidotemp_Variable + lisF)
      lisC = lisC/contador
      lisF= lisF/contador
      print('\n\nEl promedio de las temperaturas es: \nPromedio grados centigrados: ',lisC,'\nPromedio fahrenheit: ',lisF)
      file.close()
obj=TemperaturasClase()
obj.escribirMetodo('temperaturas.txt')