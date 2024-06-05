# UI Screen
screen UI:
    vbox:
        default money_string = '{:,}'.format(money)
        text "Money: [money_string]"
        text "Test"
        textbutton "Fix PC":
            action [SetVariable("pcBroke", False)]

# Player Bedroom
screen bedroom_day:

    # Bedroom Door
    imagebutton:
        pos(926, 268)
        idle "mc_door_base.png"
        hover "mc_door_select.png"
        if bedroomDoorLocked == True:
            action Call("route1")
        else:
            action Jump("hallway")

    # Computer
    imagebutton:
        pos(654, 330)
        idle "mc_pc_base.png"
        hover "mc_pc_select.png"
        if newGame == True:
            action Jump("computerNew")
        else:
            action Jump("computer")

        if pcBroke == True:
            action Call("computerBroke")
        else:
            pass

# Home Hallway
screen hallway_day:

    imagebutton:
        pos (813, 262)
        idle "house_hallway_playerDoor.png"
        hover "house_hallway_playerDoor_hover.png"
        action Jump("bedroom")

# Player Computer
screen mc_computer:

    textbutton "Back":
        xalign 0.5
        action Jump("bedroom")