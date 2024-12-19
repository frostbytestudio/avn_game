init python:
    event_manager = EventManager()

    event_manager.add_event(Event(
        name = "Morning Event",
        conditions = [
            location_is("L_home_bedroom"),
            time_of_day_is("afternoon"),
            game_day_is(1)
        ],
        action = "morning_event_label",
        priority = 10,
        unique = True
    ))

label morning_event_label:

    "Good morning! This is the morning event label!"

    return

label test_event_label:
    "This is the test event label"

    return