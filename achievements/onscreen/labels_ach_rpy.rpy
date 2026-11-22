label open_ach_scr_dm:
    hide screen graunddm
    show black
    with dissolve

    if res == "day":
        scene achiev_screen_day

    if res == "evening":
        scene achiev_screen_sunset

    if res == "night": 
        scene achiev_screen_night

    show screen achiev_dm
    with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label close_ach_scr_dm:

    hide screen stats_dm
    hide screen achiev_dm
    show black
    with dissolve

    if res == "day":
        scene bg fonmenudreammod_day_1

    if res == "evening":
        scene bg fonmenudreammod_evening_1

    if res == "night": 
        scene bg fonmenudreammod_night_1

    show screen graunddm
    show nd_particles as nd_particles1
    with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label ach_delete_achievements:

    show black
    hide screen achiev_dm
    with dissolve
    menu:
        "Вы действительно хотите сбросить ваши достижения?"
    
        "Да":
    
            $ persistent.dv_camp_end_ach = False

            $ persistent.running_with_sugar_ach = False
    
            $ persistent.us_sorry_bye_ach = False
            
            $ persistent.bad_end_ach = False

            $ persistent.us_usrd_end_scr = False

            $ renpy.pause(1, hard=True)

            play sound lockall_ach

            window show
            "Ваши достижения были сброшены. Приятной игры."
            window hide

            hide black
            show screen achiev_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)


        "Нет":
            hide black
            show screen achiev_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label ach_delete_stats:

    show black
    hide screen stats_dm
    with dissolve
    menu:
        "Вы действительно хотите обнулить вашу статистику?"
    
        "Да":
            $ persistent.semen_dancelesson = 0
            $ persistent.nd_moral_points = 0
            $ persistent.nd_seed_titles = 0
            $ persistent.papich_nd = 0
            $ nd_complited_secrets = 0
            $ renpy.pause(1, hard=True)

            play sound lockall_ach

            window show
            "Ваша статистика обнулена. Приятной игры."
            window hide

            hide black
            show screen stats_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)


        "Нет":
            hide black
            show screen stats_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label unlock_all_achievements:

    show black
    hide screen achiev_dm
    with dissolve

    "Если вы НЕ РАЗРАБОТЧИК и видите это - сообщите об этом разработчику модификации."
    
    menu:

        "Open all achievements?"
        
        "Yup":
    
            $ persistent.dv_camp_end_ach = True

            $ persistent.running_with_sugar_ach = True
    
            $ persistent.us_sorry_bye_ach = True

            $ persistent.bad_end_ach = True
            
            $ renpy.pause(1, hard=True)

            play sound unlockall_ach

            window show
            "All achievements are now open."
            window hide
            
            hide black
            show screen achiev_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)


        "No":
            hide black
            show screen achiev_dm
            with dissolve

            $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label open_stats_scr_dm:

    if res == "day":
        hide achiev_screen_day
        hide screen achiev_dm
        scene stats_screen_day
        show screen stats_dm
        with dissolve

    if res == "evening":
        hide achiev_screen_sunset
        hide screen achiev_dm
        scene stats_screen_sunset
        show screen stats_dm
        with dissolve

    if res == "night": 
        hide achiev_screen_night
        hide screen achiev_dm
        scene stats_screen_night
        show screen stats_dm
        with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label switch_stats_scr_dm:

    if res == "day":
        hide stats_screen_day
        hide screen stats_dm
        scene achiev_screen_day
        show screen achiev_dm
        with dissolve

    if res == "evening":
        hide stats_screen_sunset
        hide screen stats_dm
        scene achiev_screen_sunset
        show screen achiev_dm
        with dissolve

    if res == "night":
        hide stats_screen_night
        hide screen stats_dm
        scene achiev_screen_night
        show screen achiev_dm
        with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)