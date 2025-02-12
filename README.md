  # Proyecto Pyolingo 2DAM Acceso a datos
Este es un proyecto desarrollado por un grupo de 3 estudiantes de 2 de dam. El proyecto consiste en hacer una app para aprender idiomas estilo duolingo.

## Herramientas utilizadas:
- Python como lenguaje de programacion principal
- Base de datos MariaDB
- Plataforma de trabajo Visual Studio Code
- Control de versiones Github

## Especificaciones tecnicas
- certifi = 2024.8.30
- charset-normalizer = 3.4.0
- customtkinter = 5.2.2
- darkdetect = 0.8.0
- idna = 3.10
- numpy = 2.1.3
- packaging = 24.2
- pillow = 11.0.0
- requests = 2.32.3
- scipy = 1.14.1
- SpeechRecognition = 3.11.0
- tk = 0.1.0
- typing_extensions = 4.12.2
- urllib3 = 2.2.3
- wavio = 0.0.9

## Guia de instalacion / Ejecucion
### Instalacion de dependencias
1. Es necesario tener instalado en el equipo el ``python`` el cual se puede instalar desde su propia pagina web(https://www.python.org/) o desde el store de microsoft.
2. Una vez echo esto nos movemos al fichero ``hola.ps1`` en la carpeta ``powerShell``.
3. Una vez en el fichero desde el ``visual studio code`` con la extencion para lanzar powerShell le damos a ejecutar y este instalara / actulizara las dependencias para que la app funcione.
4. Si la opcion anterior no nos gusta tambien podemos abrir una terminal powerShell y copiar y pegar los comandos que no aparecen comentados.

### Instalacion de la base de datos
1. Primero sera necesario tener instalado el ``Xampp``  que lo podremos descargar desde su propia web(https://www.apachefriends.org/).
2. Una vez lo tengamos instalado lo ejecutaremos, encendiendo los botones de ``apache`` , ``MYSQL``.
3. Con el XAMPP en funcionamiento iremos al navegador accederemos a la ruta(http://localhost/phpmyadmin/).
4. Una vez en la web pulsamos el boton de nuevo y creamos una base de datos con el nombre de ``pyolingo``.
5. Una vez creada la base de datos en el boton de import importaremos el fichero ``pyolingo(06-11-2024).sql`` que esta en la ruta ``db/backups``.

### Ejecucion del programa
1. Cuando ya tengamos todas las dependencias instaladas y la base de datos preparada, nos ubicaremos en el fichero ``main.py``.
2. Una vez en el fichero ``main.py`` solo tendremos que ejecutar el programa con el boton ``run and debug`` y este se lanzara.
