# Pacchetto di accompagnamento per lettori — Herdr

Versione delle risorse: 1.0.0

Questo pacchetto contiene esempi eseguibili, test, prompt e istruzioni brevi per *Orchestrare agenti di IA con Herdr*. Non include il testo a pagamento del libro.

## Installazione e test

Usa Python 3.12 dalla radice del repository:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest -q tests
```

Risultato previsto: 42 test superati. Il progetto accompagna gli esempi del libro; non viene concessa una licenza open source generale.

Consulta [`examples/README.md`](examples/README.md) per la corrispondenza con i capitoli, l’avvio del sito e le indicazioni per gli esercizi. [`CHANGELOG.md`](CHANGELOG.md) riporta la cronologia delle release.
