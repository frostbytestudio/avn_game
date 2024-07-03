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
    $ time_of_day = "day"
    $ player = Player(player_name)
    jump bedroom

label bedroom:
    $ player.location = L_home_bedroom
    scene expression get_background(player.location, time_of_day)
    $ game.main()

label home_hallway:
    $ player.location = L_home_hallway
    scene expression get_background(player.location, time_of_day)
    $ game.main()

label home_entrance:
    $ player.location = L_home_entrance
    scene expression get_background(player.location, time_of_day)
    $ game.main()

screen bedroom_screen:
    text "This is the bedroom screen!"

    imagebutton:
        focus_mask True
        pos (225, 187)
        idle "objects/object_door_01.png"
        hover "objects/object_door_01_hover.png"
        action Jump("home_hallway")

screen hallway_screen:
    text "This is the hallway screen!"

    imagebutton:
        focus_mask True
        pos (175, 280)
        idle "objects/object_door_02.png"
        hover "objects/object_door_02_hover.png"
        action Jump("bedroom")

    imagebutton:
        focus_mask True
        pos (830, 0)
        idle "objects/object_door_19.png"
        hover "objects/object_door_19_hover.png"
        action Jump("home_entrance")

screen entrance_screen:
    text "This is the entrance screen!"

    imagebutton:
        focus_mask True
        pos (140, 168)
        idle "objects/object_stairs_02.png"
        hover "objects/object_stairs_02_hover.png"
        action Jump("home_hallway")