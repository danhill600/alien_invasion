#8-7. Album: Write a function called make_album() that builds a dictionary
#describing a music album. The function should take in an artist name and an
#album title, and it should return a dictionary containing these two pieces of
#information. Use the function to make three dictionaries representing different
#albums. Print each return value to show that the dictionaries are storing the
#album information correctly.
#Add an optional parameter to make_album() that allows you to store the
#number of tracks on an album. If the calling line includes a value for the num-
#ber of tracks, add that value to the album’s dictionary. Make at least one new
#function call that includes the number of tracks on an album.
def make_album(artist,title,no_of_tracks=''):
    if no_of_tracks:
        album = { 'artist_name':artist,
                 'title_of_album':title,
                 'number_of_tracks':no_of_tracks,
                }
    else:
        album = { 'artist_name':artist,
                 'title_of_album':title,
                }
    return album

#album = make_album('ween','white pepper')
#print(album)
#album = make_album('joy division','unknown pleasures', '10')
#print(album)
#album = make_album('penguin cafe orchestra','music from the penguin cafe')
#print(album)
while True:
    artist = input("enter an artist ('q' to quit)")
    if artist == 'q':
        break
    title = input("enter an album title ('q' to quit)")
    if title == 'q':
        break
    album = make_album(artist,title)
    print(album)
