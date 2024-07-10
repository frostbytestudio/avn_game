init -3 python:

    class Location(object):

        def __init__(self, name, background_key, parents=None, locked=False, label="", ref=None):
            self.name = name
            self.ref = ref
            self._label = label
            self._locked = locked
            if isinstance(parents, Location):
                self.parents = [parents]
            else:
                self.parents = parents
            self.background_key = background_key

        def call_screen(self, *args, **kwargs):
            if self.ref:
                renpy.call_screen(self.ref, *args, **kwargs)
            else:
                raise AttributeError(f"Location '{self.name}' has no screen reference ('ref') set.")