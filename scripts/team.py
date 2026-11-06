#!/usr/bin/env python3
"""Assegna lavoro a un agente inattivo già avviato e verifica la ricevuta dedicata."""
import argparse
import json
import os
import subprocess
import uuid
from pathlib import Path


def call(*args, timeout=310):
    done = subprocess.run(["herdr", *args], text=True, capture_output=True, timeout=timeout)
    if done.returncode:
        raise RuntimeError(done.stderr or done.stdout)
    return json.loads(done.stdout)["result"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("HERDR_ENV") != "1":
        raise SystemExit("Esegui il comando in un terminale gestito da Herdr")
    agent = call("agent", "get", args.target)["agent"]
    if agent["agent_status"] not in {"idle", "done"}:
        raise SystemExit("L'agente deve essere inattivo o aver terminato prima dell'assegnazione")
    path = args.output.resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit("Scegli un nuovo percorso per la ricevuta; non riutilizzare un'attività precedente")
    task_id = uuid.uuid4().hex
    prompt = args.prompt.read_text() + (
        f"\n\nQuesto task_id={task_id}\ncompletion_path={path}\n"
        'Completa il compito reale, poi scrivi JSON: {"task_id":"l’identificatore sopra","status":"completed",'
        '"summary":"consegne specifiche e verifiche","artifacts":["percorsi effettivi degli artefatti"]}. '
        "Se non puoi completare il compito, usa status=blocked e spiega il motivo nel riepilogo. Non avviare altri agenti."
    )
    settled = call("agent", "prompt", args.target, prompt, "--wait", "--timeout", "300000")
    state = settled["agent"]["agent_status"]
    if state not in {"idle", "done"} or not path.is_file():
        raise SystemExit("L'agente si è fermato senza una ricevuta accettabile; controlla agent get/read")
    receipt = json.loads(path.read_text())
    if receipt.get("task_id") != task_id or receipt.get("status") != "completed" or not receipt.get("summary"):
        raise SystemExit("La ricevuta non attesta il completamento di questa attività")
    for artifact in receipt.get("artifacts", []):
        candidate = Path(artifact)
        if not candidate.is_absolute():
            candidate = Path.cwd() / candidate
        if not candidate.is_file():
            raise SystemExit(f"Artefatto mancante: {artifact}")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
