# Manager: integrazione e accettazione

Definisci requisiti, interfacce e proprietà dei file per ogni ruolo. Completa il contratto prima delle assegnazioni parallele; includi parametri e valori restituiti di backend/database e confini transazionali.

Crea un `task_id` univoco per ogni attività. Prima di inviare un prompt, controlla lo stato della CLI. Se l’agente è bloccato o scade il timeout, leggi stato e output e accertati che il prompt sia stato consegnato; non reinviarlo alla cieca. `idle` e `done` non significano che una consegna abbia superato l’accettazione.

Raccogli artefatti, test e due revisioni indipendenti. Accetta i rilievi sulla base delle prove. Restituisci i problemi al proprietario originario del file; non modificare lo stesso codice mentre lavora il Developer. Dopo i nuovi test, produci un rapporto finale indicando il lavoro ancora incompleto.
