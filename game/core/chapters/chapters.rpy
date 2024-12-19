label conflict:
    
    if not chapter1.current_subchapter().completed:
        show home hallway blur with dissolve
        show roommate_daughter norm with dissolve

        liz "This is the conflict subchapter!"
        
        $ chapter1.current_subchapter().completed = True
    return

label resolution:
    
    if not chapter1.current_subchapter().completed:
        e "This is the resolution subchapter!"
        $ chapter1.current_subchapter().completed = True
    
    if chapter1.is_completed():
        $ chapter1.completed = True
        $ player.completed_chapters.append(chapter1.name)
        e "Chapter 1 is now complete!"
    return

label intro2:
    
    if not chapter2.current_subchapter().completed:
        e "This is the Intro 2 to Chapter 2!"
        $ chapter2.current_subchapter().completed = True
    return