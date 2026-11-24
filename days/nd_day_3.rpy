#---------------------------------------------------------------------------
# Не спойлери себе игру! 
#---------------------------------------------------------------------------

label d3_start_without:

    play ambience nda_list['rain_outside'] fadein 4
    show day_3_nd with dissolve2
    $ renpy.pause(1, hard = True)
    show day_3_blur_nd with nd_effect_5_reverse
    $ renpy.pause(1, hard = True)
    show day_3_text_nd with dissolve
    $ renpy.pause(3, hard = True)
    
    stop ambience fadeout 4
    hide day_3_nd
    hide day_3_text_nd
    hide day_3_blur_nd
    with dissolve2

    ##$ backdrop = "days"
    $ new_chapter(3, u"Это не просто сон, верно?\nДень третий")

    $ renpy.pause(3, hard = True)

    $ nd_change_time('day')

    $ renpy.pause(2)


    play ambience ambience_int_cabin_day fadein 3

    window show
    "В уши прорвалось ненастойчивое утреннее пение птиц..."
    window hide

    scene bg int_house_of_gg_day 
    hide blink
    show unblink

    $ renpy.pause(2)
    
    window show
    "Открыв глаза, я оказался в своём, уже привычном лагерном домике."
    "За зашторенным окном можно было увидеть яркий просачивающийся солнечный свет{w} — предвестник начала нового дня."
    th "Ничего себе сон, да еще такой реалистичный..."
    window hide

    $ renpy.pause(2)

    window show
    "Я оглядел свою комнату.{w} Со вчера, вроде бы, ничего и не изменилось."
    "Часы на деревянной стене показывали десять часов и двадцать минут."
    th "Судя по всему, я пропустил линейку.{w} Но зато успел выспаться."
    window hide

    $ renpy.pause(1)
    
    if dv_flag_morning_d1 == False:
        if paper_m == True:
            window show
            "Пройдясь взглядом по домику, я заметил стоявший у двери шкаф, на который я раньше почему-то не обращал внимания, и скомканный клочок бумаги, валяющийся на столе."

        else:
            "Пройдясь взглядом по домику, я заметил стоявший у двери шкаф, на который я раньше почему-то не обращал внимания, и аккуратно сложенный листок, мирно лежавший на столе."
    
    else:
        if paper_m == True:
            "Пройдясь взглядом по домику, я заметил скомканный листок, лежавший на столе."
        else:
            "Пройдясь взглядом по домику, я заметил аккуратно сложенный листок, мирно лежавший на столе." 


    nd_il "Блин, вставать ещё так неохота..."
    "Проговорил я вслух, и снова упал на свою пружинистую кровать, уткнув свой взгляд в деревянный потолок."
    window hide
    
    $ renpy.pause(1)
    
    window show
    "Всматриваясь в него, в глаза бросалась тонкая щель, через которую просачивался солнечный свет."
    "Эта щель в потолке казалась мне знакомой..." 
    window hide

    $ renpy.pause(1)
    
    stop ambience fadeout 1
    play sound sfx_scary_sting 
    scene bg tain_mesto_night with flash
    $ renpy.pause(1)
    scene bg int_house_of_gg_day with flash
    play ambience ambience_int_cabin_day fadein 3

    window show
    "В этот миг перед глазами всплыл вчерашний лес, только вот я не помнил, что я там делал и что я там забыл."
    th "Может, в записке мне объяснят, что вчера произошло?"
    window hide

    $ renpy.pause(3, hard=True)
    
    window show
    "Вскоре интерес переборол лень."

    if paper_m == True:
        "Я перешёл в положение \"сидя\", и развернув скомканный листок осмотрел его..."
    else:    
        "Я перешёл в положение \"сидя\" и посмотрел на содержание записки..."
    window hide

    show zapiska_d3 at center with dissolve
    $ renpy.pause(1)
    
    window show
    th "Хм-м..."
    th "Своей подписи автор, конечно же, не оставил."
    hide zapiska_d3 with dissolve
    th "Пошутил наверное кто-то.{w} Не может же мой сон материализоваться?" 
    window hide

    $ renpy.pause(1)
    if dv_flag_morning_d1 == False:
        window show
        th "Хотя тут всё возможно.{w} Даже тот из не откуда появившийся шкаф у двери..."
        $ renpy.pause(1)
    else:
        window show
        th "Хотя позапрошлый же материализовался..."
        window hide

        $ renpy.pause(1)
        
    if dv_flag_morning_d1 == False:
        
        $ renpy.pause(1)

        play sound sfx_open_cupboard

        $ renpy.pause(1)

        window show
        "Я встал с кровати, подошел к «новому» шкафу и, открыв дверцу, увидел на полке расческу и две розовые резинки для волос."
        th "Видимо, здесь раньше жили девушки, и забыли увезти свои вещи с собой."
        window hide
        $ renpy.pause(2)
        window show
        "Открыв глаза получше, я заметил зеркало на дверце."
        th "Ну что-же. Пора привести себя в порядок."
        "Я взял расческу, и посмотрев в зеркало пал в ступор..."
        window hide
        play sound sfx_scary_sting
        show cg d2_mirror with hpunch
        
        nd_il "Ёпт..."
        
        $ renpy.pause(1)

        window show
        nd_il "Пацан, ты кто?"
        "Очевидно, это был я.{w} Но на вид мне было не восемнадцать, а пятнадцать или шестнадцать лет."
        th "Вот это я помолодел за ночь.{w} В той рекламе с кремом действительно не врали…"
        window hide

        $ renpy.pause(1)
        
        window show
        "Факт того, что мне шестнадцать лет объяснял...{w} Да ничего он не объяснял!{w} Почему мне шестнадцать, мать их, лет?!"
        window hide

        $ renpy.pause(1)
        show black with dissolve

        window show
        nd_il "Ладно, ладно, ладно.{w} Надо умыться, как раз развеюсь."
        window hide

        $ renpy.pause(1)
        hide cg d2_mirror with dissolve
        $ renpy.pause(1)

        window show
        "Достав из шкафчика умывальные принадлежности я незамедлительно отправился к выходу из домика."
        window hide

        jump morning_d3_us_dv

    else:

        $ renpy.pause(1)

        play sound sfx_open_cupboard

        window show
        "Я встал с кровати, подошел к шкафу и, открыв его, запустил процесс расчесывания перед зеркалом..."
        window hide

        $ renpy.pause(1)
        show black with dissolve
        $ renpy.pause(3)
        hide black with dissolve
        $ renpy.pause(0,5)

        window show
        "Когда на голове был наведен марафет, я закрыл шкафчик."
        th "А теперь бы умыться."
        th "Надеюсь, вода в кранах этим утром будет тёплой."
        "С этими мыслями я отправился на выход из домика..."
        window hide


label morning_d3_us_dv:

    stop ambience fadeout 3
    show black with dissolve2
    play sound sfx_open_door_1
    $ renpy.pause(0,5)
    play ambience ambience_camp_center_day fadein 4
    play music music_list["my_daily_life"] fadein 4
    scene bg ext_house_of_sl_day with dissolve2 
    play sound sfx_close_door_1
    $ renpy.pause(1)

    window show
    "На небе плавно плыли облака, закрывая утреннее солнце.{w} Из-за этого на улице было немного прохладно."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve2

    window show
    "Я шёл к умывальникам и думал о событиях, произошедших вчера, о значении моего сна и о записке, оставленной таинственным незнакомцем,{w} а также о своем необыкновенно молодом отражении в зеркале."
    window hide

    $ renpy.pause(1)
    scene bg ext_washstand_day with dissolve2
    $ renpy.pause(1)

    window show
    "Вскоре я дошёл до умывальников и подошёл к одному из них."
    window hide

    show bg ext_washstand2_day with dissolve
    $ renpy.pause(1)
    play sound sfx_open_water_sink
    $ renpy.pause(0.5)
    play sound_loop sfx_water_sink_stream
    
    window show
    "Открыв кран, я потрогал струю воды пальцами."
    if dv_flag_morning_d1 == False:    
        "Она была всё такая же холодная, как и вчера."
        "К счастью, именно такая температура воды мне и нужна была этим утром."
        window hide

        $ renpy.pause(1)
        
        window show
        "Я поднёс ладони к струе воды и, набрав её в руки, поспешно вымыл своё заспанное лицо."
    
    else:
        "В отличие от вчерашнего дня, вода была довольно холодной."
        "Я поднёс ладони к струе воды и, набрав её в руки, поспешно вымыл своё заспанное лицо."    
    window hide

    $ renpy.pause(1)
    show blink
    $ renpy.pause(1)
    hide blink
    show unblink
    $ renpy.pause(1)
    with hpunch

    window show
    th "У-у-у. Холодная…"
    window hide

    $ renpy.pause(1)
    
    window show
    sl "Доброе утро, соня."
    "Послышался сзади женский голос."
    window hide

    stop music fadeout 4
    show blink
    $ renpy.pause(1)
    stop sound_loop
    play sound sfx_close_water_sink
    scene bg ext_washstand_day
    hide blink
    show unblink
    
    window show
    "Я вытер лицо полотенцем и повернулся."
    show sl normal pioneer at center with dspr
    "На меня улыбаясь смотрела миловидная девушка Славя."

    nd_il "Доброе."
    nd_il "Я пропустил линейку сегодня. Ольга Дмитриевна не злится?"

    show sl smile pioneer at center with dspr
    
    sl "Ничего страшного, ты ведь вчера Ульяну искал."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ко мне снова возвращалась память."
    th "Точно..."
    nd_il "Ну, да…"
    sl "И ещё. Ты вот это по дороге потерял..."
    "Славя протянула мне пакет с моим зубным порошком."
    nd_il "Спасибо, Славь."
    show sl smile2 pioneer at center with dspr
    sl "Не за что."
    hide sl with dspr
    show sl smile2 pioneer far at center with dspr
    sl "Я пошла, ещё увидимся."
    window hide

    $ renpy.pause(1)
    hide sl with dspr
    $ renpy.pause(1)
    
    play music music_list["my_daily_life"] fadein 4
    
    window show
    "Я проводил Славю взглядом, и продолжил свои водные процедуры."
    window hide

    $ renpy.pause(1)

    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream
    show bg ext_washstand2_day with dissolve
    
    window show
    th "Значит, я искал вчера Ульяну."
    th "Господи, да что у меня случилось за эту ночь с памятью?"
    window hide

    $ renpy.pause(1)
    with hpunch
    
    window show
    th "Холодна-я-я!"
    window hide

    show black with dissolve
    
    $ renpy.pause(1)
    stop sound_loop
    play sound sfx_close_water_sink
    $ renpy.pause(1)
    
    window show
    "Закончив с умываниями и чисткой зубов, я взял пакет с вещами за пазуху и пошёл к своему домику." 
    window hide

    scene bg ext_houses_day with dissolve2
    
    $ renpy.pause(1)

    window show
    "На обратном пути я заметил, как всё вокруг цвело и обретало краски. По сравнению с серой зимой в моем городе."
    "Но иногда мне не хватает дождя, прохладного и моросящего.{w} Может, я могу надеяться хотя бы на грибной дождик в этом летнем лагере?"
    window hide

    stop music fadeout 4
    scene bg ext_house_of_sl_day with dissolve2
    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_1
    scene bg int_house_of_gg_day with dissolve
    play music music_list["two_glasses_of_melancholy"] fadein 4
    play ambience ambience_int_cabin_day fadein 3
    play sound sfx_close_door_1
    $ renpy.pause(1)
    play sound sfx_open_cupboard

    window show
    "Дойдя до своего домика, я положил все вещи в шкафчик."
    "Осмелясь наконец подойти к большому шкафу, я открыл его дверцу и посмотрел в зеркало."

    show cg semyon_mirror with dissolve
    
    "Ну что, юноша, пора привести себя в порядок."
    
    show black with dissolve
    
    "Взяв расческу, я начал выравнивать свои волосы, зализывая торчавшие на макушке."
    window hide

    $ renpy.pause(1)
    
    window show
    "После нескольких повторений данной процедуры положение на голове было приведено в порядок."
    window hide

    hide black with dissolve
    $ renpy.pause(1)
    
    window show
    th "Красавчик, теперь все девушки твои."
    "Я подмигнул себе в зеркале."
    vg "Ну, да.{w} Одна уже есть."
    th "А ты у неё хоть спросил?"
    vg "Нет. а зачем? За неё уже всё решёно."
    vg "Как говорится, фабрики — рабочим, приезжим из будущего…"
    window hide

    play sound sfx_open_door_1
    $ renpy.pause(1)
    scene bg int_house_of_gg_day with dissolve 
    show mt normal pioneer at center with dspr
    play sound sfx_close_door_1
    
    window show
    "Дверь в мой домик открылась и, прервав мою великую мысль, в комнату вошла Ольга Дмитриевна."
    mt "Доброе утро, Илья. Ты сегодня поздно."
    nd_il "Доброе утро, Ольга Дмитриевна."
    mt "Давай я тебе расскажу план работы на этот день."

    hide mt with dspr
    show mt smile pioneer far at right with dspr
    
    "Вожатая бесцеремонно заняла место на второй кровати."
    window hide

    $ renpy.pause(1)

    window show
    th "Странно, что она даже ничуть не сердится на мое отсутствие на линейке."
    th "Похоже, у вожатой сегодня хорошее настроение."
    window hide

    $ renpy.pause(1)

    window show
    mt "Сегодня у нас вечером танцы, они обычно через день проходят."
    mt "Можешь даже пригласить кого-нибудь."
    nd_il "Я даже знаю кого."
    window hide

    $ renpy.pause(1)
    show mt laugh pioneer far at right with dspr
    stop music fadeout 3

    window show
    mt "Я тоже знаю."
    ".{w}.{w}."
    th "Пардон, я что, сказал это вслух?"
    window hide

    $ renpy.pause(2)

    window show
    "Я сделал непонимающее выражение лица."
    show mt smile pioneer far at right with dspr
    vg "Доигрался ты, старый дурак."
    nd_il "Ну…"
    
    if d2_dv_night_pristan == False:

        mt "Кстати об этом.{w} Я заметила, что после того как ты приехал, Ульяна начала вести себя немного по-другому."
        "Я отвел взгляд в правый нижний угол.{w} Рассматривать доски на полу мне ещё никогда не было так интересно, как сейчас."
        show mt normal pioneer far at right with dspr
        "Она продолжила."
        mt "…Хорошо, что вы нашли общий язык. Она очень много хулиганила без тебя."
        window hide

        $ renpy.pause(1)

        window show
        th "Надо как-то сменить эту тему..."
    

    elif d2_dv_night_pristan == True:

        mt "Кстати об этом.{w} Я заметила, что после того как ты приехал, Алиса начала вести себя немного по-другому."
        "Я отвел взгляд в правый нижний угол.{w} Рассматривать доски на полу мне ещё никогда не было так интересно, как сейчас."
        show mt normal pioneer far at right with dspr
        "Она продолжила."
        mt "…Хорошо, что вы нашли общий язык. Она очень много хулиганила без тебя."
        th "Надо как-то сменить тему."

    nd_il "Ольга Дмитриевна, так зачем вы всё-таки пришли?"
    mt "Мне интересно, чем занимаются пионеры в свободное время."
    show mt laugh pioneer far at right with dspr
    mt "Некоторые играют на гитаре, а некоторые разглядывают себя в зеркало."
    window hide

    $ renpy.pause(2)
    show mt normal pioneer far at right with dspr
    
    window show
    mt "Ладно, мне нужно ещё Шурика и Электроника проверить."
    window hide

    hide mt with dspr
    $ renpy.pause(1)
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play music music_list["two_glasses_of_melancholy"] fadein 4
    play sound sfx_close_door_1

    window show
    "После этого, Ольга Дмитриевна вышла из домика, оставив меня наедине со своими мыслями."
    window hide

    $ renpy.pause(1)

    window show
    th "Фу-у-ух. Как я мог произнести свои мысли вслух?"
    th "Погодите-ка.{w} Она что, за мной следила?"
    th "Надеюсь, она слышала всё кроме моих криков на свое отражение."
    th "Хотя, если она это слышала, то обязательно упомянула бы об этом в нашем диалоге..."
    window hide
    $ renpy.pause (2)

    stop music fadeout 3

    window show
    "Я лёг на кровать, и принялся обдумывать сон, вспоминая каждые его детали."
    window hide

    show blink
    stop ambience fadeout 2
    $ renpy.pause(2)

    $ nd_change_time('prolog')

    play music ndm_list['mood_worried'] fadein 3

    scene bg city_night_rain
    show prologue_dream
    with dissolve2

    window show
    th "Итак, я выхожу из здания и иду к остановке."
    
    show vsc rf at center behind prologue_dream with dspr
    
    th "На пути меня встречает какой-то парень."
    th "Он рассказывает про лагерь, говорит про мои выборы.{w} Рассказывает про их важность в нём."
    window hide

    $ renpy.pause(1)
    window show
    th "Затем сообщает, что рано или поздно, когда всё станет очень плохо, встретит меня и наведёт на путь истинный."
    window hide

    hide vsc rf with dspr
    
    $ renpy.pause(3, hard=True)
    
    show dv smile coat at center behind prologue_dream with dspr 
    
    $ renpy.pause(1)
    
    window show
    th "Потом появилась взрослая Алиса из Совёнка, отдала потерянный мной телефон, и мы пошли на остановку."
    show black with dissolve
    th "...cели в автобус и поехали куда-то..."
    th "А потом я проснулся..." 
    th "Но перед тем, как проснуться, я уснул в этом автобусе..."
    window hide

    stop music fadeout 2
    $ renpy.pause(2)
    $ nd_change_time('day')

    play ambience ambience_int_cabin_day fadein 4
    scene bg int_house_of_gg_day
    hide blink
    show unblink
    $ renpy.pause(2)
    
    window show
    nd_il "Этот сон наверняка что-то должен значить."
    nd_il "Должен заставить меня что-то вспомнить."
    nd_il "А может это и не сон вовсе, раз в его конце я уснул?"
    window hide

    $ renpy.pause(3, hard=True)

    window show
    "Я ещё немного подумал, а затем решил, что всё это пустая трата драгоценного мне времени{w}, и решил отправиться к моим новым друзьям — Шурику и его коллеге Электронику."
    th "Надеюсь, они сделали мой зарядник."
    th "Туго мне без телефона. Можно было бы \"Сектор Газа\" здешним пионерам включать."
    window hide

    $ renpy.pause(2)
    
    window show
    th "Нет. Пусть лучше последняя мысль останется у меня в мечтах..."
    window hide

    show black with dissolve
    play sound sfx_open_door_1
    stop ambience fadeout 1
    $ renpy.pause(1)

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_close_door_1

    window show
    "Выйдя из свои апартаментов, я сразу направился к зданию общих кружков."
    "Благо до него идти было не далеко."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve2
    $ renpy.pause(0.5)

    window show
    "По дороге я рассматривал вещи, которые мне раньше не бросались в глаза, и просто окружающую природу."
    window hide

    $ renpy.pause(1)

    window show
    th "…Вот зелёная мусорка{w}, а тут на дереве птичка сидит."
    th "А вон вдалеке мне на встречу Лена идёт..."
    window hide

    $ renpy.pause(1)

    show un smile pioneer far at center with dspr

    $ renpy.pause(1)
    hide un with dspr

    window show
    "На половине пути мне встретилась Лена."
    "Этим утром она выглядела воодушевленной чем-то."
    
    show un smile pioneer at center with dspr
    
    un "Доброе утро, Илья."
    nd_il "Привет Лен, куда идёшь?"
    un "В библиотеку, плакат для столовой рисовать, а ты?"
    th "Интересно, что они там нарисуют."
    vg "А сам поучаствовать не хочешь?"
    th "Давай я сначала с первым делом разберусь, а потом возьмусь за второе?"
    nd_il "Я к кибернетикам, у них какое-то изобретение там."
    un "Понятно, ну, я пошла."
    un "Ты можешь присоединиться к нам, если хочешь."
    nd_il "Я подумаю."
    window hide

    $ renpy.pause(1)
    
    hide un with dspr
    
    $ renpy.pause(1)
    
    window show
    "Лена отправилась в сторону библиотеки, а я продолжил свой путь к клубам."
    "Я понимал, что если я в советском лагере на какое-то время{w}, то нужно провести его весело и интересно.{w} Много всего попробовать и много где поучаствовать…"
    "Да, я в Советском лагере.{w} Да, меня занесло сюда непонятно как.{w} Но в любом случае, не нужно окончательно терять из-за этого свой рассудок."
    window hide

    show black with dissolve 
    $ renpy.pause(2)
    scene bg ext_clubs_day with dissolve2

    window show
    "Вот я стою пред металлической дверью кружков."
    window hide

    $ renpy.pause(1)
    
    window show
    vg "Ну, что встал?{w} Входи, уже."
    window hide

    stop ambience fadeout 2
    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    scene bg int_clubs_male_day with dissolve
    play music music_list["smooth_machine"] fadein 3
    play ambience ambience_int_cabin_day fadein 3
    play sound sfx_close_door_1

    window show
    "Я открыл дверь, и пройдя в комнату закрыл её за собой."
    window hide

    $ renpy.pause(2)

    window show
    "На мое удивление, этих двух кибернетиков внутри не было."
    "Вероятно, они были где-то в подсобном помещении."
    "Тишина..."
    window hide

    stop music fadeout 2 
    $ renpy.pause(1)
    with hpunch
    
    window show
    nd_il "Есть кто?!"
    shp "Есть!"
    "Из подсобки послышались тихие шорохи..."
    window hide

    $ renpy.pause(2)
    
    play music music_list["smooth_machine"] fadein 3
    
    show sh normal pioneer far at cright
    show el normal pioneer far at cleft
    with dspr

    window show
    "Подождав меньше минуты, ко мне вышли два гения этого лагеря - Шурик и Электроник." 
    sh "Привет Илья, зачем пришёл?"
    nd_il "Да так, за зарядкой."
    sh "Понимаешь, тут такая проблема..."

    show el grin pioneer far at cleft with dspr
    
    el "Конструкция оказалась сложнее, чем мы думали. Но всё будет готово{w} вечером."
    window hide

    hide el with dspr
    $ renpy.pause(1)
    show el normal pioneer far at cleft with dspr
    
    window show
    "Договорив, Электроник взял со стола прибор, похожий на бомбу, и показал мне."    
    sh "Да, выглядит странно, но мы работаем над этим."
    nd_il "Понятно."
    window hide

    hide el
    hide sh
    with dspr

    $ renpy.pause(1)
    
    window show
    "Краем глаза я заметил доисторический по современным меркам компьютер, заинтересовавший меня своим \"могучим\" видом."
    
    nd_il "А что это там у вас?"
    
    show el grin pioneer far at cleft with dspr
    
    el "Это электронно-вычислительная машина.{w} Настоящее чудо техники."
    el "За ней можно и текст набирать,{w} и расчеты делать,{w} и роботизацией заниматься, и еще много чего."
    el "Нашему лагерю его подарили за то, что в нем есть такие кибернетики, как мы."
    el "Внутри него есть такая штука, как процептор..."
    hide el with dspr
    th "Мда,{w} процептор, вентилятор на нем.{w} Сейчас он мне час всю поднаготную начнёт рассказывать, а у меня ещё дел по горло."
    show el grin pioneer far at cleft with dspr
    el "А передавать он может..."
    nd_il "Слушай, может по существу? А то мне ещё идти нужно..."
    el "Ладно. Смотри."
    hide el with dspr
    
    "Cказал Электроник и, подойдя к компьютеру, нажал на кнопку включения."
    window hide

    $ renpy.pause(1)
    
    window show
    "Спустя несколько секунд высветилась консоль с надписью «MS-DOS»."
    "По моим подсчетам таких компьютеров в восемьдесят седьмом году во всём мире было не более двух ста штук." 
    "Это было любопытно конечно, но как-нибудь в другой раз."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_door_clubs
    
    window show
    nd_il "Ладно, пожалуй, мне нужно идти."
    
    show sh normal pioneer far at cright
    show el normal pioneer far at cleft
    with dspr

    sh "Не забудь вечером зайти."
    nd_il "Постараюсь..."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    
    $ renpy.pause(1)

    show black with dissolve
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    play music ndm_list['mood_funny'] fadein 4
    scene bg ext_clubs_day with dissolve2
    play sound sfx_close_door_1

    $ renpy.pause(1)
    
    window show
    th "Итак, зарядка для аккумулятора моего телефона не готова, значит в домике сидеть будет скучно."
    th "Нужно куда-нибудь сходить..." 
    window hide

    $ renpy.pause(1)

    window show
    th "Может в библиотеку? Как раз посмотрю, что там за плакаты рисуют."
    window hide

    $ renpy.pause(0.5)
    scene bg ext_houses_day with dissolve2
    
    $ renpy.pause(1)

    window show
    "Разглядывая природу лагеря, я заметил, что он как будто подстраивается под моё настроение."
    "Возможно, это не более чем мои додумки или ещё одна моя выдуманная теория."
    "Но всё равно она имеет право на свое существование хотя-бы в моей голове."
    window hide

    $ renpy.pause(1)
    
    show black with dissolve
    $ renpy.pause(2)
    play sound sfx_open_door_1
    scene bg int_library_day with dissolve
    play ambience ambience_library_day fadein 3
    play sound sfx_close_door_1

    window show
    "Открыв дверь, я увидел ту же самую комнату с книжными шкафами, и Женю, сидевшую за столом и что-то читающую."
    th "Может поговорить с ней?"
    "Подумал я, сел на стул перед девушкой и смог разглядеть какую-то энциклопедию насекомых."
    mz "Чего пришёл?"
    nd_il "Да вот, книгу хочу почитать, какую посоветуешь?"
    window hide

    show mz normal glasses pioneer at center with dspr
    stop music fadeout 3
    
    window show
    "Женя подняла голову на меня, её взгляд выражал{w} — ничего.{w} Совсем ничего."
    mz "Не беси."
    
    hide mz with dspr
    
    th "Да что я ей плохого сделал-то?"
    nd_il "Женя, почему ты меня ненавидишь?"
    
    show mz normal glasses pioneer at center with dspr
    
    mz "С чего ты взял?{w} Просто не беси меня и всё."
    window hide

    $ renpy.pause(1)

    window show
    "В этот раз в её взгляде отражалось что-то другое."
    nd_il "В любом случае прости меня."
    window hide

    hide mz with dspr
    
    $ renpy.pause(1)

    window show
    "Я встал со стула и отправился в самый конец библиотеки, где было ещё одно помещение."
    "Женя проводила меня взглядом, и снова продолжила чтение."
    th "А может, отвлекать её было не очень хорошей идеей..."
    window hide

    $ renpy.pause(1)

    show black with dissolve
    stop ambience fadeout 3
    $ renpy.pause(1)
    scene bg int_editorial_day with dissolve2
    play ambience ambience_int_cabin_day fadein 2
    play music ndm_list['mood_funny'] fadein 4
    
    window show
    "Пройдя в небольшую комнатку я увидел Лену, Славю и Машу, рисующих рисунки на тему еды на больших листах бумаги за большим столом."
    "Признаться, у них неплохо получалось."
    
    show un smile pioneer far at left
    show sl smile pioneer far at center
    show mi smile pioneer far at right 
    with dspr
    
    all "Привет!"
    nd_il "Привет всем!"
    nd_il "Плакаты рисуете?"
    sl "Да. Для столовой."
    "Славя показала на ватманы и цветные карандаши, лежавшие на столе."
    nd_il "У вас хорошо получается.{w} Можно присоединиться?"
    
    show sl smile2 pioneer far at center with dspr
    
    sl "Конечно, вот тебе свободный ватман."
    
    hide un
    hide sl
    hide mi
    with dspr

    "Удивительно. Только я появился и предложил свою помощь, как меня тут-же обеспечили большим листом бумаги и цветными карандашами."
    "Я присел за стол и начал рисовать жаренную индейку на блюде."
    window hide

    $ renpy.pause (1)
    
    window show
    th "То чувство, когда рисунок не соответствует действительности."
    vg "Аниме, которые ты смотришь, кстати, тоже не соответствуют действительности."
    th "Что нереалистичного в лысом мужике в костюме супер героя, который одним ударом отправляет своих противников в космос?"
    vg "Например то, что он лысый?"
    window hide

    $ renpy.pause (1)

    show black with dissolve
    
    $ renpy.pause (1)

    window show
    th "Надеюсь я сейчас не вслух сам с собой разговариваю..."
    window hide

    $ renpy.pause (2)
    
    show d3_plakat_1 with dissolve
    window show
    "Вскоре задуманное было нарисовано."
    
    scene bg int_editorial_day with dissolve
    
    "Я показал свой рисунок девушкам."
    
    show sl smile pioneer at left with dspr
    
    sl "Классно получилось."
    
    show mi smile pioneer at right with dspr
    
    mi "Только нужно ещё что-нибудь сверху написать."
    
    hide sl
    hide mi
    with dspr
    
    nd_il "Ладно."
    
    show d3_plakat_1 with dissolve
    
    th "Хм…{w} Что-нибудь написать, но что?"
    "Я принялся перебирать варианты надписи у себя в голове, но не один из них мне не подходил, пока в голову не ударило вдохновение."
    
    show black with dissolve
    
    "Я прислонил карандаш к полотну и аккуратно выводил каждую букву приятным глазу почерком."
    "После этого я еще раз обвёл надпись карандашом и раскрасил каждую строчку под определенный цвет." 
    "Вскоре всё было закончено, я стряхнул пот со лба и прочитал то, что у меня получилось."

    show d3_plakat_2 with dissolve2

    th "Любовь приходит и уходит,"
    th "А кушать хочется всегда."
    th "Из этого всего выходит,"
    th "Что в жизни главное — еда!"

    "По моему, получилось хорошо, а главное - со смыслом."
    scene bg int_editorial_day with dissolve

    show sl laugh pioneer at left with dspr
    sl "Илья, ты настоящий поэт."
    show mi laugh pioneer at right with dspr
    mi "Тебе нужно это показать Ольге Дмитриевне."

    "Лена прикрыла рот рукой и тихо посмеялась."

    show mi smile pioneer at right with dspr
    mi "Всё, девочки, пошли, покажем наши рисунки Ольге Дмитриевне." 

    "...Но Ольга Дмитриевна уже стояла на входе в комнату."

    nd_il "А куда нам идти? Ольга Дмитриевна уже здесь."
    window hide

    $ renpy.pause (0.7)
    hide mi
    hide sl
    with dspr

    show mt smile pioneer far at fright with dspr
    
    $ renpy.pause (0.7)

    show mi smile pioneer far at left
    show sl smile pioneer far at fleft
    show un smile pioneer far at center
    with dspr
    
    window show
    "Девочки повернулись к двери и, увидев Ольгу Дмитриевну, показали ей нарисованные плакаты."
    window hide
    
    $ renpy.pause (2)

    window show
    mi "Ольга Дмитриевна, посмотрите какой плакат у Ильи."
    window hide

    hide mi
    hide sl
    hide un
    with dspr

    hide mt with dspr
    $ renpy.pause (1)
    show mt smile pioneer at center with dspr
    $ renpy.pause (1)
    show mt grin pioneer at center with dspr

    window show
    "Ольга Дмитриевна подошла ко мне и, осмотрев получившейся у меня плакат, посмеялась."
    mt "Илья, это самый оригинальный плакат, который я видела."
    window hide

    hide mt with dspr
    $ renpy.pause (1)
    show mt smile pioneer at center with dspr
    
    window show
    mt "Вы все молодцы!"
    mt "До обеда ещё час, поэтому можете заняться своими делами, а потом мы развесим плакаты, которые вы сделали."
    window hide

    $ renpy.pause (1)

    if usrr >= 3:
        window show
        th "Ну, думаю, теперь можно найти свою подругу Ульяну и зарубиться с ней в футбольчик."
        window hide

        $ renpy.pause (1)

    show black with dissolve

    scene bg int_library_day with dissolve

    window show
    "Библиотекарша снова проводила меня своим фирменным взглядом, а затем продолжила заниматься своими «важными делами»."
    th "Она вообще хоть что-то делает в своей библиотеке?"
    window hide

    stop music fadeout 3
    show black with dissolve2
    play sound sfx_open_door_1
    stop ambience fadeout 3
    play ambience ambience_camp_center_day fadein 3

