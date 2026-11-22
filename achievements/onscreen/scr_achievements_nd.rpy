init -77:

    #Изображения ачивок
    image dv_camp_end_ach           = "mods/notdream/achievements/dv_camp_end_ach.png"
    image running_with_sugar_ach    = "mods/notdream/achievements/running_with_sugar_ach.png"
    image us_sorry_bye_ach          = "mods/notdream/achievements/us_sorry_bye_ach.png"
    image bad_end_ach               = "mods/notdream/achievements/bad_end_ach.png"
    image usrd_end_ach              = "mods/notdream/achievements/usrd_end_ach.png"
    image us_end_ach                = "mods/notdream/achievements/us_end_ach.png"

    #Изображения ачивок на экране
    image achievement_locked        = "mods/notdream/achievements/onscreen/achievement_locked.png"
    image dv_camp_end_scr           = "mods/notdream/achievements/onscreen/dv_camp_end_scr.png"
    image running_with_sugar_scr    = "mods/notdream/achievements/onscreen/running_with_sugar_scr.png"
    image us_sorry_bye_scr          = "mods/notdream/achievements/onscreen/us_sorry_bye_scr.png"
    image bad_end_scr               = "mods/notdream/achievements/onscreen/bad_end_scr.png"
    image usrd_end_scr              = "mods/notdream/achievements/onscreen/usrd_end_scr.png"
    image us_end_scr                = "mods/notdream/achievements/onscreen/us_end_scr.png"

    #Изображения интерфейса экрана
    image achiev_screen_day          = "mods/notdream/achievements/onscreen/achiev_screen_day.jpg"
    image achiev_screen_sunset       = "mods/notdream/achievements/onscreen/achiev_screen_sunset.jpg"
    image achiev_screen_night        = "mods/notdream/achievements/onscreen/achiev_screen_night.jpg"

    image delete_button_ach_idle          = "mods/notdream/achievements/onscreen/delete_button_ach_idle.png"
    image delete_button_ach_hovered       = "mods/notdream/achievements/onscreen/delete_button_ach_hovered.png"

    image back_button_ach_idle          = "mods/notdream/achievements/onscreen/back_button_ach_idle.png"
    image back_button_ach_hovered       = "mods/notdream/achievements/onscreen/back_button_ach_hovered.png"

    image switch_button_right_idle          = "mods/notdream/achievements/onscreen/switch_button_right_idle.png"
    image switch_button_right_hovered       = "mods/notdream/achievements/onscreen/switch_button_right_hovered.png"
    image switch_button_left_idle           = "mods/notdream/achievements/onscreen/switch_button_left_idle.png"
    image switch_button_left_hovered        = "mods/notdream/achievements/onscreen/switch_button_left_hovered.png"

    image stats_screen_day                  = "mods/notdream/achievements/onscreen/stats_screen_day.jpg"
    image stats_screen_sunset               = "mods/notdream/achievements/onscreen/stats_screen_sunset.jpg"
    image stats_screen_night                = "mods/notdream/achievements/onscreen/stats_screen_night.jpg"

    $ nd_achievement_sfx                    = "mods/notdream/UserInterface/Main_menu/nd_achievement_sfx.mp3"

    #Переменные ачивок
    if not persistent.bad_end_ach == True:
        $ persistent.bad_end_ach = False

    if not persistent.running_with_sugar_ach == True:
        $ persistent.running_with_sugar_ach = False

    if not persistent.dv_camp_end_ach == True:
        $ persistent.dv_camp_end_ach = False

    if not persistent.us_sorry_bye_ach == True:
        $ persistent.us_sorry_bye_ach = False

    if not persistent.us_usrd_end_scr == True:
        $ persistent.us_usrd_end_scr = False

    if not persistent.us_us_end_scr == True:
        $ persistent.us_us_end_scr = False

    #Звуки lock/unlock
    $ unlockall_ach = "mods/notdream/achievements/onscreen/ach_us_sounds/unlockall_ach.ogg"
    $ lockall_ach   = "mods/notdream/achievements/onscreen/ach_us_sounds/lockall_ach.ogg"

init -5:

# Функционирование всплывания ачивок

    transform dforg_notdream_trans:
        xalign -0.5 yalign 0.05
        ease 1.0 xalign 0.0 yalign 0.05
        pause 4
        ease 1.0 xalign -0.5 yalign 0.05
        pause 1

    python:
        def notdream_achievment(pic):
            renpy.show(pic, [dforg_notdream_trans], layer="screens")
            renpy.play(nd_achievement_sfx)
#    $ notdream_achievment("achievment_notdream_start")

