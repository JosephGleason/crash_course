#!/usr/bin/python3
# alien_color = 'green'
alien_color = 'red'
# alien_color = 'yellow'

if alien_color == 'green':
    print(f'Player earned 5 points for shooting the alien.')
elif alien_color == 'yellow':
    print(f'Player earned 10 points.')
elif alien_color == 'red':
    print(f'Player earned 15 points.')
else:
    print(f'Player earned 10 points.')
