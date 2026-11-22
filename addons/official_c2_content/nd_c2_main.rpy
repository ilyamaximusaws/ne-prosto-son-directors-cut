init python:

    nd_addon_id = "13556081"
    nd_addons.append(nd_addon_id)
    
    if nd_addon_id == "13556081":
        current_addon_name = "official_c2_content"

    nd_current_addon_path = nd_addons_path + current_addon_name
    
init:
    ## - Vars - ##
    $ nd_something_var = 0

    ## - Images - ##
    
    # 1. Parts - - -
    image present_bg            = nd_current_addon_path + "/img/parts/present_bg.png"
    image present_bg_v2         = nd_current_addon_path + "/img/parts/present_bg_v2.png"
    image present_text          = nd_current_addon_path + "/img/parts/present_text.png"
    image present_fixcs         = nd_current_addon_path + "/img/parts/present_fixcs.png"
    
    # p1
    image nd_g_2_part_1_bg      = nd_current_addon_path + "/img/parts/nd_g_2_part_1_bg.png"
    image nd_g_2_part_1_text    = nd_current_addon_path + "/img/parts/nd_g_2_part_1_text.png"

    # p2
    image nd_g_2_part_2_bg      = nd_current_addon_path + "/img/parts/nd_g_2_part_2_bg.png"
    image nd_g_2_part_2_text    = nd_current_addon_path + "/img/parts/nd_g_2_part_2_text.png"

    # p3
    image nd_g_2_part_3_text    = nd_current_addon_path + "/img/parts/nd_g_2_part_3_text.png"

    # p4
    image nd_g_2_part_4_text    = nd_current_addon_path + "/img/parts/nd_g_2_part_4_text.png"

    # p5
    image nd_g_2_part_5      = nd_current_addon_path + "/img/parts/nd_g_2_part_5.png"

    # p6
    image nd_g_2_part_6_text      = nd_current_addon_path + "/img/parts/nd_g_2_part_6_text.png"

    # 2. Scenes
    image bg nd_c1_us_kitchen       = nd_current_addon_path + "/img/bg/nd_c1_us_kitchen.png"
    image bg nd_c1_us_kitchen_glow  = nd_current_addon_path + "/img/bg/nd_c1_us_kitchen_glow.png"
    image bg nd_c1_us_bedroom       = nd_current_addon_path + "/img/bg/nd_c1_us_bedroom.jpg"
    image bg nd_semen_room_day      = nd_current_addon_path + "/img/bg/nd_semen_room_day.png"
    image bg nd_me_room_day         = nd_current_addon_path + "/img/bg/nd_me_room_day.png"
    image bg nd_city_pp_1           = nd_current_addon_path + "/img/bg/nd_city_pp_1.png"
    image bg nd_int_elevator        = nd_current_addon_path + "/img/bg/nd_int_elevator.jpg"
    image bg int_car_inside         = nd_current_addon_path + "/img/bg/int_car_inside.png"
    image bg nd_rg2                 = nd_current_addon_path + "/img/bg/nd_rg2.png"
    image bg nd_to_entrance         = nd_current_addon_path + "/img/bg/nd_to_entrance.jpg"
    image bg nd_podtzd              = nd_current_addon_path + "/img/bg/nd_podtzd.png"
    image bg nd_city_up_2           = nd_current_addon_path + "/img/bg/nd_city_up_2.jpg"
    image bg nd_podtzd_stairs_1     = nd_current_addon_path + "/img/bg/nd_podtzd_stairs_1.png"
    image bg nd_podtzd_stairs_2     = nd_current_addon_path + "/img/bg/nd_podtzd_stairs_2.png"
    image bg nd_kvart_pr_1          = nd_current_addon_path + "/img/bg/nd_kvart_pr_1.png"
    image bg nd_kvart_pr_night      = nd_current_addon_path + "/img/bg/nd_kvart_pr_night.png"
    image bg nd_c3_gg_kitchen       = nd_current_addon_path + "/img/bg/nd_c3_gg_kitchen.png"
    image bg nd_gg_room_day         = nd_current_addon_path + "/img/bg/nd_gg_room_day.png"
    image bg nd_webstorm_ss         = nd_current_addon_path + "/img/bg/nd_webstorm_ss.png"
    image bg snowy_city_background  = nd_current_addon_path + "/img/bg/snowy_city_background.jpg"
    image bg nd_int_bashops         = nd_current_addon_path + "/img/bg/nd_int_bashops.png"
    # 3. Arts
    image nd_ridin_art          = nd_current_addon_path + "/img/arts/nd_ridin_art.png"
    image nd_c2_window_art      = nd_current_addon_path + "/img/arts/nd_c2_window_art.png"
    image nd_vodila_ridin       = nd_current_addon_path + "/img/arts/nd_vodila_ridin.png"
    image nd_path_tocity        = nd_current_addon_path + "/img/arts/nd_path_tocity.jpg"
    image semen_room_window_day = nd_current_addon_path + "/img/arts/semen_room_window_day.jpg"
    image nd_sky_for_fix        = nd_current_addon_path + "/img/arts/nd_sky_for_fix.png"
    image nd_sov_kv             = nd_current_addon_path + "/img/arts/nd_sov_kv.png"
    ## - Music - ##
    $ nd_archaichno             = nd_current_addon_path + "/audio/music/nd_archaichno.mp3"
    $ nd_c2_part1_start         = nd_current_addon_path + "/audio/music/nd_c2_part1_start.mp3"
    $ sy_was_a_second_idea      = nd_current_addon_path + "/audio/music/sy_was_a_second_idea.mp3"
    $ nd_have_something_to_say  = nd_current_addon_path + "/audio/music/nd_have_something_to_say.mp3"

