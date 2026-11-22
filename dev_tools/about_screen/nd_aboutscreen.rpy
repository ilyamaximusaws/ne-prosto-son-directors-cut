init:

    image bg nd_rain_window         = "mods/notdream/dev_tools/about_screen/nd_rain_window.png"
    image nd_about_modif            = "mods/notdream/dev_tools/about_screen/nd_about_modif.jpg"
    
    image nd_creators_button_hover  = "mods/notdream/dev_tools/about_screen/nd_creators_button_hover.png"
    image nd_creators_button_idle   = "mods/notdream/dev_tools/about_screen/nd_creators_button_idle.png"

    image nd_devmode_on             = "mods/notdream/dev_tools/about_screen/nd_devmode_on.png"

    image nd_goto_workshop_hover    = "mods/notdream/dev_tools/about_screen/nd_goto_workshop_hover.png"
    image nd_goto_workshop_idle     = "mods/notdream/dev_tools/about_screen/nd_goto_workshop_idle.png"

    image nd_about_template         = "mods/notdream/dev_tools/about_screen/nd_about_template.png"

    image nd_about_exit_idle        = "mods/notdream/dev_tools/about_screen/nd_about_exit_idle.png"
    image nd_about_exit_hover       = "mods/notdream/dev_tools/about_screen/nd_about_exit_hover.png"

screen nd_about_modif_screen:
    modal True

    imagebutton xpos 1157 ypos 639:
        idle ("nd_goto_workshop_idle")
        hover ("nd_goto_workshop_hover")
        action [
            Play('nd_ui_sounds', ui_click),
            OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=2474902261")
            ]

    button xpos 1150 ypos 750:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text("Версия: " + str(persistent.nd_ver), style="nd_helvuelight")
        hover_child Text("Версия: " + str(persistent.nd_ver), style="nd_helvuelight")
        action [NullAction()]

    button xpos 1200 ypos 800:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text("База: " + str(persistent.es_ver), style="nd_helvuelight")
        hover_child Text("База: " + str(persistent.es_ver), style="nd_helvuelight")
        action [NullAction()]

    button xpos 1250 ypos 850:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text(nd_devmenu_text, style="nd_helvuelight")
        hover_child Text(nd_devmenu_text, style="nd_helvuelight")
        action [NullAction()]

    imagebutton xpos 1507 ypos 639:
        idle ("nd_creators_button_idle")
        hover ("nd_creators_button_hover")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("credits_aboutmodif")
            ]

    imagebutton xpos 1474 ypos 338:
        idle ("nd_about_exit_idle")
        hover ("nd_about_exit_hover")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("nd_exit_aboutmodif")
            ]

label nd_start_aboutmodif:

    show nd_about_template
    show screen nd_about_modif_screen
    with dissolve
    $ renpy.pause(99999999999999999999999999999999999999999999999999, hard=True)

label nd_exit_aboutmodif:
    
    hide nd_about_template
    hide screen nd_about_modif_screen
    with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label nd_start_aboutmodif_titles:

    if res == "day":
        scene bg fonmenudreammod_day_1
        if persistent.music_in_menu == True:
            play music menu_nd_1 fadein 6
    if res == "evening":
        scene bg fonmenudreammod_evening_1
        if persistent.music_in_menu == True:
            play music menu_nd_3 fadein 6
    if res == "night":
        scene bg fonmenudreammod_night_1
        if persistent.music_in_menu == True:
            play music menu_nd_2 fadein 6

    show screen graunddm
    show nd_particles as nd_particles1
    show nd_about_template
    show screen nd_about_modif_screen
    with dissolve2
    $ renpy.pause(99999999999999999999999999999999999999999999999999, hard=True)

label credits_aboutmodif:

    show black 
    hide screen graunddm
    hide screen nd_about_modif_screen
    with dissolve2
    stop music fadeout 2
    stop ambience fadeout 2
    stop sound fadeout 2
    
    $ renpy.pause(1, hard=True)
    jump nd_fict_endscr_titles
#    play music ndm_list['the_most_musterious_song_on_the_internet'] fadein 4
#
#    show credits nd_credits_us:
#        xalign 0.5 
#        ypos 1.3
#        linear 90.0 ypos -3.0
#                
#    $ renpy.pause(90)
#    scene black with dissolve
#    stop music fadeout 3
#    $ renpy.pause(3, hard=True)
#    jump nd_fict_endscr_titles
#    jump nd_start_aboutmodif_titles