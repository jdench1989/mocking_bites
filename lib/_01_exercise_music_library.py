from lib._01_exercise_track import *

class MusicLibrary:

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append((track.title, track.artist))

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        search_list = []
        