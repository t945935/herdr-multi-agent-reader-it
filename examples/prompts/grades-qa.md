# QA: sistema di valutazione

Leggi l’interfaccia di `examples/grades.py` e i casi esistenti in `tests/test_contracts.py`. Verifica indipendentemente il contratto. Non modificare il codice, non eliminare test, non leggere l’autovalutazione del Developer e non avviare altri agenti.

Puoi aggiungere o modificare solo `tests/test_grades_review.py`; salva il rapporto in `reports/grade-qa.md`. Verifica materie richieste, limiti 0/100/60, booleani/NaN/stringhe, dati vuoti, nomi, parità 1/1/3, precisione non arrotondata e immutabilità dell’input.

Usa pytest. Se i test esistenti coprono già adeguatamente un caso, spiega il criterio e aggiungi solo copertura utile; non duplicare test identici. Non testare FastAPI, SQLite o CRUD del sito: questa attività riguarda i voti.

Esegui i test e conserva comando reale, codice d’uscita, rilievi e controlli non eseguiti. Usa `task_id` e `completion_path` aggiunti dal Manager nella ricevuta; elenca in `artifacts` il rapporto e i file di test creati.
