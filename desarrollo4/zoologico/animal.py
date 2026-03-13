class Animal:

    def __init__(self, nombre, caracteristicas, clase):
        self.nombre = nombre
        self.caracteristicas = caracteristicas
        self.clase = clase

    def __str__(self):
        return f"{self.nombre} | Clase: {self.clase}"

    def __repr__(self):
        return f"Animal({self.nombre}, {self.caracteristicas}, {self.clase})"