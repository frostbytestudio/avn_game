label player_bedroom:
    $ player.location = L_home_bedroom
    scene expression get_background(player.location, day_timer.current_tod)
    #$ check_and_call_subchapter(chapter1, player.location, persistent.time_of_day, gameDay, player.completed_chapters, player.completed_subchapters)
    $ game.main()

label home_hallway:
    $ player.location = L_home_hallway
    scene expression get_background(player.location, day_timer.current_tod)
    #$ check_and_call_subchapter(chapter1, player.location, persistent.time_of_day, gameDay, player.completed_chapters, player.completed_subchapters)
    $ game.main()