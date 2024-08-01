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
define anon = Character("Player", color="#c8ffc8")
default gameDay = 0

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

label introduction:

    if not chapter1.current_subchapter().completed:
        show player bedroom blur with dissolve
        show anon norm at custom_position
        anon "I hate waking up early..."
        anon "I should probably get ready for school and go downstaris...right?"
        $ chapter1.current_subchapter().completed = True
        hide player bedroom blur with dissolve
        hide anon norm with dissolve
        jump game_main

label conflict:
    
    if not chapter1.current_subchapter().completed:
        e "This is the conflict subchapter!"
        $ chapter1.current_subchapter().completed = True
    return

label resolution:
    
    if not chapter1.current_subchapter().completed:
        e "This is the resolution subchapter!"
        $ chapter1.current_subchapter().completed = True
    
    if chapter1.is_completed():
        $ chapter1.completed = True
        $ player.completed_chapters.append(chapter1.name)
        e "Chapter 1 is now complete!"
    return

label intro2:
    
    if not chapter2.current_subchapter().completed:
        e "This is the Intro 2 to Chapter 2!"
        $ chapter2.current_subchapter().completed = True
    return


label next_day:

    $ gameDay += 1
    jump game_main



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