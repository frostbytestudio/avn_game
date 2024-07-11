init python:

    class HoverImage(renpy.Displayable):
        def __init__(self, img, **kwargs):
            super(HoverImage, self).__init__(**kwargs)
            self._image = img
            self._matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)

        def render(self, width, height, st, at):
            r = renpy.render(im.MatrixColor(self._image, self._matrix), width, height, st, at)
            return r

    
    def get_door(door_id, time_of_day):
        if time_of_day in ["day", "afternoon"]:
            time_of_day = "default"
        elif time_of_day in ["evening", "night"]:
            time_of_day = "night"
        return "objects/{}_{}.png".format(door_id, time_of_day)