'''Este codigo tiene como funcion realizar 
1. Leer una cadena de texto.
2. Imprimir si la cadenas es palindromo o no.
3. Imprimir cuantos espacios y vocales encontro en la cadena.
4. Preguntar si desea analizar otra cadena con el siguiente mensaje ("¿Desea analizar otra cadena s/n?: )
5. Si la respuesta es "s" o "S" repetir el proceso, en caso contrario terminar el programa'''

repetir = 's'#se le asigna valor al primer repetir para su correto funcionamiento
while repetir == 's' or repetir == 'S' :#el gatillo para el repetir donde la condicion se cumpla 
  class polindromoClase:#la clase 

    def __init__ (self, ch_string):#nuestro contructor 
      pass

    def comprobarMetodo(self):
      ''' Este metodo tiene la tarea de comparar el texto 
      invertido y el normal pero previamente limpiado es decir
      sin espacios y todo en minusculas'''
      if texto_variable==invertido_variable:#la primera variable es el texto normal
      #la segunda variable es del texto invertido 
        print (string_variable, " es Palindromo")
      else:
        print (string_variable, " no es Palindromo")

    def contadorMetodo(self):
      ''''este metodo tiene la funcion de contar el numero de vocales
      y espacios en la cadena de pende de la variable string_variable ya que es
      dond esta todo el texto que se recibio tal cual''' 
      contadorespacio_variable=0
      contadorvocal_variable=0
      for i in str(string_variable):
        if 'a' == i:
          contadorvocal_variable += 1
        elif 'e' == i:
          contadorvocal_variable += 1
        elif 'i' == i:
          contadorvocal_variable += 1
        elif 'o' == i:
          contadorvocal_variable += 1
        elif 'u' == i:
          contadorvocal_variable += 1
        elif ' ' == i:
          contadorespacio_variable += 1          
        else:
          contadorvocal_variable += 0
          contadorespacio_variable+=0
      print('La cadena cuenta con: ',contadorvocal_variable,' vocale(s)')
      print('La cadena cuenta con: ',contadorespacio_variable,' espacio(s)')

  string_variable = input("cadena de caracteres: ")#variable global sobre la cadena que se recibe tal cual  
  texto_variable = string_variable.lower().replace(' ','')#variable global del texto recibido pero sin espacios y todo en minusculas
  invertido_variable=''#declaramos la variable antes de poder usarla
  for i in texto_variable:
    invertido_variable = i + invertido_variable#aqui usamos el for para poder invertir la cadena en lugar del reverse
  obj=polindromoClase(string_variable)#creamos el objeto
  obj.comprobarMetodo() #llamar al metodo que nos dira si la cadena es polindroma
  obj.contadorMetodo() #llamar al metodo que nos dice el numero de vocales y espacios


  repetir = str(input("\n¿Desea analizar otra cadena s/n? "))#para poder repetir el programa
  if repetir == 'n' or repetir == 'N':#en caso de acabar el programa 
    print('\nFin programa')
