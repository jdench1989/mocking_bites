from lib._01_exercise_track import *

class MusicLibrary:

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        search_results = []
        for track in self.track_list:
            if track.matches(keyword):
                search_results.append(track)
        return search_results