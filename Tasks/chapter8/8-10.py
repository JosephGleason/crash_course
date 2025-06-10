#!/usr/bin/python3
magicians = ['Helbert', 'Domekan', 'Elkasor']

def make_great(magicians):
   for i in range(len(magicians)):
        magicians[i] = magicians[i]  + " The Great"
        
def show_magicians(magicians):
    for name in magicians:
        print(f"{name.title()}")
 
make_great(magicians)
show_magicians(magicians)
