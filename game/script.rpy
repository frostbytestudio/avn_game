init -1 python:
    
    ShowSplashScreen(False)

# Presplash Loading Time
define config.minimum_presplash_time = 3.0

default player_name = ""

label splashscreen:
    if not persistent.show_splashscreen:
        return

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
    $ ShowSplashScreen(False)
    jump player_bedroom


label next_day:

    jump game_main