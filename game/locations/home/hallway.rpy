label hallway:

    if route == 2:
        scene house_hallway_mc
        hide screen bedroom_day

        show landlady_base:
            xalign 0.8
            yalign 1.0

        mom "Hello there!"
    else:
        pass

    scene house_hallway_mc
    hide screen bedroom_day

    show screen hallway_day

    $ ui.interact()
