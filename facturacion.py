#Este es un algoritmo simplificado de un sistema de facturacion
#dado que utilizo matrices como tablas para almacenar la informacion de cada usuario y sus llamadas
#cuando usualemente utilizaria base de datos como mongoDB



 #para probar mi algoritmo creo un lista de usuarios donde almaceno a cada usurio
 #y luego a cada usuario cada registro de sus llamadas en matrices

#Diseño de la matriz x usuario: tipo_de_llamada, fecha, hora, duracion, destino/distancia
usuario_1 = [["Local", "Lunes", "14:55", 13, ""], 
             ["Nacional", "Lunes", "20:55", 20, "2"],
             ["Internacional", "Martes", "10:50", 8, "España"],
             ["Local", "Domingo", "21:55", 25, ""] ]

usuario_2 = [["Internacional", "Lunes", "14:55", 18, "Italia"], 
            ["Nacional", "Lunes", "20:55", 20, "5"],
            ["Internacional", "Martes", "10:50", 8, "Uruguay"],
            ["Local", "Domingo", "14:55", 25, ""]]
 
usuario_3 = [["Nacional", "Lunes", "14:55", 13, "1"], 
            ["Nacional", "Lunes", "20:55", 20, "2"],
            ["Internacional", "Martes", "10:50", 8, "Reino Unido"],
            ["Local", "Domingo", "14:55", 25, ""]]

