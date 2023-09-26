from lib._01_exercise_track import *

# Initialises with title and artist stored correctly
def test_initilisation():
    track = Track("Mambo No 5", "Lou Bega")
    assert track.title == "Mambo No 5"
    assert track.artist == "Lou Bega"