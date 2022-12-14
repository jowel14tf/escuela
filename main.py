from profesor import *
from alumno import *
from time import sleep
from io import open

alumnos = None

class cursos():
    guadado = []
    def alumnosContar(self,alumnos):
        try:
            global rango
            rango = range(alumnos)
            global guardado
            guardado = []
            for crear in range(alumnos):
                nombre = input(f"cual es el nombre del estudiante {crear}")
                apellido = input("cual es el apellido?")
                global persona
                persona = Informacionestudiante(nombre,apellido,'primaria' , "matematica")
                guardado.append(persona.__str__())
                print(f"has creado una alumno con el nombre de {nombre}")
                print(persona.__str__())
                global i
            for i in guardado:
                print(f"tus estudiantes son: {i}")
                sleep(1)
        except TypeError:
            print("no se puedo imprimir la informacion por que falta \n el parametro alumnos")
        return ""

    def mostrarAlumnos(self,curso):
        for alumnos in rango:
            for mostrar in guardado:
                print(f"el curso de {curso} tiene los datos del estudiante numero {alumnos} \n sus datos son: {mostrar}")
                sleep(1)
        return ""
    
    def EscribirTareas(self):
        Tareas = input('cual es tu tarea?')
        
        archivo = open('Tareas.txt', "w")

        archivo.write(Tareas)

        decicion = input('quieres escribir mas tareas?' + 'si/no')
        decicion = decicion.lower()
        while decicion == "si" or decicion == " si":
            Tareas = input('cual es tu otra tarea tarea? \n')
            sleep(1)
            archivo.write("\n" + Tareas)
            decicion = input('quieres escribir mas tareas?' + 'si/no')
            if decicion == "no" or decicion == " no":
                sleep(1)
                print("ok las tareas que anotaste estan el archivo llamado tareas")
                archivo.close()
                break;
        archivo.close()
        return ""

    def AgregarTareas(self):
        archivo = open("Tareas.txt", "a")
        tareas = input("cual es la tarea que quieres agregar \n")
        archivo.write("\n")
        archivo.write(tareas)
        decicion = input('quires agregar una tarea mas? si/no')
        while decicion == "si" or decicion == " si":
            tareas = input("cual es la tareas que quieres agregar")
            archivo.write("\n" + tareas)
            if decicion == "no" or decicion == " no":
                print("ok terminamos de agregar mas tareas")
                archivo.close()
                break;
            decicion = input('quires agregar una tarea mas? si/no')
        return ""

    def MostrarTareas(self):
        archivo = open('Tareas.txt',"r")

        contenido = archivo.read()

        archivo.close

        print("el archivo contienen estas tareas: \n" )
        
        return contenido

    def MostaraUsuario(self):
        decicion = input("quieres agregar tareas ? si/no")

        if decicion == "si" or decicion == " si":
            self.EscribirTareas(self=cursos)
            decicion = input("ya que agregaste algunas tareas estas seguras que \n terminaste de hacer tareas si/no ")
            if decicion == "si" or decicion == " si":
                self.AgregarTareas(self=cursos)
            else:
                print("ok pues estamos de acuerdo :)")
        
        decicion = input("ya que estamos seguros de que anotaste todas las tareas \n quieres verla")
        if decicion == "si" or decicion == " si":
            self.MostaraUsuario(self=cursos)
        else:
            print("ok igual puedes ver las tareas en el archivo.txt")

class CursosPrimaria(cursos):
    def PrimeroPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de primero de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en primero de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de primero de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "primero de primaria"
            self.mostrarAlumnos(curso)
        return ""

    def SegundoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de segundo de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en segundo de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de segundo de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "segundo de primaria"
            self.mostrarAlumnos(curso)
        return ""

    def TerceroPrimeria(self):
        quieres = input("quieres registrar alumnos en el curso de tercero de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en tercero de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de tercero de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "tercero de primaria"
            self.mostrarAlumnos(curso)
        return ""

    def CuartoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de cuarto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en cuarto de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de cuarto de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "cuarto de primaria"
            self.mostrarAlumnos(curso)
        return ""

    def QuintoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de quinto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en quinto de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de quinto de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "quinto de primaria"
            self.mostrarAlumnos(curso)
        return ""

    def SextoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de sexto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en sexto de primaria"))
            self.alumnosContar(alumnos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de sexto de primaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "sexto de primaria"
            self.mostrarAlumnos(curso)
        return ""

