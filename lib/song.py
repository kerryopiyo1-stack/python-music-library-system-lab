#!/usr/bin/env python3

class Song:
    """Represents a song with name, artist, and genre."""

    # Class attributes (shared by all Song objects)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """Initialize a new Song object with name, artist, and genre."""
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger all class methods upon creation
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        """Increments the value of count by one."""
        Song.count += 1

    def add_to_genres(self):
        """Adds any new genres to a class attribute genres.
        Ensures there are only unique genres - no duplicates!"""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Adds any new artists to a class attribute artists.
        Ensures there are only unique artists - no duplicates!"""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Updates class attribute genre_count.
        Increments genre key by 1, if genre doesn't exist in genre_count add the key and set it to 1."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists_count(self):
        """Updates class attribute artists_count.
        Increments artist key by 1, if artist doesn't exist in artists_count add the key and set it to 1."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1