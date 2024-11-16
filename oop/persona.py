class Persona:
   def __init__(self, nombre, edad):
       # Atributos de instancia
       self.nombre = nombre
       self.edad = edad
       # Método de instancia para mostrar información
   def mostrar_info(self):
    print(f"Nombre: {self.nombre}, Edad: {self.edad}")
      
# Creación de objetos (instancias) de la clase Persona
persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)
# Uso del método de instancia para mostrar la información de cada persona
persona1.mostrar_info() # Salida: Nombre: Juan, Edad: 30
persona2.mostrar_info() # Salida: Nombre: Ana, Edad: 25