# Добавить переменную с рутом Алисы в 3-м дне с музыкальным кружком вместо футбольного поля.

    if d2_dv_night_pristan  == False:
        jump d3_us_football_morning_notdream

    if d2_dv_night_pristan  == True:
        jump d3_dv_football_morning_notdream

label d3_dv_football_morning_notdream:

    scene bg ext_library_day with dissolve2
    play sound sfx_close_door_1

    $ renpy.pause (1)

    window show
    "Выйдя из здания, встал вопрос{w} — где мне найти ещё приключений в этом лагере?"
    "Как только я подумал о развлечениях, мне сразу вспомнилась футбольная площадка."
    th "Может на футбольном поле я найду себе интересное занятие?"
    "Я осмотрелся по сторонам, и побежал по своей памяти на футбольное поле..."
    window hide

    show black with dissolve
    $ renpy.pause(1)

    show black with dissolve2
    play sound_loop sfx_run_forest fadein 2

    window show
    "Я бежал через медпункт, площадь, столовую и склад{w}, пока не показалось здание со спортзалом."
    window hide

    jump d3_football_morning_notdream

label d3_us_football_morning_notdream:

    scene bg ext_library_day with dissolve2
    $ renpy.pause (1)
    
    window show
    "Выйдя из здания, встал вопрос{w} — где мне искать Ульяну?"
    th "А вот и карта пригодилась."
    "Подумав о карте, я полез искать её в карманах, но они оказались пустыми..."
    th "Потерял?{w} Но где?" 
    th "Ну и ладно.{w} Придётся мыслить логически."
    window hide

    $ renpy.pause(1)
    
    window show
    th "В музыкальном клубе Ульяны точно не будет."
    th "На сцене — навряд ли."
    th "В клубах — только что там был..."
    th "Может она сейчас в футбол играет?"
    window hide

    $ renpy.pause (2)
    
    window show
    "Я осмотрелся по сторонам, и побежал по своей памяти на футбольное поле..."
    
    show black with dissolve2
    play sound_loop sfx_run_forest fadein 2

    "Я бежал через медпункт, площадь, столовую и склад{w}, пока не показалось здание со спортзалом."
    window hide

    jump d3_football_morning_notdream

label d3_football_morning_notdream:

    $ renpy.pause (1)
    stop sound_loop fadeout 1
    $ renpy.pause (1)
    scene bg ext_playground_day with dissolve2
    play ambience ambience_soccer_play_background fadein 3
    play music ndm_list['mood_run'] fadein 3

    window show
    "Зайдя за него к футбольному полю, я увидел настоящий матч пять на пять."
    "Правда, болельщиков не было, и я оказался первым наблюдателем."

    "Среди игроков была и Ульяна."
    window hide

    show cg us_fb_day_sport with dissolve

    $ set_mode_nvl()
    
    window show
    "Видимо она играла «в одиночку»."

    "Обходя мелких пацанов с других отрядов{w}, она побежала к воротам врага, и сделав пару финтов с обманным манёвром, забила мяч в ворота противника."
    "Видимо наши с ней тренировки дали о себе знать."
    window hide

    $ set_mode_adv()

    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_playground_day with dissolve

    window show
    "После своего гола она обратила на меня внимание и подбежала ко мне."
    window hide

    $ renpy.pause(1)
    show us grin sport far at center with dspr
    hide us
    show us grin sport at center with dspr
    
    if usrr >= 3:
        
        window show
        us "Илья! Ты видел, как я их?"
        "Запыхавшись, выговаривала Ульяна." 
        "Было видно, что она устала."
        nd_il "Да!{w} Это было великолепно!"
        "Я не стеснялся показывать свое восхищение."
        "Её рассказы о выигрышах в сухую после этого гола казались более чем правдоподобными."
        us "Илья, а зачем ты сюда пришёл?"
        nd_il "К тебе пришёл.{w} Поиграть в футбол."
        show us shy sport at center with dspr
        us "К-ко мне?"
        nd_il "Ну, да."
        window hide

        $ renpy.pause(1)

        window show
        "Видимо, я не на шутку смутил её.{w} Это было понятно по её вмиг порозовевшим щекам."
        nd_il "Просто у тебя есть мячик, а я знаю, что ты любишь футбол, поэтому пришёл сюда поиграть с тобой."
        us "Ко мне обычно приходят только для того, чтобы заставить работать или поругать за какую-нибудь мою провинность."
        window hide

        $ renpy.pause(1)
        
        window show
        us "Ты принят в мою команду, пошли."
        window hide

    elif usrr < 3:

        window show
        us "О, привет. Будешь в мяч играть?"
        "Запыхавшись, выговаривала Ульяна."
        "По её выражению лица было видно, что она устала."
        nd_il "А ты не хочешь отдохнуть?"
        us "Не-а."

        hide us with dspr

        "Я не понимал, как она не устает от всех этих пробежек, игр и шалостей."
        "Казалось, что у неё всегда с собой какие-нибудь батарейки, которые легко её подзарядят."
        "Может, конечно, она пила энергетики, но навряд ли в лагере найдётся что-то подобное.{w} А если и найдётся - то навряд-ли она почувствует от них какой-то эффект."
        "Она итак слишком активная без кофеина с таурином."
        window hide

        $ renpy.pause(1)
        show us grin sport at center with dspr

        window show
        us "Так ты будешь играть?"
        nd_il "Да, почему бы и нет."

        us "Тогда ты принят в мою команду, пошли."
        window hide

    else:

        window show
        us "О, привет. Будешь в мяч играть?"
        "Запыхавшись, выговаривала Ульяна."
        "По её выражению лица было видно, что она устала."
        nd_il "А ты не хочешь отдохнуть?"
        us "Не-а."

        hide us with dspr

        "Я не понимал, как она не устает от всех этих пробежек, игр и шалостей."
        "Казалось, что у неё всегда с собой какие-нибудь батарейки, которые легко её подзарядят."
        "Может, конечно, она пила энергетики, но навряд ли в лагере найдётся что-то подобное.{w} А если и найдётся - то навряд-ли она почувствует от них какой-то эффект."
        "Она итак слишком активная без кофеина с таурином."
        window hide

        $ renpy.pause(1)
        show us grin sport at center with dspr

        window show
        us "Так ты будешь играть?"
        window hide

        $ renpy.pause(1)
        
        window show
        nd_il "Да, почему бы и нет."
        us "Тогда ты принят в мою команду, пошли."
        window hide

    hide us with dspr
    $ renpy.pause(1)

    parr "Эй, Ульяна, так нечестно."
    nd_il "Давайте четыре против двух."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ульяна, прищурившись, посмотрела на меня." 
    "В её взгляде читались решимость и дух соперничества."
    
    hide us with dspr

    us "Давайте!"
    us "Итак, вы четверо идите на запасную скамейку, а мы с Ильёй попробуем вдвоём."
    th "А на что я, собственно, подписался?"
    th "Ладно, если играть, так по крупному."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "На что играем?"
    window hide

    $ renpy.pause(1)
    
    window show
    us "Давайте на шоколадки, которые сегодня дают после обеда!"
    "Противники начали шептаться."
    window hide

    $ renpy.pause(3, hard=True)
    
    window show
    "После коротких переговоров, самый старший заявил."
    parr "Договорились."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ульяна и капитан вражеской команды сошлись на середине поля и пожали друг другу руки."
    stop ambience fadeout 3
    th "Изи шоколадки."
    
    play music ndm_list["mood_run"] fadein 3
    play ambience ambience_soccer_play_background fadein 3
    
    "После этого сразу начался матч."
    "Четыре против двоих, не считая вратарей обеих команд."
    window hide

    $ renpy.pause(1,hard=True)

    show cg us_fb_day_sport with dissolve

    $ set_mode_nvl()
    window show
    "Ульяна быстро отобрала мяч, и побежала к вражеским воротам{w}, но её сразу же перехватили."
    "Я быстро побежал наперерез, отобрал мяч, и отдал пас Ульяне."
    "Она подбежала к воротам и попыталась забить мяч{w}, но тщетно.{w} Штанга вражеских ворот оказалась крепче."
    "После этого волна ребят с мячом побежала к нашим воротам, но Ульяна быстро отобрала мяч и отдала мне пас."
    "Я подбежал к воротам и{w}, сделав простой обманный манёвр{w}, забил мяч в ворота."
    window hide

    hide cg us_fb_day_sport with dissolve

    $ set_mode_adv()

    window show
    "Вдруг послышался мужской голос вне футбольного поля."
    muz "Молодцом, Илья."
    "Я повернулся и увидел Евгения Петровича со свистком на шее."
    th "Плюс реп."
    vg "Ага, четыреста часов, наигранных в фифу не прошли тщетно."
    th "Ну что-ж, посмотрим как дальше дело пойдет..."
    
    show us laugh sport at center with dspr 
    
    us "Илья, это было круто!"
    window hide

    hide us with dspr

    $ renpy.pause(1, hard=True)

    window show
    "Крикнула мне Ульяна, и подбежав прыгнула на меня."
    "Я поймал её руками и поднял вверх."

    parr "А вы не радуйтесь, мы просто вам поддались."
    window hide

    $ renpy.pause(1)
    play sound nds_list['whistle']

    window show
    "Евгений Петрович свистнул в свисток, и начался второй тайм."
    th "Сейчас ещё один гол будет."
    vg "Ловлю на слове."
    window hide

    $ set_mode_nvl()

    window show
    "Ульяна сразу побежала на мяч, а я сопровождал её рядом."
    "Когда девушку окружали игроки, она отдавала мяч мне, а когда окружали меня — я отдавал ей{w}, обходя соперников.{w} Но у них всё равно получилось отобрать мяч." 
    "Ульяна вновь рванула на отбор мяча."
    window hide

    $ set_mode_adv()

    window show
    th "И как она не устаёт?"
    window hide

    $ set_mode_nvl()

    window show
    "Отобрав мяч, Ульяна снова отдала пас мне."
    "Работая вдвоем, мы отдавали пасы друг другу, запутывая противников и вратаря." 
    window hide

    show black with dissolve
    show cg us_fb_day_sport with dissolve
    
    window show
    "Отдав очередной пас Ульяне, она сделала какой-то финт и очень сильно ударила мяч в ворота." 
    "Если бы вратарь не отошёл, у него была бы травма. Либо физическая, либо психологическая, либо всё вместе..."
    window hide

    $ set_mode_adv()
    
    hide cg us_fb_day_sport with dissolve

    $ renpy.pause(2)

    window show
    "Ульяна закричала от радости и запрыгнула мне на шею, и я пробежался с ней по полю."
    window hide

    $ renpy.pause(1)
    show ext_playground_day with dissolve

    play sound nds_list['applause1'] fadein 2
    
    window show
    "С трибун послышались овации."
    "Я повернулся, и увидел Ольгу Дмитриевну вместе со Славей, Леной и Мику."
    "Они помахали мне и я, с Ульяной на шее, подбежал к ним."
    window hide

    stop sound fadeout 2

    show mt smile pioneer at right
    show sl laugh pioneer at center
    show mi shocked pioneer at left
    with dspr

    window show
    sl "Молодцы! Неразделимая компания!"
    window hide

    hide mt
    hide sl
    hide mi
    with dspr

    stop music fadeout 3

    window show
    th "Как же я устал..."
    window hide

    $ renpy.pause(1)

    window show
    "Ульяна слезла с меня, и мы сели на скамейку."
    nd_il "К-к-круто мы…"
    us "Ага..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    hide black with dissolve

    window show
    "Ульяна присела на скамейку, облокотившись своим телом мне на плечо."
    us "Давай ещё раз."
    nd_il "Ты устала, да и я тоже.{w} Давай сделаем небольшой...{w} Перерыв..."
    window hide

    $ renpy.pause(1)
    show us sad sport at center with dspr

    window show
    "Ульяна посмотрела на меня своими милыми, голубыми, как небо глазами."
    "Мне кажется, или она просто строит мне щенячие глазки, чтобы заставить побегать меня ещё пару кругов на поле?" 
    "Сколько себя помню, я никогда на это не вёлся.{w} Но просто из-за того, чтобы она не обижалась..."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Ладно.{w} Только не долго."

    show us grin sport at center with dspr

    us "Ура! Побежали!"

    hide us with dspr

    "Ульяна побежала снова на поле, а мне пришлось идти за ней."
    window hide

    play music ndm_list['mood_play'] fadein 3

    $ set_mode_nvl()

    window show
    "Мы сыграли еще пару раундов, но тщетно.{w} Наши противники как-будто собрались, и легко забили нам два гола."
    "Их количество теперь действительно играло роль."
    "Но сдаваться и тем более уходить никто в нашей команде не собирался."
    window hide

    $ set_mode_adv()


    $ renpy.pause(2)

    window show
    "На зрительских местах собралась уже уйма народу, чтобы посмотреть захватывающий матч."    
    window hide

    $ renpy.pause(2)

    window show
    "Спустя минуту Евгений Петрович огласил результаты предыдущих раундов."
    window hide

    stop music fadeout 2

    window show
    fiz "В прошлом раунде команды сравняли счет.{w} Текущий: два - два.{w} Этот раунд станет решающим."

    $ renpy.pause(1)

    play sound nds_list['whistle'] 
    play music ndm_list['mood_fight_1'] fadein 3
    
    "Как только прозвучал громкий свисток, началась решающая игра."
    window hide

    $ set_mode_nvl()

    window show
    "Противники казались намного сильнее. Возможно, из-за того, что я устал.{w} Мы с Ульяной защищали свои ворота от нападения, а затем резко перешли в атаку."
    "Противники попросту не успели ничего понять." 
    "Мы бежали с Ульяной до вражеских ворот."
    "Девушка отдала мне пас, и я, сделав пару обманных манёвров, пнул мяч в ворота{w}, но попал в штангу." 
    "Мяч отскочил от штанги, и прилетел к Ульяне.{w} Она пафосно отбила его головой, но назло опять в штангу." 
    "В этот раз мяч снова попал к нашим противникам, которые резко побежали к нашим воротам.{w} Благо наш вратарь был не пальцем деланный."
    "Он схватил мяч двумя руками, и отдал пас навесом через всю толпу нам с Ульяной."
    
    show black with dissolve
    show cg us_fb_day_sport with flash

    "Мы обошли двух защитников{w}, приблизились к воротам, пас, ещё пас, обманный манёвр{w}, пас пяткой Ульяне{w}, удар и…{w} ГО-О-О-О-Л!"
    window hide

    $ set_mode_adv()

    hide cg us_fb_day_sport with dissolve
    stop music fadeout 3

    window show
    us "Ура-а-а!"
    th "Кажется, я сейчас помру."
    us "Илья, мы это сделали!"
    nd_il "Да…"
    "Это слово далось моим легким необыкновенно непосильным трудом."
    window hide

    stop ambience fadeout 3

    with vpunch
    play sound sfx_bush_body_fall
    with flash
    play sound_loop sfx_head_heartbeat fadein 2

    window show
    "Пройдя немного, мои ноги подкосились, и я упал на траву."
    window hide

    $ renpy.pause(1)
    
    window show
    us "Илья, всё хорошо?"
    nd_il "Нор…{w} Норм… мально…"
    "Ко мне подбежали девушки, включая Ольгу Дмитриевну и Евгения Петровича."
    mt "Илья, всё нормально, врача?"
    nd_il "Не над…{w} Всё хорош-о…"
    window hide

    $ renpy.pause(1)
    
    window show
    "Я попытался встать, но тщетно.{w} Ноги совсем не хотели меня слушать.{w} Если честно, то я вообще не верил в их присутствие."
    us "Илья! Вставай, дурак!"
    "Закричала Ульяна и начала трясти меня."
    "Признаться, это прибавило мне немного сил."
    window hide

    stop sound_loop fadeout 3
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    hide black with dissolve2

    window show
    "Я принял удачную попытку встать, и медленно пошёл на скамейку запасных."
    "Там-то меня уже ждала Алиса..."
    "Я лёг на скамейку и начал глубоко дышать."

    if d2_dv_night_pristan == False: 
        
        show dv grin pioneer at right with dspr
        
        dv "Уже выдохся?{w} Слабачок.{w} Но играли вы с Ульяной нормально."
        
        show us dontlike sport at left with dspr
        
        us "Много ты понимаешь в футболе... Он нормально играл..."
        window hide

        hide dv
        hide us
        with dspr

        $ renpy.pause(3, hard=True)

        window show
        "Зрители начали расходиться, пока Алиса и Ульяна о чём-то спорили."
        th "Надеюсь, шоколадки я заслужил. Эх…"
        th "Мне нужно, наверное, начать здоровый образ жизни, перестать есть в заведениях быстрого питания, и заказывать пиццу на дом."
        th "На вырученные деньги со следующего фриланса обязательно схожу в какой-нибудь спортзал..."

        show dv grin pioneer at right with dspr
        
        dv "…Ладно, разбирайтесь сами."
        
        hide dv with dspr
        
        "Демонстративно заявила Алиса и... ушла, оставив нас с Ульяной наедине."
        window hide

        $ renpy.pause(2)

        window show
        us "Прости за дурака. Я переволновалась."
        "Сказала Ульяна и обняла мою руку."
        window hide

        $ renpy.pause(1, hard=True)

        window show
        "Ольга Дмитриевна посмотрела на меня издалека утвердительным взглядом."
        window hide

        $ renpy.pause(1)
        play music ndm_list['RF_memory_1'] fadein 4
        $ renpy.pause(1)

        window show
        "Снова молчание.{w} Я ценил каждую секунду рядом с этой девушкой."
        "Почему мне нравятся эти секунды рядом с ней? Какая на это причина?"
        "Ответ на мои вопросы со слов психолога из моего сна - какая-то детская травма."
        "Травма, которую я, почему-то, не запомнил..."
        window hide

        $ renpy.pause(1)

        window show
        "И вообще, что за бред?{w} Я что, в какой-то книге, чтобы всё забыть?{w} Не было такого никогда."
        "Я всегда был таким, какой я сейчас."
        "Никаких несбывшихся желаний, ничего."
        "Всё, к чему я стремился, это сбежать от общества, запереться в квартире и работать в свое удовольствие."
        "И я этого достиг.{w} Теперь я живу от зарплаты до зарплаты."
        window hide

        $ renpy.pause(1)
        
        window show
        "Да, все рассказы о фрилансе и программировании, как о полноценной работе, были полным обманом."
        "Можно работать когда хочешь и где хочешь{w} - враньё."
        "Здесь ты выживаешь, а не работаешь."
        window hide

        $ renpy.pause(1)
        
        window show
        "А у моей подруги, сидящей справа от меня - беззаботное детство с футболом, друзьями и пакостями в лагерях."
        "Как и у меня сейчас..."
        window hide

        $ renpy.pause(1)

        if nir >= 3:
            
            jump nd_y_men9_kon4ilicb_idei

        else:

            jump us_road_nd_canirunawayplease



    elif d2_dv_night_pristan == True:

        show us normal pioneer at left with dspr
        show dv surprise pioneer at center with dspr

        window show
        dv "Илья, точно всё нормально?"
        nd_il "Да.{w} Пойдёт."
        window hide

        show dv guilty pioneer at center with dspr
        $ renpy.pause(1)

        window show
        dv "Ты прости конечно, но мы же вчера договаривались..."
        window hide

        $ renpy.pause(1)

        window show
        nd_il "А, да, точно.{w} Я вообще сначала тебя искал..."
        show dv smile pioneer at center with dspr
        dv "Да. И поэтому ты пошёл на футбольное поле."
        hide dv with dspr
        nd_il "Ну ладно, забыл я, что тут такого."
        dv "Да ничего..."
        window hide

        $ renpy.pause(1)

        hide us with dspr
        
        window show
        "Ульяна оставила нас с Алисой."
        window hide

        $ renpy.pause(3, hard=True)
        
        window show
        nd_il "Ну так это... Когда мы пойдем гитарный кружок возрождать?"

        show dv normal pioneer at center with dspr

        dv "Скоро. После обеда пойдем и у вожатой спросим."
        nd_il "Отлично."
        window hide

        $ renpy.pause(2)

        play music ndm_list['RF_memory_1'] fadein 3

        show dv normal pioneer at center with dspr

        window show
        dv "Из какого города ты сюда приехал?"
        "Вдруг поинтересовалась Алиса."
        nd_il "Из Краснодара. Красивый город."
        dv "Знаю. Мы проезжали его, когда были в автобусе."

        show dv smile pioneer at center with dspr
        
        dv "Я, вот, из Ленинграда, но этот город мне не очень нравится{w} Вообще, я переехала в него с родителями из посёлка два года назад."
        dv "Хочу смотаться куда-нибудь обратно на юг."
        nd_il "Тогда тебе понравится Краснодар."
        window hide

        $ renpy.pause(1)
        
        window show
        dv "Ладно, давай поговорим об интересах."
        nd_il "Я фрилансер."
        vg "Звучит как причина, почему тебя нужно избегать."

        show dv surprise pioneer at center with dspr
        
        dv "Кто?"
        nd_il "Ну...{w} Человек который занимается своим любимым делом и зарабатывает на этом."
        vg "А вот это уже звучит как тост."
        
        show dv smile pioneer at center with dspr
        
        dv "Ух-ты. А я всегда хотела создать какую-нибудь музыкальную рок-группу, стать успешной гитаристкой, ездить по разным городам и давать концерты."

        show dv grin pioneer at center with dspr
        
        dv "Как только у меня будет концерт в Краснодаре, я обязательно тебя найду."
        nd_il "Да я и сам не против на него прийти."
        dv "Если повезет, сможешь и поучаствовать."

        stop music fadeout 3

        hide dv with dspr
        
        play sound sfx_dinner_horn_processed

        "В этот момент из динамика послышалась музыка, зовущая пионеров в столовую."
        "Мы с Алисой встали со скамейки и пошли на обед, который обещал быть сытным и вкусным, как и в прошлые разы."
        window hide

        stop ambience fadeout 3
        show black with dissolve2
        $ renpy.pause(3, hard=True)
        play ambience ambience_camp_center_day fadein 3

        jump stol_d3_day_us_dv
        


label nd_y_men9_kon4ilicb_idei:

    window show
    "Кстати, а где она?"
    "Я оглянулся, но Ульяны на своем месте я не увидел."
    th "Ладно, может переодеваться пошла."
    window hide

    $ renpy.pause(1)
    play sound sfx_dinner_horn_processed
    $ renpy.pause(2, hard=True)

    window show
    th "А вот и обед. Пойду к столовой. Встретимся с Ульяной там."
    th "Она наверняка придёт за своим призом."
    "Подумал я, и отправился к зданию столовой."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(3, hard=True)
    play ambience ambience_camp_center_day fadein 3

    jump stol_d3_day_us_dv

label us_road_nd_canirunawayplease:

    window show
    "Мне вдруг показалось, что хоть я в лагере уже третий день, но Ульяну знаю не достаточно хорошо."
    "Лишь пара фактов о ней не давали полной картины."
    "И мне, естественно, захотелось узнать её получше."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "А ты из какого города?"
    show us normal sport at right with dspr
    us "Я из Пятигорска сюда приехала."
    window hide

    $ renpy.pause(1)
        
    window show
    us "А ты?"
    hide us with dspr
    nd_il "Я из Краснодара.{w} Красивый город.{w} Ты была там когда-нибудь?"
    show us smile sport at right with dspr
    us "Да. У меня там бабушка работает."
    nd_il "Серьезно? И кем?"
    show us grin sport at right with dspr
    us "Она тренер. Тренирует футболистов."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Может, ты тоже хочешь стать тренером?"
    hide us with dspr
    "Ульяна задумалась..."
    window hide

    $ renpy.pause(2, hard=True)
        
    show us normal sport at right with dspr
        
    window show
    us "Нет."
    us "Хочу стать врачом."
    us "А ты, наверное, как и все мальчики, космонавтом."
    nd_il "Не угадала. Я был бы программистом."
    show us surp1 sport at right with dspr
    us "Паграм… кем?"
    hide us with dspr
    th "Как бы ей объяснить..."
    window hide

    $ renpy.pause(1)
        
    window show 
    nd_il "Программист - это человек, который хорошо разбирается в новых технологиях."
    show us normal sport at right with dspr
    us "Как кибернетики что ли?"
    nd_il "Нет, эти совсем скучные."
    show us smile sport at right with dspr
    "На лице Ульяны проскочила улыбка."
    window hide

    $ renpy.pause(1)
    hide us with dspr
    stop music fadeout 4
    $ renpy.pause(2, hard=True)
    play sound sfx_dinner_horn_processed
    $ renpy.pause(1)

    window show
    "Я было хотел продолжить разговор о скучных кибернетиках, как вдруг динамик позвал пионеров в столовую."
    th "Сейчас там такая куча будет... Ни проехать ни пройти."
    th "Нужно поторопиться."
    nd_il "Ульяна, пошли на обед..."
    window hide

    $ renpy.pause(1)
        
    window show
    "Сказал я, но поздно заметил, как Ульяна уже махала мне из-за угла спортивного здания." 
    "Бегать после футбола, честно говоря, совсем не хотелось, поэтому я решил обойтись только быстрым шагом."
    window hide
        
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(3, hard=True)
    play ambience ambience_camp_center_day fadein 3
        
    jump stol_d3_day_us_dv

    
