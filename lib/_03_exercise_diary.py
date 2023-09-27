# File: lib/diary.py

class Diary:
    def __init__(self, contents):
        # Contents are stored in self.contents attribute if string
        # Else error thrown
        if isinstance(contents, str):
            self.contents = contents
        else:
            raise Exception("Contents must be a string")

    def read(self):
        # Returns the contents of the diary
        return self.contents