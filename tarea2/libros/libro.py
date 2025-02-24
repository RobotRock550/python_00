class libro():
    def __init__(self,titulo,autor,año,paginas):
        self.titulo=titulo
        self.autor=autor
        self.año=año
        self.paginas=paginas
        self.hoja=1
    def info(self):
        print(f"titulo {self.titulo}")
        print(f"autor {self.autor}")
        print(f"año {self.año}")
        print(f"paginas  {self.paginas}")

    def cambiar_pagina(self):
        print(f"Cambiaste a la pagina: {self.hoja}")
    
    def cerrar(self):
        print(f"cerraste el libro {self.titulo}")
