repetir = 's'
while repetir == 's' or repetir == 'S' :
  class polindromoClase:

    def __init__ (self, ch_string):
      pass

    def comprobarMetodo(self):
      if texto_variable==invertido_variable:
        print (string_variable, " es Palindromo")
      else:
        print (string_variable, " no es Palindromo")

    def contadorMetodo(self):
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

  string_variable = input("cadena de caracteres: ")  
  texto_variable = string_variable.lower().replace(' ','')
  invertido_variable=''
  for i in texto_variable:
    invertido_variable = i + invertido_variable
  obj=polindromoClase(string_variable)
  obj.comprobarMetodo()
  obj.contadorMetodo()


  repetir = str(input("\n¿Desea analizar otra cadena s/n? "))#para poder repetir input
  if repetir == 'n' or repetir == 'N':#en caso de que no acabar el programa 
    print('\nFin programa')
