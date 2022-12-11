import pickle

class profesor():
    def __init__(self,nombre,apellido,curso,materia):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.materia = materia


    def __str__(self):
        informacion = f"""
su nombre es: {self.nombre}
su apellido es: {self.apellido}
su curso es:{self.curso}
su profecion es:{self.profesion}
"""
        return informacion


    def recordatorio(self):
        pass
#ver los videos de pildorasInformaticas para
#entender esto ya que es mejor conprender esto mejor
