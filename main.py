from profesor import *
from alumno import *
from time import sleep


#sleep(1.2)
#despues de terminar la clase hay que saber lo curso para eso hay que hacer
#que cada curso tenga un estudiante
class curso():
    def alumnosContar(self):
        alumnos = int(input("cuantos alumnos hay?"))
        rango = range(alumnos)
        guardado = []
        for crear in range(alumnos):
            nombre = input(f"cual es el nombre del estudiante {crear}")
            apellido = input("cual es el apellido?")
            andrew = estudiante(nombre,apellido,'primaria' , "matematica")
            guardado.append(andrew.nombre)
            print(f"has creado una alumno con el nombre de {nombre}")
            print(andrew.__str__())
        for i in guardado:
            print(f"tus estuante son: {i}")
        return "aqui acaba el guardado de alumno en el curso"
"""
con el def de alumnosContar vamos hacer unos 12 curso de la mitad primaria y la otra secundaria :)
se bienen cosas
"""
print(curso.alumnosContar(self=curso))

