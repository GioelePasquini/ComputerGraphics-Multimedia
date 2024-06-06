# caricare questo file su colab nella cartella input come dataset ed eseguire il blocco note
import flask, logging, ngrok
from flask import request, send_file
import subprocess
import os
import io
import zipfile

if __name__ == '__main__':

    ngrok.set_auth_token("2hCAtAEtjMYj0RzyLs4V8lN3QE7_6fg61ry6eQuCWnpeynvSL")
    logging.basicConfig(level=logging.INFO)
    listener = ngrok.werkzeug_develop()
    print(listener.url())
    app = flask.Flask(__name__)

    # Indice per nominare i diversi file restituiti dal server
    counter = 1

    # Paths
    path_server = "/kaggle/working/output"

    @app.route("/")
    def hello():
        return "Server pronto: installati tutti i pacchetti richiesti."


    def zip_files_in_directory(directory_path):
        zip_data = io.BytesIO()
        with zipfile.ZipFile(zip_data, 'w') as zipf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, directory_path))
        return zip_data

    @app.route('/image_to_model', methods=['POST'])
    def image_to_model():
        global counter, path_server
        data = request.json
        image_path = data['image_path']
        file_name = "model_generated_"+str(counter)
        output_path = path_server+"/InstantMesh/"+file_name
        command = f"python /kaggle/working/InstantMesh/run.py configs/instant-mesh-base.yaml {image_path} --export_texmap --output_path {output_path}"
        try:
            subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print("Modello n. " + str(counter) + " creato e salvato sul server. Ora li invio.")
            zip_stream = zip_files_in_directory(output_path+"/instant-mesh-base/meshes")
            zip_stream.seek(0)
            counter += 1
            return send_file(zip_stream, mimetype='application/zip', download_name='files.zip', as_attachment=True)

        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            print("stderr:", e.stderr)

    @app.route('/text_to_image', methods=['POST'])
    def text_to_image():
        global counter, path_server
        data = request.json
        prompt = data['prompt']
        file_name = "img_generated_"+str(counter)
        output_path = path_server+"/text_to_image/"+file_name
        command = f"python /kaggle/input/text-to-image/text_to_image.py --prompt \"{prompt}\" --output_path {output_path}"
        try:
            subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print("4 immagini relative alla n. " + str(counter) + " create e salvate sul server. Ora le invio.")
            zip_stream = zip_files_in_directory(output_path)
            zip_stream.seek(0)
            counter += 1
            return send_file(zip_stream, mimetype='application/zip', download_name='files.zip', as_attachment=True)

        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            print("stderr:", e.stderr)



    @app.route('/image_to_image', methods=['POST'])
    def image_to_image():
        global counter, path_server
        data = request.json
        prompt = data['prompt']
        input_path = data['input_path']
        file_name = "img_generated_" + str(counter)
        output_path = path_server + "/image_to_image/" + file_name
        command = f"python /kaggle/input/image-to-image/image_to_image.py --prompt \"{prompt}\" --output_path {output_path} --input_path {input_path}"
        try:
            subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            print("4 immagini relative alla n. " + str(counter) + " create e salvate sul server. Ora le invio.")
            zip_stream = zip_files_in_directory(output_path)
            zip_stream.seek(0)
            counter += 1
            return send_file(zip_stream, mimetype='application/zip', download_name='files.zip', as_attachment=True)

        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del comando: {e}")
            print("stderr:", e.stderr)

    app.run(debug=True)
