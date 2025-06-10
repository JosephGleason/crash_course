#!/usr/bin/python3
def make_album(name, album, song='', tracks=''):
    music = {'artist': name.title(), 'title': album.title()}
    if song:
        music['songs'] = song
    if tracks:
        music['tracks'] = tracks
    return music
album1 = make_album('Creed', 'TheInnerLight', 'Higher', 12)
album2 = make_album('Muse', 'Origin of Symmetry')
album3 = make_album('Linkin Park', 'Meteora', 'Numb', 10)
print(album1)
print(album2)
print(album3)
