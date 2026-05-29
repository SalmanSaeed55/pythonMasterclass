class Song:
    """Represent a song with title, artist, and optional duration in seconds."""

    def __init__(self, title, artist, duration=0):
        """Initialise a Song instance.

        Args:
            title: The song title.
            artist: The performing artist or band.
            duration: Song length in seconds. Defaults to 0.
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Represent an album, using it's track list."""

    def __init__(self, name, year, artist):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)



class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)


def find_object(field, object_list):
    for item in object_list:
        if item._name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("./files/albums.txt", "r", encoding="utf-8") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
    return artist_list


def create_checkfile(artist_list):
    with open("./files/checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=checkfile)


help(Song.__init__)
print(Song.__doc__)
print(Song.__init__.__doc__)

Song.__init__.__doc__ = """Song init method
Args:
    title: The song title.
    artist: The performing artist.
    duration: Song length in seconds. Defaults to 0.
"""
help(Song)
print()
help(Album)

if __name__ == "__main__":
    artists = load_data()
    print(f"There are {len(artists)} artists.")

    create_checkfile(artists)