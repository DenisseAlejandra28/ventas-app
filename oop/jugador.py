# Definimos la clase Jugador, que representará a un jugador de un deporte o equipo.
  class Jugador:
    # Método constructor: se ejecuta al crear una nueva instancia de Jugador.
    # Aquí definimos los atributos 'nombre' y 'equipo' que almacenan el nombre del
   def __init__(self, nombre, equipo):
       self.nombre = nombre # Atributo nombre: almacena el nombre del jugador.
       self.equipo = equipo # Atributo equipo: almacena el nombre del equipo en


    # Método especial __str__: se llama automáticamente al imprimir el objeto.
    # Devuelve una representación en texto del jugador, en este caso "nombre juega

   def __str__(self):
       return f"{self.nombre} juega en {self.equipo}"
   

# Método de clase obtener: permite crear un nuevo objeto Jugador solicitando
datos al usuario.
# Usa 'cls' en lugar de 'self' porque es un método de clase (no necesita un
objeto creado previamente).
@classmethod
def obtener(cls):
# Pedimos al usuario que ingrese el nombre y el equipo del jugador.
nombre = input("Nombre: ") # Solicita el nombre del jugador.
equipo = input("Equipo: ") # Solicita el equipo del jugador.
# Creamos y devolvemos una nueva instancia de Jugador con los datos
ingresados.
return Jugador(nombre, equipo)
# Usamos el método de clase obtener para crear una instancia de Jugador.
jugador = Jugador.obtener()
# Imprimimos la información del jugador usando el método __str__ de la clase.
# Esto mostrará "nombre juega en equipo", gracias al método __str__.
print(jugador)
