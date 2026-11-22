init :
    
    $ notdream_path                 =           "mods/notdream/"                # Сокращение к папке мода
    $ notdream_imagepath            =           "mods/notdream/images/"         # Сокращение к папке изображений мода
    $ notdream_musicpath            =           "mods/notdream/music/"          # Сокращение к папке музыки мода
    $ notdream_soundspath           =           "mods/notdream/sounds/"         # Сокращение к папке звуков мода
    $ notdream_ambiencepath         =           "mods/notdream/ambience/"       # Сокращение к папке звуков окружения мода
    $ notdream_fontspath            =           "mods/notdream/fonts/"          # Сокращение к папке шрифтов
    $ notdream_UIpath               =           "mods/notdream/UserInterface/"  # Сокращение к папке пользовательского интерфейса
    $ notdream_minigamespath        =           "mods/notdream/minigames/"      # Сокращение к папке мини-игр

    #Картинки глав на экране
    image nd_part1_hovered          = notdream_UIpath + "Parts_screen_nd/parts_nd/nd_part1_hovered.png"
    image nd_part1_idle             = notdream_UIpath + "Parts_screen_nd/parts_nd/nd_part1_idle.png"
    image nd_part2_hovered          = notdream_UIpath + "Parts_screen_nd/parts_nd/nd_part2_hovered.png"
    image nd_part2_idle             = notdream_UIpath + "Parts_screen_nd/parts_nd/nd_part2_idle.png"
    image nd_part2_locked           = notdream_UIpath + "Parts_screen_nd/parts_nd/nd_part2_locked.png"

    #Картинки интерфейса экрана глав
    image back_to_menu_nd_hovered      = notdream_UIpath + "Parts_screen_nd/interface/back_to_menu_nd_hovered.png"
    image back_to_menu_nd_idle         = notdream_UIpath + "Parts_screen_nd/interface/back_to_menu_nd_idle.png"
    image coming_soon_nd               = notdream_UIpath + "Parts_screen_nd/interface/coming_soon_nd.png"

    #Главный экран глав
    image parts_screen_nd_day       = notdream_UIpath + "Parts_screen_nd/parts_screen_nd_day.jpg"
    image parts_screen_nd_evening   = notdream_UIpath + "Parts_screen_nd/parts_screen_nd_evening.jpg"
    image parts_screen_nd_night     = notdream_UIpath + "Parts_screen_nd/parts_screen_nd_night.jpg"

    #Кнопки старта главы
    image parts_start_idle          = notdream_UIpath + "Parts_screen_nd/interface/parts_start_idle.png"
    image parts_start_hover         = notdream_UIpath + "Parts_screen_nd/interface/parts_start_hover.png"

    image chapter_1_screen          = notdream_UIpath + "Parts_screen_nd/chapter_1_screen.png"
    image chapter_1_bg              = notdream_UIpath + "Parts_screen_nd/chapter_1_bg.jpg"
    image chapter_2_screen          = notdream_UIpath + "Parts_screen_nd/chapter_2_screen.png"
    image chapter_2_bg              = notdream_UIpath + "Parts_screen_nd/chapter_2_bg.jpg"

screen parts_nd_screen:

    tag menu
    modal True
    
    imagebutton xpos 0.044 ypos 0.7:
        idle ("parts_start_idle")
        hover ("parts_start_hover")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("turn_1_part_of_my_mod_notdream")
            ]

    imagebutton xpos 0.044 ypos 0.8:
        idle ("back_to_menu_nd_idle")
        hover ("back_to_menu_nd_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("hiding_nd_part_screen")
            ]

    imagebutton xpos 0.92 ypos 0.85:
        idle ("switch_button_right_idle")
        hover ("switch_button_right_hovered")
        action[
            Play('nd_ui_sounds', ui_click),
            Jump("enable_two_part_nd_selector")
            ]

    #if iknowmyway_nd_us == True:
    #    imagebutton xpos 0.60 ypos 0.31:
    #        idle ("nd_part2_idle")
    #        hover ("nd_part2_hovered")
    #        action [
    #            NullAction()
    #           ]
    #else:

    #    imagebutton xpos 0.60 ypos 0.31:
    #        idle ("nd_part2_locked")
    #        hover ("nd_part2_locked")
    #        action [
    #           Play('sound', ui_error),
    #           NullAction()
    #           ]

    #imagebutton xpos 0.619 ypos 0.41:
    #    idle ("coming_soon_nd")
    #    hover ("coming_soon_nd")
    #    action [
    #       Play('sound', ui_error),
    #        NullAction()
    #        ]
    
screen parts_nd_screen2:

    tag menu
    modal True
    

    if '13556081' in nd_addons and persistent.us_us_end_scr == True:
        imagebutton xpos 0.044 ypos 0.7:
            idle ("parts_start_idle")
            hover ("parts_start_hover")
            action [
                Play('nd_ui_sounds', ui_click),
                Jump("turn_2_part_of_my_mod_notdream")
                ]
    
    else:    
        imagebutton xpos 0.044 ypos 0.7:
            idle ("coming_soon_nd")
            hover ("coming_soon_nd")
            action [
                Play('nd_ui_sounds', ui_error),
                NullAction()
                ]

    imagebutton xpos 0.044 ypos 0.8:
        idle ("back_to_menu_nd_idle")
        hover ("back_to_menu_nd_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("hiding_nd_part_screen")
            ]

    imagebutton xpos 0.92 ypos 0.85:
        idle ('switch_button_left_idle')
        hover ('switch_button_left_hovered')
        action[
            Play('nd_ui_sounds', ui_click),
            Jump('enable_one_part_nd_selector')
            ]



