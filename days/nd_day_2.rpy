#---------------------------------------------------------------------------
# Не спойлери себе игру! 
#---------------------------------------------------------------------------

label checking_your_skill_and_money:
    
    play ambience ambience_forest_day fadein 4
    show day_2_nd with dissolve2
    $ renpy.pause(1, hard = True)
    show day_2_blur_nd with nd_effect_5_reverse
    $ renpy.pause(1, hard = True)
    show day_2_text_nd with dissolve
    $ renpy.pause(3, hard = True)

    stop ambience fadeout 4
    hide day_2_nd
    hide day_2_text_nd
    hide day_2_blur_nd
    with dissolve2

    #$ backdrop = "days"
    $ new_chapter(2, u"Это не просто сон, верно?\nДень второй")
    $ renpy.pause(3, hard = True)

    $ nd_change_time('day')
    
    
    #---Идет подсчет очков...
    
    if dv_flag_morning_d1 == True:
        $ dvrr += 1
        jump notdreamdaytwo_alice_nir
    else:
        jump notdreamdaytwo_us_nir
    
label notdreamdaytwo_alice_nir:
    
    
    $ renpy.pause(3)
    
    window show
    "В глазах слегка посветлело."    
    "Не знаю почему,{w} но я рефлекторно принял положение \"сидя\",{w} и принялся с закрытыми глазами нащупывать свой телефон на тумбе."
    window hide

    $ renpy.pause(2)

    play ambience ambience_int_cabin_day fadein 4
    hide black
    scene bg int_house_of_gg_day
    with flash
    play music music_list["trapped_in_dreams"] fadein 4

    window show
    "Поняв, что тумбы рядом нет, я разомкнул веки и увидел какой-то пустой домик."
    th "Где я и который сейчас, простите, час?.."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я принялся оглядывать помещение.{w} На стене висели часы, показывающие одиннадцать часов."
    th "Я всё ещё в лагере? Значит это не сон.{w} Хотя я точно был уверен, что проснусь в своем реальном мире и у себя в квартире. Да хотя-бы вне её."
    th "Странно..."
    window hide

    $ renpy.pause(1)
    
    window show
    "Мои глаза ещё раз оглядели комнату, и в поле зрения попал какой-то шкаф, который почему-то я не заметил в первый день."
    th "А это что такое?"
    "Я нехотя поднял себя с кровати и поплёлся к этому шкафу."
    window hide

    $ renpy.pause(2)    
    
    window show
    "С виду это был самый обычный шкаф."
    window hide

    stop music fadeout 4
    play sound sfx_open_cupboard

    window show
    "Я открыл дверцу шкафчика, и заметил на его внутренней стороне зеркало, в котором..."
    window hide

    play sound sfx_scary_sting
    show cg d2_mirror with hpunch

    window show
    nd_il "Ёпт..."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Пацан, ты кто?"
    "Очевидно, это был я.{w} Но на вид мне было не восемнадцать, а пятнадцать или шестнадцать лет."
    th "А-фи-геть.{w} Значит я действительно в прошлом?{w} Но я ведь тогда ещё даже не родился…"
    window hide

    $ renpy.pause(1)
    play music music_list["trapped_in_dreams"] fadein 4
    
    window show
    th "Я в теле другого человека?"
    th "Да нет вроде, так я и выглядел раньше. Лет пять назад если не больше."
    th "Ещё и расчесаться бы мне ещё не помешало."
    window hide
    $ renpy.pause(1)
    window show
    "Взглянув на полку я увидел розовую расческу и две резинки для волос.{w} По-видимому, здесь раньше жили девушки и забыли забрать с собой своих вещи, когда уезжали."
    th "Ладно, раз судьба позволяет, пора привести себя в порядок."
    window hide
    
    show black with dissolve
    
    window show
    "Я начал расчёсывать свои волосы, зализывая торчащие,{w} и после нескольких повторений этой процедуры всё встало на свои места, а отражение в зеркале стало выглядеть куда привлекательней."
    window hide

    show cg semyon_mirror
    hide black
    with dissolve
    
    window show
    th "Во-от. Теперь хоть на человека похож.{w} Для полной человечности только умыться не хватает."
    "Подумал я, и открыв маленький шкафчик, взял оттуда умывальные принадлежности и отправился на выход из своего домика."
    window hide

    stop music fadeout 4
    stop ambience fadeout 4
    scene black with dissolve
    $ renpy.pause(2)

    play sound sfx_open_door_1
    play ambience ambience_camp_center_day fadein 2 
    scene bg ext_house_of_sl_day with dissolve2 
    play music music_list["went_fishing_caught_a_girl"] fadein 4
    play sound sfx_close_door_1

    window show
    "На улице было довольно тепло. \nПо моему, даже чересчур."
    "Может так казалось только мне, потому что я ещё не привык к летнему времени года.{w} Хотя, единственный случай, когда я вышел на улицу, это был мой поход к психотерапевту."
    "Вот к чему приводит нахождение на улице..."
    window hide

    $ renpy.pause(1)

    window show
    "Я достал из кармана помятую карту и, найдя на ней умывальники, пошёл на место..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    scene bg ext_houses_day with dissolve2
    $ renpy.pause(1)
    
    window show
    "По дороге я разглядывал умывальные принадлежности и совсем не заметил, как вдалеке замаячила вожатая."
    window hide

    show mt normal pioneer far at center with dspr
    $ renpy.pause(1)
    show mt normal pioneer at center with dspr
    
    window show
    "Она подошла ко мне…"
    window hide

    show mt angry pioneer at center with dspr
    stop music fadeout 2
    
    window show
    mt "Почему пионер спит допоздна?"
    "И сразу начала наезжать."
    vg "Вот и пришел тебе конец."
    nd_il "Просто к расписанию не привык, сами понимаете."
    window hide

    $ renpy.pause(1)
    show mt normal pioneer at center with dspr
    
    window show
    "Я соврал, но это подействовало."
    mt "Ладно, на первый раз сделаю тебе поблажку.{w} Я не за этим тебя искала…"
    nd_il "А зачем?"
    th "Действительно.{w} Зачем вожатая может искать пионера, не явившегося на линейку?"
    window hide

    $ renpy.pause(1)
    
    window show
    "Ольга Дмитриевна протянула мне бумажку, на которой были места для росписей."
    nd_il "Что это?"
    window hide

    show mt smile pioneer at center with dspr
    
    window show
    mt "Бегунок."
    nd_il "То есть мне нужно собрать подписи и записаться на какой-нибудь кружок?"
    mt "Именно."
    nd_il "Тогда я сначала до умывальников дойду, там сначала подпись спрошу."
    window hide

    hide mt with dspr
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    
    window show
    "Я уже было хотел уходить, но Ольга Дмитриевна меня остановила."
    mt "Илья, подожди."
    window hide

    show mt normal pioneer at center with dspr
    $ renpy.pause(1)
    show mt angry pioneer at center with dspr
    
    window show
    mt "Где ты был вчера вечером?"
    window hide

    stop ambience fadeout 2
    stop music fadeout 2
    $ renpy.pause(2)
    
    window show
    ".{w}.{w}."
    th "Чёрт."
    nd_il "Я в домике спал."
    mt "А Алиса, не знаешь?"
    nd_il "Знаю, мы с ней гуляли вчера, а потом разошлись по домам."
    
    show mt normal pioneer at center with dspr
    
    mt "Понятно.{w} Значит это не вы." 
    nd_il "А что случилось?"
    mt "Вчера кто-то столовую открыл и булки украл.{w} Ещё и стакан на кухне разбили.{w} Я думала, что это вы с Алисой, но, если вы были в домиках, значит это из другого отряда мальчишки."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Да.{w} Наверное...{nw=1}"
    mt "Ладно, извините что на вас подумала."
    nd_il "Ничего страшного."
    window hide

    hide mt with dspr
    play ambience ambience_camp_center_day fadein 3
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    
    window show
    "Я развернулся и пошёл к умывальникам."
    th "Выкрутился.{w} Как всегда.{w} Единственными свидетелями нашей причастности была Ульяна.{w} Ну и я, соответственно.{w} Славя, которая, по-видимому, ничего не успела понять.{w} Слава богу, всё обошлось."
    th "Главное, чтобы теперь Ульяна ничего не рассказала.{w} Хотя какой ей смысл?{w} Она тоже в этом участвовала, пусть и за другую сторону."
    th "А вот с планом плохо получилось.{w} Не стоило, наверное, идти на дело с Алисой.{w} Я же Ульяне помочь сначала обещал."
    th "Ладно, что было, того не изменить.{w} Сейчас моя приоритетная цель: понять зачем я тут и наладить свою жизнь."
    th "А может это и есть причина, по которой меня сюда отправили?"
    window hide

    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_washstand_day with dissolve2
    
    window show
    "Вскоре на горизонте показались умывальники."
    window hide

    show black with dissolve
    show bg ext_washstand2_day with dissolve
    
    window show
    "Подойдя к одному из них, я положил умывальные принадлежности рядом и открыл кран."
    window hide

    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream 
    
    window show
    "Из него полилась на вид обычная водопроводная вода."
    "Она была на удивление теплой и свежей.{w} Видимо, на это повлиял и окружающий теплый воздух."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    stop sound_loop
    play sound sfx_close_water_sink
    $ renpy.pause(1)
    scene bg ext_washstand_day with dissolve
    
    window show
    "Закончив с водными процедурами я медленно вытер лицо полотенцем."
    nd_il "Фу-ух.{w} Идеально."
    window hide

    $ renpy.pause(1)
    scene bg ext_washstand_day with vpunch
    stop music fadeout 2
    
    window show
    "Внезапно кто-то ударил меня по плечу."
    "Повернувшись, я увидел улыбающуюся Алису."
    
    show dv grin pioneer2 at center with dspr
    
    dv "Ну что, соня, как поспал?"
    nd_il "Нормально.{w} Выспался."
    
    show dv normal pioneer2 at center with dspr
    
    dv "Ещё бы.{w} Слушай, ты Ульяну не видел?"
    nd_il "Нет, что-то случилось?"
    dv "Просто я её с утра не видела."
    dv "Может она, конечно, в футбол играет с малышнёй спозаранку, как обычно.{w} Но всё-же."
    window hide

    $ renpy.pause(1)

    window show
    "Я немного задумался.{w} Лучшая подруга Ульяны, и не знает, где она может быть."
    
    nd_il "А на утренних сборах она была?"
    dv "В том-то и дело, что не было её."
    th "Ну, с её характером, хоть я и знаком с ней день от силы, думаю, она вполне могла сбежать из лагеря на какой-нибудь машине.{w} Или её просто родители забрали, что маловероятно."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Может, сбежала из лагеря? Если так, и она не появится к полднику, надо будет её найти."
    dv "Логично. Но она такая, что может хоть целый день прятаться ото всех."
    window hide

    $ renpy.pause (1)
    
    show dv smile pioneer2 at center with dspr

    window show
    dv "Ещё я предложить хотела, может пойдём, я тебя ещё чему-нибудь на гитаре научу?"
    nd_il "Я бы с радостью, но мне нужно ещё с бегунком пройтись везде и росписи собрать."
    
    show dv grin pioneer2 at center with dspr
    
    dv "Тебя уже наша вожатка что-ли запрягла?"
    nd_il "Ага."
    dv "Ну, ты если что приходи на сцену или к моему домику.{w} И никому ни слова про вчерашнее."
    
    hide dv with dspr
    play music music_list["my_daily_life"] fadein 3
    
    "Сказала Алиса и пошла дальше, а я стоял с умывальными принадлежностями и провожал её взглядом."
    th "Ну что-же.{w} Сейчас отнесу умывальные принадлежности и побегаю с бегунком.{w} Но перед этим схожу в столовую.{w} Не с умывальными принадлежностями, конечно..."
    window hide

    $ renpy.pause (1)

    window show
    "Я отправился к своему домику…"
    window hide

    $ renpy.pause(2)
    show black with dissolve
    $ renpy.pause(3)
    scene bg ext_house_of_sl_day with dissolve2
    $ renpy.pause(1)
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 1
    scene bg int_house_of_gg_day with dissolve
    play sound sfx_close_door_1

    window show
    "Зайдя внутрь я закинул умывальные принадлежности в маленький шкафчик."
    th "Ну, в принципе, всё."
    th "Теперь бы на завтрак сходить.{w} Хотя скоро уже обед."
    th "Все равно схожу. Может мне перепадёт хотя-бы сладкий чай."
    window hide

    play sound sfx_open_door_1
    scene bg ext_house_of_sl_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    play sound sfx_close_door_1
    $ renpy.pause(1) 
    show black with dissolve
    
    window show
    "Выйдя из домика, я направился по своей памяти к столовой."
    window hide

    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve2
    
    window show
    th "...Интересно, мне что, придется теперь на постоянной основе в лагере жить?{w} Участвовать во всех мероприятиях нашей вожатой…{w} Похоже, что да. Но как-же моя квартира?"
    th "Да что я всё о доме думаю?" 
    th "Блин... Там же ипотека не уплачена... Надеюсь мне поверят, что я был в Советском Союзе."
    window hide

    $ renpy.pause(1) 
    show black with dissolve
    $ renpy.pause(1) 
    scene bg sklad with dissolve2
    stop music fadeout 2
    $ renpy.pause(2) 
    play sound sfx_hiding_in_bush
    $ renpy.pause(0.5)
    
    window show
    "Проходя мимо склада я услышал, как что-то зашуршало в кустах."
    with hpunch
    nd_il "Кто там такое!?"
    window hide

    $ renpy.pause(1) 

    window show
    "Мне никто не ответил.{w} Кусты перестали шевелиться."
    th "Блин.{w} Чертовщина какая-то рядом с этим складом творится.{w} Погодите-ка, а что я делаю рядом со складом, если мне нужно в столовую?"
    "Я сверился с картой, и поняв, что шел не туда, повернул обратно."
    nd_il "На этот раз, надеюсь, я приду куда нужно."
    window hide    

    $ renpy.pause(2)
    show black with dissolve
    play sound sfx_hiding_in_bush
    play sound_loop sfx_far_steps fadein 1
    $ renpy.pause(2)
    stop sound_loop fadeout 1
    play sound sfx_hiding_in_bush
    $ renpy.pause(1)
    scene bg ext_dining_hall_away_day with dissolve2

    window show
    "На моё собственное удивление, со второго раза, я наконец пришел к столовой."
    window hide

    scene bg ext_dining_hall_near_day with dissolve 
    
    window show
    "Взобравшись на веранду, я поспешно вошёл внутрь."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    scene black with dissolve

    play sound sfx_open_door_clubs
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve2
    
    window show
    "В столовой было не совсем людно.{w} Большинство пионеров, по-видимому, занимались своими обыденными делами по типу работы в кружках.{w} Один я ошивался по лагерю без дела.{w} Хотя почему без дела?"
    window hide

    $ renpy.pause(2)
    
    window show
    "Оглядев столовую, я увидел Славю, которая сидела за столом одна, и молча пила чай." 
    "Я подсел к ней."
    window hide

    $ renpy.pause(1)
    show sl normal pioneer at center with dspr
    $ renpy.pause(1)
    
    window show
    sl "Привет, Илья."
    nd_il "И тебе привет."
    window hide

    $ renpy.pause(1)
    
    window show
    sl "Почему тебя на линейке не было?"
    nd_il "Проспал."
    window hide

    show sl smile pioneer at center with dspr
    
    window show
    sl "Как так? Я думала, в таком лагере не возможно проспать."
    nd_il "Да я с непривычки просто.{w} Подъем очень ранний."
    sl "Тебе ещё повезло.{w} Тут подъем позже чем в других лагерях, и не наказывают сильно." 
    window hide

    $ renpy.pause(1)
    show sl normal pioneer at center with dspr
    
    window show
    sl "Кстати, тебе вожатая рассказывала про вчерашний случай в столовой?"
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Да...{w} Кто-то ворвался внутрь и кружку разбил."
    sl "И убежали через окно.{w} Их двое было.{w} Это я по шуму поняла."
    "Мне стало немного стыдно от своего поступка, и я замолчал на некоторое время."
    window hide

    $ renpy.pause(1)
    
    window show
    sl "А зачем ты сюда пришёл?"
    nd_il "Покушать пришёл. Вот, сижу... "
    
    show sl laugh pioneer at center with dspr
    
    sl "Боишься поваров попросить что ли?"    
    nd_il "Нет. Не боюсь, просто..."
    
    show sl smile pioneer at center with dspr
    
    sl "Поняла. Подожди немного."
    window hide
    
    hide sl with dissolve
    
    $ renpy.pause(1)

    window show
    "Сказав это, Славя встала из-за стола и подошла к поварам." 
    "Те любезно положили ей горячую порцию макарон с отварной курицей.{w} Взяв вилку, она подошла к столу и положила эту порцию мне."
    
    show sl smile pioneer at center with dspr
    
    "Запах еды вскружил мне голову."
    sl "Приятного аппетита."
    nd_il "Спасибо."
    
    hide sl with dspr
    
    "Я начал уплетать это аппетитное блюдо.{w} Славя сидела рядом и молча смотрела то на меня, то на свой стакан с чаем."
    "И это продолжалось достаточно продолжительное время..."
    window hide

    $ renpy.pause(2)
    
    window show
    "После очередного раза, когда она взглянула на меня, я решил задать назревший у меня в голове вопрос."
    nd_il "У меня что-то на лице?"
    
    show sl smile pioneer at center with dspr
    
    sl "Нет, прости.{w} Просто.{w} Я ещё никогда не видела, чтобы кто-то так наслаждался едой в этой столовой."
    nd_il "Ну я же не завтракал ещё… "
    sl "Ну это понятно…"
    window hide

    $ renpy.pause(1)

    window show
    sl "А тебе нравится в лагере?"
    "После короткой паузы спросила Славяна."
    th "Что же вы все об этом спрашиваете?"
    nd_il "Да.{w} Вполне.{w} Кажется, что здесь мои мечты сбываются."

    show sl laugh pioneer at center with dspr
    
    "После моих слов Славя рассмеялась."
    sl "Рада это слышать.{w} Некоторые вообще уехать отсюда хотят."
    nd_il "Неблагодарные.{w} Не ценят того, что имеют, пока не потеряют."
    th "Особенно еду."
    
    show sl smile pioneer at center with dspr
    
    sl "Ты прям так заумно говоришь этими пословицами."
    sl "Ты поэт что-ли?"
    window hide

    $ renpy.pause(1)
    
    window show
    "Мне на секунду показалось, что последние фразы она сказала как-то наигранно."
    th "Может, эта девушка видит меня насквозь?{w} Может она знает что-то?{w} Может она видела меня вчера в столовой, и просто делает вид, что не видела?"
    nd_il "Нет.{w} Слушай, можно задать глупый вопрос?"
    
    show sl normal pioneer at center with dspr
    
    sl "Нет."
    "Она ответила коротко и ясно.{w} И именно это слово поставило точку в моей трапезе."
    nd_il "Ладно.{w} Вот я и позавтракал.{w} Пойду я…"
    window hide

    $ renpy.pause(1) 
    
    window show
    "Я уже начал вставать, чтобы отнести за собой посуду, но Славя меня остановила."
    window hide

    $ renpy.pause(1) 
    
    window show
    sl "Подожди.{w} Можешь мне помочь в библиотеке?"
    nd_il "Прости, мне ещё бегунок."
    "Сказал я, относя за собой посуду, а затем быстренько вышмыгнул из столовой."
    window hide

    stop ambience fadeout 3
    scene black with dissolve
    play ambience ambience_camp_center_day fadein 3
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    scene bg ext_dining_hall_away_day with dissolve2
    
    window show
    th "Ну что-ж, теперь пойду за подписями..."
    window hide

    $ renpy.pause(0.5)
    play sound nds_list['nd_map_open']
    $ renpy.pause(0.5)
    
    window show
    "Я достал карту из кармана и сверился с бегунком…"
    window hide

    jump podpishite_my_peticiu


