init:
    #sounds
    $ nd_notify_sound = "mods/notdream/UserInterface/voicemenu/sounds/nd_notify_sound.mp3"

    # bg
    image nd_voicescreen = "mods/notdream/UserInterface/voicemenu/nd_voicescreen.png"
    image nd_voicescreen_notification_b = "mods/notdream/UserInterface/voicemenu/nd_voicescreen_notification_b.png"

    #buttons
    image nd_voicemutebutton_hover = "mods/notdream/UserInterface/voicemenu/buttons/nd_voicemutebutton_hover.png"
    image nd_voicemutebutton_idle = "mods/notdream/UserInterface/voicemenu/buttons/nd_voicemutebutton_idle.png"

    transform notify_notdream_trans:
        xpos -450 ypos 37 alpha .0
        ease 1.0 xpos 37 ypos 37 alpha 1.0
        pause 10
        ease 1.0 xpos -407 ypos 37 alpha .0
        pause 1

    transform notify_button_notdream_trans:
        xpos -52 ypos 37 alpha .0
        ease 1.0 xpos 428 ypos 37 alpha 1.0
        pause 10
        ease 1.0 xpos -52 ypos 37 alpha .0
        pause 1

    python:
        def notdream_shownotify(pic): # $ notdream_shownotify("nd_voicescreen_notification_b")
            renpy.show(pic, [notify_notdream_trans], layer="screens")
            # renpy.show_screen(scr, [notify_button_notdream_trans], layer="screens") # (, scr)
            renpy.play(nd_notify_sound)
            

screen nd_showedvoicenotify_foroff:
    tag notify
    modal False

    imagebutton at notify_button_notdream_trans:
        idle ("nd_voicemutebutton_idle")
        hover ("nd_voicemutebutton_hover")
        action [
            Play('sound', ui_click),
            Function(renpy.music.set_volume, volume=0, delay=1, channel="nd_voice"),
            SetVariable("persistent.nd_voice", False),
            ]

screen nd_showedvoicenotify_foron:

    add "mods/notdream/UserInterface/voicemenu/nd_voicescreen.png"

    imagebutton xpos 427 ypos 36:
        idle ("nd_voicemutebutton_idle")
        hover ("nd_voicemutebutton_hover")
        action [
            Play('sound', ui_click),
            Function(renpy.music.set_volume, volume=0, delay=0, channel="nd_voice"),
            SetVariable("persistent.nd_voiceplay", False),
            Hide("nd_showedvoicenotify_foron", nd_effect_5_reverse)
            ]

screen nd_voicebar_screen:
    modal False

    textbutton "Громкость озвучки":
        style 'helveticaneueroman_idle'
        xpos 600
        ypos 37
    
    bar:
        value MixerValue('nd_voice_mixer')
        right_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_chist.png"
        left_bar "mods/notdream/UserInterface/gui/Preference/nd_scale_poln.png"
        thumb "mods/notdream/UserInterface/gui/Preference/nd_begunok.png"
        xpos 830
        ypos 30
        xmaximum 470
        ymaximum 40

label label_nd_voice_on:
    $ renpy.music.set_volume(1.3, delay=1.5, channel="nd_voice")

    # $ notdream_achievment("achievment_notdream_start")
                