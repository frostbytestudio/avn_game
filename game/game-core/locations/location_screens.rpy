screen bedroom_screen:
    #text "This is the bedroom screen!"

    imagebutton:
        focus_mask True
        pos (375, 180)
        idle get_door("object_door_01", day_timer.current_tod)
        hover HoverImage(get_door("object_door_01", day_timer.current_tod))
        action Jump("home_hallway")

screen hallway_screen:

    imagebutton:
        focus_mask True
        pos (279, 262)
        idle get_door("object_door_02", day_timer.current_tod)
        hover HoverImage(get_door("object_door_02", day_timer.current_tod))
        action Jump("player_bedroom")