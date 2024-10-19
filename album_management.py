class Album:
    def  __init__(self, album_name, number_of_songs, album_artist):
        """
        a class that represents an album with its name, number of songs and artist
        """
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist
   

    def __str__(self):
        """
        a method that returns a string representation of the album
        """
        return f"Album Name: {self.album_name}\nNumber of Songs: {self.number_of_songs}\nAlbum Artist: {self.album_artist}"
    
   
#album 1
album1 = []
album1.append(Album("The Wall", 26, "Pink Floyd"))
album1.append(Album("Thriller", 9, "Michael Jackson"))
album1.append(Album("Back in Black", 10, "AC/DC"))
album1.append(Album("The Dark Side of the Moon", 10, "Pink Floyd"))
album1.append(Album("Led Zeppelin IV", 8, "Led Zeppelin"))


#sort the albums by the number of songs
sorted_albums = sorted(album1, key=lambda album: album.number_of_songs)

#swap the first two albums
sorted_albums[0], sorted_albums[1] = sorted_albums[1], sorted_albums[0]

#album 2
album2 = []
album2.append(Album("The One", 56, "Alex Periera"))
album2.append(Album("The Two", 9, "Warren Jackson"))
album2.append(Album("The Three", 10, "RC/IC"))
album2.append(Album("The Four", 10, "Ross William "))
album2.append(Album("The Five", 8, "Zed Zeppelin"))


#copy album1 to album2
album2 += album1


#add two albums to album 2 
album2.append(Album('Dark Side of the Moon', 9,  'Pink Floyd'))
album2.append(Album('Oops!... I Did It Again',  16,'Britney Spears'))

#sort the albums by the album name
album2 = sorted(album2, key=lambda album: album.album_name)
    
#find the index of the album with the name 'Dark Side of the Moon'
for album in album2:
    index= 1
    if album.album_name == 'Dark Side of the Moon':
        print(index)
    else:
        index += 1

