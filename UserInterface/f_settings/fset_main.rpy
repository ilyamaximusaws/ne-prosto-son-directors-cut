init:

    image nd_ui_mainform            = "mods/notdream/UserInterface/f_settings/main/nd_ui_mainform.png"
    
    image nd_continue_hover         = "mods/notdream/UserInterface/f_settings/buttons/nd_continue_hover.png"
    image nd_continue_idle          = "mods/notdream/UserInterface/f_settings/buttons/nd_continue_idle.png"
    image nd_insert_before          = "mods/notdream/UserInterface/f_settings/buttons/nd_insert_before.png"
    image nd_insert_after           = "mods/notdream/UserInterface/f_settings/buttons/nd_insert_after.png"
    image nd_checkbox_on            = "mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png"
    image nd_checkbox_off           = "mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png"

    image nd_f_error1               = "mods/notdream/UserInterface/f_settings/text/nd_f_error1.png"
    image nd_f_error2               = "mods/notdream/UserInterface/f_settings/text/nd_f_error2.png"
    image nd_f_thxfor               = "mods/notdream/UserInterface/f_settings/text/nd_f_thxfor.png"
    image nd_fautosave_text         = "mods/notdream/UserInterface/f_settings/text/nd_fautosave_text.png"
    image nd_fbigfont_text          = "mods/notdream/UserInterface/f_settings/text/nd_fbigfont_text.png"
    image nd_fmainmenu_text         = "mods/notdream/UserInterface/f_settings/text/nd_fmainmenu_text.png"

screen nd_fsettings:
    tag menu
    modal True

    imagebutton xpos 850 ypos 845:
        idle ("nd_continue_idle")
        hover ("nd_continue_hover")
        action [
            Play('sound', ui_click),
            Jump("cont_fs_nd")
            ]

    imagebutton xpos 732 ypos 470:
        idle ("nd_fautosave_text")
        hover ("nd_fautosave_text")
        action NullAction()

    imagebutton xpos 757 ypos 525:
        idle ("nd_fbigfont_text")
        hover ("nd_fbigfont_text")
        action NullAction()

    imagebutton xpos 765 ypos 584:
        idle ("nd_fmainmenu_text")
        hover ("nd_fmainmenu_text")
        action NullAction()

    if persistent.autosave_unlocker == True:
        
        imagebutton:
            xpos 1150 ypos 465
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png") 
            action [
                    SetVariable("persistent.autosave_unlocker", False),
                    SetVariable("config.has_autosave", False),
                    SetVariable("config.autosave_frequency", None),
                    SetVariable("config.autosave_on_choice", False) 
                    ]
    else:

        imagebutton:
            xpos 1150 ypos 465
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png") 
            action [
                    SetVariable("persistent.autosave_unlocker", True),
                    SetVariable("config.has_autosave", True),
                    SetVariable("config.autosave_frequency", 300),
                    SetVariable("config.autosave_on_choice", False) 
                    ]

    if persistent.font_size == "small":
        imagebutton:
            xpos 1125 ypos 520
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png")
            action (SetField(persistent, "font_size", "large"))
    else:
        imagebutton:
            xpos 1125 ypos 520
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png")
            action (SetField(persistent, "font_size", "small"))


    if persistent.music_in_menu == True:
        imagebutton:
            xpos 1118 ypos 579
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_on.png") 
            action [
                    Stop(channel="music", fadeout=3),
                    SetVariable("persistent.music_in_menu", False),
                    ]
    else:
        imagebutton:
            xpos 1118 ypos 579
            idle ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png")
            hover ("mods/notdream/UserInterface/f_settings/buttons/nd_checkbox_off.png") 
            action [
                    SetVariable("persistent.music_in_menu", True)
                    ]

    if persistent.nd_f_codeinserted == None:
        imagebutton xpos 789 ypos 711:
            idle ("nd_insert_before")
            hover ("nd_insert_before")
            action [
                    Jump("nd_f_activate_code")
                    ]

    if persistent.nd_f_codeinserted == False:
        imagebutton xpos 789 ypos 711:
            idle ("nd_insert_after")
            hover ("nd_insert_after")
            action [
                    Jump("nd_f_activate_code")
                    ]

        imagebutton xpos 872 ypos 766:
            idle ("nd_f_error1")
            hover ("nd_f_error1")
            action NullAction()

    if persistent.nd_f_codeinserted == True:

        imagebutton xpos 789 ypos 711:
            idle ("nd_insert_after")
            hover ("nd_insert_after")
            action NullAction()

        imagebutton xpos 842 ypos 766:
            idle ("nd_f_thxfor")
            hover ("nd_f_thxfor")
            action NullAction()

label nd_f_activate_code:
    
    hide nd_ui_mainform
    hide screen nd_fsettings 
    with dissolve

    $ nd_f_code = renpy.input(_("Введите код:"))
    $ nd_f_code = nd_f_code.strip()

    python:

        for i in nd_codes_list:
            if i == str(nd_f_code):
                persistent.nd_f_codeinserted = True
                persistent.nd_moral_points += 120
            else:
                persistent.nd_f_codeinserted = False

    show nd_ui_mainform
    show screen nd_fsettings
    with dissolve

    $ renpy.pause(999999999999999999999999999999999999999999999999999999999999999999999999, hard=True)

label nd_fscr_onnn:

    # АВТОСОХРАНЕНИЯ по умолчанию
    $ persistent.autosave_unlocker = False
    $ config.has_autosave = False
    $ config.autosave_frequency = None
    $ config.autosave_on_choice = False

    # МУЗЫКА В МЕНЮ по умолчанию
    $ persistent.music_in_menu = True

    if res == "day":

        if persistent.nd_cursor_style == "normal":
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 0, 0)]}
        else:
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 15, 15)]}

        play ambience ambience_camp_center_day fadein 4
        scene ext_house_of_mt_day_razm: 
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0
        with dissolve2

    if res == "evening":

        if persistent.nd_cursor_style == "normal":
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 0, 0)]}
        else:
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 15, 15)]}

        play ambience ambience_camp_center_evening fadein 4
        scene ext_house_of_mt_sunset_razm: 
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0
        with dissolve2

    if res == "night":

        if persistent.nd_cursor_style == "normal":
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 0, 0)]}
        else:
            $ config.mouse = {'default' : [(notdream_UIpath + 'cur/'+ persistent.nd_cursor_style + '/'+ persistent.nd_cursor_style  + '_cursor_' + res + '.png', 15, 15)]}
        
        play ambience ambience_camp_entrance_night fadein 4
        scene ext_road_night_razm:
            xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
            ease 1.0 zoom 1.0 alpha 1.0
        with dissolve2

    $ renpy.pause(1, hard=True)

    show nd_ui_mainform
    show screen nd_fsettings 
    with dissolve

    $ renpy.pause(999999999999999999999999999999999999999999999999999999999999999999999999, hard=True)







