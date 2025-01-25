from flask import Flask, render_template, request
import unicodedata

app = Flask(__name__)

# Diccionario con las enfermedades, causas y recomendaciones  
ENFERMEDADES = {
    "diabetes": {
        "causas": [
            "Alta resistencia a la insulina",
            "Genética",
            "Estilo de vida sedentario",
            "Alimentación poco saludable"
        ],
        "recomendaciones": [
            "Mantener una dieta balanceada",
            "Hacer ejercicio regularmente",
            "Monitorear los niveles de glucosa",
            "Consultar a un endocrinólogo"
        ]
    },
    "hipertension": {
        "causas": [
            "Herencia genética",
            "Estrés crónico",
            "Consumo excesivo de sal",
            "Obesidad"
        ],
        "recomendaciones": [
            "Reducir el consumo de sal",
            "Controlar el estrés",
            "Mantener un peso saludable",
            "Tomar medicamentos antihipertensivos según indicación médica"
        ]
    },
    "gripe": {
        "causas": [
            "Infección viral",
            "Bajo sistema inmunológico",
            "Exposición a temperaturas extremas"
        ],
        "recomendaciones": [
            "Descansar y mantenerse hidratado",
            "Tomar medicamentos para aliviar los síntomas",
            "Evitar el contacto cercano con otras personas"
        ]
    }
}

# Lista de registros de pacientes (esto es solo un ejemplo, puedes almacenarlos en una base de datos)
registros_pacientes = []

# Función para normalizar texto (eliminar tildes y convertir a minúsculas)
def normalizar_texto(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).lower()

# Ruta principal (página de inicio)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar diagnóstico y recomendaciones
@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    # Obtener las enfermedades seleccionadas
    enfermedades_seleccionadas = request.form.getlist('enfermedades')
    diagnosticos = {}
    
    # Obtener diagnóstico para cada enfermedad seleccionada
    for enfermedad in enfermedades_seleccionadas:
        diagnosticos[enfermedad] = ENFERMEDADES.get(enfermedad, None)
    
    return render_template('recomendaciones.html', diagnosticos=diagnosticos)

# Ruta para el registro de pacientes
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        fecha_cita = request.form.get('fecha_cita')

        # Almacenar el registro del paciente en la lista
        registros_pacientes.append({
            "nombre": nombre,
            "apellidos": apellidos,
            "telefono": telefono,
            "direccion": direccion,
            "fecha_cita": fecha_cita
        })

        # Redirigir o mostrar un mensaje de éxito
        return "Registro exitoso"

    return render_template('registro.html')

# Ruta para mostrar todos los registros de pacientes
@app.route('/ver_registros', methods=['GET'])
def ver_registros():
    return render_template('ver_registros.html', registros=registros_pacientes)

if __name__ == "__main__":
    app.run(debug=True)
