
"""
A playlist app. The students could extend it by writing `+`
and `*` (for example).
"""
class Song:
    def __init__(self, artist, song_title, record_label="Unknown Label",
                 runtime=(0, 0), genre=None):
        self.artist = artist
        self.title = song_title
        self.label = record_label
        self.runtime = runtime
        self.genre = genre

    def __str__(self):
        return "'{}' by {} ({}): {:d}:{:02d}, Genre: {}".format(
            self.title, self.artist, self.label,
            self.runtime[0], self.runtime[1], self.genre)


class Playlist:
    def __init__(self, name, songs=[]):
        self.name = name
        self.songs = songs.copy()

    def add_song(self, artist, song_title, record_label=None,
                 runtime=(0, 0), genre=None):
        new_song = Song(artist, song_title, record_label, runtime, genre)
        self.songs.append(new_song)

    def get_playlist_length(self):
        return len(self.songs)

    def get_total_runtime(self):
        total_minutes = 0
        total_seconds = 0
        for songs in self.songs:
            total_minutes += songs.runtime[0]
            total_seconds += songs.runtime[1]

        total_minutes += int(total_seconds / 60)
        total_seconds = total_seconds % 60
        return (total_minutes, total_seconds)

    def __add__(self, other):
        return Playlist(self.name + " + " + other.name, self.songs + other.songs)

    def __mul__(self, num_times):
        return Playlist(self.name + " * " + str(num_times), self.songs * num_times)

    def __str__(self):
        totmin, totsec = self.get_total_runtime()
        result = "{} (total run time of {:d}:{:02d})\n".format(self.name, totmin, totsec)
        for song in self.songs:
            result += " " * 5 + str(song) + "\n"
        return result


playlist_1 = Playlist("Top 100 - 4/10/20")

playlist_1.add_song("Drake", "Toosie Slide", "Republic", (3, 4), "Rap")
playlist_1.add_song("The Weeknd", "Blinding Lights", "Republic", (3, 11))
playlist_1.add_song("Roddy Ricch", "The Box", "Atlantic Records", (2, 59))
playlist_1.add_song("Megan Thee Stallion", "Savage", None, (2, 59))
print(playlist_1)

fela = Playlist("Fela", [])
fela.add_song("Fela Kuti", "Mr. Follow Follow", "Island", (12, 4), "Afrobeat")
fela.add_song("Fela Kuti", "Lady", "Island", (15, 44), "Afrobeat")
print(fela)

lots_of_fela = fela * 4
print(lots_of_fela)

combined_list = playlist_1 + lots_of_fela + playlist_1
print(combined_list)
