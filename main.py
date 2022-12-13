from profesor import *
from alumno import *
from time import sleep


#sleep(1.2)
#despues de terminar la clase hay que saber lo curso para eso hay que hacer
#que cada curso tenga un estudiante
class cursos():

    PrimariaGrado = None
    SecundariaGrado = None

    def cursoPrimario(self):
        
        def Primero():
            pass

        def Segundo():
            pass

        def Tercero():
            pass

        def Cuarto():
            pass

        def Quinto():
            pass

        def Sexto():
            pass

    def SucandariaGrado(self):

        def PrimeroSecundaria():
            pass
        
        def SedundoSecundaria():
            pass

        def TerceroScundaria():
            pass

        def CuartoSecundaria():
            pass

        def QuintoSecundaria():
            pass

        def SextoSecundaria():
            pass
            
    def alumnosContar(self):
        alumnos = int(input("cuantos alumnos hay?"))
        rango = range(alumnos)
        guardado = []
        for crear in range(alumnos):
            nombre = input(f"cual es el nombre del estudiante {crear}")
            apellido = input("cual es el apellido?")
            persona = estudiante(nombre,apellido,'primaria' , "matematica")
            guardado.append(persona.nombre)
            print(f"has creado una alumno con el nombre de {nombre}")
            print(persona.__str__())
        for i in guardado:
            print(f"tus estudiantes son: {i}")
        return "aqui acaba el guardado de alumno en el curso"