label notdreamdaytwo_us_nir:

    window show
    "Я проснулся от ярких лучей солнца,{w} каким-то образом просочившиеся в мои глаза через закрытые веки."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Может еще часик полежать?"
    "Подумал я, и попытался повернуться на правый бок, но ничего не получилось.{w} Мою руку как будто что-то придавило."
    "Как будто камень.{w} Хотя признаться, камень за ночь будет слегка холоднее."
    window hide

    $ renpy.pause(1)

    window show
    th "Погодите, почему в моей квартире меня встречает камень и печёт солнце?"
    th "Почему солнце вообще печёт зимой?"
    th "Думаю, мне пора вставать..."
    window hide

    play music ndm_list['nd_dance_in_the_forest'] fadein 4
    scene bg ext_polyana_day 
    show unblink
    play ambience ambience_forest_day fadein 3
    
    $ renpy.pause(2)
    
    window show
    "Открыв глаза, я заметил,{w} что лежу на зелёной травке,{w} а рядом лежит Ульяна."
    "Она обнимала мою руку и сопела."
    window hide

    $ renpy.pause(1)

    window show
    th "Где-то, на каком-то моменте я, определенно, свернул не туда..."
    window hide

    $ renpy.pause(1)
    
    window show
    "Свободной рукой я залез в карман, вытащил телефон и посмотрел на время."
    "Экран показывал семь часов утра и тридцать процентов заряда батареи."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Так рано у меня ещё никогда не удавалось вставать."
    th "Хотя на это и была своя {i}маленькая{/i} причина."
    window hide

    $ renpy.pause(2)
    
    window show
    th "Раз я не дома, то мне нужно как-то выбираться из этой ситуации..."
    window hide

    $ renpy.pause(1)

    window show
    "Ульяна ещё сильней сжала мою руку.{w} Я, конечно, был бы не против таких обниманий, но ещё чуть-чуть, и она передавит там внутри что-то важное."
    "Тем более, я уже переставал вообще чувствовать свою руку."
    window hide

    $ renpy.pause(2)
    
    window show
    nd_il "Ульяна, просыпайся, уже утро."
    "Не очень громко проговорил я, но это всё равно принесло результат."
    "Ульяна разжала мою руку и повернулась на другой бок."
    us "Ещё пять минуточек."
    "Сообщила она через сон."
    "Теперь я мог порадоваться за освобождение собственной руки."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    hide black with dissolve
    
    window show
    "Но радоваться приходилось не долго.{w} Встал вопрос о том, что мне делать с девушкой, уснувшей в лесу."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ну и что мне с тобой делать?"
    "Задал я вопрос больше самому себе, нежели Ульяне.{w} Ответа не последовало.{w} Она, кажется, действительно спала крепким богатырским сном."
    window hide

    $ renpy.pause(2)
    
    window show
    th "Может её на руках отнести к себе домой?{w} На моем заселении одна кровать в домике была свободна."
    th "Там Ульяна и выспится."
    window hide 

    $ renpy.pause(1)

    window show
    "Потерев ладони друг о друга, и мотивируя себя фразой \"И не такое поднимали\", я взял Ульяну на руки."
    window hide

    $ renpy.pause(1)
    
    window show
    "Половина дела была сделана."
    "Я огляделся, и по памяти направился к лагерю."
    window hide

    $ renpy.pause(1)
    show black with dissolve2
    play sound_loop sfx_far_steps fadein 3
    $ renpy.pause(5)
    stop sound_loop fadeout 3
    $ renpy.pause(1)
    scene bg ext_path_day with dissolve2
    
    window show
    "Таким образом я шёл, пока на моем пути не показалась тропинка, которая дала мне понять, что я на верном пути."
    "Либо, что я кружился на одном месте до этого момента."
    window hide

    play sound sfx_inhale
    $ renpy.pause(1)

    window show
    "Я вздохнул, и отправился по тропинке к лагерю."
    window hide
    
    show black with dissolve2
    $ renpy.pause(1)
    play sound_loop sfx_far_steps fadein 2

    window show
    "Я даже не знал, где в конце концов я выйду, но всё равно продолжал идти,{w} иногда заслушиваясь утренним пением птиц."
    window hide

    $ renpy.pause(3)
    stop sound_loop fadeout 3
    stop ambience fadeout 3
    stop music fadeout 6
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 4 
    scene bg ext_houses_day with dissolve2

    $ renpy.pause(2)

    window show
    "Вскоре я всё-таки добрался до лагеря."
    "Теперь мне нужно было вести себя тихо и не попадаться никому на глаза, особенно вожатой, иначе вопросы неизбежны."
    "Особенно после столовой..."
    window hide

    $ renpy.pause(1)

    window show
    th "Вот черт. Неужели я на это согласился..."
    vg "Ты сам это и затеял, друг мой."
    "После мыслей об ограблении столовой мне стало стыдно.{w} А если кто-то нас видел?"
    "Ладно, будет время подумать об этом.{w} Но не здесь и не сейчас..."
    window hide

    $ renpy.pause(1)

    show black with dissolve2
    $ renpy.pause(3)
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day 
    scene bg int_house_of_gg_day with dissolve2
    play sound sfx_close_door_1
    
    window show
    "Зайдя в свой домик я положил Ульяну на вторую кровать."
    "Она сонно повернулась на другой бок и обняла подушку, на которой лежала." 
    "А я порадовался за то, что руки теперь окончательно смогли отдохнуть.{w} Хотя кто-знает..."
    window hide

    $ renpy.pause(2)

    window show
    th "Фу-ух...{w} Надо-бы умыться."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_cupboard
    $ renpy.pause(1)

    window show
    "Я тихо открыл маленький шкафчик у своей кровати,{w} достал умывальные принадлежности, полотенце, и поспешно вышел из домика, дабы не разбудить Ульяну."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_close_door_1
    
    window show
    "Выйдя на улицу, вдалеке я увидел пробегающую Славю.{w} Но она меня не заметила, и скрылась за углом самого дальнего домика."
    th "Вот существуют ведь люди, которые просыпаются рано и бодрые."
    "Я никогда не понимал таких людей, ведь мне был предпочтительнее сладкий сон, чем бодрая беготня вокруг дома.{w} Да и времени как такового на это у меня не было."
    window hide

    show black with dissolve2
    $ renpy.pause(2)
    scene bg ext_houses_day with dissolve2
    
    window show
    "На улице было прохладно.{w} Особенно для лета.{w} Но погода все равно обещала положительные перемены к обеду."

    play sound sfx_inhale
    
    "Я вдыхал этот прохладный воздух и был погружен в свои раздумья."
    "Но думал я не совсем о воздухе, или о природе."
    window hide

    $ renpy.pause(1)

    window show
    th "Что же это?{w} Мы с Ульяной, действительно, ради конфет и сладких булок ограбили столовую?"
    th "О чем в тот момент я думал?{w} А Алиса?"
    th "Хотя, она тоже хотела ограбить столовую..."
    th "И дверь взламывала она..."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Получается, мы с Ульяной не виноваты?"
    window hide

    $ renpy.pause(1)
    
    window show
    th "Нет.{w} Пускай Алиса и взломала столовую, но сама кража произошла благодаря нам с Ульяной."
    th "В конце концов, может она там что-то забыла, а ключи получить не смогла."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Надеюсь, кроме Алисы об этом инциденте никто не узнает..."
    window hide

    show black with dissolve2
    $ renpy.pause(2)
    play music music_list["went_fishing_caught_a_girl"] fadein 3
    scene bg ext_washstand_day with dissolve2
    $ renpy.pause(1)
    scene bg ext_washstand2_day with dissolve
    $ renpy.pause(1)
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream 
    
    window show
    "Дойдя до умывальников, я достал мыло из пакета, открыл воду и попытался набрать в руки воды."
    window hide

    $ renpy.pause(1)

    window show
    "Отчаянно прислонив ладони к струе воды, я тут же почувствовал, что она недостаточно нагрелась."
    "Это ещё мягко говоря..."
    window hide

    scene bg ext_washstand2_day with vpunch 
    
    window show
    nd_il "Аа! Холодная!"
    "Я моментально отдернул руки от ледяной струи воды."
    th "А ты думал, что тёплая будет? Это же Советский лагерь."
    window hide

    $ renpy.pause(1)

    window show
    "Немного подумав головой, я начал умываться, брызгая ладонью водой себе на лицо."
    "Прилетающих брызг хватало, чтобы совершать эту утреннюю процедуру,{w} и у меня даже поднялось настроение от своей сообразительности..."
    window hide

    $ renpy.pause(2)

    window show
    "За моей спиной послышалось тихое хихиканье."
    window hide

    stop sound_loop
    play sound sfx_close_water_sink
    scene bg ext_washstand_day with dissolve
    show un laugh sport far at center with dspr
    
    window show
    "Обернувшись, я увидел Лену в белой спортивной форме, которая была ей к лицу и подчёркивала всё то, что должна подчеркивать в девушке."
    nd_il "Доброе утро."
    "Сказал я, немного удивившись её появлению, ведь пару секунд назад тут никого не было.{w} По крайней мере, я был в этом уверен."
    un "Доброе утро."
    window hide

    show un smile sport far at center with dspr
    
    window show
    un "Ты так смешно умываешься."
    nd_il "Может и так.{w} Вода до жути холодная."
    un "Знаю."
    un "Как у тебя дела?"
    un "Тебя вчера на танцах не было."
    nd_il "Не хотелось вчера никуда идти.{w} А дела у меня нормально."
    nd_il "Природой, вот, любуюсь..."
    "Я настолько правдоподобно соврал, что даже сам смог бы поверить в мною сказанное."
    window hide

    $ renpy.pause(1)
    
    window show
    un "Тут и вправду красиво. Особенно утром, когда всё распускается."
    window hide

    $ renpy.pause(1)
    
    window show
    un "Ну ладно, я побежала, увидимся на линейке."

    hide un with dspr
    
    "Сказала Лена и побежала легким бегом в сторону площади."
    window hide
    
    $ renpy.pause(1)

    window show
    th "Интересно, чего это она решила у меня за настроение спросить?{w} Девушки в этом лагере какие-то странные."
    th "Появляются из неоткуда, бегают по утрам, да еще и инициативу в общении проявляют."
    th "Прошлый раз, когда я подошёл к девушке на улице и предложил познакомиться, она всеми силами искала способ уйти от разговора."
    th "Неужели дело в том, что я умылся?{w} А как я выглядел вчера?"
    vg "Уверен, зрелище было не из приятных."
    th "Тебе ли об этом говорить..."
    window hide

    show black with dissolve
    $ renpy.pause(0.5)
    scene bg ext_washstand2_day with dissolve
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream 
    
    window show
    "Я, отчасти, завидовал Лене, ведь дома у меня никогда не получалось вставать раньше десяти часов."
    "Хотя сегодня что-то изменилось."
    "По моему мнению в этом был виноват свежий воздух лагеря, который определённо шёл мне на пользу."
    "Или та самая соня, не давшая своими \"обниманиями\" поспать мне до обеда..."
    window hide

    show black with dissolve2
    $ renpy.pause(2)
    stop sound_loop
    play sound sfx_close_water_sink
    
    window show
    "Закончив свои водные процедуры, я закрыл кран и вытер лицо полотенцем."
    window hide

    scene bg ext_washstand_day with dissolve
    
    window hide
    "На небе не было ни облачка, а солнечные лучи приятно согревали кожу."
    window show

    show black with dissolve2
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve2
    
    window show
    "Я неспеша шел к своему лагерному домику..."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Интересно, теперь мне придётся на постоянной основе тут жить?"
    th "Когда я засыпал вчера, я думал, что проснусь у себя в квартире. Но этого, по видимому, не случилось."
    th "Сколько же будет идти эта смена?"
    window hide
    
    $ renpy.pause(1)
    
    window show   
    "Помимо этого вопроса меня интересовали большинство остальных, на которые пока не было ответов.{w} Лишь предположения."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Может я здесь из-за своего неправильного образа жизни?{w} Может этот лагерь призван меня исправить, изменить меня как личность?"
    th "Не может же моё попадание сюда быть чистейшей случайностью..."
    window hide

    $ renpy.pause(1)
    
    scene bg ext_house_of_sl_day with dissolve
    $ renpy.pause(1)
    play sound sfx_open_door_1
    scene bg int_house_of_gg_day with dissolve
    play ambience ambience_int_cabin_day fadein 2
    play sound sfx_close_door_1
    
    window show
    "Дойдя до своего домика и открыв дверь, я увидел Ульяну, сидящую на кровати и подтягивающуюся."
    window hide

    show us normal pioneer far at right with dspr
    
    window show
    us "О, доброе утро."
    nd_il "Доброе."
    us "А как я тут оказалась?"
    nd_il "Вчера ты уснула в лесу, а я спать в домик пошёл."
    nd_il "И сегодня утром решил тебя забрать."

    stop music fadeout 4

    hide us with dspr
    show us dontlike pioneer far at center with dspr
    us "Ты ку-ку?"
    nd_il "Ладно, шучу.{w} Мы вчера с тобой вместе уснули."
    show us normal pioneer far at center with dspr
    nd_il "Надеюсь вопросов у других пионеров насчет этого не будет."
    us "Ой."
    us "Это правда что мы вместе спали?"
    nd_il "Да."
    show us surp3 pioneer far at center with dspr
    us "Фу-фу-фу."
    us "Почему ты меня не отнёс домой?"
    nd_il "А что подумала бы Алиса?{w} Мы её напугали, а потом придём к ней после ограбления наеденные конфетами."
    nd_il "Она вчера так на меня смотрела, будто убить хотела."
    nd_il "К тому же ты могла сама уйти, а меня в лесу оставить."
    show us shy pioneer far at center with dspr
    us "Не хорошо это, товарищей в лесу оставлять."
    us "Вообще ты сам виноват. Вот."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)
    window show
    nd_il "Прости..."
    show us shy pioneer far at center with dspr
    us "Ничего страшного, проехали."
    window hide

    hide us with dspr

    $ renpy.pause(2, hard=True)
    
    play music music_list["went_fishing_caught_a_girl"] fadein 4

    window show
    "Ульяна посмотрела в окно, а затем на меня."
    "Её лицо уже не отражало в себе смущения от диалога, случившегося минуту назад."
    "Казалось, она что-то задумала, но пыталась не подавать виду. Однако это были только догадки."

    show us normal pioneer at cright with dspr
    
    us "Ну и что будем делать?"
    "Заинтересованно спросила меня Ульяна, и не дав ответить продолжила..."
    us "Давай поиграем?"
    nd_il "Давай. А во что?"
    us "Не знаю, а ты во что хочешь?"
    "Я задумался."
    window hide

    $ renpy.pause(1)

    window show
    th "А может в \"Эрудит\"?"
    vg "Тебе говорили, что ты сама оригинальность?"
    th "А что, нормальная игра."
    vg "Ну да, по сравнению с тем, как ты играешь в \"Правда или действие\"..."
    th "Отстань. Нормальная игра."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Давай поиграем в игру \"Эрудит\"."
    
    show us smile pioneer at cright with dspr
    
    "Она согласно кивнула, и теперь нам оставалось решить, каким будет первое слово, из которого нужно составить маленькие."
    nd_il "Первым словом будет \"Информатика\""
    "Сказал я и записал его в телефонной заметке."
    nd_il "Из этого слова нужно будет составлять слова поменьше. Например \"форма\"."
    
    show us grin pioneer at cright with dspr
    
    us "Поняла.{w} Мы в такое в школе играли."
    us "Поэтому тебя будет легко выиграть."
    nd_il "Ну посмотрим..." 
    us "Чур я первая."
    us "Моё слово — \"мат\"."
    window hide

    $ renpy.pause(2)

    if persistent.nd_first_play_qte_d2 == True:
        
        menu:
            "Выиграть": 

                $ renpy.pause(1, hard=True)

                show black with dissolve

                $ renpy.pause(2, hard=True)

                $ qtr_miss = 0
                jump nd_winner_d2
            
            "Поддаться Ульяне":
                $ qtr_miss = 2
                $ usrr += 1
                jump nd_winner_d2

            "Играть самому":
                pass


    window show
    toriel "Нажимай кнопки клавиатуры, которые будут отображены на экране."
    toriel "Убедись, что раскладка клавиатуры на русском языке."
    toriel "Начинаем."
    window hide

    show stickyword with dissolve
    $ winlose = renpy.call_screen("scr_qte", word="кит", time=4.0, _layer="master")
    hide stickyword with dissolve

    if winlose:
        window show
        nd_il "Кит."

    else:

        window show
        nd_il "Так..."
        us "Илья, это же легко."
        us "Кит."
        window hide

        show stickyword with dissolve
        $ winlose = renpy.call_screen("scr_qte", word="тик", time=4.0, _layer="master")
        hide stickyword with dissolve

        window show
        nd_il "Тик."
        us "Во-от. Правильно мыслишь."

    us "Икона..."
    window hide

    show black with dissolve
    $ renpy.pause(2)
    
    window show
    "По началу было легко, но после перечисления всех очевидных комбинаций приходилось ломать голову."
    window hide

    $ renpy.pause(1)
    hide black with dissolve 

    show stickyword with dissolve
    $ winlose = renpy.call_screen("scr_qte", word="аромат", time=4.0, _layer="master")
    hide stickyword with dissolve

    if winlose:
        
        window show
        nd_il "Аромат."
        us "Финик."
        nd_il "Уже было."
        window hide

        show us smile pioneer at cright with dspr
        $ renpy.pause(1)

        window show
        us "Тогда форма."
        nd_il "Это тоже было."
        us "Сдаюсь, говори."
        window hide

        show stickyword with dissolve
        $ winlose = renpy.call_screen("scr_qte", word="корм", time=4.0, _layer="master")
        hide stickyword with dissolve

        if winlose:

            window show
            nd_il "Корм."

            show us normal pioneer at cright with dspr
            
            us "Ой. А разве слова \"корм\" не было?"
            us "Во, знаю."
            us "Фирма."
            nd_il "Уже было."

            show us sad pioneer at cright with dspr


            us "Что-то у меня не ладится. Давай сначала?"
            nd_il "Ну давай.{w} Соберись что-ли."
            window hide
        
        else:

            $ qtr_miss += 1
            
            show us grin pioneer at center with dspr
            window show
            nd_il "Корм."
            us "Ха-ха. Было уже."
            window hide

    else:

        $ qtr_miss += 1
        
        window show
        nd_il "Аромат."
        us "Уже было."
        us "Финик."
        window hide

        show stickyword with dissolve
        $ winlose = renpy.call_screen("scr_qte", word="минор", time=4.0, _layer="master")
        hide stickyword with dissolve

        if winlose:
            window show
            nd_il "Минор."
            us "Фирма..."
            window hide

        else:
            
            $ qtr_miss += 1
            
            window show

            nd_il "Форма."
            
            show us smile pioneer at cright with dspr
            
            us "Было."
            us "Похоже, ты проигрываешь."
            "Сказала Ульяна с улыбкой на лице."
            nd_il "Ничего, мне надо просто разыграться."
            us "Конечно..."
            window hide

    $ renpy.pause(1)

    stop ambience fadeout 2
    show black with dissolve
    hide us
    $ renpy.pause(1)
    
    if persistent.nd_first_play_qte_d2 == False:
        $ persistent.nd_first_play_qte_d2 = True

    window show
    "Вскоре мы решили заново начать играть в эту игру."
    "Но ничего не изменилось."

    if qtr_miss >= 2:
        $ usrr += 1
        "Как я проигрывал вначале, так я проигрывал и сейчас."
        "Даже не знаю, почему."
        "Хоть это была и моя идея, я все равно умудрился проиграть."
    
    else:
        "У Ульяны не получалось никак собраться и переиграть меня."
        "И я не знал, с чем это может быть связано."
        "Может не выспалась, а может ещё что."
        "Мне и самому не верилось, что она не может меня победить в этой игре,{w} несмотря на то, что из её слов: они играли в эту игру в школе."
    window hide

    $ renpy.pause(1)
    stop music fadeout 4
    scene bg int_house_of_gg_day with dissolve
    $ renpy.pause(1)

