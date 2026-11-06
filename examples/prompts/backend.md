# Backend

Modifica solo `examples/task_manager/main.py`. Inizializza le tabelle tramite il ciclo di vita FastAPI; rifiuta campi sconosciuti e conversioni implicite dei tipi. POST riuscita: 201; PATCH: 200; DELETE: 204; record assenti: 404; input non valido: 422. I campi PATCH omessi conservano il valore corrente; `null` esplicito è rifiutato; la descrizione può essere cancellata. Non modificare i file del ruolo Database.
