"""Convalida le prove delle affermazioni e genera un rapporto verificabile."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse


def validate(data):
    if not isinstance(data, dict) or not data.get("question"):
        raise ValueError("È obbligatoria una domanda di ricerca")
    sources = data.get("sources", [])
    if not isinstance(sources, list) or not sources:
        raise ValueError("Sono obbligatorie le fonti")
    by_id = {}
    for source in sources:
        if not {"id", "url", "title", "accessed", "kind"} <= source.keys():
            raise ValueError("Fonte incompleta")
        parsed = urlparse(source["url"])
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError("L'URL della fonte deve usare HTTP(S)")
        if source["id"] in by_id:
            raise ValueError("ID della fonte duplicato")
        by_id[source["id"]] = source
    claims = data.get("claims", [])
    if not claims:
        raise ValueError("Sono obbligatorie le affermazioni")
    for claim in claims:
        if not claim.get("text") or claim.get("status") not in {"supported", "uncertain", "conflict"}:
            raise ValueError("Affermazione non valida")
        evidence = claim.get("evidence", [])
        if claim["status"] == "supported" and not evidence:
            raise ValueError("Le affermazioni supportate richiedono prove")
        for item in evidence:
            if item.get("source") not in by_id or not item.get("quote"):
                raise ValueError("La prova richiede una fonte nota e una citazione")
    return by_id


def render(data):
    sources = validate(data)
    lines = ["# " + data["question"], "", "## Risultati e prove", ""]
    for claim in data["claims"]:
        stato = {"supported": "supportata", "uncertain": "incerta", "conflict": "in conflitto"}[claim["status"]]
        lines.extend([f"### {claim['text']}", "", "Stato: " + stato, ""])
        for evidence in claim.get("evidence", []):
            source = sources[evidence["source"]]
            lines.extend([f"> {evidence['quote']}", "", f"Source: [{source['title']}]({source['url']})", ""])
    lines.extend(["## Fonti", ""])
    for source in sources.values():
        lines.append(f"- {source['id']}: [{source['title']}]({source['url']}); {source['kind']}; consultata il {source['accessed']}")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = render(json.loads(args.input.read_text()))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report)
    print(args.output)