label nd_winner_d2:

    hide black with dissolve
    $ renpy.pause(1)

    window show

    if qtr_miss >= 2:
        
        show us smile pioneer at center

        window show
        us "У меня больше правильных ответов.{w} Я победила тебя!"
        us "С тебя выполнение моих желаний целый день!"
        "Лицо Ульяны изменилось в широкой улыбке"
        nd_il "Ещё чего. Я тебе просто поддался..."
        
        show us grin pioneer at center with dspr

        us "Ага, оправдывайся."
        us "Ты просто не хочешь признавать своего проигрыша."
        window hide

        $ renpy.pause(2, hard=True)

        show us shy pioneer at center with dspr
        
        window show
        us "Но если это правда - то спасибо..."
        us "...Тебе..."
        window hide

    else:
        
        show us sad pioneer at center with dspr

        window show
        us "Не верится, что ты меня смог обыграть..."
        nd_il "Да ладно тебе, не дуйся, это ведь просто игра."
        window hide

        hide us with dspr
        
        window show
        "Ульяна надула свои щёчки, насупилась и сложила руки."
        us "Мог бы хотя бы поддаться мне для приличия."
        nd_il "Прости, не знал что ты так отреагируешь."

        show us normal pioneer at center with dspr

        us "Ладно. Проехали..."
        window hide

    hide us with dspr

    $ renpy.pause(1)
    play sound sfx_dinner_horn_processed

    window show
    "Наверное Ульяна хотела ещё что-то сказать, но в эту минуту динамик на улице позвал всех пионеров на линейку."
    window hide

    show us normal pioneer at center with dspr

    window show
    nd_il "Ну что, пошли на площадь?"
    us "Илья..."
    window hide

    hide us with dspr
    $ renpy.pause(1)
    stop ambience fadeout 4
    show black with dissolve2
    $ renpy.pause(1)
    play sound sfx_open_door_1

    play ambience ambience_camp_center_day fadein 3
    play music ndm_list['mood_happyending'] fadein 3
    scene bg ext_house_of_sl_day with dissolve2
    $ renpy.pause(1)
    play sound sfx_close_door_1

    window show
    "Мы с Ульяной вышли из моего домика."
    
    show us normal pioneer at center with dspr
    
    us "Илья, извини, но мне нужно по делам."
    nd_il "А линейка?"
    show us grin pioneer at center with dspr
    us "Не скучай. Я скоро вернусь."
    hide us with dspr
    "Ульяна будто меня не услышала, и через секунду её уже и след простыл.{w} Она убежала."
    window hide

    $ renpy.pause(2)
    
    window show
    th "И чего она опять придумала?"
    "Подумал я, почесал голову, и отправился к пункту назначения."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg ext_houses_day with dissolve2

    $ renpy.pause(1)

    window show
    "По пути мне встретился Семён, с которым я ещё ни разу не разговаривал, что было удивительно."
    "Он ко мне вчера ни разу не подошёл.{w} И было неизвестно, подойдет ли он сегодня."
    window hide

    $ renpy.pause(1) 
    
    window show
    "Так и случилось."
    "Он будто хотел у меня что-то спросить..."
    window hide

    $ renpy.pause(1)

    window show
    "Теперь я мог разглядеть этого пионера детальнее."

    show pi2 smile pioneer at center with dspr 
    
    "У Семёна была длинная чёлка, которая закрывала глаза."
    "Одет он был в пионерскую форму, с идеально завязанным пионерским галстуком."
    "Тело его было худощавого телосложения, но выглядел он как обычный пионер."
    window hide

    $ renpy.pause(1)
    
    window show
    me "Привет, Илья. Ты тут новенький, да?"
    nd_il "Привет. Да, мы вчера на площади виделись."
    me "Вас с Ульяной Ольга Дмитриевна вчера вечером искала.{w} Где вы были?"
    nd_il "Да так, в лесу гуляли."
    
    show pi2 smile pioneer at center with dspr
    
    me "Понятно.{w} Вы как-то быстро сдружились."
    nd_il "Ну да, есть такое…"
    window hide

    $ renpy.pause(1)
    
    window show
    "Затем последовала короткая пауза, которую быстро прервал мой собеседник."
    me "Тебя, кстати, какой-то пионер искал, хотел сообщить что-то."
    me "Но я ему сказал, что ты куда-то по своим делам пошёл."
    nd_il "Понятно."
    window hide

    $ renpy.pause(1)

    hide pi2 with dissolve 
    
    window show
    th "Может это какой-нибудь мой знакомый?"
    th "Хотя с какой стати мои знакомые должны быть в пионерлагере?.."
    window hide

    show black with dissolve2
    $ renpy.pause(3, hard=True)
    scene bg ext_square_day with dissolve2
    $ renpy.pause(1)
    scene bg d4_lineup_no_un_us with dissolve 
    stop music fadeout 3
    
    window show
    "Когда я пришел на площадь, все пионеры уже стояли в ровную линейку."
    "Пионеры помладше стояли ровно, не смея сдвинутся с места."
    "А вот пионеры постарше просто разговаривали на свои темы, которые были максимально отдалены от жизни в лагере."
    window hide


    $ renpy.pause(1)
    
    
    
    if us_candy_steal == True:
        jump us_candy_true
    else:
        jump dv_unhappy_d2_lin
        
    
label us_candy_true:
    window show
    "По Алисе было видно, что она явно не выспалась.{w} Искала свою подругу?{w} Обдумывала произошедшее вчера вечером у столовой?{w} Загадка…"
    jump lineyka_normal_1_d2
    
label dv_unhappy_d2_lin:
    window show
    "Алиса посмотрела на меня исподлобья косым взглядом.{w} То-ли обиженно, то-ли с осуждением."
    "Я чувствовал вину за вчерашнее и собирался извиниться.{w} Но только после линейки."
    jump lineyka_normal_1_d2
    
label lineyka_normal_1_d2:
    
    mtp "Доброе утро, лагерь!"
    "Бодро сказала Ольга Дмитриевна."
    all "Доброе утро, Ольга Дмитриевна!"
    "Вяло прокричали пионеры."
    window hide

    $ renpy.pause(2)
    
    window show
    "После утреннего приветствия, Славя гордо вышла поднимать флаг СССР, а затем заиграл соответствующий гимн из висящих на столбах динамиков."
    window hide

    play music ndm_list['gimn'] fadein 2
    $ renpy.pause (4)
    
    $ renpy.pause (13, hard=True)
    show ussr_flag_d1 with dissolve2
    $ renpy.pause (10, hard=True)

    hide ussr_flag_d1 with dissolve2
    stop music fadeout 2
    
    $ renpy.pause (1)

    window show
    "Пока играла эта торжественная песнь, все пионеры стояли как солдаты и не смели двинуться с места, включая Ольгу Дмитриевну и меня."
    window hide

    $ renpy.pause(1)

    play music ndm_list['mood_funny'] fadein 3
    show black with dissolve
    $ renpy.pause(0.5)
    scene bg ext_square_day with dissolve 
    
    window show
    "После гимна началась зарядка." 
    "Большинство пионеров всё еще спали, и делали что-то, отдаленно напоминающее физкультурные упражнения."
    "Я же просто делал вид, что разминаюсь, что у меня, по видимому, правдоподобно получалось."
    "Хотя по факту, притворяясь, что разминаюсь, я незаметно для себя действительно разминался..."
    window hide

    $ renpy.pause(2)
    show black with dissolve
    $ renpy.pause(0.5)
    scene bg d4_lineup_no_un_us with dissolve 
    
    window show
    "После зарядки Ольга Дмитриевна начала объяснять план работы на сегодняшний день."
    "Там было что-то про уборку в библиотеке, про новые препараты для медпункта и всё такое."
    "Но я, как всегда, считал ворон.{w} А если быть точнее - количество поющих птиц на ветках деревьев."
    window hide

    stop music fadeout 4
    scene bg ext_square_day with dissolve
    show mt normal pioneer far at center with dspr
    $ renpy.pause(1)
    show mt normal pioneer at center with dspr
    $ renpy.pause(1)
    show mt angry pioneer at center with dspr

    window show
    mt "Илья, где ты был с Ульяной вчера вечером?{w} И почему её всё еще нет?"
    window hide
    
    $ renpy.pause (1)
    
    window show
    th "Упс..."
    nd_il "Мы вчера в лес за ягодами ходили, а сегодня утром она убежала куда-то."

    
    if dv_leave_d1 == True:
        jump lineyka_dv_unhappy_d2
    else:
        jump lineyka_normal_2_d2
    
    
    
label lineyka_normal_2_d2:
    "Алиса тихо хихикнула."
    
    show mt normal pioneer far at center with dspr 

    mt "Ладно, только если вы уходите, то возвращайтесь к вечеру."
    mt "Я, как вожатая, в ответе за всех вас…"

    hide mt with dspr
    
    "Меня внезапно бросило в дрожь."
    "Но совсем не от речи Ольги Дмитриевны."
    th "Вот почему Ульяна убежала сегодня утром."
    th "Я просто ненормальный..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    
    jump d2_morning_dinning
    
label lineyka_dv_unhappy_d2:
    
    show mt normal pioneer far at center with dspr 

    mt "Ладно, только если вы уходите, то возвращайтесь к вечеру."
    mt "Я, как вожатая, в ответе за всех вас…"

    hide mt with dspr
    
    "Этого я наслушался ещё со школы, поэтому просто думал о своём."
    "Ну, точнее об Ульяне.{w} О том, что я вчера побежал за ней, бросив Алису." 
    "И это был вдвойне не лучший поступок с моей стороны."
    th "Я предал как Алису, так и Ульяну."
    th "Вот почему она убежала..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    jump d2_morning_dinning
    
label d2_morning_dinning:

    play music music_list["my_daily_life"] fadein 4

    show black with dissolve

    scene bg ext_square_day with dissolve
    
    window show
    "Вскоре Ольга Дмитриевна объявила о закрытии утреннего сбора, и весь лагерь отправился к столовой на завтрак."
    "Если мне на него не успеть, то мест совсем не останется."
    "Поэтому мне приходилось бежать быстрее всех, пытаясь прорваться через толпу сонных пионеров, которая была довольно немаленькая."
    window hide

    scene bg ext_dining_hall_away_day with dissolve
    $ renpy.pause(1)
    scene bg ext_dining_hall_near_day with dissolve
    show mt normal pioneer at center with dspr
    
    window show
    "Добежав до столовой, у входа меня остановила Ольга Дмитриевна."
    mt "Илья, после завтрака тебе нужно будет отметиться во всех зданиях и кружках. Можешь даже записаться куда-нибудь"
    "Сказала вожатая и протянула мне бегунок."
    vg "\"Дальше вы не пройдете, пока не получите бумаги.\""
    mt "…А затем зайди ко мне. Я дам тебе новое задание."
    window hide

    hide mt with dspr
    $ renpy.pause(1)

    window show
    nd_il "Квест получен."
    "Отшутился я и поспешил в столовую."
    window hide

    play sound sfx_open_door_1
    show black with dissolve2

    $ renpy.pause(1)

    if dv_leave_d1 == True:
        jump d2_morning_dinning_dv_sorry_1
    else:
        jump d2_morning_dinning_slav_sorry
    
label d2_morning_dinning_slav_sorry:
    
    scene bg int_dining_hall_people_day with dissolve  
    play ambience ambience_dining_hall_full fadein 2

    window show
    "Так как я был одним из первых, мне открылся широкий выбор свободных мест."
    "Взяв порцию, и, обогнув взглядом столовую, я нашел свободное место за столом, где сидела Славяна."
    window hide
    
    $ renpy.pause(1)
    
    window show
    th "Вчера мы с Ульяной обещали ей площадь подготовить и убежали.{w} Плохо получилось..."
    th "Надо извиниться перед ней..."
    "Подумал я и подошел к её столу."
    window hide

    $ renpy.pause(1)
    show sl normal pioneer at center with dspr
    
    window show
    nd_il "Привет.{w} Можно сесть?"
    show sl smile pioneer at center with dspr
    sl "Доброе утро. Можно."
    "Я послушно приземлился на стул."

    hide sl with dspr
    
    "В тарелке был обычный омлет. Это конечно не пюре и не котлета, но хоть что-то."
    nd_il "Славя, прости нас с Ульяной, за то, что мы вчера не пришли площадь для танцев готовить."
    
    show sl smile pioneer at center with dspr
    
    sl "Ничего страшного, Илья.{w} Я не обиделась."
    sl "Шурик и Электроник во всём разобрались."
    window hide

    hide sl with dspr

    nd_il "Ну, ладно тогда."
    window hide

    $ renpy.pause(2)
    
    window show
    nd_il "Расскажи как тут в лагере. Я просто ни разу не был в лагерях."
    
    show sl laugh pioneer at center with dspr
    
    sl "Что, прямо ни разу?"
    nd_il "Да, ни разу."
    
    show sl smile pioneer at center with dspr
    
    sl "Вообще, в этом лагере весело, здесь нет таких жестоких запретов, как в других лагерях."
    sl "И подъем тут позже, и не наказывают сильно. Тебе тут понравится."
    nd_il "С подъемом мне, конечно, отчасти повезло…"
    
    hide sl with dspr
    
    "Сказал я и продолжил трапезу."
    window hide

    $ renpy.pause(3)

    show un smile pioneer far at left 
    show mi normal pioneer far at fleft
    with dspr

    window show
    "Левым краем глаза я заметил, как к нашему столу подошли уже известные мне пионерки{w} - Лена и Маша."

    un "Можно к вам сесть?"

    show sl smile pioneer close at center with dspr
    
    sl "Да, садитесь."
    
    show un normal pioneer at left
    show mi normal pioneer at right
    with dspr
    
    "Пионерки поставили порции и сели за стол."
    "Между ними началась оживлённая беседа, а я просто ел свой завтрак и думал о своём..."
    window hide

    hide un
    hide mi
    hide sl
    with dspr
    
    jump d2_razmysh_us_wat
    
label d2_morning_dinning_dv_sorry_1:   
    
    scene bg int_dining_hall_people_day with dissolve
    play ambience ambience_dining_hall_full fadein 2    
    
    window show
    "Так как я был одним из первых, мне открылся широкий выбор свободных мест за столами." 
    "Взяв порцию и, обогнув взглядом столовую, я нашел свободное место рядом с Алисой и просто пустой стол."
    window hide

    jump d2_morning_dinning_dv_sorry_2
   
label d2_morning_dinning_dv_sorry_2:

    $ d2_dv_morning_din_sorry = True

    $ renpy.pause(1)

    window show
    th "Надо извиниться перед Алисой за вчерашнее..."
    "Подумал я и подошел к её столу."
    window hide

    $ renpy.pause (1)
    
    show dv normal pioneer at center with dspr
    
    window show
    nd_il "Можно сесть?"
    dv "Ну садись."
    "Я послушно приземлился на стул."
    "В тарелке был обычный омлет.{w} И этого было для меня вполне достаточно, учитывая то, чем я питался до попадания в этот лагерь."
    nd_il "Алиса, прости пожалуйста."
    window hide

    show dv shocked pioneer at center with dspr
    
    window show
    dv "За что?"
    nd_il "За то, что оставил тебя в столовой и побежал за Ульяной."
    window hide

    $ renpy.pause(1)
    
    show dv grin pioneer at center with dspr
    
    window show
    dv "Да ничего страшного, булки хоть вернул?"
    "В этот момент у меня как будто камень м плеч упал.{w} Признаться, так легко мне еще никогда не было.{w} Или я этого не помню..."
    nd_il "Нет."
    dv "Эх ты.{w} Не догнал её значит.{w} Не удивительно.{w} Её никто догнать не может."
    dv "Только не понятно.{w} Почему ни тебя ни Ульяны не было вчера вечером."
    
    show dv laugh pioneer at center with dspr
    
    dv "Значит всё-таки догнал, и даже в лагере не появился. Странно..."
    "С многозначной улыбкой Алиса взглянула на меня.{w} Я отвернул свой взгляд в другую сторону."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Не было ничего такого.{w} Просто под звездным небом уснули."
    window hide

    $ renpy.pause(1)
    
    show dv smile pioneer at center with dspr
    
    window show
    dv "Ясный перец.{w} Ладно, не буду вас трогать."
    show dv normal pioneer at center with dspr
    
    dv "Только смотри, чтобы ты её не обижал."
    dv "А то тебе точно конец."
    nd_il "Ладно, ладно. Полегче."
    nd_il "И не собирался."
    dv "Смотри у меня."
    window hide

    hide dv with dspr
    
    $ renpy.pause(2)

    jump d2_razmysh_us_wat
    
label d2_razmysh_us_wat:

    $ renpy.pause(1)

    window show
    th "Интересно, куда Ульяна сегодня утром ушла?"
    th "Видимо, я её как-то спугнул чем-то."
    vg "Ага. Своим лицом."
    th "Шутку про лицо я от тебя сегодня уже слышал."
    vg "И не раз ещё услышишь. Буду напоминать чтобы не забывал."
    th "Ну ты и токсик..."
    window hide

    show black with dissolve
    $ renpy.pause(2)

    stop music fadeout 3
    $ renpy.pause(2)
    hide black with dissolve

    window show
    "Оглянувшись за столом я понял, что уже давно сижу один."
    "Значит и мне пора перестать потчевать и идти отсюда по своим делам."
    "А точнее, бесцельно бегать с бегунком по всему лагерю, попутно удивляясь всему происходящему вокруг."

    th "Ну ладно. Зато новые места повидаю."
    th "Клубы, книги и медпункт, я иду к вам..."
    window hide

    show black with dissolve2
    $ renpy.pause(1)
    play sound sfx_open_door_1
    $ renpy.pause(2)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve2
    play sound sfx_close_door_1
    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_dining_hall_away_day with dissolve
    $ renpy.pause(2)
    
    window show
    th "Так, теперь мне необходимо решить, куда пойти сначала..."
    window hide

    $ renpy.pause(1)
    
    play sound nds_list['nd_map_open']    
    
    $ renpy.pause(1)

    window show
    "Я достал карту из кармана и развернул её..."
    window hide

label podpishite_my_peticiu:


#Карта держится на 5-ти костылях
    
    $ disable_all_zones()
    $ set_zone("music_club", "muzclub_begun_d2") 
    $ set_zone("library", "library_d2_begun_1") 
    $ set_zone("medic_house", "aidpost_d2_begun")
    $ set_zone("clubs", "kibernetis_begun_d2")        
    


    if necessary_clubs == 1:
        $ reset_zone("clubs")
    
    if necessary_musclub == 1:
        $ reset_zone("music_club")
        
    if necessary_library == 1:
        $ reset_zone("library")
        
    if necessary_aidpost == 1:
        $ reset_zone("medic_house") 
    
    if necessary_map == 4:
        jump d2_begun_end_1
        
    
    play music ndm_list['map_music_postal'] fadein 2
    $ show_map()


