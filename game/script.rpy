init python:

    def reset_data():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)

        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)

        renpy.quit(relaunch=True)


# Presplash Loading Time
define config.minimum_presplash_time = 3.0

default player_name = ""

define e = Character("Eileen")
image splash_logo = "splash.jpg"

label splashscreen:
    show splash_logo
    with dissolve
    pause 1
    hide splash_logo
    with dissolve

    show screen age_prompt
    with dissolve
    $ ui.interact()
    hide screen age_prompt
    with dissolve

    return

label start:

    $ game = Game("YouTube VN")
    $ persistent.time_of_day = "day"
    $ player = Player(player_name)
    jump player_bedroom

label game_main:

    $ tod = game.timer.tod

    if tod == 0:
        $ persistent.time_of_day = "day"
    elif tod == 1:
        $ persistent.time_of_day = "afternoon"
    elif tod == 2:
        $ persistent.time_of_day = "evening"
    elif tod == 3:
        $ persistent.time_of_day = "night"

    $ player.location.hide_screen()
    $ player.location.call()