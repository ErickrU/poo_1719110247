repetir = 's' 
while repetir == 's' or repetir == 'S' :
  class cesarClase:
    def __init__(self):
      pass
    '''la funcion MensajeTraducidoMetodo se encarga de encriptar el mensaje y almacenarlo en la varible traduccion que es global de igual manera decodifica, esto funciona apartir de abrir un docuemnto de texto llamado archivo''' 
    def MensajeTraducidoMetodo(self, archivo):
      file = open (archivo, 'r')
      des = input("Desea codificar (c)\nDesea descodificar(d)\nR:")
      clave = int(input('\ningrese el valor del salto para su codificacion/codificacion\nValor: '))
      global traduccion
      traduccion=''
      for line in file:
        mensaje = line
        if  des == 'd':     
          clave= -clave
          for i in mensaje:
            num = ord(i)
            num += clave
            traduccion += chr(num)
        elif des == 'c': 
          for i in mensaje:
            num = ord(i)
            num += clave    
            traduccion += chr(num)
      print('\nLa codificacion/decodificaion es: ')
      print(traduccion)      
      file.close()
    '''la funcion codificar se encarga de escribir en el mismo archivo de texto donde se lee el mensaje poner el texto ya codificado de la variable global traduccion''' 
    def codificar(self,archivo,traduccion):
      file = open(archivo, 'w')
      file.write(traduccion)
      file.close()
  objeto=cesarClase()
  objeto.MensajeTraducidoMetodo('archivo.txt')
  objeto.codificar('archivo.txt',traduccion)  
  repetir = str(input("\n¿Desea cifrar/descifrar otra cadena s/n?: "))
  if repetir == 'n' or repetir == 'N':
    print('\nFin programa')