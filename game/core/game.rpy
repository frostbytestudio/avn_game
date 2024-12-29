init -6 python:

    class Game:

        def __init__(self, name):
            self.name = name
            self.timer = DayTimer()

        def main(self, clear_return_stack=True, location=None, call_location_lbl=False, call_screen_args=[]):
            renpy.scene(layer='screens')
            renpy.free_memory()
            renpy.display.render.free_memory()

            _window_hide()
        

            renpy.show_screen("game_gui")
            renpy.show_screen("navi")

            if location is None:
                player.location.call_screen(*call_screen_args)
                if call_location_lbl:
                    player.location.call()

screen game_gui:

    default day_timer = game.timer

    vbox:
        text "Current Time of Day: [persistent.time_of_day]"
        #text "TOD: [tod]"
        text "Game Day: [persistent.gameDay]"

    if(player.location == L_home_bedroom):

        hbox:

            style "navigation_menu_bottom"

            if (day_timer._tod <=2):
                imagebutton:
                    idle "navi_menu_time"
                    hover "navi_menu_time"
                    at hover_darken(-0.2)
                    focus_mask True
                    action TickTimer()
            else:
                # Don't show Advance Time after "Evening"
                pass


            imagebutton:
                idle "navi_menu_sleep"
                hover "navi_menu_sleep"
                at hover_darken(-0.2)
                focus_mask True
                action ResetTOD()

    else:
        # Don't show Advance Time and Sleep Button Outside of Player Room
        pass



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

    $ event_manager.check_events()

    $ player.location.hide_screen()
    $ player.location.call()