label stol_d3_day_us_dv:

    $ renpy.pause(1)
    scene bg ext_dining_hall_away_day with dissolve2
    $ renpy.pause(1)

    window show
    "Спустя пять минут ходьбы, на горизонте виднелась столовая."
    window hide

    scene black with dissolve
    $ renpy.pause(0.5)
    scene bg ext_dining_hall_near_day with dissolve
    
    window show
    "Лагерь был пуст, потому что все пионеры уже сидели внутри этого большого здания."
    "Я последовал их примеру и тоже поспешил войти внутрь..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    play ambience ambience_dining_hall_full fadein 2
    $ renpy.pause(1)
    play sound sfx_close_door_1

    $ renpy.pause(1)
    scene bg int_dining_hall_people_day with dissolve2

    window show
    "Зайдя в столовую, в глаза бросился плов с кусочками отварной курицы, лежавший в тарелках у пионеров."
    "После увиденного, во мне тут-же проснулся зверский аппетит." 
    "Тем более, после футбола, такой обед был никак иначе, как в тему." 
    window hide

    $ renpy.pause(1)

    if d2_dv_night_pristan == False:
        jump stol_d3_day_us

    elif d2_dv_night_pristan == True:
        jump stol_d3_day_dv


label stol_d3_day_dv:

    window show
    "Мы с Алисой взяли порции и найдя пару свободных мест за столом, где сидела Славя, поспешили туда."
    window hide

    show sl smile pioneer at left with dspr
    $ renpy.pause(0.8)

    show dv normal pioneer at right with dspr

    window show
    nd_il "Приятного аппетита, Славь."
    sl "Взаимно."
    window hide

    hide dv
    hide sl
    with dspr

    window show
    "Пожелав друг другу приятного аппетита, мы принялись за еду."
    th "Ммм… Вкусно всё-таки. Этот пионерлагерь какой-то особенный."
    
    show sl normal pioneer at left with dspr
    
    sl "Илья, я знаю, что уже достала с этой уборкой, но можешь после полдника прийти в библиотеку?{w} Там нужно книжки по полкам разложить."
    
    show dv normal pioneer at right with dspr

    dv "Слушай, Славяна. Мы с Ильёй будем заниматься важным делом. И ему будет не до ваших книг."

    show sl serious pioneer at left with dspr

    sl "А ты у него хоть спросила, до чего ему будет дело, а до чего нет?"
    nd_il "Ладно, Славь, я приду и помогу."
    "Попытался я остановить зарождающуюся ссору."
    
    hide dv with dspr
    show sl smile pioneer at left with dspr
    
    sl "Спасибо Илья."

    hide sl with dspr
    show us grin pioneer at right with dspr
    
    "Наверное, она хотела продолжить разговор, но к нашему столу подошла Ульяна и протянула мне три маленькие шоколадки."
    us "Это тебе, заслужил."
    nd_il "Благодарю."
    us "Пожалуйста."
    "Я взял шоколадки и положил на стол рядом с тарелкой."

    hide us with dspr
    
    "Ульяна осмотрела стол,{w} посмотрела сначала на меня, потом на Алису,{w} а затем молча ушла."

    nd_il "Интересно, что это с ней?"

    dv "Я потом поговорю с ней. А сейчас допивай чай, и мы идем до вожатой."
    window hide

    $ renpy.pause(2)

    window show
    "Чай мне дался быстро.{w} Мы втроем одновременно встали из-за стола, и я, отнеся поднос, вместе с Алисой вышел на улицу..."
    window hide

    show black with dissolve 
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve2
    play sound sfx_close_door_1  

    jump guitar_club_dv_d3_rt


label stol_d3_day_us:

    window show
    "Я взял порцию, и оглядев столовую увидел единственное место рядом с девушкой под именем Славя."
    window hide

    $ renpy.pause(1)

    window show
    "Подойдя к ней, я сел на стул напротив и пожелал девушке за столом приятного аппетита."

    show sl smile pioneer at center with dspr

    sl "Спасибо. Взаимно."
    window hide

    hide sl with dspr
    $ renpy.pause(1)

    window show
    th "Ммм… Как всё-таки вкусно тут готовят."
    th "Уверен, не в каждом пионерлагере всё настолько щедро и богато."
    th "Хотя нет, не уверен."
    th "Надо Ульяну спросить, во всех ли лагерях так готовят."
    window hide

    $ renpy.pause(2, hard=True)

    show sl normal pioneer at center with dspr

    window show
    sl "Илья, ты можешь вечером, после полдника, прийти в библиотеку?"
    sl "Там нужно новые книжки по полкам разложить."
    sl "А потом можешь идти, куда хочешь."
    window hide

    $ renpy.pause(1)

    window show
    "Я не очень любил уборку, особенно в таком скучном месте, как библиотека.{w} Но чем мне ещё тут заниматься?"
    "Да и Ольга Дмитриевна всё равно бы запрягла." 
    "А потом можно опять в футбол поиграть с Ульяной..."
    window show

    $ renpy.pause(1, hard=True)
    
    window show
    "Кстати, а вот и она."
    nd_il "Ладно.{w} Уберусь."
    nd_il "Всё равно, вроде как, провинился перед тобой в первый день."
    
    show sl smile pioneer at center with dspr
    
    sl "Я уже забыла. Ничего страшного."
    window hide

    hide sl with dspr

    $ renpy.pause(1)
    
    window show
    "Наверное, она хотела сказать ещё что-то, но к нашему столу подошла Ульяна и протянула мне три маленькие шоколадки."

    show us grin pioneer at right with dspr
    
    us "Это тебе, напарник, заслужил."
    "Она стояла передо мной в пионерской форме.{w} Скорость её переодевания меня уже не удивляла так, как удивляла в первые дни."
    "Я взял шоколадки и положил их на стол рядом со своей тарелкой."
    window hide

    $ renpy.pause(1)
    hide us with dspr
    $ renpy.pause(1)
    
    window show
    "Спустя пару секунд, Ульяна уже сидела на стуле рядом со Славей."
    us "О чём разговариваете?"
    nd_il "Об уборке в библиотеке после полдника."
    nd_il "Мне ещё плакаты, наверное, развешивать."
    
    show sl laugh pioneer at center with dspr
    
    sl "Верно."
    hide sl with dspr
    show us upset pioneer at right with dspr
    
    us "Скукоти-и-ища."
    nd_il "А после этого можем во что-нибудь в лагере поиграть."
    
    show us normal pioneer at right with dspr
    
    us "Ты, наверное, долго будешь."
    nd_il "А ты помоги товарищу, чтобы быстрее было."
    window hide

    $ renpy.pause(1)
    hide us with dspr

    window show
    "Я замер, в ожидании реакции Ульяны."
    "Я предчувствовал, как она скажет что-то по типу \"Не, сам как-нибудь\"."
    window hide

    $ renpy.pause(1, hard=True)
    
    show us grin pioneer at right with dspr

    window show
    us "Ладно." 
    th "Что?"
    us "Давай доедай, и побежали быстрей."
    window hide

    hide us with dspr

    show sl smile2 pioneer at center with dspr
    $ renpy.pause(1)
    hide sl with dspr
    
    window show
    "Славя, хихикнув, встала из-за стола и пошла относить за собой тарелки."
    us "Быстрей! Быстрей! Быстрей!"
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    "Я быстро доел порцию, и принялся за чай."
    us "Пей! Пей! Пей!"
    window show
    
    $ renpy.pause(1)
    
    window show
    "Я пил чай из своей кружки, попутно закусывая их маленькими шоколадками."
    "Они были настолько маленькими, что я оказался способным съесть их за десять секунд в один присест, и продолжить пить чай."
    "Вот тогда за столом я и узнал, что могу очень быстро пить."
    th "Новая мутация, вызванная перемещением во времени."
    th "Забавно."
    window hide

    $ renpy.pause(2)
    
    window show
    us "Молодец." 
    us "Всё, побежали быстрее."
    "Ульяна взяла меня за руку потащила на улицу."
    nd_il "А тарелки убрать?"
    us "Кто-нибудь другой уберет, а мы торопимся."
    window hide

    stop ambience fadeout 2
    show black with dissolve 
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve2
    play sound sfx_close_door_1 

    jump plakats_us_d3_rt

label guitar_club_dv_d3_rt:

    show un smile pioneer at fleft
    show mi smile pioneer at right
    show sl smile pioneer at left
    show mt normal pioneer at center
    with dspr

    window show
    mi "А вот и Илья с Алисой."

    show dv normal pioneer at fright with dspr

    dv "Ага, привет."
    dv "Ольга Дмитриевна, мы с Ильёй хотим вновь восстановить клуб игры на электрогитаре."

    hide un
    hide mi
    hide sl
    with dspr

    show dv normal pioneer at right with dspr
    "Ольга Дмитриевна задумалась. Славя, Маша и Лена начали шептаться."
    window hide

    $ renpy.pause(1)

    window show
    dv "Нам нужно свободное здание для него. Например - склад."
    mt "Но Алиса, я не могу отдать вам наш склад.{w} Да и, думаю, вы не захотите всё из него вытаскивать и перетаскивать."
    "Алиса замолчала."
    nd_il "Можно тогда какое-нибудь другое здание?{w} Не склад."
    "Ольга Дмитриевна вновь сделала вдумчивое выражение лица."
    window hide

    $ renpy.pause(1)

    window show
    mt "Вы можете оборудовать сцену под ваш клуб.{w} Никто пока не собирается ничего с ней делать."
    window hide

    $ renpy.pause(0.8)
    show dv smile pioneer at right with dspr
    
    window show
    "Алиса повеселела."
    dv "Спасибо Ольга Дмитриевна. Можно, мы займёмся оборудованием сцены прямо сейчас?"
    mt "Алиса, сейчас Илья должен нам помогать расклеивать плакаты."
    "В этот момент во мне проснулся навык убеждения."
    nd_il "Ольга Дмитриевна, я уже договорился Славе помочь в библиотеке после полдника.{w} Я как только освобожусь - сразу приду."
    window hide

    $ renpy.pause(1)

    window show
    mt "Ладно. Можете идти."
    nd_il "Спасибо."
    dv "Спасибо."
    "Сказали мы вместе с Алисой, и быстро пошли в сторону сцены, пока вожатая не передумала."
    window hide

    show black with dissolve

    $ renpy.pause(1)

    scene bg ext_houses_day with dissolve

    window show
    th "Сделать гитарный клуб под открытым небом - хорошая, конечно, идея.{w} Но если бы нам разрешили использовать склад для наших целей, было бы лучше,{w} хоть и пришлось бы потратить время на уборку."
    th "Хотя и со сценой заморочек должно быть не меньше."
    window hide

    show black with dissolve2

    $ renpy.pause(1)

    play music ndm_list['jzone'] fadein 3

    scene bg ext_stage_big_day with dissolve2
    
    window show
    "Подойдя к сцене, мы забрались на неё и начали осматриваться..."
    window hide

    $ renpy.pause(1)

    window show
    dv "Как-то тут пусто для клуба... "
    nd_il "А ты уверена, что нам нужен этот клуб?"
    dv "Ну конечно! Это же моя мечта."
    window hide

    show black with dissolve 
    stop ambience fadeout 2
    $ renpy.pause(2)
    hide black with dissolve
    play ambience ambience_camp_center_day fadein 3

    window show
    "Спустя некоторое время мы начали предлагать свои идеи."
    dv "Вот тут надо до блеска убрать..."
    nd_il "А тут какой-нибудь плакат наклеить..."
    dv "Здесь стойку для электрогитар поставить..."
    nd_il "За стойкой надо в музклуб сходить."
    dv "Большой плакат в библиотеке нарисуем. Но сначала возьмем покрывала и сошьем вместе."
    nd_il "А это легально?"
    dv "У меня в этом лагере всё легально."
    window hide

    $ renpy.pause(1)

    window show
    "Вскоре мы договорились и распределили работу."
    "Я иду за электрогитарами и стойкой для них,{w} а Алиса убирается на сцене и моет пол."
    "А потом мы пойдем за покрывалами на склад, и с этими покрывалами в библиотеку."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    
    stop music fadeout 3
    $ renpy.pause(3)

    play sound sfx_open_door_clubs
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_musclub_day with dissolve2
    play sound sfx_close_door_1

    window show
    "Зайдя в музыкальный кружок, я заметил только одну стойку с одной электрогитарой." 
    "Остальные должны были находится в подсобке. Я заглянул в подсобку, и найдя еще пару электрогитар, вытащил все мною найденное на улицу."
    window hide

    play sound sfx_open_door_clubs
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_music_club_verandah_day with dissolve2
    play sound sfx_close_door_1

    window show
    "Одну электрогитару для музыкального кружка Маши пришлось оставить, дабы не портить отношения с пионерами." 
    window hide

    $ renpy.pause(1)

    window show
    "Взвалив всё это добро на себя, я поплелся прямиком к сцене."
    window hide

    show black with dissolve2

    $ renpy.pause(2)

    play music ndm_list['mood_think'] fadein 4
    scene bg ext_stage_big_day with dissolve2

    window show
    "Дотащив электрогитары до сцены, я заметил, как Алиса снимает паутину со стен сцены."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Ну как убирается?"
    dv "Нормально. Как видишь." 
    nd_il "Ничего.{w} Зато клуб будет наш.{w} Настоящий."
    dv "Лучше, вместо того, чтобы болтать попусту, помог."

    scene bg ext_stage_normal_day with dissolve

    "Я залез на сцену к Алисе."

    show dv normal pioneer2 at center with dspr

    dv "Приподними меня, дотянуться не могу."

    hide dv with dspr

    "Я взял девушку, и поднял её."
    "На мое удивление, она оказалась довольно легкой."

    dv "Крепко держишь?"
    nd_il "Ага."
    dv "Тогда можешь левее?.."
    "Я попытался сделать шаг влево."
    window hide

    $ renpy.pause(1)

    window show
    dv "Ну, ты скоро там?"
    nd_il "Погоди..."
    th "Не такая она и легкая, как мне сначала показалось..."

    dv "Давай еще левее."

    "Я попытался сделать шаг, но мои ноги подкосились."
    stop music fadeout 3

    "В этот момент мир как будто замер." 
    "Мне было ясно, что будет дальше и к чему это может привести.{w} Но было уже поздно что-то предпринимать..."
    
    show black with dissolve2
    play sound sfx_alisa_falls
    stop ambience fadeout 3
    "Под визг Алисы, мы упали на пол."
    window hide

    $ renpy.pause(2)

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_stage_big_day with dissolve2

    window show
    "Солнечные лучи просачивались к сцене через ветки деревьев."
    "Лагерный воздух был чист и свеж, как утреннее щебетание птиц,{w} и согревал сердце как июльский снег."
    nd_il "Я умер?"
    "Тихо спросил я."
    window hide

    $ renpy.pause(1)

    window show
    "Внезапно послышались шаги и голос Маши."
    mi "Эй! Илья! Алиса! Вы здесь? Я просто хотела спросить насчет электрогитар..."

    show black with dissolve

    "Я попытался ответить Маше, но Алиса закрыла мой рот руками."

    play music ndm_list['mood_over'] fadein 3

    "И только сейчас я заметил,{w} что Алиса лежит на мне, закрывая меня собой и своими волосами от солнечных лучей."
    "От её волос приятно пахло.{w} Этот запах нельзя было сравнить ни с чем.{w} Скорее всего, это просто какой-нибудь шампунь."
    "Такая обстановка показалась мне довольно странной.{w} Алиса охотно демонстрировала мне свою фигуру, и не давала даже сдвинуться с места."
    "Но я считаю, что в моем случае это и не нужно было..."

    dv "Тихо."
    "Произнесла шепотом Алиса."
    window hide

    $ renpy.pause(1)

    window show
    mi "Думаю, что стоит поискать их в клубах."
    window hide

    hide black with dissolve2

    window show
    "Звуки шагов начали приглушаться, пока совсем не исчезли.{w} И тогда Алиса освободила меня из своего \"плена\"."
    window hide

    stop music fadeout 3
    $ renpy.pause(1)

    window show
    "Мы встали с места."

    show dv angry pioneer2 far at center with dspr

    dv "{b}Ты дурак{/b}?!{w} А если бы она нас заметила, то что бы она подумала?"

    show dv shy pioneer2 far at center with dspr
    dv "Это странно бы смотрелось."

    nd_il "Но мы бы быстро встали."
    dv "Это тоже смотрелось бы странно,{w} и было бы подозрительным."
    nd_il "Ладно, я понял, давай просто убираться дальше..."

    stop music fadeout 3
    hide dv with dspr
    stop ambience fadeout 3
    show black with dissolve

    "Мы раскладывали все по своим местам - электрогитары, сабвуферы, стойки для электрогитар,{w} и вся эта \"реставрация\" заняла у нас около одного-двух часов."
    "Без телефона тяжко оценивать счет времени..."
    window hide

    $ renpy.pause(2)

    window show
    "Когда все было готово,{w} мы вытерли пот со лба и осмотрели то, что у нас получилось."

    scene bg ext_stage_big_day_alice with dissolve2

    nd_il "Не плохо убрались... Только чего-то не хватает..."
    dv "Ну, наверное, большого плаката из покрывал."
    nd_il "Точно. Ну что, сейчас этим займемся?"

    show dv smile pioneer2 at right with dspr

    dv "Это только и осталось. Пойдем..."
    window hide

    stop ambience fadeout 3
    show black with dissolve2

    play music ndm_list['mood_loneliness'] fadein 6

    $ renpy.pause(2)

    $ set_mode_nvl()

    window show
    "Взять покрывала оказалось довольно легкой задачей.{w} К счастью, у Алисы оказались подходящие ключи,{w} так как это были ключи от здания прошлого клуба гитаристов,{w} которое сейчас оборудовано под склад."
    "Проще говоря - у Алисы были ключи от склада."
    "Но появилась еще одна проблема.{w} Нужно было пробраться в библиотеку..."
    window hide

    $ set_mode_adv()

    stop music fadeout 4

    $ renpy.pause(1)    
    
    play ambience ambience_camp_center_day fadein 4
    scene bg ext_library_day with dissolve2

    window show
    "Когда мы пришли к библиотеке, Алиса скинула покрывала на скамейку, и мы начали обсуждать план дальнейших действий."

    show dv smile pioneer2 at center with dspr

    nd_il "Ну и как нам туда пробраться с этими покрывалами?{w} Навряд ли эта злюка нас туда пропустит с ними."
    
    show dv normal pioneer2 at center with dspr 
    dv "Тут ты прав..."

    "Алиса задумалась..."
    window hide

    $ renpy.pause(2)

    window show
    dv "Кажется, я кое-что придумала.{w} Жди."
    hide dv with dspr
    "Сказав это, Алиса побежала куда-то, а потом скрылась за углом одного из домиков."
    window hide

    $ renpy.pause(2)

    window show
    "Я, как дурак, сидел на скамейке с N-ным количеством покрывал."
    "Прятать их было бессмысленно - они были чересчур заметны.{w} И если бы я так попался вожатой на глаза, могли бы произойти проблемы."
    window hide

    $ renpy.pause(1)

    window show
    "Внезапно меня заметил какой-то пацан и пошел ко мне."
    th "Ну вот.{w} Сейчас начнутся вопросы..."

    show vst normal pioneer at center with dspr

    pi "Привет. Ты не подскажешь, где здесь медпункт?{w} Мне нужно бегунок подписать, а я не знаю, куда идти." 
    th "А-а. Так это же новенький."
    nd_il "Сейчас попробую объяснить..."

    hide vst with dspr

    "Я начал показывать, в каком направлении нужно идти, и куда поворачивать." 
    "Его лицо выглядело сосредоточенным, и было видно, что он меня внимательно слушает и запоминает.{w} Или это просто наигранно?"

    show vst normal pioneer at center with dspr

    pi "Понял, спасибо.{w} Тебя, кстати, как зовут?"
    nd_il "Илья."
    vst_lar "А меня Василием.{w} Мы вроде как из отряда одного."
    th "Да ладно.{w} Этого не может быть."
    vst_lar "Ну ладно. Я пошел. Еще увидимся."
    hide vst with dspr
    "Пионер отправился в направлении медпункта, или по крайней мере куда я ему показал."
    th "Если это действительно тот самый Василий из моего сна, то почему он ведет себя как обычный пионер?"
    th "Скорее всего это просто совпадение."
    window hide

    $ renpy.pause(1)
    show black with dissolve 
    $ renpy.pause(1)
    hide black with dissolve 

    window show
    "Спустя минуту ожидания, я уже видел бегущую в мою сторону Алису."
    
    play music ndm_list['mood_loneliness'] fadein 6

    show dv smile pioneer2 at center with dspr 

    nd_il "Где ты была?"
    dv "Прячься."
    nd_il "Куда?"

    show dv grin pioneer2 at center with dspr

    dv "Туда."

    hide dv with dspr

    "Алиса взяла меня за руку и потащила за библиотеку.{w} Я еле как успел схватить с собой покрывала."

    stop music fadeout 3
    play sound sfx_hiding_in_bush 
    scene bg ext_glade_day with dissolve

    show dv normal pioneer2 at center with dspr

    nd_il "Может, ты объяснишь, что происходит?"
    dv "Мой план происходит."
    nd_il "Посвяти."
    dv "Хорошо.{w} Я подкинула записку Электронику от Жени, что она ждет встречи с ним у библиотеки.."
    dv "Когда Электроник постучится в дверь, выйдет эта мымра и они начнут диалог.{w} Тут мы просто прошмыгнем в библиотеку."

    "Гениально в плане Алисы было всё. Но кое-что мне не давало покоя..."

    nd_il "А как мы выбираться будем?"

    dv "Как нибудь. Тихо..."
    window hide


    play sound sfx_hiding_in_bush
    scene bg ext_library_day with dissolve
    $ renpy.pause(1)

    show el normal pioneer far at center with dspr

    $ volume(0.4, "sound")

    window show
    "Выглянув из-за кустов мы увидели Электроника, стоящим у дверей библиотеки."
    window hide

    play sound sfx_knock_door2
    $ renpy.pause(1)
    hide el with dspr

    play sound sfx_open_door_1
    show el normal pioneer far at left with dspr
    play sound sfx_close_door_1

    show mz normal pioneer far at right with dspr

    window show
    "После нескольких его стуков в дверь, вышла Женя."
    window hide

    $ renpy.pause(1)
    $ volume(1, "sound")
    play sound sfx_hiding_in_bush
    scene bg ext_glade_day with dissolve

    show dv smile pioneer at right with dspr 

    window show
    dv "Действуем. Иди за мной. И чтобы без шума."
    "Командирским голосом произнесла Алиса."
    window hide

    show black with dissolve2
    play sound sfx_hiding_in_bush
    $ renpy.pause(1)

    window show
    "Мы дошли до запасного выхода."
    play sound sfx_open_door_1
    "Дверь просто открывалась.{w} Без ключа."
    window hide

    $ renpy.pause(1)
    
    window show
    mz "Я тебе ничего не писала. Тем более насчет нашей встречи. Теперь - свободен."
    el "Послушай...{nw=1}"
    dv "Что уши греем? Заходи."
    window hide

    scene bg int_library_day with dissolve

    play sound sfx_close_door_1

    $ renpy.pause(1)

    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    play ambience ambience_int_cabin_day fadein 3
    
    $ persistent.sprite_time = 'sunset' 

    scene bg int_editorial_day with dissolve


    play sound sfx_close_door_1

    window show
    "Войдя в библиотеку мы, практически бесшумно, пробрались в подсобку со всеми покрывалами и заперли ее на ключ."

    nd_il "Отлично.{w} Гениально! Волшебно! Осталось придумать, как потом выйти отсюда целыми."

    show dv grin pioneer at right with dspr
    dv "Ну конечно. Это же мой план."

    "Это звучало так, будто мои планы всегда плохо заканчивались, но тот случай в столовой со Славей опровергал это."
    
    dv "А насчет выхода не беспокойся. Мы просто покажемся ей, она поорет немного и нас выпроводит." 
    window hide

    hide dv with dspr

    $ renpy.pause(1)

    window show
    "Немного подумав, я заметил, что мы с собой не взяли ничего, чем можно было бы работать.{w} Ни красок, ни фломастеров, ни карандашей."
    "Благо в подсобке все еще были предметы для рисования.{w} Только ножниц не наблюдалось.{w} Но была доисторическая машинка для шитья с нитками и иголками."
    "Несмотря на это, выглядела она довольно новой."

    nd_il "Как нам без ножниц резать?"
    dv "Руками рвать. Остальное у нас всё есть..."

    show black with dissolve

    "Мы с Алисой тут же начали работу."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Ух ты... Ты шить умеешь?"
    dv "Представляешь? А еще вязать несколькими способами."
    nd_il "Свяжешь мне потом что-нибудь?"
    dv "Посмотрим на твое поведение..."
    window hide

    stop ambience fadeout 3
    $ renpy.pause(2)
    scene bg int_editorial_day with dissolve
    play ambience ambience_int_cabin_day fadein 3

    window show
    "Когда покрывала были полностью сшиты в одно, встал вопрос: \"Что рисовать?\""

    show dv smile pioneer at right with dspr

    nd_il "Какие идеи?"
    dv "Есть идея акулу нарисовать.{w} Или пиратский флаг."
    nd_il "А и то и другое можно?"
    dv "Нет, только одно."
    
    hide dv with dspr

    vg "Ха-ха. Ты правда думал, что можно будет нарисовать сразу два рисунка?"
    th "Вот тебя-то спросить и забыли."
    window hide

    $ renpy.pause(1)

    window show
    th "Ну вроде-бы оба варианта одинаково хороши."
    th "Как акула, так и пиратский флаг будут смотреться грозно и круто."
    th "..."
    window hide

    $ renpy.pause(1)

    show dv grin pioneer at right with dspr
    
    window show
    dv "Ты придумал, что нам рисовать?"
    nd_il "Не знаю, пусть будет..."
    window hide

    menu:
    
        "Акула":
            
            $ dvrr_shark_p += 1
            show dv smile pioneer at right with dspr

            window show
            dv "Не плохой выбор, значит будем рисовать акулу."
            window hide

        "Пиратский флаг":
            
            $ dvrr_pirate_p += 1
            show dv smile pioneer at right with dspr
            
            window show
            dv "Не плохой выбор, значит будем рисовать пиратский флаг."
            window hide

    show black with dissolve
    stop ambience fadeout 3
    $ renpy.pause(2)

    window show
    "На рисование рисунка потребовалось больше времени, чем мы думали.{w} Затруднение вызывал лишь размер полотна, а соответственно - размер рисунка."
    "Он должен был быть внушительно большим, и это вызывало больше всего затруднений."
    window hide

    $ renpy.pause(1)
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_editorial_day with dissolve2

    window show
    "Когда рисунок был нарисован, мы посмотрели что получилось..."
    window hide

    $ renpy.pause(2)
    
    window show
    "Внизу полотна обнаружилось пустое место, которое не было ничем занято.{w} Видимо, мы просто не рассчитали размер рисунка."

    show dv normal pioneer at right with dspr

    dv "Внизу пустое место осталось, придётся обрезать."

    nd_il "А может написать там что-нибудь.{w} Например - \"Гитарный клуб\""
    
    show dv smile pioneer at right with dspr

    dv "И правда.{w} Надпись как раз поместится.{w} Хорошо у тебя смекалка работает."
    nd_il "Ага.{w} Не то что твоя седая головушка."

    show dv grin pioneer at right with dspr
    dv "Нет. Головушка нашего сторожа.{w} Хотя на ней даже седого волоска не найти."
    nd_il "Ты про Таляна что-ли?{w} Этого мужичка тихого лысого, который в столовой на задних столах сидит?"

    show dv laugh pioneer at right with dspr
    "Алиса засмеялась заливистым смехом."
    window hide

    $ renpy.pause(1)

    window show
    dv "Ха-ха. Теперь я его тоже буду Таляном называть..."
    window hide

    hide dv
    with dissolve

    $ renpy.pause(1)
    
    window show
    "Мы аккуратно написали задуманное черным маркером, и оставили засыхать созданное нами творение."
    window hide

    $ renpy.pause(3, hard=True)

    window show
    "Когда оно подсохло, мы аккуратно и компактно сложили простыни, чтобы потом вынести их на улицу к сцене и повесить на видное место."

    show dv normal pioneer at center with dspr
    
    dv "Ладно, давай теперь выносить."
    nd_il "А Женя только кричать будет? А если начнет брыкаться?"
    dv "А меня не волнует.{w} Не сожрет же она меня в конце концов."
    
    $ persistent.sprite_time = 'day' 
    
    play sound sfx_open_door_clubs    
    scene bg int_library_day with flash
    play sound sfx_close_door_1 

    "Мы вышли с плакатом из подсобки."

    play sound sfx_open_door_1
    "Жени на своем месте не было.{w} Но это играло нам на руку."
    "Мы просто вышли из библиотеки, и направились к сцене."
    window hide

    stop ambience fadeout 3
    stop music fadeout 3
    play ambience ambience_camp_center_day fadein 3
    show black with dissolve2

    $ renpy.pause(1)

    scene bg ext_stage_normal_day with dissolve2

    window show
    "Как только мы пришли к сцене, то поняли - что нас уже ждут ребята из нашего отряда."
    "Здесь и Ульяна с Машей, и Лена со Славей, и вожатая соответственно."

    show us surp1 pioneer far at center with dspr

    us "О! Вот они идут!"
    window hide

    hide us with dspr

    $ renpy.pause(1)

    show mi smile pioneer at left
    show us smile pioneer at cleft 
    with dspr

    show sl normal pioneer at right
    show un smile pioneer at cright
    with dspr

    show mt angry pioneer at center with dspr

    window show
    mt "Маша вас искала. Где вы были?"
    nd_il "Мы плакат рисовали."
    mt "А гитары куда вы положили?"
    dv "Они на сцене."

    hide mt with dspr

    "Ольга Дмитриевна взглянула на сцену.{w} Там мирно красовалась стойка с гитарами."

    show mt smile pioneer at center with dspr

    show dv normal pioneer at fright with dspr 

    dv "Вы пришли на открытие клуба посмотреть?"
    mi "Конечно!"
    nd_il "Давайте тогда плакат вешать."

    show un smile2 pioneer at cright with dspr

    un "Давайте."

    hide mt
    hide dv
    hide us
    hide un
    hide mi
    hide sl
    with dspr

    show black with dissolve

    "Мы с Алисой забрались на сцену, взяли пару стульев и, закинув плакат, зафиксировали его на доске с заранее сделанными крепежами..."
    window hide

    if dvrr_shark_p == 1:
        scene bg ext_stage_big_day_alice_flagtag
        show ext_stage_big_day_alice_shark
        with dissolve2

    if dvrr_pirate_p == 1:
        scene bg ext_stage_big_day_alice_flagtag
        show ext_stage_big_day_alice_pirate
        with dissolve2

    $ renpy.pause(2)


    show mi surprise pioneer at left
    show us surp1 pioneer at cleft
    show sl surprise pioneer at right
    show un surprise pioneer at cright
    with dspr
    play sound nds_list['applweak']

    window show
    all "Ух ты! Красиво получилось!"
    window hide

    show us normal pioneer at cleft with dspr
    
    $ renpy.pause(2)
    stop sound fadeout 3
    


    show sl normal pioneer at right with dspr
    show un smile pioneer at cright with dspr

    show dv smile pioneer at fright with dspr

    window show
    dv "Теперь надо о нашем клубе рассказать."

    show mi smile pioneer at left with dspr

    mi "Не надо, мы уже разместили объявление о вашем клубе на доске у входа в лагерь."
    mi "Рисунок рисовала Лена, а я занималась оформлением..."
    
    show dv guilty pioneer at fright with dspr

    dv "Ну... Спасибо вам... "

    all "Пожалуйста."

    show us smile pioneer at cleft with dspr
    us "Алиса, а можно к вам записаться? Я смогу."

    show mt normal pioneer at center with dspr 

    mt "Запишитесь после тихого часа."

    show us normal pioneer at cleft with dspr
    us "Ну Оль Дмитриевна..."

    nd_il "Да, я тоже не против поспать."

    show dv grin pioneer at fright with dspr

    dv "А мы и не сомневаемся."
    window hide

    stop ambience fadeout 3
    scene black with dissolve
    $ renpy.pause(1)

    window show
    "...Пионеры начали расходиться. На сцене остались лишь мы одни..."
    window hide

    $ renpy.pause(1)
    play ambience ambience_camp_center_evening fadein 3

    if dvrr_shark_p == 1:
        scene bg ext_stage_big_day_alice_flagtag
        show ext_stage_big_day_alice_shark
        with dissolve

    if dvrr_pirate_p == 1:
        scene bg ext_stage_big_day_alice_flagtag
        show ext_stage_big_day_alice_pirate
        with dissolve


    window show
    nd_il "Ладно, Алис, пора на отбой."
    show dv grin pioneer at center with dspr
    dv "Ты серьезно спать собрался?"
    nd_il "Ну да.{w} А ты запрещаешь?"

    show dv shy pioneer at center with dspr

    dv "Запрещаю. "
    window hide

    $ renpy.pause(2)

    window show
    dv "Ты знаешь, что сегодня танцы?"
    nd_il "Да."
    "Мне казалось, что Алиса на что-то намекает.{w} Что-то пытается мне сказать, но не может."
    "И вместо этого еще одно короткое молчание..."
    window hide

    $ renpy.pause(1)

    window show
    dv "Так вот. Я предлагаю встретится с тобой перед танцами вот здесь, и..."
    "Алиса замялась."
    dv "...Посмотреть на звёзды и поговорить.{w} Что ты об этом думаешь?"
    window hide

    $ renpy.pause(1)
    
    window show
    th "Она хочет встретится со мной, поговорить и посмотреть на звезды?{w} Ещё этот румянец на её лице..."
    nd_il "Да, почему бы и нет."

    show dv smile pioneer at center with dspr

    dv "Ну вот и отлично.{w} Можешь теперь идти, куда хотел..."
    nd_il "А ты куда сейчас?"
    dv "А я буду учить новую песню.{w} Если хочешь, можешь посмотреть.{w} Займи одно из зрительских мест."
    
    hide dv with dspr

    th "Что это, черт его возьми, только что было?{w} Ладно..."

    "Пожав плечами, я сел на одно из самых первых мест к сцене."
    window hide


    $ renpy.pause(1)
    play music ndm_list['butterfly'] fadein 3
    $ renpy.pause(1)
    
    window show
    "Алиса взяла гитару, подключила её к комбику, покрутила эффекты, и начала наигрывать какую-то знакомую мне мелодию.{w} Я наблюдал за игрой девушки, пока глаза не стали автоматически закрываться..."
    window hide

    $ renpy.pause(3)
    
    stop music fadeout 1
    stop ambience fadeout 1
    show blink
    
    window show
    "Вскоре я не смог препятствовать этому процессу, и провалился в глубокий сон..."
    window hide
    jump dream_d2_oldbuilding_night

