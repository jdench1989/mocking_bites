class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        return True if keyword in self.title or keyword in self.artist else False
