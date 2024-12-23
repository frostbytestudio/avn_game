# Define UI Images
image navi_menu_options = "gui/interface/options.webp"
image navi_menu_profile = "gui/interface/profile.webp"
image navi_menu_events = "gui/interface/quest.webp"
image navi_menu_inventory = "gui/interface/backpack.webp"
image navi_menu_phone = "gui/interface/phone.webp"
image navi_menu_map = "gui/interface/map.webp"
image navi_menu_time = "gui/interface/time.webp"
image navi_menu_sleep = "gui/interface/sleep.webp"

screen navi:

    layer "overlay"

    # Main Top Bar Container
    hbox:

        xfill True 
        ypos 0

        # Left Section - Settings, Profile, Events
        hbox:

            xsize 300

            imagebutton:
                idle "navi_menu_options"
                hover "navi_menu_options"
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_profile"
                hover "navi_menu_profile"
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_events"
                hover "navi_menu_events"
                focus_mask True
                action NullAction()

        # Center Section - Time and WeekDay

        # Right Section - Inventory, Phone, Map
        hbox:

            xsize 300

            imagebutton:
                idle "navi_menu_inventory"
                hover "navi_menu_inventory"
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_phone"
                hover "navi_menu_phone"
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_map"
                hover "navi_menu_map"
                focus_mask True
                action NullAction()