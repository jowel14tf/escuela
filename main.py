from profesor import *
from alumno import *
from time import sleep
from io import open

alumnos = None

class cursos():
    guadado = []
    def alumnosContar(self):
        try:
            alumnos = int(input("cuantos alumnos hay"))
        except ValueError:
            print("has introducido un valor incorrecto")
            print('introduce bien lo valores por favor')
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
            fichero = open("RegistroDeEstudiantes", "a")
        
            fichero.write(i)
        
            fichero.close()

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
            self.alumnosContar(self=cursos)
        return ""

    def SegundoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de segundo de primaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def TerceroPrimeria(self):
        quieres = input("quieres registrar alumnos en el curso de tercero de primaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def CuartoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de cuarto de primaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def QuintoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de quinto de primaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def SextoPrimaria(self):
        quieres = input("quieres registrar alumnos en el curso de sexto de primaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

class CursosSecundaria(cursos):
    
    def PrimeroSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de primero de secundaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def segundoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de segundo de secundaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def terceroSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de tercero de secundariay/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def cuartoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de cuarto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def quintoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de quinto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

    def sextoSecundaria(self):
        quieres = input("quieres registrar alumnos en el curso de sexto de secundaria y/n")
        if quieres == "y" or quieres == " y":
            self.alumnosContar(self=cursos)
        return ""

print("hola director")
sleep(0.5)
print("la semana, TODOS LOS CURSOS ESTAN VACIOS!!!")
sleep(0.5)

eleccion = input("por cual curso vamoas empezar primaria/secundaria")

if eleccion == "primaria" or eleccion == " primaria":
    print("primero vamos con primero de primaria")
    sleep(1)
    CursosPrimaria.PrimeroPrimaria(self=cursos)
    print("ahora vamos con segundo de primaria")
    sleep(1)
    CursosPrimaria.SegundoPrimaria(self=cursos)
    print("ahora vamos con tercero de primaria")
    sleep(1)
    CursosPrimaria.TerceroPrimeria(self=cursos)
    print("ahora vamos con cuarto de primaria")
    sleep(1)
    CursosPrimaria.CuartoPrimaria(self=cursos)
    print("ahora vamos con quinto de primaria")
    sleep(1)
    CursosPrimaria.QuintoPrimaria(self=cursos)
    print("ahora vamos con sexto de primaria")
    sleep(1)
    CursosPrimaria.SegundoPrimaria(self=cursos)
    print('ok')
    sleep(1)
    print('ok')
    sleep(1)
    print('ok')
    print("toca secundaria")
    quieres = input("quieres agregar alumnos a secundaria")
    if quieres == "si" or quieres == " si":
        print("ok primero primero de secundaria")
        sleep(1)
        CursosSecundaria.PrimeroSecundaria(self=cursos)
        print("ok segundo de secundaria")
        sleep(1)
        CursosSecundaria.segundoSecundaria(self=cursos)
        print("ok tercero de secundaria")
        sleep(1)
        CursosSecundaria.terceroSecundaria(self=cursos)
        print("ok cuarto de secundaria")
        sleep(1)
        CursosSecundaria.cuartoSecundaria(self=cursos)
        print("ok quinto  de secundaria")
        sleep(1)
        CursosSecundaria.quintoSecundaria(self=cursos)
        print("ok sexto de secundaria")
        sleep(1)
        CursosSecundaria.sextoSecundaria(self=cursos)

    else:
        print("ok ya que terminaste de agregar alumnos puedes sitar todos los alumnos \n en el archivo de registro de estudiante")
        print("se reiniciara el archivo si agregas mas personas")
else:
    print("ok no tienes ningun alumno agregado :(")

