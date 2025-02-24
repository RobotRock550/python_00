from libros.libro import libro

class Ciencia(libro):
    def __init__(self, titulo, autor, año, paginas,cant_formulas):
        super().__init__(titulo, autor, año, paginas)
        self.cant_formulas=cant_formulas

    def info(self):
        super().info()
        print(f"cantidad de formulas:  {self.cant_formulas}")

    def cambiar_pagina(self):
        super().cambiar_pagina()
    
    def cerrar(self):
        super().cerrar()
