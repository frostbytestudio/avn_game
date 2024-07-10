
screen age_prompt():

    vbox:
        frame:
            style_prefix "age_prompt"
            vbox:
                text "This game is {color=#f00}rated 18+{/color}, thus containing explicit sexual content."
                text "All characters depicted in this game is of the age 18 or older."
                text "Any themes and ideas depicted in this game is of fiction and any"
                text "actual act of sexual abuse is not encouraged under any circumstances."

        vbox:
            style_prefix "age_confirm"
            text "Do you understand and wish to continue?"

            hbox:
                textbutton "Yes" action Return()
                textbutton "No" action Quit(confirm=False)

style age_prompt_text:
    font "fonts/Righteous-Regular.ttf"
    color "#ccc"
    size 24
    xalign 0.5

style age_prompt_frame:
    pos (.13, 250)

style age_confirm_vbox:
    pos (.33, 300)

style age_confirm_text:
    font "fonts/Righteous-Regular.ttf"
    color "#ccc"
    size 24
    xalign 0.5

style age_confirm_hbox:
    pos (.4, 10)
    spacing 10