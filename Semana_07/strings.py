''' este codigo tiene como proposito realizar
 1. Leer una cadena de texto.
2. Imprimir cada caracter de la cadena por separado.
3. Imprimir si es número, letra o símbolo cada caracter.
4. Imprimir la longitud de la cadena.
5. Imprimir la longitud de la cadena sin espacios.
6. Preguntar si desea analizar otra cadena con el siguiente mensaje ("¿Desea analizar otra cadena s/n?: )
7. Si la respuesta es "s" o "S" repetir el proceso, en caso contrario terminar el programa.
'''
repetir = 's' #para repetir en caso de que el usuario lo dese
while repetir == 's' or repetir == 'S' :
  ch_string = input("Lista de caracteres ")#input para recibir la lista de cracteres
  class cadenaClase:#la clase

    def __init__(self):#nuestro constructor
      pass
      
    def long_T(self):
      print('La longitud de la cadena es de: ',len(ch_string),' caracteres')#para saber la longitud de la cadena use el comando len en un print muy util recuerda los parentesis 

    def long_Out(self):#esta funcion esta hecha para contar la cadena sin espacios mas sin embargo use el coamndo replace muy util solo basta con ponerlo yd entro del parentesis lo que quieres eleminar y luego por lo que tomara lugar
      long_outspace=ch_string.replace(' ','')
      print('La longitud de la cadena sin espacios es de: ',len(long_outspace),' caracteres')

    def separate(self):#para separar cada caracter y de paso decir que es use un for para poder ir de uno en uno y los if para poder saber a que tipo de caracter pertenesia 
      print('Cadena separada por caracter: ')
      for i in ch_string:
        if i.isdigit():
          print(i ,' este caracter es un numero')
        elif i.isalpha():
          print(i, ' este caracter es una letra')
        else:
          print(i, ' este caracter es no es un numero ni una letra')   

  obj=cadenaClase()
  obj.long_T()
  obj.long_Out()
  obj.separate()
  #llamar a las funciones 

  repetir = str(input("\n¿Desea analizar otra cadena s/n?: "))#para poder repetir input

  if repetir == 'n' or repetir == 'N':#en caso de que no acabar el programa 
    print('\nFin programa')