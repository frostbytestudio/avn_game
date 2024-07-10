screen bedroom_screen:
    #text "This is the bedroom screen!"

    imagebutton:
        focus_mask True
        pos (225, 187)
        idle "objects/object_door_01.png"
        hover "objects/object_door_01_hover.png"
        action Jump("home_hallway")

screen hallway_screen:

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

    imagebutton:
        focus_mask True
        pos (140, 168)
        idle "objects/object_stairs_02.png"
        hover "objects/object_stairs_02_hover.png"
        action Jump("home_hallway")