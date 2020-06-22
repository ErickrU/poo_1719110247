'''este codigo tiene como funcion 1. Leer una cadena de texto.
2. Preguntar si quiere cifrar o descifrar una cadena:
3. Si la respuesta es cifrar, debe cifrar la cadena usando su propio código César.
4. Si la respuesta es descifrar, debe descifrar la cadena usando su propio código César'''
repetir = 's' #para repetir en caso de que el usuario lo dese
while repetir == 's' or repetir == 'S' :
  class cesarClase:#la clase

    def __init__(self):
      pass
#esta clase solo cuenta con un metodo el cual se va encargar de codificar y decododificar cadanas de texto, ojo solo funciona con plabras. con los numeros no se logra realizar el cifrado exite una forma de optimizarlo y es eliminar la primera condicion la de descodificar y agregarlo clave = -clave para ahorrar un par de lineas, tambien me econtre con un problema con  los return a la altura del print(' ',traduccion)justo debajo, no retorna el valor
#la funcion de los if es que dependiendo lo solicitado codifica o decodifica despues con los for va recorreindo el valor de cada uno de los caracteres algo importante es la variable clave solo debe tener un rango de 1-26 que representa el abecedario
    def MensajeTraducidoMetodo(self):
      des = input("Desea codificar (c)\nDesea descodificar(d)\nR:")
      mensaje = input('\n Cadena de texto: ')
      clave = int(input('\ningrese el valor del salto valor entre 1-26\nValor: '))
      if  des == 'd':     
        clave= -clave
        print('\nLa descodificacion es: \n')
        for i in mensaje:
          traduccion = ('')
          if i.isalpha():
            num = ord(i)
            num += clave
            if i.isupper():
              if num > ord('Z'):
                num -= 26
              elif num < ord('A'):
                num += 26
            elif i.islower():
              if num > ord('z'):
                num -= 26
              elif num < ord('a'):
                num += 26            
              traduccion += chr(num)
              print(' ',traduccion)            
      elif des == 'c': 
        print('\nLa codificacion es: \n')
        for i in mensaje:
          traduccion = ('')
          if i.isalpha():
            num = ord(i)
            num += clave
            if i.isupper():
              if num > ord('Z'):
                num -= 26
              elif num < ord('A'):
                num += 26
            elif i.islower():
              if num > ord('z'):
                num -= 26
              elif num < ord('a'):
                num += 26            
              traduccion += chr(num)
              print(' ',traduccion)
  
  objeto=cesarClase()
  objeto.MensajeTraducidoMetodo()

  repetir = str(input("\n¿Desea cifrar/descifrar otra cadena s/n?: "))#para poder repetir input

  if repetir == 'n' or repetir == 'N':#en caso de que no acabar el programa 
    print('\nFin programa')