screen achiev_dm():
    tag menu
    modal True

    #Алиса
    if persistent.dv_camp_end_ach == False:
        imagebutton xpos 0.03 ypos 0.36:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.dv_camp_end_ach == True:
        imagebutton xpos 0.03 ypos 0.36:
            idle ("dv_camp_end_scr")
            hover ("dv_camp_end_scr")
            action [NullAction()]

    #Ульяна проиг.
    if persistent.us_sorry_bye_ach == False:
        imagebutton xpos 0.03 ypos 0.51:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.us_sorry_bye_ach == True:
        imagebutton xpos 0.03 ypos 0.51:
            idle ("us_sorry_bye_scr")
            hover ("us_sorry_bye_scr")
            action [NullAction()]

    #Одиночка
    if persistent.bad_end_ach == False:
        imagebutton xpos 0.03 ypos 0.66:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.bad_end_ach == True:
        imagebutton xpos 0.03 ypos 0.66:
            idle ("bad_end_scr")
            hover ("bad_end_scr")
            action [NullAction()]

    #Бег с сахаром
    if persistent.running_with_sugar_ach == False:
        imagebutton xpos 0.03 ypos 0.81:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.running_with_sugar_ach == True:
        imagebutton xpos 0.03 ypos 0.81:
            idle ("running_with_sugar_scr")
            hover ("running_with_sugar_scr")
            action [NullAction()]

    #Счастье каждому своё
    if persistent.us_usrd_end_scr == False:
        imagebutton xpos 0.26 ypos 0.36:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.us_usrd_end_scr == True:
        imagebutton xpos 0.26 ypos 0.36:
            idle ("usrd_end_scr")
            hover ("usrd_end_scr")
            action [NullAction()]

    #Счастье каждому своё
    if persistent.us_us_end_scr == False:
        imagebutton xpos 0.26 ypos 0.51:
            idle ("achievement_locked")
            hover ("achievement_locked")
            action [NullAction()]

    elif persistent.us_us_end_scr == True:
        imagebutton xpos 0.26 ypos 0.51:
            idle ("us_end_scr")
            hover ("us_end_scr")
            action [NullAction()]


    imagebutton xpos 0.53 ypos 0.838:
        idle ("back_button_ach_idle")
        hover ("back_button_ach_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("close_ach_scr_dm")
            ]

    imagebutton xpos 0.62 ypos 0.838:
        idle ("delete_button_ach_idle")
        hover ("delete_button_ach_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("ach_delete_achievements")
            ]

    imagebutton xpos 0.46 ypos 0.11:
        idle ("switch_button_right_idle")
        hover ("switch_button_right_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("open_stats_scr_dm")
            ]

screen stats_dm():

    tag menu
    modal True

    imagebutton xpos 0.53 ypos 0.838:
        idle ("back_button_ach_idle")
        hover ("back_button_ach_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("close_ach_scr_dm")
            ]

    imagebutton xpos 0.62 ypos 0.838:
        idle ("delete_button_ach_idle")
        hover ("delete_button_ach_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("ach_delete_stats")
            ]

    imagebutton xpos 0.016 ypos 0.11:
        idle ("switch_button_left_idle")
        hover ("switch_button_left_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("switch_stats_scr_dm")
            ]

    button xpos 0.03 ypos 0.36:
        xmaximum 600 ymaximum 100  background "transparent_notdream"
        idle_child Text("Очков морали: " + str(persistent.nd_moral_points), style="nd_calibri_text")
        hover_child Text("Очков морали: " + str(persistent.nd_moral_points), style="nd_calibri_text")
        action [NullAction()]

    button xpos 0.03 ypos 0.43:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text("Танцев с Семёном: " + str(persistent.semen_dancelesson), style="nd_calibri_text")
        hover_child Text("Танцев с Семёном: " + str(persistent.semen_dancelesson), style="nd_calibri_text")
        action [NullAction()]
    
    button xpos 0.03 ypos 0.50:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text("Просмотренных титров: " + str(persistent.nd_seed_titles), style="nd_calibri_text")
        hover_child Text("Просмотренных титров: " + str(persistent.nd_seed_titles), style="nd_calibri_text")
        action [NullAction()]

    button xpos 0.03 ypos 0.57:
        xmaximum 800 ymaximum 100  background "transparent_notdream"
        idle_child Text("Найденных секретов: " + str(nd_completed_secrets) + " из " + str(secrets_points_int), style="nd_calibri_text")
        hover_child Text("Найденных секретов: " + str(nd_completed_secrets) + " из " + str(secrets_points_int) , style="nd_calibri_text")
        action [NullAction()]
