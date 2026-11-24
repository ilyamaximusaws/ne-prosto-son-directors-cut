label nd_c2_epilogue:

    $ new_chapter(1, u"Фикционализм\nЭпилог - Одинаковы")
    $ nd_change_time('prolog')
    $ renpy.pause(4, hard=True)

    window show
    "Через закрытые веки я ощутил, как помещение наполнилось светом."
    "Я боялся открыть глаза какое-то время, не понимая почему."
    "Казалось я прошел около десяти километров без остановки.{w} Ноги болели.{w} В голове смешались мысли, причем я так и не смог понять их природу."
    "Пришло время открыть глаза."
    window hide

    $ renpy.pause(1, hard=True)
    play ambience nda_list['ambience_int_something'] fadein 4
    hide blink
    scene bg nd_ep_p2_mndoor
    show unblink
    $ renpy.pause(2, hard=True)

    window show
    "Советский подъезд."
    "Последнее место, где я хотел бы оказаться."
    "Такое поганое...{w} Господи, пожил бы еще чуть-чуть, купил бы себе нормальный дом в частном секторе."
    "Лишь бы от всего этого уйти."
    window hide

    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_mines
    $ renpy.pause(2, hard=True)

    window show
    "Внезапно дверь передо мной открывается, на пороге видна красная коса."
    "Что-то внутри меня замерло, потом попыталось запуститься. Ноги напряглись, я быстро встал. До того, как из-за двери показались голубые глазки."
    show us normal sport at center with dspr
    us "Илья, ты чего, прячешься?"
    nd_il "Пр-пр-прячусь?"
    show us smile sport at center with dspr
    us "Не валяй дурака, я тебя с утра уже жду."
    us "С того момента, когда ты написал, что уже приехал в город."
    nd_il "Ну... Ладно..."
    th "Правда я этого не помню."
    show us surp2 sport at center with dspr
    us "Заходи, глупый. Мне холодно..."
    "Я непроизвольно замялся после ею сказанного."
    us "И это... Я любя."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    stop ambience fadeout 3
    $ renpy.pause(2, hard=True)
    play sound sfx_close_door_1
    $ renpy.pause(1, hard=True)
    play ambience nda_list['ambience_int_apartaments_neutral'] fadein 4
    scene bg nd_c1_us_kitchen with dissolve3
    $ renpy.pause(1, hard=True)

    window show
    nd_il "У тебя тут мило."
    show us normal sport at left with dspr
    us "Спасибо, Илья."
    us "Вот, проходи, садись за стол, чайник уже почти вскипел..."
    hide us with dspr
    us "Ой."
    "Девочка случайно перевернула чашечку с маленькими кристалликами рукой."
    "Я докоснулся до горстки пальцем, а затем попробовал её на вкус. Солёное..."
    show us smile sport at left with dspr
    us "Стряхни тряпочкой, а-то поссоримся."
    window hide
    
    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(2, hard=True)
    play sound nds_list['nd_protirka']
    $ renpy.pause(1, hard=True)

    window show
    "Я не верил в приметы, но почему-то послушал её.{w} Выкинул соль в мусорное ведро под раковиной и сел за стол."
    window hide

    $ renpy.pause(2, hard=True)
    show us normal sport at center with dspr

    window show
    us "Как тебе город?"
    nd_il "Да вроде ничего.{w} Не знаю, почему ты хочешь уехать."
    us "Потому что мы с тобой ещё осенью договорились, что будем вместе жить..."
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Я посмотрел на полочку. Там была фотография красноволосой девочки в красивом платье."
    "Напряг глаза, чтобы разглядеть:{w} \"Ульяна\"."
    show us normal sport at center with dspr
    us "...Илья, тебе горячий или тёплый?"
    nd_il "Тёплый. Не люблю горячий."
    show us smile sport at center with dspr
    us "Я знаю, просто проверяла, что это правда ты."
    "Она улыбнулась, показывая, что это шутка."
    hide us with dspr
    "Я усмехнулся и упёр взгляд в стол."
    window hide

    play sound nds_list['nd_cup_tea_drop']
    $ renpy.pause(1, hard=True)

    window show
    "Через секунду в моём взгляде появилось блюдечко с кружечкой ароматного чая."
    window hide

    $ renpy.pause(2, hard=True)
    show us smile sport at center with dspr

    window show
    "Я перевёл взгляд на девочку."
    nd_il "Спасибо."
    us "Будешь за такие мелочи благодарить - твоё спасибо потеряет смысл."
    nd_il "Просто вежливость."
    show us normal sport at center with dspr
    us "Не надо фальши. Я видела тебя настоящего.{w=1} Влюбилась в тебя настоящего..."
    nd_il "Я всегда так себя вёл..."
    show us laugh sport at center with dspr
    us "Значит прости. Ха-ха!"
    hide us with dspr
    "Девочка усмехнулась, в одну секунду смущённо сделала глоток из кружечки."
    window hide

    $ renpy.pause(2, hard=True)
    
    show us shy sport at center with dspr

    window show
    us "Просто пытаюсь разрядить обстановку. Ты знаешь, что мы поссорились недавно."
    us "А сейчас я думаю, какой я была дурой."
    nd_il "Не говори так про себя."
    nd_il "Это бы значило, что у меня плохой вкус на девушек."
    show us shy2 sport at center with dspr
    us "Скажи прямо, ты меня все ещё любишь? После того что я сделала..."
    "Всем нам приходится в определенный этап своей жизни заключать сделку с дьяволом."
    "Простить Ульяну за то, что она вдохновила меня измениться, позже смешав дёготь с медом?"
    "В конце концов, это не зависило от неё.{w} Она не виновата в том, что доверилась человеку..."
    nd_il "Как можно тебя не любить?"
    show us normal sport at center with dspr
    us "{font=mods/notdream/fonts/notes.ttf};{/font} Твоя безумная малышка... {font=mods/notdream/fonts/notes.ttf};{/font}"
    nd_il "{font=mods/notdream/fonts/notes.ttf};{/font} ...не умеет любить... {font=mods/notdream/fonts/notes.ttf};{/font}"
    us "{font=mods/notdream/fonts/notes.ttf};{/font} ...а с той которая умеет... {font=mods/notdream/fonts/notes.ttf};{/font}"
    nd_il "{font=mods/notdream/fonts/notes.ttf};{/font} ...мне безумно скучно. {font=mods/notdream/fonts/notes.ttf};{/font}"
    show us shy2 sport at center with dspr
    us "Ха-хах. Мы пели её вместе..."
    window hide

    $ renpy.pause(2, hard=True)
    hide us with dspr

    window show
    "Она вытянула руку в мою сторону, открыв свою ладонь."
    "Я положил свою руку на её..."
    nd_il "Я тебя больше не отпущу."
    show us shy sport at center with dspr
    us "А я тебя больше не разлюблю..."
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)
    window show
    "Уля сильно сжала мою руку, засунула свои пальцы между моих, и через пару секунд отпустила."
    show us normal sport at center with dspr
    us "Вижу тебе понравилось, раз кружка уже пустая..."
    us "Ты будешь ещё чай?.."
    "Я усмехнулся."
    nd_il "Буду..."
    window hide

    $ renpy.pause(1, hard=True)
    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(2, hard=True)
    play music ndm_list['M41_BEATS_Elizabet'] fadein 4
    play ambience nda_list['ambience_int_something'] fadein 4
    scene bg nd_c1_us_bedroom with dissolve2 

    window show
    "Я засыпал под фильм, лежа под теплым пледом вместе с Ульяной, а та будто бы охраняла меня."
    "Девочка даже не думала глаза сомкнуть, хоть и знала, что мы с ней решили уйти на рассвете."
    "Я буду вести её на восток – туда, где восходит солнце.{w} Туда где мы только в мыслях."
    "Туда - где я вечно пьяный.{w} Туда - где любовь как выстрел."
    "Я обниму нирвану...{w} И научусь быть сильным..."
    "Я уверен, у нас получится."
    "Я готов ещё раз сводить её в город и подарить ей счастье, как в том сне…"
    "А может это был и не сон, может это реальность, а я сейчас сплю?"
    "Нет. Я - настоящий я. Это – мир, где мы вместе, как я и хотел."
    "А были ли Пророк-Василий, тот пионер и Семён настоящими?{w} Или они — только часть меня?"
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Я почувствовал, как рука Ульяны легла на мою голову и взъерошила мои волосы, выкидывая лишние мысли."
    "Улыбка на моем лице после этого появилась сама собой."
    nd_il "Ульяна, ты помнишь, как я подарил тебе колечко?"
    show us shy2 sport close at right with dspr
    us "Помню."
    nd_il "А как целовал тебя, пока мы аниме смотрели, помнишь?"
    show us shy sport close at right with dspr
    us "Помню. Ты его полностью проспал, и здесь тоже спишь."
    nd_il "Я думал в этом смысл. Смысл лежать у тебя в коленях и обнимать."
    hide us with dspr
    "Ульяна засмеялась."
    show us laugh sport close at right with dspr
    us "Илюша... Всё такой же."
    hide us with dspr
    "Она наклонилась и вновь поцеловала меня,{w} как раньше."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Я помнил каждый момент проведенный с ней, и был рад за это."
    "Во мне очень много воспоминаний. Я помню всё, от самого момента рождения искры внутри моей грудной клетки."
    "Пусть между нами была тысяча километров, она всегда будто бы была рядом."
    "Даже когда мне было невыносимо плохо..."
    "Когда ушла сестра, я закрывался ото всех.{w} Пока в моей жизни не появилась она."
    "Она была рядом во время моих панических атак,{w} когда я забывал принимать антидепрессанты."
    "А когда их курс был допит - она заменила мне их."
    "Она слала мне письма.{w} Успокаивала.{w} Давала надежду, что мы обязательно встретимся."
    "Единственная, кто не скрывает правду от меня..."
    "Я люблю её..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Ульяна хихикнула, будто прочитав мысли у меня в голове."
    "Странно было то, что этому я даже не удивился."
    show blink
    "Лишь глаза прикрыл, и представил, как мы с девочкой вновь идем за руку по летнему лагерю «Совёнок», наполненному яркими моментами, мечтами и, самое главное - любовью..."
    "Тот день, когда я её приревновал, а она подвернула ногу."
    "День, когда мы за чаепитием признались её подруге в содеяном в первый же день в лагере."
    "А потом она меня первый раз поцеловала в щёчку..."
    us "Мне нравится, как ты гладишь меня..."
    "Тихо произнесла девочка и положила на моё плечо свою ладонь.{w} На безымянном пальчике её было моё колечко..."
    nd_il "Я всегда мечтал сделать тебя счастливой..."
    us "Илья..."
    us "Я уже счастлива, только потому что ты меня любишь..."
    "На глазах выступили слёзы.{w} Слёзы счастья."
    nd_il "Я...{w} Тебя люблю."
    us "А я тебя, Илюш."
    window hide

    stop ambience fadeout 5
    scene black with dissolve3
    $ renpy.pause(2, hard=True)

    window show
    "У каждой истории есть свое начало и конец. У каждой истории есть канва, синопсис, прологи и эпилоги."
    "У каждой, кроме моей. Ведь моя история - это не заумные термины из литературы или заковыристые речевые обороты."
    "...Это синопсы внутри моей головы, которые пока ещё не знают, какой будет их конец."
    "Я многое потерял за время своего путешествия, многое приобрел, многое узнал и встретил многих людей."
    "Они приходили и уходили, оставляя отпечаток на моей душе."
    "Кто будет следующим?"
    "У кого хватит силы войти в мой город и сохранить его врождённую девственность?"
    "Ещё пару лет назад я бы не смог ответить на эти вопросы, но сейчас сделал бы это с полной уверенностью."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "И я боюсь привыкнуть к ней. Боюсь перестать чувствовать, перестать говорить и даже остаться."
    "Расстояние целый год для нас было мерой предосторожности, мы были далеко, но одновременно так близко."
    "Сотни моих писем ей о том, что я её люблю..."
    "У меня не будет иного выхода.{w} Сшейте наши сердца, потом скальпелем разрежьте их на куски."
    window hide

    $ renpy.pause(1, hard=True)
    if persistent.nd_fix_end == True:
        window show
        "Я останусь с ней...{w} Навсегда."
        window hide
    
    elif persistent.nd_fix_end == False:
        window show
        "Я заберу её с собой.{w} Вместе нам будет лучше..."
        window hide

    else:
        menu:
            "Остаться с Ульяной":
                $ persistent.nd_fix_end = True
            "Взять Ульяну с собой":
                $ persistent.nd_fix_end = False

    stop music fadeout 7
    $ renpy.pause(4, hard=True)

label nd_fict_end:
    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(2, hard=True)
    show nd_cit_d5 with dissolve2
    $ renpy.pause(6, hard=True)
    hide nd_cit_d5 with dissolve2
    $ renpy.pause(1, hard=True)

    jump nd_fict_endscr_titles