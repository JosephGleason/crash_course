#!/usr/bin/python3
glossary = {
    'variable': 'A name that refers to a value.',
    'loop': 'A way to repeat a block of code.',
    'function': 'A named block of code that performs a task.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'An ordered collection of items.',
    'tuple': 'An immutable sequence of items.',
    'set': 'An unordered collection of unique items.',
    'key': 'The name used to look up a value in a dictionary.',
    'value': 'The data associated with a dictionary key.',
    'method': 'A function that is associated with an object.',
}

for word, definition in glossary.items():
    print(f"{word.title()}:\n  {definition}\n")
