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

        @property
        def label(self):
            if self._label:
                return self._label
            else:
                return self.ref

    
        def hide_screen(self):
            renpy.hide_screen("ui")
            try:
                renpy.hide_screen(self.ref)

            except Exception as e:
                pass
            pass

        def call(self):
            renpy.log(f"Calling Location with label: {self.label}")
            if self._label:
                renpy.call(self.label)
            elif self.ref:
                renpy.call_screen(self.ref)
            else:
                raise AttributeError(f"'{self.__class__.__name__}' object has no valid 'label' or 'ref' to call")
            pass

        def call_screen(self, *args, **kwargs):
            if self.ref:
                renpy.call_screen(self.ref, *args, **kwargs)
            else:
                raise AttributeError(f"Location '{self.name}' has no screen reference ('ref') set.")