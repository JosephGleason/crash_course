#!/usr/bin/python3
glossary = {
    'variable': 'A name that refers to a value.',
    'loop': 'A way to repeat a block of code.',
    'function': 'A named block of code that performs a task.',
    'dictionary': 'A collection of key-value pairs.',
    'list': 'An ordered collection of items.'
}

for word, definition in glossary.items():
    print(f"{word.title()}:\n  {definition}\n")
