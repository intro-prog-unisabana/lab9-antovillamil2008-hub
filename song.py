class Song:

    def __init__(self, name, artist, length):
        self.name = str(name)
        self.artist = str(artist)
        self.length = float(length)
    
    def __str__(self):
        return f"'{self.name}' by {self.artist} {self.length}"
    
    def get_length_in_seconds(self):
        return self.length*60


my_song = Song("tv off", "Kendrick Lamar", 3.7)
print(my_song.get_length_in_seconds())
print(my_song)