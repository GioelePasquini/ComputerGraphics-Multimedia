# Link per scaricare la video demo di funzionamento

https://univpm-my.sharepoint.com/:v:/g/personal/s1113511_studenti_univpm_it/EXDxyr-QdyxFstMgzRZ9GC4BnM_B1bjFWHnzo8G_tg8ozw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=NmiuDZ


# Link per scaricare il progetto

https://univpm-my.sharepoint.com/:u:/g/personal/s1113511_studenti_univpm_it/EaMUnyxAp5pDlNp5J9bTRjsB-LMY5vrpGCtrlS-9rqP-JQ?e=LzNiHR


# Configurazione del server per l'applicazione
1. Importare il file "ponte kaggle-server.ipynb" su kaggle e selezionare come accelleratore GPU P100
2. Nel file server.py inserire il proprio authtoken di ngrok
3. Negli input del server inserire 3 dataset:
   + "server", con al suo interno il file server.py
   + "image-to-image", con al suo interno il file image_to_image.py
   + "text-to-image", con al suo intterno il file text_to_image.py
   + Il risultato nella sezione input di kaggle è il seguente:
<p align="center">
   <img width="418" alt="Immagine input" src="https://github.com/GioelePasquini/ComputerGraphics-Multimedia/assets/75083105/ca880a58-252c-488f-89bc-f13fc13db596">
</p>
4. Avviare il blocco note eseguendo tutte le celle, quando verrà eseguita l'ultima cella verrà stampato l'Url pubblico per il server da utilizzare nell'applicazione per effettuare le richieste. <br>
5. Inserire l'Url pubblico in Unity, più precisamente all'interno della scena, nel GameObject SchermoInferiore, nello script ServerRequests, all'interno dell'attributo Server Url.

<b> NB.: Il server su kaggle può gestire solo una richiesta alla volta. </b>

# Utilizzo dell'applicazione
Allo spawn, il giocatore si troverà dinanzi a due schermi che utilizzerà per interagire con l'applicazione. Lo schermo in alto verrà utilizzato per visualizzare le immagini che l'utente genererà, lo schermo in basso verrà invece utilizzato per scrivere i prompt e inviare i comandi. <br>
Lo schermo in basso è diviso orizzontalmente in 3 sezioni:
+ In quella di sinistra sono presenti dei bottoni per interagire con la tastiera virtuale di Oculus, in particolare per mostrarla, nasconderla, muoverla e per rimuovere il testo inserito fino a quel momento.
+ Nella parte centrale è presente un campo di input dove l'utente, tramite la tastiera, inserirà i suoi prompt.
+ Nella parte di destra sono presenti i bottoni per inviare le richieste di generazione al server.
<br>
L'utente può interagire con i modelli di AI generativa in 3 modi: <br>
1. Text-to-image <br>
2. Image-to-image <br>
3. Image-to-3D <br>

## Text to image
Per generare delle immagini l'utente dovrà inserire un prompt e successivamente premere il bottone "Generate Images". Apparirà una schermata di caricamento delle immagini. Il server genererà 4 immagini con il prompt inserito che, al termine della generazione, verranno visualizzate nello schermo superiore. <br>
Questa richiesta impiega circa 1 minuto per essere completata.

## Image to image
Per modificare una delle immagini che sono state generate, l'utente dovrà selezionarla nello schermo superiore, inserire il prompt con il quale intende modificare le immagini e, successivamente, premere il pulsante "Modify Images". Apparirà una finestra di caricamento. Verranno create 4 immagini a partire da quella selezionata e secondo il prompt inserito; al termine della loro generazione verranno visualizzate nello schermo superiore. <br/>
Questa richiesta impiega circa 1 minuto per essere completata.

## Image to 3D
Per generare un modello 3D a partire da un'immagine, l'utente dovrà selezionare l'immagine desiderata dallo schermo superiore e poi premere il bottone "Generate Model". Al termine della generazione il modello apparirà sopra il cilindro nero sul pavimento, a sinistra dell'utente rispetto alla posizione di spawn. <br>
Questa richiesta impiega, indicativamente, tra i 3 e i 4 minuti per essere completata.
### Tips per la generazione di modelli
Per renderepiù veloce ed efficace la generazione di un modello, cerca si selezionare una immagine di partenza in cui l'oggetto sia in primo piano, centrato nell'immagine e con uno sfondo relativamente semplice.

## Interazione con i modelli
Una volta generato un modello 3D, l'utente potrà:
+ Spostarlo e ruotarlo tramite grab.
+ Scalarlo tramite grab con due mani.
+ Duplicarlo premento il tasto <b> X </b> sul controller sinistro mentre il modello è in stato di grab.
+ Eliminarlo premento il tasto <b> Y </b> sul controller sinistro mentre il modello è in stato di grab.

