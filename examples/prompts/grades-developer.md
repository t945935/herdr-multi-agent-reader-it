# Developer: contratto di valutazione

Leggi prima i casi di valutazione in `examples/grades.py` e `tests/test_contracts.py`. Modifica solo `examples/grades.py`; non cambiare test esistenti o codice del sito e non avviare altri agenti.

Contratto: esattamente tre materie, Italiano, Storia e Matematica. I voti sono `int`/`float` finiti; rifiuta booleani, stringhe, materie mancanti o aggiuntive e valori fuori da 0–100. La media 60 è sufficiente. Una lista studenti vuota restituisce una lista vuota. Ordina per totale non arrotondato con graduatoria agonistica e conserva l’ordine d’ingresso a parità; non modificare l’input.

Mantieni le interfacce `calculate_total`, `calculate_average`, `get_grade` e `rank_students`. Verifica il contratto e correggi solo se necessario. Se è già rispettato, conserva l’implementazione e riferisci i controlli invece di riscriverla per creare differenze.

Esegui `.venv/bin/python -m pytest -q tests/test_contracts.py -k 'ranking or scores'`. Registra comando effettivo, codice d’uscita, file modificati e punti irrisolti in `reports/grade-developer.md`. Usa `task_id` e `completion_path` aggiunti dal Manager per la ricevuta.
