label bedroom:
    $ renpy.block_rollback()
    scene mc_bedroom_day

    show screen bedroom_day
    show screen UI

    hide screen hallway_day
    hide screen mc_computer

    $ ui.interact()

label bedroomNew:
    $ renpy.block_rollback()
    scene mc_bedroom_day

    show screen bedroom_day
    show screen UI

    $ ui.interact()

label computer:

    scene mc_pc
    hide screen bedroom_day

    show screen mc_computer

    $ ui.interact()

label computerNew:

    scene mc_pc_broke

    hide screen mc_computer
    hide screen bedroom_day

    mc "What the...fuck?!"
    mc "No, no, no! Not the blue screen of death!"

    mc "Seriously? What kind of game includes a blue screen of death? Who thought this was a good idea?"
    mc "Why would the developers put this in here? Are they messing with me?"

    mc "Maybe it's meant to push the story forward somehow. Ugh, fine. Guess I'll have to figure out what to do next without my PC."

    $ renpy.notify("Find a way to fix your PC!")
    $ pcBroke = True
    $ bedroomDoorLocked = False
    $ route += 1

    jump bedroom

label computerBroke:

    mc "I need to find a way to fix this stupid PC."

    jump bedroom