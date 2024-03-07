Proyecto Web Django: "Libros en Línea"

Este proyecto web Django llamado "Libros en Línea" está diseñado con una barra de navegación que dirige a diferentes páginas:
Inicio, Libros, Buscar Libros y Contacto. Los usuarios pueden ver el listado de libros disponibles, registrar sus cuentas, buscar libros y enviar comentarios a los administradores del sitio.

Funcionalidades:

1.	Herencia de HTML:
•	La herencia de HTML se implementa en todas las páginas del proyecto para mantener la consistencia en la apariencia y la estructura del sitio web.

2.	Diferentes Clases de Modelos:
•	Se han definido diferentes clases en el archivo models.py para organizar los datos de manera eficiente y mantener la integridad de la base de datos.

3.	Formulario para Insertar Datos:
•	El proyecto contiene formularios que permite a los usuarios registrar sus datos de usuario y enviar mensajes a los creadores del sitio desde la sección de contacto.
•	Los datos ingresados se almacenan en la base de datos y pueden ser visualizados desde el panel de administración.

4.	Formulario para Insertar Datos desde el Admin:
•	Desde el panel de administración de Django, los administradores pueden agregar libros especificando título, autor y género.

5.	Formulario de Búsqueda:
•	En la página de buscar libros, los usuarios pueden utilizar un formulario para buscar libros disponibles en la web.
