class estudiante():
    def __init__(self,nombre,apellido,curso,materia):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.materia = materia

    def __str__(self) -> str:
        informacion = """
tu nombre es: {0}
tu apellido es: {1}
tu curso es:{2}
tu materia es:{3}
""".format(self.nombre, self.apellido, self.curso, self.materia)
        return informacion
