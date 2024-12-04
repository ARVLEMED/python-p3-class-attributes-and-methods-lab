class Song:
    count = 0  
    genres = [] 
    artists = []  
    genre_count = {}  
    artist_count = {}  

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(self.genre)  
        self.add_to_artists(self.artist)  
        self.add_to_genre_count(self.genre)  
        self.add_to_artist_count(self.artist)  

    @classmethod
    def add_song_to_count(cls):
        """Increments the song count by 1 whenever a new song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Adds the genre to the genres list if it's not already present."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Adds the artist to the artists list if it's not already present."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Updates the genre_count histogram with the number of songs per genre."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Updates the artist_count histogram with the number of songs per artist."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
