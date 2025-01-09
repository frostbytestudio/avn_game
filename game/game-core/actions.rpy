init python:

    class TickTimer(Action):

        def __call__(self):
            game.timer.tick()
            renpy.scene(layer="screens")
            renpy.jump("game_main")

    class ResetTOD(Action):

        def __call__(self):
            game.timer.reset()
            renpy.scene(layer="screens")
            renpy.jump("next_day")

    def reset_data():
        for attr in dir(persistent):
            if not callable(attr) and not attr.startswith("_"):
                setattr(persistent, attr, None)

        for slot in renpy.list_saved_games(fast=True):
            renpy.unlink_save(slot)

        renpy.quit(relaunch=True)