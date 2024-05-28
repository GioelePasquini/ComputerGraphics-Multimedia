import requests

# URL pubblico generato da ngrok, sostituire ogni volta
url = 'https://ed83-34-16-133-6.ngrok-free.app/prova'

# Percorso dell'immagine da elaborare
image_path = '/content/drive/MyDrive/cute_tiger.jpg'

data = {'image_path': image_path}

response = requests.post(url, json=data)

print(response.json())
