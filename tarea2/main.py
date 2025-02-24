from libros.libro import libro
from libros.ciencias import Ciencia
from libros.historia import Historia
from libros.manuales import Manuales

matematicas=Ciencia("Aritmetica","baldor",1950,900,2000)
bolivia=Historia("historia de bolivia","carlos de mesa",2006,800,200)
epson=Manuales("Manual de usuario Epson","Epson",2015,50,20)

matematicas.info()
print()
bolivia.cambiar_pagina()
print()
epson.cerrar()