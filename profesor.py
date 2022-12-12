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

    def expulcion(self, n):
        if n == 0:
            return("bien, el alumno esta bien")
        elif n == 1:
            return('ok,el alumno se le tendra que pones una sancion')
        elif n == 2:
            return('el alumno sera suspendido por 15 dias')
        elif n >= 3:
            return('... el elumno  sera expulsado permanentemente')
    
    def notas(self,nota):
        
        if nota <= 0:
            return('...')
        elif nota >= 1 <= 30:
            return(f"{self.nombre} ha sacado una nota tan baja como para pasarlo")
        elif nota >= 31 <= 51:
            return(f'{self.nombre} ha sacado una nota meh pero no suficiente para pasarlo')
        elif nota >= 52 <= 64:
            return(f'{self.nombre} se ha exforzado pero no pudo pasar :(')
        elif nota >= 65 <= 69:
            return(f'{self.nombre} puede lograrlo pero se le dara una segunda opotunidad hiendo para completivo')
        elif nota == 70:
            return(f"{self.nombre} ha psasdo ya que es promedio ")
        elif nota >= 71 <= 80:
            return(f'{self.nombre} tiene una nota buena')
        elif nota >= 81 >= 89:
            return(f'{self.nombre} es un buen estudiante')
        elif nota >= 90 <= 99:
            return(f'{self.nombre} es un excelente estudiante')
        elif nota == 100:
            return(f"{self.nombre} es un estudiante meritorio")

    def promedioNotasEscolar(self,valor):
        
        while valor == True:
            si = input("quieres poner una nota? y/n")
            if si == 'y':
                numero1 = int(input("cual es la primera nota"))
                numero2 = int(input("cual es la segunda nota"))
                numero3 = int(input("cual e s la tercera nota"))
                numero4 = int(input("cual es la cuarta nota"))
                promedio = numero1 + numero2 
                promedio += numero3
                promedio += numero4
                return(f'la sumar total es: {promedio} y el promedio es {promedio / 4}')
                break;
                
            elif si == 'n':
                return("ok")
                break;
            else:
                return('la informacion es erronea')