label kibernetis_begun_d2:
    $ disable_current_zone()
    $ necessary_clubs += 1
    $ necessary_map += 1
    
    stop music fadeout 2
    show black with dissolve    
    $ renpy.pause(2)    
    scene bg ext_clubs_day with dissolve2
    $ renpy.pause(1)
    
    window show
    "Я узнал это здание сразу-же, как только оно показалось на горизонте." 
    "У него были металлические стены и металлическая дверь."
    "Не смотря на свою громоздкость, снаружи здание выглядело аккуратным, как и окружающие его предметы: лестница, каменная дорожка, скамейка неподалёку."
    window hide

    $ renpy.pause(1)
    play sound sfx_knocking_door_2
    $ renpy.pause(1)
    
    window show
    "Я произвел несколько стуков костяшкой среднего пальца, и спустя некоторое время мужской голос за дверью пригласил меня внутрь."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 3
    scene black with dissolve
    play sound sfx_open_door_clubs
    scene bg int_clubs_male_day with dissolve
    play music music_list["smooth_machine"] fadein 3
    $ renpy.pause(1)
    play sound sfx_close_door_1
    play ambience ambience_int_cabin_day fadein 3
    
    window show
    "Войдя в здание, я увидел рабочее помещение. На столе, стоящем посередине комнаты, лежал радиоприёмник, а рядом валялись детали от него.{w} В углу стоял шкаф с различными инструментами."
    "Аккуратная красная лодка красовалась на самом его верху."
    "Так же в глаза бросались самолеты, нитками подвешенные под потолком, и гармонично шатающиеся от ветерка, дующего с окон."    
    window hide

    $ renpy.pause(3)
    
    show sh normal pioneer far at cright
    show el normal pioneer far at cleft
    with dspr
    
    window show
    "Вскоре из подсобки ко мне вышли два высоких парня. Они были одеты как обычные пионеры, ничем не отличающиеся от других таких же пионеров."
    "Разве что были слишком похожи друг на друга, что не есть хорошо. По крайней мере для меня, ведь мне ещё их имена запоминать."

    nd_il "Привет, меня Ильёй зовут. Я за подписью пришел."
    
    "Сказал я и отдал им бегунок."

    sh "Привет. Меня Шуриком, а это мой коллега Электроник." 
    "Электроник молча кивнул головой."
    sh "Слушай, не хочешь вступить в наш клуб? Мы сейчас занимаемся секретной разработкой."
    "Взяв бегунок, сказал Шурик."
    
    hide sh with dspr
    
    th "Знаю я эти секретные разработки советских учёных.{w} Крем звездочку небось модифицируют."
    nd_il "Я подумаю."

    show sh normal pioneer far at cright with dspr
    
    sh "Ну как хочешь. Когда надумаешь — приходи."
    "Сказал мне советский учёный и протянул бегунок со своей подписью."

    hide sh
    hide el
    with dspr

    "Я взял бегунок, и уже собирался уходить, как вдруг вспомнил про то, что на моём телефоне заряд не бесконечный. И эту проблему в лагере могли решить только кибернетики."
    window hide

    $ renpy.pause(1)
    
    show sh normal pioneer far at cright
    show el normal pioneer far at cleft
    with dspr

    window show
    nd_il "Слушайте, а вы можете создать зарядное устройство для вот такого аккумулятора?"
    "Сказал я, вынул из своего телефона аккумулятор и отдал его кибернетикам."

    hide el with dspr

    "Электроник начал вдумчиво осматривать батарею у себя в руке, всячески вертеть и пытаться читать надписи на ней."
    window hide

    $ renpy.pause(1)

    show el smile pioneer far at cleft with dspr

    window show
    el "Видно, что импортный. Попробуем, но что ты можешь предложить взамен?"
    "Я немного подумал, а затем достал из кармана наушники.{w} Если выбирать между музыкой в наушниках и зарядкой для телефона, я бы выбрал второе."
    "Было жалко расставаться с ними. Но я понимал, что их отсутствие для меня не так критично, как отсутствие заряда батареи."
    "Поэтому я без замедления протянул руку с динамиками на проводах кибернетикам."
    nd_il "Держите."
    window hide

    $ renpy.pause(1)
    hide el
    hide sh
    with dspr

    window show
    "Шурик и Электроник взяли у меня наушники и начали осматривать их, а точнее штекер. Было видно, что он их интересует больше, чем сами наушники."
    window hide

    $ renpy.pause(2)

    show sh normal pioneer far at cright with dspr
    show el laugh pioneer far at cleft with dspr
    with hpunch
    
    window show
    el "Управимся за короткий срок!"
    th "И чего он так орет?"
    nd_il "Выручил."
    "Сказал я и пожал ему руку."
    nd_il "Ну ладно, пацаны, я пошёл."
    window hide

    $ renpy.pause(1)
    stop music fadeout 3
    show black with dissolve
    play sound sfx_open_door_clubs
    $ renpy.pause(1)
    scene bg ext_clubs_day with dissolve
    play sound sfx_close_door_1
    play ambience ambience_camp_center_day fadein 3

    window show
    th "У них весело.{w} Вот только пока придется без телефона походить." 
    th "Сразу видно, любят свою работу.{w} Умеют, могут, практикуют.{w} Все во благо Советского Союза!"
    th "Ох. Чего это со мной?{w} По видимому, советский лагерь делает свое дело..."
    window hide

    $ renpy.pause(1)

    window show
    "Ненадолго задумавшись, я полез в карман за картой..."
    window hide

    $ renpy.pause(1)
    play sound nds_list['nd_map_open']
    $ renpy.pause(1)
    jump podpishite_my_peticiu

label muzclub_begun_d2:
    $ disable_current_zone()
    $ necessary_musclub += 1
    $ necessary_map += 1

    stop music fadeout 2

    window show
    "Итак, у нас на очереди - музыкальный кружок.{w} Посижу у этой миловидной Японки.{w} Все равно торопиться мне некуда."
    "Если, конечно, она меня до смерти не заговорит, как в нашу прошлую встречу."
    "Да даже если и заговорит, зато на гитаре играть умеет. И это хорошо."
    window hide

    $ renpy.pause(1)
    scene bg ext_musclub_day with dissolve2
    
    window show
    "Меня встречало вчерашнее красивое здание.{w} Глаза напрягала лишь пожелтевшая белая краска.{w} Надеюсь, кто-нибудь когда-нибудь покрасит её в естественный белый цвет."
    window hide

    $ renpy.pause(1)
    scene bg ext_music_club_verandah_day with dissolve
    
    window show
    "Я неспешно поднялся на веранду и постучал в дверь."
    window hide

    $ renpy.pause(1)
    play sound sfx_knocking_door_2 
    $ renpy.pause(1)

    window show
    voice "Войдите!"
    window hide

    play sound sfx_open_door_clubs
    scene bg int_musclub_day with dissolve
    play ambience ambience_music_club_day fadein 2
    play music music_list["your_bright_side"] fadein 2
    play sound sfx_close_door_1
    $ renpy.pause(1)
    show mi smile pioneer far with dspr

    window show
    "Зайдя в здание, меня встречала Маша с улыбкой на лице."
    mi "Привет, Илья. Ты пришел на гитаре поиграть? А может музыку послушать?"
    nd_il "Да нет.{w} В смысле не только.{w} Я ещё за подписью."
    "Сказал я и протянул бегунок Маше."
    window hide

    $ renpy.pause(1)
    hide mi with dspr
    $ renpy.pause(1)
    
    window show
    "Она взяла ручку и, начиркав свою японскую роспись, протянула листок мне."
    nd_il "Спасибо."
    "Сказал я и взял бегунок."

    show mi smile pioneer far with dspr

    mi "Не за что. Кстати, хочешь я тебе сыграю на чём-нибудь? Я вот мелодии новые выучила недавно. Хочешь послушать?"
    nd_il "А на каком инструменте?"
    mi "На любом. Вот гитара. Видишь её? Сейчас..."

    "Протараторила Маша, взяла гитару и села на скамейку."
    "Я же сел рядом с ней и замер в ожидании концерта..."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    $ renpy.pause(3, hard=True)
    play music ndm_list['looking_for_the_miracle'] fadein 2 
    show cg d4_mi_guitar with dissolve2
    $ renpy.pause(3)

    window show
    "Первые звуки струн незамедлительно прорвались ко мне в мозг и растеклись внутри него, вызвав приятную дрожь."
    "Мику играла без единой запинки, идеально дергая струны и вовремя ставя аккорды.{w} Я ловил наслаждение от этой спокойной и убаюкивающей мелодии."
    "Каждая тронутая ею струна доставляла мне невиданное ранее удовольствие."
    window hide

    show blink

    $ renpy.pause(2, hard=True)

    $ volume (0.3, "ambience")
    play ambience nda_list['ambience_english_caffe'] fadein 5

    $ renpy.pause(1, hard=True)

    show prologue_dream with dissolve

    window show
    "Закрыв глаза, я представил кофейню, аккуратные столики из темного дерева, а слева вид на бескрайнее море."
    "Всё, о чем я мечтал было тут - ароматный чай на моём столе, запах настоящего моря..."
    "Отдых от суеты большого города, перемещение в маленький город на побережье."
    "Да, всё это время мне хотелось одного - отдыха.{w} И вот он."
    "Просто фантастика..."
    window hide

    $ renpy.pause(3, hard=True)
    stop ambience fadeout 4
    stop music fadeout 4
    
    hide prologue_dream with dissolve

    $ renpy.pause(2)
    $ volume (1.0, "ambience")
    play ambience ambience_music_club_day fadein 5
    
    window show
    mi "Илья, ты что, уснул?"
    window hide

    $ renpy.pause(1)
    play music music_list["your_bright_side"] fadein 4
    scene bg int_musclub_day
    show mi surprise pioneer far
    show unblink
    $ renpy.pause(1)

    window show
    nd_il "Это было великолепно. Я как будто был на острове."
    show mi smile pioneer at center with dspr
    th "Это просто восхитительно, у Маши получилось отправить меня в путешествие в другой конец света.{w} Либо я, действительно, просто уснул..."
    mi "Да? Спасибо большое. Я старалась. Кстати, не хочешь записаться в мой клуб? Я и Алиса сможем научить тебя играть на чём угодно!"
    th "А может мне записаться? С одной стороны я ничего не теряю, лишь попытавшись."
    window hide
    
    menu:

        "Записаться на кружок":
            $ nd_mirr += 1
            $ dvrr += 1
            $ music_kr_dv = True

            window show
            nd_il "Да, пожалуй, запиши меня."
            mi "Вот и отлично. Дай, пожалуйста, свой бегунок."
            
            hide mi with dspr

            "Я протянул Маше бегунок, и она поставила в нижнем поле свою роспись."
            window hide

            $ renpy.pause(2)

            show mi smile pioneer at center with dspr

            window show
            mi "Вот, пожалуйста, держи."
            "Маша отдала мне бегунок обратно."
            show mi normal pioneer at center with dspr
            mi "Теперь распишись вот тут…"
            hide mi with dspr
            "Японка пододвинула ко мне папку, напоминавшую по своему содержанию журнал росписей, и указала пальцем на соответствующее место в нём."
            "Я подобрал привязанную к журналу ручку с одной из страниц, и моя рука автоматом вывела роспись своего владельца."
            "Не знаю, как я мог её помнить. Последний раз подписывал документы наверное года два назад."
            window hide

            $ renpy.pause(1, hard=True)

            show mi smile pioneer at center with dspr

            window show
            mi "У тебя красивая роспись…"
            "Мне стало безумно приятно от её слов, хотя и понимал, что всегда можно лучше."
            "Такой у меня характер. Хочется совершенствовать всё, что делаешь, начиная с распорядка дня, заканчивая такой мелкой вещицей, как роспись в каком-то документе"
            nd_il "Благодарю."
            "Я театрально поклонился девушке."
            show mi happy pioneer at center with dspr
            "Она, в свою очередь, мило улыбнулась мне."
            mi "Большое спасибо, что записался. Нет, честно-честно. Я очень рада."
            nd_il "Я тоже рад, но мне нужно идти."
            nd_il "Обходной сам себя, к сожалению, не подпишет."
            show mi smile pioneer at center with dspr
            mi "Хорошо. Заходи в любое время. Всегда рада тебя тут видеть!"
            window hide
            
            stop ambience fadeout 3
            jump muzclub_begun_d2_2

        "Не записываться":
            
            window show
            nd_il "Я подумаю."
            mi "Ну ладно. Только как надумаешь, обязательно приходи. Я всегда тут. А ещё, если тебе пригодятся какие-нибудь музыкальные инструменты..."
            window hide

            stop ambience fadeout 3
            jump muzclub_begun_d2_2
            
label muzclub_begun_d2_2:
    
    stop music fadeout 3
    show black with dissolve
    play sound sfx_open_door_clubs
    $ renpy.pause(0.5)
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_musclub_day with dissolve2
    play sound sfx_close_door_1
    
    window show
    "Маша что-то торопливо прокричала за дверью, но я уже был на улице."
    window hide

    $ renpy.pause(1)
    
    scene bg ext_houses_day with dissolve2
    
    if dvrr >= 2:
        jump mi_dv_mus
    if usrr >= 1:
        jump mi_mus_us
    else:    
        jump mi_mus_nir
        
        
label mi_dv_mus:

    window show
    th "Интересно, может Алиса научит меня так-же?"
    th "Хотелось бы, конечно, но сначала её найти нужно."
    th "А пока что, единственный мой путеводитель - это карта и бегунок."
    window hide

    $ renpy.pause(1)
    play sound nds_list['nd_map_open']
    $ renpy.pause(0.5)

    window show
    th "Что там у нас дальше?"
    window hide

    jump podpishite_my_peticiu    

label mi_mus_us:
    
    window show
    th "Интересно, может Ульяна тоже умеет играть на каком-нибудь музыкальном инструменте?"
    th "На ударных, например.{w} А если не умеет, было бы прикольно её научить..."
    window hide

    $ renpy.pause(1)
    play sound nds_list['nd_map_open']
    $ renpy.pause(0.5)
    
    window show
    th "Что там у нас дальше?"
    window hide

    jump podpishite_my_peticiu    

label mi_mus_nir:

    window show
    "Интересно, долго Маша училась этому?"
    window hide

    $ renpy.pause(1)
    play sound nds_list['nd_map_open']
    $ renpy.pause(0.5)
    
    window show
    th "Что там у нас дальше?"
    window show

    jump podpishite_my_peticiu
    
label aidpost_d2_begun:

    $ necessary_aidpost += 1    
    $ disable_current_zone()
    $ necessary_map += 1
    stop music fadeout 2
    $ renpy.pause(1)
    
    
    window show
    "Так, медпункт.{w} Интересно, меня будут там проверять?{w} Надеюсь, медсестра тут добрая и она меня отпустит без всех этих проверок на здоровье."
    "Тем более, у меня боязнь этих всяких врачей."    
    window hide

    $ renpy.pause(2)
    scene bg ext_aidpost_day with dissolve2
    
    window show
    "Спустя пару минут показался медпункт." 
    "Его стены были деревянными.{w} Само же здание выглядело довольно миниатюрно."
    "В глаза также бросался флаг с красным крестом, плавно развивающийся на ветру.{w} Он находился на самой крыше медпункта, так что его можно было увидеть даже за деревьями."
    th "Ну а что, прикольно сделано. Добротно."
    window hide

    $ renpy.pause(2)
    

    play sound sfx_knocking_door_2

    window show
    "Подойдя к двери, я постучал в неё и поспешил войти внутрь."
    window hide

    show black with dissolve
    play sound sfx_medpunkt_door_open 
    hide black
    scene bg int_aidpost_day
    with dissolve2
    
    window show
    "Меня встречала медсестра, сидевшая за столом, и пишущая что-то."
    show cs normal far at center with dspr
    "На стене рядом со столом, где сидела медсестра, висел плакат с буквами.{w} Также в медпункте было две кровати, одна в углу, другая у окна."
    "Слева от второй кровати стоял шкаф с прозрачными дверцами, через которые было видно всякие препараты, мензурки, ампулы и тому подобное."
    nd_il "Здравствуйте, мне бы…"
    csp "Здравствуй, пионер. Ты, наверное, тот самый новенький."
    window hide

    play sound sfx_close_door_1
    play ambience ambience_medstation_inside_day fadein 3
    with vpunch
    play music nds_list['ohhhsh'] fadein 3
    $ renpy.pause(1)
    stop music fadeout 1

    window show
    "Я вздрогнул от внезапности."
    "Под дуновением ветра, дверь за моей спиной резко закрылась."

    cs "Меня Виолетта зовут, но пионеры зовут меня Виолой."
    cs "А тебя Ильёй, если не ошибаюсь."
    nd_il "Да, вы правы. Мне бы бегунок подписать."
    cs "Давай взглянем..."

    hide cs with dspr

    "Сказала медсестра, я подошел к ней и протянул бумажку."
    window hide

    $ renpy.pause(1)
    
    window show
    "Она взяла бегунок и хотела поставить подпись, но на половине этого действия ручка в её руке резко остановилась."
    show cs normal at center with dspr
    cs "На что-нибудь жалуетесь?"
    nd_il "Нет, ни на что не жалуюсь…"
    "Торопливо отговорился я."
    window hide

    hide cs with dspr

    $ renpy.pause(0.5)

    window show
    "Медсестра будто вспомнила про что-то, и начала рыться в бумагах на столе."
    th "Похоже, она ищет какую-нибудь мою медицинскую карточку, или ещё что-то, что будет доказывать правдивость моих слов."
    nd_il "Я проверку в поликлинике проходил перед приездом..."
    window hide

    play sound sfx_medpunkt_door_open
    play ambience ambience_medstation_inside_day fadein 3

    $ renpy.pause(0.5)

    show un normal pioneer far at right with dspr
    
    window show
    "Сказал я,{w} и уже хотел взять свой бегунок с неполной росписью медсестры,{w} как дверь за моей спиной открылась и в медпункт вошла девушка Лена."
    th "Она пришла чтобы меня спасти, да?" 
    un "Виола Сергеевна, вас Ольга Дмитриевна просит подойти к ней."
    vg "Да."

    show cs normal far at left with dspr

    cs "Передай Ольге Дмитриевне, что я сейчас приду."
    window hide

    hide cs with dspr

    $ renpy.pause(0.5)

    window show
    "Сказала Виола, дорисовав роспись на бегунке, поправила свой медицинский халат и спешно вышла из медпункта."
    window hide

    $ renpy.pause(1)
    show un smile pioneer far at right with dspr
    $ renpy.pause(1)
    hide un with dspr

    window show
    "Лена улыбнулась мне и выбежала вслед за Виолой, не закрыв за собой дверь."
    window hide

    stop ambience fadeout 3
    scene black with dissolve
    $ renpy.pause(1)

    scene bg ext_aidpost_day with dissolve2
    play ambience ambience_camp_center_day fadein 3 
    play sound sfx_close_door_1
    
    $ renpy.pause(1)
    scene black with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve
    
    window show
    th "Вот это мне повезло. Хорошо, что Лена появилась в медпункте так вовремя и так кстати. Иначе бы Виола меня не скоро отпустила."
    th "Хотя, может я и ошибаюсь, но всё указывало именно на это."
    window hide

    $ renpy.pause(1)

    window show
    th "А сейчас нужно разобраться с вопросом о том, куда мне дальше идти. Так..."
    window hide

    play sound nds_list['nd_map_open']
    $ renpy.pause(1)
    jump podpishite_my_peticiu
    
    
label library_d2_begun_1:
    $ necessary_library += 1
    $ disable_current_zone()
    $ necessary_map += 1
    stop music fadeout 2

    $ renpy.pause(1)

    scene bg ext_library_day with dissolve2

    window show
    "Ходьба до этого здания не заняла у меня слишком много времени."
    "Снаружи стены библиотеки были сделаны из дерева, как и большинство зданий в лагере."
    "Отличительной особенностью библиотеки были окна.{w} А точнее их количество.{w} Три с правой стороны от двери, и три на боковой стороне здания."
    "Итого - шесть.{w} Но было неисключено, что окна есть ещё и на тыльной стороне здания."
    "Просить повернуться библиотеку к лесу задом я не стал. Мне это было не за чем."
    window hide

    $ renpy.pause(1)

    play sound sfx_knocking_door_2

    window show
    "Я подошёл к двери и постучал, но никто и не собирался мне отвечать."
    window hide

    $ renpy.pause (1)
    show black with dissolve
    play sound sfx_open_door_1

    scene bg int_library_day with dissolve
    $ renpy.pause(1)
    show cg d2_micu_lib with dissolve

    window show
    "Приоткрыв её, я увидел спящую библиотекаршу."
    th "Видимо, не выспалась с утра.{w} Ну да ладно, пускай пока спит."
    window hide

    show black with dissolve
    stop ambience fadeout 3
    play ambience ambience_library_day fadein 3
    play sound sfx_close_door_1
    scene bg int_library_day with dissolve
    stop music fadeout 2

    window show
    "Я зашел внутрь, и принялся тихо ходить вокруг между рядами и осматривать библиотеку изнутри."
    "Касаемо обстановки мебели сказать я ничего не мог.{w} Пол на удивление не скрипел, хоть и был сделан из отёсанного дерева."
    "Он блестел, значит, его покрыли лаком или ещё чем-то защищающим..."
    "Погодите... Это не дерево, а лишь самый обычный ламинат."
    "Но фиг с этим полом. Это ведь советская библиотека..."
    window hide

    $ renpy.pause(2)
    
    window show
    "Кучи различных книг красовались на полках книжных шкафов."
    "И каждая такая полка с книгами была подписана согласно их жанрам. Тут и \"Романтика\", и \"История\", и даже \"Фантастика\"."
    window hide

    $ renpy.pause(1)
    
    window show
    "Как уже понятно, я решил подождать пока библиотекарша проснется, и скоротать это время за чтением книг." 
    "Я закрыл глаза, прошёлся указательным пальцам по книжным рядам, и остановившись на одной книге, вынул её из стопки."
    "Она была в обложке, из-за чего было непонятно, что меня в ней ждёт.{w} А полка, с которой я взял эту загадочную книгу, не имела жанровой пометки, в отличие от других."
    th "Может, это полка с книгами, содержание которых уже не актуально?"
    th "Пожалуй, я могу узнать об этом только одним способом..."
    "Я открыл эту самую загадочную книгу на случайной странице, и прочитал первое, что мне попалось на глаза."
    window hide

    $ set_mode_nvl()
    
    window show
    "ГЛАВА ПЕРВАЯ"
    "Ну вот, перед вами Винни-Пух."
    window hide
    
    $ set_mode_adv()

    window show
    th "О, так это же \"Винни-Пух\"! Вариант с неактуальностью пропадает сам собой."
    window hide
    
    nvl clear
    
    $ set_mode_nvl()
    
    window show
    "…Вот однажды, гуляя по лесу, Пух вышел на полянку. На полянке рос высокий-превысокий дуб, а на самой верхушке этого дуба кто-то громко жужжал: жжжжжжж…"
    "Винни-Пух сел на траву под деревом, обхватил голову лапами и стал думать."
    "Сначала он подумал так: \"Это — жжжжжж — неспроста! Зря никто жужжать не станет. Само дерево жужжать не может. Значит, тут кто-то жужжит. А зачем тебе жужжать, если ты — не пчела? По-моему, так!"
    "Потом он еще подумал-подумал и сказал про себя: \"А зачем на свете пчелы? Для того, чтобы делать мед! По-моему, так!"
    "Тут он поднялся и сказал:"
    "— А зачем на свете мед? Для того, чтобы я его ел! По-моему, так, а не иначе!"
    "И с этими словами он полез на дерево…"
    window hide

    $ set_mode_adv()

    if dv_leave_d1 == True:
        jump library_d2_begun_2_nodv
   
    if dv_flag_morning_d1 == True:
        jump library_d2_begun_2_nodv

    if us_candy_steal == True:
        jump library_d2_begun_2_us
    
    else:
        jump library_d2_begun_2_us