## - - - CHARACTERS ▼
## Custom mod characters container 
    $ nd_vie    = Character(u'Водитель', color="1974d2", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ nd_vi     = Character(u'Виктор', color="358fe8", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ nd_pe1    = Character(u'Бандит первый', color="358fe8", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000") # E2C778
    $ nd_pe2    = Character(u'Бандит второй', color="fb9700", what_color="F2F2F2", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000")

## - - - TITLES ▼
    $ nd_credits_fix = """{font=mods/notdream/fonts/nd_helvuelight.ttf}{size=30}Фикционализм\nby\nTandem Developers\n
    {image=mods/notdream/images/ends/fict_logo.png}\n
    Мы благодарим вас за время
    которое вы уделили дополнению \"Фикционализм\"\n
    Не забудьте оставить отзыв на странице мода в Steam
    или в нашей группе ВКонтакте!\n
    {size=35}АВТОРСТВО СЦЕНАРИЯ{/size=35}
    Илья Вольнов - любит Ульяну
    Soviet Tyan - тоже любит Ульяну\n
    {size=35}ОТВЕТСТВЕННЫЕ ЗА КОД{/size=35}
    Илья Вольнов
    Otorhin
    Skeara
    Soviet Tyan\n
    {size=35}ДИЗАЙН{/size=35}
    Илья Вольнов
    rhr a.k.a удачи без редактора\n
    {size=35}АВТОРЫ ИДЕИ{/size=35}
    Илья Вольнов
    и его нескучная жизнь\n
    {size=35}БЕТА-ТЕСТЕРЫ{/size=35}
    Soviet Tyan
    nc161tcs
    Icedragon4ik\n
    {size=35}АВТОРЫ АРТОВ{/size=35}
    Настя Танчук. Ты очень хорошо рисуешь...\n
    АВТОРСТВО МУЗЫКИ И ЗВУКОВ
    Принадлежит некоторым исполнителям,
    которые застряли в моём сердечке <3\n\n\n
    БЛАГОДАРНОСТИ ЭТИМ ЛЮДЯМ:
    Евгений Мяус, Авдеев Артём, Иван Молченко
    Сергей Петров, Алексей Носенко, Александр Алиновский,
    Александр Миронов, Диана Ниженко, Владя,
    Андрей Плевецкий, Hauntum, Мессер
    Денис Шибинский, Артём Шип, Лев Бочаров, и прочие...
    Спасибо что вы со мной в такое трудное для меня время!\n\n
    ОТДЕЛЬНЫЕ БЛАГОДАРНОСТИ:
    Подписчикам группы \"Tandem Studio | Бесконечное лето\"\n
    Создателю модификации \"Мы - это главное\"
    Я выплакал свои глазные яблоки благодаря тебе.\n
    Создателю модификации \"Новая жизнь\" - Soviet Tyan.
    Ты самый лучший человек, которого я знаю.\n
    Маше Бут - я тебя в радости не вспомнил,
    а в горести не сыскал. Мне нечего сказать.
    Я запомнил тебя такой...\n
    Константин Мирошниченко - если бы не ты,
    мой сценарий никогда бы нее увидел свет.\n
    Виктория Жучко - ты заставила меня поверить в любовь.
    Я жалею, что сейчас не рядом с тобой...
    Я за тебя очень волнуюсь...\n
    Александр и Илья - я жалею о прошлом, которого, увы,
    не вернуть назад.\n
    Иван Бочарников - не знаю где ты сейчас, но надеюсь,
    что с тобой всё хорошо.\n
    Виктор Столопов - когда-нибудь я хотел бы с тобой
    покурить кальян.\n
    Елизавета Кузнецова - ты именно та сестричка,
    которая всегда меня поймёт.\n
    Денис Баклин - у тебя потрясающие саундтреки.
    Жаль, что их нет в этой главе...\n
    Роман Тырыкин - я верю, что ты обретёшь своё счастье,
    где бы ты ни находился...\n
    Почему из моих глаз текут слёзы?..
    \n
    МАТЕРИАЛЫ, ИСПОЛЬЗОВАННЫЕ В МОДЕ,
    ПРИНАДЛЕЖАТ ИСКЛЮЧИТЕЛЬНО
    ИХ ПЕРВИЧНЫМ ПРАВООБЛАДАТЕЛЯМ\n\n
    МУЗЫКА В ТИТРАХ:
    есть что сказать - Вези меня\n\n\n
    Начало было положено 3 года назад, и,
    возможно, что мы с тобой больше не увидимся.
    Мне было приятно писать эту историю для тебя, читатель
    но у всего должен быть конец. И мой конец начнется именно здесь.
    Я хочу оставить что-то после себя... Я не умру, пока я тут - в этом месте.
    Не убивай меня. Послушай. Я написал кое что для своей любви.
    Этот стишок... Буквально крик души.
    Он посвящен девочке, по которой я сейчас очень скучаю
    Потрать пожалуйста немного времени и оцени его...

    \n\n\n\n\n\n
    Илья Вольнов - Запомню.
    \n
    Ты же знаешь, я пишу всегда
    Про твои черты и серость бытия.
    И из разу в раз в весенний день
    Пишу в серой комнате сердца лень.

    Да и пусть самоучка, пусть сам не свой
    Вместо траты совести, весь седой
    Я пишу простуженный о ночи той:
    О глазах твоих, о злости ноя,

    Что таю на тех, кто бессовестно тратит
    Свою тюрьму внутри и в тексте плачет,
    И представляет себе летний день,
    Бессовестно возлагая ношу на друзей.

    Я не знал тех дней, когда не мечтал
    Взять за руки тебя и на танец встать,
    И кружиться в нём до глубокой ночи...
    Не случилось случая, что не день то тучи

    Мне не легче знать о твоих друзьях
    О фальшивых людях и о их тенях

    Мне проще слышать твоё дыхание
    Скорее сопение... Воспринимай как данное
    Строки данные, в них мой смысл радости,
    В них мой сон, в них мой памятник.

    Гниющих прошлых лет не вернуть назад -
    Не вернуть тебя, не вернуть себя.
    Я испорчен временем и своим стихом,
    А мой стих испорчен моим пером.

    Провожая взглядом твою печаль,
    Понимая что жаль, душой стонал
    Как снег на солнце облик мой
    Терял свои формы, шёл на дно.

    Не печалься ты, не вини себя,
    Я всегда любил, я любил тебя,
    Я признал свой гнев, я стал сильней
    Тебя не отнять из души моей.

    Оставшись раз наедине с собой,
    Я тебя запомнил, запомню тебя такой.
    \n
    Спасибо. Вот и настал тот конец, которого ты так долго ждал.
    Мне не больно... Я исчезаю...
    \n\n
    ВОССТАНОВЛЕННАЯ ВЕРСИЯ В STEAM 
    by
    Soviet Tyan
    rhr
    {/size=30}{/font}
    """


label nd_official_p2_start:
    
    $ renpy.pause (1, hard=True)

    $ nd_change_time('prolog')

    $ renpy.pause (1, hard=True)

    $ volume (1, "ambience")
    $ volume (1, "music")

    play music ndm_list['mt_awaken'] fadein 5

    scene present_bg with dissolve2
    $ renpy.pause (1, hard=True)
    show present_text with dissolve
    $ renpy.pause(3, hard=True)
    hide present_text with dissolve
    $ renpy.pause(0.5, hard=True)
    scene present_bg_v2 with dissolve3
    show present_fixcs with dissolve

    $ renpy.pause (5, hard=True)

    scene black with dissolve2

    $ renpy.pause(2, hard=True)
    
    jump nd_c2_partOne

label nd_fict_endscr_titles:
    $ nd_change_time('prolog')
    $ volume (1, "ambience")
    $ volume (1, "music")
    play ambience nda_list['ambience_int_train'] fadein 7
    $ renpy.pause(1, hard=True)
    scene notdream_endscreen at nd_bus_vpunch with dissolve3
    $ renpy.pause(2, hard=True)
    show notdream_endscreen_0 with dissolve2
    play music nd_have_something_to_say fadein 4
    $ renpy.pause(3, hard=True)
    show credits nd_credits_fix:
            xalign .5
            ypos 1.4
            linear 150.0 ypos -5.0
    $ renpy.pause(150, hard=True)
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    stop ambience fadeout 4
    show thx_for_1 with dissolve
    $ renpy.pause(50)
    show black with dissolve
    stop music fadeout 3
    $ renpy.pause(3)
    scene black with dissolve2
    $ renpy.pause(5, hard=True)
    $ persistent.nd_seed_titles += 1
    $ renpy.pause(1)
    jump nd_reset_mod_params_end
    

