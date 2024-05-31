from io import BytesIO

import requests
from PIL import Image
# URL pubblico generato da ngrok, sostituire ogni volta
url = 'https://b262-35-231-235-110.ngrok-free.app/generatemodel'

# Percorso dell'immagine da elaborare
image_path = '/kaggle/working/InstantMesh/examples/house2.jpg'
#prompt = "cowboy with a white hat"
#data = {'image_path': image_path}
data = {'image_path': image_path}

response = requests.post(url, json={'image_path': image_path})

if response.status_code == 200:
    print((response.json()))
    # Crea un oggetto Image da PIL
    #img = Image.open(BytesIO(response.content))
    # Visualizza l'immagine
    #img.show()
else:
    print(f"Failed to retrieve image. Status code: {response.status_code}")