label library_d2_begun_2_us:    
    
    play sound sfx_knocking_door_2

    window show
    "Не прошло и пяти минут, как в дверь кто-то постучал.{w} Я встал из-за стола и открыл дверь."
    play sound sfx_open_door_1
    show dv normal pioneer2 with dspr
    "На пороге стояла Алиса и держала в руках какой-то роман."
    nd_il "Тихо, библиотекарша спит."
    "Сказал я шепотом и прислонил указательный палец к губам." 
    hide dv with dspr
    "Алиса кивнула и, зайдя в библиотеку, положила книгу к библиотекарше на стол."
    show dv grin pioneer2 with dspr
    dv "А ты чего читаешь?"
    th "Чёрт, какой жанр у \"Винни-Пуха?"
    nd_il "Фантастику какую-то."
    hide dv with dspr

    "Мы разговаривали шепотом, чтобы не разбудить библиотекаршу."

    show dv guilty pioneer2 with dspr

    dv "Понятно. А ты Ульяну не видел сегодня?"
    nd_il "Нет, я думал, ты знаешь, где она."
    dv "Странно всё это. Вчера вечером у столовой вообще какая-то чертовщина со мной произошла."
    nd_il "Расскажи."
    "Сказал я заинтересованно."
    show dv normal pioneer2 with dspr
    dv "Так вот, я шла на танцы мимо столовой, потом меня позвал какой-то человек в маске, дал три заколки, и сказал мне взломать столовую. Ну, я открыла дверь."
    dv "Потом из-за кустов выбежал еще один поменьше ростом, пробежал в столовую, и залез в буфет.{w} Потом какой-то культ, фонарик, и их как небывало."
    th "Так это же мы с Ульяной. Хех. Алиса, оказывается, мимо проходила…"
    nd_il "Понятно, может это из другого отряда?"
    "Спросил я, еле скрывая свою улыбку."
    show dv guilty pioneer2 with dspr
    dv "Не знаю, но если они что-то сделают с Ульяной.{w} Я за себя не отвечаю."
    dv "А ты видел её сегодня?"
    nd_il "Да, видел, она шла к умывальникам.{w} Видимо для того, чтобы умыться."
    show dv smile pioneer2 with dspr
    dv "Понятно, наверное, она сейчас с младшими отрядами мяч гоняет."
    nd_il "Может быть."
    dv "Кстати, а почему тебе просто не подделать роспись библиотекарши?"
    nd_il "Это идея, но я не умею."
    dv "Тогда давай я сделаю это за тебя?"
    window hide

    $ renpy.pause (1, hard=True)

    menu:

        "Попросить Алису":

            $ persistent.nd_moral_points -= 1
            $ fake_z_54 = True

            window show
            nd_il "Почему бы и нет."
            dv "Тогда давай сюда."

            hide dv with dspr

            "Сказала Алиса, выдернула у меня из рук бегунок, и взяв со стола библиотекарши ручку, легким движением руки поставила роспись."
            window hide

            $ renpy.pause (1, hard=True)

            show dv grin pioneer at center with dspr
            
            window show
            dv "Я эту роспись Женину уже всю выучила.{w} Всем новеньким помогаю её в этой библиотеке получить."
            nd_il "Так её Женей зовут?"
            dv "Да. А ты что, забыл?"
            nd_il "Я и не знал..."
            show dv smile pioneer at center with dspr
            dv "Ну ладно, у меня дела.{w} Так что бывай."
            dv "Если что, то меня тут не было, а роспись ты сам подделал."
            nd_il "Конечно, до встречи."
            window hide



        "Отказаться":
            $ persistent.nd_moral_points += 1
            $ fake_z_54 = False
            
            window show
            nd_il "Знаешь, я наверное лучше её разбужу."
            hide dv with dspr
            show dv grin pioneer far at center with dspr
            dv "Ну ладно, бывай тогда."
            dv "Если что, то меня тут не было."
            th "С чего бы это?"
            nd_il "Ладно, до встречи."
            window hide


    hide dv with dspr

    $ renpy.pause(1)
    play sound sfx_close_door_1

    window show
    "Через одно мгновение в помещении остался лишь я, многочисленные книги, разложенные на шкафах, и спящая девушка."
    window hide

    $ renpy.pause(2)

    if fake_z_54 == True:
        window show
        th "Ну, в принципе, поскольку подпись библиотекарши у меня есть, можно уходить."
        th "Надеюсь подделку никто не распознает."
        "С этими мыслями я отправился на выход из библиотеки."
        window hide

        stop ambience fadeout 3
        show black with dissolve
        play sound sfx_open_door_1
        $ renpy.pause(0.5)
        play ambience ambience_camp_center_day fadein 3
        scene bg ext_library_day with dissolve
        play sound sfx_close_door_1

        $ renpy.pause(1)

        play sound nds_list['nd_map_open']

        window show
        "Что там у нас следующее?"
        window hide

        jump podpishite_my_peticiu

    else:
        jump library_d2_begun_2_nodv

label library_d2_begun_2_nodv:
    
    $ renpy.pause(2)

    window show
    "Я неспешно бросил свой взгляд на библиотекаршу."
    th "Конечно, здоровый сон это хорошо, но не в рабочую же смену."
    th "Хотя если считать, что пионерам не платят за это, какая же это работа."
    th "Даже жалко как-то будить эту девушку.{w} Не знаю даже почему."


    "Я подошел к девушке и попытался её разбудить."
    window hide

    $ renpy.pause(1)

    window show
    mzp "А? Кто это?"
    "Сквозь сон промямлила библиотекарша."
    nd_il "Доброе утро, я новенький, меня Ильёй зовут."
    
    show mz bukal glasses pioneer far with dspr

    "Соня открыла глаза и, протерев очки, посмотрела на меня."

    mz "А, это ты. Меня Евгения зовут, можно просто Женя. Ну, зачем пришел?"
    nd_il "Мне бы бегунок подписать."
    "Сказал я, и достав бумажку из кармана, протянул её Жене."
    "Она поправила очки, взяла ручку, и поставив свою роспись, отдала бегунок мне."
    show mz angry glasses pioneer far with dspr
    mz "Свободен."
    th "Как-то грубо к человеку, который тебе ничего плохого не сделал.{w} Ну и ладно."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(0.5)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_library_day with dissolve
    play sound sfx_close_door_1

    window show
    "Я пожал плечами и молча вышел на улицу."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ты посмотри какая важная. Спит на рабочем месте, и у неё кто-то ещё и виноват."
    window hide

    $ renpy.pause(1)
    play sound nds_list['nd_map_open']

    window show
    "Что там у нас следующее?"
    window hide

    jump podpishite_my_peticiu
    


label d2_begun_end_1:

    play music music_list["your_bright_side"] fadein 2

    window show
    th "О! С бегунком покончено.{w} Теперь к вожатой. Но сначала нужно проверить спортплощадку. Хочется посмотреть, как Ульяна в футбол играет."

    if us_candy_steal == True:
        th "Заодно проверю на правдоподобность ту информацию о её выигрышах в сухую..."

    window hide
    
    $ renpy.pause(1)
    stop ambience fadeout 3
    show black with dissolve2 
    $ renpy.pause(2)
    scene bg ext_playground_day with dissolve2
    stop music fadeout 2
    stop ambience fadeout 2
    
    window show
    "Странно но, придя на футбольное поле, я никого не обнаружил." 
    "Ни младших отрядов, ни Ульяны — никого." 
    "Было бесшумно, даже птицы замолчали, что странно для летнего лагеря."
    window hide

    $ renpy.pause(1)
    play sound sfx_inhale 
    $ renpy.pause(1)
    
    window show
    th "Если её нет даже на футбольной площадке, тогда где она может быть?"
    window hide

    with vpunch 
    stop music fadeout 3
    
    window show
    "Сзади кто-то хлопнул меня по плечу."    
    muz "Привет, пионер. Скучаешь?"
    
    show ba normal at center with dspr
    
    "Я повернулся, и увидел светлокожего мужчину тяжёлого телосложения."
    nd_il "Здравствуйте, Меня Ильёй зовут. Я новый пионер в лагере."
    muz "А меня Евгением Петровичем. Я веду кружок футбола в этом лагере. Будем знакомы."
    hide ba normal with dspr
    "Он протянул мне свою огромную руку, и я максимально мужественно пожал её."
    th "Интересно, почему кружка футбола нет в списке?"
    "Подумал я, доставая бегунок из кармана, и повернув его обратной стороной, увидел место для еще одной подписи."
    nd_il "А я пришел за подписью."
    "Сказал я и отдал Петровичу бегунок."
    $ renpy.pause(1)
    show ba normal at center with dspr
    fiz "Пойдем в спортзал за ручкой."
    "Сказал физрук, и мы отправились в здание..."
    window hide
    
    show black with dissolve2
    $ renpy.pause(2)
    play sound sfx_open_door_clubs
    play ambience ambience_int_cabin_day fadein 3
    play sound sfx_close_door_1
    $ renpy.pause(1)
    scene bg sporthall with dissolve 
    $ renpy.pause(1)    
    show ba normal with dspr
    
    window show
    fiz "Записываться будешь?"
    "Спросил меня Евгений Петрович."
    th "Если так подумать, то что я теряю, записавшись на что-нибудь?{w} Ничего.{w} А приобретаю{w} — возможность играть в футбол когда угодно.{w} Не то чтобы я до этого не мог играть когда угодно…"
    window hide

    menu:
        "Записаться на футбол":
            
            $ usrr += 1
            $ sport_kr_us = True
            window show
            nd_il "Да, на футбол."
            if music_kr_dv == True:
                $ nir += 1

                fiz "Но ты же уже на музыку записан."
                nd_il "А, точно."
                fiz "Ничего страшного.{w} Всестороннее развитие ещё никому не мешало."
                nd_il "Пожалуй, вы правы."
                if config.developer == False:
                    if persistent.running_with_sugar_ach == False:
                        $ persistent.running_with_sugar_ach = True
                        $ notdream_achievment("running_with_sugar_ach")
                        $ persistent.nd_moral_points += 3
                

            fiz "Тогда всё готово, забирай."
            "Евгений Петрович протянул мне бегунок."
            nd_il "Спасибо."
            fiz "Не торопись. Тебе ещё кое-где нужно расписаться."
            
            hide ba normal with dspr

            "Сказал физрук, и взяв со стола журнал с ручкой, подошёл и отдал всё это дело мне."
            
            show ba normal with dspr
            
            fiz "Распишись напротив своего имени."
            nd_il "Понял."
            
            hide ba normal with dspr

            "Сказал я, вывел свою роспись в специальном месте для росписей, а затем отдал журнал обратно Евгению Петровичу."
            window hide

            $ renpy.pause(1)

            window show
            nd_il "А вы Ульяну видели сегодня?"
            
            show ba normal with dspr

            fiz "Нет, она обычно утром в футбол поиграть любит, но сегодня ее не было."
            nd_il "Ладно, спасибо."
            fiz "Не за что."
            
            hide ba normal with dspr

            "После этого я сразу же направился к Ольге Дмитриевне за её новым \"спецзаданием\"."
            window hide

            hide running_with_sugar_ach
        
        "Не записываться":
            
            window show
            nd_il "Я подумаю."
            fiz "Тебя никто не заставляет. Если решишь все-таки записаться - приходи."
            fiz "Я всегда здесь."
            nd_il "Хорошо, спасибо."
            hide ba normal with dspr
            "Сказал я, положил листок в карман, и сразу же направился к Ольге Дмитриевне за её новым \"спецзаданием\"."
            window hide
    
    
    $ renpy.pause(1)
    show black with dissolve
    stop ambience fadeout 2
    $ renpy.pause(2)
    jump d2_begun_end_2
    
label d2_begun_end_2:
    
    $ renpy.pause(1)

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve2
    
    window show
    "Пока я ходил по всем кружкам, я, кажется, запомнил весь лагерь, и мог ориентироваться без помощи карты.{w} Но на всякий случай было принято решение её оставить."
    window hide

    scene bg ext_houses_day with dissolve
    $ renpy.pause(2)
    scene bg ext_house_of_mt_day with dissolve
    
    window show
    "Дойдя до домика Ольги Дмитриевны, я увидел её, сидевшую под деревом на раскладном стуле и читающую какую-то книжку."
    th "Ну а чем же ей ещё заниматься?"
    nd_il "Ольга Дмитриевна, я собрал все подписи."

    show mt normal pioneer far at center with dspr
    
    "Я подошёл к вожатой и протянул ей бегунок со всеми подписями со всех кружков."
    "Ольга Дмитриевна опустила книгу, осмотрела бегунок, и сунула его в себе карман."
    th "Серьезно? Она его даже не проверила?"
    mt "Молодец. Через несколько минут обед. А после обеда я дам тебе новое задание."
    "Сказала Ольга Дмитриевна и снова окунулась в чтение книги."
    "После такого внезапного оборота событий мне ничего больше не оставалось делать, кроме как идти к скамейкам на площади."
    window hide

    show black with dissolve
    $ renpy.pause(2)
    scene bg ext_houses_day with dissolve   
    play music music_list["raindrops"] fadein 2 
    
    window show
    th "Как же я люблю работать, но ничего не поделаешь…"
    vg "Устал, бедняга слушать, как Маша на гитаре брынчит."
    th "Она действительно неплохо играет."
    vg "А я спорю что ли?"
    th "Слава богу, не споришь."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    $ renpy.pause(3)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve2

    window show
    "Дойдя до площади, я сел на скамейку, и начал рассматривать окрестности, а так же слушать пение птиц."
    th "Как же я так... Мог даже подписи подделать, а сэкономленное время потратить в свои блага..."
    window hide

    $ renpy.pause(1)

    window show
    "Ничего примечательного на площади кроме памятника не было,{w} поэтому я разглядывал именно его, в надежде вспомнить хоть что-нибудь про этого государственного деятеля из учебников по истории."
    window hide

    $ renpy.pause(3, hard=True)

    window show

    th "Блин. Почему я не узнаю человека на этом памятнике?"
    th "Я ведь по Истории четыре в школе имел. А тут..."
    "Я сверлил памятник и лицо этого Генды взглядом, пока не..."
    th "Господи, это же Гэндо Икари из Евангелиона."
    vg "Илья, ну ты совсем дурачок? Откуда в СССР взялся персонаж из аниме?"
    th "Ну, похож ведь."
    window hide

    $ renpy.pause(1)
    
    window show
    "Помимо памятника площадь была окружена деревьями, как и весь лагерь.{w} А по небу плыли белые и пушистые облака."
    th "Интересно, в какой части России находится этот лагерь?"
    window hide

    $ renpy.pause(1)

    window show
    "На этот вопрос мне вполне могла ответить пионерка Лена, которая проходила мимо и читала книгу."
    nd_il "Лена!"
    
    show un surprise pioneer far at center with dspr
    
    "Девушка обратила на меня внимание и подошла."
    window hide

    hide un with dspr
    $ renpy.pause(1)
    show un smile pioneer at center with dspr
    
    window show
    un "Ты чего-то хотел?"
    nd_il "Да.{w} Ты случайно не знаешь, какие населенные пункты есть рядом с лагерем?"
    un "Нет, не задумывалась об этом, я вообще приехала сюда издалека."
    nd_il "А откуда?"
    un "Из Ленинграда."
    th "С Санкт-Петербурга.{w} Значит, этот лагерь находится не на севере.{w} Оно и понятно, лето тут до необыкновения теплое."
    nd_il "А где примерно этот лагерь находится?"
    un "На Кавказе.{w} А ты что, тоже издалека?"
    th "Круг сузился."
    nd_il "Да нет, я тоже на Кавказе живу, просто всю дорогу спал."
    un "Понятно, а что ты тут сидишь один? Сейчас обед будет..."

    hide un with dspr
    
    play sound sfx_dinner_horn_processed
    
    "Не успела Лена договорить это предложение, как из динамика послышался гудок, и из неоткуда взявшиеся пионеры, все как один направились в столовую." 
    "Мне ничего не оставалось, как идти туда вместе со всеми."
    
    if dv_flag_morning_d1 == True:
        window show
        th "Надеюсь, я не потеряю эту толпу и не заблужусь..."

    window hide
    show black with dissolve
    stop music fadeout 2
    
label silent_stranger:
    
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with dissolve2
    
    window show
    "По приходу в столовую я взял свою порцию и оглянулся.{w} Единственным свободным местом в этой столовой был стол, стоявший в самом углу столовой." 
    "За этим столом сидел какой-то пионер, опустив голову вниз."
    window hide

    $ renpy.pause(2)
    
    window show
    nd_il "Можно сесть?"
    "Он согласно кивнул, и я сел за стол."
    window hide

    $ renpy.pause(2)
    
    window show
    "В тарелке у меня были макароны и отварная курица.{w} Кто бы что ни говорил, но на обед здесь подают что-то восхитительное."
    window hide

    $ renpy.pause(1)
    show tl_1_pioneer with dspr
    $ renpy.pause(1)

    window show
    pi "Почему ты сел именно сюда?"
    "Произнес пионер низким тоном."
    window hide

    $ renpy.pause(1)

    window show
    "Он был одет в пионерскую форму, но на вид ему было лет 40.{w} Помимо этого он был лысым, только седые волосы по бокам украшали его голову.{w} Или скорее служили дополнением к такому виду."
    nd_il "Других мест нет, все заняты."
    "Он промолчал, будто не услышал меня, или просто проигнорировал."
    th "Какой-то он неразговорчивый.{w} Может у него что-то случилось? В любом случае, это не моё дело."
    hide tl_1_pioneer with dspr
    "Я принялся за еду. А этот пионер все также смотрел в стол, не обращая ни на кого внимания."
    "В столовой было довольно шумно, огромное количество пионеров спешили куда-то, а я просто, неторопливо ел."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Вскоре, закончив с приемом пищи, я встал из-за стола, и уже хотел попрощаться с неизвестным пионером, но оглянувшись понял, что он уже давно ушел."
    th "А я ведь у него даже имени не спросил.{w} Пусть его будут звать \"Талян\"."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    $ renpy.pause(1)
    play sound sfx_open_door_clubs

    window show
    "Придумав обалденное имя неизвестному пионеру и отнеся свои тарелки, я отправился к моей \"любимой\" вожатой за планом работы." 
    window hide

    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_dining_hall_near_day with dissolve
    play sound sfx_close_door_1

    window show
    "Но далеко идти не пришлось — она ждала меня у входа в столовую."
    "С ней была еще одна девушка — Лена. Видимо, она была моим товарищем по несчастью."
    
    
    
 
