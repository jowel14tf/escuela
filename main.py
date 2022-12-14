from profesor import *
from alumno import *
from time import sleep
from io import open

alumnos = None

class cursos():
    guadado = []
    def alumnosContar(self):
        alumnos = int(input("cuantos alumnos hay"))
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
            print(f"has registrado un estudiante con este nombre:{nombre}")
            #print(persona.__str__())
            global i
        for i in guardado:
            pass
        quieres = input("quieres ver tus estudiante de este curso ? y/n")
        if quieres == "y" or quieres == " y":
            for i in guardado:
                print(f"tus estudiantes son: {i}")
                sleep(1)
        else:
            print("ok")
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
            self.alumnosContar(self=cursos)
        return ""

    def SegundoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de segundo de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en segundo de primaria"))
            self.alumnosContar(self=cursos)
        return ""

    def TerceroPrimeria(self):
        quieres = input("quieres registrar alumnos en el curso de tercero de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en tercero de primaria"))
            self.alumnosContar(self=cursos)
        return ""

    def CuartoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de cuarto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en cuarto de primaria"))
            self.alumnosContar(self=cursos)
        return ""

    def QuintoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de quinto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en quinto de primaria"))
            self.alumnosContar(self=cursos)
        return ""

    def SextoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de sexto de primaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en sexto de primaria"))
            self.alumnosContar(self=cursos)
        return ""

class CursosSecundaria(cursos):
    
    def PrimeroSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de primero de secundaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en primero de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de primero de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "primero de secundaria"
            self.mostrarAlumnos(curso)
        return ""

    def segundoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de segundo de secundaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en segundo de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de segundo de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "segundo de secundaria"
            self.mostrarAlumnos(curso)
        return ""

    def terceroSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de tercero de secundariay/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en tercero de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de tercero de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "tercero de secundaria"
            self.mostrarAlumnos(curso)
        return ""

    def cuartoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de cuarto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en cuarto de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de cuarto de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "cuarto de secundaria"
            self.mostrarAlumnos(curso)
        return ""

    def quintoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de quinto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en quinto de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de quinto de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "quinto de secundaria"
            self.mostrarAlumnos(curso)
        return ""

    def sextoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de sexto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            alumnos = int(input("cuantos alumnos hay en sexto de secundaria"))
            self.alumnosContar(self=cursos)
        quieres = input("quieres ver cuales son tus alumnos que estan en el curso de sexto de secundaria")
        sleep(1)
        if quieres == "y" or quieres == " y":
            curso = "sexto de secundaria"
            self.mostrarAlumnos(curso)
        return ""

print("hola director")
sleep(0.5)
print("la semana, TODOS LOS CURSOS ESTAN VACIOS!!!")
sleep(0.5)

eleccion = input("por cual curso vamoas empezar primaria/secundaria")

if eleccion == "primaria" or eleccion == " primaria":
    print("primero vamos con primero de primaria")
    CursosPrimaria.PrimeroPrimaria(self=cursos)

# ahora toca arreglar secundaria y despues configurar para que se puedan ver todos y primaria
#y hacer terminar la 1.0