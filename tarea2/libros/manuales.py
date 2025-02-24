from libros.libro import libro

class Manuales(libro):
    def __init__(self, titulo, autor, año, paginas,cant_diagramas):
        super().__init__(titulo, autor, año, paginas)
        self.cant_diagramas=cant_diagramas
    
    def info(self):
        super().info()
        print(f"cantidad de diagramas:  {self.cant_diagramas}")

    def cambiar_pagina(self):
        super().cambiar_pagina()
    
    def cerrar(self):
        super().cerrar()
