# PRE-ENTREGRA 3 - CODERHOUSE - CURSO DE PYTHON

# Sobre el autor

Mi nombre es Daniela Soler y soy estudiante del curso de Python realizado a través de la plataforma de CoderHouse. Este proyecto es para poner en práctica los conocimientos básicos de crear una app web mediante Django.

# Descripción proyecto

Consta de la creación de una página web mediante app, el cual tiene como temática brindar información al usuario acerca del Universo de Star Wars.
Este posee 7 app instaladas siendo Home la página de acceso principal, y el resto de las apps se encuentran mostradas como sub urls en la página web. Cabe mencionar que 2 de estas poseen formularios para que el usuario pueda llenar y ver los cambios que realizó directo en la página web.
A su vez, posee configurada la función administrador para crear e insertar datos a las diferentes apps, y los cambios realizados en el administrador se ven reflejadas en la página web.

Apps con formularios
- Historia: 2 formularios
- Subcripción: 1 formulario

# Especificaciones técnica

Para poder agregar información a la base de datos de cualquier app (excepto Home) y ser visualizada directo en la página web, se debe ingresar al admin de la página web `http://127.0.0.1:8000/admin/`.

Usuario: `admin`
Contraseña: `1234`

Aquí se entra al administrador de Django, donde se puede añadir información a las 6 apps (con excepción de Home). 

# Cosas a mejorar

- Aspecto de colores de la página web, el cuál se encuentra en código .css
- Lograr encadenar las imágenes puestas detro de las apps de forma más eficiente (a través de herencia).
- Hacer que desde el admin o desde los formularios, poder insertar imágenes para respetar la estructura de las apps.
- Se podría hacer más eficiente el código utilizando menos apps, ya que las apps `Juegos`, `Libreria`, `Lugares` y `series_peliculas` se basan en el mismo template, por lo que podría disminuirse el código mediante herencia de templates.
- En la lista de personajes, poder separar los botones de `Ver detalle`, `Actualizar` y `Eliminar` para mayor comodidad visual.

# Cómo hacer funcionar el proyecto

Este proyecto se pasará con link directo de la plataforma de GitHub.
Para bajar la información del proyecto, copiar el url y escribir en la consola de Visual Studio Code (dentro del directorio deseado):

**`git clone https://github.com/Daniela1221/Pre-entrega3Python.git`**

Este proyecto se encuentra respaldado en su totalidad, con excepción del entorno virtual. Por lo que se debe crear el entrono virtual para poder acceder directamente al proyecto.Ejecute

**`python -m venv .venv`**

Luego de creado el entorno virtual (se encontrará dentro de la carpeta .venv), activar el entorno de la siguiente forma. Para Windows ejecutar:

**`source .venv/Scripts/activate`**

Para Mac o Linux ejecutar:

**`source .venv\bin\activate`**

Una vez activo el entorno (aparecerá al principio del directorio `(.venv)`), debemos ejecutar archivo requirements.txt que se encuentra dentro de la carpeta `project`, el cual instalará dentro del entorno virtual lo necesario para correr el proyecto.

**`cd project`**
**`pip install -r requirements.txt`**

El cual fue creado con el comando `pip freeze >> requirements.txt`.

Realizar migraciones:

**`python manage.py makemigrations`**
**`python manage.py migrate`**

Para finalizar, hacemos correr el servidor, el cual nos dará una url local para visualizar la página web creada. Este comando debe ejecutarse DENTRO de la carpeta project para que encuentre el archivo manage.py

**`python manage.py runserver`**

Para finalizar la ejecución del servidor, pulse las teclas `CTRL + C`.
