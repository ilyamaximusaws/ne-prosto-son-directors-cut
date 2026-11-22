screen nd_say:
    window:
        background None
        id "window"
        $ timeofday = persistent.timeofday
        if persistent.font_size == "large":
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/backward_%s.png")
                xpos 20
                ypos 908
                action ShowMenu("text_history")
            add ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/dialogue_box_large.png"):
                xpos 169
                ypos 866
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/hide_%s.png")
                xpos 1508
                ypos 890
                action HideInterface()
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/save_%s.png")
                xpos 1567
                ypos 890
                action ShowMenu('save')
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/menu_%s.png")
                xpos 1625
                ypos 890
                action ShowMenu('game_menu_selector')
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/load_%s.png")
                xpos 1682
                ypos 890
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/forward_%s.png")
                    xpos 1755
                    ypos 908
                    action Skip()
            else:
                imagebutton:
                    auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/fast_forward_%s.png")
                    xpos 1755
                    ypos 908
                    action Skip()
            text what:
                id "what"
                xpos 198
                ypos 928
                xmaximum 1530
                font als_sirius_v3
                size 30
                style als_sirius_v3
                line_spacing 2
                if persistent.timeofday == "prologue":
                    color "#F2F2F2"
                elif persistent.timeofday == "day":
                    color "#F2F2F2"
                elif persistent.timeofday == "sunset":
                    color "#F2F2F2"
                elif persistent.timeofday == "night":
                    color '#F2F2F2'#"#F2F2F2"

            if who:
                text who:
                    id "who"
                    xpos 203
                    ypos 888
                    font als_sirius_v3
                    size 30
                    line_spacing 2

        elif persistent.font_size == "small":
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/backward_%s.png")
                xpos 20
                ypos 928
                action ShowMenu("text_history")
            add ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/dialogue_box.png"):
                xpos 129
                ypos 905
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/hide_%s.png")
                xpos 1526
                ypos 935
                action HideInterface()
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/save_%s.png")
                xpos 1585
                ypos 935
                action ShowMenu('save')
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/menu_%s.png")
                xpos 1643
                ypos 935
                action ShowMenu('game_menu_selector')
            imagebutton:
                auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/load_%s.png")
                xpos 1700
                ypos 935
                action ShowMenu('load')
            if not config.skipping:
                imagebutton:
                    auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/forward_%s.png")
                    xpos 1758
                    ypos 928
                    action Skip()
            else:
                imagebutton:
                    auto ("mods/notdream/UserInterface/gui/dialogue_box/"+timeofday+"/fast_forward_%s.png")
                    xpos 1755
                    ypos 928
                    action Skip()
            text what:
                id "what"
                xpos 180
                ypos 968
                xmaximum 1550
                font als_sirius_v3
                size 25.5
                if persistent.timeofday == "prologue":
                    color "#F2F2F2"
                elif persistent.timeofday == "day":
                    color "#F2F2F2"
                elif persistent.timeofday == "sunset":
                    color "#F2F2F2"
                elif persistent.timeofday == "night":
                    color '#F2F2F2'#"#F2F2F2"
                line_spacing 2
            if who:
                text who:
                    id "who"
                    xpos 190
                    ypos 933
                    font als_sirius_v3
                    size 25.5
                    line_spacing 2