label painting_business:
 
    mt "А вот и Илья."
    window hide

    $ renpy.pause(1)
    show mt normal pioneer far at center
    show un normal pioneer far at right 
    with dspr
    
    window show
    "Я подошел к ним, и Ольга Дмитриевна начала объяснять план работы."
    mt "Итак, сейчас вы будете красить здание музыкального кружка…"
    th "Ну хоть не административный корпус, и на том спасибо."
    th "Хотя,{w} если бы мне доверили красить административный корпус...{w} Это какое огромное полотно для моего творчества..."
    window hide

    $ renpy.pause(2)

    window show
    mt "…всё поняли?"
    th "Я опять все прослушал?"
    nd_il "Повторите, пожалуйста, сначала."
    mt "Лена тебе все по дороге объяснит."
    "Сказала Ольга Дмитриевна, и мы с Леной отправились куда-то."
    window hide

    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve
    
    window show
    nd_il "Лена, а куда мы идем?"
    un "На склад, возьмем краску, инструменты, и пойдем к музыкальному кружку."
    window hide

    $ renpy.pause(1)
    scene bg sklad with dissolve
    $ renpy.pause(1)

    $ renpy.pause(1)
    play sound sfx_keys_rattle
    $ renpy.pause(1)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1)
    play sound sfx_open_door_1
    $ renpy.pause(1)
    $ volume (0.4, "ambience")   
    scene bg int_clubs_male2_night with dissolve
    play sound nds_list['saray_door2']

    window show
    "Дойдя до места, Лена открыла склад ключами, которые ей, по-видимому, дала Ольга Дмитриевна, и мы вошли в помещение."
    th "А вот тут мы с Ульяной коробку уронили..."
    vg "И упали вместе на пол. Вот это воспоминание. Будешь всю жизнь помнить и думать — \"Эх, молодость…\""
    
    show un normal pioneer far at center with dspr
    
    "Мы с Леной начали искать краску по всему помещению."
    "Она лежала на верхней полке шкафа вместе с валиками. Я встал на стул и достал все малярные принадлежности."
    "Вдруг я заметил вчерашнюю коробку. Она злобно смотрела на меня, а я на неё."
    th "Мы еще встретимся…"
    "Подумал я и спустился со стула."
    "Затем я взял стремянку и положил её на плечо."
    th "Упаковался так упаковался."
    nd_il "Готово, теперь пошли к музклубу?"
    
    show un smile pioneer far at center with dspr
    
    "Та в свою очередь положительно кивнула, и мы отправились на выход из склада."
    window hide

    show black with dissolve2
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ renpy.pause(1)
    scene bg sklad with dissolve2
    play sound sfx_close_door_1
    $ volume (1.0, "ambience")
    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1)
    play sound sfx_keys_rattle
    $ renpy.pause(1)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1)

    window show
    "Мы вышли со склада, закрыли его, и понесли краску к музыкальному клубу, который казался достаточно далеким, учитывая груз на моих руках."
    window hide

    scene bg ext_houses_day with dissolve2
    
    $ renpy.pause(1)

    window show
    "Вскоре руки стали активно уставать, и я пытался перекладывать всё с одной руки на другую."
    "Но это тоже не шибко помогало."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)

    window show
    th "Нагрузили..."
    vg "Бедняга.{w} Давай неси.{w} Пролетарий."
    th "Ну спасибо."
    window hide

    $ renpy.pause(1)
    scene bg ext_musclub_day with dissolve2

    window show
    "С горем пополам, мы добрались до музыкального кружка."
    "Я поставил стремянку у стены, положил на неё валики и облокотился на рядом стоящее дерево."
    $ renpy.pause(1)
    show un smile pioneer at center with dspr
    un "Устал?"
    nd_il "А.{w} Да..."
    show un grin pioneer at center with dspr
    un "Отдыхай пока тогда."
    hide un with dspr
    "Лена взяла валик, открыла банку с краской, и опустив туда валик, начала красить стену."
    window hide

    $ renpy.pause(1)

    window show
    vg "Смотрите, за него девочка стены красит."
    th "Ты совесть или внутренний голос? Сейчас отдохну и помогу."
    vg "Давай, физкультура ещё никому не мешала."
    window hide

    $ renpy.pause(2)

    window show
    "Немного отдохнув, я тоже присоединился к ней в этом нелёгком деле."
    window hide

    $ renpy.pause(1)
    play music ndm_list['stairway_to_the_ussr'] fadein 4

    window show
    "Мы красили стены и попутно разговаривали на разные темы, начиная от жизни в лагере и заканчивая историями из личной жизни."
    show un normal pioneer at center with dspr
    un "А зачем ты меня сегодня спрашивал про лагерь?"
    nd_il "Просто хочу потом ещё сюда съездить."
    show un smile pioneer at center with dspr
    un "Понравилось отдыхать тут?"
    hide un with dspr
    nd_il "Можно и так сказать..."
    window hide

    show black with dissolve 
    $ renpy.pause(1)
    hide black with dissolve
    
    window show
    "Я заметил, что по началу, она была застенчива, но спустя 20 минут я смог разговорить эту девушку."
    "Я рассказывал ей короткие истории, которые приключились со мной в школе."
    "Как один раз кто-то из учеников проводной телефон из кабинета директора стащил и на дерево закинул,{w} как мы с друзьями первые гроши зарабатывали и все в этом духе."
    "Однако мне удавалось рассказывать только о ярких моментах своей жизни.{w} Остального я просто либо не помнил, либо помнил мало."
    "Но Лена... Я даже был удивлен, что у скромной девушки из лагеря будет такая богатая жизнь..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    scene bg ext_musclub_day with dissolve
    $ renpy.pause(1)
    
    window show
    "При дальнейшем диалоге я узнал, что Лена очень любит читать книги и что она, как и я, первый раз в лагере, и тоже много чего ещё не знает."
    "И поэтому я рассказывал Лене о том, что мне рассказывала мать, и что я больше всего любил слушать вечерами — как выжить в пионерском лагере."
    nd_il "Смотри, что бы к тебе никто не пробрался в домик пока ты спишь, можно поставить над дверью ведро воды, и когда злоумышленник откроет её, он точно больше не потревожит тебя."    
    show un normal pioneer at center with dspr
    un "Поняла, а то есть тут некоторые…"
    nd_il "Ну вот, теперь будешь пользоваться."
    hide un with dspr
    window hide

    $ renpy.pause(1)

    window show
    "Потом я ей начал рассказывать, как нужно вести себя в определенных ситуациях."
    nd_il "...Так вот, если ты встретила медведя в лесу…"
    window hide

    $ renpy.pause(1)

    window show
    "Периодически к нам выходила Маша, и всячески поддерживала наш разговор.{w} Она очень много и быстро говорила, а я даже не успевал вставить своего слова.{w} Впрочем, как обычно."
    window hide
    
    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    stop music fadeout 2
    scene bg ext_musclub_day with dissolve
    $ renpy.pause(1)

    window show
    "Вскоре со зданием было покончено, но я всё равно решил удостовериться, спросив об этом Лену."
    nd_il "Мы закончили?"
    show un smile pioneer at center with dspr
    un "Да. Закончили."
    hide un with dspr
    "Лена победно положила валик рядом с краской.{w} Я сделал тоже самое и повернулся к Маше."
    show mi normal pioneer far at center with dspr
    nd_il "Маша, можешь нам на гитаре что-нибудь ещё сыграть?"
    
    show mi smile pioneer far at center with dspr
    
    mi "Да, сейчас вынесу её, подождите секундочку."
    window hide

    hide mi with dspr
    
    $ renpy.pause(1) 

    window show
    "Мы с Леной сели на траву и принялись ждать." 
    window hide

    $ renpy.pause(3)
    
    window show
    "Спустя полминуты из клуба выбежала Маша с гитарой в руках."
    window hide

    play music ndm_list['sunny_day'] fadein 3
    $ volume (0.3, 'ambience')   
    $ renpy.pause(2)
    
    window show
    "Она села перед нами на траву и начала играть медленную мелодию подобную той, которую я слышал этим утром."
    "Я почувствовал всё тоже самое, что чувствовал во время своего визита в её клуб за росписью."
    "Но это чувство не надоедало."
    "Оно лишь увеличивалось с каждым прикосновением девушки к струнам гитары, будто скорость лодки под дуновением ветра на парус."
    "До этого я не слышал ничего подобного, но моё подсознание говорило мне о каком-то непонятном дежавю."
    window hide

    $ renpy.pause(2)
    show blink

    window show
    th "Богоподобно."
    window hide

    stop ambience fadeout 3
    $ renpy.pause(1)
    
    $ nd_change_time('night')

    $ renpy.pause(1)
    play ambience ambience_camp_center_night fadein 3
    $ volume (1, 'ambience')

    window show
    "Перед глазами показался лес, костер и пионеры. Они сидели на бревнах вокруг костра и беседовали друг с другом." 
    "Оглянувшись, я увидел Ольгу Дмитриевну, Лену и Машу, Алису, Семена беседовавшего со Славей.{w} Подождите.{w} А где Ульяна?" 
    "Где эта девушка, с которой можно хорошо провести время, напугать пионеров у костра или просто поговорить?"
    window hide

    scene bg ext_path2_night with dissolve2
    $ renpy.pause(1)
    play sound_loop sfx_far_steps fadein 1

    window show
    "Я встал с бревна и пошел в глубокую чащу леса, через колючие ветки деревьев, через кусты и овраги..."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_polyana_night with dissolve2 
    
    window show
    "...И вскоре вышел на какую-то обширную поляну."
    window hide
    
    stop music fadeout 3
    stop sound_loop fadeout 1
    
    if us_candy_steal == True:
        window show
        "По середине этой поляны лежали два пустых пакета и маски, которые мы делали вместе на складе."
        window hide

    $ renpy.pause(2)
    
    window show
    nd_il "Ульяна!"
    "Закричал я на весь лес, но ответило лишь только моё эхо."
    "Я чувствовал, что скоро должно случиться что-то плохое."
    nd_il "Уля!"
    
    play sound sfx_hiding_in_bush
    
    "Вдруг куст с густой листвой издал характерный звук."
    nd_il "Ульяна, это ты?"
    "...Но мне никто не ответил.{w} Лишь кошачий хвост показался между стволами деревьев, и исчез в беспроглядной темноте дремучего леса."
    "Или мне просто это показалось?"
    th "Проклятье."
    window hide

    $ renpy.pause(1)

    play sound sfx_hiding_in_bush
    show black with dissolve 
    
    window show
    "Я побежал через эти кусты глубоко в лес, перепрыгивая через всевозможные препятствия, пока не показалась протоптанная тропинка." 
    play sound sfx_hiding_in_bush
    "Бежав по ней, я думал что выйду в лагерь, но я вышел в какое-то другое таинственное место."
    window hide

    $ renpy.pause(1)
    play music ndm_list['moonlit_night'] fadein 3
    scene bg tain_mesto_night with dissolve2
    
    window show
    "Здесь протекало чистое прозрачное озеро."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я остановился, чтобы перевести дух."
    nd_il "Ульяна, я не могу больше бежать."    
    window hide

    $ renpy.pause(1)
    with vpunch
    play sound sfx_bush_body_fall
    show blink
    $ renpy.pause(1)

    window show
    "Я упал,{w} и остался так лежать под стрекотание лесных сверчков..."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    $ renpy.pause(6)
    
    $ nd_change_time('day')

    window show
    mt "Просыпайся!"
    window hide

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_musclub_day
    show mt normal pioneer at center
    show unblink
    
    window show
    "Я открыл глаза и увидел Ольгу Дмитриевну."
    mt "Илья, ты так сильно устал?"
    nd_il "Похоже, что да, Ольга Дмитриевна."
    mt "Ладно. Вы с Леной хорошо поработали, и заслужили отдых."    
    "Вожатая показала рукой на белоснежное здание музыкального кружка."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Зато белая краска теперь действительно белая."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я оглянулся, но ни Лены, ни Маши я не увидел."
    th "Нужно срочно что-то делать."
    mt "Когда отдохнёшь, отнеси все инструменты на склад."
    window hide

    $ renpy.pause(1)
    
    play sound sfx_keys_rattle
    hide mt with dspr
    
    window show
    "Отдав мне ключи, вожатая отправилась в сторону площади."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    
    window show
    "Я потер руки и взял стремянку, краску и валик, и отправился к складу." 
    window hide

    $ renpy.pause(3)
    play sound sfx_open_door_1
    $ renpy.pause(1)
    
    window show
    "Открыв склад и войдя в него я молча положил все инструменты на свои места, а затем отправился на площадь."
    window hide

    play sound sfx_close_door_1
    $ renpy.pause(2)
    scene bg ext_square_day with dissolve2
    
    window show
    "Придя к площади, я сел на скамейку, и окунулся в океан собственных мыслей и размышлений, не дающих мне покоя."
    th "Если Ульяна еще не появилась в лагере, то придется её найти… А тем более тот сон..."
    th "Что он мог значить?"
    th "Он явно приснился мне не просто так."
    window hide

    $ renpy.pause(1)
    show pi2 smile pioneer at left with dspr
    $ renpy.pause(1)
    hide pi2 smile pioneer with dspr
    
    window show
    "Ко мне подошел Семён и сел рядом."
    me "Видок у тебя не важный.{w} Что-то случилось?"
    nd_il "Ничего, просто думаю, где может быть Ульяна."
    me "Волнуешься за неё что ли?"
    nd_il "Разве что чуть-чуть.{w} Просто давно её не видел в лагере."
    window hide

    $ renpy.pause(1)
    
    window show
    "Наступило короткое молчание."
    window hide

    $ renpy.pause(2)
    
    window show
    me "Не беспокойся.{w} Всякое может быть." 
    me "Погуляет и вернётся."
    "Эти рассуждения показались мне логичными и до боли знакомыми."
    nd_il "Наверное…"
    window hide

    $ renpy.pause(1)
    show pi2 smile pioneer at left with dspr
    
    window show
    me "Скоро полдник, не опоздай."

    hide pi2 smile pioneer with dspr

    "Сказав это, Семён пошел по своим делам, оставив меня наедине с мыслями."
    window hide

    $ renpy.pause(1)

    window show
    th "Может и вправду мне не о чем волноваться?{w} Хотя почему я вообще волнуюсь?{w} Как и сказал Семён \"Всякое может быть\"."
    th "А он с виду задорный и совсем не подозрительный."
    th "Раз он пытался меня подбодрить, теперь мы с ним, похоже, друзья."
    window hide

    $ renpy.pause(1)
    play sound sfx_dinner_horn_processed
    $ renpy.pause(2)    
    
    window show
    "В это же мгновение динамик позвал пионеров в столовую. Благо идти до неё было недалеко..."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_dining_hall_away_day with dissolve
    $ renpy.pause(1)
    scene bg ext_dining_hall_near_day with dissolve
    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_clubs
    scene bg int_dining_hall_people_day with dissolve2
    play ambience ambience_dining_hall_full fadein 3   
    
    window show
    "Зайдя в столовую, я увидел нашу вожатую, которая разговаривала с поварами." 
    "Я незаметно для неё взял поднос, и отправился за один из свободных столов."
    window hide

    $ renpy.pause(1)
    
    window show
    "В моей тарелке была запеканка." 
    "Есть это, откровенно говоря, не хотелось, поэтому я ограничил себя сладким чаем."
    th "Вот и первый минус лагерной столовой."
    th "Ну это же даже в школе невозможно было есть."
    window hide

    $ renpy.pause(1)
    show mt normal pioneer at right with dspr
    $ renpy.pause(1)
    hide mt with dspr

    window show
    "Ко мне подошла Ольга Дмитриевна и села рядом со мной.{w} Видимо, другие свободные места кончились..."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Может Ульяна ушла из-за того, что не хочет меня видеть?"
    window hide

    $ renpy.pause(1)
    
    show mt normal pioneer at center with dspr

    window show
    mt "Почему пионер грустит?"
    nd_il "Да я не грущу, просто задумался."
    "Может, я действительно выглядел так, будто грущу,{w} но я так не думал."
    mt "Илья, я твоя вожатая, ты можешь рассказать мне всё, что тебя беспокоит."
    nd_il "Все в порядке Ольга Дмитриевна.{w} Просто настроения нет."
    window hide

    $ renpy.pause(1)
    
    window show
    "Вот что я ещё заметил.{w} Все вокруг почему-то очень волнуются из-за моего настроения и отношения к этому лагерю.{w} Может, конечно, они действительно за меня переживают."
    "Кажется я забыл, что нахожусь в немного другой стране.{w} Логично, что тут будет другой менталитет."

    show mt smile pioneer at right with dspr    
    
    mt "Илья, вы с Леной очень быстро управились с крашением музыкального кружка.{w} И я договорилась с поварами, чтобы они дали вам по мороженному."
    "Видимо она хотела поднять мне настроение.{w} И как я считаю, у неё это успешно получилось."
    nd_il "Спасибо, Оль Дмитриевна."
    
    hide mt with dspr
    
    "Сказал я, встал из-за стола, отнес тарелку с \"запиханкой\" и отправился к поварам, коих можно с гордостью назвать \"предвестниками радости\"."
    window hide

    $ renpy.pause(2)

    window show
    "Как только я подошёл к своеобразному \"столу заказов\", повариха сразу обратила на меня внимание."
    pov "Здравствуй, тебя Илья зовут?"
    nd_il "Да, я."
    pov "Нам сказала ваша вожатая, что бы мы наградили тебя и еще одну девушку мороженным за проделанную работу."
    "Повариха залезла в холодильник и, достав оттуда два брикета эскимо, протянула их мне."
    nd_il "Спасибо вам."
    pov "На здоровье."
    "Взяв оба мороженного и оглянувшись, я увидел Лену.{w} Она сидела за последним столом и допивала чай. Видимо, запеканка ей тоже не особо понравилась."
    window hide

    $ renpy.pause(1)

    window show
    "Я подошел к ней отдал один брикет с мороженным."
    nd_il "Держи. Это нам с тобой за покраску кружка."

    show un smile pioneer at center with dspr
    
    un "Спасибо."
    nd_il "Это поварам спасибо."
    "Мы оба улыбнулись друг другу.{w} Лена продолжила пить чай, а я уже собирался выходить на улицу со своей \"холодной наградой\"."    
    window hide

    show black with dissolve2
    play sound sfx_open_door_1 
    $ renpy.pause(1)
    
    $ nd_change_time('sunset')
    
    scene bg ext_dining_hall_near_sunset with dissolve2
    play ambience ambience_camp_center_evening fadein 3
    $ renpy.pause(1)
    play sound sfx_close_door_1 
    $ renpy.pause(1)
    scene bg ext_dining_hall_away_sunset with dissolve
    
    window show
    th "Доем мороженное и на поиски..."
    window hide

    $ renpy.pause(1)

    window show
    "Подумал я, сел на лавочку рядом со столовой и развернул мороженное."
    "Даже вечером солнце жарило как ненормальное, поэтому казалось, что эскимо таяло прямо на глазах."
    window hide

    $ renpy.pause(3)

    window show
    "Быстро расправившись с мороженным, я вытер рот предусмотрительно украденной из столовой салфеткой. Теперь чистыми руками можно было достать карту."
    window hide

    play sound nds_list['nd_map_open']

    $ renpy.pause(1)
    
    window show
    th "Где же она может быть?"
    th "Тут три варианта: дом, футбольная площадка и сцена.{w} Самое банальное оставлю на последнее. Поэтому сперва..."
    window hide

label us_searching_main:
    
    

    $ disable_all_zones()
    $ set_zone("estrade", "estrade_searching_us_d2") 
    $ set_zone("sport_area", "sport_searching_us_d2")
    
    if necessary_search_us_scene == 1:
        $ reset_zone("estrade")
    
    if necessary_search_us_sport == 1:
        $ reset_zone("sport_area")
    
    if necessary_search_us_map == 2:
        jump d2_search_us_preend
    
    
    
    $ show_map()
    
label sport_searching_us_d2:

    $ disable_current_zone()    
    $ necessary_search_us_sport += 1
    $ necessary_search_us_map += 1
    show black with dissolve
    $ renpy.pause(2)
    
    window show
    "Спустя пару минут показалось уже знакомое здание со спортзалом."
    window hide

    $ renpy.pause(1)
    scene bg us_fb_p_sunset with dissolve2
    
    window show
    "Зайдя за него, я увидел младшие отряды.{w} Но внимательно осмотревшись, понял, что Ульяны здесь нет."
    th "Ульяны здесь нет, значит..."
    window hide

    jump us_searching_main
    
