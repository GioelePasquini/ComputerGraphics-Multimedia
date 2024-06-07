using System;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;
using System.Collections;
using System.IO;
using System.IO.Compression;
using System.Text;
using System.Runtime.Serialization.Json;

public class ServerRequests : MonoBehaviour
{
    // Classe per il JSON da inserire nella richiesta al server
    public class JsonData
    {
        public string prompt = "";
        public string image_path = "";
    }
    
    // Link del server
    [SerializeField] private string serverUrl = "https://81ed-34-116-95-1.ngrok-free.app/";
    
    // Prompt per il testo da inviare al server, questo prompt andrà collegato al text field presente
    // nell'interfaccia grafica
    [SerializeField] private string prompt = "";
    
    // Path della immagine sul server con cui lavorare, va ricavata dall'immagine che l'utente ha 
    // selezionato nell'interfaccia grafica
    [SerializeField] private string image_path = "";
    
    /*
     * Percorso in cui salvare i file decompressi.
     * In Unity, il percorso di salvataggio è relativo alla cartella "Assets" del progetto.
     * Nella cartella ServerOutputs verranno salvati i file decompressi, dividendoli in 3 sotto-cartelle
     * in base al tipo di richiesta con i quali sono stati ottenuti (txt2img, img2img o img2mdl).
     */
    [SerializeField] private string savePath = "Assets/ServerOutputs";
    

    
    // Funzione da collegare al bottone di txt2img
    public void OnTxt2ImgClick()
    {
        // Avvia la coroutine per inviare la richiesta POST
        StartCoroutine(SendTxt2ImgRequest());
    }
    
    // Funzione da collegare al bottone di img2img
    public void OnImg2ImgClick()
    {
        // Avvia la coroutine per inviare la richiesta POST
        StartCoroutine(SendImg2ImgRequest());
    }
    
    // Funzione da collegare al bottone di img2mdl
    public void OnImg2MdlClick()
    {
        // Avvia la coroutine per inviare la richiesta POST
        StartCoroutine(SendImg2MdlRequest());
    }

    // Routine per inviare la richiesta txt2img al server
    IEnumerator SendTxt2ImgRequest()
    {
        // Crea il payload JSON
        JsonData jsonData = new JsonData
        {
            prompt = prompt,
            image_path = image_path
        };
        string json = JsonUtility.ToJson(jsonData);
        byte[] jsonToSend = new UTF8Encoding().GetBytes(json);
        // Configura la richiesta POST
        string urlRequest = serverUrl + "text_to_image";
        UnityWebRequest www = new UnityWebRequest(urlRequest, "POST");
        www.uploadHandler = new UploadHandlerRaw(jsonToSend);
        www.downloadHandler = new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        Debug.Log("Richiesta txt2img inviata al server");
        yield return www.SendWebRequest();

        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("Errore nella richiesta: " + www.error);
        }
        else
        {
            string path = savePath + "/txt2img";
            // Gestione della risposta
            byte[] responseData = www.downloadHandler.data;

            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }

            using (MemoryStream zipStream = new MemoryStream(responseData))
            {
                using (ZipArchive archive = new ZipArchive(zipStream))
                {
                    foreach (ZipArchiveEntry entry in archive.Entries)
                    {
                        string filePath = Path.Combine(path, entry.FullName);
                        string directoryPath = Path.GetDirectoryName(filePath);

                        if (!Directory.Exists(directoryPath))
                        {
                            Directory.CreateDirectory(directoryPath);
                        }

                        if (entry.Name != "")
                        {
                            entry.ExtractToFile(filePath, true);
                        }
                    }
                }
            }
            Debug.Log("File decompressi correttamente in: " + path);