screen nd_game_menu_selector:
    tag menu
    modal True

    $ nd_music_is_play = renpy.music.is_playing(channel='music')
    $ timeofday = persistent.timeofday
    $ time_of_day = persistent.timeofday

    button:
        style "blank_button"
        xalign 0
        yalign 0
        xfill True
        yfill True
        action Return()

    add "mods/notdream/UserInterface/gui/quick_menu/"+timeofday+"/quick_menu.png":
        xalign 0.5
        yalign 0.5

    vbox align(0.95, 0.38):
        xsize 410
        ysize 100
        
        hbox align (0.5, 0.5):
            text "{size=22}Время,{/size}":
                xalign 0.5
                style 'helveticaneueroman_idle'
        
        hbox align (0.5, 0.5):
            text "{size=22}Проведенное в игре:{/size}":
                xalign 0.5
                style 'helveticaneueroman_idle'

        hbox align(0.5, 0.5):
            add "nd_gametime" align(.90, .38)

    if nd_music_is_play:
        add "mods/notdream/UserInterface/gui/quick_menu/nd_shazam.png" align(.96,.55)

        vbox align(0.94, 0.58):
            xsize 400
            ysize 100
        
            hbox align (0.04, 0.45):
                text "{size=22}Сейчас играет:{/size}":
                    xalign 0.55
                    style 'helveticaneueroman_idle'

            hbox align(0.05, 0.16):
                add 'nd_game_music' align(.94,.55)

    #add 'nd_game_music' align(.94,.55)

    imagebutton xpos 1434 ypos 728:
        idle ("mods/notdream/UserInterface/gui/quick_menu/day/main_menu_idle.png")
        hover ("mods/notdream/UserInterface/gui/quick_menu/day/main_menu_hover.png")
        action [
            Jump('nd_true_exit'),
            ]

    imagebutton xpos 1589 ypos 913:
        idle ("mods/notdream/UserInterface/gui/quick_menu/day/save_idle.png")
        hover ("mods/notdream/UserInterface/gui/quick_menu/day/save_hover.png")
        action[
            ShowMenu('nd_Save')
            ]

    imagebutton xpos 1728 ypos 913:
        idle ("mods/notdream/UserInterface/gui/quick_menu/day/load_idle.png")
        hover ("mods/notdream/UserInterface/gui/quick_menu/day/load_hover.png")
        action[
            ShowMenu('nd_Load2')
            ]

    imagebutton xpos 1465 ypos 913:
        idle ("mods/notdream/UserInterface/gui/quick_menu/day/preferences_idle.png")
        hover ("mods/notdream/UserInterface/gui/quick_menu/day/preferences_hover.png")
        action[
            ShowMenu('nd_preferences2')
            ]

    imagebutton xpos 1404 ypos 280:
        idle ("mods/notdream/UserInterface/gui/quick_menu/day/quit_idle.png")
        hover ("mods/notdream/UserInterface/gui/quick_menu/day/quit_hover.png")
        action[
            ShowMenu('nd_exit_yes_no')
            ]

