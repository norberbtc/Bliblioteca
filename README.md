# Sistema de Gestión de Biblioteca en Python

Este proyecto es una aplicación de terminal que te permite gestionar una biblioteca. Puedes agregar libros, prestarlos a usuarios, registrar nuevos usuarios y guardar los datos en un archivo. A continuación, se describen las principales características y cómo usar la aplicación:

## Características

1. **Agregar Libro**: Puedes ingresar el título y autor de un libro. Si el libro ya existe en la biblioteca, se incrementa su cantidad en uno. Si no existe, se agrega con una cantidad inicial de 1.

2. **Mostrar Libros**: Muestra la lista de libros en la biblioteca junto con su autor, cantidad y disponibilidad (disponible o no disponible) en la consola.

3. **Prestar Libro**: Permite prestar un libro a un usuario dado su título y nombre de usuario. Verifica si el libro está disponible y si el usuario está registrado. Si ambos criterios se cumplen, presta el libro al usuario y actualiza la disponibilidad del libro y la cantidad en la biblioteca.

4. **Registrar Usuario**: Agrega un usuario a la biblioteca.

5. **Guardar Datos**: Guarda los datos actuales de la biblioteca (libros y usuarios) en un archivo llamado `datos_biblioteca.pkl` utilizando el módulo `pickle`.

6. **Cargar Datos**: Intenta cargar los datos previos de la biblioteca desde el archivo `datos_biblioteca.pkl`. Si el archivo no existe, inicializa la biblioteca como vacía.

7. **Listar Usuarios**: Muestra una lista de los usuarios registrados en la biblioteca en la consola.

## Uso

1. Ejecuta el archivo `biblioteca.py` en la terminal.

2. Selecciona una opción del menú:

   - Para agregar un libro, ingresa el título y autor.
   - Para prestar un libro, ingresa el título del libro y el nombre de usuario.
   - Para registrar un usuario, ingresa el nombre de usuario.
   - Para guardar los datos, selecciona la opción correspondiente.
   - Para listar usuarios, selecciona la opción correspondiente.
   - Para salir, selecciona la opción "7".

3. Los datos se guardarán automáticamente al seleccionar la opción "Guardar Datos".
