# 🎵 Taller de Música Elguera - Sistema de Gestión de Inscripciones

> **Proyecto Universitario** - Desarrollo de Aplicaciones Web

Sistema web para la gestión de inscripciones y promoción de cursos de música del Taller de Música Elguera en Arequipa, Perú.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue.svg)

## 📚 Información Académica

- **Institución**: Universidad Nacional de San Agustin
- **Curso**: Introduccion al Desarrollo de Software / Ingeniería de Sistemas
- **Ciclo/Semestre**: 2
- **Año Académico**: 2025
- **Docente**: Ing. Marco Aedo Lopez

## 👥 Autor
Josue Enrique Camero Elguera

## 📋 Descripción del Proyecto

Aplicación web desarrollada con Flask como proyecto final del curso de Introduccion al Desarrollo de Software. El sistema permite a los estudiantes del Taller de Música Elguera explorar los diferentes instrumentos y talleres musicales disponibles, conocer los planes de estudio, y realizar inscripciones en línea. Incluye un panel administrativo para gestionar las inscripciones.

### 🎯 Objetivos del Proyecto

#### Objetivo General
Integrar frontend, backend y base de datos en un proyecto personal, reforzando la comprensión del flujo completo de una aplicación web.
#### Objetivos Específicos
- Implementar un sistema de gestión de base de datos relacional con PostgreSQL
- Desarrollar una interfaz web responsive y accesible siguiendo las mejores prácticas de UX/UI
- Crear un sistema de validación de datos en el frontend y backend
- Aplicar el patrón MVC (Model-View-Controller) en la arquitectura del proyecto
- Implementar un panel administrativo para la gestión de inscripciones
- Desplegar la aplicación en un servicio de hosting en la nube

## ✨ Características Implementadas

- **Página principal** con información del taller y galería de imágenes interactiva
- **Páginas dedicadas** para cada instrumento/taller:
  - Guitarra Eléctrica
  - Guitarra Acústica
  - Batería
  - Canto
  - Órgano/Teclado
  - Violín
  - Aprestamiento Musical (niños 3-5 años)
- **Sistema de inscripción** con formulario validado (cliente y servidor)
- **Tres planes de estudio**: Inicial, Básico y Pro
- **Panel administrativo** para visualizar inscripciones
- **Diseño responsive** adaptado a dispositivos móviles y tablets
- **Integración con redes sociales** del taller
- **Mapa de ubicación** mediante Google Maps API

## 🛠️ Stack Tecnológico

### Backend
- **Flask 3.1.2** - Framework web minimalista de Python
- **Flask-SQLAlchemy 3.1.1** - ORM para abstracción de base de datos
- **PostgreSQL** - Sistema de gestión de base de datos relacional
- **psycopg2-binary 2.9.11** - Adaptador PostgreSQL para Python
- **Gunicorn 23.0.0** - Servidor WSGI para entorno de producción

### Frontend
- **HTML5** - Estructura semántica de las páginas
- **CSS3** - Estilos y diseño visual
  - CSS Grid para layouts complejos
  - Flexbox para alineación de elementos
  - Animaciones y transiciones personalizadas
- **JavaScript** (Vanilla) - Interactividad del lado del cliente
  - Validación de formularios
  - Galería lightbox
  - Carrusel infinito de imágenes

### Herramientas de Desarrollo
- **Git & GitHub** - Control de versiones
- **VS Code** - Editor de código
- **PostgreSQL Admin** - Gestión de base de datos
- **Postman** - Pruebas de endpoints (opcional)

### Despliegue
- **Render** - Plataforma de hosting en la nube
- **PostgreSQL en la nube** - Base de datos administrada

---

## 🚀 INSTRUCCIONES PARA EJECUTAR EL PROYECTO

### 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

