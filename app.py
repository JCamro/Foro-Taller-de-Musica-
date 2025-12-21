from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index(): # Cambiado de root a index
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


@app.route("/reserva", methods=["POST"])
def reserva():
    if request.method == "POST":
        
        nombre_estudiante = request.form.get("nombre")
        dni_estudiante = request.form.get("dni")
        telefono_estudiante = request.form.get("telefono")
        instrumento_seleccionado = request.form.get("instrumento")
        plan_seleccionado = request.form.get("plan")

        try:
            # 2. Creamos el objeto con el modelo Inscripcion que definimos antes
            nueva_inscripcion = Inscripcion(
                nombre=nombre_estudiante,
                dni=dni_estudiante,
                instrumento=instrumento_seleccionado,
                plan=plan_seleccionado
            )

            # 3. Guardamos en PostgreSQL
            

            # 4. Redirigimos al inicio con un mensaje de éxito (opcional)
            return redirect()
            
        except Exception as e:
            # En caso de error, deshacemos los cambios
            
            # BD ROLLBACK
            
            return f"Error al guardar: {str(e)}", 500
        
    return render_template("reserva.html")


if __name__ == "__main__":
    app.run(debug=True)