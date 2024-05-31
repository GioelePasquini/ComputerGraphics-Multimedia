from io import BytesIO

import requests
from PIL import Image
# URL pubblico generato da ngrok, sostituire ogni volta
url = 'https://e04d-34-83-243-250.ngrok-free.app/mao'

# Percorso dell'immagine da elaborare
image_path = '/content/drive/MyDrive/cute_tiger.jpg'
prompt = "cowboy with a white hat"
#data = {'image_path': image_path}
data = {'prompt': prompt}

response = requests.post(url, json={'prompt': prompt})

if response.status_code == 200:
    # Crea un oggetto Image da PIL
    img = Image.open(BytesIO(response.content))
    # Visualizza l'immagine
    img.show()
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")