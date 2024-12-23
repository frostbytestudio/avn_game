init -10 python:

    class Event:
        """
        Represents a single event with conditions and an action.
        """
        def __init__(self, name, conditions, action, priority=0, unique=True):
            self.name = name
            self.conditions = conditions
            self.action = action
            self.priority = priority
            self.unique = unique
            self.completed = False

        def is_triggered(self, **kwargs):
            """
            Checks if all conditions are met for this event.
            """
            return not self.completed and all(condition(**kwargs) for condition in self.conditions)

        def trigger(self):
            """
            Triggers the event action and marks it as completed if unique.
            """
            renpy.call_in_new_context(self.action)
            if self.unique:
                self.completed = True

    class EventManager:
        """
        Manages a list of events, checks conditions, and trigger events.
        """
        def __init__(self):
            self.events = []

        def add_event(self, event):
            """
            Adds a new event to the manager.
            """
            self.events.append(event)

        def check_events(self, **kwargs):
            """
            Checks all events and queues those whose conditions are met.
            Executes them one by one.
            """
            triggered_events = []

            # Checks all events and adds triggered ones to the queue
            for event in sorted(self.events, key=lambda e: e.priority, reverse=True):
                print(f"DEBUG: Triggering Event: {event.name}")
                triggered_events.append(event)

            for event in triggered_events:
                event.trigger()

    # Condition Checks

    # Condition: Location Check
    def location_is(location_name):
        return lambda **kwargs: persistent.player_location == location_name

    # Condition: Time of Day Check
    def time_of_day_is(tod_name):
        return lambda **kwargs: (
            print(f"DEBUG: Checking if time_of_day == {tod_name} (Current: {persistent.time_of_day})") or persistent.time_of_day == tod_name)

    # Condition: Game Day Check
    def game_day_is(day):
        return lambda **kwargs: persistent.gameDay == day