# 🎵 Taller de Música Elguera

Sistema web para la gestión de inscripciones y promoción de cursos de música del Taller de Música Elguera en Arequipa, Perú.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Descripción

Aplicación web desarrollada con Flask que permite a los estudiantes explorar los diferentes instrumentos y talleres musicales disponibles, conocer los planes de estudio, y realizar inscripciones en línea. Incluye un panel administrativo para gestionar las inscripciones.

## ✨ Características

- **Página principal** con información del taller y galería de imágenes
- **Páginas dedicadas** para cada instrumento/taller:
  - Guitarra Eléctrica
  - Guitarra Acústica
  - Batería
  - Canto
  - Órgano/Teclado
  - Violín
  - Aprestamiento Musical (niños 3-5 años)
- **Sistema de inscripción** con formulario validado
- **Tres planes de estudio**: Inicial, Básico y Pro
- **Panel administrativo** para visualizar inscripciones
- **Diseño responsive** adaptado a dispositivos móviles
- **Integración con redes sociales** (Facebook, YouTube, TikTok)
- **Mapa de ubicación** con Google Maps

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask 3.1.2** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para base de datos
- **PostgreSQL** - Base de datos (con psycopg2-binary 2.9.11)
- **Gunicorn 23.0.0** - Servidor WSGI para producción

### Frontend
- **HTML5** y **CSS3**
- **JavaScript** vanilla para interactividad
- **Diseño responsive** con CSS Grid y Flexbox
- **Animaciones CSS** personalizadas

### Despliegue
- Compatible con **Render** (configurado para PostgreSQL en la nube)
- Variables de entorno para configuración segura

## 📦 Instalación

### Prerrequisitos
- Python 3.8 o superior
- PostgreSQL instalado y corriendo
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/taller-musica-elguera.git
cd taller-musica-elguera
```

2. **Crear entorno virtual**
```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**

Crear una base de datos PostgreSQL:
```sql
CREATE DATABASE taller_musica;
```

5. **Configurar variables de entorno**

Crear un archivo `.env` en la raíz del proyecto:
```env
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/taller_musica
```

6. **Ejecutar la aplicación**
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🗂️ Estructura del Proyecto
```
taller-musica-elguera/
│
├── app.py                          # Aplicación principal Flask
├── requirements.txt                # Dependencias del proyecto
│
├── templates/                      # Plantillas HTML
│   ├── index.html                  # Página principal
│   ├── reserva.html                # Formulario de inscripción
│   ├── aprestamiento.html          # Página de aprestamiento
│   ├── bateria.html                # Página de batería
│   ├── canto.html                  # Página de canto
│   ├── guitarra.html               # Página de guitarra acústica
│   ├── guitarra_Electrica.html     # Página de guitarra eléctrica
│   ├── organo.html                 # Página de órgano
│   └── violin.html                 # Página de violín
│
└── static/                         # Archivos estáticos
    ├── css/
    │   ├── style.css               # Estilos página principal
    │   ├── baseinstrumetos.css     # Estilos base instrumentos
    │   └── contenidoinstrumentos.css # Estilos contenido
    ├── script/
    │   └── script.js               # JavaScript principal
    └── imagenes/                   # Imágenes del sitio
        ├── hero-img/
        ├── talleres/
        ├── intrumentos_sf/
        ├── iconos/
        ├── galeria/
        ├── slide/
        └── logo-redes/
```

## 💾 Modelo de Datos

### Tabla: Reserva

| Campo       | Tipo         | Descripción                          |
|-------------|--------------|--------------------------------------|
| dni         | String(20)   | DNI del estudiante (Primary Key)     |
| ap_paterno  | String(100)  | Apellido paterno                     |
| ap_materno  | String(100)  | Apellido materno                     |
| nombre      | String(100)  | Nombres del estudiante               |
| telefono    | String(20)   | Número telefónico de contacto        |
| instrumento | String(50)   | Instrumento o taller seleccionado    |
| plan        | String(50)   | Plan elegido (inicial/basico/pro)    |

