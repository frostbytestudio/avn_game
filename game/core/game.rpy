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

            if location is None:
                player.location.call_screen(*call_screen_args)
                if call_location_lbl:
                    player.location.call()

screen game_gui:

    default tod = game.timer.tod
    default time_pieces_positions = [554, 499, 444]

    add "images/gui/ui_piece_time.png" xpos 441 ypos 2
    for i in xrange(3 - game.timer._tod):
        add "images/gui/ui_day_cycle_bar.png" pos time_pieces_positions[i], 29

    vbox:
        text "Current Time of Day: [persistent.time_of_day]"
        text "TOD: [tod]"
        text "Game Day: [gameDay]"

    if(player.location == L_home_bedroom):
        if (tod <= 2):
            imagebutton:
                idle "images/gui/ui_piece_skip.png"
                pos 507, 46
                action TickTimer()

        if tod == 3:
            textbutton "Reset TOD":
                pos 0, 80
                action ResetTOD()
    else:
        # Don't show button anywhere else
        pass