#TODOITS - PYTHON
#Crear tareas
#Revisar tareas
#Modificar tarea 
#Eliminar tarea
#CRUD Create - Read - Update  Delete 
opcion = " "
tarea = []

def opciones():
  print("A. Ingresar una nueva tarea")
  print("B. Mostrar las tareas pendientes")
  print("C. Modificar tareas disponibles")
  print("D. Eliminar las tareas")
  print("E. Salir del programa")
  opcion = input("Ingrese aquí la opción deseada: ")
  opcion = opcion.upper()
  return opcion
  

opcion = opciones()
while (opcion != "E" ):
  if(opcion == "A"):
    tarea.append(input("Ingrese su tarea: "))
    print("Se guardo su tarea con exito\n")
    opcion = opciones()
  
  elif(opcion == "B"):
    print("Tareas pendientes\n")
    for elemento in tarea:
      posicion = tarea.index(elemento)
      print(posicion,":",elemento,"\n")
    opcion = opciones()
  
  elif(opcion == "C"):
    posicion = int(input("¿Cual tarea desea modificar? "))
    tarea[posicion] = input("Ingrese su nueva tarea") 
    print("Se modifico la tarea con exito")
    opcion = opciones()
  
  elif(opcion == "D"):
    tarea.pop(int(input("¿Que tarea desea eliminar: ")))
    print("Se elimino la tarea con exito")
    opcion = opciones()
  

