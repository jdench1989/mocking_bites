from lib._01_exercise_music_library import *
from unittest.mock import Mock

def create_fake_track(title, artist):
    fake_track = Mock()
    fake_track.title = title
    fake_track.artist = artist
    return fake_track

# Class initialises with an empty track list
def test_track_list_initially_empty():
    music_library = MusicLibrary()
    assert music_library.track_list == []

## Given multiple tracks in isolation (no class integration)
# Adds both to tracklist as a title/artist tuple
def test_tracklist_add_without_integration():
    music_library = MusicLibrary()
    fake_track_1 = create_fake_track("Bohemian Rhapsody", "Queen")
    fake_track_2 = create_fake_track("Backstreet's Back", "Backstreet Boys")
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    assert music_library.track_list == [("Bohemian Rhapsody", "Queen"), ("Backstreet's Back", "Backstreet Boys")]