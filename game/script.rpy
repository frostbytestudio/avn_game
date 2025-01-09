init python:


# Presplash Loading Time
define config.minimum_presplash_time = 3.0

default player_name = ""

define anon = Character("Player", color="#c8ffc8")
define liz = Character("Liz", color="#e9216dff")



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
    $ day_timer = game.timer
    $ player = Player(player_name)
    $ event_manager.check_events()
    jump player_bedroom


label next_day:

    jump game_main