label plakats_us_d3_rt:

    show un smile pioneer at fleft
    show mi smile pioneer at right
    show sl smile pioneer at left
    show mt normal pioneer at center
    with dspr

    $ renpy.pause(1)

    window show
    "Выйдя на улицу, меня с девочками ждала Ольга Дмитриевна и чувство дежавю."
    ".{w}.{w}."
    sl "А вот и Илья."
    show us normal pioneer at fright with dspr
    us "И я с ним. Ну, где плакаты?"
    show mt smile pioneer at center with dspr
    mt "За ними ещё в библиотеку сходить нужно." 
    mt "Ульяна, откуда такое стремление помочь товарищу?"
    show us smile pioneer at fright with dspr
    us "Он обещал поиграть со мной после уборки."
    show mi grin pioneer at right with dspr
    mi "Понятно. Давайте, чтобы быстрее было разделимся."

    th "Именно после таких слов в фильмах ужасов происходило что-то плохое."
    th "Погодите, что?"

    mt "Лена с Мику идут в библиотеку, а вы с Ульяной идёте к кибернетикам за ножницами и скотчем."
    mt "Встречаемся у столовой."

    hide un
    hide mi
    hide sl
    hide us
    with dspr

    "У меня было много вопросов, но так как Ульяна сильно торопилась, я мог задать только один."

    us "Всё Илья, побежали."
    "Сказав это, Ульяна взяла меня за руку и потянула за собой."

    th "А что будет делать вожатая? Почему именно мы с Ульяной? Почему ножницы и скотч у кибернетиков? Почему мне опять приходится делать выбор? Какой вопрос ей задать?!"
        
    us "Да пошли уже, упрямый."
    "Ульяна потянула сильнее..."

    nd_il "Как открыть крем звёздочку с первого раза?"
    
    hide mt with dspr
    scene bg ext_dining_hall_away_day with dissolve 
    
    "Ульяна буквально потащила меня за собой к зданию общих кружков." 
    window hide

    $ renpy.pause(1)
    
    window show
    "Вожатая провожала меня недоумевающим взглядом, а затем прокричала мне в след..."
    mt "Руками!"
    window hide

    show black with dissolve
    $ renpy.pause(1)
    
    window show
    th "Опять я какой-то бред сморозил."
    th "И что мне теперь делать с этой информацией?"
    window hide

    $ renpy.pause(1)

label d3_kibernetis_us_event:
    stop ambience fadeout 3
    $ renpy.pause(3, hard=True)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with dissolve2

    window show
    "Вскоре мы добежали до здания общих кружков."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    th "Почему это здание называется \"здание общих кружков\", но по факту тут только клуб кибернетиков?"
    vg "Слишком много вопросов для одного дня, не находишь?"
    th "Возможно, ты прав.{w} Мне определенно нужно отвлечься."
    vg "Входи уже, не тупи."

    show us normal pioneer with dspr

    us "Илья, чего встал, пошли."
    window hide

    $ renpy.pause(1)
    hide us with dspr
    $ renpy.pause(1)

    stop ambience fadeout 3
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play music music_list["smooth_machine"] fadein 4
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_clubs_male_day with dissolve2
    play sound sfx_close_door_1

    window show
    "Открыв дверь, я увидел Шурика и Электроника."
    "Шурик набирал что-то на компьютере, а Электроник паял мой будущий зарядник."

    nd_il "Привет, кибернетики!"

    show el normal pioneer at center with dspr
    el "О, с возвращением, Илюх. Зачем пришёл?"


    nd_il "Слушай, Электроник, у вас есть в клубе ножницы и скотч?"
    window hide

    $ renpy.pause(1)
    show el smile pioneer at center with dspr

    window show
    el "Да были вроде, подожди, сейчас вынесу."

    hide el with dspr

    "Сказал Электроник и ушёл в подсобное помещение, не заметив Ульяну."
    window hide

    show us normal pioneer at fleft with dspr
    
    $ renpy.pause(1)
    hide us with dspr
    show us smile pioneer at center with dspr
    hide music fadeout 1

    window show
    "Рыжая девушка вышла из-за моей спины и, заметив моток медной проволоки, начала вести себя слегка... не сдержанно."
    "У неё просто горели глаза от этого мотка медной проволоки."
    "И, кажется, с этим уже ничего нельзя было поделать..."
    window hide

    stop music fadeout 3
    $ renpy.pause(1)

    window show
    nd_il "Ульяна, что бы ты не задумала — пожалуйста не надо."
    window hide

    $ renpy.pause(1, hard=True)

    hide us with dspr
    
    window show
    "Ульяна подбежала к проволоке, схватила её, подняла вверх и закричала Шурику на всё помещение."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    us "Шурик! Это вам нужно?"
    sh "Да, не трогай."
    "Шурик повернулся, и как только понял, у кого находится проволока, тут-же взволновался."

    play music music_list["pile"] fadein 3
    
    sh "Ульяна, не трогай проволоку!"

    "Крикнув, Шурик побежал спасать медный моток."
    window hide

    $ renpy.pause(1)

    show cg d5_sh_us with dissolve 

    $ renpy.pause(3)

    hide cg d5_sh_us with dissolve

    window show   
    "Ульяна кинула моток мне."
    
    show sh serious pioneer at center with dspr
    show us smile pioneer far at right with dspr

    sh "Илья, мы взрослые люди, давай ты отдашь проволоку."

    vg "Думаю ему скучно каждый день сидеть в этой комнатушке и паять микросхемы."
    vg "Может поиграть с ним?"
    th "И то верно."

    nd_il "Ульяна, лови."
    hide sh
    hide us
    with dspr
    
    "Сказал я и кинул проволоку Ульяне, а она мне..."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    hide black with dissolve
    $ renpy.pause(1)
    
    window show
    "И вот так мы играли с кибернетиком в \"собачку\"{w}, пока Шурику не надоело, и он не позвал своего сотоварища Электроника."
    show el normal pioneer far at fleft with dspr
    "Когда он вышел из подсобки, проволока уже летела в руки к Ульяне."
    stop music fadeout 2
    
    el "Что у вас тут происходит?"
    "Ульяна спряталась за меня, держа за спиной несчастный моток."
    
    show sh serious pioneer at center with dspr
    
    sh "Они проволокой кидались."
    
    show el serious pioneer at fleft with dspr
    el "Ульяна, опять ты."
    th "Так, то-есть Ульяна не первый раз у них проволоку берёт." 
    "Я невольно улыбнулся."
    el "Верни нам проволоку."
    "Электроник протянул руку, ожидая того, что Ульяна отдаст недавно украденную вещь."
    us "Не-а."
    el "Илья, хоть ты скажи ей."
    "Сказал кибернетик и посмотрел на меня, ожидая действий с моей стороны."
    hide el
    hide sh
    with dspr
    show us grin pioneer at center with dspr

    nd_il "Ульяна, мы уже поиграли.{w} Ты можешь отдать проволоку кибернетикам."
    el "А не-то мы вожатой пожалуемся!"
    
    show us sad pioneer at center with dspr
    us "Илья, ты что, с ними заодно?"
    window hide

    $ renpy.pause(1)

    window show
    th "Да вы шутите. Ну какая жалость?"
    nd_il "Ульяна, да что ты как маленькая?"

    show us dontlike pioneer at center with dspr
    
    us "Я не маленькая!"
    window hide

    hide us with dspr
    $ renpy.pause(1)
    play sound sfx_drop_alisa_bag
    $ renpy.pause(1)
    play sound sfx_chair_fall
    play sound sfx_open_door_clubs
    $ renpy.pause(1)
    play sound sfx_close_door_1

    window show
    "Топнув ногой, Ульяна кинула проволоку на полку самого дальнего шкафа, чуть не задев модель лодки, и вышла из здания."
    th "Что это с ней?" 
    th "Я её обидел?"

    show el normal pioneer at center with dspr
    
    el "Илья, вот ножницы и скотч."
    nd_il "Спасибо."
    window hide

    hide el with dspr

    $ renpy.pause(1)
    
    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with flash
    play sound sfx_close_door_1
    
    $ renpy.pause(1)
    
    window show
    "Я ожидал, что Ульяна будет стоять на улице, но её там не оказалось."
    "Она слишком быстро убежала, не дав извиниться перед ней за небрежное вскользь брошенное словечко."
    window hide

    $ renpy.pause(1)

    window show
    th "Вот теперь я действительно виноват перед ней."
    window hide

    $ renpy.pause(1)
    
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(2, hard=True)
    play ambience ambience_camp_center_day fadein 3 
    scene bg ext_houses_day with dissolve2 

    $ renpy.pause(1)

    window show
    th "Неужели она так обиделась на это?"
    th "Может эта проволока правда ей нужна была?"
    th "В конце концов она бы поигралась и потом отдала."
    window hide

    $ renpy.pause(2)
    
    window show
    th "Какой же я дурак…"
    window hide

    $ renpy.pause(1)

    window show
    "На моей душе было очень тяжко от этого, но сейчас ничего нельзя было сделать, кроме как идти дальше к столовой."
    th "Зато смогу плакаты без всяких задержек повесить..."
    window hide

    $ renpy.pause(1)
    play sound sfx_hiding_in_bush
    
    window show
    strange_g "Илья..."
    
    with vpunch

    "Я вздрогнул от внезапности."
    
    nd_il "Кто это?"
    
    strange_g "Ты потом сам всё поймёшь." 
    strange_g "Найди Ульяну и извинись перед ней."
    nd_il "Я как раз думал об этом."
    nd_il "И кто это вообще?"
    strange_g "Поторопись..."
    
    play sound sfx_hiding_in_bush
    
    "Кусты вновь зашуршали, и что-то скрылось за ними, а может быть и в них самих."
    th "Что только что было?{w} Надо мной кто-то решил пошутить?"
    window hide

    $ renpy.pause (1)
    
    window show
    th "В любом случае, как он и сказал, мне нужно торопиться."
    window hide

    $ renpy.pause (1)
    show black with dissolve2
    $ renpy.pause (3, hard=True)
    scene bg ext_dining_hall_away_day with dissolve2
    
    window show
    "Вот уже показалась столовая, но девочек рядом с ней я не увидел."
    th "Видимо, я надолго там в клубах задержался."
    th "Может быть они уже внутри сидят и меня ждут?"
    window hide

    $ renpy.pause (1)
    show black with dissolve
    $ renpy.pause (1)
    scene bg ext_dining_hall_near_day with dissolve

    window show
    "Я забежал по лестнице на веранду и открыв двери в столовую, зашел внутрь..."
    window hide

    $ renpy.pause (1)

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause (1, hard=True)
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve2
    play sound sfx_close_door_1 
    
    window show
    "Около одного из рядов я заметил стоящих девушек из моего отряда."
    "Скорее всего, они ждали именно меня, и начинать работу до моего прихода не собирались."
    "Ну конечно, у меня ведь были ножницы."

    show un smile pioneer at fright 
    show mt smile pioneer at left
    show sl smile pioneer at right
    show mi smile pioneer at center
    with dspr

    mt "Илья, ты чего так долго?"
    mt "И где твоя помощница?"
    "Долго придумывать отмазку не пришлось."
    window hide

    $ renpy.pause (1)

    window show
    nd_il "Скотч пришлось поискать, а Ульяна на футбольное поле побежала."
    "В моём голосе промелькнула нотка волнения.{w} Но никто, кажется, этого не заметил."
    mt "Ладно. Илья, поставь стул у этой стены и держи его, а Маша залезет на него и наклеит первый плакат."
    nd_il "Будет сделано."
    window hide
    
    $ renpy.pause (1)

    hide mi
    hide mt
    hide sl
    hide un
    with dspr

    window show
    "По команде Ольги Дмитриевны, мы с Машей взяли один из стульев, и принялись выполнять задание."
    mt "...а Лена и Славя будут расклеивать плакаты внизу..."
    window hide

    $ renpy.pause (1, hard=True)
    stop ambience fadeout 2
    show black with dissolve
    $ renpy.pause (3, hard=True)
    play ambience ambience_dining_hall_empty fadein 2
    hide black with dissolve
    
    window show
    "Держа стул, я не мог ни о чём думать, кроме как о Ульяне и её обиде на меня."
    "Не думать о голосе, сообщившем мне что-то через шорох кустов."
    window hide

    $ renpy.pause (1)

    window show
    th "Кто был обладателем этого голоса?"
    th "И почему мне нужно куда-то торопиться?"
    window hide

    $ renpy.pause (1)
    
    window show
    "Я задавался вопросами, на которые у меня не было ответов."
    "А незнание порождает страх чего-то неизведанного, неизученного, будущего..."
    window hide

    $ renpy.pause (1, hard=True)
    
    window show
    "Это чувство будто разъедало меня изнутри."
    "Я хотел от него избавиться, отвлекаясь то на поваров, то на погоду на улице.{w} Но мне ничего не помогало."
    "Вместе с тем, невыносимо хотелось бежать куда-то."
    window hide

    $ renpy.pause (1)
    
    $ renpy.pause (1, hard=True)
    stop ambience fadeout 2
    show black with dissolve
    $ renpy.pause (2, hard=True)
    play ambience ambience_dining_hall_empty fadein 2
    hide black with dissolve

    window show
    "Вот настало время моего плаката."
    "Я подал его наверх к Маше.{w} Она, зафиксировала его и ловко приклеила скотчем к стене..."
    window hide

    $ renpy.pause (1)

    show sl smile2 pioneer at center with dspr

    window show
    sl "Вы уже закончили? Нам тоже сейчас скотч нужен."
    window hide

    $ renpy.pause (1)
    
    window show
    "Маша спустила мне скотч и ножницы, а я протянул их Славе."
    window hide

    hide sl with dspr
    
    $ renpy.pause (1, hard=True)

    window show
    th "Нет, это не возможно больше терпеть."
    nd_il "Ольга Дмитриевна, можно мне уже идти.{w} Я тороплюсь. "
    mt 'Ладно, иди.'
    sl "И про уборку в библиотеке не забудь."
    window hide

    $ renpy.pause (1)
    stop ambience fadeout 3
    show black with dissolve2
    play sound sfx_open_door_clubs
    $ renpy.pause (2, hard=True)
    play ambience ambience_camp_center_day fadein 2
    scene bg ext_dining_hall_near_day with flash
    play sound sfx_close_door_1
    $ renpy.pause (1)
    show black with dissolve
    scene bg ext_dining_hall_away_day with dissolve

    window show
    th "Надеюсь, Ульяна будет на футбольном поле."
    th "Иначе я даже не знаю, где она может быть."
    window hide

    $ renpy.pause (1)
    
    window show
    "Я поправил пионерские шорты, и со всей скорости рванул на футбольное поле."
    window hide

    show black with dissolve2
    play sound_loop sfx_run_forest fadein 2
    $ renpy.pause (2, hard=True)

    window show
    "Я бежал очень быстро, чуть ли не сбивая c ног проходящих мимо пионеров."
    "А последним больше ничего не оставалось, кроме как смотреть мне в след и, возможно, крутить пальцем у виска."
    window hide

    $ renpy.pause (3, hard=True)
    stop sound_loop fadeout 1
    $ renpy.pause (1, hard=True)
    play ambience ambience_soccer_play_background fadein 3
    show cg d6_pioneer with dissolve2

    window show
    "Через минуту я уже стоял, облокотившись на стену здания, за которым было футбольное поле, и откуда доносились голоса."
    parr "Ну что, в этот раз мы тебя выиграем без твоего друга."
    us "Не дождётесь.{w} В этот раз мне никто мешать не будет."
    window hide

    play music ndm_list['RF_memory_1'] fadein 3
    stop ambience fadeout 3
    $ renpy.pause (1)

    window show
    th "Я правда ей только мешаю?"
    "Я заглянул за угол здания и увидел, как Ульяна играет со своими друзьями."
    window hide

    window show
    "Сев у стены, мне пришлось смотреть на этот спектакль с весёлыми актёрами, подстроенный судьбой специально для меня."     
    "Ведь жизнь театр, да?{w} Если так, то мой театр будет похож на грязное здание с тусклым золотом, актёры которого давно спились или повесились.{w} А за театром — эшафот."
    window hide

    $ renpy.pause (1)
    
    window show
    "Птицы в лагере прекратили своё пение, а тени стали намного гуще, чем были до этого."
    th "А, собственно, зачем я ей?{w} У неё есть друзья, которые явно веселее какого-то задрота из будущего."
    window hide

    show black with dissolve

    $ renpy.pause (1)

    $ set_mode_nvl()

    window show
    "Вот Ульяна разгоняется к мячу."
    th "Это как в той песне..."
    "Прорывает оборону противника."
    th "...Ждать, дышать, бежать и видеть..."
    "Мяч потерян, противник бежит к воротам."
    th "...И кого-то сильно ненавидеть..." 
    "Вратарь отбивает мяч Ульяне.{w} Она бежит к воротам противника."
    th "...Или сильно невзначай обидеть..."
    "Готовится забить мяч в ворота."
    th "...Ждать, дышать, бежать и видеть..."
    window hide

    stop music fadeout 1
    $ set_mode_adv()

    with flash    
    play music ndm_list['RF_memory_2'] fadein 1

    window show
    usp "А-а-ай."
    "Нога Ульяны подкосилась, и она прокатилась коленкой по земле."
    "Это я как будто почувствовал на себе.{w} Будто упала не Ульяна, а я."
    th "...и терпеть."
    window hide

    scene bg ext_playground_day with fade
    $ renpy.pause (1)

    window show
    "Я выбежал из-за угла, и буквально за пять секунд добежал до Ульяны."
    window hide

    $ renpy.pause (1)

    window show
    nd_il "Тебе больно?"
    th "Тупой вопрос..."
    us "А-ай"
    "По щеке Ульяны медленно прокатилась слеза."
    nd_il "Прости меня.{w} Я отнесу тебя к медсестре и всё будет нормально..."
    window hide

    show black with dissolve2
    play sound_loop sfx_run_forest fadein 1

    window show
    "Я не обращал внимание на пионеров, которые смотрели на меня то ли осуждающе, то ли с уважением, то ли с сочувствием."
    "Сейчас мне больше всего хотелось, чтобы Ульяне вновь стало лучше."
    window hide

    stop sound_loop fadeout 2
    scene bg ext_aidpost_day with dissolve2

    play sound sfx_knock_door2

    window show
    "Дойдя до домика медсестры, я постучал носком в дверь."
    play sound sfx_open_door_clubs
    show cs normal at center with dspr
    "Из него показалась уже знакомая мне медсестра в белом халате."
    cs "Здравствуй, пионер, что случилось?"
    "Увидев Ульяну на моих руках, медсестра забеспокоилась."
    nd_il "Я не профессионал но, кажется, она подвернула ногу."
    hide cs with dspr
    "Только я успел сказать, но медсестра уже среагировала."

    scene bg int_aidpost_day with dissolve
    play ambience ambience_medstation_inside_day fadein 2

    "Она подбежала к стеклянному шкафу, и принялась искать препараты.{w} А я положил Ульяну на кровать, подложил ей под голову какое-то скомканное одеяло и зафиксировал обе ноги в согнутом положении."
    "У Ульяны на коленке был порез, и это был не томатный сок."

    "Медсестра подбежала к нам с темной коричневой баночкой с надписью «Йод», и взяв ватную палочку, намазала на рану девочки."
    us "А-а-й!"
    "Закричала Ульяна, и схватила меня за руку." 
    "Я вдруг вспомнил, как один раз расшиб коленку на улице, и как мне мама намазала рану йодом.{w} Это было очень больно."
    vg "Кстати, я ещё тогда тебе говорил: не надо ездить на велосипеде, если не умеешь нормально тормозить."

    cs "Пионер, сними с неё обувь, я посмотрю насколько всё сложно."
    window hide

    $ renpy.pause (0.4)
    
    window show
    "Я аккуратно развязал шнурки и снял с ног Ульяны оба кроссовка."

    vg "Третий день в лагере, а уже раздеваешь свою подругу?"
    th "Ой, только тебя тут не хватало..."

    nd_il "Ульяна, какая нога болит?"
    us "Правая."

    "Так-же аккуратно сняв носок с правой ноги, я оценил её состояние." 
    "Это не было похоже на что-то серьезное.{w} Скорее всего, просто мышцу потянула."

    show cs normal glasses at center with dspr

    "Медсестра подошла, надела очки и осмотрела ногу пострадавшей."
    window hide

    $ renpy.pause (1)

    window show
    "В результате осмотра, специалистом был вынесен вердикт."
    cs "Не размяла мышцы перед нагрузкой.{w} В футбол играли?"
    us "Да, Виола Сергеевна."
    cs "Понятно. Я пойду за вожатой, а ты следи, чтобы твоя подруга не вставала."
    window hide

    stop music fadeout 3
    play sound sfx_open_door_clubs
    $ renpy.pause (1)
    hide cs with dspr
    $ renpy.pause (1)
    play sound sfx_close_door_1
    $ renpy.pause (1)

    window show
    th "Хорошо, что я успел вовремя.{w} Вот насчет чего меня предупреждал тот голос..." 
    th "Интересно, кому он принадлежит?{w} И почему он предсказывает будущее?"
    
    show us normal sport at right with dspr

    us "Илья, спасибо, что заботишься обо мне."
    
    show us grin sport at right with dspr
    
    us "Быть маленькой не так уж и плохо."
    "Ульяна тихо хихикнула."
    window hide

    $ renpy.pause (1)

    window show
    nd_il "Сильно нога болит?"
    
    show us sad sport at right with dspr
    
    us "Да, не могу даже пошевелить, больно."

    nd_il "Так мы сейчас это исправим."
    
    hide us with dspr
    
    "Сказал я, и подойдя к шкафчику с прозрачными дверцами достал оттуда шприц, снял с него иглу и показал его Ульяне."
    
    show us fear sport far at center with dspr
    
    us "Не надо!"
    nd_il "Чего кричишь? Он даже без иглы, смотри."
    
    show us normal sport far at center with dspr
    
    "Я показал Ульяне шприц ещё раз."
    
    show us calml sport far at center with dspr
    
    us "Не пугай меня тогда, негодяй."

    "Сказала Ульяна и погрозила мне пальцем." 
    "Её лицо было слишком серьезным для моей психики, и я засмеялся в голос."
    hide us with dspr
    show black with dissolve
    "Мой смех был настолько заразительным, что его подхватила Ульяна{w}, а вскоре и ещё какой-то пионер на улице."
    window hide

    $ renpy.pause (2)

    hide black with dissolve
    play sound sfx_knock_door2

    window show
    "Но наш смех прервал настойчивый стук в дверь."
    nd_il "Ульяна, я проверю кто там, а ты не вставай."

    "Ульяна подмигнула мне, и я вышел на улицу."
    window hide

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_clubs
    scene bg ext_aidpost_day with dissolve2
    play ambience ambience_camp_center_day fadein 2
    play sound sfx_close_door_1
    $ renpy.pause (1)
    show vst normal pioneer at center with dspr
    $ renpy.pause (1)

    window show
    "Меня встречал какой-то пионер, которого я ещё ни разу не видел в этом лагере."
    "Он был немного похож на Семёна."
    nd_il "Здравствуй.{w} Ты к медсестре?"
    show vst surprise pioneer at center with dspr
    pi "Да, а где она?{w} Мне бы бегунок подписать."
    nd_il "Она ушла к вожатой. Так что можешь пока взять роспись в спортивном кружке."
    pi "Но его нет в списке."
    nd_il "Переверни бегунок."
    window hide

    hide vst with dspr

    $ renpy.pause (1)
    
    window show
    "Он перевернул листок и, заметив ещё одно место для подписи, почесал голову."
    pi "Спасибо. Как тебя звать?"
    nd_il "Илья, а тебя как?"
    show vst smile pioneer at center with dspr
    vst_lar "Василий, можешь звать просто Вася."
    th "Да этого не может быть.{w} Просто совпадение."
    vst_lar "Ладно, я пошел. Ещё увидимся."
    window hide

    $ renpy.pause (1)
    hide vst with dspr
    $ renpy.pause (1)
    
    window show
    "Действительно, совпадение."
    window hide

    $ renpy.pause (2, hard=True)
    
    window show
    "Я уже собирался зайти обратно в медпункт, как заметил на небе темное дождевое облако."
    "Определенно, сегодня вечером должен был пойти дождь.{w} И этот факт не мог меня никак не радовать."
    "Я уже представлял, как буду спать сегодня под успокаивающие звуки дождя..."
    window hide

    $ renpy.pause (1)

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_clubs
    $ renpy.pause (1)
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_aidpost_day with dissolve

    window show
    "Ульяна лежала на кровати с закрытыми глазами и посапывала."
    play sound sfx_close_door_1
    "Я попытался тихо закрыть за собой дверь, но та непослушно хлопнула, и Ульяна открыла глаза."
    window hide

    $ renpy.pause(1)

    show us normal sport far at right with dspr

    window show
    us "Ну кто там?"
    nd_il "Да так, просто новенький какой-то."
    us "Ясно."
    window hide

    $ renpy.pause(1)
    hide us with dspr
    
    window show
    nd_il "Кстати, к вечеру дождь будет."
    
    show us sad sport far at right with dspr
    
    us "Как это? Значит танцы отменят?"
    
    show us normal sport far at right with dspr
    
    nd_il "Не расстраивайся. Вожатая что-нибудь придумает..."
    us "Угу..."
    window hide

    $ renpy.pause(1)
    hide us with dspr

    window show
    "Ульяна вновь положила голову на подушку."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я лёг на вторую кровать, закрыл глаза и задумался."
    window hide

    $ renpy.pause(1)
    show blink
    
    $ renpy.pause(1)

    window show
    th "А может это не совпадение?{w} Может это он подложил мне записку утром?.."
    window hide

    $ renpy.pause(1)

    window show
    us "Илья."
    window hide

    show us normal sport far at center
    hide blink
    show unblink

    $ renpy.pause(2)

    window show
    us "Расскажи что-нибудь."
    nd_il "О чем?"
    us "Ну о чем-нибудь..."
    th "Да о чём же я ей расскажу?"
    th "А может..."
    nd_il "Хочешь я тебе расскажу историю про одного мальчика, который попал из будущего в прошлое?"
    us "Хочу."
    window hide

    hide us with dspr
    
    $ renpy.pause(1)

    window show
    "Я начал свой рассказ..."
    window hide

    stop ambience fadeout 3
    play music ndm_list['toxicity_1'] fadein 4
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Это было заснеженной зимой две тысячи восемнадцатого года."
    "В это время в одной квартирке живёт мальчик по имени... {w}Женя. Ему 18 лет, и он выполняет заказы через новейшие технологии.{w} Он может доставлять еду не выходя из дома, работать не выходя из дома, {w}ну и тому подобное."
    "Но однажды ему приснился сон, где он стоит у ворот неизвестного ему лагеря."
    "Этот сон показался ему странным и очень реалистичным.{w} И решил он рассказать об этом своему лучшему другу, который посоветовал обратиться Жене к психотерапевту."
    "Вот Женя выходит из своего дома, садится на летающий автобус, и отправляется на место."
    "Вдруг ему очень сильно захотелось спать.{w} Женя закрыл глаза и уснул."

    nvl clear

    "Прошёл час{w}, прошёл ещё час.{w} Долго спал Женя."
    "Вдруг автобус остановился, он открыл глаза и заметил, что он приехал не к психологу, а в самый настоящий лагерь."
    "Посмотрев на свои часы он понял, что помимо того, что он оказался в нескольких сотен километров от дома, так он ещё и в прошлом…"
    window hide

    stop music fadeout 3
    play ambience ambience_int_cabin_day fadein 3
    $ set_mode_adv()
    $ renpy.pause(1)
    
    window show
    "Я встал с кровати и подошёл к Ульяне."
    window hide

    $ renpy.pause(1)
    
    window show
    "Она лежала на боку и тихонько посапывала.{w} Видимо, она очень устала."
    "Когда она спит, она похожа на ангела. Такого милого и беззащитного." 
    "Я представил, как она обхватывает мою шею своими руками и прижимает к себе."
    "А я чувствую запах её волос..."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Я просто больной."
    th "Навряд ли до этого когда-нибудь дойдет..."
    window hide

    $ renpy.pause(2)
    show blink
    $ renpy.pause(1)
    stop ambience fadeout 3

    window show
    "Я лёг на свою кровать, положил руки под голову и закрыл глаза."
    window hide

    $ renpy.pause (3)

    jump dream_d2_oldbuilding_night

