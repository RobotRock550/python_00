class libro:
    # Constructor (__init__) para inicializar las propiedades
    def __init__(self, autor, editorial, anio,titulo,tipo_tapa,cant_hojas):
        self.autor = autor
        self.editorial = editorial
        self.anio = anio
        self.titulo = titulo
        self.tipo_tapa = tipo_tapa
        self.cant_hojas = cant_hojas
        self.pagina=1

    # Método para mostrar la información del auto
    def mostrar_info(self):
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial}")
        print(f"Año: {self.anio}")
        print(f"Titulo: {self.titulo}")
        print(f"Tapa: {self.tipo_tapa}")
        print(f"Cantidad de hojas: {self.cant_hojas}")

    # Método para arrancar el auto
    def cambiar_pagina(self):
        print(f"Cambiaste a la pagina {self.pagina} de {self.cant_hojas}")
        self.pagina+=1

    # Método para detener el auto
    def arrancar_paginas(self,cantidad):
        self.cant_hojas-=cantidad
        print(f"Has arrancado {cantidad} paginas, quedan {self.cant_hojas} paginas.")

    def quemar_libro(self):
        print(f"estas quemando a {self.titulo}")

# Crear objetos de la clase Auto
libro1 = libro("Gabriel García Márquez", "Sudamericana", 1967,"Cien años de soledad","tapa dura",471)

# Usar los métodos de los objetos
libro1.mostrar_info()
libro1.cambiar_pagina()
libro1.arrancar_paginas(20)
libro1.cambiar_pagina()
libro1.quemar_libro()
libro1.cambiar_pagina()
print()  # Separador entre autos
