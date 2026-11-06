"""Contratto condiviso; la graduatoria usa totali non arrotondati."""

from collections.abc import Mapping
from math import isfinite

SUBJECTS = frozenset({"Italiano", "Storia", "Matematica"})


def validate_scores(scores):
    if not isinstance(scores, Mapping) or set(scores) != SUBJECTS:
        raise ValueError("I voti devono includere esattamente Italiano, Storia e Matematica")
    for value in scores.values():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError("I voti devono essere numerici e non booleani")
        if not isfinite(value) or not 0 <= value <= 100:
            raise ValueError("I voti devono essere finiti e compresi tra 0 e 100")
    return scores


def calculate_total(scores):
    return sum(validate_scores(scores).values())


def calculate_average(scores):
    return calculate_total(scores) / 3


def get_grade(average):
    if isinstance(average, bool) or not isinstance(average, (int, float)):
        raise ValueError("La media deve essere numerica")
    if not isfinite(average) or not 0 <= average <= 100:
        raise ValueError("La media deve essere compresa tra 0 e 100")
    return "Sufficiente" if average >= 60 else "Insufficiente"


def rank_students(students):
    if not isinstance(students, list):
        raise ValueError("Gli studenti devono essere forniti come lista")
    rows = []
    for student in students:
        if not isinstance(student, Mapping):
            raise ValueError("Ogni studente deve essere un oggetto")
        name = student.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Il nome dello studente è obbligatorio")
        total = calculate_total(student.get("scores"))
        average = total / 3
        rows.append({"name": name.strip(), "scores": dict(student["scores"]),
                     "total": total, "average": average, "grade": get_grade(average)})
    rows.sort(key=lambda row: row["total"], reverse=True)
    previous = None
    rank = 0
    for index, row in enumerate(rows, 1):
        if previous is None or row["total"] != previous:
            rank = index
        previous = row["total"]
        row["rank"] = rank
    return rows
