screen bedroom_screen:
    #text "This is the bedroom screen!"

    imagebutton:
        focus_mask True
        pos (225, 187)
        idle get_door("object_door_01", persistent.time_of_day)
        hover HoverImage(get_door("object_door_01", persistent.time_of_day))
        action Jump("home_hallway")

screen hallway_screen:

    imagebutton:
        focus_mask True
        pos (175, 280)
        idle get_door("object_door_02", persistent.time_of_day)
        hover HoverImage(get_door("object_door_02", persistent.time_of_day))
        action Jump("player_bedroom")

screen entrance_screen:

    text "Home Entrance Screen"