# Define UI Images
image navi_menu_icon_options = "gui/interface/options.webp"
image navi_menu_icon_profile = "gui/interface/profile.webp"
image navi_menu_icon_events = "gui/interface/quest.webp"
image navi_menu_icon_inventory = "gui/interface/backpack.webp"
image navi_menu_icon_phone = "gui/interface/phone.webp"
image navi_menu_icon_map = "gui/interface/map.webp"
image navi_menu_icon_time = "gui/interface/time.webp"
image navi_menu_icon_sleep = "gui/interface/sleep.webp"

# Define The Screen NAVI
screen navi:

    layer "overlay"

    # Left Section - Settings, Profile, Events
    hbox:

        # Main Top Container
        xfill True
        ypos 0 


        xsize 300

        imagebutton:
            idle "navi_menu_icon_options"
            hover "navi_menu_icon_options"
            focus_mask True
            action NullAction()

        imagebutton:
            idle "navi_menu_icon_profile"
            hover "navi_menu_icon_profile"
            focus_mask True
            action NullAction()

        imagebutton:
            idle "navi_menu_icon_events"
            hover "navi_menu_icon_events"
            focus_mask True
            action NullAction()

    # Center Section - Time and Weekday

    # Right Section - Inventory, Cell Phone, Map