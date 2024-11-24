import re
patron = r"^\d{2}-\d{2}-\d{4}:\d{2}:\d{2}$"
citas = {
    "01":{"Paciente": "Andres",
    "Fecha y Hora": "11-22-2024:21:03",
    "Dentista": "Juan Luis Fortuna",
    "Motivo de Consulta": "Revision"

    }
}

def agendar_consulta():
    global id_unico
    while True:
        paciente = input("Ingrese nombre del paciente: ")
        try:
            int(paciente)
            print("Debes ingresar un nombre")
            continue
        except ValueError:
            if paciente != "":
                break

    while True:
        id_unico = input("Ingrese un ID de cita unico: ")
        if id_unico in citas:
            print("Ya existe una cita con ese id. Ingrese uno unico")
        else:
            break

    while True:
        fecha_hora = input("Fecha y hora de la cita: EJ; dia-mes-año: hora(24h-formato)-minuto: ").strip()
        if re.fullmatch(patron, fecha_hora):
            break
        else:
            print("Tienes que ingresar fecha y hora con este formato EJ; '23-04-2005:16:04'")

    while True:
        dentista = input("Nombre de su dentista: ")
        try:
            int(dentista)
            print("Debes ingresar un nombre valido para el dentista.")
        except ValueError:
            if dentista != "":
                break

    while True:
        motivo_consulta = input("Motivo de consulta EJ: 'Limpieza', 'Extraccion', 'Revision': ").lower()
        if motivo_consulta in ["limpieza", "extraccion", "revision"]:
         citas[id_unico] = {
        "Paciente": paciente,
        "Fecha y Hora": fecha_hora,
        "Dentista": dentista,
        "Motivo de Consulta": motivo_consulta}
         print("Cita agendada correctamente")
         break
        else:
            print("Escribe una de las 3 opciones validas: 'Limpieza', 'Extraccion', 'Revision'")
def consultar_citas():
    while True:
         decision = input("Ingrese el ID unico para ver los datos: ").strip()
         if decision in citas:
            print(citas[decision])
            break
         else:
            print("No se encuentra el ID")
    consultar_citas()
def actualizar_citas():
    decision = (input("Ingrese un id para actualizar: "))
    if decision in citas:
      print("1. Actualizar paciente")
      print("2. Actualizar id")
      print("3. Actualizar Fecha y Hora")
      print("4. Actualizar dentista")
      print("5. Actualizar motivo de consulta")
      decision_2 = (input("Ingrese el numero de la opcion deseada: "))
      if decision_2 == "1":
        while True:
         paciente = input(f"Ingrese un nombre para actualizar el nombre del id {decision}: ")
         try:
            int(paciente)
         except ValueError:
            citas[decision]["Paciente"] = paciente
            print("Se a actualizado correctamente el nombre del id")
            break
      if decision_2 == "2":
        while True:
         nuevo_id = input(f"Ingrese un nuevo id para actualizar el id del id {decision}: ")
         if nuevo_id in citas:
            print("Ese id actualmente esta ocupado por un paciente")
         else:
          citas[nuevo_id] = citas.pop(decision)
          print("Se ha actualizado el id correctamente")
          break
      if decision_2 == "3":
        while True:
            fecha_hora = input("Ingresa la fecha y hora (formato: '23-04-2005:16:04'): ").strip()
            if re.fullmatch(patron, fecha_hora):
                print("Fecha y Hora actualizada correctamente")
                break
            else:
                print("Tienes que ingresar fecha y hora con este formato EJ; '23-04-2005:16:04'")
      if decision_2 == "4":
        while True:
         dentista = input(f"Ingrese un nombre para actualizar el dentista del id {decision}: ")
         try:
             int(dentista)
             print("Ingrese un nombre valido")
         except ValueError:
             citas[decision]["Dentista"] = dentista
             print("Dentista se a actualizado correctamente")
             break
      if decision_2 == "5":
         while True:
            motivo_consulta = input(" Escribe el motivo de consulta para actualizarlo EJ: 'Limpieza', 'Extraccion', 'Revision': ").lower()
            if motivo_consulta in ["limpieza", "extraccion", "revision"]:
               citas[decision]["Motivo de Consulta"] = motivo_consulta
               print("El motivo de consulta se a actualizado correctamente")
               break
            else:
               print("Tienes que escribir el motivo de consulta EJ: 'Limpieza', 'Extraccion', 'Revision' ")              
def eliminar_citas():
    while True:
     decision = input("Ingrese el id unico que desea eliminar. Se eliminaran todos los datos existentes del id: ")
     if decision in citas:
        del citas[decision]
        print("Se a eliminado el id permanentemente.")
        break
     else:
        print("Ese id no pudo ser encontrado")            
def exportar():
     with open("citas.txt", "w") as archivo:
        for id_cita, datos in citas.items():
            archivo.write(f"ID: {id_cita}\n")
            for clave, valor in datos.items():
                archivo.write(f"  {clave}: {valor}\n")
            archivo.write("\n")  
     print("citas exportadas correctamente en la carpeta del archivo.")
def menu():
    while True:
        print("Menu")
        print("1. Agendar Consulta")
        print("2. Consultar Citas")
        print("3. Actualizar Citas")
        print("4. Eliminar Citas")
        print("5. Exportar Citas")
        print("6. Salir")
        Decision = (input("Ingrese el numero de la opcion deseada: "))
        if Decision == "1":
            agendar_consulta()
        elif Decision == "2":
            consultar_citas()
        elif Decision == "3":
            actualizar_citas()
        elif Decision == "4":
            eliminar_citas()
        elif Decision == "5":
            exportar()
        elif Decision == "6":
           break
        else:
           print("Ingrese un numero representado en el menu")
menu()













    

      
     
    
   


      




  

    
   

       