screen nd_Load:
    tag menu
    modal True
    window:
        add "mods/notdream/UserInterface/gui/Load/nd_load_menu_osn.png":
            xpos -4
            ypos -4
        text "{font=[nd_Script]}ЗАГРУЗКИ{/font}":
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.007
            antialias True
            kerning 2

        textbutton ["ЗАГРУЗИТЬ ИГРУ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            ypos 0.92
            xalign 0.5
            action [Play('nd_ui_sounds', ui_click), 
            (nd_FunctionCallback(nd_on_load_callback,selected_slot), FileLoad(selected_slot))]

        textbutton ["УДАЛИТЬ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 1555
            ypos 970
            action [Play('nd_ui_sounds', ui_click), 
            FileDelete(selected_slot)]

        textbutton ["НАЗАД"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 235
            ypos 970
            action [Play('nd_ui_sounds', ui_click),
                Jump("nd_activate_screen_mainmenu")
                ]

        vbox:
            xalign 0.023
            yalign 0.5
            grid 1 10:
                textbutton "A":
                    right_padding 55
                    text_size 50
                    xpos 32
                    style "nd_button_None"
                    text_style "nd_text_small_save_load"
                    action (FilePage("auto"), SetVariable("selected_slot", False))
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 50
                        xpos 32
                        style "nd_button_None"
                        text_style "nd_text_small_save_load"
                        action (FilePage("nd_FilePage_"+ str(i)), SetVariable("selected_slot", False))

        
        grid 4 3:
            xpos 0.13
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "nd_save_load_button"
                        fixed:
                            text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                + "\n" +FileSaveName(i)):
                                    style "nd_save_load_button"
                                    xpos 15
                                    ypos 15

screen nd_Save:
    tag menu
    modal True
    window:
        add "mods/notdream/UserInterface/gui/Load/nd_load_menu_osn.png":
            xpos -4
            ypos -4
        text "{font=[nd_Script]}СОХРАНЕНИЯ{/font}":
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.007
            antialias True
            kerning 2
        
        textbutton ["СОХРАНИТЬ ИГРУ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            ypos 0.92
            xalign 0.5
            action [Play('nd_ui_sounds', ui_click), 
            (nd_FunctionCallback(nd_on_save_callback, selected_slot), FileSave(selected_slot))]

        textbutton ["УДАЛИТЬ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 1555
            ypos 970
            action [Play('nd_ui_sounds', ui_click), 
            FileDelete(selected_slot)]

        textbutton ["НАЗАД"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 235
            ypos 970
            action [Play('nd_ui_sounds', ui_click),
                ShowMenu('nd_game_menu_selector')
                ]

        vbox:
            xalign 0.023
            yalign 0.5
            grid 1 10:
                textbutton "A":
                    right_padding 55
                    text_size 50
                    xpos 32
                    style "nd_button_None"
                    text_style "nd_text_small_save_load"
                    action (FilePage("auto"), SetVariable("selected_slot", False))
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 50
                        xpos 32
                        style "nd_button_None"
                        text_style "nd_text_small_save_load"
                        action (FilePage("nd_FilePage_"+ str(i)), SetVariable("selected_slot", False))

        grid 4 3:
            xpos 0.13
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "nd_save_load_button"
                        fixed:
                            text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                + "\n" +FileSaveName(i)):
                                    style "nd_save_load_button"
                                    xpos 15
                                    ypos 15

screen nd_Load2:
    tag menu
    modal True
    window:
        add "mods/notdream/UserInterface/gui/Load/nd_load_menu_osn.png":
            xpos -4
            ypos -4
        text "{font=[nd_Script]}ЗАГРУЗКИ{/font}":
            size 100
            text_align 0.5
            xalign 0.5
            yalign 0.007
            antialias True
            kerning 2

        textbutton ["ЗАГРУЗИТЬ ИГРУ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            ypos 950
            xalign 0.5
            action [(nd_FunctionCallback(nd_on_load_callback,selected_slot), FileLoad(selected_slot)),
            Play('nd_ui_sounds', ui_click)] 

        textbutton ["УДАЛИТЬ"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 1555
            ypos 970
            action [FileDelete(selected_slot),
            Play('nd_ui_sounds', ui_click)] 

        textbutton ["НАЗАД"]:
            text_style "nd_text_big_save_load"
            style "nd_button_None"
            xpos 235
            ypos 970
            action [Play('nd_ui_sounds', ui_click),
            ShowMenu("nd_game_menu_selector")]
             

        vbox:
            xalign 0.023
            yalign 0.5
            grid 1 10:
                textbutton "A":
                    right_padding 55
                    text_size 50
                    xpos 32
                    style "nd_button_None"
                    text_style "nd_text_small_save_load"
                    action (FilePage("auto"), SetVariable("selected_slot", False))
                for i in range(1, 10):
                    textbutton str(i):
                        right_padding 55
                        text_size 50
                        xpos 32
                        style "nd_button_None"
                        text_style "nd_text_small_save_load"
                        action (FilePage("nd_FilePage_"+ str(i)), SetVariable("selected_slot", False))
        
        grid 4 3:
            xpos 0.13
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):
                fixed:
                    add FileScreenshot(i):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "nd_save_load_button"
                        fixed:
                            text ( "%s." % i
                                + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation["Empty_slot"][_preferences.language])
                                + "\n" +FileSaveName(i)):
                                    style "nd_save_load_button"
                                    xpos 15
                                    ypos 15

screen nd_exit_yes_no:
    tag menu
    modal True

    add "/mods/notdream/UserInterface/exit_bg.jpg":
        xpos 0
        ypos 0
    
    text 'Ты вновь хочешь уйти?':
        style "nd_text_big_save_load"
        size 120
        drop_shadow [(2, 1)]
        color "#ffffff"
        text_align 0.5
        align(0.5,0.5)
        pos(1300, 372)
        antialias True
        kerning 2

    textbutton "Да":
        style "nd_text_big_save_load"
        text_style "nd_text_big_save_load"
        text_color "#ff0000"
        text_hover_color "#cc0000"
        align(0.5,0.5)
        pos(1006, 588)
        action Quit(confirm=False)

    textbutton "Нет":
        style "nd_text_big_save_load"
        text_style "nd_text_big_save_load"
        text_color "#ff0000"
        text_hover_color "#cc0000"
        align(0.5,0.5)
        pos(1566, 588)
        action ShowMenu('nd_game_menu_selector')


screen nd_preferences:
    
    tag menu
    modal True

    add "mods/notdream/UserInterface/gui/Preference/nd_preference_osn.png"
    
    imagebutton:
        xpos 163 ypos 935
        idle ("mods/notdream/UserInterface/gui/Preference/nd_back_preference_idle.png")
        hover ("mods/notdream/UserInterface/gui/Preference/nd_back_preference_hover.png")
        action [Play('nd_ui_sounds', ui_click),
        Jump("end_nd_prefs")]

    hbox:
        spacing 20 # Расстояние, между баром и боксом.
        xsize 800 # Размер, дабы не растекалось по всему экрану.
        ysize 600
        align (.17, .5)

        viewport id "nd_v_prefrences_1": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
            xfill True
            yfill False
            mousewheel True # Разрешаем прокрутку мышью.

            vbox:
                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_rezim_osn.png"# xpos 164 ypos 542

                    if not _preferences.fullscreen:
                        imagebutton:
                            #xpos 718 ypos 544
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (Preference("display", "fullscreen"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 544
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (Preference("display", "window"))

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_prefs_skip_unseen.png"# xpos 164 ypos 344

                    if not _preferences.skip_unseen:
                        imagebutton:
                            #xpos 718 ypos 346
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (Preference("skip", "all"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 346
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (Preference("skip", "seen"))

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_18_content.png"# xpos 164 ypos 248

                    if persistent.window_nd == True:
                        imagebutton:
                            #xpos 718 ypos 250
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action [
                                Function(nd_routepoints_window_off)
                                ]
                    else:   
                        imagebutton:
                            #xpos 718 ypos 250
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
                            action [
                                Function(nd_routepoints_window_on)
                                ]
                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_autosave_title.png" #xpos 164 ypos 440
                    if persistent.autosave_unlocker == True:
                        imagebutton:
                            #xpos 718 ypos 442
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
                            action [
                                    SetVariable("persistent.autosave_unlocker", False),
                                    SetVariable("config.has_autosave", False),
                                    SetVariable("config.autosave_frequency", None),
                                    SetVariable("config.autosave_on_choice", False) 
                                    ]
                    else:
                        imagebutton:
                            #xpos 718 ypos 442
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
                            action [
                                    SetVariable("persistent.autosave_unlocker", True),
                                    SetVariable("config.has_autosave", True),
                                    SetVariable("config.autosave_frequency", 300),
                                    SetVariable("config.autosave_on_choice", False) 
                                    ]

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_cursorstyle_title.png" #xpos 164 ypos 748

                    if persistent.nd_cursor_style == "normal":
                        imagebutton:
                            #xpos 718 ypos 748
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action [
                                    SetVariable("config.mouse_displayable", MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_prologue_v2.png', 30, 30)),
                                    SetVariable("persistent.nd_cursor_style", "circle"),
                                    ]
                    else:
                        imagebutton:
                            #xpos 718 ypos 748
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
                            action [
                                    SetVariable("config.mouse_displayable", MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_prologue_v2.png', 0, 0)),
                                    SetVariable("persistent.nd_cursor_style", "normal"),
                                    ]

                null width 15 height 40

                grid 2 1 xfill True: #(This example of grid only has 2 line and 1 rows, so a total of 1 items can be placed in it)
                    add "mods/notdream/UserInterface/gui/Preference/nd_razmer_menu.png" #xpos 164 ypos 646
                    if persistent.font_size == "small":
                        imagebutton:
                            #xpos 718 ypos 646
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (SetField(persistent, "font_size", "large"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 646
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (SetField(persistent, "font_size", "small"))

                null width 15 height 40

#                grid 2 1 xfill True:
#                    spacing 5
#                    add "mods/notdream/UserInterface/gui/Preference/nd_textspeed_menu.png"
#                    # ТУТ ЗАМЕНИТЬ ТЕКСТ НА "СКОРОСТЬ" by Otorhin
#                    bar:
#                        value Preference("text speed")
#                        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
#                        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
#                        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
#                        xmaximum 470
#                        ymaximum 40
        
        # vbar value YScrollValue("nd_v_prefrences_1") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" thumb_offset -12
        # vbar value YScrollValue("nd_v_prefrences_1") # Бар, как второй элемент hbox-а.

    add "mods/notdream/UserInterface/gui/Preference/nd_textspeed_menu.png" xpos 1180 ypos 503
        #Text speed code by Otorhin
    bar:
        value Preference("text speed")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xmaximum 470
        ymaximum 40
        xpos 1270
        ypos 500

    add "mods/notdream/UserInterface/gui/Preference/nd_music_menu.png" xpos 1180 ypos 769
    bar:
        value Preference("music volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 761
        xmaximum 470
        ymaximum 40
        
    add "mods/notdream/UserInterface/gui/Preference/nd_sound_menu.png" xpos 1198 ypos 838
        
    bar:
        value Preference("sound volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 829
        xmaximum 470
        ymaximum 40
        
    add "mods/notdream/UserInterface/gui/Preference/nd_ambience_menu.png" xpos 1167 ypos 908
        
    bar:
        value Preference("voice volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 897
        xmaximum 470
        ymaximum 40


    add "mods/notdream/UserInterface/gui/Preference/nd_mmusic_title.png" xpos 1229 ypos 684
    if persistent.music_in_menu == True:

        imagebutton:
            xpos 1592 ypos 683
            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
            action [
                    SetVariable("persistent.music_in_menu", False),
                    Jump("nd_turn_music_in_menu_pr")
                    ]
    else:

        imagebutton:
            xpos 1592 ypos 683
            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
            action [
                    SetVariable("persistent.music_in_menu", True),
                    Jump("nd_turn_music_in_menu_pr")
                    ]

    if persistent.nd_f_codeinserted == True:

        imagebutton:
            xpos 1244 ypos 333
            idle ("mods/notdream/UserInterface/gui/Preference/pref_active_code_button.png")
            hover ("mods/notdream/UserInterface/gui/Preference/pref_active_code_button.png")
            action NullAction()

    else:
        imagebutton:
            xpos 1278 ypos 339
            idle ("mods/notdream/UserInterface/gui/Preference/pref_ent_code_button_idle.png")
            hover ("mods/notdream/UserInterface/gui/Preference/pref_ent_code_button_hover.png")
            action [
                    Play('nd_ui_sounds', ui_click),
                    Jump('nd_enter_code_start'),
                    ]

screen nd_preferences2:
    
    tag menu
    modal True

    add "mods/notdream/UserInterface/gui/Preference/nd_preference_osn.png"
    
    imagebutton:
        xpos 163 ypos 935
        idle ("mods/notdream/UserInterface/gui/Preference/nd_back_preference_idle.png")
        hover ("mods/notdream/UserInterface/gui/Preference/nd_back_preference_hover.png")
        action [Play('nd_ui_sounds', ui_click),
        ShowMenu('nd_game_menu_selector')]
        
    hbox:
        spacing 20 # Расстояние, между баром и боксом.
        xsize 800 # Размер, дабы не растекалось по всему экрану.
        ysize 600
        align (.17, .5)

        viewport id "nd_v_prefrences_1": # Вьюпорт обязательно с id, дабы можно было прицепить к нему бар.
            xfill True
            yfill False
            mousewheel True # Разрешаем прокрутку мышью.

            vbox:
                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_rezim_osn.png"# xpos 164 ypos 542

                    if not _preferences.fullscreen:
                        imagebutton:
                            #xpos 718 ypos 544
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (Preference("display", "fullscreen"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 544
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (Preference("display", "window"))

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_prefs_skip_unseen.png"# xpos 164 ypos 344

                    if not _preferences.skip_unseen:
                        imagebutton:
                            #xpos 718 ypos 346
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (Preference("skip", "all"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 346
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (Preference("skip", "seen"))

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_18_content.png"# xpos 164 ypos 248

                    if persistent.window_nd == True:
                        imagebutton:
                            #xpos 718 ypos 250
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action Function(nd_routepoints_window_off)
                    else:
                        imagebutton:
                            #xpos 718 ypos 250
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
                            action Function(nd_routepoints_window_on)

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_autosave_title.png" #xpos 164 ypos 440
                    if persistent.autosave_unlocker == True:
                        imagebutton:
                            #xpos 718 ypos 442
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
                            action [
                                    SetVariable("persistent.autosave_unlocker", False),
                                    SetVariable("config.has_autosave", False),
                                    SetVariable("config.autosave_frequency", None),
                                    SetVariable("config.autosave_on_choice", False) 
                                    ]
                    else:
                        imagebutton:
                            #xpos 718 ypos 442
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
                            action [
                                    SetVariable("persistent.autosave_unlocker", True),
                                    SetVariable("config.has_autosave", True),
                                    SetVariable("config.autosave_frequency", 300),
                                    SetVariable("config.autosave_on_choice", False) 
                                    ]

                null width 15 height 40

                grid 2 1 xfill True:
                    add "mods/notdream/UserInterface/gui/Preference/nd_cursorstyle_title.png" #xpos 164 ypos 748

                    if persistent.nd_cursor_style == "normal":
                        imagebutton:
                            #xpos 718 ypos 748
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
                            action [
                                    SetVariable("config.mouse_displayable", MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_prologue_v2.png', 30, 30)),
                                    SetVariable("persistent.nd_cursor_style", "circle"),
                                    ]
                    else:
                        imagebutton:
                            #xpos 718 ypos 748
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
                            action [
                                    SetVariable("config.mouse_displayable", MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_prologue_v2.png', 0, 0)),
                                    SetVariable("persistent.nd_cursor_style", "normal"),
                                    ]

                null width 15 height 40

                grid 2 1 xfill True: #(This example of grid only has 2 line and 1 rows, so a total of 1 items can be placed in it)
                    add "mods/notdream/UserInterface/gui/Preference/nd_razmer_menu.png" #xpos 164 ypos 646
                    if persistent.font_size == "small":
                        imagebutton:
                            #xpos 718 ypos 646
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
                            action (SetField(persistent, "font_size", "large"))
                    else:
                        imagebutton:
                            #xpos 718 ypos 646
                            xalign .5
                            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
                            action (SetField(persistent, "font_size", "small"))

                null width 15 height 40

        # vbar value YScrollValue("nd_v_prefrences_1") bottom_bar "images/misc/none.png" top_bar "images/misc/none.png" thumb "images/gui/settings/vthumb.png" thumb_offset -12
        # vbar value YScrollValue("nd_v_prefrences_1") # Бар, как второй элемент hbox-а.

    add "mods/notdream/UserInterface/gui/Preference/nd_textspeed_menu.png" xpos 1180 ypos 503
    #Text speed code by Otorhin
    bar:
        value Preference("text speed")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xmaximum 470
        ymaximum 40
        xpos 1270
        ypos 500

    add "mods/notdream/UserInterface/gui/Preference/nd_music_menu.png" xpos 1180 ypos 769
    bar:
        value Preference("music volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 761
        xmaximum 470
        ymaximum 40
        
    add "mods/notdream/UserInterface/gui/Preference/nd_sound_menu.png" xpos 1198 ypos 838
        
    bar:
        value Preference("sound volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 829
        xmaximum 470
        ymaximum 40
        
    add "mods/notdream/UserInterface/gui/Preference/nd_ambience_menu.png" xpos 1167 ypos 908
        
    bar:
        value Preference("voice volume")
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 1270
        ypos 897
        xmaximum 470
        ymaximum 40


    add "mods/notdream/UserInterface/gui/Preference/nd_mmusic_title.png" xpos 1229 ypos 684
    
    if persistent.music_in_menu == True:
        imagebutton:
            xpos 1592 ypos 683
            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png")
            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_on.png") 
            action [
                    SetVariable("persistent.music_in_menu", False),
                    ]
    else:

        imagebutton:
            xpos 1592 ypos 683
            idle ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png")
            hover ("mods/notdream/UserInterface/gui/Preference/nd_pref_tumbnail_off.png") 
            action [
                    SetVariable("persistent.music_in_menu", True),
                    ]

screen nd_skip_scenario_d5():

    imagebutton xalign 0.98 yalign 0.03:
        idle ("mods/notdream/UserInterface/gui/skip_menu/nd_skip_idle.png")
        hover ("mods/notdream/UserInterface/gui/skip_menu/nd_skip_hover.png")
        action [
            Play('sound', ui_click), 
            Hide("nd_skip_scenario_d5", dissolve),
            Jump("nd_continue_d5_usmz")
            ]

label nd_true_exit:

    hide screen nd_game_menu_selector
    scene black 
    with dissolve
    stop music fadeout 3
    pause 1

    $ nd_screens_diact()
    $ MainMenu(confirm=False)()

label nd_turn_music_in_menu_pr:

    if persistent.music_in_menu == True:
        if res == 'day':
            play music menu_nd_1 fadein 2
        if res == 'evening':
            play music menu_nd_3 fadein 2
        if res == 'night':
            play music menu_nd_2 fadein 2
            
    if persistent.music_in_menu == False:
        stop music fadeout 2

    show screen nd_preferences
    $ renpy.pause(999999999999999999999999999999999, hard=True)

    # $ nd_music_menu_on_off()