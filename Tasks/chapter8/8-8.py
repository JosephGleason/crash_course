#!/usr/bin/python3
def make_album(name, album, song='', tracks=''):
    music = {'artist': name.title(), 'title': album.title()}
    if song:
        music['songs'] = song
    if tracks:
        music['tracks'] = tracks
    return music
while True:
    artist_input = input("Enter artist name (or 'q' to quit): ")
    if artist_input == 'q':
        break
    album_input = input("Enter album name (or 'q' to quit): ")
    if album_input == 'q':
        break
    
    song_input = input("Enter song name (optional): ")
    tracks_input = input("Enter track count (optional): ")

    # convert track input to integer if it's a number
    if tracks_input.isdigit():
        tracks_input = int(tracks_input)
    else:
        tracks_input = ''

    album = make_album(artist_input, album_input, song=song_input, tracks=tracks_input)
    print(f"\nAlbum created: {album}\n")
