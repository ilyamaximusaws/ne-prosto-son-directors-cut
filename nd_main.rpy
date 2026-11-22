# ╔═════════════════════════════════════════════════════╗
# ║
# ║ "Это не просто сон, верно?"
# ║ Авторство модификации: https://vk.com/bmodmakersitw 
# ║ 
# ║ При использовании материалов, указывайте авторство
# ║ в конечных титрах или в другом доступном месте.
# ║
# ║ Tandem Studio © 2020
# ║
# ╚═════════════════════════════════════════════════════╝

init -11 python:
## - - - MODIFICATION ▼
## Version settings container
    persistent.nd_ver = str("3.0 [[R]")
    persistent.es_ver = str("1.3")

## Modification main label container
    try:
        mods["notdream"]=u"Это не просто сон, верно?"
        modsImages["notdream"] = ("mods/notdream/UserInterface/imageicon_tablemods.jpg", False, 'Это не просто сон, верно?')
    except:
        mods["notdream"]=u"Это не просто сон, верно?"

## Compatability Addons Module
    
    nd_addons_path = "mods/notdream/addons/"
    nd_addons = [
    ]

## Persistent conditions container

    if persistent.nd_fix_end == True:
        persistent.nd_fix_end = True

    elif persistent.nd_fix_end == False:
        persistent.nd_fix_end = False
    else:
        persistent.nd_fix_end = None


    nd_completed_secrets = 0

    if persistent.autosave_unlocker == False:
        config.has_autosave = False
        config.autosave_frequency = None
        config.autosave_on_choice = False

    elif persistent.autosave_unlocker == True:
        config.has_autosave = True
        config.autosave_frequency = 1000
        config.autosave_on_choice = True

    if not persistent.music_in_menu == True:
        persistent.music_in_menu = False

    if not persistent.first_start_nd == False:
        persistent.first_start_nd = True

    if not persistent.first_start_nk_miz == True:
        persistent.first_start_nk_miz = False

    if persistent.nd_moral_points <= -99999:
        persistent.nd_moral_points = 0

    if persistent.nd_seed_titles <= -99999:
        persistent.nd_seed_titles = 0
    
    if persistent.nd_seed_titles == None:
        persistent.nd_seed_titles = 0

    if persistent.semen_dancelesson <= -99999:
        persistent.semen_dancelesson = 0

    if not persistent.nd_first_play_qte_d2 == True:
        persistent.nd_first_play_qte_d2 = False

    if persistent.papich_nd <= -9999:
        persistent.papich_nd = 0

    if persistent.papich_nd == 1:
        nd_completed_secrets += 1

    if persistent.thunder_nd == 1:
        nd_completed_secrets += 1

    if not persistent.censored_notdream == True:
        persistent.censored_notdream = False

    if not persistent.censored_notdream == False:
        persistent.censored_notdream = True

    if not persistent.nd_voiceplay == True:
        renpy.music.set_volume(0, delay=0, channel="nd_voice")
        persistent.nd_voiceplay = False
    if not persistent.nd_voiceplay == False:
        renpy.music.set_volume(1, delay=0, channel="nd_voice")
        persistent.nd_voiceplay = True

init:
## - - - VARIABLES ▼
## Mod`s variables container
    $ nd_devmenu_text               =           "Release by {i}Tandem Studio{/i}"
    $ secrets_points_int            =           2                               # Всего секретов в модификации
    $ iknowmyway_nd_us              =           None                            # Когда завершишь 6 день, удали. Кодер из будущего: похуй)
    $ qtr_miss                      =           0                               # Поражения игрока в игре "Эрудит"
    $ usrr                          =           0                               # Очки отношений с Ульяной
    $ dvrr                          =           0                               # Очки отношений с Алисой
    $ nir                           =           0                               # Очки к концовке "Нирвана"
    $ usrf                          =           0                               # Очки отношений с Ульяной после 3 дня
    $ nd_mirr                       =           0                               # Очки отношений с Мику
    $ autosave_autoload_unlocker    =           1                               # Разблокировка автосохранения / Для отключения необходимо значение единицы изменить на ноль
    $ d1_dv_guitar_learning         =           False                           # Игрок получает эту переменную в True после того, как откажется с Ульяной идти играть в футбол
    $ dv_leave_d1                   =           False                           # Уйти от Алисы в первом дне после кражи булок (побежать за Ульяной)
    $ dv_flag_morning_d1            =           False                           # Остаться с Алисой (не бежать за Ульяной)
    $ us_candy_steal                =           False                           # Отправиться с Ульяной в столовую за конфетами
    $ d2_dv_morning_din_sorry       =           False                           # Извиниться перед Алисой в столовой во 2-м дне
    $ d2_dv_night_pristan           =           False                           # Ивент с пристанью и Алисой во 2-м дне
    $ d2_nirvana_night_pristan      =           False                           # Ивент с пристанью с Алисой и Ульяной во 2-м дне
    $ paper_m                       =           False                           # Мятость бумажки после выбора в первом сне
    $ fake_z_54                     =           None                            # Фейк роспись 2-й день
    $ persistent.ss_first_time      =           False                           # Первая встреча игрока с Самантой
    $ userpcname                    =           os.environ.get('username')      # Взять имя пользователя
    $ d2_night_dv                   =           False                           # ПРИСТАНЬ (2 день) | С алисой
    $ d2_night_csx                  =           False                           # ПРИСТАНЬ (2 день) | Ульяна
    $ d2_night_nir                  =           False                           # ПРИСТАНЬ (2 день) | Нирвана
    $ d2_dv_night_pristan_q         =           False                           # Приглашение Алисы на встречу у пристани
    $ us_scenario_road              =           False                           # Развитие с персонажем \Ульяна\ после 3-го дня
    $ dv_scenario_road              =           False                           # Развитие с персонажем \Алиса\ после 3-го дня
    $ nir_scenario_road             =           False                           # Развитие \Нирвана\ после 3-го дня
    $ sich_scenario_road            =           False                           # Одинокий волк после 3-го дня. Плохая концовка
    $ necessary_clubs               =           0                               # Карта во втором дне
    $ necessary_musclub             =           0                               # Карта во втором дне
    $ necessary_aidpost             =           0                               # Карта во втором дне
    $ necessary_library             =           0                               # Карта во втором дне
    $ necessary_map                 =           0                               # Карта во втором дне
    $ necessary_search_us_scene     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_sport     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_map       =           0                               # Карта во время поисков Ульяны
    $ music_kr_dv                   =           False                           # Запись на кружок МУЗЫкИ
    $ persistent.fall_stair_bunker  =           0                               # Количество падений с лестницы в бункере
    $ sport_kr_us                   =           False                           # Запись на кружок ФУТБОЛА
    $ dvrr_shark_p                  =           0                               # Плакат акулы в клубе гитаристов
    $ dvrr_pirate_p                 =           0                               # Плакат пирата в клубе гитаристов
    $ gg_sorry_us                   =           False                           # Концовка Ульяны "Прощай"
    $ gg_goodbye_us                 =           False                           # Концовка Ульяны "Прости"
    $ miss_us_r_1                   =           False                           # Обида Ульяны на что-либо
    $ old_camp_sh_cheese            =           False                           # Сыр для Шурика в старом лагере
    $ open_nirvana_road_nd          =           None                            # Состояние рута нирваны, выдаваемое во время сна в автобусе в прологе.
    $ nd_us_flaggs                  =           0                               # Флаги с Ульяной после 3 дня
    $ persistent.dv_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True
    $ persistent.us_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True
    $ nd_credits_us                 =           "{font=mods/notdream/fonts/nd_helvuelight.ttf}{size=30}Это не просто сон, верно?\nby\nTandem Studio\n\n  {image=mods/notdream/images/ends/tandem_logo.png}\n\nМы благодарим вас за время\n которое вы уделили нашей модификации\n\nНе забудьте оставить отзыв на странице мода в Steam\nили в нашей группе ВКонтакте!\n\n{size=35}АВТОРСТВО СЦЕНАРИЯ{/size=35}\nИлья Мяус                         {color=#999999}Рут Ульяны{/color=#999999}\nАлександр Алексеев       {color=#999999}Рут Алисы{/color=#999999} \nДенис Баклин                   {color=#999999}Рут Мику{/color=#999999}    \n\n{size=35}ОТВЕТСТВЕННЫЕ ЗА КОД{/size=35}\nИлья Мяус\nАлександр Скорняков{color=#999999}{/color=#999999}\n\n{size=35}ДИЗАЙН{/size=35}\nИлья Мяус\n\n{size=35}АВТОРЫ ИДЕИ{/size=35}\nИлья Мяус\nИван Бочарников\nДенис Баклин\n\n{size=35}БЕТА-ТЕСТЕРЫ{/size=35}\nИван Бочарников           {color=#999999}Сценарная и тех. составляющие{/color=#999999}\n        xeaal            {color=#999999}Грамматика и пунктуация{/color=#999999}\nВиктор Столопов         {color=#999999}Техническая составляющая{/color=#999999}\n\nКРЕАТИВНЫЙ ДИРЕКТОР\nИван Бочарников\n\nТЕХНИЧЕСКАЯ СОСТАВЛЯЮЩАЯ\nИлья Мяус\nАлександр Шевцов\n\nАВТОРСТВО МУЗЫКИ И ЗВУКОВ\nДенис Баклин\nСергей Ейбог\nВиктор Цой\nГустав Ар\n\nИ ДРУГИЕ ПРАВООБЛАДАТЕЛИ, ТАКИЕ КАК\nМод \"7дл\"\nМод \"Мы - это главное\"\nМод \"Новая Жизнь\"\nNoiseFX.ru\n\n\n\nСПЕЦИАЛЬНЫЕ БЛАГОДАРНОСТИ\nКонстантин Мирошниченко          {color=#999999}Публикация первого сценария{/color=#999999}\nМария Бут                         {color=#999999}Поддержка автора <3{/color=#999999}\nИван Молченко                                {color=#999999}Верный друг автора модификации{/color=#999999}\nАлександр Зимнухов                    {color=#999999}Брат автора, хороший человек{/color=#999999}\n\n{color=#999999}И конечно же мама и папа{/color=#999999}\n\n\n\nДРУГИЕ\nВиктор Овлепин, Евгений Мяус, Авдеев Артём,\nСергей Петров, Алексей Носенко, Александр Алиновский,\nАлександр Миронов, Диана Ниженко, Владя,\nАндрей Плевецкий,\nДенис Шибинский, Артём Шип, Лев Бочаров и прочие...\n\n\nОтдельная благодарность:\n\n Подписчикам группы \"Tandem Studio | Бесконечное лето\"\n\n Группе \"Mods by Soviet Tyan\"\n за великолепную модификацию \"Новая жизнь\"\n\nРазработчикам мода \"7 Дней лета\"\n за мод и ресурсы\n\nСообществу \"LEONZO\"\n\nГруппе \"Летние Вести\" или \"Алый Вестник\"\n\nРазработчикам мода \"Последнее Лето\"\n\nРазработчикам мода \"Мы - это главное\"\n\n\"Бесконечное Лето / Soviet Games\"\n\nГруппе \"Как создать свой мод для игры Бесконечное Лето\"\nА также руководству в Steam\n\nРазработчикам модификации \"Путь к успеху\"\n\nСтранице игры на \"Fandom Wiki\"\n\nМодификации \"Алеся: Побег из лагеря\"\n\n\nМАТЕРИАЛЫ, ИСПОЛЬЗОВАННЫЕ В МОДЕ,\nПРИНАДЛЕЖАТ ИСКЛЮЧИТЕЛЬНО\nИХ ПЕРВИЧНЫМ ПРАВООБЛАДАТЕЛЯМ\n\n\nМУЗЫКА В ТИТРАХ:\nUnknown Artist - Like The Wind (P)\n\n\n\nНАДЕЕМСЯ УВИДЕТЬ ВАС ЗДЕСЬ СНОВА!{/size=30}{/font}"
    $ nd_credits_dv                 =           "Tandem Studio благодарит вас за время\n уделённое время модификации\n\"Это не просто сон, верно?\".\n\nНе забудьте оставить отзыв на странице мода в Steam\nили в группе ВКонтакте!\n\nАвторы сценария:\nИлья Мяус\nАлександр Алексеев\nДенис Баклин\nИван Бочарников\n\nНаписание кода:\nИлья Мяус\n\nАвторы идеи:\nИлья Мяус\nИван Бочарников\n\nБета-тестер:\nИван Бочарников\n\nВизуальная составляющая:\nИлья Мяус\n\nТехническая составляющая:\nИлья Мяус\n\nКомпозитор:\nДенис Баклин\n\nИные источники музыки и звуков:\nСергей Ейбог\nМод \"7дл\"\nМод \"Мы - это главное\"\nМод \"Новая Жизнь\"\nNoiseFX.ru\n\n\n\n Специальные благодарности:\n Константину Мирошниченко - за поддержку\n Марии Бут - за поддержку <3.\n Ивану Молченко - за поддержку.\n Александру Зимнухову - за поддержку.\n Дмитрию Петрову - за поддержку.\nТимуру Мустафину - как инвестору :)\n\n Маме и Папе \n\n\n\n А так же другим, таким как:\n Виктор Овлепин, Евгений Мяус, Авдеев Артём,\n Сергей Петров, Алексей Носенко, Александр Алиновский,\n Александр Миронов, Диана Ниженко, Владя,\n Андрей Плевецкий,\n Денис Шибинский и другим...\n\n\n Отдельная благодарность:\n\n Подписчикам группы \"Tandem Studio | Бесконечное лето\"\n\n Группе \"Mods by Soviet Tyan\"\n за великолепную модификацию \"Новая жизнь\"\n\nРазработчикам мода \"7 Дней лета\"\n за мод и ресурсы\n\nСообществу \"LEONZO\"\n\nГруппе \"Летние Вести\" или \"Алый Вестник\"\n\n Разработчикам мода \"Последнее Лето\"\n\n Разработчикам мода \"Мы - это главное\"\n\n\"Бесконечное Лето / Soviet Games\"\n\nГруппе \"Как создать свой мод для игры Бесконечное Лето\"\n А также руководству в Steam\n\n Разработчикам модификации \"Путь к успеху\" \n\n Странице игры на \"Fandom Wiki\"\n\n\"7dots\" за основу для меню с разработчиками мода.\n\nМодификации \"Алеся: Побег из лагеря\"\n\nМатериалы, использованные в моде,\nпринадлежат исключительно\nих первичным правооладателям\n\n\n\n НАДЕЕМСЯ УВИДЕТЬ ВАС ЗДЕСЬ СНОВА!"
    $ ND_PATH                       =           "mods/notdream/"                # Сокращение к папке мода
    $ ND_IMAGES                     =           "mods/notdream/images/"         # Сокращение к папке изображений мода
    
    $ ND_MUSIC                      =           'mods/notdream/audio/music/'    # Сокращение к папке музыки мода
    $ ND_SOUNDS                     =           "mods/notdream/audio/sounds/"   # Сокращение к папке звуков мода
    $ ND_AMBIENCE                   =           "mods/notdream/audio/ambience/" # Сокращение к папке звуков окружения мода
    $ ND_VOICE                      =           "mods/notdream/audio/voice/"    # Сокращение к папке голосов мода
    $ ND_MMUSIC                     =           'mods/notdream/UserInterface/Main_menu/'

    $ ND_FONTS                      =           "mods/notdream/fonts/"          # Сокращение к папке шрифтов
    $ ND_UI                         =           "mods/notdream/UserInterface/"  # Сокращение к папке пользовательского интерфейса
    $ ND_MINIGAMES                  =           "mods/notdream/minigames/"      # Сокращение к папке мини-игр
    $ nepodhod_87                   =           False                           # ты - пидор
    $ nd_us_s_r                     =           False                           # АЧЕ)
    $ nd_scept                      =           0                               # Очки скептицизма
    $ nd_stoic                      =           0                               # Очки стоицизма

    $ nd_knb_stone                  =           False
    $ nd_knb_sci                    =           False
    $ nd_knb_paper                  =           False

    $ nd_lst_lar                    =           False
    $ nd_lst_us                     =           False

