init python:

    class Route:
        def __init__(self, routeName):
            self.routeName = routeName

init python:
    route = Route("Test")
    
    if isinstance(route, Route):
        print(route.routeName)
    else:
        print(f"Expected 'route' to be a Route instance but got {type(route)} instead.")

default money = 50
default newGame = True
default pcBroke = False
default player_name = ""
default landlady_name = "Sharron"
default bedroomDoorLocked = False
default route = 0

define mc = Character("[player_name]")
define mom = Character("[landlady_name]")

label start:

    # Create player name
    $ player_name = renpy.input("What is your name?", length=20, exclude='{}#$%&?¡¿1234567890()_+=\/|[]*^@!~`<>.:;"')
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "MC"


    "Please note this is an early build ([config.version]) of the game, it may contain bugs and unfinished content."

    menu:
        "Please select an option above."

        "New Game":
            jump newgame

        "Cheat":
            jump bedroom

    return

label newgame:
    
    scene black
    with fade

    mc "Another day in this room..."
    mc "It's been six months since Dad left. Six months of wondering why he disappeared."
    mc "If it wasn't for [landlady_name], I'd probably be on the streets right now. She's been amazing, really."

    mc "But I can't keep leeching off her forever. I've got to do something with my life."
    mc "Maybe get a job? Or finally look into going to college? Anything to give me some direction."

    mc "And then there's her daughter... I haven't met her yet. Maybe she's nice?"
    mc "It's weird, though. Living under the same roof for so long without ever crossing paths."
    mc "She's always either in her room or out with friends. Right now, she's on a trip, but she should be back in a couple of days."
    mc "Maybe I'll talk to her then?"

    with dissolve
    mc "Alright, enough moping around. Time to figure things out."

    $ money = 0
    $ bedroomDoorLocked = True

    jump bedroomNew

label route1:

    mc "I should really look on my PC to find a job."

    jump bedroom