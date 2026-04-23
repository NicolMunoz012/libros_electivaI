# Sistema de Gestión de Libros - Django

Una aplicación web desarrollada en Django para la gestión de autores y libros con funcionalidades CRUD completas.

## 🚀 Características

- ✅ CRUD completo para Autores
- ✅ CRUD completo para Libros
- ✅ Relación Autor-Libro (ForeignKey)
- ✅ Interfaz responsive con Bootstrap
- ✅ Panel de administración de Django
- ✅ Validación de formularios
- ✅ Base de datos SQLite (desarrollo) / PostgreSQL (producción)

## 📋 Requisitos

- Python 3.11+
- Django 6.0.4
- Ver `requirements.txt` para dependencias completas

## 🛠️ Instalación Local

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd libros_electivaI
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # Linux/Mac
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   cd proyecto
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor**
   ```bash
   python manage.py runserver
   ```

7. **Acceder a la aplicación**
   - Aplicación: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## 🌐 Despliegue en Render

### Opción 1: Despliegue Manual

1. **Conectar repositorio a Render**
   - Ve a [Render Dashboard](https://dashboard.render.com/)
   - Conecta tu repositorio de GitHub/GitLab

2. **Crear Base de Datos PostgreSQL**
   - Crea una nueva base de datos PostgreSQL (plan gratuito)
   - Copia la URL de conexión interna

3. **Crear Servicio Web**
   - Crea un nuevo Web Service
   - Selecciona Python 3 como runtime
   - Configurar comandos:
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn proyecto.wsgi:application --bind 0.0.0.0:$PORT`

4. **Configurar Variables de Entorno**
   ```
   DATABASE_URL=<url_de_tu_base_de_datos_postgresql>
   SECRET_KEY=<clave_secreta_generada>
   DEBUG=False
   WEB_CONCURRENCY=4
   PYTHON_VERSION=3.11.0
   ```

### Opción 2: Despliegue con Blueprint (render.yaml)

1. **Usar el archivo render.yaml incluido**
   - El proyecto incluye un archivo `render.yaml` preconfigurado
   - Ve a Render Dashboard > Blueprints
   - Crea nuevo Blueprint desde tu repositorio
   - Render creará automáticamente la base de datos y el servicio web

## 📁 Estructura del Proyecto

```
libros_electivaI/
├── proyecto/                    # Proyecto Django principal
│   ├── manage.py               # Script de gestión de Django
│   ├── proyecto/               # Configuración del proyecto
│   │   ├── settings.py         # Configuración (desarrollo/producción)
│   │   ├── urls.py            # URLs principales
│   │   └── wsgi.py            # Configuración WSGI
│   ├── gestion/               # Aplicación principal
│   │   ├── models.py          # Modelos (Autor, Libro)
│   │   ├── views.py           # Vistas CRUD
│   │   ├── forms.py           # Formularios
│   │   ├── urls.py            # URLs de la aplicación
│   │   ├── admin.py           # Configuración del admin
│   │   └── templates/         # Templates HTML
│   └── templates/             # Templates globales
├── requirements.txt           # Dependencias Python
├── Procfile                  # Configuración para Render
├── build.sh                  # Script de construcción
├── render.yaml              # Blueprint de Render
└── README.md                # Este archivo
```

## 🔧 Configuración de Producción

El proyecto está configurado para funcionar tanto en desarrollo como en producción:

- **Desarrollo**: Usa SQLite, DEBUG=True
- **Producción**: Usa PostgreSQL, DEBUG=False, archivos estáticos con WhiteNoise

### Variables de Entorno

- `DEBUG`: True/False (desarrollo/producción)
- `SECRET_KEY`: Clave secreta de Django
- `DATABASE_URL`: URL de conexión a la base de datos
- `WEB_CONCURRENCY`: Número de workers de Gunicorn

## 📝 Uso de la Aplicación

### Gestión de Autores
- **Listar**: Ver todos los autores registrados
- **Crear**: Agregar nuevo autor con nombre, correo, nacionalidad, fecha de nacimiento y biografía
- **Editar**: Modificar información de autores existentes
- **Eliminar**: Eliminar autores (elimina también sus libros asociados)

### Gestión de Libros
- **Listar**: Ver todos los libros con información del autor
- **Crear**: Agregar nuevo libro asociado a un autor
- **Editar**: Modificar información de libros existentes
- **Eliminar**: Eliminar libros específicos

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es parte de un taller académico de Django.

## 👥 Autores

- Desarrollado como parte del Taller 2 Django - Almacenamiento de Libros
- Universidad Cooperativa de Colombia - Electiva I