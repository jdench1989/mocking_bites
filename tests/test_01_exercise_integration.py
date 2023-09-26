from lib._01_exercise_music_library import *
from lib._01_exercise_track import *
import pytest

# Given a track
# Adds track to the library
def test_adds_track_to_library():
    music_library = MusicLibrary()
    music_library.add(Track("Bohemian Rhapsody", "Queen"))
    assert music_library.track_list == [("Bohemian Rhapsody", "Queen")]

# Given multiple tracks
# Adds both to tracklist as a title/artist pair
def test_adds_multiple_tracks():
    music_library = MusicLibrary()
    music_library.add(Track("Bohemian Rhapsody", "Queen"))
    music_library.add(Track("Careless Whisper", "Wham!"))
    assert music_library.track_list == [("Bohemian Rhapsody", "Queen"), ("Careless Whisper", "Wham!")]

# Given multiple tracks in track_list
# And given a keyword
# search() returns a list of (title, artist) tuples matching 
# the keyword in either field
def test_keyword_search():
    music_library = MusicLibrary()
    music_library.add(Track("Bohemian Rhapsody", "Queen"))
    music_library.add(Track("Careless Whisper", "Wham!"))
    music_library.add(Track("We Are The Champions", "Queen"))
    assert music_library.search("Careless") == [(("Careless Whisper", "Wham!"))]
    assert music_library.search("Queen") == [("Bohemian Rhapsody", "Queen"), ("We Are The Champions", "Queen")]