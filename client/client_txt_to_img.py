import zipfile
import io
import requests
import os

# URL del server
url = 'https://79d1-34-151-86-131.ngrok-free.app/text_to_image'

response = requests.post(url, json={'prompt':"blue pickachu"})

if response.status_code == 200:
    zip_content = io.BytesIO(response.content)

    # DECIDERE BENE output_directory QUANDO INTEGRIAMO
    output_directory = r"C:\Users\gioel\PycharmProjects\CG&M\output\text_to_image"
    os.makedirs(output_directory, exist_ok=True)

    with zipfile.ZipFile(zip_content, 'r') as zf:
        zf.extractall(output_directory)

    print(f"Files saved successfully in '{output_directory}'")
else:
    print("Errore:", response.status_code, response.text)