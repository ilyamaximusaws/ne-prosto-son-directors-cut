label showing_nd_part_screen:

    # if res == "day":
    #     hide screen graunddm
    #     show bg ext_house_of_mt_day
    #     with dissolve

    # if res == "evening":
    #     hide screen graunddm
    #     show bg ext_house_of_mt_sunset
    #     with dissolve
    # if res == "night":
    #     hide screen graunddm
    #     scene bg ext_road_night
    #     with dissolve

    stop music fadeout 2
    stop ambience fadeout 2
    hide screen graunddm
    hide bg fonmenudreammod_day_1
    hide bg fonmenudreammod_evening_1
    hide bg fonmenudreammod_night_1
    hide nd_particles1
    hide nd_particles
    scene black 
    with nd_effect_5_reverse
    $ renpy.pause(0.5, hard=True)
    play ambience nda_list['rain_outside'] fadein 3
    scene chapter_1_bg with nd_effect_5_reverse
    show chapter_1_screen with nd_effect_5_reverse
    show screen parts_nd_screen with dissolve
    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label hiding_nd_part_screen:

    stop ambience fadeout 2

    if res == "day":
        hide screen parts_nd_screen2
        hide screen parts_nd_screen
        scene black 
        with nd_effect_5
    
    if res == "evening":
        hide screen parts_nd_screen2
        hide screen parts_nd_screen
        scene black 
        with nd_effect_5

    if res == "night":
        hide screen parts_nd_screen2
        hide screen parts_nd_screen
        scene black 
        with nd_effect_5
    
    $ renpy.pause(0.5, hard=True)

    if res == "day":

        play ambience ambience_camp_center_day fadein 4
        if persistent.music_in_menu == True:
            play music menu_nd_1 fadein 4
        scene bg fonmenudreammod_day_1

    if res == "evening":
        play ambience ambience_camp_center_evening fadein 4
        if persistent.music_in_menu == True:
            play music menu_nd_3 fadein 4
        scene bg fonmenudreammod_evening_1

    if res == "night":
        if persistent.music_in_menu == True:
            play music menu_nd_2 fadein 4
        play ambience ambience_camp_entrance_night fadein 4
        scene bg fonmenudreammod_night_1

    show screen graunddm
    show nd_particles
    with nd_effect_5

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label turn_1_part_of_my_mod_notdream:
    stop ambience fadeout 2
    hide screen parts_nd_screen
    show black
    with dissolve_fast
    jump notdream_prolog_d1

label turn_2_part_of_my_mod_notdream:
    stop ambience fadeout 2
    hide screen parts_nd_screen2
    show black
    with dissolve_fast
    jump nd_official_p2_start

label enable_two_part_nd_selector:
    stop ambience fadeout 2
    hide screen parts_nd_screen
    scene black
    with nd_effect_5_reverse
    $ renpy.pause(0.3, hard=True)
    play ambience nda_list['nd_groove_night'] fadein 3
    scene chapter_2_bg with nd_effect_5_reverse
    show chapter_2_screen with nd_effect_5_reverse
    show screen parts_nd_screen2 with dissolve
    $ renpy.pause(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label enable_one_part_nd_selector:
    stop ambience fadeout 2
    hide screen parts_nd_screen2
    scene black
    with nd_effect_5
    $ renpy.pause(0.3, hard=True)
    play ambience nda_list['rain_outside'] fadein 3
    scene chapter_1_bg with nd_effect_5
    show chapter_1_screen with nd_effect_5_reverse
    show screen parts_nd_screen 
    with dissolve
    $ renpy.pause(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, hard=True)