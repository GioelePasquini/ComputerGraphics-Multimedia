# caricare questo file su colab nella cartella input come dataset ed eseguire il blocco note

import flask, logging, ngrok
from flask import request
import subprocess
import jsonify

if __name__ == '__main__':
    ngrok.set_auth_token("2hCAtAEtjMYj0RzyLs4V8lN3QE7_6fg61ry6eQuCWnpeynvSL")  # Replace with your ngrok token
    logging.basicConfig(level=logging.INFO)
    listener = ngrok.werkzeug_develop()
    print(listener.url())
    app = flask.Flask(__name__)


    @app.route("/")
    def hello():
        return "Server pronto: installati tutti i pacchetti richiesti."

    def run_command(image_path):
        command = f"python /kaggle/working/InstantMesh/run.py configs/instant-mesh-base.yaml {image_path} --export_texmap"
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print("ok")
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            print("stderr:", e.stderr)


    @app.route('/generatemodel', methods=['POST'])
    def process():
        data = request.json
        image_path = data['image_path']
        run_command(image_path)

        result = f"Elaborazione completata per {image_path}"

        return jsonify({"result": result})


    '''@app.route("/get-model", methods=["POST"])
    def get_model():
        path = request.form.get('path')
        return path'''



    app.run(debug=True)
