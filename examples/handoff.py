"""Convalida una registrazione esplicita di passaggio, non un'affermazione dell'agente."""

import argparse
import hashlib
import json
from pathlib import Path


def validate(record, root):
    required = {"task_id", "from", "to", "completed", "next", "artifacts"}
    if not isinstance(record, dict) or not required <= record.keys():
        raise ValueError("Mancano campi obbligatori nel passaggio")
    if any(not isinstance(record[key], str) or not record[key].strip()
           for key in ["task_id", "from", "to", "completed", "next"]):
        raise ValueError("I campi testuali del passaggio non possono essere vuoti")
    if not isinstance(record["artifacts"], list) or not record["artifacts"]:
        raise ValueError("Il passaggio deve includere artefatti")
    root = Path(root).resolve()
    for artifact in record["artifacts"]:
        if not isinstance(artifact, dict) or set(artifact) != {"path", "sha256"}:
            raise ValueError("Ogni artefatto deve includere percorso e sha256")
        path = (root / artifact["path"]).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError("Il percorso dell'artefatto deve indicare un file nel progetto")
        if hashlib.sha256(path.read_bytes()).hexdigest() != artifact["sha256"]:
            raise ValueError("L'hash dell'artefatto non corrisponde")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    validate(json.loads(args.record.read_text()), args.root)
    print("Passaggio accettato")
