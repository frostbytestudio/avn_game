init python:

    class Player(object):

        def __init__(self, name=""):
            self.name = name
            self.location = None
            self.completed_chapters = []
            self.completed_subchapters = []