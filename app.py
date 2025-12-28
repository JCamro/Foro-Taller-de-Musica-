import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- CONFIGURACIÓN DE BASE DE DATOS ---
uri = os.getenv("DATABASE_URL") 

# Corrección de protocolo para Render
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELO DE DATOS ---
class Reserva(db.Model):
    dni = db.Column(db.String(20), primary_key=True)
    ap_paterno = db.Column(db.String(100), nullable=False)
    ap_materno = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    instrumento = db.Column(db.String(50), nullable=False)
    plan = db.Column(db.String(50), nullable=False)

# Crear las tablas automáticamente si no existen
with app.app_context():
    db.create_all()

# --- RUTAS ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aprestamiento_musical")
def aprestamiento():
    return render_template("aprestamiento.html")

@app.route("/bateria")
def bateria():
    return render_template("bateria.html")

@app.route("/canto")
def canto():
    return render_template("canto.html")

@app.route("/guitarra_electrica")
def guitarra_electrica():
    return render_template("guitarra_Electrica.html")

@app.route("/guitarra_acustica")
def guitarra_acustica():
    return render_template("guitarra.html")

@app.route("/organo")
def organo():
    return render_template("organo.html")

@app.route("/violin")
def violin():
    return render_template("violin.html")

@app.route("/reserva", methods=["GET", "POST"])
def reserva():
    if request.method == "POST":
        # Captura de datos del formulario (deben coincidir con el 'name' en HTML)
        nueva_reserva = Reserva(
            dni=request.form.get("dni"),
            ap_paterno=request.form.get("apellido-paterno"),
            ap_materno=request.form.get("apellido-materno"),
            nombre=request.form.get("nombre"),
            telefono=request.form.get("telefono"),
            instrumento=request.form.get("instrumento"),
            plan=request.form.get("plan")
        )
        
        try:
            db.session.add(nueva_reserva)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()  # Limpia la sesión para permitir nuevos intentos
            return f"Hubo un error al guardar la reserva: {e}"

    return render_template("reserva.html")

@app.route("/admin_taller")
def admin():
    # Consulta todos los registros guardados
    inscritos = Reserva.query.all()
    
    html = """
    <h1>Lista de Alumnos Inscritos</h1>
    <table border="1" style="width:100%; border-collapse: collapse;">
        <tr>
            <th>DNI</th>
            <th>Apellido Paterno</th>
            <th>Apellido Materno</th>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>Instrumento</th>
            <th>Plan</th>
        </tr>
    """
    
    for alumno in inscritos:
        html += f"""
        <tr>
            <td>{alumno.dni}</td>
            <td>{alumno.ap_paterno}</td>
            <td>{alumno.ap_materno}</td>
            <td>{alumno.nombre}</td>
            <td>{alumno.telefono}</td>
            <td>{alumno.instrumento}</td>
            <td>{alumno.plan}</td>
        </tr>
        """
    
    html += "</table><br><a href='/'>Volver al inicio</a>"
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)