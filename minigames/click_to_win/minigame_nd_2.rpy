init 15 python:
    nd_minigame_bar = 90
    nd_minigame_score = 0
    nd_you_press_button = 0
init:
    transform nd_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,1.22)
        rotate frp

    image nd_minigame_2_tip = "mods/notdream/minigames/click_to_win/minigame_2_tip.png"

screen nd_2_minigame:
    add "mods/notdream/minigames/click_to_win/nd_bar.png" align(0.5,0.5)
    add "mods/notdream/minigames/click_to_win/nd_point.png" at nd_point_move(nd_minigame_bar)
    #text "[nd_minigame_score]\nКоличество нажатий" align(0.5,0.1)
    #text "[nd_minigame_bar]\nЗначение бара" align(0.5,0.2)
    text "[nd_you_press_button]" align(0.5,0.3)

    if nd_minigame_bar >= -14 and nd_minigame_bar <= 14:
        key "K_SPACE":
            if nd_you_press_button == 0:
                if nd_minigame_score < 1:
                    action [SetVariable("nd_minigame_score", nd_minigame_score + 1), SetVariable("nd_you_press_button", nd_you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("nd_end_clicktowin")
            elif nd_you_press_button == 1:
                action SetVariable("nd_minigame_score", nd_minigame_score + 0)
    else:
        key "K_SPACE" action [SetVariable("nd_minigame_score", 0), Show("you_press_button_bad")]

screen nd_timer_left:
    timer 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 repeat True action [If(nd_minigame_bar >= -90, SetVariable("nd_minigame_bar", nd_minigame_bar - 1)),If(nd_minigame_bar == -90, Hide("nd_timer_left"), Show("nd_timer_right")), If(nd_minigame_bar == -90, SetVariable("nd_you_press_button", 0))]
screen nd_timer_right:
    timer 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001 repeat True action [If(nd_minigame_bar <= 90, SetVariable("nd_minigame_bar", nd_minigame_bar + 1)),If(nd_minigame_bar == 90, Hide("nd_timer_right"), Show("nd_timer_left")), If(nd_minigame_bar == 90, SetVariable("nd_you_press_button", 0))]

screen you_press_button_good:
    text "{color=#1e8e00}Хорошая работа!{/color}" at nd_move_good
    timer 1.0 action Hide("you_press_button_good")
screen you_press_button_bad:
    #hbox at nd_move_bad:
    text "{color=#950000}Промах!{/color}" at nd_move_bad
    timer 1.0 action Hide("you_press_button_bad")
transform nd_move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0
transform nd_move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0
################################################################################
label nd_start_clicktowin:
    show nd_minigame_2_tip with dissolve
    show screen nd_timer_left
    $ renpy.transition(dissolve)
    $ renpy.call_screen('nd_2_minigame', dissolve)
    #call screen nd_2_minigame
################################################################################
label nd_end_clicktowin: #End minigame. And jump continue game
    hide nd_minigame_2_tip
    hide screen nd_2_minigame
    hide screen nd_timer_left
    hide screen nd_timer_right
    with dissolve
    $ renpy.pause(0.3)