label dream_d2_oldbuilding_night:

    $ nd_change_time('prolog')
    
    $ renpy.pause (3)

    play ambience ambience_old_camp_outside fadein 3
    play music ndm_list['toxicity_2'] fadein 3 
    show ext_old_building_night_moonlight
    show prologue_dream
    with dissolve
    
    window show
    "Вот я стою перед заброшенным зданием. Оно выглядит довольно высоким и старым."
    "Вокруг меня встал тёмный лес, манящий своей загадочностью, но заброшенное здание выглядит куда маняще."
    window hide

    scene black with dissolve
    stop ambience fadeout 2
    $ renpy.pause (2)
    scene bg int_old_building_night
    show prologue_dream
    with dissolve
    play ambience ambience_catacombs fadein 3
    
    window show
    "Пройдя внутрь, я увидел что-то вроде прихожей."
    "По средине стоял поломанный стол, который был довольно потрёпан временем, как и всё, что находилось внутри этого жуткого дома." 
    "Больше всего мне хотелось убежать подальше, но ноги меня никак не хотели слушаться."
    "Они повели меня к какому-то люку, откуда доносились неопознанные голоса."
    window hide

    $ renpy.pause (1)

    window show
    dream_voices "Не плачь. Мы найдём выход отсюда…"
    window hide

    stop music fadeout 2

    show black with flash
    stop ambience fadeout 2
    $ renpy.pause (1)
    
    if d2_dv_night_pristan == False:
        jump d2_poldn_us_notdream
    
    else:
        jump d2_poldn_dv_notdream

label d2_poldn_dv_notdream:

    $ renpy.pause (3)

    $ nd_change_time('sunset')

    play ambience ambience_int_cabin_evening fadein 4
    scene bg int_house_of_gg_sunset
    with flash

    $ renpy.pause (2)

    window show
    "Я разомкнул веки и проснулся...{w} у себя в домике."
    "На улице слегка светило солнце, лучи которого просачивались через темные тучки."
    window hide

    $ renpy.pause (1)

    window show
    "Я был в недоумении,{w} ведь я точно засыпал не в домике, а на зрительском месте у сцены..."
    th "А может это всё просто сон?{w} А я на самом деле всё это время спал?"
    th "Нет, меня бы уже давно разбудили здешние пионеры или, на крайний случай, Алиса с Ульяной."
    window hide

    $ renpy.pause (1)

    play sound sfx_dinner_horn_processed

    window show
    "Мысли в голове прервал гудок из динамиков."
    th "Похоже, мне в столовую.{w} Как раз там и спрошу, что со мной произошло."
    th "Хотя это будет звучать тупо, если я спрошу: \"Алиса, ты звала меня на свидание перед тихим часом?\" или \"Алиса, как я попал в свой домик, если отрубился, слушая твою игру на электрогитаре\"."
    th "Скорее всего, тогда и свидания уже не будет."
    th "Кто в здравом уме захочет общаться и проводить время с шизанутым \"пришельцем из будущего\"?"
    window hide

    play sound sfx_open_door_1
    show black with dissolve

    window show
    "C этими мыслями я покинул свои апартаменты и отправился в столовую."
    window hide

    play sound sfx_close_door_1

    stop ambience fadeout 4
    $ renpy.pause (1)
    play ambience ambience_camp_center_evening fadein 4

    window show
    "На улице покрапывал мелкими капельками дождик.{w} Он был достаточно мелким, чтобы его не замечать."
    "Правда, было интересно, как мы будем готовить площадь к танцам, если дождь к этому времени не закончится и еще сильнее наберет обороты."
    window hide

    $ renpy.pause (2)
    scene bg ext_dining_hall_away_sunset with dissolve2 
    $ renpy.pause (1)
    scene bg ext_dining_hall_near_sunset with fade

    show mt normal pioneer at center with dspr

    window show
    "У входа в столовую меня встретила Ольга Дмитриевна."
    mt "Илья, не забудь про библиотеку."
    nd_il "Не забуду."
    window hide

    play sound sfx_open_door_1
    play ambience ambience_dining_hall_full fadein 2
    scene bg int_dinning_hall_people_rain_2 with dissolve
    
    $ renpy.pause (1)

    window show
    th "Вот блин, только проснулся, а уже работать заставляют."
    vg "Бедолага..."
    window hide

    $ renpy.pause (1)

    window show
    "Я взял свою порцию и нашел целый свободный стол, без никого и без ничего."
    "Был еще вариант сесть с Леной, но мне не очень хотелось сейчас разговаривать.{w} Лучшим сейчас было уединиться с собой и подумать. "
    window hide

    $ renpy.pause (1)

    window show
    "Я, естественно, без всяких задумок сел за подаренный мне судьбою свободный стол."
    window hide

    $ renpy.pause (2)

    window show
    th "Если это был не сон,{w} и Алиса меня правда позвала смотреть на звезды,{w} тогда нужно подготовиться, одеться как-нибудь нормально,{w} потому что в этой пионерской форме идти на свидание - это, извините меня, извращение."
    "Внезапно из хриплых динамиков раздался голос вожатой..."
    dy "В связи с неблагоприятными погодными условиями танцы будут проводиться в спортзале спортивного кружка."
    window hide

    $ renpy.pause (2)

    show dv smile pioneer at left
    show us smile pioneer at right
    with dspr

    window show
    "По окончанию сообщения вожатой, ко мне, словно по команде, подсели девочки, о которых я недавно вспоминал{w} - Алиса и Ульяна, тем самым выведя меня из раздумий."
    dv "Добрый вечер, сонный герой."
    nd_il "Привет."
    window hide

    $ renpy.pause (2)

    show dv grin pioneer at left with dspr

    window show
    dv "Илья, ты видел эти новые плакаты?{w} Бред конечно, но вон тот, что со стишком, выглядит оригинально."
    "Алиса показала на мой плакат, который я делал в библиотеке."
    nd_il "Рад, что тебе понравилось.{w} Это я плакаты ходил рисовать, а потом вышел этот шедевр."  
    window hide

    $ renpy.pause (1)

    show dv normal pioneer at left with dspr

    window show
    us "Илья, а куда ты сейчас собираешься идти?"
    nd_il "Я, наверное, сейчас пойду в библиотеку убираться. А ты?"

    show us smile pioneer at right with dspr
    
    "Ульяна подозрительно улыбнулась, будто что-то замыслила."
    us "А я пойду готовиться к танцам."
    
    hide us with dspr
    hide dv with dspr
    
    "И после этих слов она побежала на выход из столовой."

    show dv shy pioneer at center with dspr
    dv "Ладно, я тоже пойду.{w} И не забудь за вечер."
    hide dv with dspr

    "Сказала Алиса и пошла за своей подругой."
    window hide

    $ renpy.pause(1.5)
    show black with dissolve
    $ renpy.pause(1)    
    
    window show
    "Я тоже в столовой на долго не задержался."
    "Отнеся поднос, я свободно вышел из столовой..."
    window hide

    stop ambience fadeout 3

    $ renpy.pause(2)
    jump library_us_pavuk


label d2_poldn_us_notdream:

    $ nd_change_time('sunset')

    $ renpy.pause (2)
    play ambience ambience_int_cabin_evening fadein 2
    
    $ renpy.pause (1)

    scene bg nd_int_aidpost_sunset
    hide blink
    show unblink
    
    $ renpy.pause (2)

    window show
    "Проснувшись, я оказался в медпункте совсем один.{w} Ульяны на своём месте не было."
    "Я не помнил, что мне снилось.{w} Но главное, что я отдохнул, и был готов продолжить свое времяпровождение в этом лагере."
    window hide

    $ renpy.pause (1)
    
    window show
    th "Быстро Ульяна поправилась.{w} Иногда сон действительно лечит."
    window hide

    $ renpy.pause (1)

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_clubs
    $ renpy.pause (1)
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_aidpost_sunset with dissolve
    play sound sfx_close_door_1

    show cs normal far at center with dspr
    
    window show
    "Выйдя из медпункта, я заметил на улице накрапывающий мелкими капельками дождик и идущую ко мне на встречу медсестру."
    show cs normal at center with dspr
    cs "Проснулся, пионер?"
    cs "Ты ведь полдник проспал.{w} Поторопись — из-за дождя его сдвинули, ещё дают."
    hide cs with dspr
    nd_il "Уже иду..."
    window hide

    $ renpy.pause (1)
    show black with dissolve2
    $ renpy.pause (1)
    
    window show
    "Несмотря на мелкий дождик, солнце не стеснялось и дальше согревать лагерь своими лучами."
    "Что было немного странным. Ведь ничего подобного я до этого момента не видел."
    window hide

    $ renpy.pause (2)
    scene bg ext_dining_hall_away_sunset with dissolve2 
    $ renpy.pause (1)
    show black with dissolve
    $ renpy.pause (1)
    scene bg ext_dining_hall_near_sunset with fade
    $ renpy.pause (1)
    show mt normal pioneer at center with dspr

    window show
    "У входа в столовую меня встретила наша вожатая - Ольга Дмитриевна."
    mt "Не забудь про уборку в библиотеке."
    nd_il "Не забуду."
    window hide

    hide mt with dspr

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause (2)
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dinning_hall_people_rain_2 with dissolve2
    play sound sfx_close_door_1
    
    $ renpy.pause (1)

    window show
    th "Вот блин, только проснулся, а уже работать заставляют."
    window hide

    $ renpy.pause (1)
    
    window show
    "Я взял свою порцию и занял свободное место за одним из столов.{w} И это место было среди Алисы и Ульяны."
    window hide 
    
    $ renpy.pause (1)

    show dv smile pioneer at left
    show us smile pioneer at right
    with dspr

    window show
    dv "Привет, сонный герой."
    nd_il "Привет Алиса."
    window hide

    $ renpy.pause (1)
    
    window show
    nd_il "Сегодня вечером будем чилить. Ты идёшь на пати? Только без кринжа."
    show us surp1 pioneer at right 
    show dv shocked pioneer at left
    with dspr
    "Девочки непонимающе посмотрели на меня, а я продолжил потчевать."
    us "Илья, а что ты только что сказал?"

    nd_il "Не бери в голову.{w} Как твоя нога?{w} Ты идёшь сегодня на танцы?"
    show us sad pioneer at right with dspr 
    us "Болит чуть-чуть, но танцевать я всё равно буду."
    show dv grin pioneer at left with dspr
    dv "У неё готовится интересный сюрприз для тебя."
    show us surp3 pioneer at right with dspr
    us "Не для него!"
    dv "А для кого? Для Сыроежкина?"
    us "Нет..."
    hide dv 
    hide us
    with dspr
    th "Вот блин. Будет интересно посмотреть, что подготовит Ульяна..."

    "Подумал я, и принялся доедать свой полдник, пока девочки отвлечены своим разговором."
    "Иначе, предчувствую, поесть мне нормально не удастся."
    window hide

    $ renpy.pause (1)
    
    window show
    "Пока я ел, я много думал.{w} И не только о танцах, уборке и Ульяне с Алисой."
    "Мне было интересно узнать этого новенького Василия получше."
    "Хотя, может лучше его пока не трогать?"
    window hide

    $ renpy.pause(1)

    window show
    "Внезапно из хриплых динамиков раздался голос вожатой."
    dy "В связи с неблагоприятными погодными условиями танцы будут проводиться в спортзале спортивного кружка."
    dy "Ужина не будет."

    show dv normal pioneer at left
    show us smile pioneer at right
    with dspr

    dv "А я думала, что эти танцульки отменят."

    nd_il "Да ладно тебе, пофлексим, почилим, и всё нормально будет."
    window hide

    $ renpy.pause(2)

    show dv angry pioneer at left with dspr
    show us surp2 pioneer at right with dspr

    window show
    dv "Достал. Давай объясняй, что это значит."
    nd_il "Ну смотри, флексить — это значит двигаться в такт музыке.{w} Чилить — значит отдыхать с друзьями.{w} А кринж — это стыд или позор.{w} А ещё есть такое понятие, как низкий флекс…"
    window hide

    $ renpy.pause(1)

    show black with dissolve 

    hide dv
    hide us 
    with dspr

    window show
    "Я рассказывал всю эту модную фигню, а девочки меня внимательно слушали."
    window hide

    $ renpy.pause(1)
    hide black with dissolve
    $ renpy.pause(1)

    show dv smile pioneer at left
    show us normal pioneer at right
    with dspr

    window show
    "Когда я закончил перечислять все эти новомодные понятия, Алиса улыбнулась."
    dv "Ладно, иностранец. На этот раз отмазался."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Чуть не убила."
    window hide

    $ renpy.pause(1)
    show dv grin pioneer at left with dspr
    
    window show
    dv "Илья, ты видел эти новые плакаты?{w} Бред конечно, но вон тот, что со стишком ничего-так."
    "Алиса показала на мой плакат, который я делал в библиотеке."
    nd_il "Рад, что тебе понравилось.{w} Это я плакаты ходил рисовать, а потом вышел этот шедевр."
    window hide

    $ renpy.pause(1)
    show dv normal pioneer at left with dspr
    
    window show
    us "Илья, а куда ты сейчас собираешься идти?"

    nd_il "Я, наверное, сейчас пойду в библиотеку убираться. А ты?"
    
    show us smile pioneer at right with dspr
    
    "Ульяна подозрительно улыбнулась, будто что-то замыслив."
    us "А я пойду готовиться к танцам."
    
    hide us with dspr

    "И после этих слов она побежала на выход из столовой."
    th "Походу, она правда что-то от меня скрывает..."
    
    show dv smile pioneer far at left with dspr
    
    dv "Ладно, я тоже пойду.{w} Вечером увидимся."
    
    hide dv with dspr
    
    "Сказала Алиса и пошла за своей подругой.{w} Но в отличие от неё, она убрала свой поднос."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Опять Ульяна на меня посуду оставляет. Так уж и быть..."
    th "Клянусь, я делаю это в последний раз."
    window hide

    $ renpy.pause(1.5)
    
    stop ambience fadeout 3
    show black with dissolve
    
    window show
    "Отнеся поднос за собой и за Ульяной, я вышел на улицу."
    window hide

    $ renpy.pause(2)

    jump library_us_pavuk

label library_us_pavuk:
    

    play ambience nda_list['indoors_evening'] fadein 3
    
    scene bg ext_dining_hall_away_sunset with dissolve2 
    play sound sfx_close_door_1

    $ renpy.pause(1)

    window show
    "Погода была не очень хорошая. Покрапывал дождик и солнышко спряталось за тучку."
    "Но бояться этого дождя было нечего.{w} Его капли были тёплыми, и падали довольно редко."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Теперь нужно выполнить обещанное..."

    show black with dissolve
    stop ambience fadeout 3
    
    "Подумал я, и побежал в сторону \"кладовой книг\" пионерлагеря \"Совенок\"."
    window hide

    $ renpy.pause(2)
    play sound sfx_knock_door2
    $ renpy.pause(2)
    play sound sfx_open_door_clubs
    play ambience ambience_library_day fadein 2
    scene bg int_library_sunset with dissolve2
    play sound sfx_close_door_1

    window show
    "По приходу в библиотеку я увидел Славю и Мику, убирающихся на полках."

    show sl smile pioneer far at left
    show mi smile pioneer far at right 
    with dspr

    sl "О, привет Илья. Пришёл книги расставлять?"

    nd_il "Ну, да. Вам помочь?"

    mi "Конечно. Нам осталось пару шкафов убрать. Сейчас быстро управимся."
    hide mi
    hide sl
    with dspr

    "Мы начали уборку."

    "Так как девочки были ниже меня ростом, то и убирали нижние книжные полки, а я верхние."
    window hide

    $ renpy.pause(1)    
    show black with dissolve
    $ renpy.pause(1.5)
    hide black with dissolve
    $ renpy.pause(1)
    
    window show
    "Вот так мы убрали первый шкаф.{w} Теперь оставалось убрать второй."
    "Мне показалось странным, что библиотекарши нет на своём месте.{w} Всё-таки глаз уже привык, что она либо спит, либо читает какую-то книгу."

    nd_il "А где библиотекарша?"
    mi "Не знаю, но думаю, что она очень обрадуется, что мы убрались в её библиотеке."
    "Сказала Мику, попутно протирая пыль с полок."

    sl "Это точно."
    window hide

    show black with dissolve 
    $ renpy.pause(1)
    hide black with dspr

    window show
    "Вскоре с уборкой было закончено."
    "Я стряхнул пыль с рук, и было хотел сказать про подготовку к танцам{w}, но увидел, как со стены на меня смотрит огромный... Паук!"
    # Еле как удержался написать ПАВУК. 
    nd_il "Кажется, у нас гость."

    show mi smile pioneer at fleft with dspr

    mi "Давайте его выпустим!"

    th "Надеюсь, этим буду заниматься не я."
    "Подумал я, и хотел выйти, но этот паук спустился на дверь..."
    window hide

    $ renpy.pause(1)

    window show
    "...А затем и на ручку этой двери."

    th "Отлично, теперь я взаперти."

    show sl laugh pioneer at right with dspr

    sl "Илья, ты что, паука испугался?"

    nd_il "Да нет…"
    "..."
    nd_il "Да."

    show sl smile pioneer at right with dspr

    sl "Сейчас я этого друга выпущу..."

    hide sl with dspr
    hide mi with dspr

    if d2_dv_night_pristan == True:
        "Сказала Славя и убежала в конец библиотеки, в ту комнатку, где мы c Алисой рисовали Плакат для нашего клуба."
    else:
        "Сказала Славя и убежала в конец библиотеки, в ту комнатку, где мы рисовали плакаты."
    window hide

    $ renpy.pause(2)

    show sl normal pioneer at center with dspr

    window show
    "Cпустя несколько секунд она вышла оттуда с картонной коробкой."

    sl "Сейчас покажу, как это делается."
    window hide

    hide sl with dspr
    $ renpy.pause(1)

    window show
    "Сказала Славя и поставила коробку над пауком."

    play sound sfx_open_door_clubs fadein 2
    
    "Тот послушно залез внутрь, и Славя открыла дверь."
    window hide

    $ renpy.pause(1)

    window show
    "Вытащив коробку на улицу, Славя аккуратно перевернула её на бок, и я увидел уползающего вдаль паука."
    window hide

    $ renpy.pause(1)
    play sound sfx_close_door_1
    $ renpy.pause(1)
    show sl laugh pioneer at center with dspr

    window show
    sl "Трусиха ты, Илья."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ну и ладно.{w} Я пойду в спортзал к танцам его готовить."
    
    show sl smile pioneer at center with dspr
    show mi smile pioneer far at fright with dspr
    mi "Передай Ольге Дмитриевне, что мы тоже сейчас придём."
    hide sl
    hide mi
    with dspr
    nd_il "Обязательно."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_door_clubs
    stop ambience fadeout 3
    show black with dissolve2

    window show
    "После уборки библиотеки и диалога с девочками, я отправился к зданию спортивного кружка."
    window hide

    $ renpy.pause(1)
    play sound sfx_close_door_1
    play ambience nda_list['indoors_evening'] fadein 3

    $ renpy.pause(1)
    play sound_loop sfx_far_steps fadein 2
    $ renpy.pause(2)

    window show
    vg "Не могу не согласится со Славей."
    nd_il "Да ты же видел, какой он огромный."
    vg "Оправдывайся…"
    window hide

    $ renpy.pause(2)
    stop sound_loop fadeout 2
    $ renpy.pause(1)

    play sound sfx_open_door_1
    $ volume(0.5, 'ambience')
    play ambience nda_list['indoors_evening'] fadein 3

    $ renpy.pause(1)
    play sound sfx_close_door_1
    play sound_loop sfx_steps_clubs_nextroom
    $ renpy.pause(1)
    stop sound_loop fadeout 2
    play sound sfx_open_door_clubs
    scene bg int_sporthall_sunset_rain with dissolve2

    window show
    "Дойдя до спортзала, я увидел следующую картину."
    "Шурик и Электроник вешают гирлянды, Ольга Дмитриевна ими командует, а Лена и Женя о чём-то разговаривают…"
    "В общем, кипела работа."

    mt "Илья, иди сюда. Помоги кибернетикам гирлянды повесить."

    nd_il "Хорошо, Ольга Дмитриевна.{w} Сейчас ещё Славя и Маша подойдут."

    "Ответил я вожатой, а затем подошёл к кибернетикам,{w} пристально рассматривающим гирлянду."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Вам помощь нужна?"

    sh "Да, подержи пока вон тот конец провода, а мы закинем вон туда наверх."
    "Шурик показал на выемки, за которые должна цепляться гирлянда."
    "Они были над окнами, и одним им действительно было не справиться."
    window hide

    $ renpy.pause(2)
    
    show black with dissolve

    window show
    "Я подошёл к одному концу гирлянды и взял его в руки."
    window hide

    $ renpy.pause(1)

    window show
    "Электроник и Шурик ловко закинули гирлянду за кольцо."

    el "Отлично, давай теперь зацепим по бокам спортзала."
    sh "Давай."

    "Мы закрепили гирлянду сначала у двери, а потом у окна, и получалось так, что гирлянда теперь была над импровизированным танцполом."

    sh "Теперь закрепим гирлянду за второе кольцо. Илья, держи вон тот провод, чтобы ничего не оторвалось."

    "Я крепко взялся за провод, и кибернетики без труда закинули гирлянду на второе кольцо,{w} а затем нажали на кнопку включения."
    "Огоньки загорелись разными цветами, плавно затухая и загораясь вновь."
    
    scene bg int_sporthall_sunset_pred with dissolve2

    "Было поистине красиво.{w} А если включить их вечером…"
    
    sh "Отлично. Спасибо за помощь, Илюх."
    sh "Можешь ещё кое где нам помочь?"
    nd_il "Без проблем.{w} Что нужно делать?"
    sh "Буду краток, нужна помощь с колонками. Сможешь подключить?"
    nd_il "Да, приходилось уже так делать."
    el "Тогда подключи колонки, пока мы с Шуриком настроим проигрыватель."
    nd_il "Будет сделано."
    window hide


    show black with dissolve
    $ renpy.pause(1)

    window show
    "Я подошёл к сабвуферу."
    "В теории, способ подключения таких колонок почти ничем не отличался от способа подключения современных."
    "Я соединил цепь красными и чёрными проводами, подсоединив всё это дело к сабвуферу, и попытался включить через пульт."
    "На моё собственное удивление, всё заработало с первого раза."
    "Хотя подключением аудиосистем я занимался очень давно."
    window hide

    $ renpy.pause(1)
    hide black with dissolve 
    $ renpy.pause(1)
    
    window show
    nd_il "Я сделаль!"
    "Закричал я кибернетикам через весь зал."
    "Те быстрым шагом подошли ко мне и осмотрели сделанную мной работу."
    window hide
    
    $ renpy.pause(1)
    
    window show
    el "Быстро ты справился. Мы с Шуриком час пытались разобраться, как это работает."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Странно, что на сцене колонки уже были подключены."
    th "Вероятно, их подключали кибернетики с прошлого отряда."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ну я просто уже знал, как это делается…"
    nd_il "Профессионализм..."
    window hide

    $ renpy.pause(1)
    
    window show
    "Наш разговор прервала Ольга Дмитриевна."

    mt "Спасибо всем, кто помогал в подготовке к танцам."
    mt "Теперь вы можете пойти к своим домикам, и переодеться к предстоящему мероприятию."

    stop ambience fadeout 3
    show black with dissolve

    "После сообщения вожатой, пионеры поспешно пошли на выход из спортзала.{w} В том числе Славя и Маша.{w} И я."
    window hide

    $ renpy.pause(1)

