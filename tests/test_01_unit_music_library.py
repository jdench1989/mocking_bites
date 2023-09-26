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
# Adds both to tracklist
def test_tracklist_add_without_integration():
    music_library = MusicLibrary()
    fake_track_1 = create_fake_track("Bohemian Rhapsody", "Queen")
    fake_track_2 = create_fake_track("Backstreet's Back", "Backstreet Boys")
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    assert music_library.track_list == [fake_track_1, fake_track_2]

# Given multiple tracks in track_list in isolation (no class integration)
# And given a keyword
# search() returns a list of tracks matching the keyword in either field
def test_keyword_search():
    music_library = MusicLibrary()
    fake_track_1 = create_fake_track("Title1", "Artist1")
    fake_track_2 = create_fake_track("Title2", "Artist2")
    fake_track_3 = create_fake_track("Title3", "Artist3")
    fake_track_1.matches.return_value = True
    fake_track_2.matches.return_value = False
    fake_track_3.matches.return_value = True
    music_library.add(fake_track_1)
    music_library.add(fake_track_2)
    music_library.add(fake_track_3)
    assert music_library.search("Test") == [fake_track_1, fake_track_3]
    