label estrade_searching_us_d2:
    $ disable_current_zone()    
    $ necessary_search_us_scene += 1
    $ necessary_search_us_map += 1
    
    show black with dissolve
    $ renpy.pause(1)
    
    window show
    "...Мне надо идти на сцену."
    window hide

    $ renpy.pause(3)
    
    play music ndm_list['solo_dv_d2'] fadein 3
    $ volume(0.1, "music")

    window show
    "Спустя минуту в далеке уже виднелась сцена."
    "Оттуда доносилась глухая музыка, и я решил пойти посмотреть, что там."
    window hide

    $ renpy.pause(1)
    stop music fadeout 3
    scene bg ext_stage_big_sunset with dissolve2
    $ volume(1.0, "music")
    play music ndm_list['solo_dv_d2'] fadein 3

    window show
    "Дойдя до неё, я увидел Алису, которая играла на рок-гитаре с закрытыми глазами. Она, видимо, наслаждалась своей игрой."
    "Решив послушать как она играет, я сел на место на трибуне и принялся слушать её."
    window hide

    show cg d1_dv_guitar with dissolve
    $ renpy.pause(1)
    if dv_flag_morning_d1 == True:

        window show
        "Она была неотразимой. Музыка, которую она играла вчера, преобразилась и выглядела шикарно."
        "А самое главное, была собственного сочинения,{w} что добавляло ещё больше крутизны в её игру."
        window hide

    
    $ renpy.pause(1)

    window show
    "Мне на секунду показалось, что она видит меня, или уже давно закончила свою игру.{w} Но она продолжала играть, придумывая более усложнённые варианты аккордов."        
    window hide

    $ renpy.pause(2)
    scene bg ext_stage_big_sunset with dissolve
    stop music fadeout 3

    window show
    "Вскоре она закончила игру резким ударом по струнам, и плавно подняла свою голову на меня."

    play sound_loop nds_list['applweak'] 
    
    "Я начал хлопать."
    
    stop sound_loop fadeout 1
    
    dv "Ну как? Тебе понравилось?"
    "Улыбнувшись спросила Алиса."
    nd_il "Это было великолепно!"
    "После моего комплимента, на лице Алисы проскочила нотка смущения.{w} Или мне просто показалось?"
    dv "Да ладно тебе."
    
    
    if dv_flag_morning_d1 == True:
        dv "Так ты всё-таки нашёл меня, чтобы на гитаре поиграть?"
        th "Точно, мне же нужно Ульяну найти.{w} Хотя, может задержаться на немного?"
    else:
        dv "Так и зачем ты пришёл? Чтобы на гитаре моей поиграть?"
        th "Мне нужно Ульяну найти.{w} И никаких задержек."
    
    window hide
    
    $ renpy.pause(1)

    window show
    nd_il "Прости, я бы остался, но мне нужно Ульяну найти ещё.{w} Пока с ней чего плохого не случилось."
    nd_il "Кстати, ты не видела её?"
    dv "Нет не видела."
    dv "Можешь проверить наш домик. Если она будет там - она должна тебе ответить."
    nd_il "Хорошо, я побежал её искать..."
    
    if dvrr >= 3:
        $ d2_dv_night_pristan_q = True            
        dv "Ладно, только когда найдёшь..."
        "У Алисы немного порозовели щёки."
        dv "...Приходи к пристани.{w} Там поговорим может быть...{w} Как вчера..."
        nd_il "Хорошо."
        "Я встал со зрительского места."
        $ renpy.pause(1)
        dv "Только не забудь."
        nd_il "Не забуду."
        "Ответив, я направился дальше на поиски Ульяны."
        window hide
        $ renpy.pause(1)
        jump us_searching_main
    
    elif nir >= 2:

        $ d2_dv_night_pristan_q = True            
        dv "Ладно, только когда найдёшь..."
        "У Алисы немного порозовели щёки."
        dv "...Приходи к пристани.{w} Там поговорим может быть...{w} Как вчера..."
        nd_il "Хорошо."
        "Я встал со зрительского места."
        $ renpy.pause(1)
        dv "Только не забудь."
        nd_il "Не забуду."
        "Ответив, я направился дальше на поиски Ульяны."
        window hide
        $ renpy.pause(1)
        jump us_searching_main
    
    else:
        dv "Удачи тебе в поисках."
        "Подмигнув, сказала Алиса."
        "Я подмигнул ей в ответ, и встав со зрительского места направился дальше, на поиски Ульяны."
        window hide
        $ renpy.pause(1)
        jump us_searching_main
        
        
        
label d2_search_us_preend:

    show black with dissolve2
    $ renpy.pause(1)

    window show
    th "...Может она действительно в своем домике отдыхает?"
    "Подумал я и быстрым шагом отправился к домику Ульяны и Алисы."
    window hide

    $ renpy.pause(2)
    
    if d2_dv_night_pristan_q == True:

        window show
        th "Зачем Алиса позвала меня на пристань?"
        th "Она выглядела стеснительной...{w} Может она что-то чувствует ко мне?"
        th "Хотя, может я, как всегда, могу всё преувеличить, и она просто хочет поговорить..."
        window hide


    $ renpy.pause(2)
    scene bg ext_house_of_dv_sunset with dissolve2
    
    window show
    "Вскоре я уже стоял у входной двери в домик рыжих."

    play sound sfx_knocking_door_2

    "Я несколько раз с паузами постучал в деревянную дверь, но мне никто не ответил. Даже на второй и третий разы."
    "Вероятно, внутри домика никого не было."
    window hide

    $ renpy.pause(1)

    window show
    th "А может она на вчерашнем пляже?"
    "Подумав об этом я незамедлительно побежал на секретный пляж Ульяны, на котором мы вчера с ней отдыхали после её экскурса по Совёнку."
    window hide

    stop ambience fadeout 4
    show black with dissolve2
    $ renpy.pause(1)
    play ambience ambience_camp_center_evening fadein 4
    scene bg ext_path_sunset with dissolve2
    
    window show
    "Передо мной оказался небольшой пролесок." 
    "Я шел по нему и думал, что именно сейчас увижу Ульяну, которая сидит под деревом и смотрит в горизонт." 
    window hide

    stop ambience fadeout 4
    show black with dissolve2
    play sound sfx_hiding_in_bush
    $ renpy.pause(1)
    play ambience ambience_lake_shore_day fadein 4
    scene bg tain_beach_us with dissolve2
    
    window show
    "Но придя к тому самому месту,{w} я никого не увидел."
    "Ни следов Ульяны, ничего."
    "Только слепящее глаза солнце над водой встречало меня своими красноватыми лучами."
    window hide

    play music ndm_list['mood_worried'] fadein 4

    $ renpy.pause(1)

    window show
    th "Здесь мы вчера лежали на песке, тут фотографировались, а тут музыку слушали..."
    window hide

    $ renpy.pause(1)
    
    show blink
    
    window show
    "Я закрыл глаза."
    vg "Илья, может тот сон, он вещий?"
    window hide

    $ renpy.pause(1)
    
    window show
    th "Может быть.{w} Я уже готов даже в это поверить..."
    window hide

    stop music fadeout 1
    stop ambience fadeout 1
    $ renpy.pause(1)
    scene bg tain_mesto_night with flash
    $ renpy.pause(0.3)
    scene bg tain_beach_us with flash
    play ambience ambience_lake_shore_day fadein 1

    window show
    th "Нет, я найду её. Я знаю, где она может быть."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    play ambience ambience_forest_day fadein 3
    play sound_loop sfx_run_forest fadein 3
    
    window show
    "Я побежал со всех ног в лес, в то место из своего дневного сна."
    window hide

    $ renpy.pause(1)
    
    window show
    "По дороге только и приходилось перепрыгивать ямы, различные препятствия и многое другое, что уже говорило о том, что я вышел за пределы лагеря."
    window hide

    stop ambience fadeout 2
    $ renpy.pause(1)
    play ambience ambience_camp_entrance_evening fadein 3
    play sound sfx_hiding_in_bush
    scene bg ext_camp_entrance_sunset_wahf with dissolve
    stop sound_loop fadeout 3
    
    window show
    "Но в конце концов я выбежал к воротам лагеря." 

    th "Да как я вообще попал сюда?"
    th "Мне казалось, что я бежал вглубь лагеря, а не к воротам."
    window hide

    $ renpy.pause(1)
    play sound sfx_inhale 
    $ renpy.pause(1)

    window show
    "Оглянувшись по сторонам, я побежал на память к поляне." 
    "Той, что из моего сна. Либо к той, где мы уснули вместе."
    window hide

    play sound sfx_hiding_in_bush
    show black with dissolve2

    play ambience ambience_forest_day fadein 3
    $ renpy.pause(1)
    play sound_loop sfx_run_forest fadein 2
    $ renpy.pause(4)
    scene bg ext_polyana_sunset with dissolve2
    stop music fadeout 3
    stop sound_loop fadeout 2
    play sound sfx_bush_body_fall
    play sound_loop sfx_head_heartbeat fadein 2
    
    window show
    "Я вынырнул из-за кустов, и на секунду увидел ту самую поляну."
    "Но ноги встретили какое-то твёрдое препятствие, и последним, что я почувствовал, был сильный удар по голове."    
    window hide

    $ renpy.pause(1)
    show black with flash
    stop ambience fadeout 3
    stop sound_loop fadeout 2
    $ renpy.pause(7, hard=True)
    play ambience ambience_camp_center_night fadein 3
    
    $ nd_change_time('night')
    
    window show
    "Пролежав на траве в отключке несколько часов, я медленно открыл веки." 
    window hide

    scene bg ext_polyana_night
    hide blink
    show unblink
    
    $ renpy.pause(1)

    window show
    "Было уже довольно темно.{w} Лунный свет падал на траву, на которой я лежал."
    play sound sfx_inhale
    "В лёгкие тут же прорвался лесной слегка влажный воздух. Голова раскалывалась, но не настолько, чтобы можно было прекратить эти поиски."
    "Я верил, что я совсем близко. Что вот-вот увижу Ульяну."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я набрался достаточным количеством сил для того, чтобы подняться на ноги."
    "Вокруг меня была именно та поляна из моего сна."
    "Она была точь в точь такой же.{w} И это поражало мой разум."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я набрал в лёгкие побольше воздуха и прокричал:"
    with hpunch
    nd_il "Ульяна!"
    "...Но мне ответило лишь моё эхо."
    "Хоть я и не был до конца уверен, что смог бы через него услышать, как мне в ответ кричит рыжая пионерка."
    window hide

    window show
    "Очередной раз, оглянув поляну я заметил знакомый мне куст."
    "Он точно был тем самым, который я видел в своём сне."
    window hide

    $ renpy.pause(1)
    show black with dissolve 
    play sound sfx_hiding_in_bush
    
    window show
    "В миг я понял, что на верном пути и побежал через него в сторону таинственного волшебного места с прозрачной водой."
    "Я не знал что будет со мной дальше."
    "Может, я найду Ульяну и мы вернемся в лагерь.{w} А может я останусь ночевать здесь, заблудившись в этом лесу.{w} А может я пойду на корм какому-нибудь зверью."
    
    play sound_loop sfx_run_forest fadein 1
    
    "Бежать пришлось через поваленное дерево и сквозь кусты, куда вела моя интуиция."
    window hide

    $ renpy.pause(2)
    stop sound_loop fadeout 2
    scene bg ext_path2_night with dissolve 
    
    window show
    "Вскоре я вышел на протоптанную тропинку.{w} И если порядок предыдущих локаций можно было списать на совпадение, то тут уже всё встало на свои места..."
    window hide

    $ renpy.pause(1)

    window show
    th "Это был не просто сон…"
    window hide

    $ renpy.pause(1)
    play sound_loop sfx_far_steps fadein 1
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_path_night with dissolve
    
    window show
    "Недолго идя по тропинке, вскоре меня встретила развилка."

    stop sound_loop fadeout 2
    
    "Было два пути — налево и направо."
    th "Ну, куда идем?"
    vg "Куда тебя зовет сердце, друг мой."
    vg "Да, точно, я забыл. У тебя нет сердца."
    th "Очень смешно."

    "Я задумался, осмотрел тропинку и...{w} Заметил следы. Следы человека с босыми ногами, и следы человека в ботинках."
    th "Может Ульяна потеряла обувь?{w} Нет, она бы вернулась в лагерь."
    th "Хотя что мне мешает обратно вернутся к этой тропинке в случае неудачи?"
    th "Ладно, нельзя терять ни минуты."
    window hide

    $ renpy.pause(1)
    
    window show
    "Взвесив все факты, я принял решение бежать по левой тропинке..."
    window hide

    show black with dissolve2
    
    play sound_loop sfx_run_forest fadein 2

    $ renpy.pause(1)
    
    window show
    "Я бежал и бежал..."
    "Она как будто бесконечная..."
    "Я было уже хотел развернуться назад, но..."
    window hide

    stop sound_loop fadeout 2
    $ renpy.pause(2)
    scene bg tain_mesto_night with dissolve2
    play music ndm_list['mood_friendship_1'] fadein 3
    
    window show
    "Я выбежал к тому самому озеру."
    "Оно было таким-же прозрачным, как и во сне..."
    "Но тут не было Ульяны, вопреки всем моим ожиданиям."
    scene bg tain_mesto_night with vpunch
    nd_il "Ульяна!"
    "Снова мне никто не ответил..."
    window hide
    
    $ renpy.pause(1)

    window show
    "Я подошел к озеру, свесил ноги и опустил голову вниз."
    th "И что теперь? Где ты можешь быть?"
    window hide

    $ renpy.pause(1)
    show blink

    window show
    th "А может... Уже нигде?{w} Может тебя уже давно нет?"
    th "Почему она ушла? Это из-за того, что мы вместе уснули с ней?"
    th "Почему я не использовал хотя-бы половину вещества, находящегося у себя в голове, чтобы отвести её тогда в лагерь..."
    th "Опять во всём виноват я. И тут больше некого винить."
    th "Последний человек в этом лагере, с которым мне было весело, просто отвернулся от меня."
    th "Или того хуже, умер... Из за меня..."
    th "От голода или холода, или съеден каким-то медведем..."
    th "И если это так, то пусть и я закончу так же в мире, о котором ничего не знаю, даже как я попал сюда."
    th "Возможно если я совершу суицид, я смогу вернутся домой, а может всё начнётся с начала, или закончится..."
    window hide

    $ renpy.pause(2)
    stop music fadeout 1
    stop ambience fadeout 2
    $ renpy.pause(2)

    window show
    "Я откинул мысли об этом прежде,{w} чем мои глаза плавно закрыли две теплые маленькие ладошки."
    usp "Угадай кто?"
    th "Ульяна…"
    nd_il "Это сбежавшая из лагеря девочка, которую я ищу."
    "Я повернулся..."
    window hide

    $ renpy.pause(1)
    
    show us grin pioneer at center
    hide blink
    show unblink
    play music ndm_list['mood_depr'] fadein 4
    
    window show
    "На меня смотрели голубые как небо глаза. Это была Ульяна."
    us "Нашел меня всё-таки."
    nd_il "Черт его возьми, я волновался!{w} Где ты была?"

    show us shy pioneer at center with dspr
    
    us "В смысле волновался? За меня?"
    nd_il "Да. Искал. И, как видишь, нашел."
    us "Гуляла.{w} Новые места искала.{w} Не стоило за меня волноваться."
    nd_il "Все хорошо? Что-нибудь болит?"
    show us shy2 pioneer at center with dspr
    us "Нет, дурак."
    us "Я же сказала что вернусь."
    us "Хотя и вправду немного заблудилась..."
    nd_il "Тогда не будем задерживаться, и пойдем в лагерь?"
    
    show us grin pioneer at center with dspr
    
    us "Да. Пошли."
    
    hide us with dspr
    
    "Улыбнувшись, сказала Ульяна, и поскакала к лагерю.{w} А я шел за ней, стараясь не отставать."
    window hide

    play ambience ambience_forest_night fadein 3
    play sound_loop sfx_far_steps fadein 2
    $ renpy.pause(1)
    show black with dissolve2
    $ renpy.pause(2)
    stop sound_loop fadeout 1
    scene bg ext_path_night with dissolve2
    
    window show
    "Вскоре мы пришли к развилке."
    "Я хотел пойти по той тропинке, по которой пришёл, но Ульяна быстро исправила меня."
    us "Нет Илья, этим путём будет быстрее."
    nd_il "Но...{nw=1}"
    us "Никаких \"но\". Пошли за мной..."
    window hide

    $ renpy.pause(1)

    window show
    "Было решено идти так, как сказала эта рыжая девушка. Ведь она, определенно, знала этот лес больше, нежели я."
    window hide

    play sound_loop sfx_far_steps fadein 3
    show black with dissolve2
    $ renpy.pause(1)

    window show
    th "...И в чем был смысл тогда её искать, если она всё знает."
    th "Похоже, это была какая-то её игра, которую мне не дано понять."
    th "Да какая к черту игра, когда за тебя кто-то волнуется..."
    vg "Да помолчи уже, нытик."
    vg "Ты получаешь внимание от девочки. Грех жаловаться на это."
    th "Ну знаете ли..."
    window hide

    stop music fadeout 4
    $ renpy.pause(2)

label d2_search_us_end:

    stop sound_loop fadeout 2
    stop ambience fadeout 2
    $ renpy.pause(1)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_square_night with dissolve2
    
    window show
    "Вскоре мы дошли до лагеря и вышли прямиком на площадь."
    "Некоторые пионеры все еще гуляли по лагерю, хоть и было уже довольно темно."
    window hide

    $ renpy.pause(1)

    window show
    "Там же нам встретилась Ольга Дмитриевна."
    show mt normal pioneer at center with dspr
    mt "Илья, ты не был на ужине."
    mt "Ты нашел Ульяну?"
    nd_il "Она меня нашла."
    "Улыбнувшись проговорил я."
    show mt smile pioneer at center with dspr
    mt "Ладно.{w} Вы наверное есть хотите."
    mt "Давайте я вам столовую открою, и вы поедите?"
    us "Нет, Оль Дмитриевна, спасибо. Я кушала."
    "У меня возникли сомнения. Чем Ульяна могла питаться в лесу? Или она в тихую в домике кушала?"
    nd_il "Я тоже не хочу."
    show mt normal pioneer at center with dspr
    mt "Ну ладно, тогда идите спать."
    mt "Завтра трудный день."
    hide mt with dspr
    th "У меня, наверное, каждый день трудный."
    th "Хотя сегодня я особо ничем и не занимался...{w} Разве что музыкальный кружок с Леной покрасил, Алису послушал."
    th "Никогда этого не забуду..."
    show mt angry pioneer at center with dspr
    mt "И не уходите больше за пределы лагеря или в лес.{w} Там ведь опасно."
    us "Простите, так получилось."
    show mt normal pioneer at center with dspr
    mt "Ульяна, мы завтра утром с тобой отдельно поговорим на эту тему."
    mt "А теперь идите по домикам."
    nd_il "Хорошо."
    us "Так точно."
    mt "Спокойной ночи."
    window hide

    hide mt with dspr
    
    $ renpy.pause(1)

    window show
    "Сказала Ольга Дмитриевна, и отойдя от нас на другой конец площади присела на скамейку к какой-то своей подружке, вероятно вожатой из другого отряда."
    window hide

    $ renpy.pause(2)

    if dvrr >= 3:
        
        window show
        "Погодите.{w} Меня же Алиса попросила с ней у пристани встретиться."
        window hide

        $ renpy.pause(1)
       
        menu:
            
            "Не идти на пристань":
                $ persistent.nd_moral_points -=1
                $ d2_night_csx = True
                $ usrr += 1

                window show
                "Действительно, зачем мне это?"
                "Можно поговорить с Алисой и завтра.{w} А сегодня я очень устал."
                window hide

                $ renpy.pause(1)
                
                window show
                "Мы с Ульяной отправились к нашим домикам..."
                window hide

                jump d2_search_us_end_2


            "Пойти на пристань":
                $ persistent.nd_moral_points +=1
                $ d2_dv_night_pristan = True
                $ d2_night_dv = True
                $ dvrr += 1
                jump d2_dv_guitarclub

    elif nir >= 2:

        window show
        "Погодите.{w} Меня же Алиса попросила с ней у пристани встретиться."
        "А может сходить туда вместе с Ульяной?"
        window hide

        $ renpy.pause(1)
        menu:

            "Пойти на пристань с Ульяной":
                $ d2_night_nir = True
                $ nir += 1
                $ persistent.nd_moral_points -=1

                show us normal pioneer at center with dspr
                
                window show
                nd_il "Ульяна, не хочешь сходить со мной на пристань?"
                th "Ну, вообще не только со мной, но мы это опустим."
                
                show us shy pioneer at center with dspr
                
                us "Что?"
                nd_il "Ну, на пристань.{w} Сходить."
                us "Зачем?"
                th "Да что же ты такая любопытная то..."
                nd_il "Просто прогуляться."
                us "Со мной?{w} Ну…{w} Пошли…"
                
                hide us with dspr
                
                "Мы отправились в сторону пристани, но нас, как назло, заметила Ольга Дмитриевна."
                mt "Пионеры, ваши домики в другой стороне. "
                us "Я серёжку потеряла."
                "Ульяна подмигнула мне, и я понял, что нам нужно бежать."
                window hide

                $ renpy.pause(1)
                
                show black with dissolve 
                
                scene bg ext_path2_night with dissolve:
                    zoom 1.05anchor (48,27)
                    ease 0.20pos (0, 0)
                    ease 0.20pos (25,25)
                    ease 0.20pos (0, 0)
                    ease 0.20pos (-25,25)
                    repeat

                window show
                th "Опять приходится переходить на бег.{w} Если так пойдет дальше, я скоро себе ноги сотру."
                vg "Не ной.{w} Сам на пристань захотел."
                th "Так я погулять."
                vg "Ну вот тебе и прогулка."
                window hide

                jump d2_us_dv_pristan

            "Не идти на пристань":
                $ d2_night_csx = True
                $ usrr += 1
                window show
                "Действительно, зачем мне это?"
                "Можно поговорить с Алисой и завтра.{w} А сегодня я очень устал."
                window hide

                $ renpy.pause(1)

                window show
                "Как только я подумал об этом, мы с Ульяной тут же отправились к нашим домикам..."
                window hide

                jump d2_search_us_end_2


            "Пойти на пристань самому":
                $ d2_dv_night_pristan = True
                $ d2_night_dv = True
                $ dvrr += 1
                $ persistent.nd_moral_points +=1
                jump d2_dv_guitarclub

    else:       
    
        $ usrr += 1

        window show
        nd_il "Ну что, пошли по домам?"
        window hide

        $ renpy.pause(1)
        show us normal pioneer at center with dspr
        window show
        us "Да, пошли."
        hide us with dspr
        "Ульяна произнесла это слегка задумчивым тоном.{w} Похоже, обдумывала нашу встречу в лесу."
        "Тем не менее, нами было принято решение отправится по домикам..."
        window hide

        jump d2_search_us_end_2
        
