albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
    [
        (1, "Welcome to my Nightmare"),
        (2, "Devil's Food"),
        (3, "The Black Widow"),
        (4, "Some Folks"),
        (5, "Only Women Bleed"),
    ]
    ),
    ("Bad Company", "Bad Company", 1974,
    [
        (1, "Can't Get Enough"),
        (2, "Rock Steady"),
        (3, "Ready for Love"),
        (4, "Don't Let Me Down"),
        (5, "Bad Company"),
        (6, "The Way I Choose"),
        (7, "Movin' On"),
        (8, "Seagull"),
    ]
    ),
    ("Nightflight", "Budgie", 1981,
    [
        (1, "I Turned to Stone"),
        (2, "Keeping a Rendezvous"),
        (3, "Reaper of the Glory"),
        (4, "She Used Me Up"),
    ]
    ),
    ("More Mayhem", "Imelda May", 2011,
    [
        (1, "Pulling the Rug"),
        (2, "Psycho"),
        (3, "Mayhem"),
        (4, "Kentish Town Waltz"),
    ]
    ),
]
SONGS_LIST = 3
SONG_TITLE_INDEX = 0
SONG_TITLE = 1

while True:
    print("Please choose your album - invalid choice exits the program")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    album_choice = int(input())

    if 1 <= album_choice <= len(albums):
        songs = albums[album_choice - 1][SONGS_LIST]
    else:
        break

    print("Please choose your song:")
    for index, (track_number, song) in enumerate(songs):
        print(f"{index + 1}: {song}")

    song_choice = int(input())

    if 1 <= song_choice <= len(songs):
        title = songs[song_choice - 1][SONG_TITLE]
        print(f"Playing {title}")

    print(f"{"=" * 50}")
