class Libro:
   # Atributo de clase
   total_libros = 0
   def __init__(self, titulo, autor):
      # Atributos de instancia
     self.titulo = titulo
     self.autor = autor
     # Incrementa el total de libros cada vez que se crea un nuevo objeto Libro
     Libro.total_libros += 1
     # Método de instancia
   def mostrar_info(self):
       # Utiliza self para acceder a los atributos de la instancia específica
      print(f"Título: {self.titulo}, Autor: {self.autor}")
    # Método de clase
    @classmethod
   def mostrar_total_libros(cls):
       # Utiliza cls para acceder al atributo de clase
      print(f"Total de libros: {cls.total_libros}")
# Creación de objetos (instancias de la clase Libro)
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")


# Uso del método de instancia para mostrar información específica de cada libro
libro1.mostrar_info() # Salida: Título: Cien Años de Soledad, Autor: Gabriel
García Márquez
libro2.mostrar_info() # Salida: Título: Don Quijote de la Mancha, Autor: Miguel de
Cervantes
# Uso del método de clase para mostrar el total de libros creados
Libro.mostrar_total_libros() # Salida: Total de libros: 2
