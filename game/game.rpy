init -6 python:

    class Game:

        def __init__(self, name):
            self.name = name
            renpy.log("Game initialized with name: {}".format(name))

        def main(self, clear_return_stack=True, location=None, call_location_lbl=False, call_screen_args=[]):
            renpy.scene(layer='screens')
            renpy.free_memory()
            renpy.display.render.free_memory()
            
            _window_hide()

            #renpy.show_screen("game_gui")

            if location is None:
                player.location.call_screen(*call_screen_args)
                if call_location_lbl:
                    player.location.call()