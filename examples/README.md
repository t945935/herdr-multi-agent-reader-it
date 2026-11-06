# Pacchetto eseguibile per lettori

Esegui ogni comando dalla radice del progetto estratto. Importa i moduli tramite `examples.*`.

I prompt per il sistema di valutazione sono `prompts/grades-developer.md` e `prompts/grades-qa.md`; `prompts/qa.md` è specifico per il sito. Assegna il lavoro in una tua copia d’esercizio per preservare la versione di riferimento.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
.venv/bin/python -m examples.pipeline
```

| Capitolo | Punto d’ingresso | Aspetto dell’accettazione |
| --- | --- | --- |
| 1 | `calculator.py` | Aritmetica, divisione per zero e tipi |
| 2 | `grades.py` | Limiti dei voti, materie mancanti e parità |
| 3 | `../scripts/probe_herdr.py --live` | Avvio, lettura, attesa e pulizia di un riquadro shell |
| 4 | `../scripts/team.py` | Assegnazioni per fasi, ID univoci e accettazione degli artefatti |
| 5 | `prompts/reviewer-a.md`, `reviewer-b.md` | Revisioni indipendenti e decisione del Manager |
| 6 | `handoff.py` | Esistenza dei file, ambito del progetto e SHA-256 |
| 7 | `task_manager/` | CRUD, convalida, pagine statiche, persistenza dopo il riavvio |
| 8 | `research.py` | Affermazioni, fonti, citazioni e incertezza |
| 9 | `pipeline.py` | Codici d’uscita, timeout, accettazione e arresto al fallimento |
| 10 | `queue.py` | Deduplicazione, lease, recupero, lettere morte e concorrenza |

Avvia il sito:

```bash
.venv/bin/python -m uvicorn examples.task_manager.main:app --host 0.0.0.0 --port 8000
```

Con WSL apri `http://localhost:8000/` in un browser Windows. I dati d’esempio sono salvati per impostazione predefinita in `examples/data/tasks.db`; i test automatici usano una directory temporanea senza toccare quel database.

La coda in background è un esempio finito di calcolo puro e non chiama modelli a pagamento. L’assegnazione effettiva a un modello è esplicita in `scripts/team.py`; prima installa e autentica la CLI pertinente.
