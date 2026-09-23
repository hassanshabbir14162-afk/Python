class Playlist:

    def __init__(self,name, genre):
        self.name=name
        self.genre=genre
        self.songs=[]
        print(f"Playlist '{self.name}' ({self.genre}) is ready)

    def add song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")

    def remove.songs(self, song):
        if song in self.songs:
            self.remove.song