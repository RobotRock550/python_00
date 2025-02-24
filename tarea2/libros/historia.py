from libros.libro import libro

class Historia(libro):
    def __init__(self, titulo, autor, año, paginas,cant_imagenes):
        super().__init__(titulo, autor, año, paginas)
        self.cant_imagenes=cant_imagenes

    def info(self):
        super().info()
        print(f"cantidad de imagenes:  {self.cant_imagenes}")

    def cambiar_pagina(self):
        super().cambiar_pagina()
    
    def cerrar(self):
        super().cerrar()