label prep_dance_sem_d3_nd:

    play sound sfx_open_door_clubs
    $ renpy.pause(2)
    play sound sfx_close_door_1
    $ renpy.pause(1)
    $ volume (1.0, 'ambience')
    play ambience nda_list['indoors_evening'] fadein 3
    scene bg ext_playground_prerain with dissolve2

    $ renpy.pause(1)

    window show
    "Я вышел на футбольную площадку."
    "С севера поддувал легкий ветерок."
    "Воздух был немного влажным, скорее всего из-за приближающейся погоды."
    th "Фу-ух, теперь нужно переодеться во что-нибудь чистое. Но где его взять?"
    th "Может на складе? Ключи от него у Ольги Дмитриевны, но почему я должен её отвлекать своими заботами?.."

    show pi2 smile pioneer at cright with dspr
    "Вдруг ко мне подошёл Семён."

    me "Привет, Илюх, чего загрустил?"
    nd_il "Не грущу я."
    window hide

    $ renpy.pause(1)

    if d2_dv_night_pristan == True:
        window show
        nd_il "Скоро танцы, а я не знаю во что переодеться."
        nd_il "Вещей я сюда с собой не привёз."
        "Я решил ему немного соврать. Ибо не хотелось говорить о своем \"свидании\" с Алисой."
        me "Так это не беда. Можешь считать меня своим стилистом."
        nd_il "У тебя есть вещи под мой размер?"

    else:
        window show
        nd_il "Скоро танцы, а я не знаю во что переодеться."
        nd_il "Вещей я сюда с собой не привёз."
        me "Так это не беда. Можешь считать меня своим стилистом."
        nd_il "У тебя есть вещи под мой размер?"
    
    hide pi2 smile pioneer with dspr
    show pi2 grin pioneer at center with dspr

    me "Не у меня, у вожатой, с которой мне приходится жить."
    me "Пошли за мной.{w} Станешь таким красавцем, что даже библиотекарша поломается."
    me "Поверь, я пробовал."
    "Его слова звучали более чем убедительно."
    nd_il "Ладно, заинтересовал, пошли."
    window hide

    hide pi2 pioneer grin with dspr 
    show black with dissolve
    
    $ renpy.pause(1)

    play sound_loop sfx_far_steps fadein 3

    window show
    th "Он, наверное, ко всему лагерю подкатывал пока меня не было.{w} Даже к вожатой."
    th "Кстати…"

    nd_il "А разве вожатая не захочет сама переодеться для танцев?"
    me "Мы её опередим."
    window hide

    $ renpy.pause(3)

    stop sound_loop fadeout 3

    scene bg ext_house_of_mt_prerain with dissolve2

    window show
    "Вскоре мы дотащились до домика вожатой.{w} Того самого, на другом конце лагеря."
    me "Давай я проверю домик.{w} Подожди."

    "Сказал Семён и, обойдя домик, показал мне большой палец."

    th "Значит никого."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 3
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience nda_list['light_rain_inside'] fadein 2
    scene bg mt_house_rain with dissolve2
    play sound sfx_close_door_1

    window show
    "Я поспешно вошёл в домик, а за мной в него зашёл Семён."

    "Внутри и вправду никого не было."
    "Семён начал рыться то в своём шкафчике, то в шкафчике вожатой, выбрасывая оттуда модные шмотки."
    "Ну, модные на то время."

    th "Я офигею, если у него есть джинсы с дырками."
    me "Джинсы с дырками пойдут? Или тебе обычные?"
    th "Да ладно, серьезно?"
    nd_il "Обычные."
    me "Тогда держи."
    "Семён не глядя бросил в меня светлые джинсы."
    me "Давай теперь рубашку тебе подберём..."
    window show

    $ renpy.pause(2, hard=True)

    window show
    "Пока он искал мне рубашку, мне представилась возможность разглядеть домик вожатой детальнее."
    "На стенах были полки как у меня в домике,{w} кровати и…{w} Постер с Фантомасом?!"

    show pi2 grin pioneer at center with dspr

    me "Что уставился на стены?{w} На, примеряй."
    "Семён всучил мне в руки темную рубашку и джинсы."

    me "Если Ольга Дмитриевна придёт, и ты не хочешь, чтобы она увидела тебя в трусах, то спрячься за дверцу её шкафа."

    hide pi2 grin pioneer with dspr
    "Сказав это, он встал у двери, видимо подпирая её на случай, если вожатая таки пожалует в свой домик."
    window hide

    $ renpy.pause(1)

    show black with dissolve
    
    window show
    "Я зашёл за дверку шкафа и начал надевать свой вечерний костюм."
    window hide

    $ renpy.pause(1)
    play sound nds_list['applysuit']
    $ renpy.pause(1)
    hide black with dissolve
    $ renpy.pause(1)

    window show
    "На удивление, джинсы мне оказались в аккурат.{w} И рубашка тоже."
    window hide

    $ renpy.pause(0.5)
    hide black with dissolve
    $ renpy.pause(0.5)

    window show
    "Я вышел из-за дверцы шкафа и показался Семёну."

    show pi2 smile pioneer at center with dspr
    
    me "Во-о-т! Совсем другой парень."

    hide pi2 smile pioneer with dspr
    
    "Сказал Семён и показал большой палец, а затем вновь залез в свой шкафчик и, достав оттуда белую футболку, кинул её мне."
    
    show pi2 grin pioneer at right with dspr
    
    me "С черной рубашкой должно смотреться идеально."
    nd_il "Спасибо."
    me "Примеряй."
    window hide

    hide pi2 grin pioneer with dspr
    $ renpy.pause(0.5)
    show black with dissolve
    $ renpy.pause(0.5)

    window show
    "Я снова зашёл за дверцу шкафа, чтобы примерить футболку."
    window hide

    $ renpy.pause(2)
    play sound nds_list['applysuit']
    $ renpy.pause(1)

    window show
    "Она тоже мне отлично подошла.{w} Как так получается, что любая одежда, которую достает Семён из шкафчика, идеально подходит в соответствии с моим весом и ростом?"
    window hide

    $ renpy.pause(1)
    play sound sfx_open_door_clubs
    
    window show
    "Я был уже готов выйти из-за шкафа, как в домик вошла Ольга Дмитриевна."
    window hide

    $ renpy.pause(1)
    
    window show
    me "Ольга Дмитриевна. У нас в домике Илья. Я ему одежду подбираю на танцы."
    mt "Понятно, я тогда вас на улице подожду."
    window hide

    $ renpy.pause(0.5)
    play sound sfx_close_door_1
    $ renpy.pause(2, hard=True)
    hide black with dissolve

    window show
    "Я вышел из-за шкафа, и Семён оценивающе взглянул на меня."

    show pi2 normal pioneer at center with dspr

    me "Илья, я тебе футболку дал не для того, чтобы ты её рубашкой закрыл.{w} Расстёгивай."
    
    "Я послушался Семёна и расстегнул все пуговицы на рубашке."

    me "Так-то лучше. Теперь давай на выход из домика. Вожатая на улице ждёт."
    window hide

    hide pi2 normal pioneer with dspr

    play sound sfx_open_door_1
    $ renpy.pause(1)
    scene black with dissolve
    play ambience nda_list['rain_outside'] fadein 3
    $ renpy.pause(1)
    
    scene bg ext_house_of_mt_prerain
    show nd_light_rain_effect
    with dissolve2

    play sound sfx_close_door_1
    $ renpy.pause(1)

    show mt normal pioneer at center with dspr

    window show
    "На улице нас взглядом встретила Ольга Дмитриевна и небольшой дождик."
    
    show mt smile pioneer at center with dspr

    mt "Отлично выглядишь. Это тебя так Семён нарядил?"
    nd_il "Да, Ольга Дмитриевна."

    hide mt with dspr 

    play sound sfx_open_door_1
    "Мы с Семёном пропустили вожатую в домик."
    play sound sfx_close_door_1

    nd_il "Теперь и пригласить кого-нибудь не стыдно. А когда можно тебе эти вещи принести?"

    show pi2 smile pioneer at center with dspr

    me "Да на всегда забирай.{w} Ты хоть танцевать умеешь? Медляки там хотя-бы?"
    th "Вот блин."
    window hide

    if persistent.semen_dancelesson == 0:
        jump semen_dancelesson_true

    if d2_dv_night_pristan == True:
        jump semen_dancelesson_menu_dv

    if persistent.semen_dancelesson >= 1:
        jump semen_dancelesson_menu

label semen_dancelesson_menu_dv:

    menu:
    
        "Да, умею. (Пропустить)":
            jump semen_dancelesson_false
    
        "Нет, не умею.":
            jump semen_dancelesson_true


label semen_dancelesson_menu:

    menu:
    
        "Да, умею (Пропустить)":
            jump semen_dancelesson_false
    
        "Нет, не умею (Испытать незабываемый опыт ещё раз)":
            jump semen_dancelesson_true
            
label semen_dancelesson_false:

    window show
    nd_il "Да, умею, не в первой же мне."
    "Сказал я с улыбкой.{w} Мне казалось, что он меня ничему особо новому не научит."
    "Хотя и танцевал я, наверное, всего пару раз в жизни."
    me "Отлично, тогда иди и зажги танцпол."
    nd_il "А ты?"
    me "А я уже договорился Лене в медпункте помочь.{w} Да и не хочу я во всех этих свистоплясках участвовать."
    nd_il "Тогда удачи.{w} Еще раз спасибо за костюм."
    window hide

    show black with dissolve2
    play sound_loop sfx_far_steps fadein 2
    $ renpy.pause(1)

    window show
    me "Главное не ссы девку на танцы пригласить!"
    "Прокричал этот пионер мне вслед..."
    window hide

    $ renpy.pause(2)

    window show
    th "Какой-то Семён всё-таки странный.{w} Одежда у него модная откуда-то в шкафчике взялась..."
    th "И ведёт он себя как-то \"по блатному\"."
    th "Но за шмотки его только поблагодарить можно."
    th "Итог:{w} тип он вроде мутный но, черт его возьми, харизматичный."
    window hide

    if d2_dv_night_pristan == True:
        jump dv_stars_roadto_dv
    else:
        jump us_dancing_roadto_us_nir        

label semen_dancelesson_true:

    window show
    nd_il "Нет, ни разу не приходилось."

    show pi2 grin pioneer at center with dspr

    me "Ну ты походу совсем жизни не видал. Давай я тебя научу."
    nd_il "Прям тут что ли?"
    me "Нет. Пошли место покажу."

    scene black with dissolve

    "Сказал Семён и повёл меня куда-то в лес..."
    window hide

    $ renpy.pause(1)
    play sound_loop sfx_far_steps fadein 1
    $ renpy.pause(2)
    stop sound_loop fadeout 2
    $ renpy.pause(1)
    scene bg ext_polyana_prerain_2
    show nd_light_rain_effect
    with dissolve2

    window show
    "И остановились мы у какой-то поляны..."
    me "Вот тут."
    "Семён присел на немного влажную траву."
    "С неба всё так же моросил дождик, но листья деревьев сохраняли относительную сухость травы."
    me "Итак. Чтобы научиться танцевать медляки, нужно знать несколько простых правил."
    me "Первое — старайся не быть каменным, не бойся брать девушку за талию."   
    me "Второе — старайся при танце не наступать на ноги партнера."             
    me "Третье — не делай резких движений…"                                     
    th "Вот это он затирает, будто танцпол — это минное поле..."

    me "…И помни, танцпол — это не минное поле, не нужно боятся наступить не туда."

    th "Успокоил."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    hide black with dissolve
    show pi2 smile pioneer at center with dspr
    play music ndm_list['USSR_1'] fadein 3

    window show
    me "...А теперь давай перейдем к практике."
    
    nd_il "Мы что, сейчас вместе танцевать будем?"

    me "Можешь на том дереве потренироваться, а я оценю твои навыки."
    hide pi2 smile pioneer with dspr
    "Семён показал мне на одно из деревьев.{w} Это был дуб.{w} Большой такой."
    "Я положил свои руки на \"талию\" этого дерева и показал Семёну."

    me "Отлично, теперь давай движения - вперёд, назад."

    "Я начал выполнять его указания."
    "Получалось нормально. Я имитированл медленный танец с деревом"
    "Иногда поворачивал голову к Семёну, и он мне молча кивал."
    "Но вскоре меня начало одолевать чувство{w}, будто этот пионер надо мной просто шутит."

    nd_il "Слушай, может все-таки нормально потанцуем?"
    nd_il "Я имею ввиду, не с деревом."
    me "Ну давай.{w} Подойди и пригласи меня на танец."
    window hide

    $ renpy.pause(1)
    show pi2 smile pioneer at center with dspr

    window show
    "Я подошёл к Семёну."

    nd_il "Потанцуем?"

    hide pi2 smile pioneer with dspr
    show pi2 grin pioneer at center with dspr

    me "Совсем дурачок что ли?{w} Надо говорить: \"Разрешите пригласить вас на танец\"."
    th "Точно, это-же СССР."
    "Я убрал руку за спину."
    nd_il "Разрешите пригласить вас на танец."

    hide pi2 grin pioneer with dspr

    me "Другое дело. Теперь руки на талию{w}, чуть выше{w}, во-о-т."
    me "Теперь повторяй за моими ногами.{w} Ногу вперед, ногу назад.{w} Да, вот так..."
    "Я пытался выучить движения, которые нужно делать."
    window hide


    $ renpy.pause(0.5)
    show black with dissolve
    $ renpy.pause(2)
    $ renpy.pause(0.5)

    window show
    "Вскоре у меня начало получаться."

    me "Отлично танцуешь, теперь давай научимся танцевать по кругу…"
    "Семён показывал мне движения, а я их запоминал и повторял."
    window hide

    $ renpy.pause(1)
    stop music fadeout 3
    hide black with dissolve
    $ renpy.pause(0.5)

    window show
    "Танец закончился так же внезапно, как и начался."

    show pi2 smile pioneer at center with dspr

    me "Всё, Илюх. Я научил тебя всему, что знаю сам.{w} А теперь иди и зажги танцпол."
    nd_il "А ты разве не идёшь?"
    me "Не, я пообещал Лене в медпункте помочь."
    me "Да и не хочу во всех этих свистоплясках участвовать."
    nd_il "Понятно. Спасибо тебе ещё раз."
    window hide

    show black with dissolve2
    play sound_loop sfx_far_steps fadein 2

    window show
    me "Главное не ссы девку на танцы пригласить!"
    "Прокричал этот пионер мне в след..."
    window hide

    $ renpy.pause(2)

    window show
    th "Какой-то Семён всё-таки странный.{w} Одежда у него модная откуда-то в шкафчике взялась..."
    th "И ведёт он себя как-то \"по блатному\"."
    th "Но за шмотки его только поблагодарить можно."
    th "Итог:{w} тип он вроде мутный но, черт его возьми, харизматичный."
    window hide
    
    $ persistent.semen_dancelesson += 1

    $ renpy.pause(2, hard=True)
    
    if d2_dv_night_pristan == False:
        jump us_dancing_roadto_us_nir

    elif d2_dv_night_pristan == True:
        jump dv_stars_roadto_dv

label dv_stars_roadto_dv:

    $ nd_change_time('sunset')


    stop sound_loop fadeout 3
    stop ambience fadeout 3

    $ renpy.pause(3)

    play ambience nda_list['light_rain_inside'] fadein 3

    if dvrr_shark_p == 1:
        scene bg ext_stage_big_night_alice_shark_rain with dissolve2

    if dvrr_pirate_p ==1:
        scene bg ext_stage_big_night_alice_pirate_rain with dissolve2

    window show
    "Подойдя к сцене - месту нашей с Алисой встречи, я никого не увидел."
    "Возможно, она ещё не подготовилась или забила на эту встречу."
    th "Но это ведь не логично - назначить встречу, а потом не прийти на неё..."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Алиса! Ты тут?!"
    dv "Не кричи. Здесь я."
    "Донёсся голос девушки с крыши сцены."
    th "Да как вы туда забираетесь?"
    dv "Залезай сюда."
    nd_il "Да, сейчас."
    window hide

    $ renpy.pause(1)

    window show
    "Осмотрев сцену, способа забраться наверх я не нашёл."
    nd_il "А как?"
    dv "Тут лестница есть за сценой."
    th ".{w}.{w}."
    nd_il "Понял, сейчас..."
    window hide

    show black with dissolve2
    stop ambience fadeout 3

    window show
    "Зайдя за сцену, там действительно была лестница, ведущая на крышу."
    "Я незамедлительно принялся забираться наверх..."
    window hide

    $ renpy.pause(3)

    play ambience ambience_camp_center_night fadein 4
    show cg dv_on_scene_with_ilya with dissolve2

    window show
    dv "Вот ты теперь и здесь.{w} Кстати, классный костюмчик.{w} Тебе идёт."
    "В отличии от меня, Алиса была в обычной пионерской форме. Но ей она хотя бы к лицу..."
    nd_il "Спасибо. ты тоже красиво выглядишь..."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Так, и зачем мы здесь?"
    window hide

    $ renpy.pause(0.5)

    window show
    dv "Просто так."
    scene black with dissolve
    "Я не успел удивиться простодушию девушки, как..."
    window hide
    stop ambience fadeout 3
    play music ndm_list['intheend_piano'] fadein 4
    
    $ renpy.pause(1)    
    show cg sun_forest_dvr with dissolve2
    $ renpy.pause(2)

    window show
    "...наши взгляды припали к красному закату солнца."
    "Это неописуемо красиво..."
    "Красноватые лучи рассеивались в воздухе, наполненном чем-то...{w} Родным и близким сердцу.{w} Чем-то, что у тебя давно отняли в совсем юном возрасте, а потом заботливо вернули на место..."
    "Как пазл, собранный воедино спустя 10 лет..."
    window hide

    $ renpy.pause(1)

    window show
    "Я почувствовал прикосновение женской ладони, и в миг по коже пробежались мурашки."
    "Обстановка была странной, но именно в ней я понял, что что-то чувствую к Алисе."

    show blink

    "Алиса решительна, строга и вместе с тем мила, как падающие желтые осенние листья, как прохладный ветерок на берегу моря..."
    "А её глаза имеют какой-то особенный оранжевый оттенок, которого нет ни у одной из мне знакомых девушек в лагере..."
    window hide

    $ renpy.pause(1)

    window show
    "Я почувствовал, как она легонько сжала мою руку."
    dv "Тут красиво, правда ведь?"
    "Я молча кивнул головой."
    window hide

    $ renpy.pause(1)

    window show
    "Солнце полностью зашло.{w} И только-только его лучи скрылись за пышным лесом, мы с Алисой взглянули друг на друга."
    window hide

    $ volume(0.4, "music")
    play ambience nda_list['light_rain_outside'] fadein 3

    if dvrr_shark_p == 1:
        scene bg ext_stage_big_night_alice_shark_rain
        hide blink
        show unblink
    if dvrr_pirate_p ==1:
        scene bg ext_stage_big_night_alice_pirate_rain 
        hide blink
        show unblink

    $ renpy.pause(1)

    window show
    nd_il "Это было нечто.{w} Я никогда прежде не видел такой красоты."
    dv "Правда что-ли? А что же ты тогда видел?"
    nd_il "Понимаешь, последние несколько лет я совсем не выхожу из своей квартиры, и тем более - из дома.{w} И я не знаю почему. Я уже забыл, что со мной когда-либо происходило.{w} Я живу больше настоящим, или скорее существую."
    nd_il "А первый и последний мой выход из дома закончился попаданием сюда."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я немного улыбнулся, чтобы добавить в выше мною сказанное немного юмора."
    "Ведь я знал, что мой образ жизни отчасти неправильный, но для меня не остается другого выхода."
    dv "Но ведь ты говорил, что зарабатываешь, занимаясь любимым делом."
    nd_il "Да, я зарабатываю сидя дома..."
    window hide

    $ renpy.pause(2)

    window show
    "Алиса задумалась, и после короткой паузы достала из кармана юбки швейцарский ножик."
    dv "Я взяла его у Ульяны погонять."
    window hide

    $ renpy.pause(1)

    window show
    "Видимо, Алиса хотела меня удивить, но я ожидал от неё чего-то подобного."
    dv "Я думала ты хотя-бы удивишься.{w} Такого как ты легко удивить."
    window hide

    $ renpy.pause(1)

    window show
    dv "Давай напишем здесь свои инициалы."
    nd_il "Хорошая идея."
    window hide

    $ renpy.pause(1) 
    
    window show
    "Алиса ловко покрутила охотничий нож, и вырезала на деревянной крыше первую букву своего имени - \"А\""
    dv "А теперь ты."
    "Я взял нож и вырезал рядом букву \"И\", а также..."
    window hide

label dv_camp_end_menu:

    menu:
    
        "Обвести инициалы сердечком":
            jump dv_camp_end_1_2    

        "Отдать нож Алисе":
            window show
            th "Я не могу..."
            th "Я зашел слишком далеко."
            th "И мне кажется, я здесь совсем не для этого."
            th "У этого должен быть только один конец..."

            "Я неуверенно сжал рукоятку ножа, и..."
            window hide
            jump dv_camp_end_menu
            
