label player_bedroom:
    $ player.location = L_home_bedroom
    scene expression get_background(player.location, persistent.time_of_day)
    $ game.main()

label home_hallway:
    $ player.location = L_home_hallway
    scene expression get_background(player.location, persistent.time_of_day)
    $ game.main()

label home_entrance:
    $ player.location = L_home_entrance
    scene expression get_background(player.location, persistent.time_of_day)
    $ game.main()