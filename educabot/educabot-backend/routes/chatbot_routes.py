<<<<<<< HEAD
=======
from flask import Blueprint, request, jsonify
import openai
import os

chatbot_bp = Blueprint('chatbot_bp', __name__)

@chatbot_bp.route('/chat', methods=['POST'])
def chat_with_gpt():
    try:
        # Capturar datos enviados en la solicitud
        data = request.get_json()
        pregunta = data.get('pregunta', '').strip()

        # Validar si la pregunta está vacía
        if not pregunta:
            return jsonify({'mensaje': 'Por favor, escribe una pregunta válida.'}), 400

        # Llamar a la API de OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil y profesional."},
                {"role": "user", "content": pregunta}
            ],
            max_tokens=100,  # Ajusta según tu necesidad
            temperature=0.7
        )

        # Procesar la respuesta
        respuesta = response['choices'][0]['message']['content'].strip()
        return jsonify({'respuesta': respuesta}), 200

    except openai.error.OpenAIError as oe:
        return jsonify({'mensaje': f'Error en la API de OpenAI: {str(oe)}'}), 500
    except Exception as e:
        return jsonify({'mensaje': f'Error al procesar la solicitud: {str(e)}'}), 500
>>>>>>> parent of 9dbd3cc (avance 4)