| Software | Versión Mínima | Descarga |
|----------|----------------|----------|
| **Python** | 3.8+ | [python.org](https://www.python.org/downloads/) |
| **PostgreSQL** | 12+ | [postgresql.org](https://www.postgresql.org/download/) |
| **pip** | 20+ | Incluido con Python |
| **Git** | 2.30+ | [git-scm.com](https://git-scm.com/downloads) |

### ✅ Verificar Instalaciones

Abre tu terminal y ejecuta los siguientes comandos para verificar:
```bash
# Verificar Python
python --version
# Debería mostrar: Python 3.8.x o superior

# Verificar pip
pip --version
# Debería mostrar la versión de pip

# Verificar PostgreSQL
psql --version
# Debería mostrar: psql (PostgreSQL) 12.x o superior

# Verificar Git
git --version
# Debería mostrar: git version 2.x.x
```

---

### 📥 Paso 1: Clonar el Repositorio
```bash
# Clonar el proyecto desde GitHub
git clone https://github.com/JCamro/Foro-Taller-de-Musica

# Navegar al directorio del proyecto
cd taller-musica-elguera

# Verificar que estás en la rama correcta
git branch
```

---

### 🔧 Paso 2: Configurar el Entorno Virtual

#### En Windows:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Tu terminal debería mostrar (venv) al inicio
```

**Nota**: Para desactivar el entorno virtual en cualquier momento, ejecuta:
```bash
deactivate
```

---

### 📦 Paso 3: Instalar Dependencias

Con el entorno virtual activado:
```bash
# Actualizar pip (recomendado)
pip install --upgrade pip

# Instalar todas las dependencias del proyecto
pip install -r requirements.txt

# Verificar instalación
pip list
```

Deberías ver instalados:
- Flask 3.1.2
- Flask-SQLAlchemy 3.1.1
- psycopg2-binary 2.9.11
- Gunicorn 23.0.0
- Y otras dependencias

---

### 🗄️ Paso 4: Configurar PostgreSQL

#### 4.1 Crear la Base de Datos

**Opción A: Usando pgAdmin (Interfaz Gráfica)**

1. Abre pgAdmin
2. Conecta al servidor PostgreSQL
3. Click derecho en "Databases" → "Create" → "Database"
4. Nombre: `taller_musica`
5. Click "Save"

**Opción B: Usando línea de comandos**
```bash
# Conectar a PostgreSQL (Windows)
psql -U postgres

# Conectar a PostgreSQL (macOS/Linux)
sudo -u postgres psql
```

Una vez dentro de PostgreSQL:
```sql
-- Crear la base de datos
CREATE DATABASE taller_musica;

-- Crear un usuario (opcional pero recomendado)
CREATE USER taller_user WITH PASSWORD 'tu_contraseña_segura';

-- Otorgar privilegios
GRANT ALL PRIVILEGES ON DATABASE taller_musica TO taller_user;

-- Salir de PostgreSQL
\q
```

#### 4.2 Verificar la Conexión
```bash
# Conectar a la base de datos creada
psql -U postgres -d taller_musica

# Si todo funciona, verás:
# taller_musica=#

# Salir
\q
```

---

### ⚙️ Paso 5: Configurar Variables de Entorno

#### 5.1 Crear archivo `.env` (Recomendado para desarrollo)

En la raíz del proyecto, crea un archivo llamado `.env`:
```bash
# En Windows
echo. > .env

# En macOS/Linux
touch .env
```

#### 5.2 Editar el archivo `.env`

Abre `.env` con tu editor de texto y agrega:
```env
# Configuración de Base de Datos
DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/taller_musica

# O si creaste un usuario específico:
# DATABASE_URL=postgresql://taller_user:tu_contraseña_segura@localhost:5432/taller_musica

# Configuración de Flask
FLASK_ENV=development
FLASK_DEBUG=True
```

#### 5.3 Verificar `.gitignore`

Asegúrate de que tu archivo `.gitignore` contenga:
```
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
```

---

### 🎯 Paso 6: Inicializar la Base de Datos

El proyecto crea automáticamente las tablas al iniciar, pero puedes verificar:
```bash
# Activar entorno virtual (si no está activado)
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Iniciar Python interactivo
python

# Dentro de Python, ejecutar:
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
...     print("Tablas creadas exitosamente")
... 
>>> exit()
```

---

### ▶️ Paso 7: Ejecutar la Aplicación

#### Método 1: Ejecución Directa (Desarrollo)
```bash
# Asegúrate de que el entorno virtual esté activado
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

# Ejecutar la aplicación
python app.py
```

Deberías ver algo como:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in production.
 * Running on http://127.0.0.1:5000
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

#### Método 2: Usando Flask CLI (Alternativa)
```bash
# Configurar la aplicación Flask
export FLASK_APP=app.py    # macOS/Linux
set FLASK_APP=app.py       # Windows CMD
$env:FLASK_APP="app.py"    # Windows PowerShell

# Ejecutar en modo desarrollo
flask run

# O en un puerto específico
flask run --port=8000
```

---

### 🌐 Paso 8: Acceder a la Aplicación

Abre tu navegador web y visita:

**URLs disponibles:**

| URL | Descripción |
|-----|-------------|
| `http://localhost:5000` | Página principal |
| `http://localhost:5000/reserva` | Formulario de inscripción |
| `http://localhost:5000/guitarra_electrica` | Página de guitarra eléctrica |
| `http://localhost:5000/guitarra_acustica` | Página de guitarra acústica |
| `http://localhost:5000/bateria` | Página de batería |
| `http://localhost:5000/canto` | Página de canto |
| `http://localhost:5000/organo` | Página de órgano |
| `http://localhost:5000/violin` | Página de violín |
| `http://localhost:5000/aprestamiento_musical` | Página de aprestamiento |
| `http://localhost:5000/admin_taller` | Panel administrativo |

---

### ✅ Paso 9: Probar la Aplicación

#### 9.1 Realizar una Inscripción de Prueba

1. Ve a `http://localhost:5000/reserva`
2. Completa el formulario con datos de prueba:
   - **DNI**: 12345678
   - **Apellido Paterno**: Pérez
   - **Apellido Materno**: García
   - **Nombres**: Juan Carlos
   - **Edad**: 25
   - **Teléfono**: 987654321
   - **Instrumento**: Guitarra Eléctrica
   - **Plan**: Paquete Pro
3. Click en "Enviar Inscripción"

#### 9.2 Verificar en el Panel Administrativo

1. Ve a `http://localhost:5000/admin_taller`
2. Deberías ver tu inscripción de prueba en la tabla

#### 9.3 Verificar en la Base de Datos
```bash
# Conectar a PostgreSQL
psql -U postgres -d taller_musica

# Ver todas las inscripciones
SELECT * FROM reserva;

# Deberías ver tu registro de prueba
# Salir
\q
```

---

### 🛑 Detener la Aplicación

Para detener el servidor Flask:

1. En la terminal donde está corriendo, presiona: `CTRL + C`
2. Para desactivar el entorno virtual: `deactivate`

---

## 📂 Estructura de Archivos Importantes
```
taller-musica-elguera/
│
├── 📄 app.py                    ⭐ ARCHIVO PRINCIPAL - Aplicación Flask
├── 📄 requirements.txt          ⭐ DEPENDENCIAS - Instalar con pip
├── 📄 .env                      ⭐ CONFIGURACIÓN - Variables de entorno
├── 📄 .gitignore               ⭐ GIT - Archivos a ignorar
├── 📄 README.md                 📖 Esta documentación
│
├── 📁 templates/                🎨 VISTAS - HTML Templates
│   ├── index.html
│   ├── reserva.html
│   └── [otros archivos .html]
│
├── 📁 static/                   🎭 RECURSOS ESTÁTICOS
│   ├── 📁 css/                  🎨 Hojas de estilo
│   ├── 📁 script/               💻 JavaScript
│   └── 📁 imagenes/             🖼️ Imágenes y assets
│
└── 📁 venv/                     🐍 ENTORNO VIRTUAL (no subir a Git)
```


## 🗂️ Modelo de Datos

### Diagrama Entidad-Relación

El sistema utiliza una base de datos relacional con la siguiente estructura:

### Tabla: Reserva (Modelo - MVC)

| Campo       | Tipo         | Restricciones | Descripción                          |
|-------------|--------------|---------------|--------------------------------------|
| dni         | String(20)   | PRIMARY KEY, NOT NULL | DNI del estudiante (identificador único) |
| ap_paterno  | String(100)  | NOT NULL      | Apellido paterno del estudiante      |
| ap_materno  | String(100)  | NOT NULL      | Apellido materno del estudiante      |
| nombre      | String(100)  | NOT NULL      | Nombres del estudiante               |
| telefono    | String(20)   | NOT NULL      | Número telefónico de contacto (9 dígitos) |
| instrumento | String(50)   | NOT NULL      | Instrumento o taller seleccionado    |
| plan        | String(50)   | NOT NULL      | Plan elegido (inicial/basico/pro)    |

**Nota**: El DNI se utiliza como clave primaria ya que es único para cada estudiante en Perú.

---

## 🎯 Rutas de la Aplicación (Controlador - MVC)

| Ruta                     | Método    | Descripción                           | Controlador    |
|--------------------------|-----------|---------------------------------------|----------------|
| `/`                      | GET       | Página principal del taller           | `index()`      |
| `/reserva`               | GET, POST | Formulario de inscripción             | `reserva()`    |
| `/aprestamiento_musical` | GET       | Información aprestamiento musical     | `aprestamiento()` |
| `/bateria`               | GET       | Información curso de batería          | `bateria()`    |
| `/canto`                 | GET       | Información taller de canto           | `canto()`      |
| `/guitarra_electrica`    | GET       | Información guitarra eléctrica        | `guitarra_electrica()` |
| `/guitarra_acustica`     | GET       | Información guitarra acústica         | `guitarra_acustica()` |
| `/organo`                | GET       | Información órgano/teclado            | `organo()`     |
| `/violin`                | GET       | Información curso de violín           | `violin()`     |
| `/admin_taller`          | GET       | Panel administrativo                  | `admin()`      |

---

## 💰 Sistema de Planes de Estudio

### Paquete Inicial - S/ 80
- 4 sesiones mensuales (1 por semana)
- Material de estudio digital incluido
- Asesoría personalizada
- Ideal para principiantes

### Paquete Básico - S/ 160
- 8 sesiones mensuales (2 por semana)
- Material de estudio digital incluido
- Técnica y repertorio
- Asesoría personalizada
- Recomendado para progreso constante

### Paquete Pro - S/ 200 ⭐ (Más Popular)
- 12 sesiones mensuales (3 por semana)
- Material premium incluido
- Acceso a jam sessions grupales
- Grabación de covers/demos
- Participación en eventos
- Certificado de nivel
- Ideal para estudiantes comprometidos

---

## 🔧 Funcionalidades Técnicas Destacadas

### Validación de Formularios (Frontend - JavaScript)
```javascript
// Validación de DNI: 8 dígitos numéricos
function dniValido(dni) {
    const regexDni = /^[0-9]{8}$/;
    return regexDni.test(dni);
}

// Validación de teléfono: inicia con 9 y tiene 9 dígitos
function numeroValido(numero) {
    const regexCelular = /^9[0-9]{8}$/;
    return regexCelular.test(numero);
}

// Validación de edad según instrumento
function validarClasificacionEdad(edad, instrumento) {
    // Lógica de validación por instrumento
}
```

### Validación Backend (Python - Flask)
```python
@app.route("/reserva", methods=["GET", "POST"])
def reserva():
    if request.method == "POST":
        try:
            nueva_reserva = Reserva(...)
            db.session.add(nueva_reserva)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            return f"Error: {e}"
```

### Características de UX/UI Implementadas
- **Navegación sticky**: Menú fijo al hacer scroll
- **Carrusel infinito**: Animación CSS con `@keyframes`
- **Galería lightbox**: Modal JavaScript para expandir imágenes
- **Cards interactivas**: Efectos hover y transiciones suaves
- **Diseño mobile-first**: Responsive desde 320px hasta 4K
- **Integración Google Maps**: iFrame responsive

---

## 🚀 Despliegue en Producción

### Plataforma: Render

1. **Preparación del repositorio**
```bash
git add .
git commit -m "Preparar para despliegue"
git push origin main
```

2. **Configuración en Render**
- Crear cuenta en [Render.com](https://render.com)
- Nuevo Web Service → Conectar con GitHub
- Configurar variables de entorno
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

3. **Variables de entorno necesarias**
```
DATABASE_URL=postgresql://user:pass@host:5432/dbname
FLASK_ENV=production
SECRET_KEY=tu_clave_secreta_aqui
```

### URL del Proyecto Desplegado
🔗 [https://taller-musica-elguera.onrender.com/](https://taller-musica-elguera.onrender.com/)

---

## 📊 Resultados y Análisis

### Funcionalidades Logradas
✅ Sistema CRUD completo para inscripciones  
✅ Interfaz responsive en todos los dispositivos  
✅ Validación de datos en frontend y backend  
✅ Panel administrativo funcional  
✅ Integración con servicios externos (Google Maps)  
✅ Despliegue exitoso en la nube  

### Métricas del Proyecto
- **Líneas de código Python**: ~150
- **Líneas de código HTML/CSS**: ~2500
- **Líneas de código JavaScript**: ~100
- **Tiempo de desarrollo**: [X semanas]
- **Páginas implementadas**: 10
- **Rutas funcionales**: 10

---

## 🧪 Pruebas Realizadas

### Pruebas Funcionales
- ✅ Registro de estudiantes con datos válidos
- ✅ Validación de formularios (DNI, teléfono, edad)
- ✅ Navegación entre páginas
- ✅ Visualización en panel administrativo
- ✅ Responsive design en diferentes dispositivos

### Pruebas de Usabilidad
- ✅ Navegación intuitiva
- ✅ Tiempo de carga < 3 segundos
- ✅ Formularios fáciles de completar
- ✅ Feedback visual en interacciones

---

## 📝 Conclusiones

Este proyecto universitario permitió aplicar de manera práctica los conocimientos adquiridos en el curso de Desarrollo de Aplicaciones Web. Se logró implementar exitosamente:

1. **Arquitectura MVC**: Separación clara entre modelo, vista y controlador
2. **Base de datos relacional**: Diseño e implementación con PostgreSQL
3. **Frontend moderno**: HTML5, CSS3 y JavaScript siguiendo estándares web
4. **Backend robusto**: Flask con manejo de sesiones y validaciones
5. **Despliegue en la nube**: Experiencia con plataformas de hosting modernas

### Aprendizajes Clave
- Manejo de ORMs (SQLAlchemy)
- Validación de datos en múltiples capas
- Diseño responsive y accesible
- Control de versiones con Git
- Deployment y gestión de variables de entorno

### Posibles Mejoras Futuras
- [ ] Sistema de autenticación para administradores
- [ ] Dashboard con estadísticas de inscripciones
- [ ] Sistema de pagos en línea
- [ ] Notificaciones por correo electrónico
- [ ] Sistema de horarios y asignación de profesores
- [ ] App móvil nativa

---

## 📱 Información del Taller

- 📍 **Dirección**: Sosa Ruiz 706, Arequipa, Perú
- 📘 **Facebook**: [Taller de Música Elguera](https://www.facebook.com/TallerDeMusicaElguera)
- 🎥 **YouTube**: [Marc Band Rock](https://www.youtube.com/@marcbandrock9383/videos)
- 🎵 **TikTok**: [@taller.elguera](https://www.tiktok.com/@taller.elguera)

---

## 📚 Referencias y Recursos

### Documentación Consultada
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [CSS Tricks](https://css-tricks.com/)
