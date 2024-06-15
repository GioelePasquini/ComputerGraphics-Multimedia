# Configurazione del server per l'applicazione
1. Importare il file server-funzionante.ipynb su kaggle e selezionare come accelleratore GPU P100
2. Nel file server.py inserire il proprio authtoken di ngrok
3. Negli input del server inserire 3 dataset:
   + "server", con al suo interno il file server.py
   + "image-to-image", con al suo interno il file image_to_image.py
   + "text-to-image", con al suo intterno il file text_to_image.py
   + Il risultato nella sezione input di kaggle è il seguente:
<p align="center">
   <img width="418" alt="Immagine input" src="https://github.com/GioelePasquini/ComputerGraphics-Multimedia/assets/75083105/ca880a58-252c-488f-89bc-f13fc13db596">
</p>
4. Avviare il blocco note eseguendo tutte le celle, quando verrà eseguita l'ultima cella verrà stampato l'Url pubblico per il server da utilizzare nell'applicazione per effettuare le richieste
5. Inserire l'Url pubblico in Unity, più precisamente all'interno della scena, nel GameObject SchermoInferiore, nello script ServerRequests, all'interno dell'attributo Server Url.


