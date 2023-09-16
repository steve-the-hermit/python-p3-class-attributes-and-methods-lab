class Song:
    count = 0  # Class-level variable to count the total number of Song objects
    genres = set()  # Class-level set to store all Song genres
    artists = set()  # Class-level set to store all Song artists
    genre_count = {}  # Class-level dictionary to keep count of Songs for each genre
    artist_count = {}  # Class-level dictionary to keep count of Songs for each artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
