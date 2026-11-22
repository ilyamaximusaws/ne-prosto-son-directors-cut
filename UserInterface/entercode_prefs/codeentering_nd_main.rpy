init:
    image nd_enter_code_button              = "mods/notdream/UserInterface/entercode_prefs/codeimages/enter_code_button.png"
    image nd_enter_code_button_entered      = "mods/notdream/UserInterface/entercode_prefs/codeimages/enter_code_button_entered.png"
    image nd_codeins_main_form_1            = "mods/notdream/UserInterface/entercode_prefs/codeimages/main_form_1.png"
    image nd_codeins_main_form_entering     = "mods/notdream/UserInterface/entercode_prefs/codeimages/main_form_entering.png"
    image nd_codeins_main_form_error        = "mods/notdream/UserInterface/entercode_prefs/codeimages/main_form_error.png"
    image nd_codeins_main_form_success      = "mods/notdream/UserInterface/entercode_prefs/codeimages/main_form_success.png"
    image nd_cis_back_idle                  = "mods/notdream/UserInterface/entercode_prefs/codeimages/nd_cis_back_idle.png"
    image nd_cis_back_hover                 = "mods/notdream/UserInterface/entercode_prefs/codeimages/nd_cis_back_hover.png"
    image alm_mf_ci                         = "mods/notdream/UserInterface/entercode_prefs/codeimages/alm_mf_ci.jpg"

screen nd_code_insertform:

    tag menu
    modal True

    imagebutton xpos 600 ypos 427:
        idle ("nd_cis_back_idle")
        hover ("nd_cis_back_hover")
        action [
                Jump("nd_enter_code_end")
                ]

    imagebutton xpos 616 ypos 557:
        idle ("nd_enter_code_button")
        hover ("nd_enter_code_button")
        action [
                Jump("nd_enter_code_processed")
                ]

label nd_enter_code_start:
    
    hide screen nd_preferences 
    scene alm_mf_ci
    with dissolve
    $ renpy.pause(0.5, hard=True)
    show nd_codeins_main_form_1
    show screen nd_code_insertform
    with dissolve

    $ renpy.pause(9999999999999999999999999999999999999999999999, hard=True)

label nd_enter_code_processed:
    
    hide screen nd_code_insertform
    hide nd_codeins_main_form_1
    show nd_codeins_main_form_entering
    with nd_effect_5_reverse

    $ nd_f_code = renpy.input(_("Введите код: (Enter - Ввод/Отмена)"))
    $ nd_f_code = nd_f_code.strip()
    
    python:

        for i in nd_codes_list:
            if i == str(nd_f_code):
                persistent.nd_f_codeinserted = True
                persistent.nd_moral_points += 120
                
            else:
                persistent.nd_f_codeinserted = False
        
    if persistent.nd_f_codeinserted == True:
        jump nd_enter_code_success

    if persistent.nd_f_codeinserted == False:
        jump nd_enter_code_error

label nd_enter_code_success:
    
    hide nd_codeins_main_form_entering
    show nd_codeins_main_form_success
    with nd_effect_5_reverse

    $ renpy.pause(3, hard=True)

    hide nd_codeins_main_form_success
    with dissolve

    $ renpy.pause(0.5, hard=True)

    hide alm_mf_ci
    show screen nd_preferences
    with dissolve

    $ renpy.pause(9999999999999999999999999999999999999999999999, hard=True)

label nd_enter_code_error:

    hide nd_codeins_main_form_entering
    show nd_codeins_main_form_error
    with nd_effect_5_reverse

    $ renpy.pause(3, hard=True)

    hide nd_codeins_main_form_error
    show nd_codeins_main_form_1
    show screen nd_code_insertform
    with nd_effect_5
    $ renpy.pause(9999999999999999999999999999999999999999999999, hard=True)

label nd_enter_code_end:
    
    hide nd_codeins_main_form_1
    hide screen nd_code_insertform
    with dissolve

    $ renpy.pause(0.5, hard=True)

    hide alm_mf_ci
    show screen nd_preferences
    with dissolve

    $ renpy.pause(9999999999999999999999999999999999999999999999, hard=True)