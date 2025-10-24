# Inventario Escolar

Aplicacion web desarrollada con Django para la gestión de equipos tecnológicos del Colegio Andes del Sur.

## Objetivos principales:
- Desarrollar una aplicación web funcional utilizando el framework Django.
- Configurar una base de datos relacional (SqLite o MySQL).
- Aplicar el ORM de Django mediante la creación del modelo `Equipo`.
- Personalizar el panel de administración para facilitar la gestión.
- Documentar el código y mantener buenas prácticas de desarrollo.

## Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/inventario_escolar.git
   cd inventario_escolar

2. Crear entorno virtual e instalar dependencias:
   python -m venv venv
   venv\Scripts\activate
   pip install django

3. Ejecutar migraciones:
  python manage.py migrate

4. Iniciar el servidor:
   python manage.py runserver

Funciones
* Registro y gestión de equipos desde la administración.
* Personalización del panel admin.
* Conexión funcional a la base de datos (SqLite)
