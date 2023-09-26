from lib._01_exercise_track import *

# Initialises with title and artist stored correctly
def test_initilisation():
    track = Track("Mambo No 5", "Lou Bega")
    assert track.title == "Mambo No 5"
    assert track.artist == "Lou Bega"

# Given a title and artist
# matches() returns correct value
def test_matches_returns_correct_value():
    track = Track("Common People", "Pulp")
    assert track.matches("Common") == True
    assert track.matches("Pulp") == True
    assert track.matches("Elvis") ==False