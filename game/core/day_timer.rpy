init -6 python:

    class DayTimer:

        def __init__(self):
            self._tod = 0

        @property
        def tod(self):
            return self._tod

        def tick(self, tod=None):
            if tod is None:
                tod = self._tod + 1

            if not 0 <= tod <= 3:
                return

            renpy.block_rollback()

            self._tod = tod

        def reset(self, tod=None):
            self._tod = 0