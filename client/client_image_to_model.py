import os
import requests
import zipfile
import io
# URL pubblico generato da ngrok, sostituire ogni volta
url = 'https://79d1-34-151-86-131.ngrok-free.app/image_to_model'

# Percorso dell'immagine da elaborare
image_path = "/kaggle/working/output/image_to_image/img_generated_3/image_3.png"
file_name = os.path.splitext(os.path.basename(image_path))[0]
response = requests.post(url, json={'image_path': image_path}, verify=True)

if response.status_code == 200:
    # Leggi il contenuto del file ZIP direttamente dalla risposta
    zip_content = io.BytesIO(response.content)

    # DECIDERE BENE output_directory QUANDO INTEGRIAMO
    output_directory = r"C:\Users\gioel\PycharmProjects\CG&M\output\image_to_model\prova"
    os.makedirs(output_directory, exist_ok=True)

    with zipfile.ZipFile(zip_content, 'r') as zf:
        zf.extractall(output_directory)

    print(f"Files saved successfully in '{output_directory}'")
else:
    print("Errore:", response.status_code, response.text)

