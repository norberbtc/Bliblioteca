import pickle

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        if titulo in self.libros:
            self.libros[titulo] += 1
        else:
            self.libros[titulo] = 1

    def mostrar_libros(self):
        print("Lista de libros:")
        for titulo, cantidad in self.libros.items():
            print(f"{titulo} (Autor: {self.obtener_autor(titulo)}), Cantidad: {cantidad}")

    def prestar_libro(self, titulo, usuario):
        if titulo in self.libros and self.libros[titulo] > 0:
            if usuario in self.usuarios:
                self.libros[titulo] -= 1
                print(f"Libro '{titulo}' prestado a {usuario}.")
            else:
                print(f"El usuario '{usuario}' no está registrado.")
        else:
            print(f"El libro '{titulo}' no está disponible.")

    def registrar_usuario(self, usuario):
        self.usuarios[usuario] = True

    def guardar_datos(self):
        with open("datos_biblioteca.pkl", "wb") as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)

    def cargar_datos(self):
        try:
            with open("datos_biblioteca.pkl", "rb") as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        except FileNotFoundError:
            print("El archivo 'datos_biblioteca.pkl' no existe. Inicializando biblioteca vacía.")

    def obtener_autor(self, titulo):
        # Implementa la lógica para obtener el autor de un libro (puede ser una base de datos o diccionario)
        return autor

if __name__ == "__main__":
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()

    while True:
        print("\n--- Menú ---")
        print("1. Agregar Libro")
        print("2. Mostrar Libros")
        print("3. Prestar Libro")
        print("4. Registrar Usuario")
        print("5. Guardar Datos")
        print("6. Listar Usuarios")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca.agregar_libro(titulo, autor)
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a prestar: ")
            usuario = input("Ingrese el nombre de usuario: ")
            biblioteca.prestar_libro(titulo, usuario)
        elif opcion == "4":
            usuario = input("Ingrese el nombre de usuario a registrar: ")
            biblioteca.registrar_usuario(usuario)
        elif opcion == "5":
            biblioteca.guardar_datos()
            print("Datos guardados correctamente.")
        elif opcion == "6":
            print("Usuarios registrados:")
            for usuario in biblioteca.usuarios:
                print(usuario)
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")
