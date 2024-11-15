from flask import Flask, request, jsonify, render_template
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import json

app = Flask(__name__)

# Carga el modelo y el tokenizador de Hugging Face
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Carga la base de conocimientos desde un archivo JSON
with open('knowledge_base.json', 'r', encoding='utf-8') as kb_file:
    knowledge_base = json.load(kb_file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message").strip()
    inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_new_tokens=50,  # Limita la cantidad de nuevos tokens generados
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.5,  # Reduce la creatividad para respuestas más precisas
        top_k=50,        # Controla la diversidad
        top_p=0.9,       # Controla la diversidad
        do_sample=True   # Habilitar el muestreo
    )
    
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    
    # Integrar la lógica para usar la base de conocimientos
    for item in knowledge_base:
        if item['pregunta'].lower() in user_input.lower():
            response = item['respuesta']
            break

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)