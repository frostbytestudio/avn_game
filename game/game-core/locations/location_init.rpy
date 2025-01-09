init -2 python:

    L_home_bedroom = Location("Bedroom", background_key="home_bedroom", parents=[None], label="player_bedroom", ref="bedroom_screen")
    L_home_hallway = Location("Hallway", background_key="home_hallway", parents=[None], ref="hallway_screen")
    L_home_entrance = Location("Entrance", background_key="home_entrance", parents=[None], ref="entrance_screen")

    home_bedroom_day = "images/backgrounds/location_home_bedroom_day.jpg"
    home_bedroom_evening = "images/backgrounds/location_home_bedroom_evening.jpg"
    home_bedroom_night = "images/backgrounds/location_home_bedroom_night.jpg"

    home_hallway_day = "images/backgrounds/location_home_hallway_day.jpg"
    home_hallway_night = "images/backgrounds/location_home_hallway_night.jpg"

    home_kitchen_day = "images/backgrounds/location_home_kitchen_day.jpg"

    home_entrance_day = "images/backgrounds/location_home_entrance_day.jpg"

    # Define a dictionary to map location and time of day to variables
    backgrounds = {
        "home_bedroom": {
            "day": home_bedroom_day,
            "afternoon": home_bedroom_day,
            "evening": home_bedroom_evening,
            "night": home_bedroom_night,
            "default": home_bedroom_day  # Fallback/default background
        },
        "home_hallway": {
            "day": home_hallway_day,
            "evening": home_hallway_night,
            "night": home_hallway_night,
            "default": home_hallway_day  # Fallback/default background
        },
        "home_kitchen": {
            "day": home_kitchen_day,
            "default": home_kitchen_day
        },
        "home_entrance": {
            "day": home_entrance_day,
            "default": home_entrance_day
        }
    }

    def get_background(location, time_of_day, blur=False):
        return backgrounds[location.background_key].get(time_of_day, backgrounds[location.background_key].get("default"))