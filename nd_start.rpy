init python:
    
    import os
    import platform 
    import re

init -1999 python:

    userpcname = os.environ.get("USERNAME")

    # Дата, время, сбор информации
    import datetime

    h = int(datetime.datetime.now().strftime("%H"))
    
    res = "night"
    
    if (h >= 6) and (h < 18):
        res = "day"
    if (h >= 18) and (h <= 21): 
        res = "evening"
    if (h >= 22) and (h <= 23):
        res = "night"

label notdream:

    python:
        nd_screens_save_act()
        prolog_time()
        _game_menu_screen = "nd_game_menu_selector"
        
    window hide
    stop sound fadeout 2
    stop music fadeout 2
    stop ambience fadeout 2
        
    scene black:
        subpixel True
        truecenter
        zoom 1.2
        linear 5.0 zoom 1.0
    with dissolve

    $ renpy.movie_cutscene('mods/notdream/UserInterface/nd_enterin.ogv')

    $ volume (1, "ambience") 
    $ volume (1, "music")
    $ volume (1, "sound")
    $ volume (0.4, "ambience")
    $ volume (0.7, "music")
    $ volume (0.2, "nd_ui_sounds") 

label norm_start_nf:

    if res == "day":

        if not persistent.first_start_nd == False:
            $ persistent.nd_f_codeinserted = None
            $ persistent.nd_cursor_style = "normal"
            jump nd_fscr_onnn

        $ nd_change_time('day')

        play ambience ambience_camp_center_day fadein 4
        show ext_house_of_mt_day_razm:
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0

        $ renpy.pause(1.0, hard=True)
        show un_mainmenu_day with dspr
        $ renpy.pause(0.5, hard=True)
        show us_mainmenu_day with dspr

        $ renpy.pause(0.5, hard=True)

        show for_continue_nd with dissolve

        $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999)
        play sound ui_click
        hide for_continue_nd with dissolve

        $ renpy.pause(0.3, hard=True)

        hide un_mainmenu_day with dspr
        hide us_mainmenu_day with dspr
        
        $ renpy.pause(1, hard=True)
        scene bg ext_house_of_mt_day with dissolve
        
        if persistent.music_in_menu == True:
            play music menu_nd_1 fadein 6
        
        $ renpy.pause(1, hard=True)

        scene bg fonmenudreammod_day_1

    if res == "evening":

        if not persistent.first_start_nd == False:
            $ persistent.nd_f_codeinserted = None
            $ persistent.nd_cursor_style = "normal"
            jump nd_fscr_onnn

        $ nd_change_time('sunset')

        play ambience ambience_camp_center_evening fadein 4
        show ext_house_of_mt_sunset_razm:
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0


        $ renpy.pause(1.5, hard=True)

        show dv_mainmenu_evening with dspr

        $ renpy.pause(0.5, hard=True)

        show for_continue_nd with dissolve

        $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999)
        play sound ui_click

        hide for_continue_nd with dissolve

        $ renpy.pause(0.3, hard=True)

        hide dv_mainmenu_evening with dspr
        
        $ renpy.pause(1, hard=True)

        scene bg ext_house_of_mt_sunset with dissolve

        if persistent.music_in_menu == True:
            play music menu_nd_3 fadein 6

        $ renpy.pause(1, hard=True)

        scene bg fonmenudreammod_evening_1

    if res == "night":
        
        if not persistent.first_start_nd == False:
            $ persistent.nd_f_codeinserted = None
            $ persistent.nd_cursor_style = "normal"
            jump nd_fscr_onnn

        $ nd_change_time('night')

        play ambience ambience_camp_entrance_night fadein 4
        show ext_road_night_razm:
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0

        $ renpy.pause(1, hard=True)

        if persistent.music_in_menu == True:
            play music menu_nd_2 fadein 6
        scene bg ext_road_night with dissolve2
            
        $ renpy.pause(1, hard=True)

        scene bg fonmenudreammod_night_1

    show screen graunddm
    show nd_particles
    with dissolve

    if persistent.window_nd == True:
        $ nd_routepoints_window_on()
    else:
        $ nd_routepoints_window_off()

    $ renpy.block_rollback()

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)


label cont_fs_nd:

    $ persistent.first_start_nd = False

    hide screen nd_fsettings 
    hide nd_ui_mainform
    with dissolve

    if res == "day":

        $ renpy.pause(1, hard=True)

        show un_mainmenu_day with dspr
        $ renpy.pause(1, hard=True)
        show us_mainmenu_day with dspr

        $ renpy.pause(1, hard=True)

        show for_continue_nd with dissolve

        $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999)
        play sound ui_click
        hide for_continue_nd with dissolve

        $ renpy.pause(1, hard=True)

        hide un_mainmenu_day with dspr
        hide us_mainmenu_day with dspr
        
        $ renpy.pause(1, hard=True)
        scene bg ext_house_of_mt_day with dissolve
        
        if persistent.music_in_menu == True:
            play music menu_nd_1 fadein 6
        
        $ renpy.pause(1.5, hard=True)

        scene bg fonmenudreammod_day_1

    if res == "evening":

        $ renpy.pause(1, hard=True)

        show dv_mainmenu_evening with dspr

        $ renpy.pause(1, hard=True)

        show for_continue_nd with dissolve

        $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999)
        play sound ui_click

        hide for_continue_nd with dissolve

        $ renpy.pause(1, hard=True)

        hide dv_mainmenu_evening with dspr
        
        $ renpy.pause(1, hard=True)
        scene bg ext_house_of_mt_sunset with dissolve

        if persistent.music_in_menu == True:
            play music menu_nd_3 fadein 6

        $ renpy.pause(1.5, hard=True)

        scene bg fonmenudreammod_evening_1

    if res == "night":

        $ renpy.pause(1.5, hard=True)

        show for_continue_nd with dissolve

        $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999)
        play sound ui_click

        hide for_continue_nd with dissolve

        $ renpy.pause(1, hard=True)
        scene bg ext_road_night with dissolve

        if persistent.music_in_menu == True:
            play music menu_nd_2 fadein 6
            
        $ renpy.pause(1.5, hard=True)

        scene bg fonmenudreammod_night_1
        
    show screen graunddm
    show nd_particles
    with dissolve

    $ renpy.block_rollback()
    
    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

