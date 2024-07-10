init python:

    class TickTimer(Action):

        def __call__(self):
            game.timer.tick()
            renpy.scene(layer="screens")
            renpy.jump("game_main")