## - - - IMAGES ▼
## Mod images container
    image bg sklad                                  = ND_IMAGES + "bg/storage_day.jpg"
    image bg ogorod                                 = ND_IMAGES + "bg/dream1_ogorod.jpg"
    image bg int_kvart                              = ND_IMAGES + "bg/int_kvart_night.jpg"
    image bg int_kvart_night                        = ND_IMAGES + "bg/int_kvart_night_1.jpg"
    image bg nd_bg_psychabinet                      = ND_IMAGES + "bg/nd_bg_psychabinet.png"
    
    # MH HOME BG`s
    image bg int_house_of_gg_day                    = ND_IMAGES + "bg/int_house_of_gg_day.jpg"
    image bg ext_home_night                         = ND_IMAGES + "bg/ext_slavya_home_night.jpg"
    image bg ext_home_sunset                        = ND_IMAGES + "bg/ext_home_sunset.jpg"
    image bg int_house_of_gg_night                  = ND_IMAGES + "bg/int_house_of_gg_night.png"
    image bg int_house_of_gg_night_1                = ND_IMAGES + "bg/int_house_of_gg_night_1.png"
    image bg int_house_of_gg_sunset                 = ND_IMAGES + "bg/int_house_of_gg_sunset.png"
    image bg int_house_of_gg_night_2                = ND_IMAGES + "bg/int_house_of_gg_night_2.jpg"
    image bg int_house_of_gg_extra_night            = ND_IMAGES + "bg/int_house_of_gg_night_1.png"
    image bg ext_house_of_gg_night2                 = ND_IMAGES + "bg/ext_house_of_gg_night2.jpg"
    # OTHER
    image bg int_sporthall_sunset_color             = ND_IMAGES + "bg/int_sporthall_sunset_color.png"
    image bg ext_violet_path_night                  = ND_IMAGES + "bg/ext_violet_path_night.png"
    image bg int_hallway_sporthall                  = ND_IMAGES + "bg/int_hallway_sporthall.jpg"
    image bg int_hallway_sporthall_night            = ND_IMAGES + "bg/int_hallway_sporthall_night.png"
    image bg ext_volley_court                       = ND_IMAGES + "bg/ext_volley_court.png"
    image bg d4_lineup_no_un_us                     = ND_IMAGES + "bg/d4_lineup_no_un_us.jpg"
    image bg vor_lar_tum                            = ND_IMAGES + "bg/vor_lar_tum.jpg"
    image bg vor_zap_tum                            = ND_IMAGES + "bg/vor_zap_tum.jpg"
    image bg ext_camp_entrance_sunset_wahf          = ND_IMAGES + "bg/ext_camp_entrance_sunset_wahf.jpg"
    image bg ext_music_club_verandah_day            = ND_IMAGES + "bg/ext_music_club_verandah_day.jpg"
    image bg int_shaht_tem                          = ND_IMAGES + "bg/int_shaht_tem.jpg"
    image bg sporthall                              = ND_IMAGES + "bg/int_sporthall.jpg"
    image bg prolog_bus_inside                      = ND_IMAGES + "bg/zima_liaz.jpg"
    image bg oblaka                                 = ND_IMAGES + "bg/oblaka.jpg"
    image bg us_fb_p_sunset                         = ND_IMAGES + "bg/us_fb_p_sunset.jpg"
    image bg tain_beach_us                          = ND_IMAGES + "bg/tain_beach_us.jpg"
    image bg pole_1                                 = ND_IMAGES + "bg/us_fb_p_sunset_2.jpg"
    image bg us_fb_sunset                           = ND_IMAGES + "bg/us_fb_sunset.jpg"
    image bg us_fall_forest                         = ND_IMAGES + "bg/us_fall_forest.jpg"
    image bg gorod_doma                             = ND_IMAGES + "bg/gorod_doma.jpg"
    image bg sneg_lavochka                          = ND_IMAGES + "bg/sneg_lavochka.jpg"
    image bg ext_stage_big_sunset                   = ND_IMAGES + "bg/ext_stage_big_sunset.jpg"
    image bg int_editorial_day                      = ND_IMAGES + "bg/int_editorial_day.jpg"
    image bg int_school_ext_nd                      = ND_IMAGES + "bg/int_school_ext_nd.jpg"
    image int_school_night                          = ND_IMAGES + "bg/int_school_night_nd.png"
    image bg tain_mesto_night                       = ND_IMAGES + "bg/tain_mesto_night.jpg"
    image bg ext_house_of_dv_sunset                 = ND_IMAGES + "bg/ext_house_of_dv_sunset.jpg"
    image bg ext_houses_night                       = ND_IMAGES + "bg/ext_houses_night.jpg"
    image bg ext_houses_night_1                     = ND_IMAGES + "bg/ext_houses_night_1.jpg"
    image bg ext_house_of_dv_mono                   = ND_IMAGES + "bg/ext_house_of_dv_mono.jpg"
    image bg city_night_rain                        = ND_IMAGES + "bg/city_night_rain.jpg"
    image bg city_toronto_rain                      = ND_IMAGES + "bg/city_toronto_rain.jpg"
    image intro_xx_rain                             = ND_IMAGES + "bg/intro_xx_rain.jpg"
    image us_memories                               = ND_IMAGES + "bg/us_memories.jpg"
    image blackclouds_bluesky                       = ND_IMAGES + "bg/blackclouds_bluesky.jpg"
    image bg ext_aidpost_sunset                     = ND_IMAGES + "bg/ext_aidpost_sunset.jpg"
    image bg int_sporthall_sunset_rain              = ND_IMAGES + "bg/int_sporthall_sunset_rain.jpg"
    image bg int_sporthall_sunset_pred              = ND_IMAGES + "bg/int_sporthall_sunset_pred.jpg"
    image bg int_sporthall_night_dance              = ND_IMAGES + "bg/int_sporthall_night_dance.jpg"
    image bg int_sporthall_night                    = ND_IMAGES + "bg/int_sporthall_night.jpg"
    image bg rainy_idle_nd                          = ND_IMAGES + "bg/rainy_idle_nd.jpg"
    image bg int_library_sunset                     = ND_IMAGES + "bg/int_library_sunset.jpg"
    image bg ext_yulya_dream_bunker                 = ND_IMAGES + "bg/ext_yulya_dream_bunker.jpg"
    image bg dancestatement                         = ND_IMAGES + "bg/dancestatement.jpg"
    image bg d4_us_bseansky                         = ND_IMAGES + "bg/d4_us_bseansky.jpg"
    image bg ext_stage_big_day                      = ND_IMAGES + "bg/ext_stage_big_day.jpg"
    image bg ext_stage_big_clear_day                = ND_IMAGES + "bg/ext_stage_big_clear_day.jpg"
    image bg ext_stage_near_clear                   = ND_IMAGES + "bg/ext_stage_near_clear.jpg"
    image bg ext_glade_day                          = ND_IMAGES + "bg/ext_glade_day.jpg"
    image ussr_flag_d1                              = ND_IMAGES + "bg/ussr_flag_d1.png"
    image smartphone_first                          = ND_IMAGES + "bg/smartphone_first.png"
    image bg clouds_day                             = ND_IMAGES + "bg/clouds_day.jpg"
    image bg ussrr_m_p4                             = ND_IMAGES + "bg/ussrr_m_p4.jpg"
    image bg ext_entrance_night_clear_closed_nd     = ND_IMAGES + "bg/ext_entrance_night_clear_closed_nd.jpg"
    image nd_tolpa                                  = ND_IMAGES + "bg/nd_tolpa.png"
    image bg nd_4_underwater                        = ND_IMAGES + "bg/underwater.jpg"
    image zdes_moi_glaz                             = ND_IMAGES + "bg/zdes_moi_glaz.jpg"
    image lineup_all_firstperson                    = ND_IMAGES + "bg/lineup_all_firstperson.jpg"
    image bg ext_volley_court_night                 = ND_IMAGES + "bg/ext_volley_court_night.jpg"
    image bg ext_stage_big_night_alice_pirate_rain  = ND_IMAGES + "bg/dv_r/ext_stage_big_night_alice_pirate_rain.jpg"
    image bg ext_stage_big_night_alice_shark_rain   = ND_IMAGES + "bg/dv_r/ext_stage_big_night_alice_shark_rain.jpg"
    image bg ext_stage_big_day_alice                = ND_IMAGES + "bg/dv_r/ext_stage_big_day_alice.jpg"
    image bg ext_stage_big_day_alice_flagtag        = ND_IMAGES + "bg/dv_r/ext_stage_big_day_alice_flagtag.jpg"
    image ext_stage_big_day_alice_pirate            = ND_IMAGES + "bg/dv_r/ext_stage_big_day_alice_pirate.png"
    image ext_stage_big_day_alice_shark             = ND_IMAGES + "bg/dv_r/ext_stage_big_day_alice_shark.png"
    image int_catacombs_living_dark                 = ND_IMAGES + "bg/int_catacombs_living_dark.jpg"
    image bg int_clubs_sunset                       = ND_IMAGES + "bg/int_clubs_sunset.jpg"
    image bg ext_clubs_sunset                       = ND_IMAGES + "bg/ext_clubs_sunset.jpg"
    image bg ext_house_of_dv_sunrise                = ND_IMAGES + "bg/ext_house_of_dv_sunrise.jpg"
    image bg ext_path2_sunset                       = ND_IMAGES + "bg/ext_path2_sunset.jpg"
    image bg ext_old_building_sunset_red            = ND_IMAGES + "bg/ext_old_building_sunset_red.jpg"
    image bg int_old_building_day                   = ND_IMAGES + "bg/int_old_building_day.jpg"
    image bg int_mine_exit_light                    = ND_IMAGES + "bg/int_mine_exit_light.jpg"
    image bg int_mine_exit                          = ND_IMAGES + "bg/int_mine_exit.jpg"
    image bg ext_shower_night                       = ND_IMAGES + "bg/ext_shower_night.jpg"
    image bg ext_playground_rain_night              = "mods/notdream/images/notdream_rain_bg/ext_playground_rain_night.jpg"
    image bg ext_path_night_light                   = ND_IMAGES + "bg/ext_path_night_light.jpg"
    image bg ext_path2_night_light                  = ND_IMAGES + "bg/ext_path2_night_light.jpg"
    image bg int_mine_exit_night_light_forest       = ND_IMAGES + "bg/int_mine_exit_night_light_forest.jpg"
    image bg int_mine_exit_night_light_forest_opened= ND_IMAGES + "bg/int_mine_exit_night_light_forest_opened.jpg"
    image vlad_pavlenko_pizza                       = "mods/notdream/images/bg/dv_r/nd_bruh.jpg"
    image nd_new_mainmenu                           = "mods/notdream/images/bg/dv_r/nd_new_mainmenu.jpg"
    image movie                                     = Movie(size=(1920, 1080), xpos=0, ypos=0, xanchor=0, yanchor=0)
    image bg nd_vladis_kamen                        = ND_IMAGES + "bg/nd_vladis_kamen.jpg"
    image bg nd_d1_lineup_mi                        = ND_IMAGES + "bg/nd_d1_lineup_mi.jpg"
    image bg nd_il_us_d5                            = ND_IMAGES + "bg/nd_il_us_d5.jpg"
    image bg nd_ext_backentrance_night              = ND_IMAGES + "bg/nd_ext_backentrance_night.jpg"
    image bg nd_ext_storage_day                     = ND_IMAGES + "bg/nd_ext_storage_day.jpg"
    image bg nd_int_musclub_sunset                  = ND_IMAGES + "bg/nd_int_musclub_sunset.png"
    image bg nd_il_us_d5_noflashlight               = ND_IMAGES + "bg/nd_il_us_d5_noflashlight.jpg"
    image bg nd_il_us_d5_flashlight                 = ND_IMAGES + "bg/nd_il_us_d5_flashlight.jpg"
    image bg nd_ext_road_night                      = ND_IMAGES + "bg/nd_ext_road_night.jpg"
    image bg int_house_of_dv_sunset                 = ND_IMAGES + "bg/int_house_of_dv_sunset.jpg"
    image nd_cit_d5                                 = ND_IMAGES + "ends/nd_cit_d5.png"
    image bg int_nd_kitchen                         = ND_IMAGES + "bg/int_nd_kitchen.jpg"
    image nd_kolonka_norm                           = ND_IMAGES + "bg/nd_kolonka_norm.png"
    image bg nd_bg_lastss_forest                    = ND_IMAGES + "bg/nd_bg_lastss_forest.png"
    image bg nd_roadtofuture_d6                     = ND_IMAGES + "bg/nd_roadtofuture_d6.jpg"
    image bg nd_bg_lastss_far                       = ND_IMAGES + "bg/nd_bg_lastss_far.png"
    image bg nd_ext_path_forest_day                 = ND_IMAGES + "bg/nd_ext_path_forest_day.png"
    image bg ext_forest_night_last                  = ND_IMAGES + "bg/ext_forest_night_last.png"
    image bg nd_bad_end_bg                          = ND_IMAGES + "bg/nd_bad_end_bg.jpg"
    image bg nd_int_aidpost_sunset                  = ND_IMAGES + "bg/nd_int_aidpost_sunset.png"
    
    #---CG
    image cg us_fb_day_sport            = ND_IMAGES + "bg/us_fb_day_sport.jpg"
    image cg nd_pioneer_d4              = ND_IMAGES + "bg/nd_pioneer_d4.jpg"
    image cg us_boat                    = ND_IMAGES + "bg/us_boat.jpg"
    image cg semyon_mirror              = ND_IMAGES + "bg/semyon_mirror.jpg"
    image cg d2_us_fall_on_playgr       = ND_IMAGES + "bg/d2_us_fall_on_playgr.jpg"
    image cg d1_dv_guitar               = ND_IMAGES + "bg/d1_dv_guitar.jpg"
    image cg us_night_t                 = ND_IMAGES + "bg/us_night_t.jpg"
    image cg d3_dance_imleft            = ND_IMAGES + "bg/d3_dance_imleft.jpg"
    image cg mi_raper_d4_nd             = ND_IMAGES + "bg/mi_raper_d4_nd.jpg"
    image cg dv_on_scene_with_ilya      = ND_IMAGES + "bg/dv_on_scene_with_ilya.jpg"
    image cg sun_forest_dvr             = ND_IMAGES + "bg/sun_forest_dvr.jpg"
    image cg beach_play                 = ND_IMAGES + "bg/beach_play.jpg"
    image cg ussrr_dv_p_d4              = ND_IMAGES + "bg/ussrr_dv_p_d4.jpg"
    image cg d1_grasshopper_nd          = ND_IMAGES + "bg/d1_grasshopper_nd.jpg"
    image cg d1_ussr_falling_nd         = ND_IMAGES + "bg/d1_ussr_falling_nd.jpg"
    image cg d3_soccer_nd               = ND_IMAGES + "bg/d3_soccer_nd.jpg"
    image cg us_football_evening        = ND_IMAGES + "bg/us_football_evening.jpg"
    image us_for_playground             = ND_IMAGES + "bg/us_for_playground.png"
    image cg us_dv_mi_beach_d4          = ND_IMAGES + "bg/us_dv_mi_beach_d4.jpg"
    image cg nd_us_football_sunset      = ND_IMAGES + "bg/nd_us_football_sunset.jpg"
    image cg nd_unbelievable_art        = ND_IMAGES + "cg/nd_unbelievable_art.png"
    image cg nd_goodend_nfm             = ND_IMAGES + "cg/nd_goodend_nfm.png"
    image cg nd_us_boat_d5              = ND_IMAGES + "bg/nd_us_boat_d5.png"
    image cg nd_us_milata               = ND_IMAGES + "bg/nd_us_milata.jpg"
    image cg nd_u_costra_alice          = ND_IMAGES + "bg/nd_u_costra_alice.jpg"
    image cg nd_d5_coster_gg            = ND_IMAGES + "bg/nd_d5_coster_gg.jpg"
    image cg nd_d5_coster_gg_propusk    = ND_IMAGES + "bg/nd_d5_coster_gg_propusk.jpg"
    image cg nd_kiss_usr                = ND_IMAGES + "cg/nd_kiss_usr.png"
    image cg d5_us_boat                 = ND_IMAGES + "bg/d5_us_boat.jpg"
    image cg nd_concertists             = ND_IMAGES + "bg/nd_concertists.png"
    image cg nd_p2_anime_us             = ND_IMAGES + "cg/nd_p2_anime_us.png"
    
    #---Extra
    image nd_fix_snowfall                       = ND_IMAGES + "extra/nd_fix_snowfall.png"
    image dreaming_uv_us                        = ND_IMAGES + "extra/dreaming_uv_us.jpg"
    image splatter_notdream                     = ND_IMAGES + "extra/splatter_notdream.png"
    image splatter_dark_notdream                = ND_IMAGES + "extra/splatter_dark_notdream.png"
    image zapiska_d3                            = ND_IMAGES + "bg/zapiska_d3.png"
    image zapiska_d4_u                          = ND_IMAGES + "bg/zapiska_d4_u.png"
    image zapiska_d4_o                          = ND_IMAGES + "bg/zapiska_d4_o.png"
    image bush_frame                            = ND_IMAGES + "extra/bush_frame.png"
    image bush_frame_night                      = ND_IMAGES + "extra/bush_frame_night.png"
    image nd_sp_cam                             = ND_IMAGES + "extra/nd_sp_cam.png"
    image nd_blood_light                        = ND_IMAGES + "extra/nd_blood_light.png"
    image nd_blood_light2                       = ND_IMAGES + "extra/nd_blood_light2.png"
    image nd_blood_light3                       = ND_IMAGES + "extra/nd_blood_light3.png"
    image nd_ef_4                               = ND_IMAGES + "extra/nd_ef_4.png"
    image nd_in_bushes                          = ND_IMAGES + "extra/nd_in_bushes.png"
    image nd_dozimer_cifr                       = ND_IMAGES + "extra/nd_dozimer_cifr.png"
    image nd_dozimer_nocifr                     = ND_IMAGES + "extra/nd_dozimer_nocifr.png"
    image nd_5_rubasov                          = ND_IMAGES + "extra/nd_5_rubasov.png"
    image nd_thunder_backentrancet              = ND_IMAGES + "extra/nd_thunder_backentrancet.png"
    image nd_falling_star_1                     = ND_IMAGES + "extra/nd_falling_star_1.png"
    image nd_bsrn                               = ND_IMAGES + "extra/nd_bsrn.png"
    image nd_sept_fired                         = ND_IMAGES + "extra/nd_sept_fired.png"
    image nd_hard_fog                           = ND_IMAGES + "extra/nd_hard_fog.png"
    image nd_light_fog                          = ND_IMAGES + "extra/nd_light_fog.png"
    image sb_d6_eye_1                           = ND_IMAGES + "extra/sb_d6_eye_1.png"
    image sb_d6_eye_2                           = ND_IMAGES + "extra/sb_d6_eye_2.png"
    image ext_playground_prerain_meteor         = ND_IMAGES + "extra/ext_playground_prerain_meteor.png"

    #---Наряжаемая площадь sunset
    image bg ext_square_sunset3     = ND_IMAGES + "bg/ext_square_sunset3.jpg" #только колонки
    image bg ext_square_sunset2     = ND_IMAGES + "bg/ext_square_sunset2.jpg" #колонки и гирлянды

    #---Собственные bg экстерьера спортзала
    image bg ext_sport_1_day        = ND_IMAGES + "bg/ext_sport_1_day.jpg"
    image bg ext_sport_2_day        = ND_IMAGES + "bg/ext_sport_2_day.jpg"

    #---Прекраснейшие плакаты для столовой :D
    image d3_plakat_1               = ND_IMAGES + "bg/d3_plakat_1.jpg"
    image d3_plakat_2               = ND_IMAGES + "bg/d3_plakat_2.jpg"


    #---Карта
    image map_complete              = ND_IMAGES + "bg/map_complete.jpg"
    image map_uncomplete            = ND_IMAGES + "bg/map_uncomplete.jpg"

    #---Disclamer
    image bg disclamer2             = ND_IMAGES + "disclamer/disclamer_u2.png"
    image bg caution_hv_nd          = ND_IMAGES + "disclamer/caution_hv_nd.jpg"
    image bg present_1              = ND_IMAGES + "disclamer/present_1.jpg"
    image bg present_2              = ND_IMAGES + "disclamer/present_2.jpg"
    image bg disclamer3             = ND_IMAGES + "disclamer/disclamer_u3.png"

    #---Достижения
    image achievment_notdream_start     = ND_IMAGES + "achievments/achievment_start.png"
    image achievment_nordream_d1_stol   = ND_IMAGES + "achievment_d1_stol.png"
    image achievment_nordream_d2_army   = ND_IMAGES + "achievment_d2_army.png"

