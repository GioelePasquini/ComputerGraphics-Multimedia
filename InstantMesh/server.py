from flask import Flask, request, jsonify
from pyngrok import ngrok
import subprocess


# Configura l'authtoken di ngrok
ngrok.set_auth_token("2h5rieBL9lrpCOaSIc5Xhwovj74_69Cz6hV2bKKSuJnBW6uQU")

app = Flask(__name__)


@app.route('/')
def home():
    return "Server Flask su Colab è attivo."




def run_command(image_path):
    command = f"python run.py configs/instant-mesh-base.yaml {image_path} --export_texmap"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("ok")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        print("stderr:", e.stderr)

@app.route('/prova', methods=['POST'])
def process():
    data = request.json
    image_path = data['image_path']
    run_command(image_path)

    result = f"Elaborazione completata per {image_path}"

    return jsonify({"result": result})


# Avviare il server Flask
port = 5000
public_url = ngrok.connect(port).public_url
print(f"Server pubblico URL: {public_url}")
app.run(port=port, debug=True)
'''
import subprocess

def run_command(image_path):
    command = f"python run.py configs/instant-mesh-base.yaml {image_path}"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        print("ok")
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del comando: {e}")
        print("stderr:", e.stderr)

run_command('/content/InstantMesh/examples/house3.jpg')
'''