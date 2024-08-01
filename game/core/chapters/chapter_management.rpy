init -10 python:

    class Chapter():

        class SubChapter:

            def __init__(self, name):
                self.name = name
                self.completed = False

        def __init__(self, name, subchapters):
            self.name = name
            self.subchapters = [self.SubChapter(sc) for sc in subchapters]
            self.current_subchapter_index = 1
            self.completed = False

        def start(self):
            self.current_subchapter_index = 0
            renpy.call(self.subchapters[self.current_subchapter_index].name)

        def current_subchapter(self):
            if self.current_subchapter_index >= 0 and self.current_subchapter_index < len(self.subchapters):
                return self.subchapters[self.current_subchapter_index]
            else:
                return None

        def call_subchapter(self, subchapter_name):
            for i, subchapter in enumerate(self.subchapters):
                if subchapter.name == subchapter_name:
                    self.current_subchapter_index = i
                    renpy.call(subchapter.name)
                    return

        def is_completed(self):
            return all(subchapter.completed for subchapter in self.subchapters)


    def check_and_call_subchapter(chapter, location, tod, game_day, completed_chapters, completed_subchapters):
        for subchapter in chapter.subchapters:
            if subchapter.completed:
                continue
            elif location == L_home_bedroom and tod == "day" and game_day == 0:
                chapter.call_subchapter("introduction")
                return
            elif location == L_home_hallway and tod == "day" and game_day == 1:
                chapter.call_subchapter("conflict")
                return



        if chapter.is_completed():
            chapter.completed = True
            print(f"Chapter {chapter.name} is completed!")