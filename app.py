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
    enfermedad = normalizar_texto(request.form.get('enfermedad').strip())
    diagnostico = ENFERMEDADES.get(enfermedad, None)
    return render_template('recomendaciones.html', enfermedad=enfermedad, diagnostico=diagnostico)

if __name__ == "__main__":
    app.run(debug=True)