## Forming images list container
    python:
        for i in renpy.list_files():
            if i.startswith("mods/notdream/images/notdream_rain_bg/") and i.endswith((".jpg", ".png")):
                renpy.image(((str("bg ")) + str(i)[38:-4]), i)
            if i.startswith("mods/notdream/images/gorod_d5/") and i.endswith((".jpg", ".png")):
                renpy.image(((str("bg ")) + str(i)[30:-4]), i)
            if i.startswith("mods/notdream/images/bg/koster/") and i.endswith((".jpg", ".png")):
                renpy.image(((str("bg ")) + str(i)[31:-4]), i)

## Non "scenarried" images container 
    image cursor_original               = ND_UI                 +       "cursor_original.png"
    image notdream_endscreen_0          = ND_UI                 +       "notdream_endscreen_0.png"
    image notdream_endscreen            = ND_UI                 +       "notdream_endscreen.png"
    image notdream_startscreen          = ND_UI                 +       "notdream_startscreen.png"
    image notdream_startscreen_bg       = ND_UI                 +       "notdream_startscreen_bg.jpg"
    image notdream_startscreen_1        = ND_UI                 +       "notdream_startscreen_1.jpg"
    image notdream_startscreen_2        = ND_UI                 +       "notdream_startscreen_2.jpg"
    image notdream_startscreen_3        = ND_UI                 +       "notdream_startscreen_3.jpg"
    image notdream_startscreen_4        = ND_UI                 +       "notdream_startscreen_4.jpg"
    image INJDR_1                       = ND_UI                 +       "INJDR_1.jpg"
    image INJDR_2                       = ND_UI                 +       "INJDR_2.jpg"
    image bg present_d1d1               = ND_UI                 +       "present_d1d1.jpg"
    image dm_savedata_idle              = ND_UI                 +       "Main_menu/items/dm_savedata_idle.png"
    image dm_savedata_hover             = ND_UI                 +       "Main_menu/items/dm_savedata_hover.png"
    image what_you_done                 = ND_UI                 +       "what_you_done.jpg"
    image group_dreammod_hovered        = ND_UI                 +       "Main_menu/items/group_dreammod_hovered.png"
    image group_dreammod                = ND_UI                 +       "Main_menu/items/group_dreammod.png"
    image achieve_screen                = ND_UI                 +       "achieve_screen.jpg"
    image transparent_notdream          = ND_UI                 +       "Main_menu/items/transparent_notdream.png"
    image fonmenudreammoddemoend        = ND_UI                 +       "fonmenudreammoddemoend.jpg"
    image music_concert_d1              = ND_UI                 +       "music_concert_d1.jpg"
    image for_continue_nd               = ND_UI                 +       "Main_menu/start/for_continue_nd.png"
    image ext_house_of_mt_day_razm      = ND_UI                 +       "Main_menu/start/ext_house_of_mt_day_razm.jpg"
    image ext_house_of_mt_sunset_razm   = ND_UI                 +       "Main_menu/start/ext_house_of_mt_sunset_razm.jpg"
    image ext_road_night_razm           = ND_UI                 +       "Main_menu/start/ext_road_night_razm.jpg"
    image us_mainmenu_day               = ND_UI                 +       "Main_menu/sprites/us_mainmenu_day.png"
    image un_mainmenu_day               = ND_UI                 +       "Main_menu/sprites/un_mainmenu_day.png"
    image dv_mainmenu_evening           = ND_UI                 +       "Main_menu/sprites/dv_mainmenu_evening.png"
    image bg fonmenudreammod_day_1      = ND_UI                 +       "Main_menu/items/fonmenudreammod_day_1.jpg"
    image bg fonmenudreammod_evening_1  = ND_UI                 +       "Main_menu/items/fonmenudreammod_evening_1.jpg"
    image bg fonmenudreammod_night_1    = ND_UI                 +       "Main_menu/items/fonmenudreammod_night_1.jpg"
    image advice_dreammod               = ND_UI                 +       "Main_menu/items/advice_dreammod.png"
    image bg settings_nd_day            = ND_UI                 +       "Main_menu/settings/settings_nd_day.jpg"
    image bg settings_nd_sunset         = ND_UI                 +       "Main_menu/settings/settings_nd_sunset.jpg"
    image bg settings_nd_night          = ND_UI                 +       "Main_menu/settings/settings_nd_night.jpg"
    image secret_nd_settings            = ND_UI                 +       "secret_nd_settings.jpg"
    image titles_bg                     = ND_IMAGES             +       "ends/titles_bg.jpg"
    image thx_for_1                     = ND_IMAGES             +       "ends/thx_for_1.jpg"
    
    image nd_mainmenu_day_mobile        = ND_UI                 +       "Main_menu/mobile_v/nd_mainmenu_day_mobile.png"
    image nd_mainmenu_evening_mobile    = ND_UI                 +       "Main_menu/mobile_v/nd_mainmenu_evening_mobile.png"
    image nd_mainmenu_night_mobile      = ND_UI                 +       "Main_menu/mobile_v/nd_mainmenu_night_mobile.png"
    image nd_normally                   = ND_UI                 +       "nd_normally.png"

    image nd_about_button_hover         = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_about_button_hover.png"
    image nd_about_button_idle          = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_about_button_idle.png"
    image nd_bugsg_button_hover         = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_bugsg_button_hover.png"
    image nd_bugsg_button_idle          = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_bugsg_button_idle.png"
    image nd_exit_button_hover          = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_exit_button_hover.png"
    image nd_exit_button_idle           = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_exit_button_idle.png"
    image nd_load_button_hover          = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_load_button_hover.png"
    image nd_load_button_idle           = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_load_button_idle.png"
    image nd_newgame_button_hover       = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_newgame_button_hover.png"
    image nd_newgame_button_idle        = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_newgame_button_idle.png"
    image nd_profile_button_hover       = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_profile_button_hover.png"
    image nd_profile_button_idle        = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_profile_button_idle.png"
    image nd_settings_button_hover      = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_settings_button_hover.png"
    image nd_settings_button_idle       = ND_UI                 +       "Main_menu/mobile_v/buttons/nd_settings_button_idle.png"

    image nd_developer_mode_alert       = ND_UI                 +       "nd_developer_mode_alert.png"

    # Изображения относящиеся к концовкам:
    ## US TRUE
    image us_true_sorry                 = ND_IMAGES             +       "ends/us_true/end_us_true_1.jpg"
    image us_true_bye                   = ND_IMAGES             +       "ends/us_true/end_us_true_1_1.jpg"
    # DV DEMO
    image dvr_camp_end_1                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_1.jpg"
    image dvr_camp_end_2                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_2.jpg"
    image dvr_camp_end_3                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_3.jpg"
    image dvr_camp_end_4                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_4.jpg"
    image dvr_camp_end_5                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_5.jpg"
    image dvr_camp_end_6                = ND_IMAGES             +       "ends/dv_beta/dvr_camp_end_6.jpg"

    image nd_progress_logo = "mods/notdream/UserInterface/gui/Preference/nd_progress_logo.png"
    image nd_ambience_menu = "mods/notdream/UserInterface/gui/Preference/nd_ambience_menu.png"
    image nd_exit_please   = "mods/notdream/UserInterface/gui/Preference/nd_exit_please.jpg"

## - - - FILES ▼
## Forming list with files def container
    python:
        def nd_form_files_list(path):
            return {i[len(path):i.rfind(".")]:i for i in renpy.list_files() if i.startswith(path)}
## Archives pull-up container
    python:
        config.archives.append("mods/notdream/images/sprites/own_sprites/nd_nda_01")
        config.archives.append("mods/notdream/images/cg/nd_artas_01")

