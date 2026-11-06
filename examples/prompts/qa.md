# QA

Modifica solo `tests/`. I test devono rispettare i requisiti, non indebolirli per passare. Isola SQLite con `tmp_path` e avvia `TestClient` tramite il ciclo di vita dell’applicazione. Copri CRUD, tipi, valori nulli, campi sconosciuti, record mancanti e persistenza dopo il riavvio. Esegui i test e registra comando, versione, codice d’uscita e riepilogo dei fallimenti.
