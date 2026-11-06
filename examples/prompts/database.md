# Database

Modifica solo `examples/task_manager/db.py`. Fornisci `init_db`, `get_tasks`, `get_task`, `create_task`, `update_task` e `delete_task`. I test possono sostituire `DB_PATH`; chiudi sempre le connessioni, usa transazioni per le scritture e parametri nei valori SQL. Genera i nomi di colonna dinamici solo da una lista consentita fissa. Restituisci `None`/`False` per record assenti; non nascondere eccezioni del database fingendo di avere una lista vuota.
