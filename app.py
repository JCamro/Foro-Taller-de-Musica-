import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

uri = os.getenv("DATABASE_URL") 

if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    instrumento = db.Column(db.String(50), nullable=False)
    plan = db.Column(db.String(50), nullable=False)


# Crear las tablas en la base de datos
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
        # Datos del formulario
        nueva_reserva = Reserva(
            nombre=request.form.get("nombre"),
            dni=request.form.get("dni"),
            telefono=request.form.get("telefono"),
            instrumento=request.form.get("instrumento"),
            plan=request.form.get("plan")
        )
        
        # Guardar en la base de datos de Render
        try:
            db.session.add(nueva_reserva)
            db.session.commit()
            return redirect(url_for('index')) # Redirige al inicio tras éxito
        except Exception as e:
            return f"Hubo un error al guardar la reserva: {e}"

    return render_template("reserva.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)