## 🎯 Rutas Principales

| Ruta                     | Método | Descripción                           |
|--------------------------|--------|---------------------------------------|
| `/`                      | GET    | Página principal                      |
| `/reserva`               | GET/POST | Formulario de inscripción           |
| `/aprestamiento_musical` | GET    | Página de aprestamiento musical       |
| `/bateria`               | GET    | Página de batería                     |
| `/canto`                 | GET    | Página de canto                       |
| `/guitarra_electrica`    | GET    | Página de guitarra eléctrica          |
| `/guitarra_acustica`     | GET    | Página de guitarra acústica           |
| `/organo`                | GET    | Página de órgano/teclado              |
| `/violin`                | GET    | Página de violín                      |
| `/admin_taller`          | GET    | Panel administrativo (inscripciones)  |

## 💰 Planes de Estudio

### Paquete Inicial - S/ 80
- 4 sesiones (1 por semana)
- Material de estudio incluido
- Ideal para comenzar

### Paquete Básico - S/ 160
- 8 sesiones (2 por semana)
- Técnica y repertorio
- Constancia en el aprendizaje

### Paquete Pro - S/ 200 ⭐ (Recomendado)
- 12 sesiones mensuales
- Acceso a jam sessions
- Grabaciones y presentaciones
- Material premium incluido

## 🔧 Funcionalidades Especiales

### Validación de Formularios (JavaScript)
- **DNI**: 8 dígitos numéricos
- **Teléfono**: Debe iniciar con 9 y tener 9 dígitos
- **Edad**: Validación según instrumento seleccionado
  - Aprestamiento: 3-5 años
  - Violín/Órgano: 6+ años
  - Batería/Guitarras: 7+ años
  - Canto: 5+ años

### Características de UX/UI
- Navegación sticky con efecto hover
- Carrusel infinito de imágenes
- Galería lightbox expandible
- Cards con animaciones al hover
- Diseño mobile-first responsive
- Integración de Google Maps

## 🚀 Despliegue en Producción

### Render (Recomendado)

1. Crear cuenta en [Render.com](https://render.com)
2. Crear un nuevo Web Service
3. Conectar repositorio de GitHub
4. Configurar variables de entorno:
   - `DATABASE_URL`: URL de PostgreSQL proporcionada por Render
5. Render detectará automáticamente el `requirements.txt`
6. El build command será: `pip install -r requirements.txt`
7. El start command será: `gunicorn app:app`

### Variables de Entorno Necesarias
```
DATABASE_URL=postgresql://...
FLASK_ENV=production
```

## 📱 Contacto y Redes Sociales

- 📍 **Dirección**: Sosa Ruiz 706, Arequipa, Perú
- 📘 **Facebook**: [Taller de Música Elguera](https://www.facebook.com/TallerDeMusicaElguera)
- 🎥 **YouTube**: [Marc Band Rock](https://www.youtube.com/@marcbandrock9383/videos)
- 🎵 **TikTok**: [@taller.elguera](https://www.tiktok.com/@taller.elguera)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🐛 Reporte de Bugs

Si encuentras algún bug, por favor abre un issue en GitHub con:
- Descripción detallada del problema
- Pasos para reproducir el error
- Capturas de pantalla (si aplica)
- Navegador y versión utilizada

## 📝 Notas Adicionales

- El sistema usa SQLAlchemy con `db.create_all()` para crear las tablas automáticamente
- La corrección de protocolo `postgres://` a `postgresql://` es necesaria para Render
- El proyecto incluye manejo de errores con rollback en caso de fallo en inscripciones
- Los enlaces de WhatsApp están pendientes de configuración

## 🎓 Autores

Desarrollado para el Taller de Música Elguera - Arequipa, Perú

---

⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!
