# Define UI Images
image navi_menu_options = "gui/interface/options.webp"
image navi_menu_profile = "gui/interface/profile.webp"
image navi_menu_events = "gui/interface/quest.webp"
image navi_menu_inventory = "gui/interface/backpack.webp"
image navi_menu_phone = "gui/interface/phone.webp"
image navi_menu_map = "gui/interface/map.webp"
image navi_menu_time = "gui/interface/time.webp"
image navi_menu_sleep = "gui/interface/sleep.webp"

screen time_display():

    vbox:

        yalign 0.5
        
        text "8:00 AM" style "time_display_text"
        text "Monday" style "time_display_text"


# INIT THE STYLES AND TRANSFORMS #

# Define a transform for the darkened hover state
transform hover_darken(dark_amount=-0.2):
    on idle:
        matrixcolor Matrix.identity()
        zoom 0.04
    on hover:
        matrixcolor BrightnessMatrix(dark_amount)
        zoom 0.04
    on insensitive:
        matrixcolor BrightnessMatrix(dark_amount)
        zoom 0.04

# Style for Nav Menu
style navigation_menu:
    spacing 18          # Controls the gap between icons
    xalign 0.0          # X pos the entire menu
    yalign 0.0          # Y pos the entire menu
    xpadding 20         # X margin from the screen edge
    ypadding 20         # Y margin from the screen edge

style time_display_text:
    text_align 0.5
    bold True
    font "DejaVuSans.ttf"
    outlines [ (2, "#000000", 0, 0) ]
    size 24
    color "#ffffff"
    yalign 0.5


screen navi:

    layer "overlay"

    # Main Top Bar Container
    hbox:

        xfill True  # Stretch across the screen width
        ypos 0      # Position at top

        # Left Section - Settings, Profile, Events
        hbox:

            style "navigation_menu"
            xsize 300

            imagebutton:
                idle "navi_menu_options"
                hover "navi_menu_options"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_profile"
                hover "navi_menu_profile"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_events"
                hover "navi_menu_events"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

        # Center Section - Time and WeekDay
        use time_display()

        # Right Section - Inventory, Phone, Map
        hbox:

            xalign 1.0  # Right-align this section
            xsize 300   # Match left section width

            imagebutton:
                idle "navi_menu_inventory"
                hover "navi_menu_inventory"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_phone"
                hover "navi_menu_phone"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

            imagebutton:
                idle "navi_menu_map"
                hover "navi_menu_map"
                at hover_darken(-0.2)
                focus_mask True
                action NullAction()

        # Bottom Right Section - Advance Time, Sleep