            // Aggiorna l'AssetDatabase per riflettere i nuovi file aggiunti (solo nell'editor)
            #if UNITY_EDITOR
            UnityEditor.AssetDatabase.Refresh();
            #endif
        }
    }
    
    // Routine per inviare la richiesta img2img al server
    IEnumerator SendImg2ImgRequest()
    {
        // Crea il payload JSON
        JsonData jsonData = new JsonData
        {
            prompt = prompt,
            image_path = image_path
        };
        string json = JsonUtility.ToJson(jsonData);
        byte[] jsonToSend = new UTF8Encoding().GetBytes(json);
        // Configura la richiesta POST
        string urlRequest = serverUrl + "image_to_image";
        UnityWebRequest www = new UnityWebRequest(urlRequest, "POST");
        www.uploadHandler = new UploadHandlerRaw(jsonToSend);
        www.downloadHandler = new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        Debug.Log("Richiesta img2img inviata al server");
        yield return www.SendWebRequest();

        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("Errore nella richiesta: " + www.error);
        }
        else
        {
            string path = savePath + "/img2img";
            // Gestione della risposta
            byte[] responseData = www.downloadHandler.data;

            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }

            using (MemoryStream zipStream = new MemoryStream(responseData))
            {
                using (ZipArchive archive = new ZipArchive(zipStream))
                {
                    foreach (ZipArchiveEntry entry in archive.Entries)
                    {
                        string filePath = Path.Combine(path, entry.FullName);
                        string directoryPath = Path.GetDirectoryName(filePath);

                        if (!Directory.Exists(directoryPath))
                        {
                            Directory.CreateDirectory(directoryPath);
                        }

                        if (entry.Name != "")
                        {
                            entry.ExtractToFile(filePath, true);
                        }
                    }
                }
            }
            Debug.Log("File decompressi correttamente in: " + path);

            // Aggiorna l'AssetDatabase per riflettere i nuovi file aggiunti (solo nell'editor)
            #if UNITY_EDITOR
            UnityEditor.AssetDatabase.Refresh();
            #endif
        }
    }
    
    // Routine per inviare la richiesta img2mdl al server
    IEnumerator SendImg2MdlRequest()
    {
        // Crea il payload JSON
        JsonData jsonData = new JsonData
        {
            prompt = prompt,
            image_path = image_path
        };
        string json = JsonUtility.ToJson(jsonData);
        byte[] jsonToSend = new UTF8Encoding().GetBytes(json);
        // Configura la richiesta POST
        string urlRequest = serverUrl + "image_to_model";
        UnityWebRequest www = new UnityWebRequest(urlRequest, "POST");
        www.uploadHandler = new UploadHandlerRaw(jsonToSend);
        www.downloadHandler = new DownloadHandlerBuffer();
        www.SetRequestHeader("Content-Type", "application/json");
        Debug.Log("Richiesta img2mdl inviata al server");
        yield return www.SendWebRequest();

        if (www.result == UnityWebRequest.Result.ConnectionError || www.result == UnityWebRequest.Result.ProtocolError)
        {
            Debug.LogError("Errore nella richiesta: " + www.error);
        }
        else
        {
            string path = savePath + "/img2mdl";
            // Gestione della risposta
            byte[] responseData = www.downloadHandler.data;

            if (!Directory.Exists(path))
            {
                Directory.CreateDirectory(path);
            }

            using (MemoryStream zipStream = new MemoryStream(responseData))
            {
                using (ZipArchive archive = new ZipArchive(zipStream))
                {
                    foreach (ZipArchiveEntry entry in archive.Entries)
                    {
                        string filePath = Path.Combine(path, entry.FullName);
                        string directoryPath = Path.GetDirectoryName(filePath);

                        if (!Directory.Exists(directoryPath))
                        {
                            Directory.CreateDirectory(directoryPath);
                        }

                        if (entry.Name != "")
                        {
                            entry.ExtractToFile(filePath, true);
                        }
                    }
                }
            }
            Debug.Log("File decompressi correttamente in: " + path);

            // Aggiorna l'AssetDatabase per riflettere i nuovi file aggiunti (solo nell'editor)
            #if UNITY_EDITOR
            UnityEditor.AssetDatabase.Refresh();
            #endif
        }
    }
}
