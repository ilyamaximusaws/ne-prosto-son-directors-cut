screen nd_fake_mainmenu:
    
    tag nd_fake_mainmenu
    modal True

    imagemap:
        if _preferences.language == "spanish":
            auto "images/gui/title_menu/mainmenu_es_%s.jpg"
        elif _preferences.language == "italian":
            auto "images/gui/title_menu/mainmenu_it_%s.jpg"
        elif _preferences.language == "english":
            auto "images/gui/title_menu/mainmenu_en_%s.jpg"
        elif _preferences.language == "chinese":
            auto "images/gui/title_menu/mainmenu_ch_%s.jpg"
        else:
            auto "images/gui/title_menu/mainmenu_%s.jpg"
        hotspot (439,265,318,621) clicked Jump("nd_vlad_eat_pizza")
        hotspot (787,261,270,537) clicked Jump("nd_vlad_eat_pizza")
        hotspot (1067,748,252,312) clicked Jump("nd_vlad_eat_pizza")
        hotspot (1083,258,229,538) clicked Jump("nd_vlad_eat_pizza")
        hotspot (1459,532,149,295) clicked Jump("nd_vlad_eat_pizza") hovered Play("test_one", "sound/sfx/menu_gate.ogg")
        hotspot (494, 125,  768, 86) clicked Jump("nd_vlad_eat_pizza")
        if config.developer:
            hotspot (1578,953,342,127) clicked Jump("nd_vlad_eat_pizza")
    if True in persistent.endings.values():
        imagebutton auto "images/gui/title_menu/owl_%s.png" xpos 135 ypos 606 action Jump("nd_vlad_eat_pizza") hovered Play("test_two", "sound/test.ogg")

    button style "soviet_button" pos (0.89,0.85) action Jump("nd_vlad_eat_pizza")

label nd_vlad_eat_pizza:
    
    hide screen nd_fake_mainmenu

    stop music
    show black
    play movie "mods/notdream/images/bg/dv_r/videoplayback.ogv" loop
    show movie

    $ renpy.pause(52, hard=True)

    hide movie
    stop movie

    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show text "{size=32}Будь крепок, анон!{/size=32}" with dissolve
    $ renpy.pause(5, hard=True)

    if persistent.papich_nd == 0:
        $ persistent.papich_nd = 1
        $ nd_completed_secrets += 1
        
    $ persistent.fall_stair_bunker = 0

    return