dias_habiles =["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "lunes", "martes", "miercoles", "jueves", "viernes"] #datos brindados en el enunciado

"""Llamadas nacionales: informacion obtenida de la pagina de telecom
Codigo: 2-3	más de 30 hasta 110 Km. costo: 0.35 horario normal 0.29 horario reducido (costos inventados)
Codigo: 4	más de más de 110 hasta 170 Km. costo: 0.45 horario normal 0.39 horario reducido (costos inventados)
Codigo: 5	más de 170 hasta 240 Km. costo: 0.55 horario normal 0.49 horario reducido (costos inventados)
Codigo: 6-12	más de 240 Km. costo: 0.65 horario normal 0.59 horario reducido (costos inventados)
"""

"""
LLamadas internacionales: informacion brindada de la pagina de Movistar
DESTINO	TARIFA SIN IMPUESTOS	TARIFA CON IMPUESTOS	FRACCIONAMIENTO
EE.UU, Perú, Uruguay, Paraguay, Chile, Brasil, España	$ 5,11	$ 6,18	Por Minuto
Resto del Mundo	$ 9,30	$ 11,25	Por Minuto
Cuba, Inmarsat, Senegal	$ 41,89	$ 50,69	Por Minuto

"""
destino_1 = ["EE.UU", "Perú", "Uruguay", "Paraguay", "Chile", "Brasil", "España"]
destino_2 = ["Cuba", "Inmarsat", "Senegal"]


def horarioEnInt(hora):

  inicioLlam = hora
  inicioLlam = inicioLlam.replace(":", "")
  horario = int(inicioLlam)

  return horario

def subTotalLocales(listadoLlamadasLocales):
  minHN = 0
  minHR = 0
  for fila in range(len(listadoLlamadasLocales)):
    hora = horarioEnInt((listadoLlamadasLocales[fila][2])) #Llamo a funcion para que a la hora le elimine las : y lo pase a int
    if (listadoLlamadasLocales[fila][1] in dias_habiles):
      if( hora >= 800 and hora <= 2000):
        minHN = minHN + listadoLlamadasLocales[fila][3]
    else:
      minHR = minHR + listadoLlamadasLocales[fila][3]

  subTotHN = minHN*0.2
  subTotHR = minHR*0.1

  totalLocales = subTotHN+subTotHR

  print("\nLlamadas locales:")
  print("\n\t\tEn horario normal....................", subTotHN)
  print("\n\t\tEn horario reducido..................", subTotHR)
  print("\nTotal en llamadas locales............................", totalLocales)
 
 
  return totalLocales


def subTotalNacionales(listadoLlamadasNacionales):
  subTotHR = 0
  subTotHN = 0
  for fila in range(len(listadoLlamadasNacionales)):
    hora = horarioEnInt((listadoLlamadasNacionales[fila][2])) #Llamo a funcion para convertir horario
    if (listadoLlamadasNacionales[fila][1] in dias_habiles) and (hora >= 800 and hora <= 2000):
      if(listadoLlamadasNacionales[fila][4] =="2") or (listadoLlamadasNacionales[fila][4] =="3"): #pregunto la distancia
        subTotHN = subTotHN + listadoLlamadasNacionales[fila][3]*0.35
      elif (listadoLlamadasNacionales[fila][4] =="4"):
        subTotHN = subTotHN + listadoLlamadasNacionales[fila][3]*0.45
      elif (listadoLlamadasNacionales[fila][4] =="5"):
        subTotHN = subTotHN + listadoLlamadasNacionales[fila][3]*0.55
      else:
        subTotHN = subTotHN + listadoLlamadasNacionales[fila][3]*0.65
    else:
        if(listadoLlamadasNacionales[fila][4] =="2") or (listadoLlamadasNacionales[fila][4] =="3"):
          subTotHR = subTotHR + listadoLlamadasNacionales[fila][3]*0.29
        elif (listadoLlamadasNacionales[fila][4] =="4"):
          subTotHR = subTotHR + listadoLlamadasNacionales[fila][3]*0.39
        elif (listadoLlamadasNacionales[fila][4] =="5"):
           subTotHR = subTotHR + listadoLlamadasNacionales[fila][3]*0.49
        else:
          subTotHR = subTotHR + listadoLlamadasNacionales[fila][3]*0.59

  totalNacionales = subTotHN + subTotHR    
  print("\nLlamadas nacionales:")
  print("\n\t\tEn horario normal....................", subTotHN)
  print("\n\t\tEn horario reducido..................", subTotHR)
  print("\nTotal en llamadas Nacionales.........................", totalNacionales)
 
  return totalNacionales


def subTotalInternacional (listadoLlamadasInternacionales):

  subTotInt=0
  for fila in range(len(listadoLlamadasInternacionales)):
    if listadoLlamadasInternacionales[fila][4] in destino_1:
      subTotInt = subTotInt + listadoLlamadasInternacionales[fila][3]*5.11
    elif listadoLlamadasInternacionales[fila][4] in destino_2:
      subTotInt = subTotInt + listadoLlamadasInternacionales[fila][3]*41.89
    else:
      subTotInt = subTotInt + listadoLlamadasInternacionales[fila][3]*9.30

  print("\nTotal de llamadas internacionales....................", subTotInt)

  return subTotInt



def facturar(usr):
  tipo_local =[]
  tipo_nacional =[]
  tipo_internacional =[]

  for fila in range(len(usr)):

    if  usr[fila][0] == "Local":
       tipo_local.append(usr[fila])
    elif usr[fila][0] == "Nacional":
      tipo_nacional.append(usr[fila])
    elif usr[fila][0] == "Internacional":
      tipo_internacional.append(usr[fila])
  
  sTL = subTotalLocales(tipo_local)
  sTN = subTotalNacionales(tipo_nacional)
  sTI = subTotalInternacional(tipo_internacional)

  subtotal =  sTL+sTN+ sTI
  
  print("\n\nSubtotal.............................................", round(subtotal, 4))

  impuestos = subtotal*0.21

  print("\nImpuestos............................................", round(impuestos, 4))

  total = subtotal + impuestos
  print("\n\nEl importe total de su factura es....................", round(total, 4))

  


def selec_usr():
    usr = input("\nIngrese el id del usuario a facturar: ")

    if usr == "1":
      facturar(usuario_1)

    elif usr == "2":
        facturar(usuario_2)

    elif  usr == "2":
        facturar(usuario_3)

    else: 
      print("\n El usuario no existe\n")
      new_selct = input("Desea volver a intentarlo? :")
      if new_selct == "si":
          selec_usr()
      else:
            exit();


selec_usr()