## - - - EFFECTS ▼
## Rain effect container
    image notdream_raindrop_large   = ND_IMAGES + "particles/raindrop_large.png"
    image notdream_raindrop_normal  = ND_IMAGES + "particles/raindrop_normal.png"
    image notdream_raindrop_small   = ND_IMAGES + "particles/raindrop_small.png"

    image nd_light_rain_effect:
        truecenter
        xzoom 1.3 yzoom 2.2
        contains:
            SnowBlossom("notdream_raindrop_normal", 10, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("notdream_raindrop_small", 25, 50, (25, 50), (1400, 1500))

    image nd_light_rain_effect_l:
        "nd_light_rain_effect"
        rotate 16.0

    image nd_light_rain_effect_l:
        "nd_light_rain_effect"
        rotate -16.0

    image nd_rain_effect:
        truecenter
        xzoom 1.3
        yzoom 2.11
        contains:
            SnowBlossom("notdream_raindrop_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("notdream_raindrop_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("notdream_raindrop_small", 150, 50, (25, 50), (1400, 1500))

    image nd_rain_effect_rain_l:
        "nd_rain_effect"
        truecenter
        rotate 16.0

    image nd_rain_effect_rain_r:
        "nd_rain_effect"
        truecenter
        rotate -16.0

    image nd_rain_effect_hard_rain:
        contains:
            "nd_rain_effect"
        contains:
            "nd_rain_effect"

    image nd_rain_effect_hard_rain_l:
        contains:
            "nd_rain_effect_l"
            truecenter
        contains:
            "nd_rain_effect_l"
            truecenter

    image nd_rain_effect_hard_rain_r:
        contains:
            "nd_rain_effect_r"
            truecenter
        contains:
            "nd_rain_effect_r"
            truecenter
## Rain effect (alternate) container 
    image nd_raindrop_particle_large = "mods/notdream/images/particles/alternate/nd_raindrop_large.png"
    image nd_raindrop_particle_normal = "mods/notdream/images/particles/alternate/nd_raindrop_normal.png"
    image nd_raindrop_particle_small = "mods/notdream/images/particles/alternate/nd_raindrop_small.png"
    image nd_raindrop_particle_large2 = "mods/notdream/images/particles/alternate/nd_raindrop_large2.png"
    image nd_raindrop_particle_normal2 = "mods/notdream/images/particles/alternate/nd_raindrop_normal2.png"
    image nd_raindrop_particle_small2 = "mods/notdream/images/particles/alternate/nd_raindrop_small2.png"

    image nd_light_rain_alternate:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("nd_raindrop_particle_normal", 10, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("nd_raindrop_particle_small", 25, 50, (25, 50), (1400, 1500))

    image nd_light_rain_l_alternate:
        "nd_light_rain"
        rotate 16.0

    image nd_light_rain_r_alternate:
        "nd_light_rain"
        rotate -16.0

    image nd_rain_alternate:
        truecenter
        xzoom 1.3yzoom 1.7
        contains:
            SnowBlossom("nd_raindrop_particle_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("nd_raindrop_particle_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("nd_raindrop_particle_small", 150, 50, (25, 50), (1400, 1500))

    image nd_rain_l_alternate:
        "nd_rain"
        rotate 16.0

    image nd_rain_r_alternate:
        "nd_rain"
        rotate -16.0

    image nd_hard_rain_alternate:
        contains:
            "nd_rain"
        contains:
            "nd_rain"

    image nd_hard_rain_l_alternate:
        contains:
            "nd_rain_l"
        contains:
            "nd_rain_l"

    image nd_hard_rain_r_alternate:
        contains:
            "nd_rain_r"
        contains:
            "nd_rain_r"
## Blur effect container 
    python:
        def nd_get_size(d):
            w, h = renpy.render(renpy.easy.displayable(d), 0, 0, 0, 0).get_size()
            return int(round(w)), int(round(h))

        def nd_show_blur(img, timefortransit, degree):
            w, h = nd_get_size(img)
            factor = im.Scale(renpy.easy_displayable(img), w / degree, h / degree)
            factor = Transform(factor, size = (w, h))
            renpy.show(img, what=factor)
            renpy.transition(Dissolve(timefortransit))
## Particles effect container
    python:
        class nd_particles(renpy.Displayable, NoRollback):
            def __init__(self, particle):
                super(nd_particles, self).__init__()
                self.particle = renpy.displayable(particle)
                self.parts_cache = []

                if self.parts_cache:
                    self.__init__()

                self.max_parts = 50
                self.oldst = None

            def nd_particles_create_cache(self):
                self.parts_cache = [self.nd_particles_get_anim() for i in xrange(self.max_parts)]

            def nd_particles_get_anim(self):
                part = self.particle
                pos = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
                pos2 = [random.randint(0, config.screen_width), random.randint(0, config.screen_height)]
                dist = [pos2[0] - pos[0], pos2[1] - pos[1]]
                speed = random.uniform(45, 55)
                alpha = random.uniform(.25, 1.0)
                zoom = random.uniform(.25, .75)
                time = math.sqrt(dist[0] ** 2 + dist[1] ** 2) / speed
                elapsed_time = time
                birth_time = time - random.uniform(.5, 3.5)
                death_time = random.uniform(.5, 3.5)
                current_zoom = .0
                current_alpha = .0
                return [part, pos, pos2, dist, speed, alpha, zoom, time, elapsed_time, birth_time, death_time, current_zoom, current_alpha]

            def nd_particles_visit(self):
                return [i[0] for i in self.parts_cache]

            def nd_particles_update(self, st):
                if self.oldst == None:
                    self.oldst = st

                self.tick = st - self.oldst
                self.oldst = st

                for part in self.parts_cache:
                    if part[8] <= part[7]:
                        part[8] -= self.tick

                    else:
                        part[8] = 0
                        self.tick = 0

                    if part[8] <= .0:
                        upd_val = self.nd_particles_get_anim()
                        for i in xrange(1, 13):
                            part[i] = upd_val[i]
                    try:
                        path_progress = part[8] / part[7]
                        xdist_now = part[3][0] * path_progress
                        part[1][0] = part[2][0] - xdist_now

                        ydist_now = part[3][1] * path_progress
                        part[1][1] = part[2][1] - ydist_now

                        alpha_time = part[7] - part[9]
                        alpha_el_time = alpha_time
                        alpha_el_time -= self.tick
                        alpha_progress = alpha_el_time / alpha_time
                        alpha_now = part[5] * (1.0 - alpha_progress)
                        zoom_now = part[6] * (1.0 - alpha_progress)

                        if part[8] >= part[9]:
                            if part[12] < part[5] and part[11] < part[6]:
                                part[12] += alpha_now
                                part[11] += zoom_now

                            elif part[12] > part[5] and part[11] > part[6]:
                                part[12] = part[5]
                                part[11] = part[6]

                        if part[8] <= part[10]:
                            if part[12] > .0 and part[11] > .0:
                                part[12] -= alpha_now
                                part[11] -= zoom_now

                            elif part[12] <= .001 and part[11] <= .001:
                                part[12] = .0
                                part[11] = .0

                    except ZeroDivisionError:
                        pass

            def render(self, width, height, st, at):
                if not self.parts_cache:
                    self.nd_particles_create_cache()

                renderObj = renpy.Render(config.screen_width, config.screen_height)

                for part in self.parts_cache:
                    xpos, ypos = part[1]
                    alpha, zoom = part[12], part[11]
                    t = Transform(child = part[0], zoom = zoom, alpha = alpha)
                    cp_render = renpy.render(t, width, height, st, at)
                    renderObj.blit(cp_render, (xpos, ypos))

                self.nd_particles_update(st)
                renpy.redraw(self, 0)
                return renderObj

## - - - ANIMATIONS ▼
## Animated BG`s initialization container

    # Поезда
    image nd_train_night        =   "mods/notdream/images/anim/train_night.png"
    image nd_train_sun          =   "mods/notdream/images/anim/train_sun.png"
    image nd_train_day          =   "mods/notdream/images/anim/train_day.png"
    image nd_train_day2         =   "mods/notdream/images/anim/train_day2.png"

    # Части картинок
    image nd_boatnight_t1          = "mods/notdream/images/anim/boatnight_t1.png"
    image nd_boatnight_t2          = "mods/notdream/images/anim/boatnight_t2.png"
    image nd_boatnight_t3          = "mods/notdream/images/anim/boatnight_t3.png"
    image nd_boatnight_t4          = "mods/notdream/images/anim/boatnight_t4.png"
    image nd_boatday_t             = "mods/notdream/images/anim/boatday_t.png"
    image nd_boatsun_t             = "mods/notdream/images/anim/boatsun_t.png"
    image nd_plyazhday_t           = "mods/notdream/images/anim/plyazhday_t.png"
    image nd_plyazhsunset_t        = "mods/notdream/images/anim/plyazhsunset_t.png"
    image nd_plyazhnight_t         = "mods/notdream/images/anim/plyazhnight_t.png"
    image nd_backDayHouseOD        = "mods/notdream/images/anim/houseOD/day/back.png"
    image nd_backDaySquare         = "mods/notdream/images/anim/campSquare/day/back.png"
    image nd_backWithoutStarsGate  = "mods/notdream/images/anim/gate/night/backWithoutStars.png"
    image nd_backStarsGate_1       = "mods/notdream/images/anim/gate/night/backStars_1.png"
    image nd_backStarsGate_2       = "mods/notdream/images/anim/gate/night/backStars_2.png"
    image nd_backDayCanteen        = "mods/notdream/images/anim/canteen/day/back.png"

    #Вырезанные картинки
    image nd_boatsun_s              = "mods/notdream/images/anim/boatsun_s.png"
    image nd_boatday_s              = "mods/notdream/images/anim/boatday_s.png"
    image nd_boatnight_s            = "mods/notdream/images/anim/boatnight_s.png"
    image nd_plyazhday_s            = "mods/notdream/images/anim/plyazhday_s.png"
    image nd_plyazhsunset_s         = "mods/notdream/images/anim/plyazhsunset_s.png"
    image nd_plyazhnight_s          = "mods/notdream/images/anim/plyazhnight_s.png"
    image nd_gatenight_s            = "mods/notdream/images/anim/gate/night/front.png"
    image nd_frontDaySquare         = "mods/notdream/images/anim/campSquare/day/front.png"
    image nd_frontDayHouseOD        = "mods/notdream/images/anim/houseOD/day/front.png"
    image nd_frontDayCanteen        = "mods/notdream/images/anim/canteen/day/front.png"
    image nd_beamsDayCanteen        = "mods/notdream/images/anim/canteen/day/beams.png"

    #Листва домик ОД
    image nd_1secLeft                  = "mods/notdream/images/anim/houseOD/day/1secLeft.png"
    image nd_1secRight                 = "mods/notdream/images/anim/houseOD/day/1secRight.png"
    image nd_2secLeft                  = "mods/notdream/images/anim/houseOD/day/2secLeft.png"
    image nd_2secRight                 = "mods/notdream/images/anim/houseOD/day/2secRight.png"
    image nd_4secLeft                  = "mods/notdream/images/anim/houseOD/day/4secLeft.png"
    image nd_4secRight                 = "mods/notdream/images/anim/houseOD/day/4secRight.png"

    #Листва площадь
    image nd_daySquare1secLeft         = "mods/notdream/images/anim/campSquare/day/Left1.png"
    image nd_daySquare1secRight        = "mods/notdream/images/anim/campSquare/day/Right1.png"
    image nd_daySquare2secLeft         = "mods/notdream/images/anim/campSquare/day/Left2.png"
    image nd_daySquare2secRight        = "mods/notdream/images/anim/campSquare/day/Right2.png"
    image nd_daySquare4secLeft         = "mods/notdream/images/anim/campSquare/day/Left4.png"
    image nd_daySquare4secRight        = "mods/notdream/images/anim/campSquare/day/Right4.png"

    #облака
    image nd_cloud_test = "mods/notdream/images/anim/cloud_test.png"
    image nd_cloud_test2 = "mods/notdream/images/anim/cloud_test2.png"
    image nd_cloud_test3 = "mods/notdream/images/anim/cloud_test3.png"
    image nd_cloud_big1 = "mods/notdream/images/anim/campSquare/day/cloud_big.png"

    #Звездопад

    image nd_zvezda     = "mods/notdream/images/anim/zvezdo.png"
    image nd_zvezda1    = "mods/notdream/images/anim/zvezdo1.png"
    image nd_zvezda2    = "mods/notdream/images/anim/zvezdo1.png"
    image nd_zvezda3_h  = "mods/notdream/images/anim/star_xvost1.png"
    image nd_zvezda4_h  = "mods/notdream/images/anim/star_xvost.png"
## TRAIN ANIMATION CONTAINER
    
    #ДЕНЬ
    image nd_train_den:
        subpixel True
        contains:
            xalign -1.0 yalign 0.57
            HBox(   "nd_train_day")
            linear 30.0 xalign 2.0 yalign 0.57
            pause(100.0)
            repeat
    #2...
    image nd_train_den2:
        subpixel True
        contains:
            xalign 2.0 yalign 0.476
            HBox(   "nd_train_day2")
            linear 30.0 xalign -1.0 yalign 0.476
            pause(100.0)
            repeat
    #ЗАКАТ
    image nd_train_sunset:
        subpixel True
        contains:
            xalign -0.3 yalign 0.577
            HBox(   "nd_train_sun")
            linear 30.0 xalign 1.5 yalign 0.575
            pause(100.0)
            repeat
    #3...
    image nd_train_sunset2:
        subpixel True
        contains:
            xalign -1.0 yalign 0.476
            HBox(   "nd_train_sun")
            linear 30.0 xalign 1.5 yalign 0.476
            pause(100.0)
            repeat
    #НОЧЬ
    image nd_train_noch:
        subpixel True
        contains:
            xalign 1.9 yalign 0.5765
            HBox(   "nd_train_night")
            linear 30.0 xalign -1.0 yalign 0.571
            pause(100.0)
            repeat
    #4...
    image nd_train_noch2:
        subpixel True
        contains:
            xalign 2.0 yalign 0.476
            HBox(   "nd_train_night")
            linear 30.0 xalign -1.0 yalign 0.476
            pause(100.0)
            repeat
## CANTEEN ANIMATION CONTAINER
    image canteen_day:
        subpixel True
        contains:
            xalign 0.0
            yalign 0.0
            "nd_backDayCanteen"
        contains:
            "nd_cloud_canteen_day"
        contains:
            "nd_cloud_canteen_day_2"
        contains:
            xalign 0.0
            yalign 0.0
            "nd_frontDayCanteen"
        contains:
            "nd_beams_canteen"

    image beams_canteen:
        "nd_beamsDayCanteen" with dissolve
        pause(3.5)
        "nd_frontDayCanteen" with dissolve
        pause(2.5)
        repeat

    image cloud_canteen_day:
        contains:
            subpixel True
            xalign 1.0
            HBox("nd_cloud_test")
            linear 100.0 xpos -1.0
            repeat

    image cloud_canteen_day_2:
        contains:
            subpixel True
            xalign 1.0
            yanchor -1.0
            HBox("nd_cloud_test2")
            linear 75.0 xpos -1.0
            repeat

    ## // scene canteen_day
## BOAT STATION ANIMATION CONTAINER
    
    # DAY
    image nd_day_boat:
        subpixel True
        contains:
            xalign 0.0
            yalign 0.0
            "nd_boatday_t"
        contains:
            "nd_train_den"
        contains:
            xalign 0.0
            yalign 0.0
            "nd_boatday_s"

    # SUNSET
    image nd_sunset_boat:
        subpixel True
        contains:
            xalign 0.0
            yalign 0.0
            "nd_boatsun_t"
        contains:
            "nd_train_sunset"
        contains:
            xalign 0.0
            yalign 0.0
            "nd_boatsun_s"

    # NIGHT
    image nd_night_boat:
        subpixel True
        contains:
            xalign 0.0
            yalign 0.0
            "nd_noch_boat"
        contains:
            "nd_starss"
        contains:
            "nd_train_noch"
        contains:
            xalign 0.0
            yalign 0.0
            "nd_boatnight_s"
## STARS STATIC ANIMATION CONTAINER
    image nd_noch_boat:
        "nd_boatnight_t1" with dissolve
        pause(2.5)
        "nd_boatnight_t3" with dissolve
        pause(2.5)
        "nd_boatnight_t1" with dissolve
        pause(2.5)
        "nd_boatnight_t4" with dissolve
        pause(2.5)
        "nd_boatnight_t2" with dissolve
        pause(2.5)
        "nd_boatnight_t4" with dissolve
        pause(2.5)
        "nd_boatnight_t3" with dissolve
        pause(2.5)
        "nd_boatnight_t1" with dissolve
        pause(2.5)
        "nd_boatnight_t4" with dissolve
        pause(2.5)
        "nd_boatnight_t3" with dissolve
        pause(2.5)
        "nd_boatnight_t1" with dissolve
        pause(2.5)
        "nd_boatnight_t4" with dissolve
        pause(2.5)
        "nd_boatnight_t3" with dissolve
        pause(2.5)
## STARS FALLING ANIMATION CONTAINER
    image nd_starss:
        contains:
            subpixel True
            xalign 1.5 yalign 0.2
            HBox(   "nd_zvezda1")
            linear 2.0 xalign -0.5 yalign 0.2
            pause(15.0)
            repeat
        contains:
            subpixel True
            xalign 1.5 yalign 0.3
            HBox(   "nd_zvezda")
            linear 1.0 xalign -0.9 yalign 1.5
            pause(18.0)
            repeat
        contains:
            subpixel True
            xalign 1.0 yalign -0.2
            HBox(   "nd_zvezda3_h")
            linear 1.0 xalign -0.9 yalign 1.2
            pause(30.0)
            repeat
        contains:
            subpixel True
            xalign 1.5 yalign 0.22
            HBox(   "nd_zvezda4_h")
            linear 1.0 xalign -0.5 yalign 0.22
            pause(19.0)
            repeat
        contains:
            subpixel True
            xalign 1.5 yalign 0.2
            HBox(   "nd_zvezda2")
            linear 3.0 xalign -0.5 yalign 0.4
            pause(20.0)
            repeat
## NIGHT GATE ANIMATION CONTAINER
    image nd_night_gate:
        subpixel True
        contains:
            xalign 0.0
            yalign 0.0
            "nd_stars_gate_glimmer"
        contains:
            "nd_stars_gate"
        contains:
            xalign 0.0
            yalign 0.0
            "nd_gatenight_s"
## STARS GATE GLIMMER ANIMATION CONTAINER
    image nd_stars_gate_glimmer:
        "nd_backWithoutStarsGate" with dissolve
        pause(3.5)
        "nd_backStarsGate_1" with dissolve
        pause(6.5)
        "nd_backStarsGate_2" with dissolve
        pause(6.5)
        "nd_backStarsGate_1" with dissolve
        pause(6.5)
        "nd_backWithoutStarsGate" with dissolve
        pause(3.5)
        "nd_backStarsGate_2" with dissolve
        pause(6.5)
        repeat
## FALLING STARS GATE ANIMATION CONTAINER
    image nd_stars_gate:
        contains:
            subpixel True
            xalign 1.5 yalign 0.3
            HBox(   "nd_zvezda")
            linear 1.0 xalign -0.9 yalign 1.5
            pause(18.0)
            repeat
        contains:
            subpixel True
            xalign 1.0 yalign -0.2
            HBox(   "nd_zvezda3_h")
            linear 1.0 xalign -0.9 yalign 1.2
            pause(30.0)
            repeat
        contains:
            subpixel True
            xalign 1.5 yalign 0.2
            HBox(   "nd_zvezda2")
            linear 3.0 xalign -0.5 yalign 0.4
            pause(20.0)
            repeat
## BOAT STATION ANIMATION CONTAINER
    image cloud_boathouse_day_nd:
        contains:
            subpixel True
            xalign 1.0
            HBox("nd_cloud_test")
            linear 240.0 xpos -1.0
            repeat

    image cloud_boathouse_day2_nd:
        contains:
            subpixel True
            xalign 1.0
            yanchor -1.0
            HBox("nd_cloud_test2")
            linear 190.0 xpos -1.0
            repeat

## - - - OTHERS ▼
## DATETIME PAUSEMENU CONTAINER
    python:
        import datetime

        persistent.game_last_time = datetime.datetime.now()
        if persistent.gametime is None:
            persistent.gametime = 0

        def show_gametime(st, at):
            nd_t = datetime.datetime.now()
            dt = nd_t - persistent.game_last_time
        
            persistent.game_last_time = nd_t
            persistent.gametime += dt.total_seconds()

            minutes, seconds = divmod(int(persistent.gametime), 60)
            hours, minutes = divmod(minutes, 60)
        
            img = Text("{font=mods/notdream/fonts/nd_helvuelight.ttf}{size=40}%0*d:%0*d:%0*d{/font}{/size}" % (2, hours, 2, minutes, 2, seconds))
        
            return img, .1

init python:
    nd_music_data = {
                'sound/music/a_promise_from_distant_days.ogg' : 'Sergey Eybog - A Promise From Distant Days',
                'sound/music/a_promise_from_distant_days_v2.ogg' : 'Sergey Eybog - A Promise From Distant Days v2',
                'sound/music/afterword.ogg' : 'Sergey Eybog - Afterword',
                'sound/music/always_ready.ogg' : 'Sergey Eybog - Always Ready',
                'sound/music/awakening_power.ogg' : 'Between August and December - Awakening Power',
                'sound/music/blow_with_the_fires.ogg' : 'Between August and December – Blow with the Fires',
                'sound/music/confession.ogg' : 'Sergey Eybog - Confession',
                'sound/music/dance_of_fireflies.ogg' : 'Sergey Eybog - Dance Of Fireflies',
                'sound/music/doomed_to_be_defeated.ogg' : 'Between August and December - Doomed to be Defeated',
                'sound/music/door_to_nightmare.ogg' : 'Sergey Eybog - Door To Nightmare',
                'sound/music/doubt_everyone.ogg' : 'Sergey Eybog - Doubt Everyone',
                'sound/music/drown.ogg' : 'Sergey Eybog - Drown',
                'sound/music/eat_some_trouble.ogg' : 'Sergey Eybog - Eat Some Troubles!',
                'sound/music/eternal_longing.ogg' : 'Between August and December - Eternal Longing',
                'sound/music/everlasting_summer.ogg' : 'Sergey Eybog - Everlasting Summer',
                'sound/music/feeling_good.ogg' : 'Sergey Eybog - Feeling Good',
                'sound/music/faceless.ogg' : 'Between August and December - Faceless',
                'sound/music/farewell_to_the_past_short.ogg' : 'Sergey Eybog - Farewell To The Past(edit)',
                'sound/music/farewell_to_the_past.ogg' : 'Sergey Eybog - Farewell To The Past',
                'sound/music/forest_maiden.ogg' : 'Sergey Eybog - Forest Maiden',
                'sound/music/gentle_predator.ogg' : 'Between August and December - Gentle Predator',
                'sound/music/get_to_know_me_better.ogg' : 'Sergey Eybog - Get To Know Me Better',
                'sound/music/glimmering_coals.ogg' : 'Between August and December - Glimmering Coals',
                'sound/music/goodbye_home_shores.ogg' : 'Sergey Eybog - Goodbye Home Shores',
                'sound/music/heather.ogg' : 'Between August and December - Heather',
                'sound/music/i_dont_blame_you.ogg' : "Sergey Eybog - I Don't Blame You",
                'sound/music/i_want_to_play.ogg' : 'Sergey Eybog - I Want To Play',
                'sound/music/into_the_unknown.ogg' : 'Between August and December - Into the Unknown',
                'sound/music/just_think.ogg' : 'Sergey Eybog - Just Think',
                'sound/music/vzveites_kostrami.ogg' : 'Неизвестен - Взвейтесь кострами',
                'sound/music/lets_be_friends.ogg' : "Sergey Eybog - Let's Be Friends",
                'sound/music/lightness.ogg' : 'Between August and December - Lightness',
                'sound/music/lightness_radio.ogg' : 'Between August and December - Lightness(radio bus)',
                'sound/music/meet_me_there.ogg' : 'Sergey Eybog - Meet Me There',
                'sound/music/memories.ogg' : 'Sergey Eybog - Memories',
                'sound/music/memories_piano_outdoors.ogg' : 'Sergey Eybog - Memories(piano outdoors)',
                'sound/music/miku_song_flute.ogg' : 'Песня Мику без голоса',
                'sound/music/miku_song_voice.ogg' : 'Песня Мику с голосом', 
                'sound/music/dinner_horn_processed.ogg' : 'Горн в столовую',
                'sound/music/my_daily_life.ogg' : 'Sergey Eybog - My Daily Life',
                'sound/music/mystery_girl.ogg' : 'Sergey Eybog - Mystery Girl',
                'sound/music/no_tresspassing.ogg' : 'Sergey Eybog - No Trespassing',
                'sound/music/orchid.ogg' : 'Between August and December - Orchid',
                'sound/music/pile.ogg' : 'Between August and December - Pile',
                'sound/music/raindrops.ogg' : 'Sergey Eybog - Raindrops',
                'sound/music/reflection_on_water.ogg' : 'Sergey Eybog - Reflection On Water',
                'sound/music/reminiscences.ogg' : 'Sergey Eybog - Reminiscences',
                'sound/music/revenga.ogg' : 'Неизвестен - Revenga',
                'sound/music/scarytale.ogg' : 'Between August and December - ScaryTale',
                'sound/music/she_is_kind.ogg' : 'Sergey Eybog - She Is Kind',
                'sound/music/silhouette_in_sunset.ogg' : 'Sergey Eybog - Silhouette In Sunset',
                'sound/music/smooth_machine.ogg' : 'Sergey Eybog - Smooth Machine',
                'sound/music/so_good_to_be_careless.ogg' : 'Sergey Eybog - So Good To Be Careless',
                'sound/music/sparkles.ogg' : 'Неизвестен - Sparkles',
                'sound/music/sunny_day.ogg' : 'Between August and December - Sunny Day',
                'sound/music/sweet_darkness.ogg' : 'Sergey Eybog - Sweet Darkness',
                'sound/music/take_me_beautifully.ogg' : 'Sergey Eybog - Take Me Beautifully',
                'sound/music/that_s_our_madhouse.ogg' : "Between August and December - That's Our Madhouse",
                'sound/music/timid_girl.ogg' : 'Sergey Eybog - Timid Girl',
                'sound/music/torture.ogg' : 'Between August and December - Torture',
                'sound/music/trapped_in_dreams.ogg' : 'Sergey Eybog - Trapped In Dreams',
                'sound/music/tried_to_bring_it_back.ogg' : 'Sergey Eybog - I Tried To Bring It Back',
                'sound/music/two_glasses_of_melancholy.ogg' : 'Sergey Eybog - Two Glasses Of Melancholy',
                'sound/music/waltz_of_doubts.ogg' : 'Sergey Eybog - Waltz Of Doubts',
                'sound/music/went_fishing_caught_a_girl.ogg' : 'Sergey Eybog - Went Fishing, Caught A Girl',
                'sound/music/what_do_you_think_of_me.ogg' : 'Sergey Eybog - What Do You Think Of Me',
                'sound/music/you_lost_me.ogg' : 'Sergey Eybog - You Lost Me',
                'sound/music/you_won_t_let_me_down.ogg' : "Between August and December - You Won't Let Me Down",
                'sound/music/your_bright_side.ogg' : 'Sergey Eybog - Your Bright Side',
                'sound/music/410.ogg' : 'Between August and December - 410',
                'sound/music/everlasting_summer_op_edition.ogg' : 'Everlasting Summer opening',
                ND_MUSIC + 'nd_veselo_dohuya.mp3' : 'Просто веселая музыка',
                ND_MUSIC + 'i_crash_u_crash.mp3' : 'Lil Peep - I crash you crash',
                ND_MUSIC + 'i_dont_sleep.ogg' : 'Flog The Rapper - I Don` t Sleep',
                ND_MUSIC + 'in_my_zone.ogg' : 'VIPN - In My Zone',
                ND_MUSIC + 'komarova.mp3' : 'Игорь Скляр - Комарово',
                ND_MUSIC + 'king_winner.ogg' : 'Вадим Мулерман - Король Победитель',
                ND_MUSIC + 'jzone.ogg' : 'Jayswan - Zone',
                ND_MUSIC + 'b3_floodmoor.mp3' : 'Borderlands 3 - Floodmoor',
                ND_MUSIC + 'b3_interlude_2.mp3' : 'Borderlands 3 - Interlude',
                ND_MUSIC + 'b3_meridian.mp3' : 'Borderlands 3 - Meridian',
                ND_MUSIC + 'bass_i_love_you.mp3' : 'Basstronics - Bass I Love You',
                ND_MUSIC + 'kossandra_part_2.mp3' : 'Miyagi & Andy Panda - Кассандра',
                ND_MUSIC + 'kossandra_part_2.mp3' : 'Miyagi & Andy Panda - Кассандра',
                ND_MUSIC + 'butterfly.ogg' : 'BONES - Butterfly',
                ND_MUSIC + 'ca_fall_gsynth.mp3' : 'ConcernedApe - Fall (Ghost Synth)',
                ND_MUSIC + 'ca_nocturne_of_ice.mp3' : 'ConcernedApe - Nocturne Of Ice',
                ND_MUSIC + 'ca_wind.mp3' : 'ConcernedApe - Wind',
                ND_MUSIC + 'catacombs_dark_ambient.ogg' : 'Pavel Wostrow - Catacombs',
                ND_MUSIC + 'Disco_1.ogg' : 'Юрий Шатунов - Белые Розы',
                ND_MUSIC + 'Disco_2.ogg' : 'Carrie - Europe',
                ND_MUSIC + 'Disco_3.ogg' : 'Real Life - Catch me I`m Falling',
                ND_MUSIC + 'Disco_4.ogg' : 'Pink Floyd - Another Brick In The Wall',
                ND_MUSIC + 'dv_camp_end.ogg' : 'BONES - CtrlAltDelete',
                ND_MUSIC + 'early_morning.ogg' : 'TERNOX - Early Morning',
                ND_MUSIC + 'eternal.ogg' : 'RUDE - Eternal Youth',
                ND_MUSIC + 'evertale.ogg' : 'Undertale - Main Theme',
                ND_MUSIC + 'fall_asleep.ogg' : 'Группа \"Перекресток\" - Потерянный рай',
                ND_MUSIC + 'glori_morning.ogg' : 'Waterflame - Glorious Morning',
                ND_MUSIC + 'GW_pyramid.ogg' : 'GW - Pyramid',
                ND_MUSIC + 'harmony_1.ogg' : 'Soul of Serendipity - Harmony',
                ND_MUSIC + 'intheend_piano.ogg' : 'Linkin Park - In The End (Piano)',
                ND_MUSIC + 'late_again.ogg' : 'towser - late again',
                ND_MUSIC + 'lonely.ogg' : 'idealism - Lonely',
                ND_MUSIC + 'looking_for_the_miracle.ogg' : 'Looking For The Miracle',
                ND_MUSIC + 'love_knows_no_boundaries.mp3' : 'Denis Baklin - Love Knows No Boundaries (TS)',
                ND_MUSIC + 'love_theme_1.ogg' : 'Justin Stone - On Your Own',
                ND_MUSIC + 'LP_in_the_end.mp3' : 'Linkin Park - In The End (Remix)',
                ND_MUSIC + 'LP_in_the_end_Full.ogg' : 'Linkin Park - In The End (Remix)',
                ND_MUSIC + 'lzr_pznp.mp3' : 'LIZER - Под звуки наших поцелуев',
                ND_MUSIC + 'map_music_postal.ogg' : 'Postal 2 - Map Music',
                ND_MUSIC + 'me_suicideboys.ogg' : 'Jack Wall - Suicide Mission',
                ND_MUSIC + 'mma_there.mp3' : 'Three Days Grace - Animal I have become',
                ND_MUSIC + 'mood_depr.ogg' : 'Многоточие - Щемит в душе тоска',
                ND_MUSIC + 'mood_dream.ogg' : 'Last Summer Mod - Dream (Моя любимая)',
                ND_MUSIC + 'mood_goodover.ogg' : 'Кино - Последний Герой',
                ND_MUSIC + 'mood_play.ogg' : 'Billy Preston - Outa-Space',
                ND_MUSIC + 'mood_romantic.ogg' : 'Кино - Пачка Сигарет',
                ND_MUSIC + 'mood_run.ogg' : 'Виктор Цой - Стук',
                ND_MUSIC + 'mood_sad.ogg' : 'I Am Waiting For You Last Summer - And Nothing Changed Yet',
                ND_MUSIC + 'mood_sad1.ogg' : 'Jorg Wohler - Angels Arrive',
                ND_MUSIC + 'mood_serendipity.ogg' : 'ЛСП - Тело',
                ND_MUSIC + 'mood_strange.ogg' : 'Кино - Апрель',
                ND_MUSIC + 'mood_think.ogg' : 'Кино - Кукушка',
                ND_MUSIC + 'mus_alone.ogg' : 'Myamo & Ganju - Someone',
                ND_MUSIC + 'nd_1219_music.ogg' : 'Вадим Wolf - За правду на весах (1219 Минус)',
                ND_MUSIC + 'nd_a_painful_story.ogg' : 'Paul Kreminski - A Painful Story',
                ND_MUSIC + 'nd_an_novichok.mp3' : 'Skillet - Hero',
                ND_MUSIC + 'nd_atmos_rework.mp3' : 'Atmosphere Ambient',
                ND_MUSIC + 'nd_attack_of_the_unknown.mp3' : 'Denis Baklin - Attack of the Unknown (TS)',
                ND_MUSIC + 'nd_beach_of_Love.mp3' : 'Denis Baklin - Beach of Love (TS)',
                ND_MUSIC + 'nd_blackefio_chto.mp3' : 'April Rain - Deadman On Vacation',
                ND_MUSIC + 'nd_bye_horus.mp3' : 'Жека Расту - Ванлав (Minus)',
                ND_MUSIC + 'nd_crippy_er.mp3' : 'Valezart - Haunted Manor',
                ND_MUSIC + 'nd_creepy_embient.mp3' : 'Dark Ambient',
                ND_MUSIC + 'nd_crybaby.mp3' : 'Lil Peep - Crybaby',
                ND_MUSIC + 'nd_dance_in_the_forest.mp3' : 'Denis Baklin - Dance In The Forest (TS)',
                ND_MUSIC + 'nd_db_moonlight.mp3' : 'Denis Baklin - Moonlight (TS)',
                ND_MUSIC + 'nd_faded_revival.ogg' : 'CJ AKO - Тебе (Пианино)',
                ND_MUSIC + 'nd_ddv_bb1.mp3' : 'Matt Quentin - Waves',
                ND_MUSIC + 'nd_deep_despair.ogg' : 'БРАТУБРАТ - Воскресенье (Minus)',
                ND_MUSIC + 'nd_fighting_withsh.ogg' : 'Jeremy Soule - Tooth and Claw',
                ND_MUSIC + 'nd_fuckyou_music.ogg' : 'Eduard Studio - Illuminati',
                ND_MUSIC + 'nd_hard_rage.ogg' : 'Dead By April - Mystery',
                ND_MUSIC + 'nd_hatters_instrumental.mp3' : 'The Hatters - Instrumental',
                ND_MUSIC + 'nd_horror_raskaz_us.mp3' : 'Valezart - Haunted Manor',
                ND_MUSIC + 'nd_icuc_d5.mp3' : 'Sadstation & VMZ - Depressao (Minus)',
                ND_MUSIC + 'nd_in_catacombs.mp3' : 'Catacombs Ambient',
                ND_MUSIC + 'nd_lct_wart.mp3' : 'Denis Baklin - Last Minutes (TS)',
                ND_MUSIC + 'nd_lightsout.mp3' : 'Gwala Vision - Lights Out',
                ND_MUSIC + 'nd_loos_badend.mp3' : 'Denis Baklin - What I`ve Done (TS)',
                ND_MUSIC + 'nd_losing_you.ogg' : 'Dead By April - Losing You',
                ND_MUSIC + 'nd_main_d5_music.mp3' : 'Oxxxymiron - Накануне',
                ND_MUSIC + 'nd_meeting_miriam.mp3' : 'Carter Burwell - Meeting Miriam',
                ND_MUSIC + 'nd_miku_last_hope.mp3' : 'Denis Baklin - Last Hope (Miku) (TS)',
                ND_MUSIC + 'nd_my_secrets.mp3' : 'Denis Baklin - My Secrets (TS)',
                ND_MUSIC + 'nd_nachalo_1.mp3' : 'SoSoCrazyBoy - Sinkingrose',
                ND_MUSIC + 'nd_path_to_the_stars.mp3' : 'Denis Baklin - Path To The Stars (TS)',
                ND_MUSIC + 'nd_prancing_clouds.mp3' : 'Denis Baklin - Prancing Clouds (TS)',
                ND_MUSIC + 'nd_prikolist_ah.mp3' : 'Bobby Prince  - The Healer Stalks',
                ND_MUSIC + 'nd_rainy_morning.mp3' : 'Denis baklin - Rainy Morning (TS)',
                ND_MUSIC + 'nd_sad_dream.mp3' : 'Denis baklin - Meeting Miku (TS)',
                ND_MUSIC + 'nd_sigaret_steal.mp3' : 'Shawn Lee feat. Ben Morfitt - Bully Theme',
                ND_MUSIC + 'nd_siyay_lol.mp3' : 'Ramil` - Сияй',
                ND_MUSIC + 'nd_something_ok.mp3' : 'ADM1TR1POW - Depressed',
                ND_MUSIC + 'nd_sp_r.ogg' : 'Гостья из будущего - Ёжик',
                ND_MUSIC + 'nd_ultra_epicmusic.mp3' : 'Denis Baklin - Colosseum (TS)',
                ND_MUSIC + 'nd_ussr_forward.mp3' : 'Denis Baklin - USSR Forward (TS)',
                ND_MUSIC + 'nid_aop.mp3' : 'Nicole Dollanganger  - Angels Of Porn II',
                ND_MUSIC + 'notdreamovsky_saspens_1.ogg' : 'Borislav Slavov  - New York Aftermath',
                ND_MUSIC + 'oblivion.ogg' : 'Lily Potter - oblivion',
                ND_MUSIC + 'old_camp_ambient_music.ogg' : 'Ambient Sound Center - Dark Room',
                ND_MUSIC + 'old_camp_inside_music.ogg' : 'Horror Music Orchestra - Chopped Up',
                ND_MUSIC + 'outsmull_lose_me_in_yourself.mp3' : 'OutSmull Beats - Lose Me In Yourself',
                ND_MUSIC + 'prepare_the_stage_of_night.mp3' : 'Atrium Carceri - Prepare The Stage Of Night',
                ND_MUSIC + 'princest.ogg' : 'Электрофорез - Русская Принцесса',
                ND_MUSIC + 'promise_silent_hill_cover.ogg' : 'Konami Kukeiha Club - Promise',
                ND_MUSIC + 'remnants_of_summer.ogg' : 'Jishle - Remnants Of Summer',
                ND_MUSIC + 'RF_decision_us_1.ogg' : 'Arabian Trap - Kollo',
                ND_MUSIC + 'RF_decision_us_2.ogg' : 'BONES - Calcium',
                ND_MUSIC + 'RF_memory_1.ogg' : 'Scorpions - Holiday',
                ND_MUSIC + 'RF_memory_2.ogg' : 'Scorpions - Holiday',
                ND_MUSIC + 'RF_rage.ogg' : 'The Kills - Cheap And Cheerful (Remix)',
                ND_MUSIC + 'RF_rm_1.ogg' : 'BONES - Air',
                ND_MUSIC + 'RF_wake.ogg' : '$uicideboy$ - Am/Pm',
                ND_MUSIC + 'sleep_sharing.mp3' : 'Oxxxymiron - Обмен сном (Remix by Foradream)',
                ND_MUSIC + 'son_kanabis.ogg' : 'Call of Duty + Linkin Park - Numb',
                ND_MUSIC + 'stairway_to_the_ussr.ogg' : 'Boogie Belgique - Stairway To The USSR',
                ND_MUSIC + 'stigmata_september.mp3' : 'Stigmata - Сентябрь',
                ND_MUSIC + 'the_most_musterious_song_on_the_internet.mp3' : 'The Most Musterious Song On The Internet',
                ND_MUSIC + 'top_stressedout.mp3' : 'Twenty One Pilots - Stressed Out',
                ND_MUSIC + 'toxicity_1.ogg' : 'Lil Peep - Toxic City',
                ND_MUSIC + 'toxicity_2.ogg' : 'Lil Peep - Toxic City',
                ND_MUSIC + 'two_of_us.ogg' : 'dizralph.c - Two Of Us',
                ND_MUSIC + 'us_dreaming.ogg' : 'Мод \"Мы - это главное\" - us_dreaming.ogg',
                ND_MUSIC + 'USSR_1.ogg' : 'Цой - Восьмиклассница',
                ND_MUSIC + 'vs_vs4dead.mp3' : 'Velial Squad - VS4DEATH',
                ND_MUSIC + 'vs_pulsar.mp3' : 'Velial Squad - Pulsar',
                ND_MMUSIC + 'menu_nd_1.ogg' : 'Denis Baklin - Our Bright Side (Day)',
                ND_MMUSIC + 'menu_nd_3.ogg' : 'Denis Baklin - Our Bright Side (Sunset)',
                ND_MMUSIC + 'menu_nd_2.ogg' : 'Denis Baklin - Our Bright Side (Night)',
                ND_MUSIC + 'gimn.ogg' : 'Гимн СССР',
                ND_MUSIC + 'mood_fight_1.ogg' : 'Linkin park - Lying From You',
                ND_MUSIC + 'mood_funny.ogg' : 'Кино - Место для шага вперёд',
                ND_MUSIC + 'White_Atlantis.ogg' : 'Sergey Cheremisinov - White Atlantis',
                ND_MUSIC + 'RF_club_music_1.ogg' : 'BONES - HDMI',
                ND_MUSIC + 'nd_ss_ss_ss.mp3' : 'Velial Squad - Что-то не так',
                ND_MUSIC + 'cs_large_magellanic_cloud.mp3' : "Curtis Schweitzer — Large Magellanic Cloud",
                ND_MUSIC + 'oc_with_her.mp3' : "OVERRCLOCK — With Her",
                ND_MUSIC + 'b3_the_firehawk_rises.mp3' : "Borderlands 3 (OST) — The Firehawk Rises",
                ND_MUSIC + 'cs_large_magellanic_cloud.mp3' : "Curtis Schweitzer — Large Magellanic Cloud",
                ND_MUSIC + 'da_the_colors_of_the_evening.mp3' : "Daminika — The Colors Of The Evening",
                ND_MUSIC + 'gothurted_imd.mp3' : "gothurted — Inside my dream",
                ND_MUSIC + 'rf_detstvo_piano.mp3' : "Rauf & Faik — Детство (Piano)",
                ND_MUSIC + 'top_leave_the_city.mp3' : "Twenty One Pilots - Leave The City",
                ND_MUSIC + 'top_legend.mp3' : "Twenty One Pilots - Legend",
                "mods/notdream/addons/official_c2_content/audio/music/" + 'nd_archaichno.mp3': "Gde Fantom? - Eto Tak Arkhaichno",
                "mods/notdream/addons/official_c2_content/audio/music/" + 'nd_c2_part1_start.mp3': "20TOKENS - Розовые Сны",
                "mods/notdream/addons/official_c2_content/audio/music/" + 'sy_was_a_second_idea.mp3': "Symbo`1 - Was a second idea",
                ND_MUSIC + 'top_bandito_slowed.mp3' : "Twenty One Pilots - Bandito",
                ND_MUSIC + 'Outsider_No_More_Cyber.mp3' : "P.T. Adamczyk - Outsider No More",
                ND_MUSIC + 'soma_awake.mp3' : "Mikko Tarmia - Awaken",
                #Awaken - Mikko Tarmia
                }

    def nd_show_music(st, at):
        music_is_play = renpy.music.is_playing(channel='music')
        if music_is_play:
            what_music_play = renpy.music.get_playing(channel='music')
            if what_music_play not in nd_music_data:
                what_music_play = 'Шазам не знает такого трека'
            else:
                what_music_play = nd_music_data[what_music_play]
        else:
            what_music_play = None
        if what_music_play != None:
            img = Text('{size=24}%s{/font}' % (what_music_play), style="nd_helvuelight_whit")
        else:
            img = Text('')

        return img, .1

## TIME CHANGE CONTAINER
    def nd_change_time(target=None):
        if target == "day":
            nd_day_time()
        elif target == "sunset":
            nd_sunset_time()
        elif target == "night":
            nd_night_time()
        else:
            nd_prolog_time()

    def nd_day_time():
        global notdream_UIpath
        day_time()
        persistent.sprite_time = "day"

        if persistent.nd_cursor_style == "normal":
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_day_v2.png', 0, 0)
        else:
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_day_v2.png', 30, 30)

    def nd_sunset_time():
        global notdream_UIpath
        sunset_time()
        persistent.sprite_time = "sunset"

        if persistent.nd_cursor_style == "normal":
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_evening_v2.png', 0, 0)
        else:
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_evening_v2.png', 30, 30)

    def nd_night_time():
        global notdream_UIpath
        night_time()
        persistent.sprite_time = "night"

        if persistent.nd_cursor_style == "normal":
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_night_v2.png', 0, 0)
        else:
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_night_v2.png', 30, 30)

    def nd_prolog_time():
        global notdream_UIpath
        prolog_time()
        persistent.sprite_time = "night"

        if persistent.nd_cursor_style == "normal":
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/normal/normal_cursor_prologue_v2.png', 0, 0)
        else:
            config.mouse_displayable = MouseDisplayable(notdream_UIpath + 'cur/circle/circle_cursor_prologue_v2.png', 30, 30)

init:
## POST ANIMATED BG`S IMAGES CONTAINER
    image nd_gametime = DynamicDisplayable(show_gametime)
    image nd_game_music = DynamicDisplayable(nd_show_music)
    image nd_particles = nd_particles("mods/notdream/images/particles/dust_particle.png")
## CUSTOM TRANSITIONS CONTAINER
    $ nd_effect_1           = ImageDissolve("mods/notdream/images/effects/nd_effect_1.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_1_pause     = ImageDissolve("mods/notdream/images/effects/nd_effect_1.png", 2.5, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_2           = ImageDissolve("mods/notdream/images/effects/nd_effect_2.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_3           = ImageDissolve("mods/notdream/images/effects/nd_effect_3.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_3_reverse   = ImageDissolve("mods/notdream/images/effects/nd_effect_3.png", 1.0, ramplen = 25, reverse = True, alpha = True)
    $ nd_effect_4_pause     = ImageDissolve("mods/notdream/images/effects/nd_effect_4.png", 2.5, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_4           = ImageDissolve("mods/notdream/images/effects/nd_effect_4.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_5           = ImageDissolve("mods/notdream/images/effects/nd_effect_5.png", 1.0, ramplen = 25, reverse = False, alpha = True)
    $ nd_effect_5_reverse   = ImageDissolve("mods/notdream/images/effects/nd_effect_5.png", 1.0, ramplen = 25, reverse = True, alpha = True)
    $ dissolve3             = Dissolve(3)
    $ dissolve4             = Dissolve(4)
    $ dissolve5             = Dissolve(5)
    $ dissolve6             = Dissolve(6)
## Routepoints window container
    python:
        ## defs
        def nd_routepoints_window_off():
            persistent.window_nd = False
            while editoverlay_nd in config.overlay_functions:
                config.overlay_functions.remove(editoverlay_nd)

        def nd_routepoints_window_on():
            persistent.window_nd = True
            while editoverlay_nd in config.overlay_functions:
                config.overlay_functions.remove(editoverlay_nd)
            config.overlay_functions.append(editoverlay_nd)

        # vars
        nd_rp = {}
        nd_rp['dvrr']           = "Очки Алисы"
        nd_rp['usrr']           = "Очки Ульяны (1-3 д.)"
        nd_rp['nd_us_flaggs']   = "Очки Ульяны (3-5 д.)"
        nd_rp['nir']            = "Очки Нирваны"
        nd_rp['nd_stoic']       = "Очки стоицизма"
        nd_rp['nd_scept']       = "Очки скептицизма"
        nd_rp['nepodhod_87']    = "Wasted-показатель"
        nd_sk = ['dvrr', 'usrr', 'nd_us_flaggs', 'nir', 'nd_stoic', 'nd_scept', 'nepodhod_87']

        def editoverlay_nd():
            ui.vbox(ypos=2)

            nd_sw = [dvrr, usrr, nd_us_flaggs, nir, nd_stoic, nd_scept, nepodhod_87]
            for widg,val in zip(nd_sk,nd_sw):
                ui.vbox()
                ui.button(clicked=None, xpadding=4)
                ui.text("%s: %d" % (nd_rp[widg], val), style="button_text", size=14)
                ui.close()
            ui.close()

        # while editoverlay_nd in config.overlay_functions:
        #     config.overlay_functions.remove(editoverlay_nd)
        #config.overlay_functions.append(editoverlay_nd)

## - - - CHARACTERS ▼
## Custom mod characters container
    $ nd_il             =           Character(u'Илья', color="8FBC8F", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ fx_il             =           Character(u'Илья', color="b7bc8f", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ fx_pe             =           Character(u'Незнакомец', color="b7bc8f", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ fx_pe1            =           Character(u'Незнакомец', color="bcb78f", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ fx_pe2            =           Character(u'Незнакомец', color="8fbc96", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ cassw             =           Character(u'Кассир', color="FFA500", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ je_stor           =           Character(u'Кассир (в ювелирном)', color="6495ed", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ fx_il             =           Character(u'Илья', color="bcb78f", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ psih              =           Character(u'Психотерапевт', color="7B68EE", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ testpers3         =           Character(u'Девушка', color="FFA500", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ vg                =           Character(u'Внутренний голос', color="808080", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ toriel            =           Character(u'Помощь', color="808080", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ fiz               =           Character(u'Физрук', color="919192", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ muz               =           Character(u'Мужчина', color="919192", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ pov               =           Character(u'Повариха', color="6495ed", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ stranger          =           Character(u'Незнакомец', color="0026FF", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ vst               =           Character(u'Василий', color="0026FF", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ parr              =           Character(u'Парень', color="5c5cff", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ strange_g         =           Character(u'Голос', color="004AA6", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ dream_voices      =           Character(u'Голоса', color="0426BA", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ dy                =           Character(u'Голос из динамика', color="11A41B", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ hgt               =           Character(u'Вместе', color="2587CB", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ grk               =           Character(u'Пацан', color="808080", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ snk               =           Character(u'Саша', color="999999", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ pioneer_he        =           Character(u'Пионер', color="954B0F", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ pioneer_she       =           Character(u'Пионерка', color="1AAF9F", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ rost              =           Character(u'Ростислав', color="88171F", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ tolpa             =           Character(u'Толпа', color="D60D0D", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_ms             =           Character(u'Машинист', color="ffd919", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_gri            =           Character(u'Григорий', color="fde910", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ vst_lar           =           Character(u'Василий', color="e8ab56", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ il_for_r          =           "{color=8FBC8F}Илья{/color}"
    $ nd_da             =           Character(u'Даша', color="7CC868", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_whoer          =           Character(u'...', color="ededed", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_prophet        =           Character(u'Пророк', color="005aeb", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_anmt           =           Character(u'Вожатая 2-го отряда', color="#d57c3c", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
    $ nd_barplady       =           Character(u'Парикмахерша', color="#3cd5a7", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")
## - - - AUDIO ▼
## AudioFolders init container // nds_list[] | ndm_list[] | nda_list[]
    $ nds_list  =   nd_form_files_list(ND_SOUNDS)
    $ ndm_list  =   nd_form_files_list(ND_MUSIC)
    $ nda_list  =   nd_form_files_list(ND_AMBIENCE)
## Interface audio container
    $ menu_nd_1                         = ND_UI                 +       "Main_menu/menu_nd_1.ogg"
    $ menu_nd_2                         = ND_UI                 +       "Main_menu/menu_nd_2.ogg"
    $ menu_nd_3                         = ND_UI                 +       "Main_menu/menu_nd_3.ogg"
    $ ui_click                          = ND_UI                 +       "Main_menu/ui_click.ogg"
    $ nd_ui_hover                       = ND_UI                 +       "Main_menu/nd_ui_hover.mp3"
    $ ui_newgame_click                  = ND_UI                 +       "Main_menu/ui_newgame_click.ogg"
    $ ui_error                          = ND_UI                 +       "Main_menu/ui_error.ogg"
## Modification audio channels and mixes container
    $ renpy.music.register_channel("back_ambience", "ambience", True)
    $ renpy.music.register_channel("nd_ui_sounds", "sound", False)

    $ renpy.music.set_mixer(90,"nd_voice_mixer")
    $ renpy.music.register_channel("nd_voice", "nd_voice_mixer", False)

## - - - TRANSFORMS ▼
## Bus shake effect container
    transform nd_bus_vpunch:
        align( .5, .53) zoom 1.1
        ease 0.3 zoom 1.1 align( .5, .47)
        pause(0.2)
        ease 0.3 zoom 1.1 align( .5, .53)
        pause(0.2)
        repeat

    transform nd_logo_transform:
        xalign 0.5 yalign 0.5 zoom 1.6 alpha 0.0
        ease 0.5 zoom 1.0 alpha 1.0
        pause 3
        ease 0.5 zoom 0.5 alpha 0.0

## - - - FONTS ▼
## Custom fonts container
    $ nd_Script                                             =       notdream_fontspath + "nd_mainmenu_shrift.ttf"

    $ style.dreammod_text_hover                             =       Style(style.default)
    $ style.dreammod_text_hover.color                       =       "ffffff"
    $ style.dreammod_text_hover.font                        =       notdream_fontspath + "dreammod_text.ttf"
    $ style.dreammod_text_hover.size                        =       45
    $ style.dreammod_text_hover.drop_shadow                 =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.dreammod_text_hover.drop_shadow_color           =       "#000"
    $ style.dreammod_text_hover.kerning                     =       1

    $ style.dreammod_text_idle                              =       Style(style.default)
    $ style.dreammod_text_idle.color                        =       "9b9b9b"
    $ style.dreammod_text_idle.font                         =       notdream_fontspath  + "dreammod_text.ttf"
    $ style.dreammod_text_idle.size                         =       45
    $ style.dreammod_text_idle.drop_shadow                  =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.dreammod_text_idle.drop_shadow_color            =       "#000"
    $ style.dreammod_text_idle.kerning                      =       1

    $ style.dreamname_nazv                                  =       Style(style.default)
    $ style.dreamname_nazv.font                             =       notdream_fontspath + "Everlasting_Summer1.ttf"
    $ style.dreamname_nazv.color                            =       "010107"
    $ style.dreamname_nazv.size                             =       40
    $ style.dreamname_nazv.drop_shadow                      =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.dreamname_nazv.drop_shadow_color                =       "#000"
    $ style.dreamname_nazv.kerning                          =       1

    $ style.nd_calibri_text                                 =       Style(style.default)
    $ style.nd_calibri_text.color                           =       "9b9b9b"
    $ style.nd_calibri_text.font                            =       notdream_fontspath + "calibri_font.ttf"
    $ style.nd_calibri_text.size                            =       45
    $ style.nd_calibri_text.drop_shadow                     =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.nd_calibri_text.drop_shadow_color               =       "#000"
    $ style.nd_calibri_text.kerning                         =       1

    $ style.notes_text                                      =       Style(style.default)
    $ style.notes_text.color                                =       "fedc7c"
    $ style.notes_text.font                                 =       notdream_fontspath + "notes.ttf"
    $ style.notes_text.size                                 =       25
    $ style.notes_text.drop_shadow                          =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.notes_text.drop_shadow_color                    =       "#000"
    $ style.notes_text.kerning                              =       1


    $ style.dreammod_text_zago                              =       Style(style.default)
    $ style.dreammod_text_zago.color                        =       "9b9b9b"
    $ style.dreammod_text_zago.font                         =       notdream_fontspath  + "dreammod_text.ttf"
    $ style.dreammod_text_zago.size                         =       75
    $ style.dreammod_text_zago.drop_shadow                  =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.dreammod_text_zago.drop_shadow_color            =       "#000"
    $ style.dreammod_text_zago.kerning                      =       1

    $ style.nd_text_big_save_load                           =       Style(style.default)
    $ style.nd_text_big_save_load.font                      =       "mods/notdream/fonts/nd_mainmenu_shrift.ttf"
    $ style.nd_text_big_save_load.size                      =       75
    $ style.nd_text_big_save_load.color                     =       "#ffffff"
    $ style.nd_text_big_save_load.hover_color               =       "#808080"
    $ style.nd_text_big_save_load.selected_color            =       "#ffffff"
    $ style.nd_text_big_save_load.selected_idle_color       =       "#ffffff"
    $ style.nd_text_big_save_load.selected_hover_color      =       "#808080"
    $ style.nd_text_big_save_load.insensitive_color         =       "#ffffff"

    $ style.nd_button_None                                  =       Style(style.button)
    $ style.nd_button_None.background                       =       None
    $ style.nd_button_None.hover_background                 =       None
    $ style.nd_button_None.selected_background              =       None
    $ style.nd_button_None.selected_hover_background        =       None
    $ style.nd_button_None.selected_idle_background         =       None

    $ style.nd_save_load_button                             =       Style(style.button)
    $ style.nd_save_load_button.background                  =       "mods/notdream/UserInterface/gui/Load/nd_load_Buttol_idle.png"
    $ style.nd_save_load_button.hover_background            =       "mods/notdream/UserInterface/gui/Load/nd_load_Buttol_hover.png"
    $ style.nd_save_load_button.selected_background         =       "mods/notdream/UserInterface/gui/Load/nd_load_Buttol_selected.png"
    $ style.nd_save_load_button.selected_hover_background   =       "mods/notdream/UserInterface/gui/Load/nd_load_Buttol_selected.png"
    $ style.nd_save_load_button.selected_idle_background    =       "mods/notdream/UserInterface/gui/Load/nd_load_Buttol_selected.png"

    $ style.nd_text_small_save_load                         =       Style(style.default)
    $ style.nd_text_small_save_load.font                    =       "mods/notdream/fonts/nd_mainmenu_shrift.ttf"
    $ style.nd_text_small_save_load.size                    =       60
    $ style.nd_text_small_save_load.color                   =       "#ffffff"
    $ style.nd_text_small_save_load.hover_color             =       "#808080"
    $ style.nd_text_small_save_load.selected_color          =       "#ffffff"
    $ style.nd_text_small_save_load.selected_idle_color     =       "#ffffff"
    $ style.nd_text_small_save_load.selected_hover_color    =       "#808080"
    $ style.nd_text_small_save_load.insensitive_color       =       "#ffffff"

    $ style.nd_text_quick_menu                              =       Style(style.default)
    $ style.nd_text_quick_menu.font                         =       "mods/notdream/fonts/nd_mainmenu_shrift.ttf"
    $ style.nd_text_quick_menu.size                         =       55
    $ style.nd_text_quick_menu.color                        =       "#dedede"
    $ style.nd_text_quick_menu.hover_color                  =       "#aeaeae"
    $ style.nd_text_quick_menu.selected_color               =       "#dedede"
    $ style.nd_text_quick_menu.selected_idle_color          =       "#dedede"
    $ style.nd_text_quick_menu.selected_hover_color         =       "#aeaeae"
    $ style.nd_text_quick_menu.insensitive_color            =       "#dedede"

    $ style.nd_helvuelight                                  =       Style(style.default)
    $ style.nd_helvuelight.color                            =       "9b9b9b"
    $ style.nd_helvuelight.font                             =       notdream_fontspath  + "nd_helvuelight.ttf"
    $ style.nd_helvuelight.size                             =       25
    $ style.nd_helvuelight.drop_shadow                      =       [ (2, 2), (2, 2), (2, 2), (2, 2) ]
    $ style.nd_helvuelight.drop_shadow_color                =       "#0f0f0f"
    $ style.nd_helvuelight.kerning                          =       1

    $ style.nd_nant_bs                                      =       Style(style.default)
    $ style.nd_nant_bs.color                                =       "9b9b9b"
    $ style.nd_nant_bs.font                                 =       notdream_fontspath  + "nd_nant_bs.ttf"
    $ style.nd_nant_bs.size                                 =       75
    $ style.nd_nant_bs.drop_shadow                          =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.nd_nant_bs.drop_shadow_color                    =       "#000"
    $ style.nd_nant_bs.kerning                              =       1

    $ style.helveticaneueroman_idle                         =       Style(style.default)
    $ style.helveticaneueroman_idle.color                   =       "e5e5e5"
    $ style.helveticaneueroman_idle.font                    =       notdream_fontspath  + "helveticaneueroman.ttf"
    $ style.helveticaneueroman_idle.size                    =       30
    $ style.helveticaneueroman_idle.drop_shadow             =       [ (2, 2), (2, 2), (2, 2), (2, 2) ]
    $ style.helveticaneueroman_idle.drop_shadow_color       =       "#0f0f0f"
    $ style.helveticaneueroman_idle.kerning                 =       0.5

    $ style.helveticaneueroman_hover                        =       Style(style.default)
    $ style.helveticaneueroman_hover.color                  =       "9b9b9b"
    $ style.helveticaneueroman_hover.font                   =       notdream_fontspath  + "helveticaneueroman.ttf"
    $ style.helveticaneueroman_hover.size                   =       30
    $ style.helveticaneueroman_hover.drop_shadow            =       [ (2, 2), (2, 2), (2, 2), (2, 2) ]
    $ style.helveticaneueroman_hover.drop_shadow_color      =       "#0f0f0f"
    $ style.helveticaneueroman_hover.kerning                =       0.5

    $ style.nd_helvuelight_norm                             =       Style(style.default)
    $ style.nd_helvuelight_norm.color                       =       "f2f2f2"
    $ style.nd_helvuelight_norm.font                        =       notdream_fontspath  + "nd_helvuelight.ttf"
    $ style.nd_helvuelight_norm.size                        =       25
    $ style.nd_helvuelight_norm.drop_shadow_color           =       "#000"
    $ style.nd_helvuelight_norm.kerning                     =       1

    $ style.nd_helvuelight_whit                             =       Style(style.default)
    $ style.nd_helvuelight_whit.color                       =       "e5e5e5"
    $ style.nd_helvuelight_whit.font                        =       notdream_fontspath  + "nd_helvuelight.ttf"
    $ style.nd_helvuelight_whit.size                        =       25
    $ style.nd_helvuelight_whit.drop_shadow                 =       [ (2, 2), (2, 2), (2, 2), (2, 2) ]
    $ style.nd_helvuelight_whit.drop_shadow_color           =       "#0f0f0f"
    $ style.nd_helvuelight_whit.kerning                     =       1

    $ als_sirius_v3                                         =       notdream_fontspath  + "als_sirius_vf3.ttf"
    $ style.als_sirius_v3                                   =       Style(style.default)
    $ style.als_sirius_v3.kerning                           =       1
    $ style.als_sirius_v3.drop_shadow                       =       [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.als_sirius_v3.drop_shadow_color                 =       "#000"


init 1111 python:
## - - - ADDONS ▼
## parallax effects container
    class nd_MouseParallax(renpy.Displayable):
        def set(self, *args):
            self.xoffset, self.yoffset = 0.0, 0.0
            self.layer_info = args
            for i in self.layers():
                if i in config.layers + ["master2"]:
                    config.layers.remove(i)
            index = config.layers.index("master") + 1
            for xdist, ydist, layer in args:
                if not layer in config.layers:
                    config.layers.insert(index, layer)
                    index += 1
            config.layers.insert(index, "master2")

        def __init__(self, *args):
            super(renpy.Displayable, self).__init__()
            self.set(*args)
            config.overlay_functions.append(self.overlay)
            return

        def layers(self):
            layers = []
            for dx, dy, layer in self.layer_info:
                layers.insert(0, layer)
            return layers

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def parallax(self, xdist, ydist):
            func = renpy.curry(trans)(xdist=xdist, ydist=ydist, disp=self)
            return Transform(function=func)

        def overlay(self):
            ui.add(self)
            for xdist, ydist, layer in self.layer_info:
                renpy.layer_at_list([self.parallax(xdist, ydist)], layer)
            return

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEMOTION:
                self.xoffset, self.yoffset = ((float)(x) / (config.screen_width)) - 0.5, ((float)(y) / (config.screen_height)) - 0.5
            return


    def trans(d, st, at, xdist=None, ydist=None, disp=None):
        d.xoffset, d.yoffset = int(round(xdist * disp.xoffset)), int(round(ydist * disp.yoffset))
        if xdist != 0 or ydist != 0:
            xzoom = (config.screen_width + abs(xdist + xdist)) / float(config.screen_width)
            yzoom = (config.screen_height + abs(ydist + ydist)) / float(config.screen_height)
            if yzoom > xzoom:
                d.zoom = yzoom
            else:
                d.zoom = xzoom
            d.anchor = (.5, 1.0)
            d.align = (.5, 1.0)
        return 0

    # список для хранения изображений с указанием слоев
    nd_parallax_images = []

    # показать несколько изображений, каждое на своем слое параллакса
    # можно с эффектом transform или даже с несколькими
    # количество изображений не должно превышать количество слоев
    # иначе лишние будут выведены на слой master2 поверх остальных
    # $ showp("city1", ("city2", truecenter), ("city3", [truecenter, woo]))
    def nd_showp(*args):
        global nd_parallax_images
        layers = nd_mouse_parallax.layers()
        for i in args:
            at = []
            image = i
            if isinstance(image, tuple):
                image, at = image
                if not isinstance(at, list):
                    at = [at]
            l = "master2"
            if len(layers) > 0:
                l = layers.pop()
            renpy.show(image, at_list=at, layer=l)
            i = (image, l)
            if not i in nd_parallax_images:
                nd_parallax_images.append(i)

    # убрать одно изображение с указанного (или с любого) слоя
    def nd_hidep(image, layer=None):
        global nd_parallax_images
        if not layer:
            layer = "master2"
            for ii, ll in nd_parallax_images:
                if ii == image:
                    layer = ll
        i = (image, layer)
        renpy.hide(image, layer=layer)
        if i in nd_parallax_images:
            nd_parallax_images.remove(i)

    # очистить все слои параллакса
    # и при необходимости добавить новые изображения
    def nd_scenep(*args):
        global nd_parallax_images
        for i in nd_parallax_images:
            image, layer = i
            renpy.hide(image, layer=layer)
        nd_parallax_images = []
        if args:
            showp(*args)

    nd_mouse_parallax = nd_MouseParallax((-60, -15, "l0"), (-40, -10, "l1"), (-20, -5, "l2"))

init:
## - - - OTHER ▼
## Advices random generation container
    $ nd_gen_advice = ""
    $ nd_advice_list = ["МЫ РАДЫ ТЕБЯ ВИДЕТЬ!",
                    "Посмотрите пункт \"профиль\" в главном меню.\nТам находится ваша статистика за весь мод!",
                    "Если вы не получили ни одной ачивки за\nпрохождение, значит вы шли на рут Ульяны.", 
                    "Перед прохождением налейте себе горячего чаю!",
                    "Никаких советов, просто пожелаю\nприятного времяпрепровождения.",
                    "Влюбились в наш мод? А мы влюбились в Ульяну!\nВас ждут красивые арты на её руте :)",
                    "Будь добрым пионером.",
                    "Нажимая на молнию в пятом дне,\nс небольшим шансом вы можете открыть секрет!"
                    ]

    $ nd_genegrated_advice = renpy.random.choice(nd_advice_list) 
    $ nd_gen_advice = nd_genegrated_advice
## Timeless relic
    if res == "day":
        $ nss_sa = "Добрый день, " + "читатель!" #str(userpcname)
    if res == "evening":
        $ nss_sa = "Добрый вечер, " + "читатель!" #str(userpcname)
    if res == "night":
        $ nss_sa = "Добрый вечер, " + "читатель!" #str(userpcname)

## - - - "PLICK PLUCK" ▼

## MAIN MENU CONTAINER (PC) // graunddm()
screen graunddm():
    tag menu
    modal True

    button xpos 0.04 ypos 0.26:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("Новая игра", style="helveticaneueroman_hover")
        hover_child Text("Новая игра", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("showing_nd_part_screen"),
            ]

    button xpos 0.04 ypos 0.32:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("Сохранения", style="helveticaneueroman_hover")
        hover_child Text("Сохранения", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            Jump('start_nd_load')
            ]


    button xpos 0.04 ypos 0.38:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("Профиль", style="helveticaneueroman_hover")
        hover_child Text("Профиль", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("open_ach_scr_dm")
            ]

    button xpos 0.04 ypos 0.44:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("Настройки", style="helveticaneueroman_hover")
        hover_child Text("Настройки", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("start_nd_prefs")
            #Jump("settings_nd_mod_on")
            ]

    button xpos 0.04 ypos 0.50:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("О модификации", style="helveticaneueroman_hover")
        hover_child Text("О модификации", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            Jump("nd_start_aboutmodif")
            ]

    button xpos 0.04 ypos 0.56:
        xmaximum 303 ymaximum 100  background "transparent_notdream"
        idle_child Text("Нашли ошибку?", style="helveticaneueroman_hover")
        hover_child Text("Нашли ошибку?", style="helveticaneueroman_idle")
        hovered [Play('nd_ui_sounds', nd_ui_hover)]
        action [
            Play('nd_ui_sounds', ui_click),
            OpenURL("https://vk.com/topic-178104256_40477812")
            ]

    if not renpy.mobile:
        button xpos 0.04 ypos 0.62:
            xmaximum 303 ymaximum 100  background "transparent_notdream"
            idle_child Text("Выход в меню", style="helveticaneueroman_hover")
            hover_child Text("Выход в меню", style="helveticaneueroman_idle")
            hovered [Play('nd_ui_sounds', nd_ui_hover)]
            action [
                Play('nd_ui_sounds', ui_click),
                Jump('notdream_exit_tomenu')
                ]
    else:
        button xpos 0.04 ypos 0.62:
            xmaximum 303 ymaximum 100  background "transparent_notdream"
            idle_child Text("Выход", style="helveticaneueroman_hover")
            hover_child Text("Выход", style="helveticaneueroman_idle")
            hovered [Play('nd_ui_sounds', nd_ui_hover)]
            action [
                Play('nd_ui_sounds', ui_click),
                Quit(confirm=False)
                ]
    imagebutton xpos 0.03 ypos 0.72:
        idle ("group_dreammod")
        hover ("group_dreammod_hovered")
        action [
            Play('nd_ui_sounds', ui_click),
            OpenURL("https://vk.com/bmodmakersitw")
            ]

    vbox align(0.87, 0.1):
        xsize 400
        ysize 100
        hbox align(0.8, 0.1):
            text nss_sa:
                xalign 0.9
                style 'helveticaneueroman_idle'
        hbox align(0.90, 0.1):
            text "РАДЫ ТЕБЯ ВИДЕТЬ":
                size 23
                xalign 0.95
                style 'helveticaneueroman_idle'

    #button xpos 0.70 ypos 0.1:
    #    xmaximum 700 ymaximum 100  background "transparent_notdream"
    #    idle_child Text(nss_sa + "{vspace=10}" + "{space=70}{size=22}ДАННЫЕ ЗАГРУЖЕНЫ{/size}", style="helveticaneueroman_idle")
    #   hover_child Text(nss_sa + "{vspace=10}" + "{space=70}{size=22}ДАННЫЕ ЗАГРУЖЕНЫ{/size}", style="helveticaneueroman_idle")
    #    action [NullAction()]

## DEVELOPER MODE FUNCS CONTAINER
label notdream_exit_tomenu:

    stop music fadeout 3
    stop ambience fadeout 3
    hide screen graunddm
    show black
    with dissolve2

    $ renpy.pause (1, hard=True)

    $ config.has_autosave = False
    $ config.autosave_frequency = None
    $ config.autosave_on_choice = False

    $ iknowmyway_nd_us              =           None                            # Когда завершишь 6 день, удали.
    $ qtr_miss                      =           0                               # Поражения игрока в игре "Эрудит"
    $ usrr                          =           0                               # Очки отношений с Ульяной
    $ dvrr                          =           0                               # Очки отношений с Алисой
    $ nir                           =           0                               # Очки к концовке "Нирвана"
    $ usrf                          =           0                               # Очки отношений с Ульяной после 3 дня
    $ autosave_autoload_unlocker    =           1                               # Разблокировка автосохранения / Для отключения необходимо значение единицы изменить на ноль
    $ d1_dv_guitar_learning         =           False                           # Игрок получает эту переменную в True после того, как откажется с Ульяной идти играть в футбол
    $ dv_leave_d1                   =           False                           # Уйти от Алисы в первом дне после кражи булок (побежать за Ульяной)
    $ dv_flag_morning_d1            =           False                           # Остаться с Алисой (не бежать за Ульяной)
    $ us_candy_steal                =           False                           # Отправиться с Ульяной в столовую за конфетами
    $ d2_dv_morning_din_sorry       =           False                           # Извиниться перед Алисой в столовой во 2-м дне
    $ d2_dv_night_pristan           =           False                           # Ивент с пристанью и Алисой во 2-м дне
    $ d2_nirvana_night_pristan      =           False                           # Ивент с пристанью с Алисой и Ульяной во 2-м дне
    $ paper_m                       =           False                           # Мятость бумажки после выбора в первои сне
    $ fake_z_54                     =           None                            # Фейк роспись 2-й день
    $ persistent.ss_first_time      =           False                           # Первая встреча игрока с Самантой
    $ userpcname                    =           os.environ.get('username')      # Взять имя пользователя
    $ d2_night_dv                   =           False                           # ПРИСТАНЬ (2 день) | С алисой
    $ d2_night_csx                  =           False                           # ПРИСТАНЬ (2 день) | Ульяна
    $ d2_night_nir                  =           False                           # ПРИСТАНЬ (2 день) | Нирвана
    $ d2_dv_night_pristan_q         =           False                           # Приглашение Алисы на встречу у пристани
    $ us_scenario_road              =           False                           # Развитие с персонажем \Ульяна\ после 3-го дня
    $ dv_scenario_road              =           False                           # Развитие с персонажем \Алиса\ после 3-го дня
    $ nir_scenario_road             =           False                           # Развитие \Нирвана\ после 3-го дня
    $ sich_scenario_road            =           False                           # Одинокий волк после 3-го дня. Плохая концовка
    $ necessary_clubs               =           0                               # Карта во втором дне
    $ necessary_musclub             =           0                               # Карта во втором дне
    $ necessary_aidpost             =           0                               # Карта во втором дне
    $ necessary_library             =           0                               # Карта во втором дне
    $ necessary_map                 =           0                               # Карта во втором дне
    $ necessary_search_us_scene     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_sport     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_map       =           0                               # Карта во время поисков Ульяны
    $ music_kr_dv                   =           False                           # Запись на кружок МУЗЫкИ
    $ sport_kr_us                   =           False                           # Запись на кружок ФУТБОЛА
    $ dvrr_shark_p                  =           0                               # Плакат акулы в клубе гитаристов
    $ dvrr_pirate_p                 =           0                               # Плакат пирата в клубе гитаристов
    $ gg_sorry_us                   =           False                           # Концовка Ульяны "Прощай"
    $ gg_goodbye_us                 =           False                           # Концовка Ульяны "Прости"
    $ miss_us_r_1                   =           False                           # Обида Ульяны на что-либо
    $ old_camp_sh_cheese            =           False                           # Сыр для Шурика в старом лагере
    $ open_nirvana_road_nd          =           None                            # Состояние рута нирваны, выдаваемое во время сна в автобусе в прологе.
    $ persistent.dv_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True
    $ persistent.us_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True

    $ volume (1, "ambience")
    $ volume (1, "music")
    $ volume (1, "sound")

    $ nd_screens_diact()
    $ MainMenu(confirm=False)()

    return

label nd_turn_on_autosave:
    $ persistent.autosave_unlocker = True
    $ config.has_autosave = True
    $ config.autosave_frequency = 300
    $ config.autosave_on_choice = False

    show screen nd_preferences

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)
label nd_turn_off_autosave:
    $ persistent.autosave_unlocker = False
    $ config.has_autosave = False
    $ config.autosave_frequency = None
    $ config.autosave_on_choice = False

    show screen nd_preferences

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)
label nd_deactivate_forgui_sl:
    hide screen nd_Load
    hide screen nd_Save
    with dissolve
label nd_activate_screen_mainmenu:
    hide screen nd_Load
    scene black
    with dissolve
    $ renpy.pause(0.5)

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

label nd_reset_mod_params_end:
    $ iknowmyway_nd_us              =           None                            # Когда завершишь 6 день, удали.
    $ qtr_miss                      =           0                               # Поражения игрока в игре "Эрудит"
    $ usrr                          =           0                               # Очки отношений с Ульяной
    $ dvrr                          =           0                               # Очки отношений с Алисой
    $ nir                           =           0                               # Очки к концовке "Нирвана"
    $ usrf                          =           0                               # Очки отношений с Ульяной после 3 дня
    $ autosave_autoload_unlocker    =           1                               # Разблокировка автосохранения / Для отключения необходимо значение единицы изменить на ноль
    $ d1_dv_guitar_learning         =           False                           # Игрок получает эту переменную в True после того, как откажется с Ульяной идти играть в футбол
    $ dv_leave_d1                   =           False                           # Уйти от Алисы в первом дне после кражи булок (побежать за Ульяной)
    $ dv_flag_morning_d1            =           False                           # Остаться с Алисой (не бежать за Ульяной)
    $ us_candy_steal                =           False                           # Отправиться с Ульяной в столовую за конфетами
    $ d2_dv_morning_din_sorry       =           False                           # Извиниться перед Алисой в столовой во 2-м дне
    $ d2_dv_night_pristan           =           False                           # Ивент с пристанью и Алисой во 2-м дне
    $ d2_nirvana_night_pristan      =           False                           # Ивент с пристанью с Алисой и Ульяной во 2-м дне
    $ paper_m                       =           False                           # Мятость бумажки после выбора в первои сне
    $ fake_z_54                     =           None                            # Фейк роспись 2-й день
    $ persistent.ss_first_time      =           False                           # Первая встреча игрока с Самантой
    $ userpcname                    =           os.environ.get('username')      # Взять имя пользователя
    $ d2_night_dv                   =           False                           # ПРИСТАНЬ (2 день) | С алисой
    $ d2_night_csx                  =           False                           # ПРИСТАНЬ (2 день) | Ульяна
    $ d2_night_nir                  =           False                           # ПРИСТАНЬ (2 день) | Нирвана
    $ d2_dv_night_pristan_q         =           False                           # Приглашение Алисы на встречу у пристани
    $ us_scenario_road              =           False                           # Развитие с персонажем \Ульяна\ после 3-го дня
    $ dv_scenario_road              =           False                           # Развитие с персонажем \Алиса\ после 3-го дня
    $ nir_scenario_road             =           False                           # Развитие \Нирвана\ после 3-го дня
    $ sich_scenario_road            =           False                           # Одинокий волк после 3-го дня. Плохая концовка
    $ necessary_clubs               =           0                               # Карта во втором дне
    $ necessary_musclub             =           0                               # Карта во втором дне
    $ necessary_aidpost             =           0                               # Карта во втором дне
    $ necessary_library             =           0                               # Карта во втором дне
    $ necessary_map                 =           0                               # Карта во втором дне
    $ necessary_search_us_scene     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_sport     =           0                               # Карта во время поисков Ульяны
    $ necessary_search_us_map       =           0                               # Карта во время поисков Ульяны
    $ music_kr_dv                   =           False                           # Запись на кружок МУЗЫкИ
    $ sport_kr_us                   =           False                           # Запись на кружок ФУТБОЛА
    $ dvrr_shark_p                  =           0                               # Плакат акулы в клубе гитаристов
    $ dvrr_pirate_p                 =           0                               # Плакат пирата в клубе гитаристов
    $ gg_sorry_us                   =           False                           # Концовка Ульяны "Прощай"
    $ gg_goodbye_us                 =           False                           # Концовка Ульяны "Прости"
    $ miss_us_r_1                   =           False                           # Обида Ульяны на что-либо
    $ old_camp_sh_cheese            =           False                           # Сыр для Шурика в старом лагере
    $ open_nirvana_road_nd          =           None                            # Состояние рута нирваны, выдаваемое во время сна в автобусе в прологе.
    $ persistent.dv_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True
    $ persistent.us_rf_unlock_nir   =           False                           # Переменная, если значение которых = True, Nirvana при "Я останусь здесь" = True
    $ persistent.fall_stair_bunker  =           0

    $ volume (1, "ambience")
    $ volume (1, "music")
    $ volume (1, "sound")

    jump notdream

label start_nd_prefs:
    hide screen graunddm
    scene black
    with dissolve
    $ renpy.pause(0.5)
    show screen nd_preferences
    with dissolve

    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)
label end_nd_prefs:

    hide screen nd_preferences
    scene black
    with dissolve
    $ renpy.pause(0.5)

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
label start_nd_load:
    hide screen graunddm
    scene black
    with dissolve
    $ renpy.pause(0.5)
    show screen nd_Load
    with dissolve
    $ renpy.pause(99999999999999999999999999999999999999999999999999999999999999999999, hard=True)
