#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Return True if obj is instance of a subclass of a_class (not a_class itself)."""
    return isinstance(obj, a_class) and type(obj) != a_class