label d2_search_us_end_2:    
    
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_night_1 with dissolve    
    
    window show
    nd_il "Ульяна, так где ты всё-таки была?"
    us "Ну, я уходила на целый день, потому что...{w} Искала одно место..."
    us "Я тебе пока не могу сказать, что это за место.{w} Может потом..."
    nd_il "Ладно, можешь не говорить.{w} Главное, что с тобой всё в порядке."
    window hide

    $ renpy.pause(1)

    if usrr >= 3:

        window show
        "Ульяна слегка засмущалась от сказанного мной, но попыталась скрыть это и слегка отвернулась, как только я посмотрел на неё."
        "От её поведения в данную секунду я слегка умилился."
        window hide
    
    else:

        window show
        "Ульяна показалась мне на мгновение достаточно вдумчивой. Особенно для своего характера."
        "Было странно видеть её такой сейчас."
        window hide

    $ renpy.pause(2)

    window show
    us "А как ты нашел то место с озером?"
    nd_il "Это что, был ещё один \"тайный путёк\"?"
    "На лице Ульяны проскочила улыбка."
    us "Можно и так сказать."
    window hide

    show black with dissolve

    $ renpy.pause(1)

    scene bg ext_home_night with dissolve2
    
    window show
    "Мы подошли к моему домику и остановились около его входа.."
    window hide
    
    if usrr >= 3:
        play music ndm_list['mood_love_2'] fadein 3
        show us shy2 pioneer at center with dspr 
        
        window show
        us "Ну ты это..."
        us "Прости меня, что заставила волноваться."
        nd_il "Прости, что поставил в такую ситуацию."
        nd_il "И если ты из-за этого уходила сегодня...."
        us "Дурак."
        
        hide us with dspr
        
        "Сказав это, Ульяна заключила меня в объятия."
        "А я рефлекторно обнял её в ответ."
        "Она была ниже меня, поэтому мне пришлось слегка нагнуться, и почувствовать приятный запах её рыжих волос."
        "Этот запах старательно пытался заставить меня вспомнить что-то приятное из своего прошлого.{w} Но я не смог."
        window hide

        $ renpy.pause(1)

        window show
        nd_il "Ничего страшного."
        window hide

        $ renpy.pause(2)
        show us shy2 pioneer at center with dspr
        
        window show
        us "Ладно. Спокойной ночи тебе."

    else:
        
        show us normal pioneer at center with dspr
        
        window show
        us "Прости, что заставила волноваться и всё такое."
        "Ульяна посмотрела на меня странным взглядом, который я не смог никак расшифровать."
        nd_il "Ничего страшного."
        show us smile pioneer at center with dspr
        us "Тогда спокойной ночи."
        
        
    hide us with dspr
    "Ульяна побежала к своему домику."
    nd_il "Спокойной!"
    window hide

    stop music fadeout 3
    $ renpy.pause(2)
    
    window show
    th "Денёк выдался что надо."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_gg_night_1 with dissolve2
    play sound sfx_close_door_1
    
    window show
    "Войдя в домик я даже не разделся."
    window hide

    play sound sfx_open_window
    
    $ renpy.pause(1)

    window show
    "Открыв верхнюю часть окна на проветривание, я упал на свою кровать."

    if dv_flag_morning_d1 == True:
        "Странно. Сегодня она мне казалась необыкновенно мягкой."
        "И абсолютно всё равно, что она скрипит. Мне это не мешало в своей квартире, значит не будет мешать и здесь."

    if dv_flag_morning_d1 == False:
        "По сравнению с травой, на которой я заснул вчера, эта кровать показалась мне по необыкновению мягкой."
        "И абсолютно всё равно, что она скрипит. Мне это не мешало в своей квартире, значит не будет мешать и здесь."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 2
    show blink
    
    window show
    "Я закрыл глаза."
    window hide

    $ renpy.pause(1)
    
    window show
    "Мне вдруг на секунду показалось, что всё идет по какому-то неопределенному мною плану."
    "Хотя какой вообще план?{w} Мне просто, как обычно это бывает перед сном, в голову лез всякий бред."
    "Который у меня без труда удавалось скомкать и выбросить подальше.{w} И этот случай не должен был стать для меня исключением."
    window hide

    $ renpy.pause(1)
    
    window show
    "Повернувшись на правый бок я тут же почувствовал приближение сна..."
    window hide

    $ renpy.pause(2)
    
    jump nonly_for_beta_nd
    
label d2_us_dv_pristan:
    $ d2_nirvana_night_pristan = True
    
    scene bg ext_boathouse_night with dissolve2
    
    window show
    "Когда мы прибежали к пристани, увидели Алису, стоявшую рядом с домиком и, видимо, ждущую меня." 
    "Она обратила на нас внимание и подошла ближе."
    
    show dv angry pioneer2 at center with dspr
    
    us "Алиса, и ты тут?"
    dv "Как видишь."
    dv "Илья, мы же договаривались…"
    nd_il "Насчет Ульяны ты ничего не уточняла."
    window hide

    $ renpy.pause(2)

    window show
    dv "Ладно."
    
    hide dv with dspr
    
    "Буркнув сказала Алиса, и мы пошли медленным шагом вдоль берега."
    window hide

    $ renpy.pause(1)
    
    play ambience ambience_lake_shore_night fadein 3
    scene bg ext_beach_night with dissolve2
    
    window show
    "Природа была на удивление тихой и успокаивающей, а море убаюкивающим."
    "Смотря на это море, я заметил вдалеке какие-то острова."
    nd_il "А что вон там?"
    "Сказал я, и показал пальцем вдаль на остров что ближе, и тот, что дальше от пляжа."

    show dv normal pioneer2 at left
    show us smile pioneer at right
    with dspr
    
    "Алиса хотела что-то сказать, но Ульяна перебила её."
    
    us "Это Остров Ближний и Остров Дальний.{w} Там такие ягодки растут вкусные.{w} Когда-нибудь хочу там побывать."
    
    show dv smile pioneer2 at left with dspr
    dv "Я тебя, когда хочешь, свожу."

    show us grin pioneer at right with dspr
    us "Нет. Я хочу, чтобы нас свозил Илья."

    "Везти их куда-то сейчас я, естественно, не хотел."
    nd_il "Потом как-нибудь."

    show us smile pioneer at right with dspr
    us "Ура!"
    dv "Ульяна, тише."
    show us grin pioneer at right with dspr
    us "Хорошо, хорошо."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    scene bg ext_beach_night with dissolve
    $ renpy.pause(1)
    
    window show
    "Вскоре мы остановились, сели на песок, и продолжили наш разговор."
    dv "Илья, а ты откуда приехал?"
    nd_il "Ну... из Краснодара."
    us "А я из Пятигорска."
    dv "Я из Ленинграда сюда приехала.{w} Решила посмотреть, как тут люди живут."
    nd_il "Ну, и как?"
    dv "Тут, кажется, небо ниже. И теплее само собой."
    window hide

    $ renpy.pause(1)
    
    window show
    "Алиса прикоснулась своей рукой к моей правой.{w} Ульяна сделала с моей левой рукой тоже самое."
    nd_il "Знаете, а с вами прикольно."
    "Девочки заинтересованно взглянули на меня."
    nd_il "С вами не соскучишься.{w} Вы весёлые, можете придумать что-то интересное."
    window hide

    $ renpy.pause(1)  
    
    window show
    dv "Спасибо. Ты тоже вроде{w} прикольный."
    dv "А где этот твой проигрыватель?"
    us "И фотоаппарат."
    nd_il "Кибернетикам отдал, чтобы они мне его зарядили."
    us "Понятно. Я думала, что он у тебя без подзарядки может работать."
    nd_il "Если бы ещё он работал без подзарядки, это был бы просто чудо-аппарат."
    us "Чудо-чудо аппарат."
    "Ульяна тепло улыбнулась со своей шутки.{w} Я улыбнулся ей в ответ." 
    window hide

    $ renpy.pause(1)

    window show
    us "А у тебя есть животные какие-нибудь домашние?.."
    window hide

    $ renpy.pause(1)

    show black with dissolve 
    $ renpy.pause(1)

    window show
    "Мы разговаривали о разных вещах, сидя на песке и смотря в горизонт, на звездное небо, в море."
    window hide

    $ renpy.pause(1)
    
    window show
    "И сидели бы, если бы не чувство сна."
    window hide

    hide black with dissolve2

    window show
    us "Ребят.{w} Я уже спать хочу.{w} Пошли домой."
    nd_il "Да.{w} Кажется мы действительно засиделись."
    nd_il "Пора по домам..."
    window hide

    $ renpy.pause(1)
    show black with dissolve2
    stop ambience fadeout 2
    $ renpy.pause(1)
    play ambience ambience_camp_center_night fadein 2

    $ renpy.pause(2)
    scene bg ext_houses_night with dissolve2
    $ renpy.pause(1)
    scene bg ext_house_of_dv_night with dissolve2
    
    window show
    "Проводив девушек до дверей их домика, мы остановились."
    window hide

    show dv normal pioneer2 at left
    show us normal pioneer at right 
    with dspr
    
    window show
    nd_il "Ну, пока девчёнки."
    window hide

    hide us with dspr
    $ renpy.pause(2)
    show us normal pioneer at right with dspr
    $ renpy.pause(1)
    hide us with dspr
    play sound sfx_open_door_1
    play sound sfx_close_door_1
    
    window show
    "Ульяна сонно подошла ко мне и заключила в объятия, а затем открыла дверь домика и ушла внутрь."
    nd_il "Устала."
    
    show dv smile pioneer2 at left with dspr
    
    dv "Похоже на то." 
    dv "Ладно, давай."
    window show

    hide dv with dspr
    $ renpy.pause(1)
    show dv normal pioneer2 at center with dspr
    $ renpy.pause(1)
    hide dv with dspr
    play sound sfx_open_door_1
    play sound sfx_close_door_1
    
    window show
    "Сказала Алиса и, обнявшись со мной, тоже ушла к себе."
    window hide

    $ renpy.pause(2)
    
    window show
    "Немного постояв, я тоже отправился к своему домику."
    window hide

    scene bg ext_houses_night with dissolve2

    window show
    th "Да… Вот это денёк. А завтра, кажется, будет только интереснее.{w} Хотя… Может завтра уже и не будет."
    window hide

    scene bg ext_home_night with dissolve

    window show
    th "Может я проснусь у себя в квартире, на своей кровати.{w} И забуду об том, что сейчас происходит."
    window hide

    play sound sfx_open_door_1
    scene bg int_house_of_gg_night_1 with dissolve 
    play ambience ambience_int_cabin_night fadein 3
    play sound sfx_close_door_1
    
    window show
    "Зайдя в домик, я даже не разделся."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_window 
    $ renpy.pause(1)
    play sound sfx_bed_squeak1

    window show
    "Открыв окно на проветривание я лёг на кровать."
    window hide

    stop ambience fadeout 2
    stop music fadeout 2
    show blink
    $ renpy.pause(1)
    
    window show
    "В это-же мгновение я почувствовал помутнение разума и проваливание в сон..."
    window hide

    $ renpy.pause(3)
    
    jump nonly_for_beta_nd
    
label d2_dv_guitarclub:

    window show
    nd_il "Мне нужно ещё кое-куда сходить."
    
    show us normal pioneer at center with dspr
    
    us "А куда?"
    nd_il "Увидится нужно с другом."
    us "Ладно. Я тогда пошла."
    
    hide us with dspr 
    
    "Ульяна демонстративно зевнула, и пошла к своему домику."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Отлично. Теперь забот будет гораздо меньше."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я дождался, пока Ольга Дмитриевна отвлечётся, а затем побежал к пристани, как мы и договаривались с Алисой."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    play sound_loop sfx_run_forest
    $ renpy.pause(1)
    
    window show
    "Быстро пробежав через пролесок, я вышел на пляж..."
    window hide

    stop sound_loop fadeout 2 
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_boathouse_night with dissolve2

    window show
    "На пристани виднелась рыжая фигура.{w} Заметив друг друга, мы замерли. Алиса рукой подозвала меня к себе."
    window hide

    $ renpy.pause(2)

    window show
    "Уже через несколько секунд я уже был на пристани"
    window hide

    $ renpy.pause(1)
    show dv smile pioneer2 at center with dspr
    
    window show
    dv "Всё, таки пришёл. Я тебя уже давно жду."
    nd_il "Ты что-то хотела м…{w} Обсудить?"
    
    show dv shy pioneer2 at center with dspr

    dv "Да. Хотела."
    "Алиса замялась."
    nd_il "Пошли прогуляемся пока по побережью.{w} Там всё и расскажешь."
    dv "Ну пошли."

    hide dv with dspr
    scene bg ext_beach_night with dissolve2
    
    "И вот мы уже шагаем по темному берегу, смотря вдаль – в горизонт, куда заходят темные облака."
    "Не знаю почему, но мне было как-то спокойнее в компании этой девушки."
    "Это будто бы... свидание?"
    "Не верится, что со мной кому-то может нравится проводить время.{w} Я ведь на улицу даже не выхожу."
    window hide

    play music ndm_list['precious'] fadein 3
    $ renpy.pause (1)

    window show
    dv "Илья. Ты хочешь дальше заниматься гитарой?"
    nd_il "Да."
    dv "Просто ты…{w} Способный ученик."
    "Алиса немного покраснела."
    window hide

    $ renpy.pause (1)

    window show
    dv "Знаешь, у нас в лагере раньше было два кружка музыки. Один с Электрогитарой, другой на остальных инструментах."
    dv "И я, конечно, вела электрогитару.{w} Но ко мне совсем никто не ходил, поэтому кружок пришлось закрыть."
    dv "Я бы хотела… Может, мы с тобой сможем его восстановить?"
    window hide

    $ renpy.pause (1)
    
    window show
    nd_il "Я только за.{w} Только нам нужно здание."
    window hide

    $ renpy.pause (1)
    
    window show
    dv "Под здание можно подстроить склад."
    dv "Просто уберемся в нём, вынесем ненужное и готово.{w} И аппаратуру есть где ставить."
    nd_il "А куда мы денем вещи со склада? Раздадим пионерам?"
    "Алиса улыбнулась."
    dv "У нас в лагере два склада.{w} Так-что это не проблема." 
    dv "Думаю, завтра утром с этим разберемся.{w} Ты главное допоздна особо не спи."
    nd_il "Уж постараюсь. Но не обещаю."
    dv "Я тебе покажу \"не обещаю\". Не проснёшься – разбужу."
    "На лице у Алисы была улыбка, которая мне что-то напоминала. {w}Что-то родное и близкое сердцу."
    window hide

    $ renpy.pause (1)
    show black with dissolve
    $ renpy.pause (1)
    hide black with dissolve
    $ renpy.pause (1)
    
    window show
    "Вскоре мы остановились и присели на мягкий песок."
    dv "Кстати, Илья. А ты нашел Ульяну?"
    nd_il "Она уже в домике давно спит, дорогая."
    "Я ожидал, что Алиса после слова \"дорогая\" как минимум нахмурится, но она только улыбнулась.{w} Вот это было действительно странно."
    window hide

    $ renpy.pause (1)
    
    window show
    dv "Илья. А вы когда с Леной забор красили, она тебе ничего про меня не говорила?"
    nd_il "Нет.{w} По крайней мере я не помню об этом. Просто пожаловалась на хулиганов в лагере."
    nd_il "Я сказал, где и как ведро с водой вешать,{w}{nw=1} и…"
    dv "Короче, рано или поздно Ульяна в домик мокрой вернётся."
    "Она взяла меня за руку своей нежной теплой ладонью.{w} Я непроизвольно сжал её."
    window hide

    stop music fadeout 2
    $ renpy.pause (1)

    window show
    dv "Хочешь силами помериться?"
    window hide

    show black with dissolve2
    $ renpy.pause (1)
    
    window show
    "Вот так романтика превратилась в армреслинг."
    window hide

    $ renpy.pause (3)
    
    window show
    "Не понимаю как, но Алиса умудрилась меня победить.{w} Может это из-за усталости, а может я и вправду такой дрыщ..."

    hide black with dissolve2

    "Остальное время мы смотрели в горизонт, в синий небосклон, и так до тех пор, пока нас обоих не начало клонить в сон."
    window hide

    $ renpy.pause (1)

    window show
    dv "Ладно. Мне кажется, нам пора по домам.{w} А то меня уже в сон клонит."
    nd_il "Согласен."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause (2)
    play ambience ambience_camp_center_night fadein 3
    $ renpy.pause(1)
    scene bg ext_home_night with dissolve
    
    window show
    "Мы подошли к моему домику и остановились."
    
    show dv shy pioneer2 at center with dspr
    
    dv "Похоже, мы пришли."
    
    hide dv with dspr
    
    "Сказала Алиса и заключила меня в крепкое объятие. Я машинально обнял её в ответ."
    show dv shy pioneer2 at center with dspr
    
    dv "Не забудь про утро и музыкальный клуб. Спокойной ночи."
    nd_il "Спокойной."
    
    hide dv with dspr
    
    "Алиса пошла к своему домику, а я провожал её взглядом, пока она не скрылась за углом."
    window hide

    $ renpy.pause(1)

    play sound sfx_open_door_1
    scene bg int_house_of_gg_night_1 with dissolve 
    play ambience ambience_int_cabin_night fadein 3
    play sound sfx_close_door_1    
    
    $ renpy.pause(1)
    play sound sfx_open_window
    $ renpy.pause(1)
    play sound sfx_bed_squeak1

    window show 
    "Я зашел в свой домик, открыл форточку, и не раздеваясь лёг на не расправленную кровать."
    window hide

    $ renpy.pause(1)

    window show
    th "Зачем она спрашивала меня на счёт Лены?"
    window hide

    $ renpy.pause(1)
    show blink
    $ renpy.pause(1)
    
    window show
    "Смотря в потолок на протяжении пяти минут, я закрыл глаза и провалился в глубокий сон{w}, словно в бездонную пропасть."
    window hide
    
    $ renpy.pause(3)

    jump nonly_for_beta_nd


label nonly_for_beta_nd:
    
    stop music fadeout 1
    stop ambience fadeout 1

    $ renpy.pause(3)

    jump notdream_dream_d2_d3