from lib._01_exercise_music_library import *
from lib._01_exercise_track import *
import pytest

# Given a track
# Adds track to the library
def test_adds_track_to_library():
    music_library = MusicLibrary()
    track1 = Track("Bohemian Rhapsody", "Queen")
    music_library.add(track1)
    assert music_library.track_list == [track1]

# Given multiple tracks
# Adds both to tracklist as a title/artist pair
def test_adds_multiple_tracks():
    music_library = MusicLibrary()
    track1 = Track("Bohemian Rhapsody", "Queen")
    track2 = Track("Careless Whisper", "Wham!")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.track_list == [track1, track2]

# Given multiple tracks in track_list
# And given a keyword
# search() returns a list of (title, artist) tuples matching 
# the keyword in either field
def test_keyword_search():
    music_library = MusicLibrary()
    track1 = Track("Bohemian Rhapsody", "Queen")
    track2 = Track("Careless Whisper", "Wham!")
    track3 = Track("We are the champions", "Queen")
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.search("Careless") == [track2]
    assert music_library.search("Queen") == [track1, track3]