label dv_camp_end_1_2:

    $ renpy.pause(2)

    window show
    "...Обвел наши инициалы сердечком."
    window hide
    
    $ renpy.pause(2)

    show dv shy pioneer2 at center with dspr

    window show
    "Алиса немного покраснела. Я отдал ей ножик и мы замолчали."
    window hide
    
    $ persistent.nd_moral_points += 1

    $ renpy.pause(3)

    window show
    dv "Это что, мешок с сахаром?.."
    "Интонация девушки звучала достаточно смущённо, чтобы не обратить на это внимания."
    nd_il "Это...{nw=1}"
    show dv guilty pioneer2 at center with dspr
    dv "Да. Я поняла... Это сердечко. Ха-ха."

    hide dv with dspr

    "Алиса посмотрела на меня своими глазами, будто разглядывая что-то у меня на лице.{w} Мы смотрели друг на друга."
    window hide

    $ renpy.pause(1) 

    window show
    "Я слегка приблизился к девушке, но вместо того, чтобы отодвинуться, она наоборот - приблизилась ко мне."
    window hide

    stop music fadeout 2
    stop ambience fadeout 2
    show blink

    $ renpy.pause(2)
    
    window show
    "Мы закрыли глаза, и я сам не заметил, как наши губы сплелись в легком поцелуе."
    window hide

    $ renpy.pause(5)

    window show
    "Поцелуй продолжался не долго, но по личным ощущениям, прошло не менее вечности."
    "И ради этого я провел бы ещё одну..."
    window hide

    $ renpy.pause(1)

    play ambience nda_list['light_rain_outside'] fadein 4


    hide blink
    show unblink
    $ renpy.pause(1)
    show dv shy pioneer2 at center with dspr

    window show
    "Я открыл глаза, а вместе со мной и Алиса."
    "Румянец разукрасил лицо девушки и, вероятно,моё лицо было не менее смущённым."
    window hide

    $ renpy.pause(1)

    window show
    "Я вдохнул в грудь свежий воздух, и вновь ощутил капельки дождя на своей коже."
    "Мир вокруг будто стал сказкой, а я в ней - писателем своей истории."
    "Мне пришлось вдохнуть еще немного воздуха, чтобы сказать то, что я хотел сказать."
    nd_il "Алиса..."
    window hide

    $ renpy.pause(1)
    play sound sfx_hiding_in_bush
    show dv scared pioneer2 at center with dspr
    with hpunch

    window show
    "Внезапно послышался шум кустов неподалёку.{w} Алиса вздрогнула от внезапности вслед за мной." 
    "Вероятно, она тоже испытывала ко мне что-то. И ждала того момента, пока я скажу своё слово." 
    "Но кто-то за нами следил!"
    window hide

    $ renpy.pause (1)

    window show
    th "Это может быть Ульяна, или кто-то другой.{w} И если он видел что-то больше, чем моё нелепое недоговоренное признание..."
    window hide

    show black with dissolve

    window show
    nd_il "Я сейчас проверю и вернусь..."
    window hide

    $ renpy.pause(1)

    play sound_loop sfx_run_forest fadein 2

    $ renpy.pause(2)

    stop sound_loop fadeout 2
    play sound sfx_hiding_in_bush

    $ renpy.pause(1)

    scene bg ext_path2_night with flash

    window show
    "Прыгнув в них я ожидал поймать Ульяну, но в кустах просто никого не было."
    nd_il "Черт! Убежала!"

    play sound sfx_hiding_in_bush

    dreamgirl "Илья..."

    "Я резко вспрыгнул и встал в боевую стойку."
    nd_il "Кто это?"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    dreamgirl "Сейчас ты сам всё поймёшь."
    window hide

    $ renpy.pause(0.5)
    play sound sfx_hiding_in_bush
    show da normal far at center behind nd_rain_effect 
    with dspr

    window show
    "Раздвигая кусты, из-за них вышла девушка."
    "На ней я смог заметить животные ушки и хвост.{w} Похоже, её не смущал дождь. Возникало чувство, будто её этот дождь даже не трогал, проходя через её тело насквозь. Словно она - призрак."
    "Но призраков я не боялся, да и всего мифического. Я просто в это не верил.{w} А значит я просто не видел, как на неё попадают эти самые капли дождя."
    "Но я всё-таки пал в ступор. Я не знал, что мне даже говорить этой девушке. Тем более если она одета не в пионерскую форму, а в какую-то рваную, но современную одежду..."
    "Скорее всего, надо было сначала представиться. Но как?{w} Ладно.{w} Что нибудь придумаю."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Здравствуйте, меня Ильёй зовут.{w} Для друзей просто \"попаданец\".{w} А вас как?"
    
    hide da with dspr
    show da normal at center behind nd_rain_effect with dspr
    $ renpy.pause(0.5, hard=True)
    show da guilty at center behind nd_rain_effect with dspr
    dreamgirl "Илья, не придуривайся."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Вам помочь?"
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Нет, я просто хочу с тобой поговорить."
    play music ndm_list['mood_dream'] fadein 3
    "Девушка подошла ко мне поближе так, что я смог различить её лицо."
    "Очертания и внешность этой девушки показались мне необыкновенно знакомыми,{w} но вместе с тем и до боли чужими."
    "Что-то странное происходило у меня в голове. Необыкновенная тяга к этому человеку (или существу?) одолела меня."
    "Существо животного происхождения, с ушками и хвостом енота проедало мне душу своим взглядом."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Мне кажется, я тебя знаю."
    "Неуверенно, но четко произнес я."
    show da upset at center behind nd_rain_effect with dspr
    dreamgirl "Ты сам всё вспомнишь через считанные минуты..."
    dreamgirl "А сейчас я должна предупредить тебя об опасности."
    "Я удивился.{w} Какая опасность? Неужели моё попадание сюда это не есть главная опасность? Может она хочет сказать, что я отсюда могу никогда не выбраться?"
    "Тем не менее, нужно было вести себя сдержанно. По её выражению лица казалось, что она и сама скоро ответит мне на этот вопрос."
    nd_il "Мне угрожает опасность?"
    "Переспросил я с слегка взволнованным тоном."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Илья, пойми. Ты находишься в пионерлагере, в котором живут абсолютно реальные люди.{w} У всех этих пионеров и пионерок есть собственная история, собственный характер и семья, которая их всех ждёт."
    nd_il "Но я не хотел попадать сюда, в этот лагерь."
    dreamgirl "Я знаю..."
    show da guilty at center behind nd_rain_effect with dspr
    "Девушка замолчала, отведя свой взгляд,{w} но всего на секунду."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "...Но так получилось. Он сам захотел, чтобы ты появился здесь."
    dreamgirl "И я вижу, что у тебя сейчас много вопросов. Но повремени с ними. Я отвечу тебе на них чуть-чуть попозже."
    dreamgirl "Есть некоторые пионеры в лагере, внешностью очень похожие на тебя. Встречал их когда-нибудь?"
    window hide

    $ renpy.pause(2, hard=True)
    
    window show
    nd_il "Не уверен. Скорее всего нет."
    show da upset at center behind nd_rain_effect with dspr
    dreamgirl "Эти пионеры говорят обратное, что все обитатели этого лагеря не настоящие.{w} Но верить им или нет — дело твоё."
    dreamgirl "Если хочешь, чтобы все твои знакомые из этого лагеря без риска вернулись целыми и здоровыми, нужно сделать правильный выбор.{w} Сейчас ты можешь решить свою судьбу и судьбу этих людей."
    dreamgirl "Либо ты просыпаешься в своей квартире, забыв о лагере и о дорогих в нём тебе людей навсегда, либо продолжаешь жить здесь дальше до конца смены."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Пойми, я буду поддерживать тебя, не зависимо от твоего выбора, но во втором случае с некоторой вероятностью ты можешь подвергнуть себя и обитателей этого лагеря опасности."
    dreamgirl "Если ты хочешь вернуться домой, то иди по той тропинке прямо в лес."
    dreamgirl "Решение принимать только тебе."

    hide da with dspr
    play sound sfx_hiding_in_bush
    "Договорив девушка нырнула в кусты и пропала в беспроглядной темноте леса."
    window hide

    $ renpy.pause(1)

    window show
    th "Почему мне приходится делать такие выборы?"
    th "Вот о чём мне говорила та записка..."
    th "И почему она будет меня поддерживать, независимо от моего выбора?.."
    window hide

    stop music fadeout 5
    $ renpy.pause(2, hard=True)

    window show
    th "Кажется я знаю кто эта девушка..."
    window hide
    
    show prologue_dream
    with flash
    with vpunch
    
    window show
    "Я упал на колени."
    window hide

    scene bg rainy_idle_nd with dissolve
    stop ambience fadeout 3
    $ renpy.pause(0.5)
    
    window show
    "Внезапно все звуки вокруг пропали, а мир будто начал рассыпаться на мелкие детали."
    "Я окунулся в воспоминание…"
    window hide

    hide prologue_dream
    with dissolve
    $ renpy.pause(0.5)
    play music ndm_list['dv_camp_end'] fadein 3
    show splatter_notdream with flash
    $ renpy.pause(0.5)

    window show
    nd_da "Илья, давай в прятки."
    nd_il "Давай! Ты вода!"
    "Сказал я и бросился наутёк к кустам, дабы спрятаться за стенкой нашего большого двухэтажного дома."
    "Вспоминая его, понимаешь, что он был действительно огромным для такой маленькой семьи - Мамы, папы, меня, и моей сестры."
    "Она была во многом старше меня, учила меня ценить мир вокруг и уважению."
    "Сколько помню, она всегда была добра со мной, даже в периоды, когда ей самой было плохо..."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_da "Раз, два, три, четыре, пять. Я иду искать!"
    "Прозвучало будто у меня в подкорке мозга."
    "Тело бросило в прохладную дрожь, будто ветер врезался в спину и прополз по ней змеёй."
    window hide

    $ renpy.pause(3)

    window show
    "Вот уже был слышен небольшой топот со стороны угла."
    "К этому моменту я аккуратно отходил назад, пока не споткнулся об камень и не упал, тем самым раскрыв свое местонахождение."
    nd_da "Ага! Попался!"
    "Сразу же закричала она, оказавшись в поле моего зрения, и побежала стучать по стене нашего дома."
    "Игры с сестрой позволяли мне получать удовольствие, которого не могли мне дать родители."
    "Они постоянно были либо на работе, либо занимались домашними делами. Сестра же всегда была за моим присмотром с самого раннего детства."
    window hide

    $ renpy.pause(2)

    window show
    "{i}Вечер, десятое декабря, две тысячи восьмой год. Пол восьмого.{\i}"
    "Весь день в этот момент для меня казался глубочайшим провалом в памяти. Помнится лишь его нещадный вечер..."
    nd_il "Даш, а ты куда собираешься?"
    nd_da "Я ухожу на всю ночь гулять со своими подругами.{w} Не волнуйся за меня, хорошо?"
    nd_da "И родителям тоже скажи, когда с работы придут, чтобы не волновались."
    nd_il "Ты правда вернёшься? Все будет хорошо?"
    "Даша наклонилась, оказавшись прямо перед моим лицом."
    nd_da "Илья, я тебя когда-нибудь обманывала?"
    nd_il "Ну...{w} Нет."
    nd_da "Вот, видишь. Я не стану тебя обманывать."
    nd_da "Я вернусь завтра утром, может немного раньше."
    "Даша мне тепло улыбнулась и обняла.{w} Сегодня был её день рождения."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "После её слов я понял, что делать там, с её подругами, мне нечего.{w} Они были старше меня, и общих тем разговора у меня с ними вряд ли бы нашлось."
    "Удивляюсь. Я был достаточно смышлёным парнем. Отчасти, благодаря ей."
    "Она уделяла мне много заботы, вместе с тем на её плечах было много воспитательных бесед."
    "Она хотела стать психологом в будущем."
    window hide

    $ renpy.pause(2)
    
    window show
    "Как она и сказала, её не было всю ночь."
    "Мои родители за неё волновались, но я знал, что волноваться было нечего."
    "Она говорила, что придёт утром. Я передал её слова родителям, и те немного успокоились."
    "Я был уверен, что поводов на волнения не было, и она, как и сказала, придёт утром."
    window hide

    $ renpy.pause(2)

    window show
    "Всё шло своим чередом. Мы легли спать, темнота начинала поглощать мой разум, но резко отпускала с включением света в гостиной."
    "Даши не было. Время - час ночи."
    "Снова звук выключателя и... Провал, опять провал..."
    "Нейроны будто не успевали восстанавливаться от того, насколько быстро ко мне в голову приходит воспоминание о том дне..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Как я помню, родители просыпались за всю ночь около трёх раз, ожидая, что Даша появится. Но её всё не было и не было."
    "Стрелка часов перешагнула за шесть."
    "Примерно тогда из коридора, по стенам дома, раздался телефонный звонок."
    "\"Это точно должна была быть сестра. Иначе и быть не может.\" - думал я тогда."
    "Не знаю, о чём и почему...{w} В коридоре собралась вся моя крохотная семья."
    window hide

    $ renpy.pause(1)
    
    window show
    "Мама поднимает телефонную трубку, ожидая, что сейчас оттуда донесется голос моей сестры."
    "Но грубый хриплый мужской вонзился в уши кинжалом в тот злополучный момент..."
    window hide

    hide splatter_notdream
    show splatter_dark_notdream
    with flash

    window show
    dreamgirl "…Просим приехать на опознание…"
    window hide

    $ renpy.pause(1)
    play sound sfx_broken_dish
    $ renpy.pause(2)

    window show
    "На глазах мамы появились капельки слёз."
    "Отец... С его лица слезла улыбка, давая понять, что что-то идёт не так."
    "Тогда-то я и понял... Но не поверил своим ушам..."
    dreamgirl "Илья, иди в свою комнату..."
    window hide

    $ renpy.pause(2)

    window show
    "{i}Лицо закрыли простынью, а крест втоптали в снег.{/i}"
    "{i}В костёр охапкой-россыпью летит гвоздик букет...{/i}"
    "Я не верил, что передо мной сейчас моя сестра. Я не верил, что она больше не с нами."
    "Что она больше никогда не сможет рассказать мне чего-либо, понять меня, когда мне грустно."
    "Хочется кричать, но понимаешь, что не можешь."
    "Я был так мал, что просто забыл суть своего существования... Без неё."
    "Всё время я провел с ней, и вот, я стою перед ней, держа её за охолодевшую руку, казалось, ещё недавно крепко прижимающую меня к себе."
    "На глазах выбились горькие слёзы, плавно скользящие по и без того мокрым щекам."
    "Эти глаза ещё ни разу не видели смерти..."
    window hide

    $ renpy.pause(2)
    
    $ volume (0.8, "music")
    
    play ambience nda_list['light_rain_outside'] fadein 2

    hide splatter_dark_notdream with dissolve


    scene bg ext_path2_night with dissolve
    
    $ renpy.pause(1)

    window show
    "Мне на секунду показалось, что всё это и вправду нелепый сон, который закончится, как только я вернусь домой."
    "Время с Алисой было самым лучшим, но я не хотел ей как-то навредить."
    "Я не хотел навредить больше никому."
    "Может ей будет немного больно сейчас, чем ужасно больно потом?"
    window hide

    $ renpy.pause(2)    

    window show
    "Я взглянул на тропинку в лес и, вспомнив поцелуй девушки, пошел прямо."

    play sound_loop sfx_far_steps

    "Меня ничего не держало здесь.{w} Лишь девушка по имени Алиса. И я буду по ней очень скучать."
    "Не верится, что я забуду её, и она меня."
    "Но с ней ведь всё будет в порядке.{w} Хотя бы с ней..."
    window hide

    stop ambience fadeout 4
    stop sound_loop fadeout 4
    show black with dissolve2

    $ renpy.pause(1)
    
    window show
    "Вскоре стало совсем темно.{w} Я не мог ничего поделать, а ноги сами несли меня вперед."
    nd_il "Алиса..."
    dv "Ты мне тоже очень нравишься..."
    "Послышался голос девушки из моего сознания, как будто это было моим воспоминанием."
    "Нет. Это было тем, что происходит сейчас.{w} Но как,{w} если сейчас я иду в темноту?"
    "Может, это альтернативная реальность внутри моей головы?"
    "Я словно существую сразу в двух местах..."
    "Да ну нет...{w} Вся эта реальность не может быть чем-то большим чем просто сном..."
    window hide

    $ renpy.pause(2)

    window show
    "Вскоре мне начало казаться, что я иду по воздуху, или я просто парил в нём.{w} Но я шёл и шёл, пока в конце не показался белый свет..."
    window hide

label dv_camp_titles_for_menu:

    $ renpy.pause(1)

    stop music fadeout 5
    show black with flash
    
    $ renpy.pause(1)
    if config.developer == False:
        if persistent.dv_camp_end_ach == False:
            $ notdream_achievment("dv_camp_end_ach")
            $ persistent.dv_camp_end_ach = True
            $ persistent.nd_moral_points += 5

    $ renpy.pause(6)

    $ volume (1, "music")

    play music ndm_list['intheend_piano'] fadein 4
    scene dvr_camp_end_1 with dissolve2

    $ renpy.pause(5, hard=True)

    scene dvr_camp_end_2 with dissolve

    $ renpy.pause(5, hard=True)

    scene dvr_camp_end_1 with dissolve

    $ renpy.pause(1, hard=True)

    scene dvr_camp_end_3 with dissolve

    $ renpy.pause(5, hard=True)

    scene dvr_camp_end_1 with dissolve
    
    $ renpy.pause(1, hard=True)
    
    scene dvr_camp_end_4 with dissolve

    $ renpy.pause(5, hard=True)

    scene dvr_camp_end_1 with dissolve

    $ renpy.pause(1, hard=True)

    scene dvr_camp_end_5 with dissolve

    $ renpy.pause(5, hard=True)

    scene dvr_camp_end_1 with dissolve

    $ renpy.pause(2, hard=True)

    scene dvr_camp_end_6 with dissolve

    $ renpy.pause(1, hard=True)

    hide dv_camp_end_ach
    jump credits_nd_as_dv_camp


label us_dancing_roadto_us_nir:

    $ renpy.pause(2)

    scene bg ext_playground_prerain 
    show nd_rain_effect
    with dissolve2

    window show
    "По пути со мной шли пионеры, которые так-же переоделись на танцы."
    "Но среди них я никого из своего отряда не увидел."
    th "Может я рано?{w} Или поздно?{w} Без телефона и времени ничего не понятно."
    th "Надо к кибернетикам сходить ещё..."
    th "Да и черт с ними. Разберусь с этим завтра."
    th "А сегодня телефон мне и не нужен."
    window hide

    $ renpy.pause(1)

    stop sound_loop fadeout 3
    show black with dissolve2
    $ renpy.pause(1)
    play sound sfx_open_door_clubs
    stop ambience fadeout 2
    $ volume(0.2, "music")
    play music ndm_list['Disco_4'] fadein 2
    
    window show
    "Вот я уже захожу в здание со спортзалом, прохожу короткий коридор, и вижу дверь, ведущую непосредственно на дискотеку." 
    window hide

    stop ambience fadeout 1
    play sound sfx_open_door_1
    $ volume(1, "music")
    play music ndm_list['Disco_4'] fadein 1
    scene bg int_sporthall_night_dance with flash

    $ nd_change_time('night')

    window show
    "Я, не останавливаясь распахиваю дверь, и вижу танцпол с танцующими пионерами."
    window hide

    $ renpy.pause(3, hard=True)

    window show
    "Осмотрев спортзал я понял, что девушка ещё не пришла, и сев на скамейку, принялся её ждать. Ждать и думать о «сюрпризе», который она обещала подготовить."
    "На противоположной стороне зала я мог видеть Василия, который клеился к Ольге Дмитриевне."
    "Ну у него и вкусы конечно…{w} Но как я могу его осуждать?{w} Он, вроде как, в моём сне парень в возрасте, двадцати пяти или тридцати лет.{w} А если он не имеет ничего общего с моим сном?"
    "В любом случае чтобы осуждать его, нужно встать на его место…"
    window hide

    $ renpy.pause(1)
    stop music fadeout 2
    show black with dissolve
    $ renpy.pause(3, hard=True)
    play music ndm_list['Disco_1'] fadein 2
    hide black with dissolve
    $ renpy.pause(1)

    window show
    "Прошло примерно десять минут моих размышлений о Ольге Дмитриевне и Василии, и я уже начал сомневаться в том, что я всё правильно понял насчет встречи вечером, как в спортзал вошла Алиса в вечернем платье,{w} но без своей подруги."
    "Она села между Василием и Ольгой Дмитриевной, и начала что-то обсуждать с вожатой."
    "Это сулило тотальный облом Василию в подкате к Ольке.{w} Но по его лицу, он не особо расстроился."
    window hide

    $ renpy.pause(1)

    window show
    th "Опять Ульяны нет, видимо её сюрприз отменяется."
    th "Не может же она так долго готовиться к этим танцам..."
    window hide

    $ renpy.pause(1)
    $ volume(0.1, "sound")
    play sound sfx_open_door_1
    
    window show
    "Но дверь в спортзал вновь открылась, и в дверях показались рыжие волосы... Ульяны!"
    window hide

    $ renpy.pause(1)
    show us normal dress far at fleft with dspr

    window show
    "На ней было красивое вечернее платье, которое подчеркивало её красоту и женственность."
    "Непривычно так говорить о девушке, которая недавно играла в футбол с мальчишками."
    window hide

    $ renpy.pause(0.4)
    
    window show
    th "Какая же она… Красивая…"
    window hide

    $ renpy.pause(0.8)
    hide us with dspr
    
    window show
    "Она осмотрела спортзал и, видимо не найдя меня, сразу пошла на танцпол."
    "За ней же подтянулись Ольга Дмитриевна и Алиса."
    window hide

    $ renpy.pause(1)
    show cg d3_dance_imleft with dissolve2
    $ renpy.pause(1)

    window show
    "Я было задумался о том, чтобы присоединиться к ней, но потом подумал, что лучше подождать, пока она закончит танцевать, если это можно так назвать.{w} На самом деле это было больше похоже на кривляния."
    "Вот Васян вышел на танцпол, и начал танцевать смесь лезгинки, тектоника и брейк-данса."
    "Возможно в понятии этих пионеров это круто, но для меня это были обычные понты."
    window hide

    $ renpy.pause(1)

    window show
    th "Вообще мужчина не должен уметь танцевать. Разве что только медленные танцы.{w} Да и то не всегда."
    window hide

    show black with dissolve
    $ renpy.pause(2)

    scene bg int_sporthall_night_dance with dissolve 
    hide black with dissolve

    window show
    "Пока этот новенький Василий танцевал, Ульяна уже устала, и заметив меня одного, сидящего на скамейке, подошла ко мне и села рядом."

    show us grin dress close at left with dspr

    us "Илья, ты отлично выглядишь."
    
    nd_il "Спасибо, ты тоже в этом наряде выглядишь просто ослепительно."
    window hide

    $ renpy.pause(1)
    show us shy dress close at left with dspr

    window show
    us "Спасибо."
    window hide

    $ renpy.pause(1)
    show us laugh dress close at left with dspr

    window show
    us "А я и не знала, что ты так сильно пауков боишься."
    nd_il "Да он был огромным."
    window hide

    $ renpy.pause(0.4)
    
    window show
    th "..."
    window hide

    $ renpy.pause(0.4)

    window show
    nd_il "Погоди-ка, а откуда ты знаешь про паука?"
    hide us with dspr

    "Ульяна засмеялась, да засмеялась так, что казалось она сейчас лопнет. Если смех продлевает жизнь, то из-за этого случая Ульяна будет жить как минимум лет двести."
    th "Так это был её розыгрыш.{w} Как она поймала такого \"тарантула\" и не побоялась впустить его в библиотеку?"
    nd_il "Ты что, самая храбрая что ли?"
    "Я начал щекотать Ульяну, а та продолжала смеяться дальше."
    us "Ай-яй-яй-яй. Не надо. Всё, я больше не буду. Ай-я-я-яй."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я перестал щекотать Ульяну, и она смогла отдышаться."
    us "Всё, ты сам напросился."
    "Сказала Ульяна и вытянула ко мне свои руки. Но я остановил её."
    nd_il "Стой, подожди.{w} Каждый виновный имеет право на последнюю просьбу перед своей смертью."
    "Да, мы все всё правильно поняли."
    "Для меня щекотка действительно считалась второй смертью."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ульяна опустила свои руки и посмотрела на меня."

    show us normal dress close at center with dspr

    us "Ла-а-адно. Твоя предсмертная просьба будет исполнена."
    window hide

    $ renpy.pause(1)
    stop music fadeout 3

    window show
    "Ульяна замерла в ожидании того, что я попрошу в свой \"последний час\"."
    hide us with dspr
    "Именно в этот момент Ольга Дмитриевна подошла к микрофону, и из динамиков послышался её голос."
    dy "А сейчас медленная музыка. Кавалеры приглашают дам."
    window hide

    play music ndm_list['Disco_2'] fadein 2
    $ renpy.pause(1)
    
    window show
    "После речи вожатой сразу-же включилась медленная музыка.{w} Это было моим шансом."
    th "Илья, это отличный момент, чтобы пригласить её на танец.{w} К тому же она уже заведомо согласилась…"
    window hide

    $ renpy.pause(2)
    
    window show
    nd_il "Ульяна, можно пригласить тебя...{w} на танец?"
    "Это предложение далось мне с необъяснимой тяжестью.{w} Я даже не понимал - почему."
    
    show us shy dress at center with dspr

    "Девочка смягчила свой взгляд.{w} По ней было видно, что она не ожидала такого развития событий."
    "И, возможно, даже не думала, что кто-то её сегодня пригласит."
    "А платье, потому что хотела..."
    us "М-меня? Н-на танец?"
    nd_il "Да. На танец."
    
    show us shy2 dress at center with dspr
    
    us "М-можно, конечно."
    
    hide us with dspr
    
    "Она медленно протянула мне свою ладонь."
    "Я аккуратно взял её, встал вместе с девушкой с лавочки и уверенно повёл за собой на танцпол."
    window hide

    $ renpy.pause(1)
    
    show cg us_night_t with dissolve
    
    window show
    "Уже через секунду её руки касались моих плеч, а мои были на талии." 
    "Мы кружились в этом медленном танце, рассматривая друг у друга в глазах отражения от гирлянд и света."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Ульяна, ты когда-нибудь уже танцевала медленные танцы?"
    window hide

    $ renpy.pause(1)

    window show
    "Ульяна отвела взгляд на мою рубашку."
    us "Нет, но я видела, как это делают другие."
    "Пионерка выглядела смущённой от такой обстановки, и говорила со мной вполголоса."
    "Было видно, что это её первый медленный танец."
    "У меня он тоже был первым. Но почему я вижу в её лице столько стеснения?"
    "Словно у неё никогда не было любви.{w} Чувства, когда тебя любят, и когда ты любишь кого-то."
    "Испытываешь ответственность за человека.{w} И действия твоего субъекта симпатии предают какой-то окрас и смысл."
    "Неужели мы оба чувствуем это прямо сейчас?{w} Или это мои беспочвенные додумки?"
    window hide

    $ renpy.pause(1)
    
    window show
    "Пока мы танцевали, я не замечал ничего вокруг."
    "Казалось, что мы одни в этом мире, рядом никого нет, а эта громкая музыка доносится из глубины сознания."
    "Мы мыслили одинаково, были единым механизмом, поочередно переставляя ноги то вперед, то назад."
    "Это сплотило нас ещё больше, ведь если одна из частей механизма выйдет из строя, это повлечет за собой его полный отказ... "
    window hide

    $ renpy.pause(1)    
    stop music fadeout 4
    $ renpy.pause(0.3)
    show blink

    window show
    "Когда музыка закончилась, я плавно приземлился с носков и опустил руки.{w} Ульяна сделала тоже самое и прильнула к моей груди, а я обнял её."
    us "Спасибо за танец."
    us "Мне понравилось."
    nd_il "Взаимно."
    window hide

    $ renpy.pause(0.5)
    hide blink
    show unblink
    scene bg int_sporthall_night_dance with dissolve
    $ renpy.pause(1)
    
    window show
    "Мы с Ульяной отправились обратно на скамейку, где нас ждала Алиса."

    show us shy2 dress at left with dspr
    show dv normal dance at right with dspr

    dv "Слушай, я тут выходила на улицу и...{w} Там кто-то просил тебя позвать."
    nd_il "Алиса, ты серьезно?{w} Ну кто меня может звать?"
    dv "Я не вру.{w} Правда."
    nd_il "Ладно. Подождите меня."
    window hide

    hide us
    hide dv normal dance
    with dspr

    show black with dissolve2
    stop music fadeout 3
    $ volume(1, "sound")
    $ renpy.pause(1)
    play sound sfx_open_door_1
    play sound sfx_close_door_1
    play sound sfx_steps_clubs_nextroom
    $ renpy.pause(2)
    play sound sfx_open_door_clubs

    $ renpy.pause(2)
    play ambience nda_list['light_rain_outside'] fadein 2
    
    scene bg ext_playground_rain_night
    show nd_rain_effect
    with dissolve2

    $ renpy.pause(1)

    jump ulya_ends_dream

label ulya_ends_dream:

    $ nd_change_time('night')
    
    window show
    "Было уже довольно темно. Дождь прибавил свои темпы, и я ещё сильнее ощущал влажность воздуха."
    "Я оглянулся вокруг, чтобы понять, кто мог сказать Алисе меня позвать.{w} Но тут никого не было.{w} Лишь дождь падал своими каплями на землю, создавая чарующий звук, под который приятно засыпать."
    "Но спать мне сейчас было не к чему. Мне нужно было понять, кто и зачем меня звал.{w} Может он уже от нетерпения ушёл?{w} Или это Алиса меня разыграла, чтобы я постоял под дождём да помокнул."
    "Интересно получается, значит они стоят там в спортивном зале и обсуждают танец, а я должен под дождём ждать кого-то."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Понятно. Ещё один их розыгрыш."
    th "Впрочем, ничего нового.{w} Могли что-нибудь по жёстче придумать, как тогда в столовой."
    "Я невольно передёрнулся, вспоминая тот случай.{w} Нет.{w} Сколопендра в тарелке это уже лишнее."

    play sound sfx_hiding_in_bush
    
    dreamgirl "Подожди, Илья."
    
    with hpunch
    
    "Я вздрогнул от неожиданности."
    nd_il "Кто ты?"
    window hide


