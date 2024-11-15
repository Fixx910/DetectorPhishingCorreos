from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa CORS

import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

# Habilitar CORS para todas las rutas
CORS(app)

# Cargar los modelos entrenados
clf_text = joblib.load('modelo_phishing_texto.pkl')
clf_link = joblib.load('modelo_phishing_enlaces.pkl')
vectorizer = joblib.load('vectorizer.pkl')


@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    try:
        data = request.json  # Obtener los datos JSON de la solicitud
        print(data)  # Ver los datos recibidos
        email_content = data['text']  # Acceder a la clave 'text' en lugar de 'email_content'
        
        # Lógica de detección de spam (simplificada)
        result = "¡Cuidado es phishing!" if "free" in email_content.lower() else "¡Correo seguro!"
        
        return jsonify({"result": result})  # Enviar la respuesta como JSON
    
    except KeyError:
        # Si falta la clave 'text', se maneja el error
        return jsonify({"error": "Missing 'text' in the request"}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
