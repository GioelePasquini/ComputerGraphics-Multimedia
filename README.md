1) Aprire con colab il file ponte-server.ipynb
2) Nella sezione input di kaggle inserire il file image_to_image.py in /kaggle/input/image-to-image
3) Nella sezione input di kaggle inserire il file text_to_image.py in /kaggle/input/text-to-image
4) Nella sezione input di kaggle inserire il file server.py in /kaggle/input/server
5) Nella sezione accelerator, attivare la GPU
6) Runnare tutte le celle di ponte-server.ipynb
7) Andare su ide e runnare i diversi client in base a ciò che si vuoe fare (text-to-image, image-to-image o image-to-model)
   N.B. Prendere l'url stampato sul blocco onte del ponte-server e aggiornare le variabili "url" presenti nei diversi client.
   N.B. Bisogna capire bene come aggiustare i path di salvataggio in locale lato client.