label ulya_allends_dream: 

    window show
    dreamgirl "Сейчас ты сам всё поймёшь."
    window hide

    $ renpy.pause(0.5)
    play sound sfx_hiding_in_bush
    show da normal far at center behind nd_rain_effect 
    with dspr

    window show
    "Раздвигая кусты, из-за них вышла девушка."
    "На ней я смог заметить животные ушки и хвост.{w} Похоже, её не смущал дождь. Возникало чувство, будто её этот дождь даже не трогал, проходя через её тело насквозь. Словно она - призрак."
    "Но призраков я не боялся, да и всего мифического. Я просто в это не верил.{w} А значит я просто не видел, как на неё попадают эти самые капли дождя."
    "Но я всё-таки пал в ступор. Я не знал, что мне даже говорить этой девушке. Тем более если она одета не в пионерскую форму, а в какую-то рваную, но современную одежду..."
    "Скорее всего, надо было сначала представиться. Но как?{w} Ладно.{w} Что нибудь придумаю."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Здравствуйте, меня Ильёй зовут.{w} Для друзей просто \"попаданец\".{w} А вас как?"
    
    hide da with dspr
    show da normal at center behind nd_rain_effect with dspr
    $ renpy.pause(0.5, hard=True)
    show da guilty at center behind nd_rain_effect with dspr
    dreamgirl "Илья, не придуривайся."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Вам помочь?"
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Нет, я просто хочу с тобой поговорить."
    play music ndm_list['mood_dream'] fadein 3
    "Девушка подошла ко мне поближе так, что я смог различить её лицо."
    "Очертания и внешность этой девушки показались мне необыкновенно знакомыми,{w} но вместе с тем и до боли чужими."
    "Что-то странное происходило у меня в голове. Необыкновенная тяга к этому человеку (или существу?) одолела меня."
    "Существо животного происхождения, с ушками и хвостом енота проедало мне душу своим взглядом."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Мне кажется, я тебя знаю."
    "Неуверенно, но четко произнес я."
    show da upset at center behind nd_rain_effect with dspr
    dreamgirl "Ты сам всё вспомнишь через считанные минуты..."
    dreamgirl "А сейчас я должна предупредить тебя об опасности."
    "Я удивился.{w} Какая опасность? Неужели моё попадание сюда это не есть главная опасность? Может она хочет сказать, что я отсюда могу никогда не выбраться?"
    "Тем не менее, нужно было вести себя сдержанно. По её выражению лица казалось, что она и сама скоро ответит мне на этот вопрос."
    nd_il "Мне угрожает опасность?"
    "Переспросил я с слегка взволнованным тоном."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Илья, пойми. Ты находишься в пионерлагере, в котором живут абсолютно реальные люди.{w} У всех этих пионеров и пионерок есть собственная история, собственный характер и семья, которая их всех ждёт."
    nd_il "Но я не хотел попадать сюда, в этот лагерь."
    dreamgirl "Я знаю..."
    show da guilty at center behind nd_rain_effect with dspr
    "Девушка замолчала, отведя свой взгляд,{w} но всего на секунду."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "...Но так получилось. Он сам захотел, чтобы ты появился здесь."
    dreamgirl "И я вижу, что у тебя сейчас много вопросов. Но повремени с ними. Я отвечу тебе на них чуть-чуть попозже."
    dreamgirl "Есть некоторые пионеры в лагере, внешностью очень похожие на тебя. Встречал их когда-нибудь?"
    window hide

    $ renpy.pause(2, hard=True)
    
    window show
    nd_il "Не уверен. Скорее всего нет."
    show da upset at center behind nd_rain_effect with dspr
    dreamgirl "Эти пионеры говорят обратное, что все обитатели этого лагеря не настоящие.{w} Но верить им или нет — дело твоё."
    dreamgirl "Если хочешь, чтобы все твои знакомые из этого лагеря без риска вернулись целыми и здоровыми, нужно сделать правильный выбор.{w} Сейчас ты можешь решить свою судьбу и судьбу этих людей."
    dreamgirl "Либо ты просыпаешься в своей квартире, забыв о лагере и о дорогих в нём тебе людей навсегда, либо продолжаешь жить здесь дальше до конца смены."
    show da normal at center behind nd_rain_effect with dspr
    dreamgirl "Пойми, я буду поддерживать тебя, не зависимо от твоего выбора, но во втором случае с некоторой вероятностью ты можешь подвергнуть себя и обитателей этого лагеря опасности."
    dreamgirl "Если ты хочешь вернуться домой, то иди по той тропинке прямо в лес."
    dreamgirl "Решение принимать только тебе."

    hide da with dspr
    play sound sfx_hiding_in_bush
    "Договорив девушка нырнула в кусты и пропала в беспроглядной темноте леса."
    window hide

    $ renpy.pause(1)

    window show
    th "Почему мне приходится делать такие выборы?"
    th "Вот о чём мне говорила та записка..."
    th "И почему она будет меня поддерживать, независимо от моего выбора?.."
    window hide

    stop music fadeout 5
    $ renpy.pause(2, hard=True)

    window show
    th "Кажется я знаю кто эта девушка..."
    window hide
    
    show prologue_dream
    with flash
    with vpunch
    
    window show
    "Я упал на колени."
    window hide

    scene bg rainy_idle_nd with dissolve
    stop ambience fadeout 3
    $ renpy.pause(0.5)
    
    window show
    "Внезапно все звуки вокруг пропали, а мир будто начал рассыпаться на мелкие детали."
    "Я окунулся в воспоминание…"
    window hide

    hide prologue_dream
    with dissolve
    $ renpy.pause(0.5)
    play music ndm_list['dv_camp_end'] fadein 3
    show splatter_notdream with flash
    $ renpy.pause(0.5)

    window show
    nd_da "Илья, давай в прятки."
    nd_il "Давай! Ты вода!"
    "Сказал я и бросился наутёк к кустам, дабы спрятаться за стенкой нашего большого двухэтажного дома."
    "Вспоминая его, понимаешь, что он был действительно огромным для такой маленькой семьи - Мамы, папы, меня, и моей сестры."
    "Она была во многом старше меня, учила меня ценить мир вокруг и уважению."
    "Сколько помню, она всегда была добра со мной, даже в периоды, когда ей самой было плохо..."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_da "Раз, два, три, четыре, пять. Я иду искать!"
    "Прозвучало будто у меня в подкорке мозга."
    "Тело бросило в прохладную дрожь, будто ветер врезался в спину и прополз по ней змеёй."
    window hide

    $ renpy.pause(3)

    window show
    "Вот уже был слышен небольшой топот со стороны угла."
    "К этому моменту я аккуратно отходил назад, пока не споткнулся об камень и не упал, тем самым раскрыв свое местонахождение."
    nd_da "Ага! Попался!"
    "Сразу же закричала она, оказавшись в поле моего зрения, и побежала стучать по стене нашего дома."
    "Игры с сестрой позволяли мне получать удовольствие, которого не могли мне дать родители."
    "Они постоянно были либо на работе, либо занимались домашними делами. Сестра же всегда была за моим присмотром с самого раннего детства."
    window hide

    $ renpy.pause(2)

    window show
    "{i}Вечер, десятое декабря, две тысячи восьмой год. Пол восьмого.{\i}"
    "Весь день в этот момент для меня казался глубочайшим провалом в памяти. Помнится лишь его нещадный вечер..."
    nd_il "Даш, а ты куда собираешься?"
    nd_da "Я ухожу на всю ночь гулять со своими подругами.{w} Не волнуйся за меня, хорошо?"
    nd_da "И родителям тоже скажи, когда с работы придут, чтобы не волновались."
    nd_il "Ты правда вернёшься? Все будет хорошо?"
    "Даша наклонилась, оказавшись прямо перед моим лицом."
    nd_da "Илья, я тебя когда-нибудь обманывала?"
    nd_il "Ну...{w} Нет."
    nd_da "Вот, видишь. Я не стану тебя обманывать."
    nd_da "Я вернусь завтра утром, может немного раньше."
    "Даша мне тепло улыбнулась и обняла.{w} Сегодня был её день рождения."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "После её слов я понял, что делать там, с её подругами, мне нечего.{w} Они были старше меня, и общих тем разговора у меня с ними вряд ли бы нашлось."
    "Удивляюсь. Я был достаточно смышлёным парнем. Отчасти, благодаря ей."
    "Она уделяла мне много заботы, вместе с тем на её плечах было много воспитательных бесед."
    "Она хотела стать психологом в будущем."
    window hide

    $ renpy.pause(2)
    
    window show
    "Как она и сказала, её не было всю ночь."
    "Мои родители за неё волновались, но я знал, что волноваться было нечего."
    "Она говорила, что придёт утром. Я передал её слова родителям, и те немного успокоились."
    "Я был уверен, что поводов на волнения не было, и она, как и сказала, придёт утром."
    window hide

    $ renpy.pause(2)

    window show
    "Всё шло своим чередом. Мы легли спать, темнота начинала поглощать мой разум, но резко отпускала с включением света в гостиной."
    "Даши не было. Время - час ночи."
    "Снова звук выключателя и... Провал, опять провал..."
    "Нейроны будто не успевали восстанавливаться от того, насколько быстро ко мне в голову приходит воспоминание о том дне..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Как я помню, родители просыпались за всю ночь около трёх раз, ожидая, что Даша появится. Но её всё не было и не было."
    "Стрелка часов перешагнула за шесть."
    "Примерно тогда из коридора, по стенам дома, раздался телефонный звонок."
    "\"Это точно должна была быть сестра. Иначе и быть не может.\" - думал я тогда."
    "Не знаю, о чём и почему...{w} В коридоре собралась вся моя крохотная семья."
    window hide

    $ renpy.pause(1)
    
    window show
    "Мама поднимает телефонную трубку, ожидая, что сейчас оттуда донесется голос моей сестры."
    "Но грубый хриплый мужской вонзился в уши кинжалом в тот злополучный момент..."
    window hide

    hide splatter_notdream
    show splatter_dark_notdream
    with flash

    window show
    dreamgirl "…Просим приехать на опознание…"
    window hide

    $ renpy.pause(1)
    play sound sfx_broken_dish
    $ renpy.pause(2)

    window show
    "На глазах мамы появились капельки слёз."
    "Отец... С его лица слезла улыбка, давая понять, что что-то идёт не так."
    "Тогда-то я и понял... Но не поверил своим ушам..."
    dreamgirl "Илья, иди в свою комнату..."
    window hide

    $ renpy.pause(2)

    window show
    "{i}Лицо закрыли простынью, а крест втоптали в снег.{/i}"
    "{i}В костёр охапкой-россыпью летит гвоздик букет...{/i}"
    "Я не верил, что передо мной сейчас моя сестра. Я не верил, что она больше не с нами."
    "Что она больше никогда не сможет рассказать мне чего-либо, понять меня, когда мне грустно."
    "Хочется кричать, но понимаешь, что не можешь."
    "Я был так мал, что просто забыл суть своего существования... Без неё."
    "Всё время я провел с ней, и вот, я стою перед ней, держа её за охолодевшую руку, казалось, ещё недавно крепко прижимающую меня к себе."
    "На глазах выбились горькие слёзы, плавно скользящие по и без того мокрым щекам."
    "Эти глаза ещё ни разу не видели смерти..."
    window hide

    stop music fadeout 3
    $ renpy.pause(2)
    play ambience nda_list['light_rain_outside'] fadein 2

    if usrr >= 3:
        jump us_root_road_exit

    elif usrr < 3:
        jump dv_nir_root_road_exit

    else:
        jump dv_nir_root_road_exit
label us_root_road_exit:

    window show
    usp "Илья, Илья!"
    window hide

    hide splatter_dark_notdream with dissolve

    window show
    "Я всё также сидел на прохладной траве, а с неба падали тяжёлые капли дождя.{w} Настолько тяжёлые, что каждый их удар как будто оставлял в коже пулевые ранения."
    us "Илья. Всё хорошо? Илья, успокойся! Хватит плакать!"
    "Крикнув, Ульяна прыгнула на меня сзади, тем самым вернув меня в реальный мир."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Всё хорошо."
    window hide

    $ renpy.pause(1)
    show blink

    window show
    "Сказав это, я крепко обнял Ульяну. Мне сейчас так не хватало объятий..."
    "В этот момент капли перестали падать на меня. Будто что-то закрыло меня от дождя."
    "Ульяна взяла с собой зонтик? Откуда?"
    us "Илья. Не плачь."
    "Ульяна нежно погладила меня по голове."
    us "Ты так из-за танца расстроился?"
    nd_il "Нет, Уля. Всё куда серьезней.{w} Не заморачивай себе голову."
    window hide

    scene bg ext_playground_rain_night
    show nd_rain_effect_hard_rain

    hide blink
    show unblink
    $ renpy.pause(1)
    
    show us shy dress close at center behind nd_rain_effect_hard_rain 
    with dspr

    window show
    "Окончательно придя в себя, я разжал руки и выпустил Ульяну из объятий."
    us "Илья, я хотела тебе сказать." 
    us "Завтра утром восход будет красивый."
    
    show us shy2 dress close at center behind nd_rain_effect_hard_rain 
    with dspr
    
    us "Я думала, может ты...{w} Cоставишь мне компанию?"
    window hide

    $ renpy.pause(1)
    hide us with dspr
    
    window show
    "Именно тут я вновь вспомнил про величину значимости своего выбора."
    window hide

    stop ambience fadeout 3
    $ renpy.pause(1)
    
    window show
    th "Она сказала мне, что если я хочу оставить всё здесь в целости, я должен уйти отсюда."
    th "Но вместе с тем, я не могу отказать Ульяне..."
    th "Иначе буду винить себя всю свою оставшуюся жизнь, если вдруг вспомню об этом."
    th "В конце концов это будет выглядеть так, будто мне не понравилось с ней танцевать."
    "Я не знал, могу ли я остаться."
    "Но что-то должно было помочь мне сделать выбор..."
    window hide

    $ renpy.pause(1)

label root_road_us_dv_nir:

    if us >= 4 and sport_kr_us == True:

        menu: 
            "Прислушаться к дождю":
                $ persistent.nd_moral_points += 1
                $ usrr += 1 # Дальнейший сценарий будет только с Ульяной и выходом на одну из её концовок.
                $ us_scenario_road = True
                jump us_scenario_road_d3

            "Услышать биение сердца":
                $ sich_scenario_road = True
                $ renpy.pause(1)
                play ambience nda_list['light_rain_outside'] fadein 3
                play sound sfx_head_heartbeat fadein 2

                window show
                "Я почувствовал дрожь по всему телу."
                "Как это прекрасно. Слышать биение своего сердца и осознавать, что ты живое существо, способное мыслить."
                "И что ты никому в этой жизни не причинишь вреда, пусть даже параллельной вселенной или прошлому, в котором есть те, кто тебя ценит."
                "И пусть я сейчас действую себе в убыток, но именно этот вариант будет правильным."
                "К тому же я ведь с самого начала присутствия в этом лагере хотел домой. И вот - я теперь могу уйти."
                window hide
                
                $ persistent.nd_moral_points += 1

                $ renpy.pause(1)
                stop sound_loop fadeout 2
                $ renpy.pause(1)
                
                window show
                nd_il "Ульяна.{w} Прости.{w} Я не смогу с тобой пойти на восход."
                nd_il "Меня сегодня забирают родители."
                th "От моего вранья внутри моей груди что-то укололось. Я знал, что она мне этого никогда не простит. Даже если очень сильно захочет."
                nd_il "Пойми меня правильно, пожалуйста..."
                window hide

                $ renpy.pause(1)

                show us sad pioneer at center behind nd_rain_effect_hard_rain 
                with dspr

                window show
                us "Жалко..."
                us "Тогда можно я тебе напоследок кое-что скажу?"
                us "Только закрой глаза. И не подсматривай."
                window hide

                hide us with dspr
                show blink
                $ renpy.pause(1)

                window show
                "Я почувствовал как она поцеловала меня в щёку."
                "От этого внутри стало немного теплее."
                "Но у меня было ещё одно чувство."
                "Одинокости."
                th "Я никогда больше не увижу эту девушку.{w} И она меня никогда не увидит."
                th "И то, как я просто брошу её тут одну..."
                window hide

                $ renpy.pause(1)
                
                window show
                th "Может можно взять её с собой?"
                window hide

                $ renpy.pause(1)
                hide blink
                show unblink
                $ renpy.pause(2)                
                
                window show
                "Но в тот же миг её не было рядом.{w} Она убежала, забрав с собой мои мечты, мою любовь.{w} А любил ли я её вообще?"
                "Сделал ли я что-то, за что можно любить меня?"
                window hide

                $ renpy.pause(1)

                show black with dissolve2

                play sound_loop sfx_far_steps
                $ renpy.pause(3)
                
                window show                
                "Я пошёл по тропинке в лес."
                "Мне казалось, я что-то теряю.{w} Но это уже было не важно."
                nd_il "Ульяна..."
                "Непроизвольно произнес я.{w} Как будто это и вовсе не я произнес.{w} Тело само двигалось, говорило.{w} А думал я."
                window hide

                menu:
                
                    "Прощай":
                        $ gg_goodbye_us = True

                        window show
                        strange_g  "Прощай, Ульяна."
                        
                
                    "Прости":
                        $ gg_sorry_us = True
                        
                        window show
                        strange_g  "Прости, Ульяна."

                th "Кто это сказал? Готов поклясться, это был не я..."
                window hide

                stop ambience fadeout 2
                stop music fadeout 2
                stop sound_loop fadeout 2
                show black with flash

                $ renpy.pause(5, hard=True)

                jump usrf_true_end_nd

label usrf_true_end_nd:

    play music ndm_list['tamsp14'] fadein 3
    scene bg semen_room_window with dissolve2

    $ set_mode_nvl()

    window show
    "Прошло семь дней с того момента, как мне приснился этот сон."
    "Я доделал свои запланированные дела, сходил на улицу (в кои-то веки), пообщался с друзьями в Интернете,{w} ведь в жизни у меня их никогда и не было,{w} кроме Йоси."
    "Из их слов, обо мне не было слышно ничего целых две недели."
    "Странно, что я даже не помню, что я делал всё это время."
    "Как будто эту часть моей жизни кто-то вырезал.{w} Но я точно помню, что это было что-то насыщенное..."
    window hide

    $ set_mode_nvl()
                
    window show
    "После этого мне больше ни разу не снились ворота лагеря."
    "Но случилось кое-что странное."
    "Когда я вышел во двор, ко мне подбежала рыжая девушка с голубыми, как небо, глазами, и просто начала разглядывать моё лицо."
    "Она спросила: \"Вы помните меня?\"."
    "Она мне точно кого-то напоминала. Но я был уверен, что не видел её никогда."
    "Сказав ей об этом, она сделала грустное лицо, и выдавив из себя: \"Простите\" отправилась в неизвестном направлении, а вскоре и совсем скрылась за углом многоэтажки."
    "Больше ничего необычного я не встречал.{w} Хотя начало появляться чувство, будто я что-то потерял..."
    window hide

    $ set_mode_adv()

    show black with dissolve2
    stop music fadeout 4

    $ renpy.pause (5, hard=True)

    if gg_goodbye_us == True:
        scene us_true_bye with dissolve2

    if gg_sorry_us == True:
        scene us_true_sorry with dissolve2 

    $ renpy.pause(1, hard=True)

    if config.developer == False:
        if persistent.us_sorry_bye_ach == False:
            $ persistent.us_sorry_bye_ach = True
            $ notdream_achievment("us_sorry_bye_ach")
            $ persistent.nd_moral_points += 3
        
    $ renpy.pause(1, hard=True)

    jump credits_nd_as

label dv_nir_root_road_exit:

    scene black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg ext_playground_rain_night
    show nd_rain_effect_hard_rain
    with dissolve

    window show
    "Придя в себя я посмотрел в глубину леса."
    "Мне казалось это единственным выходом из ситуации."
    "Я не получил ничего в этом лагере.{w} Ничему не научился, и мое дальнейшее пребывание здесь кажется мне бессмысленным."

    scene black with dissolve

    "Я решительно пошёл по тропинке в лес."
    "Мне казалось, я что-то теряю.{w} Но это уже было не важно."
    "Я ухожу, и пусть это случится как можно быстрей."

    usp "Илья!"
    window hide

    stop ambience fadeout 2
    stop music fadeout 2
    stop sound_loop fadeout 2
    show black with flash

    $ renpy.pause(5, hard=True)
                
    play music ndm_list['tamsp14'] fadein 3
    scene bg semen_room_window with dissolve2

    $ set_mode_nvl()

    window show
    "Прошло семь дней с того момента, как мне приснился этот сон."
    "Я дописал программу, сходил на улицу (в кои-то веки), пообщался с друзьями в интернете,{w} ведь в жизни у меня их никогда и не было."
    "Из их слов, обо мне не было слышно ничего целых две недели."
    "Странно, что я даже не помню, что я делал всё это время."
    "Как будто эту часть моей жизни кто-то вырезал.{w} Но я точно помню, что это было что-то насыщенное..."
    window hide

    $ set_mode_adv()

    window show
    "И это действительно конец..."
    "Хотя..."
    "Могу ли я считать это концом?{w} Может, это только начало?{w} Начало всего."
    "Пусть я и живу как какой-то затворник, это мне нравится."
    "Отложу дела на завтра, ведь сегодня у меня сеанс у психотерапевта..."
    window hide

    show black with dissolve2
    stop music fadeout 2
    $ renpy.pause(1, hard=True)
    if config.developer == False:
        if persistent.bad_end_ach == False:
            $ persistent.bad_end_ach = True
            $ notdream_achievment("bad_end_ach")

    $ renpy.pause(1, hard=True)
    jump credits_nd_as

label us_scenario_road_d3:
    play ambience nda_list['light_rain_outside'] fadein 3
    $ renpy.pause(3, hard=True)

    window show
    "Я прислушался к звукам дождя."
    "Они так успокаивали меня, и казалось, что я осознаю свой выбор."
    "Будто я слышу послание в звуках бьющихся капель о землю и о листву."
    "Словно азбукой морзе они пытаются мне что-то сказать. В чём-то убедить..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Я не хочу забывать Ульяну."
    th "К тому-же меня там, в моей квартире, никто не ждёт. А тут я хоть кому-то нужен."
    window hide

    $ renpy.pause(1)
    
    window show
    th "А что случится после смены?{w} Если я поеду в свой город...{w} У меня же нет здесь ни семьи, никого."
    th "А там?.."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Так когда там этот твой восход начинается?"
    show us grin dress close at center behind nd_rain_effect_hard_rain 
    with dspr

    us "Ура!"
    us "В три часа ночи."
    us "Я тебя разбужу."
    window hide

    $ renpy.pause(2, hard=True)
    show us normal dress close at center behind nd_rain_effect_hard_rain 
    with dspr
    
    window show
    us "Спасибо тебе еще раз за танец…{w} Я не думала, что меня кто-то пригласит танцевать…"   
    nd_il "Пожалуйста."
    nd_il "Давай тогда по домикам, раз завтра рано вставать."
    window hide

    $ renpy.pause(1)
    hide us with dspr

    window show
    "Я уже хотел уходить, но Ульяна взяла меня за руку и остановила."
    window hide

    show us shy dress at center behind nd_rain_effect_hard_rain 
    with dspr
    
    $ renpy.pause(1)
    
    window show
    us "Пошли вместе."
    window hide

    $ renpy.pause(1)
    show black with dissolve2
    $ renpy.pause(0.5)

    window show
    "Идя по каменной дорожке, я не мог забыть о правильности своих действий. Но всё происходило само собой."
    "Я просто шёл, держа Ульянин зонтик у себя в руке.{w} Шёл и наслаждался стуком капель дождя..."
    window hide

    $ renpy.pause(1)
    
    window show
    us "Илья, почему ты там на поле плакал?"
    window hide

    $ renpy.pause(1)
    
    window show 
    nd_il "Я не знаю, что на меня нашло…"
    us "Ничего страшного, я всегда поддержу тебя.{w} Для этого ведь существуют товарищи, верно?"
    nd_il "Ну...{w} Верно..."
    window hide

    $ renpy.pause(1)

    window show
    "В наше время найти такого друга, как Ульяна, кажется, практически невозможно. Сколько не ищи таких людей - не найдёшь."
    "Скорее всего это из-за менталитета.{w} Тут он более доброжелательный, теплый."
    "Тебя встречают так, будто уже давно ждут..."
    "Не верится, что этого государства больше не существует."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    us "Мы сегодня в футбол хорошо поиграли. Почаще бы так."
    nd_il "Ага..."
    window hide

    show black with nd_effect_5
    $ renpy.pause(2)

    scene bg ext_house_of_dv_night_rain:
        subpixel True
        truecenter
        zoom 1.2
        linear 2.5 zoom 1.0
    show nd_rain_effect
    with dissolve
    
    $ renpy.pause(2.5, hard=True)

    show us shy dress at center behind nd_rain_effect 
    with dspr

    window show
    us "У тебя одежда промокла. Простынешь."
    nd_il "Я посушу её."
    us "И не забудь про восход.{w} Я тебя разбужу."
    nd_il "Не забуду. По крайней мере сейчас."
    "Отшутился я, отдавая Ульяне зонтик, но Ульяна, кажется, проигнорировала мою тупую шутку..."
    window hide

    $ renpy.pause(1)
    
    window show
    us "Спокойной ночи."
    nd_il "Спокойной ночи."
    hide us with dspr
    "Мы заключили друг друга в недолгие объятия."
    "..."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_door_1
    play sound sfx_close_door_1

    window show
    "Ульяна забежала в домик и помахала мне из окна, а затем зашторила его."
    "После этого мне ничего больше не оставалось, как отправиться к своему домику."
    window hide

    show black with dissolve
    
    $ renpy.pause(2)
    play music ndm_list['oblivion'] fadein 2

    window show
    th "Подумать только.{w} Меня никогда за медленные танцы не благодарили. А тут…"
    th "Как бы не влюбиться в эту девушку.{w} В эту непоседливую решительную спортсменку, которая, кажется, готова свернуть горы ради достижения своей цели.{w} Но вместе с этим романтичную и даже скромную."
    th "Кто бы что ни говорил, как бы не наказывали её за розыгрыши, но именно последнюю черту характера у неё никогда не отнять."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Странно, что такой человек как я смог подружиться с ней и найти общий язык."
    th "Что поделать, люблю я иногда допустить нещадный задор.{w} Хотя по моей прошлой жизни такого не скажешь."
    th "Перемены не всегда шли мне на пользу, но сейчас что-то, определенно, изменилось…"
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 2
    $ renpy.pause(1)
    play sound sfx_open_door_1
    play ambience nda_list['rainy_weather_inside'] fadein 3
    scene bg int_house_of_gg_night_1 with dissolve2
    play sound sfx_close_door_1

    $ renpy.pause(1)

    window show
    "Я дошёл до своего домика, открыл дверь, и начал раздеваться, чтобы приготовиться ко сну, пока не обратил внимание на стол."
    "От утренней записки осталась лишь горстка пепла."
    window hide

    $ renpy.pause(1)
    with hpunch

    window show
    nd_il "Что? Как это возможно?"
    th "Кто-то в этом лагере очень любит шутить."
    th "И навряд ли это Ульяна."
    window hide

    $ renpy.pause(2)

    window show
    "Я небрежно смахнул пепел со стола, снял одежду и повесил её на сушилку за окном."
    "После этого я спешно зашторил окно, расправил кровать и лёг на неё."
    window hide

    stop music fadeout 2
    stop ambience fadeout 2
    show blink
    $ renpy.pause(1)

    $ nd_change_time('night')

    window show
    "Перед глазами всплыли события уходящего дня."
    window hide

    scene bg int_clubs_male_day
    show prologue_dream
    with flash
    $ renpy.pause(1)
    
    window show
    "Кибернетики..."
    window hide

    scene bg int_dining_hall_day
    show prologue_dream
    with flash
    $ renpy.pause(1)

    window show
    "Плакаты с едой..."
    window hide

    scene cg d3_soccer_nd
    show prologue_dream
    with flash
    $ renpy.pause(1)

    window show
    "Футбол..."
    window hide

    hide prologue_dream
    show black  
    with dissolve
    $ renpy.pause(1)

    window show
    "Не знаю почему, но сейчас во мне было счастье.{w} И я не могу его никак объяснить."
    "Разве что своей больной психикой."
    window hide

    $ renpy.pause(3)
    
    if usrr >= 4:

        jump notdream_ss_random_dream_2_Yulya


    else:
        jump credits_nd_as

label credits_nd_as:

    stop ambience fadeout 3
    $ renpy.pause(4, hard=True)
    show black with dissolve
    hide bad_end_ach
    play music ndm_list['the_most_musterious_song_on_the_internet'] fadein 4
    $ renpy.pause(1, hard=True)

    show titles_bg with dissolve2

    show credits nd_credits_us:
            xalign 0.5 
            ypos 1.3
            linear 90.0 ypos -3.0
                
    $ renpy.pause(90, hard=True)
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show thx_for_1 with dissolve
    $ renpy.pause(50)
    show black with dissolve
    stop music fadeout 3
    $ renpy.pause(3)

    if persistent.nd_seed_titles == None:
        $ persistent.nd_seed_titles = int(0)

    $ persistent.nd_seed_titles += 1

    $ renpy.pause(1)

    jump nd_reset_mod_params_end

label credits_nd_as_dv_camp:

    $ renpy.pause(2, hard=True)

    show credits nd_credits_dv:
            xalign 0.5 
            ypos 1.3 
            linear 52.0 ypos -4.0
                
    $ renpy.pause(55, hard=True)
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    show thx_for_1 with dissolve
    $ renpy.pause(55)
    show black with dissolve2
    stop music fadeout 3
    $ renpy.pause(3)

    if persistent.nd_seed_titles == None:
        $ persistent.nd_seed_titles = int(0)

    $ persistent.nd_seed_titles += 1

    $ renpy.pause(1)

    jump nd_reset_mod_params_end

