init -6 python:

    class DayTimer:

        # Time CONSTS
        TIME_OF_DAY = ["day", "afternoon", "evening", "night"]
        TIME_OF_DAY_DISPLAY = ["Day", "Afternoon", "Evening", "Night"]
        DAY_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        def __init__(self):
            self._tod = 0
            self._weekday_index = 0
            self._game_day = 1

        @property
        def current_tod(self):
            return self.TIME_OF_DAY[self._tod]

        @property
        def current_tod_display(self):
            return self.TIME_OF_DAY_DISPLAY[self._tod]

        @property
        def current_weekday(self):
            return self.DAY_OF_WEEK[self._weekday_index]

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
            self._weekday_index = (self._weekday_index + 1) % len(self.DAY_OF_WEEK)