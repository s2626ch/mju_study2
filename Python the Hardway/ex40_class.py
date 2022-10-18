class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing(self):
        for line in self.lyrics:
            print(line)


birthday_song = Song(["happy ", "No sue", "Stop"])
bulls_on_parade = Song(["Shell", "Family"])

birthday_song.sing()
bulls_on_parade.sing()
