"""Capitolo iniziale: contratto essenziale per esercizi di sviluppo e revisione."""

from math import isfinite


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Era atteso un numero, escluso il tipo bool")
    if not isfinite(value):
        raise ValueError("Era atteso un numero finito")
    return value


def add(a, b):
    return _number(a) + _number(b)


def subtract(a, b):
    return _number(a) - _number(b)


def multiply(a, b):
    return _number(a) * _number(b)


def divide(a, b):
    a, b = _number(a), _number(b)
    if b == 0:
        raise ZeroDivisionError("Non è possibile dividere per zero")
    return a / b
