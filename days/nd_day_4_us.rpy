#---------------------------------------------------------------------------
# Не спойлери себе игру! 
#---------------------------------------------------------------------------

label notdream_ss_random_dream_2_Yulya:

    $ nd_change_time('prolog')

    jump notdream_dream_2_Yulya

label notdream_dream_2_Yulya:

    play ambience ambience_old_camp_outside fadein 4
    show day_4_nd with dissolve2
    $ renpy.pause(1, hard = True)
    show day_4_text_nd with dissolve
    $ renpy.pause(0.3, hard = True)
    show day_4_text_red_nd with dissolve
    $ renpy.pause(0.7, hard = True)
    hide day_4_text_red_nd with dissolve
    $ renpy.pause(0.3, hard = True)
    show day_4_text_red_nd with dissolve
    $ renpy.pause(0.7, hard = True)
    hide day_4_text_red_nd with dissolve
    $ renpy.pause(0.3, hard = True)
    show day_4_text_red_nd with dissolve
    $ renpy.pause(0.7, hard = True)
    hide day_4_text_red_nd with dissolve
    $ renpy.pause(2, hard = True)

    stop ambience fadeout 4
    hide day_4_nd
    hide day_4_text_nd
    hide day_4_blur_nd
    with dissolve2

    $ new_chapter(4, u"Это не просто сон, верно?\n День четвертый | Ульяна")

    $ renpy.pause(3)

    $ renpy.pause(1)

    window show
    "В глазах размыло, и я окунулся в сновидение."
    window hide

    $ renpy.pause(1)    
    
    show prologue_dream
    with dissolve
    
    window show
    nd_da "Илья, пошли за мной!"
    nd_il "Куда?"
    nd_da "Сейчас увидишь."
    "Девушка хихикнула и вновь спряталась за стенку."
    "Я побежал за ней, чтобы посмотреть на то, что она хотела мне показать."
    window hide

    stop music fadeout 2
    $ renpy.pause(2)

    play music ndm_list['me_suicideboys'] fadein 2 

    $ renpy.pause(2)

    scene bg ext_yulya_dream_bunker
    show prologue_dream
    with dissolve

    $ renpy.pause(1)

    window show
    "Она меня привела к какому-то входу в бункер, и мы застыли на одном месте рядом друг с другом."
    "Было достаточно жутко от того вида, что перед нами открывался.{w} Неужели она действительно хотела сходить туда именно со мной?"
    nd_da "Пойдём туда."
    nd_il "А если там кто-то есть?"
    nd_da "Я тебя защищу."
    nd_da "Пошли."
    nd_il "Хорошо, пошли."
    "Не поверить ей нельзя было. Я чувствовал себя в безопасности рядом с ней настолько, что хоть без парашута прыгнул с ней. Но сейчас был менее экстремальный случай."
    window hide

    $ renpy.pause(1)

    window show
    "Прокрутив вентиль, дверь в помещение открылась."
    window hide

    scene bg int_catacombs_hole
    show prologue_dream
    with dissolve

    window show
    "Внутри это напоминало туннель, ведущий в какое-то убежище или бункер. В каком-то месте его пол обвалился, показывая внутри себя глубокую темноту"
    window hide

    $ renpy.pause(2)

    window show
    "Из тьмы послышались какие-то трудно разборчивые голоса на иностранном языке, который я не мог определить. Это было что-то среднее между японским и немецким."
    nd_il "Даш, может не стоит?"
    "Но Даша не ответила.{w} Она отпустила мою руку и ушла в пустоту."
    "О нет, это была не просто пустота."
    "Казалось, это самостоятельная материя, которая может поглощать, но не возвращать.{w} Что-то вроде чёрной дыры."
    "С каждым её шагом мне становилось всё хуже и хуже. Казалось что я теряю свои силы и уверенность в себе."
    "Всё могло дойти до того, что я просто потеряю сознание и останусь лежать на бетонном полу этого \"бункера\" или тем, куда-бы эта дверь вела."
    window hide

    $ renpy.pause(1)
    with hpunch

    window show
    nd_il "Даша!"
    "Закричал я изо всех сил имя своей сестры, но она не отреагировав, скрылась в темноте этого каменного коридора."
    "И внезапно из его темноты донеслось..."
    window hide

    stop music fadeout 3
    $ renpy.pause(1)
    show black with dissolve
    with hpunch

    window show
    dreamgirl "Рота подъем!"
    window hide

    $ renpy.pause(2)

label morning_with_us:

    $ nd_change_time('night')

    $ renpy.pause(1)
    
    scene bg int_house_of_gg_night_1

    hide blink
    show unblink
    play ambience ambience_int_cabin_night fadein 2

    window show
    "Проснувшись, я чуть-чуть приоткрыл слипающиеся глаза." 
    
    show us normal pioneer close at center with dspr

    "И меня встретила Ульяна."
    window hide

    $ renpy.pause(1)

    window show
    "Она стояла перед моей кроватью и осматривала меня, проснулся я или нет."
    "Её внешность... Её достаточно сложно не узнать."
    "Прямые красные волосы, голубые, словно летнее небо, глаза...{w} Казалось, в этих глазах был запечатан целый мир, в котором эта девочка постоянно находилась, в котором могла бесконечно набираться сил на свои розыгрыши."
    "Этим мне и нравилось проводить с ней время. Она никогда не была скучной, а в каких-то моментах даже до простоты загадочной."
    window hide

    $ renpy.pause(1)
    show us normal pioneer at center with dspr
    $ renpy.pause(1)
    show us grin pioneer at center with dspr

    window show
    us "Илья, вставай! Рассвет скоро.{w} Чего смотришь?"
    us "Ты обещал!"
    nd_il "А.{w} Да.{w} Сей…"
    "Я перестал сверлить Ульяну взглядом и попытался выдать что-то с глубоким смыслом. Но получилось, что получилось."
    window hide

    $ renpy.pause(1)
    show us smile pioneer at center with dspr

    window show
    us "Вставай кому говорят!"
    window hide

    $ renpy.pause(1)                
    
    window show
    nd_il "А…{w} Ну…{w} Доброе утро."
    "Сквозь пересохшее горло проговорил я."

    show us grin pioneer at center with dspr
    
    us "Доброе утро, давай вставай."
    
    hide us with dspr

    "Ульяна потянула меня за торчащую из под одеяла руку."
    "И этого было достаточно, чтобы я немного взбодрился от недавно увиденного беспокойного сна."
    nd_il "Ульяна. Можно я оденусь? Просто я без этого…"
    window hide

    $ renpy.pause(1)
    show us surp3 pioneer at center with dspr
    $ renpy.pause(1)

    window show
    us "Ой."
    "Ульяна слегка подпрыгнула от мною сказанного и отпустила мою руку."
    us "Я тогда на улице подожду."
    window hide

    hide us with dspr

    play sound sfx_open_door_1
    $ renpy.pause(1)    
    play sound sfx_close_door_1

    window show
    "Ульяна как метеор выбежала из моего домика."
    window hide

    $ renpy.pause(1)
    
    window show
    vg "Доброе утро. Как спалось?{w} Целых четыре часа спал, если не больше.{w} Рекорд!"
    th "Запиши в мою биологическую книгу рекордов."
    window hide

    play sound sfx_open_cupboard

    $ renpy.pause(1)

    window show
    "Дав указание внутреннему голосу, я встал с кровати, и подойдя к шкафчику начал надевать пионерскую форму."
    window hide

    $ renpy.pause(1)

    window show
    "За окном лагерь освещал яркий лунный свет, просачиваясь через шторки. Глаза слипались."
    "К тому же я не совсем понимал, что происходит." 
    th "Может сейчас война?{w} Какой сейчас год?{w} Месяц?{w} День?"
    vg "Слушай.{w} Ты вчера согласился с Ульяной восход смотреть."
    vg "А мог сейчас лежать в своей квартире на своей кровати и спать как младенец."
    th "Если я так решил, значит так нужно."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    play sound nds_list['applysuit']
    $ renpy.pause(1)
    hide black with dissolve

    window show
    "Надев шорты и рубашку из нового комплекта одежды, я попытался завязать красный пионерский галстук,{w} но потом понял,{w} что в моем положении, это как жонглировать шариками на тонком канате с завязанными глазами."
    "То есть - невозможно.{w} Поэтому я просто накинул его на плечи и вышел на улицу."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_home_night with dissolve2    
    play sound sfx_close_door_1
    
    $ renpy.pause(1)

    window show
    "Там меня уже ждала Ульяна, играя сама с собой в футбол маленьким камешком."

    show us normal pioneer at center with dspr

    "Она осмотрела меня всего с ног до головы, и на её лице показалась улыбка."

    show us grin pioneer at center with dspr 
    
    us "Илья, ты что, не умеешь пионерские галстуки завязывать?"
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ну вообще-то....{w} Нет.{w} Помоги, пожалуйста."
    us "Как ребёнок чесслово."
    us "Иди сюда, завяжу."
    window hide

    $ renpy.pause(1)
    hide us with dspr
    $ renpy.pause(1)
    
    window show
    "Я подошёл к ней, и та лёгким движением сделала узелок..."
    window hide

    $ renpy.pause(1)
    
    window show
    "Пару магических движений, и на мне уже был аккуратно завязанный галстук."
    th "Как она это сделала?"
    nd_il "Спасибо…"

    show us smile pioneer at center with dspr

    us "Благодарности потом. А сейчас следуй за мной."

    hide us with dspr
    
    "Скомандовала Ульяна и, махнув рукой, побежала куда-то вперёд..."
    window hide

    show black with dissolve
    
    $ renpy.pause(1)
    
    window show
    "...а мне пришлось шагом идти за ней,{w} так как бегать с утра мне не очень хотелось."
    "Да и не в таком состоянии я был, чтобы бегать."
    "Да и вообще, почему я в этом лагере только и делаю, что играю с ней в догонялки?"
    window hide

    $ renpy.pause(1)
    scene bg ext_houses_night_1 with dissolve2

    window show
    us "Догоняй! Ты чего такой вялый?"
    nd_il "Я не выспался, кажется."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ульяна подбежала ко мне, и начала меня подталкивать сзади."
    "Я всё также послушно шёл дальше."
    "Хотя, где это \"дальше\" мне было не до конца понятно."
    window hide

    $ renpy.pause(1)

    window show
    "И шёл я так, пока нам на встречу не вышел..."
    show sh normal pioneer far at center with dspr
    "Шурик?!"
    window hide

    $ renpy.pause(1)
    show sh normal pioneer at center with dspr
    $ renpy.pause(1)
    
    window show
    sh "Привет ребят. А что вы тут делаете?"
    window hide

    $ renpy.pause(3, hard=True)
    
    window show
    "Мы с Ульяной остановились и наступила неловкая тишина, которую я поторопился незамедлительно нарушить."
    nd_il "А мы встретились тут просто, о жизни поговорить захотели." 
    show us smile pioneer at left with dspr
    us "А ты что тут делаешь и куда идешь?"
    "С подозрением глядя на Шурика произнесла Ульяна, прищурив свои глаза."
    window hide

    $ renpy.pause(1)
    
    window show
    sh "Только никому, ладно?" 
    
    hide sh with dspr
    
    "Мы с Ульяной согласно кивнули, и принялись внимательно слушать кибернетика."
    window hide

    $ renpy.pause(1)
    show sh normal pioneer at center with dspr
    
    window show
    sh "Мы с Электроником мастерим секретное изобретение, которое даст огромный толчок советской науке."
    sh "И вот сегодня я остался доделывать его, но мне не хватает деталей, поэтому я направляюсь в старый лагерь."
    sh "Только не разглашайте никому…{nw=1}"

    show us surp1 pioneer at left with dspr
    
    us "Ничего себе!"
    show sh serious pioneer at center with dspr
    sh "Тихо. Прошу."
    
    show us normal pioneer at left with dspr
    
    nd_il "Ульяна, тсс."
    window hide

    $ renpy.pause(1)
    
    hide us with dspr
    show sh normal pioneer at center with dspr

    window show
    sh "Илья, ты не забудь сегодня прийти в клубы и забрать аккумуляторную батарею свою и зарядник к нему."
    sh "И ещё. Мне вчера вечером сказали эту записку тебе передать."
    "Кибернетик протянул мне какую-то смятую бумажку."
    window hide

    $ renpy.pause(1)
    
    hide sh with dspr
    
    window show
    "Я взял её и осмотрел..."
    window hide

    show zapiska_d4_u with dissolve 
    $ renpy.pause(1)

    window show
    "На вид это была обычная, ничем не примечательная смятая в комок бумажка, коих в Советском союзе было не сосчитать."
    nd_il "Шурик, а зачем ты её смял?"
    us "А что там написано?"
    "Шурик замялся, видимо не понимая, на чей вопрос ему ответить первым."
    sh "Да не знаю я. Мне её такой отдали, и сказали не разворачивать..."
    window hide

    hide zapiska_d4_u with dissolve
    
    $ renpy.pause(1)

    show us normal pioneer at center with dspr

    window show
    "Я убрал записку в карман.{w} Ульяна посмотрела на меня вопросительным взглядом."
    us "А почему ты не прочитал её?"
    nd_il "Потом прочитаю."
    us "Ты хотел сказать \"прочитаем\"."
    "Сказала она на мою короткую фразу, перевернув её смысл, а затем продолжила."
    us "Ну раз потом, так потом. А нам нужно идти."

    hide us with dspr

    "Сказала Ульяна, и взяв меня за руку потащила куда-то.{w} Скорее всего к своему секретному пляжу."
    "К пляжу, где мы и должны будем сегодня встретить восход..."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    hide black with dissolve
    $ renpy.pause(1)

    window show
    nd_il "Ульяна, расскажи про этот ваш \"старый лагерь\"."
    
    show us normal pioneer at fleft with dspr

    us "Ну, там раньше тоже пионеры жили, но сейчас он заброшен."
    us "И ещё слухи ходят, что там призраки обитают, и людей по ночам пугают."
    us "Если хочешь, я тебе потом о нём легенду какую-нибудь расскажу."
    nd_il "Будет интересно послушать."
    us "Я тебе этот лагерь в первый день на карте нарисовала."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Вот блин. А я её потерял."
    window hide

    $ renpy.pause(1)
    show us smile pioneer at fleft with dspr
    
    window show
    us "Ничего страшного, я тебе таких ещё хоть сотню нарисую."
    nd_il "Целую сотню?"
    show us grin pioneer at fleft with dspr
    us "Ну как...{w} Не сотню, но много."
    window hide

    $ renpy.pause(1)

    window show
    "По виду Ульяны было видно, что она наполнена позитивом."
    "Я не понимал, как столько жизнерадостности может умещаться в одном человеке.{w} Особенно этим ранним утром."
    "И ведь её жизнерадостность, это не всё, чем она меня может удивить."
    "Осталось столько ещё неизведанного в её характере..."
    window hide
    
    hide us with dspr

    $ renpy.pause(1)
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(3)
    play sound_loop sfx_far_steps fadein 3
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_path2_night with dissolve2
    $ renpy.pause(1)
    
    window show
    "Показался уже знакомый мне пролесок, пробежав через который, мы должны будем оказаться на берегу, где в первый день лежали на песке."
    window hide

    $ renpy.pause(2)
    
    window show
    "Мы шли довольно тихо, ни о чём не беседуя."
    window hide

    show black with dissolve
    stop sound_loop fadeout 2
    $ renpy.pause(1)
    
    window show
    "Перешагнув через поваленное дерево я увидел кусты, за которыми должно находиться секретное место Ульяны."
    window hide

    $ renpy.pause(1)
    
    window show
    us "Тихо. Там кто-то есть."
    
    play sound sfx_hiding_in_bush
    
    "Прошептала мне Ульяна и, пригнувшись, аккуратно посмотрела через листву."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Кто там?"
    "Прошептал я Ульяне."
    window hide

    $ renpy.pause(1)
    
    window show
    us "Там..."
    window hide

    $ renpy.pause(1)

    window show
    "Я подошёл к кустам, за которыми были еле слышны какие-то голоса."
    "Мне пришлось лечь на траву рядом с Ульяной и посмотреть за густую листву…"
    window hide

    stop ambience fadeout 3
    show black with dissolve2

    play ambience ambience_lake_shore_night fadein 3
    
    window show
    "Там сидели какой-то парень с другого отряда и девушка."
    "И они, обнимаясь на песке, целовали друг друга."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Оу-у..."
    th "Нас обоих не должно здесь быть..."
    "Мы с Ульяной лежали на прохладной траве и смотрели на всё это."
    "Насчёт меня было всё понятно. Мне, по моей прошлой жизни, уже есть восемнадцать лет.{w} Но что насчет Ульяны?"
    "Боже, как же мы так попали...{w} Похоже наш восход либо отменяется, либо...{w} Не могу даже думать, все мысли только об одном."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    us "Они… Целуются…"
    "Не отрывая глаз, тихо произнесла Ульяна."
    "Её интонация голоса была немного смешанной, совмещая в себе интерес но и в то же время отвращение."
    window hide

    $ renpy.pause(1)
    
    window show
    "Ульяна замолчала и просто застыла на одном месте."
    th "Боже... Нас не должно было здесь быть..."
    window hide

    $ renpy.pause(1)

    window show
    pioneer_he "Нравится?"
    "Тихо спросил девушку парень, всё также продолжая её целовать."
    pioneer_she "Да…"
    window hide

    $ renpy.pause(1)
    
    window show
    "Через пару мгновений он повалил девушку на песок, оставив её снизу..."
    window hide

    $ renpy.pause(1)

    window show
    nd_il "Ульяна, все нормально? Очнись."
    "Я дотронулся до Ульяны и она смогла пошевелиться."
    us "Фу-у! Чем они занимаются?"
    "Произнесла пионерка шёпотом."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ульяна, это... Ну..."
    "Я не думал, что мне придётся объяснять это ей.{w} Особенно сейчас."
    "В голове были смешанные чувства."
    "Страх, удивление, разочарование...{w} Что мне ей сказать?"
    th "С одной стороны - она задала вопрос и имеет право получить на него ответ. А с другой..."
    "Я сделал вид, что её не услышал."
    window hide

    $ renpy.pause(2)

label us_main_d4_m_sun:

    stop music fadeout 3
    stop ambience fadeout 3
    $ renpy.pause(3, hard=True)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_path2_night with dissolve2
    $ renpy.pause(1)

    window show
    "Ульяна отвернулась от кустов и отвесила мне подзатыльник."
    "Он был не слишком сильный, и показался мне какой-то странной попыткой к дальнейшему моему обвинению."
    show us dontlike pioneer at center with dspr
    us "Тебе не стыдно?"
    th "Чего?"
    nd_il "А что я? Я не знал что там. Тем более никуда я не смотрел."
    hide us with dspr
    us "Ладно, я знаю другое место."
    window hide

    $ renpy.pause(1, hard=True)
    show us upset pioneer far at center with dspr

    window show
    us "Пошли, чего встал?"
    nd_il "А.{w} Да, пошли..."
    window hide

    stop ambience fadeout 2
    show black with dissolve
    $ renpy.pause(2)
    play sound_loop sfx_far_steps fadein 3 
    play ambience ambience_camp_center_night fadein 3
    $ renpy.pause(2)
    play music music_list['meet_me_there'] fadein 3
    scene bg ext_path2_night with dissolve2

    window show
    th "Что это только что было?"
    th "Забыть бы это как страшный сон.{w} Или странный?{w} Или это и есть сон?"
    "Нужно было отвлечься. Я прислушивался к звукам сверчков, сов, других обитателей темного леса."
    "В кармане у меня была записка, которую мне передал Шурик. И я не знал. Может мне её открыть сейчас..."
    window hide

    $ renpy.pause(1)

    window show
    us "Как они нашли мой тайный пляж?"
    nd_il "Да и не говори. Просто звери..."
    window hide

    show us normal pioneer at center with dspr

    window show
    us "А может это ты им показал?"
    nd_il "Да я даже без тебя на него не ходил.{w} Вот те крест.{w} Веришь?"
    show us grin pioneer at center with dspr
    us "Ладно, верю."
    us "Видел бы ты своё лицо сейчас. Ха-ха."
    nd_il "Ну знаете ли..."
    show us smile pioneer at center with dspr
    us "У меня ещё один пляж есть."
    nd_il "И мы сейчас на него идём?"
    us "Именно."
    window hide

    $ renpy.pause(1)

    stop sound_loop fadeout 2

    $ renpy.pause(1)

    window show
    nd_il "А давай всё таки посмотрим..."
    "Решив наконец посмотреть записку, которую дал мне кибернетик, я остановился и развернул согнутую бумажку…"
    window hide

    $ renpy.pause(1)
    play sound nds_list['papersmack']
    $ renpy.pause(2) 
    $ renpy.pause(1)

    window show
    th "В шесть вечера на пристани..."
    window hide

    $ renpy.pause(1)

    window show
    us "Илья, ты что застыл? Что там написано?"
    window hide

    hide zapiska_d4_o with dissolve 

    show us normal pioneer at center with dspr

    window show
    nd_il "Тут написано \"В шесть вечера на пристани\"."
    window hide

    hide us with dspr

    window show
    "Только я успел договорить, как бумажка в моей руке начала рассыпаться в песок."
    
    with hpunch 

    "Я начал быстро оттряхивать руку от {i}песка{/i}, образовавшегося из этой {i}бумажной{/i} записки."
    th "Чего?!"
    th "Как?!" 
    th "Почему эта бумажка только что рассыпалась в чёртов песок?!{w} Это точно не сон?!"
    window hide
    
    $ renpy.pause(1)
    
    with flash_red
    
    $ renpy.pause(1)
    
    window show
    "Я вновь ущипнул себя, и почувствовал всё ту-же боль."
    "А это значит, что это уже далеко не безумное сновидение."
    window hide

    $ renpy.pause(1)
    show us surp1 pioneer at center with dspr
    
    window show
    us "Илья, ты как этот фокус сделал?"
    th "Мне бы самому это знать."
    nd_il "Я не знаю. Оно само."
    "Ульяна посмотрела на меня удивлённым взглядом."
    "Признаться,{w} я был удивлён не меньше её." 
    "Мне это уже не казалось каким-то розыгрышем.{w} Всё было предельно серьёзно."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Только давай это останется между нами?"
    window hide

    show us smile pioneer with dspr
    $ renpy.pause(1)
    hide us with dspr
    $ renpy.pause(1)

    window show
    "Ульяна положительно кивнула, и мы отправились дальше."
    window hide

    stop music fadeout 4
    $ renpy.pause(1)
    show black with dissolve2
    play sound_loop sfx_far_steps fadein 2
    $ renpy.pause(3, hard=True)
    stop sound_loop fadeout 2
    scene bg ext_path2_night with dissolve2

    $ renpy.pause(1)

    window show
    "Ульяна резко остановилась перед какими-то кустами, и показала на них указательным пальцем."

    show us normal pioneer at center with dspr

    us "Вот за ними ещё один пляж."
    us "Только я на него обычно не хожу."
    window hide

    stop ambience fadeout 3 
    show black with dissolve
    $ renpy.pause(1)

    window show
    "Ульяна отодвинула кусты и..."
    window hide

    $ renpy.pause(1)

    play music ndm_list['nd_beach_of_Love'] fadein 2
    play ambience ambience_lake_shore_night fadein 2
    scene bg d4_us_bseansky with dissolve2

    $ renpy.pause(1)

    window show
    "...увидев прекрасное зрелище, я издал протяжное \"Ва-ау...\""
    window hide

    $ renpy.pause(2, hard=True)
    
    window show
    "Я сел на песок, и уставился на красное солнце, постепенно встающее из-за горизонта."
    "Ульяна села рядом со мной."
    us "Ого... Оно так близко..."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    "Ульяна положила голову мне на плечо."
    "Поначалу я немного растерялся. Но спустя пару секунд моя рука немного приобняла Ульяну."
    window hide

    $ renpy.pause(3, hard=True)
    
    window show
    "В горизонте показались маленькие, еле заметные огоньки."
    window hide

    $ renpy.pause(1)

    window show
    us "Это так красиво."
    "Еле слышно произнесла Ульяна."
    nd_il "Да, это волшебно."
    window hide

    $ renpy.pause(1)
    show splatter_notdream with dissolve2
    $ renpy.pause(1)

    window show
    "Я был очень поражен этим восходом солнца."
    "Мне не шло больше ничего в голову. Мысль о недавно увиденном забылась сама собой, словно сон."
    "Все иные мысли как будто вытеснились из моей головы под ослепительной красотой этого красного солнца, красующегося на стыке неба и моря..."
    "Удивляло, как Ульяна удачно подобрала время и день, для того чтобы показать мне такое."
    "После этого, признаться, во мне загорелся какой-то огонь.{w} Будто я увидел смысл существования, скрытый от меня за семью стенами. Возможно, ради подобного и стоит жить, а не ради текста на мониторе, набираемого через клавиатуру."
    "Почему-то меня охватывало чувство дежавю. Будто я когда-то в жизни уже видел что-то подобное. Будто это со мной уже происходило. Но я наотрез отказывался верить этому чувству..."
    window hide

    $ renpy.pause(1)  
    show black with dissolve2
    $ renpy.pause(2)
    
    window show
    "..."
    window hide

    stop ambience fadeout 3
    $ renpy.pause(3, hard=True)

    $ nd_change_time('sunset')

    play ambience ambience_lake_shore_night fadein 3
    scene bg tain_beach_us with dissolve2
    stop music fadeout 2

    window show
    "Мы сидели и смотрели на солнце, пока весь лагерь не был озарён утренним солнечным светом."
    "Восход был встречен вместе с Ульяной под напевание мелодий птицами, оживанием всего живого даже в моей душе."
    "Я был благодарен этой красноволосой девушке за то, что она мне подарила такое воспоминание, которое я ещё не скоро забуду."
    us "Ну что, пойдём по домикам?"
    nd_il "Угу..."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    scene black with dissolve2

    $ renpy.pause(5, hard=True)

label morning_calling_d4:

    $ nd_change_time('day')

    $ renpy.pause(3, hard=True)
    scene bg int_house_of_gg_day 
    hide blink
    show unblink
    play ambience ambience_int_cabin_day fadein 3

    $ renpy.pause(1)
    play music ndm_list['early_morning'] fadein 4

    $ renpy.pause(1, hard=True)

    window show
    "Проснувшись, я оказался в своём лагерном домике."
    "Через шторы просачивались яркие солнечные лучи, а птицы напевали свою утреннюю песню через открытую форточку окна."
    "Я оглядел комнату.{w} Часы показывали десять часов и пятьдесят четыре минуты."
    "А это значило, что я снова пропустил линейку, на которой определенно говорили о расписании и планах на этот день. Но это было не очень принципиально, о расписании можно спросить у Слави."
    "А ещё, раз я проснулся, нужно причесаться, умыться, почистить зубы... Мой план на это утро понятен."
    "А что насчёт Ульяны? Почему я остался в лагере? Неужели это всё только для того чтобы я взглянул с ней на восход?"
    "В моём горле появился комок. Я подверг опасности весь лагерь. Поддавшись своим чувствам в подкорке головного мозга, я просто... Я уподобился тем, кого всю жизнь ненавидел."
    "Нужно исправить это сегодня. Как только появится автобус, я уеду отсюда. Но что насчёт Ульяны?.."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я перевернулся на спину с замученным выражением лица и принял позу Ленина в Мавзолее.{w} Я планировал в раздумьях пролежать вплоть до двенадцати часов."
    window hide

    $ renpy.pause(2)

    play sound sfx_knocking_door_outside

    window show
    "И именно в этот момент в мою дверь постучали."
    th "Кому я так сильно понадобился?"
    nd_il "Войдите!"
    window hide

    $ renpy.pause(1)
    play sound sfx_open_door_1
    show mt normal pioneer far at center with dspr
    play sound sfx_close_door_1
    $ renpy.pause(1)
    
    window show
    "Прокричал я, и в домик вошла Ольга Дмитриевна."
    th "Ну конечно."
    mt "Доброе утро, Илья."
    "Я было подумал, что она не будет меня ругать за это, но упустил то, что я таким образом просыпаю уже вторую линейку."
    show mt angry pioneer far at center with dspr
    
    mt "Ты опять линейку проспал."
    window hide

    $ renpy.pause(1)

    window show
    "Настроение итак было фиговым, чтобы начинать огрызаться со взрослыми людьми, поэтому у меня был только один выход: сыграть виновного."
    nd_il "Не злитесь, Ольга Дмитриевна."
    nd_il "В следующий раз я постараюсь прийти вовремя.{w} Поймите, я не специально."
    window hide

    $ renpy.pause(2, hard=True)
    show mt normal pioneer far at center with dspr
    $ renpy.pause(1, hard=True)
    hide mt with dspr

    window show
    "После моего ответа Ольга Дмитриевна смягчила свой взгляд, и села передо-мной на кровать."
    "И кажется, это сработало..."
    mt "Илья, пойми, я не хочу показаться злой старой тёткой перед пионерами."
    mt "Я такая же пионерка, как и вы."
    mt "И мне кажется, я итак вам слишком много разрешаю."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    nd_il "Ольга Дмитриевна, я ни в коем случае не считаю вас злой или старой."
    nd_il "Давайте лучше обсудим планы на сегодняшний день."
    window hide

    window show
    vg "Поаккуратнее со своим мнением. Ты в Советском Союзе, не забывай."
    th "То же государство, просто с коммунистическим строем."
    window hide

    $ renpy.pause(1, hard=True)
    show mt grin pioneer at center with dspr
    
    window show
    mt "Давайте."
    "Я не верил своим глазам.{w} Ольга Дмитриевна только что, словно маленькая девочка, передразнила меня."
    mt "У нас сегодня день пляжных игр."
    mt "Мы будем играть в волейбол на пляже, и те, кто умеют плавать смогут поиграть на воде в мяч…"
    th "Из неё получился бы хороший тамада."

    show mt smile pioneer at center with dspr

    mt "...Если захочешь, то тоже сможешь поиграть с друзьями."
    nd_il "Круто. Я ещё ни разу не был на не секретном пляже."
    "Улыбнувшись, проговорил я."
    mt "Значит сегодня будет прекрасная возможность."
    mt "Погоди, что значит \"на секретном\"?"
    nd_il "Это уже не имеет значения. С этого дня он уже официально не секретный."
    "Ольга Дмитриевна непонимающе посмотрела на меня. Хотя по выражению её лица, она даже не пыталась понять мною сказанное."
    window hide

    $ renpy.pause(2)
    show mt normal pioneer at center with dspr
    
    window show
    mt "Заговорилась я с тобой.{w} Пойду Шурика с Электроником проверю."
    mt "А ты вставай, одевайся, и к умывальникам."
    nd_il "Будет сделано."
    window hide

    hide mt with dspr
    $ renpy.pause(1)
    play sound sfx_open_door_1
    play sound sfx_close_door_1    
    
    window show
    "С этими словами вожатая вышла из домика, оставив меня одного в нём."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Кстати.{w} Нужно и мне к Электронику сходить за зарядкой."
    th "Но пока, как и сказала вожатая, время отправляться к умывальникам."
    window hide

    $ renpy.pause(1)

    show black with dissolve2
    stop ambience fadeout 2
    $ renpy.pause(2)
    play ambience ambience_camp_center_day fadein 3
    $ renpy.pause(1)
    play sound sfx_close_door_1
    scene bg ext_house_of_sl_day with dissolve2
    $ renpy.pause(2)
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_houses_day with dissolve2

    $ renpy.pause(1)

    window show
    "На улице ярко светило солнце, приятно согревая кожу."
    "От вчерашнего дождя не осталось и следа, как будто его вообще не было."
    "Я шёл по каменной дорожке и наслаждался этим летним и по необыкновению спокойным утром."
    "Может оно и к лучшему, что я не ушёл отсюда. Это место определённо идёт мне на пользу, пусть и не так быстро и действенно. Хотя учитывая, что я появился здесь всего три дня назад, оба этих аргумента существенно теряют свой вес."
    "Не каждый сможет измениться за это время так, как изменился я.{w} Хотя бы в том, что мне не противно общество, в котором я нахожусь."
    "Да и та девочка-енот Даша..."
    "Она возможно будет следить за мной и моей безопасностью, вместе с безопасностью этого лагеря. И не понятно, почему я так в этом уверен."
    window hide

    $ renpy.pause(1)
    show black with dissolve2
    scene bg ext_washstand_day with dissolve2

    window show
    "Вскоре на горизонте показались умывальники."
    "Которые с самого начала моего появления в лагере показались мне странными."
    window hide

    scene bg ext_washstand2_day with dissolve
    $ renpy.pause(1)
    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream
    $ renpy.pause(1)
    
    window show
    "Подойдя к одному из них, я открыл кран и набрал в руки воды."
    "Она была на удивление тёплой.{w} Видимо, успела нагреться за время, пока я спал в своей кровати.{w} Оно и не мудрено. До одиннадцати часов сплю в этом лагере, наверное, только я."
    "Благодаря более-менее тёплой воде я спокойно умыл лицо, вытер его насухо полотенцем и принялся за чистку зубов."
    window hide

    $ renpy.pause(1)

    window show
    "В голове заиграла песня \"Glorious Morning\", а ещё радовал тот факт, что скоро она будет играть из динамика моего телефона."
    "Так как свои наушники я отдал на растерзание кибернетикам, именно так мне и придётся довольствоваться музыкой.{w} Но даже это будет лучше чем никак."
    th "Может, с этими \"учёными\" можно было договориться как-то по другому?{w} Идей каких-нибудь для их изобретений из будущего посоветовать."
    th "Хотя что мне им советовать. Они уже, по идее, другим проектом заняты.{w} Да и не стоит оно того."
    window hide

    $ renpy.pause(1)
    
    stop sound_loop
    play sound sfx_close_water_sink
    
    $ renpy.pause(1)

    scene bg ext_washstand_day with dissolve

    window show
    "Я ещё раз умыл лицо и обернулся назад, зная, что обитатели этого лагеря любят появляться в этом месте у меня за спиной."
    "Да и в моей памяти до сих пор сохранился такой момент неловкой встречи с Леной."

    show us smile pioneer at center with dspr
    
    "Меня встретила Ульяна, держащая в руках лёд."
    "Быстро среагировав, она спрятала его за спину, но недостаточно аккуратно, чтобы я этого не заметил."
    
    stop music fadeout 3
    
    nd_il "Доброе утро, Ульяна. Где ты нашла лёд в этот жаркий день?"

    show us sad pioneer at center with dspr

    us "Ну блин! Как ты узнал?"
    nd_il "Да, жаль, а ведь всё могло получить…"
    window hide

    play music ndm_list['apocalyptica_hope'] fadein 3

    with flash_red

    show us laugh pioneer at center with dspr

    window show
    "В это мгновение по моей спине прокатился холод и застрял на моём поясе."
    "Значит затейников было двое, но для меня это уже перестало иметь какую-то значимость."
    with hpunch
    nd_il "Аа-аа-аа!"
    "Сзади послышался хохот, по которому можно легко узнать его владельца — Алиса." 
    
    hide us with dspr
    show dv laugh pioneer at center with dspr

    "Я повернулся к Алисе, но потом понял, что сделал это очень зря."
    "Очередную порцию льда за шиворот засыпала мне Ульяна."

    nd_il "Ай-ай-ай-ай-ай."

    hide dv with dspr

    "Я начал вытаскивать лёд из-за шиворота, но он как назло укатывался всё дальше.{w} Пока девочки истерично хохотали, я набрал в руки воды, и обрызгал первую и вторую негодяйку."
    window hide

    $ renpy.pause(1)
    
    window show
    "Вот только я не учёл одного: их было вдвое больше, и они также принялись набирать в руки воду." 
    window hide

    show black with dissolve
    
    window show
    "Мне ничего не оставалось, как бежать."
    "Бежать сверкая пятками, иначе я мог оказаться под залпами воды."
    window hide

    $ renpy.pause(1)

    window show
    "Быстро схватив свои умывальные принадлежности я побежал к своему домику."
    window hide

    scene bg ext_houses_day with dissolve

    window show
    us "Он убегает! Лови его!"
    th "Это конец.{w} Если я не успею, то моей оставшейся сухой одежде каюк."
    window hide

    show black with dissolve

    window show
    "Я перепрыгнул через заборчик чтобы запутать преследователей, а затем побежал через другие домики к своему."
    window hide

    scene bg ext_house_of_sl_day with dissolve
    
    window show
    "Проходя через кусты и высокую траву, я подбежал к двери своего домика, и открыв её забежал внутрь."
    window hide

    $ renpy.pause(1)
    
    stop ambience fadeout 3
    play sound sfx_open_door_1
    show black with dissolve
    scene bg int_house_of_gg_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    play sound sfx_close_door_1

    window show
    "Теперь нужно было как-то заблокировать эту дверь, а замка на ней конечно не было."
    "Я оглянул домик, и решение моей проблемы пришло само собой."
    window hide

    $ renpy.pause(1)
    
    window show
    "Я пододвинул шкафчик к двери, и девочки уже не смогли бы пробраться в моё жилище."
    vg "Во дурак."
    vg "Дверь наружу открывается, гений."
    th "Будь, что будет."
    window hide

    stop music fadeout 3
    $ renpy.pause(2)

    window show
    dv "Ульяна!"
    window hide

    $ volume (0.2, 'sound')
    play sound sfx_alisa_falls
    $ renpy.pause(1, hard=True)
    play sound nds_list['box_fall']
    $ volume (1.0, 'sound')
    $ renpy.pause(1, hard=True)

    window show
    th "Уп-с-с. . ."
    mt "Ульяна, ты опять за своё?!{w} Я тебе сколько раз говорила смотреть, куда бежишь?!" 
    mt "Это уже не первый раз!"
    mt "Мне придётся вынести тебе наказание!"
    us "Не надо, Ольга Дмитриевна, я больше не буду."
    mt "Вот это мы и посмотрим."
    mt "Сегодня ты весь день будешь дежурить в столовой."
    us "Но Ольга Дмитриевна!"
    mt "Никаких но.{w} В пол первого идёшь накрывать младшим отрядам…"
    window hide

    $ renpy.pause(2)

    stop ambience fadeout 3
    play sound sfx_open_door_1
    show black with dissolve
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1)

    show mt rage pioneer far at right
    show us sad pioneer far at left
    show dv guilty pioneer far at fleft 
    with dspr

    $ renpy.pause(1)

    window show
    "Выйдя на улицу передо-мной оказалась интересная картина:{w} мокрая вожатая с наполовину полным стаканом чая отчитывает не менее мокрую Ульяну.{w} А Алиса стоит рядом и смотрит на всё это." 
    window hide

    hide us
    hide dv
    hide mt
    with dspr

    window show
    "Я подошёл к вожатой за спину и похлопал по плечу, прервав лекцию о том, как плохо хулиганить."
    "Мне стало жалко Ульяну. Они с Алисой просто хотели разыграть меня. Но если бы не вожатая, им бы действительно удалось."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Ольга Дмитриевна, я тоже к этому причастен."

    show mt normal pioneer at center with dspr

    th "Если делить наказание, то поровну."
    mt "Илья, ты серьёзно?"
    mt "Я думала, что ты-то по взрослее, по опытнее будешь."
    "Ульяна сделала недовольное лицо и закатила глаза."
    nd_il "Я готов поделить наказание с товарищем."
    window hide

    $ renpy.pause(2)

    window show
    mt "Ладно, пионеры. Надеюсь вы выполните свои обязанности."
    window hide

    hide mt with dspr

    $ renpy.pause(1)

    show dv guilty pioneer at left with dspr
    show us sad pioneer at center with dspr

    window show
    "Мы с Алисой стояли и с сожалением смотрели на мокрую Ульяну."

    dv "Я это... Пошла.{w} Вы сами тут разберётесь как-нибудь, да?"

    hide dv 
    with dspr

    "Сказала Алиса, быстрым шагом уходя с места преступления."

    th "Почему она всегда бросает меня и Ульяну в подобных ситуациях?"
    th "Меня-то понятно почему. А свою подругу?"
    us "Ну, чего уставился?"
    us "Ты специально со мной в столовой дежурить пошёл, чтобы поиздеваться?"
    window hide

    menu:
    
        "Поднять ей настроение":

            $ nd_us_flaggs += 1
            $ persistent.nd_moral_points += 1

            window show
            nd_il "Ульяна, не пойми меня неправильно. Я просто хочу тебе помочь."
            
            show us dontlike pioneer at center with dspr
            
            us "Делать тебе нечего, кроме того, как малявкам помогать."
            us "Ты из себя вон какой взрослый, а сам даже пионерский галстук завязать не можешь."
            nd_il "Ульяна, пожалуйста, давай не будем ссориться.{w} Это не выгодно нам обоим."
            us "А какая тебе выгода от дежурства в столовой?"
            nd_il "Я просто хочу больше времени провести с тобой."
            window hide

            $ renpy.pause(1)
            
            show us shy pioneer at center with dspr

            window show
            "Щёки Ульяны немного порозовели после мною сказанного. Отступать сейчас было некуда, даже если сейчас не время для откровений."
            nd_il "Понимаешь, мне давно ни с кем не было так весело, как сейчас с тобой."
            us "Правда?"
            nd_il "Да, и к тому же считаю наказание Ольги Дмитриевны по отношению только к тебе не совсем оправданным. Я ведь мог уйти сейчас также как Алиса, но это не решило бы проблему."
            nd_il "Ладно, давай встретимся в пол первого у столовой?"
            show us shy2 pioneer at center with dspr
            "Ульяна улыбнулась мне. Я вновь увидел в её глазах что-то.{w} Это было похоже на то, что я видел, когда она стояла над моей кроватью."
            "Её взгляд... Я не замечал этого раньше, но он способен меняться из разу в раз. Словно молодая девушка примеряет платья."
            "И сейчас платье Ульяны выглядело невероятно..."
            us "Хорошо. Я побежала..."
            window hide

            hide us with dspr
            $ renpy.pause(1)

            window show
            nd_il "Увидимся..."
            "Проговорил я себе под нос, провожая вслед убегающую пионерку."
            "Мне предстояло сейчас зайти в свой домик и переодеться в новую форму, а потом уже решить, куда мне идти дальше и что делать."
            "Этим утром мне нужно было уложиться сразу в три дела."
            window hide

            $ renpy.pause(1)

            show black with dissolve2

        "Промолчать":


            $ persistent.nd_moral_points -= 1
            $ miss_us_r_1 = True
            $ nepodhod_87 = True

            $ renpy.pause(1)
            
            show us dontlike pioneer at center with dspr

            window show
            us "Я это с самого начала поняла..."
            hide us with dspr
            nd_il "Стой!"
            "Ульяна убежала в неизвестном направлении."
            window hide

            $ renpy.pause(2)
            
            window show
            "Я стоял на дороге, как дурак, осматриваясь по сторонам в поисках косых взглядов и тому подобного."
            "Слава богу, что кроме нас с Ульяной тут никого не было."
            "Никто не видел этого случившегося позора."
            window hide

            $ renpy.pause(1)
            
            window show
            th "Почему я не сказал ни слова? Чего я испугался?"
            "Иногда чтобы показаться умным - нужно просто молчать. Сейчас всё произошло наоборот. Я чувствовал себя очень неловко. И даже не знаю из-за чего. Из-за того что я не утешил эту пионерку или потому-что вся моя спина была мокрой, будто от пота."
            "Но делать было нечего.{w} Что случилось то случилось, и исправить всё я смогу только лишь после визита в столовую к ней на помощь в дежурстве."
            window hide

            $ renpy.pause(1)
            
            window show
            "После этого я сразу же отправился домой для того, чтобы посушить свою пионерскую форму и поменять её на новую."
            window hide

            show black with dissolve2


label home_d2_us_gb:

    $ renpy.pause(2, hard=True)

    if miss_us_r_1 == True:

        window show
        th "Интересно, она правда на меня обиделась?"
        vg "А ты как думаешь?"
        th "Ну не знаю. Я же ничего не сделал."
        vg "Так может, в этом всё дело?" 
        window hide

    else:
        
        window show
        th "Интересно, а за дежурства повара будут давать какое-нибудь мороженое, как в тот раз."
        vg "Ещё работу не выполнил, а уже о награде мечтаешь."
        vg "Ты знал, что дежурство на весь день?"
        th "Оно того, определенно, стоит."
        window hide

    stop ambience fadeout 3
    $ renpy.pause(2, hard=True)
    play sound sfx_open_door_1
    scene bg int_house_of_gg_day with dissolve
    play ambience ambience_int_cabin_day fadein 3
    play sound sfx_close_door_1

    $ renpy.pause(1)

    window show
    "Войдя внутрь, я открыл шкафчик, и достав оттуда комплект свежей формы положил его себе на стол."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    play sound nds_list['applysuit']
    $ renpy.pause(2, hard=True)
    play sound sfx_open_window
    $ renpy.pause(2, hard=True)

    scene bg int_house_of_gg_day with dissolve2
    
    window show
    "Сняв свою мокрую одежду, я положил её на сушилку за окном."
    "Солнце пекло знатно, и по ощущениям форма должна была высохнуть менее чем за час."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    play sound nds_list['applysuit']
    $ renpy.pause(1)
    scene bg int_house_of_gg_day with dissolve

    play sound sfx_open_cupboard
    $ renpy.pause(1)

    window show
    "Надев новый комплект, я подошёл к шкафу, открыл дверцу и посмотрел на себя в зеркало."
    "Галстук я не развязывал, а просто снял его с мокрой пионерской формы и надел поверх сухой."
    "Не было смысла его сушить, так как на нем и не было следов разбоя этих девушек."
    window hide

    $ renpy.pause(1)

    show cg semyon_mirror with dissolve

    window show
    "Признаться, в новой форме я выглядел довольно солидно.{w} Учитывая, что эта самая солидность ограничивалась степенью поглаженности и загрязнённости моей формы."

    if miss_us_r_1 == True:
        vg "Интересно, кто тебе будет теперь галстук завязывать."
    window hide

    $ renpy.pause(1)

    show black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg int_house_of_gg_day with dissolve

    window show
    th "Так, теперь мне нужно к кибернетикам сходить за зарядкой..."
    th "Потом музыку послушать.{w} Ах, и Ольге Дмитриевне на пляже помочь, а то потом не отстанет от меня."
    th "К тому же я утром для себя решил, что постараюсь принести для этого лагеря как можно больше пользы. Чего бы мне это не стоило."
    "Для меня слишком принципиально не стать тем, кого я презираю. А чтобы этого не допустить, нужно тренироваться, ограничивать себя в сомнительных благах."
    "К ним относится не только то, что приносит удовольствие, но и то, что приносит страдание другим..."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    play sound sfx_open_door_1    
    $ renpy.pause(1, hard=True)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve2
    play sound sfx_close_door_1

    $ renpy.pause(1)
    show black with dissolve
    scene bg ext_houses_day with dissolve

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(1)
    scene bg ext_clubs_day with dissolve2
    $ renpy.pause(1)

    play sound sfx_knock_door2
    
    $ renpy.pause(2)

    stop ambience fadeout 2
    play sound sfx_open_door_clubs
    show black with dissolve
    $ renpy.pause(1)
    play music music_list["smooth_machine"] fadein 3
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_clubs_male_day with dissolve
    play sound sfx_close_door_1

    window show
    "Постучав в дверь и зайдя внутрь, я увидел Электроника, работающего над своим новым проектом..."
    "А нет, погодите.{w} Он просто чинил утюг."
    th "Вот она - работа для настоящих кибернетиков."
    "От этой мысли, у меня на лице невольно возникла улыбка, которую я попытался спрятать за эмоцией заинтересованности."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Привет.{w} Я за аккумулятором и зарядкой пришёл."
    window hide

    $ renpy.pause(1)
    show el normal pioneer far at center with dspr
    $ renpy.pause(1)
    show el normal pioneer at center with dspr
    $ renpy.pause(1)

    window show
    el "Здорóво.{w} Держи."
    el "Только советую полностью свой агрегат не заряжать."
    el "А то я не уверен, что он в таком случае что-то не замкнёт..."
    el "А так при частичной зарядке этого аккумулятора замыкания произойти не должно."
    
    hide el with dspr
    
    "Сказав это, Электроник протянул мне мой аккумулятор и устройство, отдалённо напоминающее современную, так называемую \"лягушку\" для зарядки батарей телефонов."
    "Я взял аккумулятор, зарядник, и положил их к себе в карман шорт. В них создался неприятный горб, который сразу будет бросаться в глаза."
    "Увидев это, я достал из кармана изобретение кибернетика и оставил его в руке."
    nd_il "Спасибо.{w} Ну я это,{w} пойду пожалуй."
    "Произнес я, открывая входную дверь."
    window hide

    hide el with dspr

    play sound sfx_open_door_clubs
    stop music fadeout 2

    window show
    el "Подожди."

    show el surprise pioneer at center with dspr

    el "Ты Шурика не видел сегодня?"
    th "О, точно, как я мог забыть."
    nd_il "Видел.{w} Он утром сегодня в старый лагерь уходил.{w} За деталями какими-то."
    window hide

    $ renpy.pause(1)
    show el normal pioneer at center with dspr

    window show
    el "Точно."
    el "А за какими деталями он тебе не сказал?"
    nd_il "Либо не сказал, либо я не помню."

    show el smile pioneer at center with dspr
    
    el "Ну ладно тогда."
    el "Заходи если что вдруг случится."
    
    hide el with dspr
    
    nd_il "Всенепременно."    
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_clubs_day with dissolve
    play sound sfx_close_door_1

    $ renpy.pause(1)

    window show
    th "Странные эти кибернетики на самом деле.{w} Но за подгон в виде зарядного устройства стоит отдать им должное."
    th "Схожу в домик, как раз проверю его."
    th "В нём определенно должна быть какая-нибудь розетка. А если не будет, проверю в домике Ольги Дмитриевны.{w} У неё-то точно розетка найдётся."
    th "Должна же она себе как-то кофе или чай разогревать в конце концов. Либо же за этим она ходит в столовую..."
    window hide

    show black with dissolve2
    $ renpy.pause(1)
    
    window show
    "По пути я разглядывал сделанную кибернетиками приблуду."
    "Какие-то провода, выпирающие медные контакты, на которые, видимо, ставится батарея.{w} Причём вся эта конструкция выглядела достаточно крепкой, хоть и \"открытой\"."
    th "Вот оно, славянское изобретение!.."
    
    $ renpy.pause(1)
    
    th "А если без шуток, то кибернетики реально постарались над своей работой"
    th "Смогли прыгнуть выше головы. Хотя..."
    th "Наверняка к ним подходило множество пионеров со своими какими-то просьбами что-то для них спаять.{w} Однако мой \"заказ\" точно должен был удивить его исполнителей."
    th "Тем более что им пришлось работать с технологиями будущего..."
    window hide

    $ renpy.pause(1)

    scene bg ext_house_of_sl_day with dissolve2
    $ renpy.pause(1)

    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_int_cabin_day fadein 2
    scene bg int_house_of_gg_day with dissolve
    play sound sfx_close_door_1

    window show
    "Зайдя внутрь своего домика, я принялся искать розетку по всему домику."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    $ renpy.pause(2)
    hide black with dissolve
    $ renpy.pause(1)

    window show
    "Найдя розетку под своей кроватью, я сильно обрадовался находке, и подключил прибор в сеть."
    "Красный индикатор показал, что прибор действительно подключен и работает."
    window hide

    $ renpy.pause(1)
    
    window show
    "После этого я вставил аккумулятор в медные выемки, и на приборе загорелся зелёный индикатор."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Похоже, что-то работает.{w} Сейчас посмотрю, сколько процентов."
    window hide

    play sound sfx_open_cupboard

    window show
    "Достав из шкафчика свой телефон, я вставил внутрь него батарею, зажал кнопку питания и принялся ждать запуска."
    window hide

    $ renpy.pause(2)
    
    window show
    "Спустя сорок секунд экран включился.{w} Индикатор батареи показывал восемьдесят семь процентов."
    th "Они, видимо, уже мою зарядку проверяли.{w} Красота да и только."

    with hpunch
    
    nd_il "Слава вам, кибернетики!"
    "Я закричал во весь голос, забыв о том, что у меня открыто окно, и всем на улице были слышны мои ликования. Но в текущий момент это меня ни капельки не волновало."
    window hide

    $ renpy.pause(2, hard=True)
    play sound sfx_knock_door3_dull
    
    window show
    "Послышался стук в дверь."
    th "Это, кажется, по поводу моих криков."
    "Я быстро закинул телефон под подушку."
    nd_il "Входите!"
    window hide

    play sound sfx_open_door_1
    $ renpy.pause(1)
    show mt normal pioneer far at center with dspr
    play sound sfx_close_door_1
    $ renpy.pause(1)

    window show
    "На пороге показалась Ольга Дмитриевна."
    mt "Илья, ты чего раскричался?"
    nd_il "Кибернетиков хвалю, Ольга Дмитриевна."

    hide mt with dspr
    show mt smile pioneer at center with dspr
    
    "По-видимому, вожатая быстро смекнула текущую ситуацию, чтобы обернуть её в плюс для себя."
    mt "Ну раз ты умылся и уже свободен, можешь прийти на пляж и помочь нам его подготовить к мероприятию?"
    "И моё хорошее настроение стало причиной не отказать вожатой в её просьбе."
    nd_il "Да, Ольга Дмитриевна, без проблем."

    hide mt with dspr
    show mt smile pioneer far at center with dspr
    mt "Тогда приходи на пляж. Там уже всё есть, осталось только расставить."

    play sound sfx_open_door_1
    hide mt with dspr
    play sound sfx_close_door_1

    "Как только дверь захлопнулась за спиной вожатой, я хлопнул в ладоши и потёр их друг о друга."
    th "Как я уже говорил, сейчас музыка будет играть из моего телефона."
    "Я достал телефон из-под подушки, и включил мечту этого тёплого утра."
    "А точнее — \"Glorious Morning\"."
    window hide

    $ renpy.pause(1)
    play music ndm_list['glori_morning'] fadein 4

    window show
    "Тишину внутри домика тут же развеяли издаваемые моим телефоном звуковые волны, так желаемые мной."
    "Я был ужасным меломаном, и не мог прожить без музыки ни единого дня. И в этом была моя слабость. Слабость, за которую я себя ненавидел. Но даже это будет безобиднее многих аморальных вещей, принятых в этом обществе."
    window hide

    $ renpy.pause(1)

    window show
    th "Неужели..."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve
    $ renpy.pause(1)

    window show
    "Я вышел из домика и, слегка пританцовывая, отправился в сторону предполагаемого пляжа."
    "Как я понял, в какой стороне находится пляж?{w} Да очень просто."
    "В ту сторону шли некоторые пионеры. Да и Ольга Дмитриевна ещё не достаточно пропала из виду со своего пришествия в мой домик."
    window hide

    show black with dissolve2
    $ renpy.pause(2, hard=True)
    scene bg ext_houses_day with dissolve2

    window show
    "Некоторые пионеры смотрели на меня косо из-за новомодного \"проигрывателя мини-пластинок\" у меня в кармане, но это меня ничуть не волновало.{w} Я просто шёл дальше до места назначения." 
    window hide

    show black with dissolve
    $ renpy.pause(2)
    hide black with dissolve

    window show
    "Но внезапно меня постигла истина."
    "Заслушавшись красивой песней, я потерял Ольгу Дмитриевну и пионеров, идущих за ней на пляж."
    th "И как теперь понять, куда мне идти?"
    th "Может у кого-нибудь из отряда спросить?"
    window hide

    $ renpy.pause(1)

    stop ambience fadeout 3
    show black with dissolve2

label pl_d4_nd_l:

    $ renpy.pause(3)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_square_day with dissolve2

    window show
    "Проходя через площадь, я увидел Лену, сидящую на скамейке и читающую какую-то книгу."
    "И эта девушка должна была мне указать на путь истинный.{w} Навести меня на сторону пляжа."
    "И я не упустив этой возможности подбежал к ней, чтобы задать свой вопрос."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Привет, Лен.{w} Ты не подскажешь, где тут пляж?"
    window hide

    show un surprise pioneer at center with dspr
    $ renpy.pause(1)
    show un smile pioneer at center with dspr

    window show
    un "Привет, Илья. Вон туда дальше идёшь, потом поворачиваешь направо и там будет пляж."
    nd_il "Спасибо."
    un "Пожалуйста."
    un "А откуда у тебя музыка играет?"
    nd_il "Это из проигрывателя мини-пластинок.{w} Ничего особенного."
    th "Действительно, карманный проигрыватель в СССР, ничего особенного."
    window hide

    stop music fadeout 3
    show black with dissolve2
    $ renpy.pause(2)

    window show
    "Так, сначала налево, потом направо. Пара пройденных метров и кажется... Я его вижу!"
    window hide

    $ renpy.pause(3, hard=True)

    play music ndm_list['jzone'] fadein 3
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_beach_day with dissolve2

    window show
    "Пройдя по указанному Леной пути, я вышел на пляж."
    window hide

    $ renpy.pause(1)
    
    window show
    "На песке валялась волейбольная сетка для пляжного волейбола, два маленьких мячика, сдутые лодки, большой мячик и подобие ворот для игр на воде." 
    "Также рядом лежали такие инструменты как насос, молоток и тому подобные."
    "Видимо, именно этим инструментарием мне предстояло сейчас работать.{w} И я тут же прикинул, сколько времени уйдет на эту самую работу."
    window hide

    $ renpy.pause(1)
    
    window show
    th "Ну… Тут работы примерно на часик."
    window hide

    $ renpy.pause(1)

    window show
    "Я оглянулся вокруг, и найдя девочек из своего отряда, медленно отправился к ним."
    "Они тоже искали пионеров из отряда, чтобы привлечь их к нашему общему делу."
    window hide

    $ renpy.pause(1)

    show sl smile pioneer at left
    show mt normal pioneer at center
    show mi smile pioneer at right
    with dspr

    window show
    mi "Привет, Илья!"
    nd_il "Привет всем! Какой у нас план работы?"
    sl "Нам сейчас нужно всё к пляжным играм подготовить."
    window hide

    $ renpy.pause(1)
    
    window show
    mt "Илья, вы с Машей должны поставить сетку и надуть все мячики и лодки."
    mt "Славя и Электроник будут ставить буйки и делить пляж на зоны."
    mt "Сейчас ещё работники подойдут.{w} А вы пока можете начать работу."
    window hide

    hide sl
    hide mt
    with dspr
    hide mi with dspr

    $ renpy.pause(2)

    show mi smile pioneer at center with dspr

    window show
    nd_il "Давай поставим сначала сетку, а потом возьмёмся за следующее?"
    mi "Хорошо, только давай управимся быстро, а то нужно ещё в столовой успеть пообедать, а потом сразу же купаться. Кстати, ты умеешь плавать? Я вот умею плавать. давно-давно научилась..."
    nd_il "Да, умею.{w} Приходилось в бассейн ходить."
    nd_il "Давай, как ты сказала, побыстрей начнём работать. Меньше слов - больше дела, так сказать."
    mi "Да, давай начнём. Только подожди я молоток принесу. Вот забьём сетку и можно будет в волейбол играть…"
    "Японка говорила так быстро, что я даже не успевал обдумывать всё ею сказанное.{w} Возможно, если вывести всё ею сказанное на монитор, придётся большинство предложений обрывать многоточием или просто пропускать, а если считать в листах бумаги, то за всё время общения со мной она наговорила на три тома знаменитого романа Льва Толстого."
    "\"Война и мир\", ну конечно же. И тут она начнёт рассказывать, как они изучали его ещё в школе. Не знаю с чего я решил, что в этой параллельной вселенной в Японских школах преподают русских писателей."
    window hide

    $ renpy.pause(1)

    hide mi with dspr
    
    window show
    "Но слава богу, она ушла за молотком..."
    th "Вот это пулемёт. С ней не соскучишься.{w} Всегда поддержит разговор если что..."
    th "С этой стороны, не нужно даже напрягать мозги, чтобы придумать новую тему для разговора."
    th "Но зато необходимо научиться понимать ею сказанное."
    th "Не то, чтобы она выговаривала слова не чётко. Скорее наоборот. Просто слишком быстро."
    window hide

    show black with dissolve
    $ renpy.pause (2, hard=True)
    hide black with dissolve

    show mi smile pioneer at right with dspr
    
    window show
    "Как только Маша вернулась с нужным нам инструментом, мы незамедлительно начали работу."

    hide mi with dspr 

    "Я поставил сетку, а Маша начала забивать её в песок." 
    "Пока она это делала, я заметил, что на вбиваемой ножке нарисована отметка, и под ней надпись \"11 см\"."
    "Видимо, это сделано для того, чтобы точнее и правильнее забить сетку в песок,{w} что предусмотрительно."
    window hide

    $ renpy.pause (1)
    
    window show
    "Когда Маша забила первую ножку до отметки, я остановил её, и мы сразу же взялись за вторую ножку."
    window hide

    $ renpy.pause (1)
    
    window show
    "Растянув сетку я зафиксировал ножку снизу, а Маша принялась её забивать."
    window hide

    $ renpy.pause (1)
    show blink
    $ renpy.pause (2)
    hide blink
    show unblink
    $ renpy.pause (1)

    window show
    "Пока мы работали, нам удалось завязать разговор,{w} что в принципе не удивительно,{w} если учитывать то, что моя собеседница — чересчур разговорчивая девушка."

    show mi smile pioneer at center with dspr

    mi "Илья, а ты откуда сюда приехал?"
    "На моё удивление, девушка ограничилась одним вопросительным предложением."
    nd_il "Я сюда из Краснодара приехал.{w} Довольно красивый город.{w} Ты обязательно должна побывать там."
    th "По крайней мере, через тридцать лет."
    mi "Обязательно побываю. А я из Токио приехала. Тоже очень хороший город. Если поедешь в Японию то обязательно тоже там побывай."
    "Слово \"Токио\" Японка произнесла с достаточно японским акцентом, чтобы ей поверить."
    hide mi with dspr
    "Насколько я знал, Токио — это столица Японии.{w} На картинках в интернете она выглядела просто замечательно." 
    "Этот город у меня даже на рабочем столе стоял..."
    window hide

    $ renpy.pause (2)

    window show
    "Тем временем Маша забила вторую ножку в песок, и положив молоток села рядом с сеткой."
    nd_il "Давай теперь мячик накачаем."

    show mi grin pioneer at center with dspr
    
    mi "Давай…"
    
    hide mi with dspr
    
    "Маша встала с песка и уже хотела побежать за насосом, но я её остановил."
    nd_il "Матсу! Я сам принесу."
    "Сказал я и побежал за насосом."

    stop music fadeout 3

    "Услышав знакомое слово на родном языке, Маша остановилась и начала ждать меня у сетки."
    window hide

    show black with dissolve
    $ renpy.pause (1)
    hide black with dissolve2

    window show
    "Взяв насос, я заметил приближающихся потенциальных работников: Алису, Лену, Семёна, и Ольгу Дмитриевну в их главе."
    window hide

    show dv guilty pioneer far at fleft
    show un smile pioneer far at left
    show mt normal panama pioneer at center
    show pi2 normal pioneer at right
    with dspr

    window show
    "По лицу Алисы было видно, что тащили её на пляж силой."
    "Из меня невольно вырвался смешок."
    window hide

    $ renpy.pause (1)

    show dv grin pioneer far at fleft with dspr

    window show
    "Алиса заметила меня и посмеялась надо мной, видимо из-за того, что меня заставили работать."
    "Но её радость была мне не до конца понятна. Она же знала, что её привели сюда для того же самого. Видимо, мысль о том что я тоже работаю невероятно грела ей душу."
    window hide

    hide dv
    hide un
    hide mt
    hide pi2 normal pioneer
    with dspr

    window show
    "Я показал ей язык, и отправился к Маше надувать вместе с ней мячики и лодки."
    window hide

    show black with dissolve
    $ renpy.pause (2)
    hide black with dissolve 
    show mi normal pioneer at center with dspr
    $ renpy.pause (1)
    hide mi with dspr

    window show
    "Придя к ней, я взял волейбольный мячик и принялся надувать его насосом."
    "Маша же надувала мягкие шарики ртом, что у неё хорошо получалось. Это было не удивительно если брать во внимание её быстрое произношение слов." 
    th "Надо как-нибудь попросить её зачитать Эминема, а самому посмотреть на это зрелище."
    "А почему бы не предложить ей это прямо сейчас?{w} Как раз перерыв сделаем."
    nd_il "Маша, ты можешь кое-что зачит...{w} Кхм.{w} Спеть для меня?"

    show mi smile pioneer at center with dspr

    mi "Да Илья, а что ты хочешь, чтобы я спела для тебя? Что-то на японском?.."
    nd_il "Сейчас покажу."
    window hide

    hide mi with dspr
    
    $ renpy.pause (1)
    
    window show
    "Я вновь достал свой телефон, включил первый попавшийся трек и открыв слова к нему отдал телефон Японке."
    nd_il "Можешь спеть под музыку этот отрывок из песни?"
    nd_il "Он быстрый, я сам не смогу его спеть, хочу послушать как споёшь его ты."
    
    show mi smile pioneer at center with dspr
    
    mi "Поняла. Сейчас послушаю..."
    nd_il "Ладно, слушай."
    
    hide mi with dspr
    
    "Сказал я и продолжил надувать мячики."
    window hide
    
    show black with dissolve

    $ renpy.pause (2)
    
    hide black with dissolve

    window show
    "Вскоре лодка была надута."
    "Краем уха я слышал, как Маша переслушивала этот момент песни и пыталась своим голосом подыгрывать автору, таким образом тренируясь в произношении."
    "Видимо её совсем не смущала подобная скорость. Из чего я могу сделать вывод, что она очень хорошо знала английский."
    "Япония удивительная страна. Её жители могут знать от трёх языков, когда я даже двух выучить до конца не могу. Моё знание английского ограничивается высказываниями о my own opinion в двух-трёх предложениях. Мне приходилось учить этот язык из-за мечты когда-нибудь уехать из страны, в которой жил двадцать лет."
    "Была у меня ещё идея выучить чешский и уехать в эту страну на учёбу,{w} но не сложилось."
    "Я решил забить на дальнейшее обучение, из-за плоскостопия и проблем с кожей меня не взяли в армию. Концом этой истории стала работа программистом и попадание сюда."
    
    show mi smile pioneer at center with dspr
    mi "Я готова, включи её на том моменте, на котором ты хотел."
    "Разрушила мои раздумья Маша, протянув мне в руке мой телефон."
    th "Да ладно, даже без текста что ли? Удивляешь,{w} Маша."
    window hide

    $ renpy.pause (1)
    
    window show
    "Я перемотал трек в нужное мне место, и в ожидании чего-то стоящего нажал на кнопку \"Play\"."
    "Из динамика телефона послышались клавиши пианино, Мику немного прислушалась, приготавливаясь к своей части..."
    window hide

    play music ndm_list['au_zachem'] fadein 3
    show mi serious pioneer at center with dspr
    stop ambience fadeout 3
    $ renpy.pause (21, hard=True)
    show black with dissolve2
    $ renpy.pause (1, hard=True)
    show cg mi_raper_d4_nd with flash

    window show
    mi "So Ray J. went straight to the radio station {nw=1}"
    $ renpy.pause (0.1)
    mi "The very next day, \"Hey Fab,{nw=1}"
    $ renpy.pause (0.1)
    mi "I'ma kill you!\"{nw=1}"
    $ renpy.pause (0.1)
    mi "Lyrics comin' at you at supersonic speed...{nw=1}"

    $ renpy.pause (0.2)

    mi "Uh, summa-lumma, dooma-lumma, you assumin' I'm a human. {nw=1}"
    $ renpy.pause (0.1)
    mi "What I gotta do to get it through to you I'm superhuman? {nw=1}"
    $ renpy.pause (0.1)
    mi "Innovative and I'm made of rubber so that anything you say is {nw=1}"
    $ renpy.pause (0.1)
    mi "ricochetin' off of me and it'll glue to you and... {nw=1}"
    
    "Маша читала его на одном дыхании, идеально попадая в ударные и не оставляла голосу из динамика ни малейшего шанса."
    th "А-фи-геть."
    "Я представлял как она в кепке \"OBEY\" читает рэп в микрофон на большой сцене."

    mi "...I'm devastating, more than ever demonstrating {nw=1}"
    $ renpy.pause (0.1)
    mi "How to give a censed audience a feeling like it's levitating {nw=1}"
    $ renpy.pause (0.1)
    mi "Never fading, and I know the haters are forever waiting {nw=1}"
    $ renpy.pause (0.1)
    mi "For the day that they can say I fell off, they'll be celebrating {nw=1}"
    $ renpy.pause (0.1)
    mi "'Cause I know the way to get 'em motivated {nw=1}"
    $ renpy.pause (0.1)
    mi "I make elevating music {nw=1}"
    $ renpy.pause (0.1)
    mi "you make elevator music..."

    th "Всё, надо заканчивать."

    stop music fadeout 6

    nd_il "Маша, стой, всё."
    window hide

    $ renpy.pause (1)
    scene black with dissolve2
    $ renpy.pause (2)
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_beach_day with dissolve2

    window show
    parr "Ну блин."

    "Скопившиеся зрители вокруг нас начали расходиться сразу после того, как я выключил музыку и тем самым закончил концерт."

    show mi grin pioneer at center with dspr

    mi "А есть у этого исполнителя ещё какие-нибудь песни? Я его ещё ни разу не слышала."
    th "Это потому, что он из будущего."
    nd_il "Ну да, есть. Давай я тебе что-нибудь другое включу?"
    mi "Давай, только в этой песне слова плохие были."
    nd_il "Навряд ли здесь кто-то кроме нас знает их значение."
    mi "А вообще у него неплохой стиль. Мне нравится. Я даже не знаю, как он называется."
    nd_il "Это рэп."
    mi "А, понятно. Я о таком даже не знала. Покажешь мне ещё какие-нибудь похожие песни?.."
    
    hide mi with dspr

    "Я принялся искать в своей музыкальной библиотеке что-то подобное. И найдя примерно ещё один трек на иностранном языке, мы продолжили с ней нашу работу."
    "Звук в телефоне был убавлен почти до минимума, так, чтобы никому кроме нас не было слышно этой музыки.{w} При широком оглашении о таком девайсе у пионера, этим делом могла заинтересоваться администрация лагеря."
    "А этого мне совсем не хотелось."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    "Солнце пекло, мне хотелось уйти отсюда куда-нибудь в тенёк. Казалось, недолго мне растаять на такой жаре."
    "Но с другой стороны нам с этой японкой оставалось сделать совсем немного: лодка, пару мячиков, и всё было готово..."
    window hide

    show black with dissolve
    $ renpy.pause (2)
    hide black with dissolve

    window show
    "Вскоре всё было закончено."
    "Я даже вспотел, и не совсем потому что я работал. Без панамы под таким солнцем находиться достаточно тяжело."
    "Я уже хотел позвать Ольгу Дмитриевну, чтобы та посмотрела на проделанную нами работу, но она уже сама шла к нам на встречу."
    window hide

    show mt normal panama pioneer far at center with dspr
    $ renpy.pause (1)
    show mt normal panama pioneer at center with dspr
    show mi smile pioneer at right with dspr

    window show
    mi "Ольга Дмитриевна, мы закончили!"
    "С гордостью произнесла Маша."
    mt "Молодцы."
    mt "Маша, ты можешь идти отдыхать."
    mt "А тебе, Илья,{w} если ты ещё не забыл,{w} бежать на дежурство в столовой."
    nd_il "Не забыл.{w} Дайте только отдохнуть пять минут..."
    window hide

    hide mt
    hide mi
    with dspr

    $ renpy.pause (1)

    window show
    "Ольга Дмитриевна ушла по каким-то своим делам, а я лениво и присел на песок и принялся разглядывать работающих пионеров."
    window hide

    $ renpy.pause (1)
    
    window show
    "Алиса и Семён собираются ставить ворота на воду. Было не понятно, как они собираются это делать, если судя по их действиям, они пытаются не заходить в воду."
    "Лена расставляет надувные лодки рядом с пляжем и привязывает их к берегу, и к ней подходит Славя, видимо, предлагая свою помощь."
    "А Маша уходит с пляжа по своим делам. Деловая девушка. К тому же очень талантливая, но чертовски разговорчивая."
    th "Читает рэп она, конечно, обалденно."
    th "Приедет на свою родину после отдыха в лагере и начнёт свою карьеру."
    th "Как говорится, построит свою империю с нуля."
    window hide

    $ renpy.pause (1)

    window show
    th "Вот я тоже сейчас отдохну, и пойду к столовой.{w} Хотя там, наверное, похолоднее будет..."
    window hide

    stop ambience fadeout 2
    show black with dissolve 
    $ renpy.pause (3, hard=True)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_away_day with dissolve2

    window show
    "Вот уже показалась столовая."
    window hide

    show black with dissolve
    scene bg ext_dining_hall_near_day with dissolve
    stop music fadeout 3
    
    window show
    "Я взбежал по лестнице на веранду и забежал внутрь."
    window hide

    play sound sfx_open_door_1
    stop ambience fadeout 3
    scene bg int_dining_hall_day with dissolve
    play ambience ambience_dining_hall_empty fadein 2
    play sound sfx_close_door_1
    
    $ renpy.pause (1)

    window show
    "Там меня уже ждала Ульяна, облокотившись на стену."

    if miss_us_r_1 == True:
        $ miss_us_r_l = False
        "Она повернулась к открывающейся двери, но заметив меня отвела взгляд в другую сторону."
        "Я хотел подойти к ней и извиниться, почему-то зная, что она меня простит. Либо давно поняла, что тогда был именно её промах."
        nd_il "Слушай, извини если обидел тогда, ничего не сказав."
        show us normal pioneer at center with dspr
        us "Ничего страшного. Я тебя простила."
        show us smile pioneer at center with dspr
        us "На дураков зла не держат."
        nd_il "Ну спасибо."


    else:
        "Как только я появился из-за двери, она меня заметила и широко улыбнулась."
        show us smile pioneer at center with dspr
        us "Пришёл, помощничек."
        nd_il "Как видишь. Не брошу же я тебя, раз обещание дал."
        nd_il "Не то что ты, хозяйка слова."
        us "А я не обещала, что не буду тебя больше разыгрывать."
        nd_il "Ладно, тут ты права."

    nd_il "И какой у нас план работы?"

    show us normal pioneer at center with dspr

    us "Сначала нужно протереть столы и накрыть на них."
    us "Только не все, а три ряда. Это для младших отрядов."
    nd_il "Понятно. Я тогда пойду, тряпки нам возьму."
    us "Давай, а я буду следить, чтобы ты не отлынивал."
    nd_il "Больно нужно."

    hide us with dspr

    show black with dissolve

    "Оглядев столовую и найдя тазик с надписью \"тряпки\" на нём, я с энтузиазмом направился к нему."
    window hide

    $ renpy.pause (1)

    scene bg caution_hv_nd with dissolve

    window show
    "Но мой энтузиазм пропал сразу же, как только я поближе взглянул на него."
    "Вода внутри выглядела не очень доброжелательно,{w} было ощущение будто оттуда сейчас вылезет какой-нибудь монстр и схватит своими щупальцами."
    "Добавим к этому тёмно-зеленую жидкость и что-то плавающее на поверхности, похожее на червяка,{w} даже если присмотревшись это окажется просто ниткой."
    "По-видимому этот тазик стоял здесь уже достаточно давно."
    window hide

    $ renpy.pause (1)
    
    window show
    th "Мне придётся лезть…{w} Туда?"
    th "Это, мягко говоря, не самая приятная инициатива."
    window hide

    show black with dissolve
    scene bg int_dining_hall_day with dissolve

    $ renpy.pause (1)

    window show
    "Я оглянул столовую,{w} и обнаружив одинокую вилку на дальнем столе, я решил применить её для своей задумки."
    window hide

    $ renpy.pause (1)

    show black with dissolve
    scene bg caution_hv_nd with dissolve

    window show
    "Вновь подойдя к заклятому тазику, и протянув туда вилку, я попытался поддеть из него какую-нибудь тряпку."
    "Так как вода была тёмной и за ней ничего не было видно, этот \"ход конём\" приходилось осуществлять вслепую."
    window hide

    $ renpy.pause (2, hard=True)

    scene bg int_dining_hall_day with flash
    $ renpy.pause (1)
    show us dontlike pioneer at right with dspr

    window show
    us "Горе луковое."

    hide us with dspr
    "Сказала Ульяна, и без опаски засунув руку к монстру, достала оттуда две синие тряпки."

    nd_il "Спасибо…"
    show us smile pioneer at center with dspr

    us "Глаза боятся - руки делают."
    us "На, держи одну тряпку."
    us "Идём протирать столы."
    hide us with dspr

    "Ульяна отдала мне тряпку, и найдя на одном из столов пустую тарелку из-под хлеба начала сметать туда все крошки."
    "Я последовал её примеру, взял ещё одну пустую тарелку, и начал сметать туда крошки с других столов."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause (4, hard=True)
    play ambience ambience_dining_hall_empty fadein 3
    hide black with dissolve2

    window show
    "Вскоре, как был убран первый ряд, мы перешли на второй."

    show us normal pioneer at center with dspr
    
    us "А чем ты там на пляже занимался?"
    nd_il "Работал.{w} Ставил сетку волейбольную, надувал лодки, мячики…"
    us "А ещё вы с Машей музыку слушали."
    th "Как она узнала? Небось подсматривала за мной, пока меня не было.{w} Страшно.{w} Может ревнует?{w} Да ну."
    nd_il "Подсматривала?"
    us "Рассказали."
    nd_il "Ты права. Она песню пела для меня одну…"
    
    show us grin pioneer at center with dspr
    
    us "Я тебе хоть сто песен могу спеть."

    hide us with dspr

    nd_il "А ну попробуй..."
    window hide

    $ renpy.pause (1)
    stop ambience fadeout 3
    $ volume (0.7, 'music')
    play music ndm_list['au_zachem'] fadein 2
    $ renpy.pause (3)
    show black with dissolve2
    $ renpy.pause (1)
    play ambience ambience_dining_hall_empty fadein 2
    stop music fadeout 1
    play sound nds_list['plate_stop']
    show us normal pioneer at center behind black
    hide black 
    with dspr
    
    $ volume (1.0, 'music')

    window show
    us "Но... Но я не знаю эту песню."
    us "Давай какую-нибудь другую."
    window hide

    $ renpy.pause (1)
    
    window show
    nd_il "А какую ты знаешь?"
    show us grin pioneer at center with dspr
    us "Разные знаю."
    us "Про короля-победителя у тебя есть?"
    nd_il "Подожди..."
    th "Что-то знакомое..."
    window hide

    $ renpy.pause (1)
    
    window show
    nd_il "Кажется, я тебя понял..."
    "Пролистав свой плейлист и введя в строку поиска песню с названием, сказанным Ульяной, я нашёл ту самую от Вадима Мулермана."
    window hide

    play music ndm_list['king_winner'] fadein 2
    $ renpy.pause (1)

    show us smile pioneer at center with dspr
        
    window show
    us "Во-от! Сейчас спою!"
    
    show us grin pioneer at center with dspr
    
    us "А давай вместе?"
    
    hide us with dspr
    
    "Я немного подумал, оглядел столовую,{w} и поняв,{w} что позориться не перед кем, решил согласиться."
    "Хотя в советском союзе подобное должно приветствоваться."
    "Это же не та страна, что будет на этом месте через 12 лет."
    nd_il "Давай."
    window hide

    $ renpy.pause (1)

    window show
    "Мы начали петь и сметать хлебные крошки со столов."
    window hide

    show black with dissolve2

    window show
    hgt "Железный шлем, деревянный костыль!"
    hgt "Король с войны возвращался домой!"
    hgt "Солдаты пели, глотая пыль!"
    hgt "И пел с ними вместе король хромой!.."
    window hide

    $ renpy.pause (1)

    window show
    "Мы продолжали петь эту поистине великую песнь, попутно убираясь в столовой."
    "И, признаться, мне даже нравилось. Нравилось быть в этом лагере. Я словно чувствовал здесь себя своим. Хоть я здесь всего и четвертый день, я привык ко всему вокруг."
    "На моём счету в этой столовой как минимум двенадцать посещений, а глобально: пять снов, две игры в футбол с Ульяной, знакомство со всеми из своего отряда... Столько всего произошло за такой короткий срок."
    "И я уже не так однозначно относился к моим ранним попыткам сбежать из этого лагеря. Оглядываясь назад понимаешь, что делал это зря."
    window hide

    $ renpy.pause (1)
    hide black with dissolve
    $ renpy.pause (1)

    window show
    "Так был протёрт весь второй ряд, а затем и остальные пять буквально за пять минут."
    "Теперь нужно было вымыть пол и накрыть на столы.{w} И мы решили начать с первого пункта в этом коротком списке…"

    show us normal pioneer at center with dspr

    us "Илья, давай наперегонки? Кто больше и быстрее всех вымоет пол – тот и выиграл."
    nd_il "Давай."
    show us smile pioneer at center with dspr
    us "Тогда я начну с этого угла, а ты с того."
    "Ульяна указала мне на противоположный угол столовой." 
    nd_il "Без проблем."

    hide us with dspr 
    show black with dissolve
    
    "Взяв из одного угла по швабре, и искупав их в ведрах, мы встали на разных углах столовой, приготовившись к погоне за чистотой кафельного пола."
    window hide

    $ renpy.pause (1)

    window show
    us "Начинаем!"
    window hide

    $ renpy.pause (1)

    window show
    "Пол в этой столовой нельзя было назвать совсем грязным, но и чистым тоже."
    "Со стороны младших отрядов он, конечно, был загрязнён сильнее, но не настолько весомо, насколько я себе это представлял сначала."
    "И по самой нашей с Ульяной игре на перегонки: поначалу выигрывал я, но потом Ульяна догнала меня и даже перегнала."
    "Швабра с тряпкой легко скользила по этому полу. Правда сложности добавляло то, что после тряпки приходится ступать по скользкому, тем самым снижая свою скорость для удержания равновесия."
    "Тем не менее, у Ульяны всё вышеперечисленное получалось лучше, нежели у меня."
    window hide

    $ renpy.pause (3, hard=True)
    stop music fadeout 5
    hide black with dissolve2

    window show
    "Вскоре пол в столовой сиял, как не сиял пол в Государственном Эрмитаже."
    "Да и времени оставалось у нас с запасом.{w} До обеда по меньшей мере было ещё десять минут."
    us "Всё. Теперь осталось накрыть на столы."
    nd_il "Ага…"
    "Голос Ульяны звучал уставшим. Но это и не удивительно."
    "Такая быстрая уборка неплохо расходует силы, особенно в моём случае."
    window hide

    $ renpy.pause (1)

    window show
    "Тем не менее, мы отказались от долгого отдыха и принялись за новую работу, заключающуюся в разносе подносов по всем трём рядам."
    "Работа однообразная, но зато быстрая, за счет чего не такая утомительная."
    window hide

    $ renpy.pause (2)

    window show
    "Управившись и с этой работой, у меня в голове появилась предусмотрительная,{w} с ноткой заботливости идея."
    nd_il "Давай ещё своему отряду накроем, чтобы они сами не ходили и не искали свободных мест."
    us "Давай, только в столовой нет разделения столов по отрядам."
    nd_il "Тогда выберем любые два."
    us "Ну хорошо."
    window hide

    show black with dissolve 

    $ renpy.pause (1)
    
    window show
    "Отсчитав семь порций на семерых человек, мы поскорее накрыли на два стола, выбранные у стены столовой, и принялись ждать сигнала из динамиков снаружи здания столовой."
    "По расчётам, он должен был прозвучать уже с минуты на минуту."
    window hide

    stop ambience fadeout 3
    $ renpy.pause (3, hard=True)

    play sound sfx_dinner_horn_processed

    $ renpy.pause (3, hard=True)
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with dissolve2
    $ renpy.pause (1)

    window show
    "Спустя пару минут столовая наполнилась огромным количеством людей."
    "Казалось, что их было больше, чем в остальные дни."
    "Но не это было главным."
    "А главным было то - что мы хорошо справились со своей работой и нашли козырные места для своего отряда."
    window hide

    $ renpy.pause (2)
    
    window show
    "Радость длилась не долго."
    "Не успел я порадоваться концу работы на этот обеденный час,{w} как к нашим столам замаячил какой-то пионер."
    "Я думал, что это Василий или Семён идёт своей легкой походкой, но присмотревшись понял, что с этим пионером я ещё не знаком."

    show rost serious pioneer at center with dspr

    pi "Пацан, это столы нашего отряда.{w} Вали отсюда."
    nd_il "Дружок, а где можно удостоверится в подлинности сие факта?"
    "Если-бы он вежливо попросил, то может быть, я ему и освободил \"его\" столы. Но в данный момент он напрашивался на что-то серьезное."
    "Не хотелось ему искать для своего отряда столы, и решил он наши, уже накрытые занять. Очень интересная у него логика."
    "И судя по ней, я должен был ему тут же отдать места в столовой.{w} Но ни я, не мой внутренний голос а-ля \"альтер-эго\" не хотели этого признавать."
    pi "Я тебе ещё раз повторяю: это наши столы. Найди своему отряду другие."
    th "Нормально так."
    nd_il "А не то что?"
    pi "А если не освободишь, встретимся за столовой."
    window hide
    
    play music ndm_list['nd_losing_you'] fadein 3
    
    $ renpy.pause (1)
    
    window show
    nd_il "Отчего же не здесь? Или кто-то испугался?"
    hide rost with dspr
    "Я встал из-за стола.{w} В миг стало ясно, что я был выше него сантиметров на пять или семь."
    show rost serious pioneer at center with dspr
    "А ещё, что назад сдавать некуда ни ему, ни мне."
    "Внутри моей головы будто проснулся вулкан. Я не знаю отчего, но мне хотелось за что-то отомстить ему."
    "Я понимал, что это не правильно, что этого не должно было случиться, что как и сказала Ульяна, здесь нет разделения столов на отряды.{w} Обманула?{w} Исключено!"
    "Я сжал руку в кулак. Чувство необъяснимого превосходства одолело меня."
    window hide

    $ renpy.pause (1)
    
    show nd_tolpa behind rost with dissolve
    
    window show
    "Вмиг нас окружили неизвестные мне пионеры из других отрядов. Некоторые старше, некоторые младше."
    "Подумав о том, что у этого \"авторитета\" могут быть своеобразные лагерные \"телохранители\" (в простонародии - шестёрки), меня что-то передёрнуло изнутри."
    window hide

    $ renpy.pause (1)
    
    window show
    "Мне казалось, что я уже где-то видел этого пионера. Что его внешность мне знакома, хотя это и было полностью исключено."
    window hide

    $ renpy.pause (1)

    show nd_rey normal pioneer at fright with dspr


    window show
    "Я было хотел перейти к дальнейшим действиям, но из толпы вышла девушка лет семнадцати и встала между нами."
    testpers3 "Не быкуйте друг на друга.{w} Давайте решим всё мирно."
    
    hide nd_rey with dspr

    th "Дипломатка значит."
    pi "Я согласен!"
    th "Струсил значит, клоун.{w} Это было просто."
    "Было забавно видеть, как рост прибавляет тебе уважения среди тебе подобных."
    window hide

    $ renpy.pause (1)
    
    window show
    nd_il "Окей."
    "Произнес я, но подумав о том, что в советском лагере вряд-ли знают значение этого слова, добавил:"
    nd_il "Хорошо{w}, и как...{nw=1}"
    pi "Несите стаканы!"
    nd_il "Что?"
    window hide

    hide rost serious pioneer with dspr
    $ renpy.pause (1)
    hide nd_tolpa with dissolve
    $ renpy.pause (1)

    window show
    "Как только пионер дал команду, два парня младше него побежали нести стаканы за один свободный стол."
    "Этот стол стал таковым сразу после инициации это пионера нашего конфликта."
    "Интересно, где сейчас были вожатые младших отрядов, или Ольга Дмитриевна?{w} Видела ли она это?{w} А может она наблюдает за нами через эту толпу?"
    "Навряд ли она спокойно бы смотрела на то, как два пионера устроили спарринг прямо в столовой."
    window hide

    $ renpy.pause (1)
    
    show nd_tolpa with dissolve
    $ renpy.pause (1)
    show rost serious pioneer at center with dspr

    window show
    "Мы сели друг напротив друга.{w} Нас вновь окружили пионеры."
    "Здесь в толпе я уже смог заметить Ульяну, Алису, Славю и Электроника."
    "Алиса подмигнула мне и жестом выразила респект, а Ульяна провела пальцем по горлу и указала движением своих голубых глаз на пионера."
    "Если и участвовать в подобном мероприятии, то точно для того, чтобы его видела эта парочка.{w} Правда думал я в этот момент немного о другом, слегка отдалённом от этой лагерной романтики."
    th "Пипец, ну и во что я вляпался?"
    window hide

    $ renpy.pause (1)

    window show
    th "А вот и стаканы…"
    th "Ладно уж.{w} Попробуем.{w} Прорвёмся."
    th "Может не всё так страшно, как кажется."
    window hide

    $ renpy.pause (1)

    window show
    testpers3 "У каждого на стороне по десять стаканов."
    testpers3 "Общее время всех выпитых стаканов показывает победителя."
    testpers3 "Проще говоря, играем на перегонки."
    testpers3 "До оглашения начала игры стаканы трогать запрещается."
    testpers3 "Начинём на счёт три."
    window hide

    play sound sfx_inhale
    $ renpy.pause (1)

    window show
    "Кинув взгляд прямо на лицо пионера, я глубоко вздохнул."
    window hide

    $ renpy.pause (1)

    window show
    testpers3 "Раз.."
    window hide

    play sound sfx_head_heartbeat
    
    window show
    "Я почувствовал, как стучит моё сердце от ненависти к нему в данный момент."
    testpers3 "Два…"
    "Я сжал руку, словно сжимая в ней тарзанку, на которой в эту минуту собирался раскачаться и прыгнуть."
    "В голову ударила решимость.{w} Мир вокруг расплылся, и в нём остались лишь стаканы с компотом, противник передо-мной и голос..."
    testpers3 "Три!"
    window hide

    show blink
    $ renpy.pause (1)

    hide rost serious pioneer
    hide nd_tolpa

    window show
    "В этот момент я резко схватил два стакана и залпом залил их в себя."
    "Не оставив времени на отдышку, я принялся за третий и четвёртый,{w} пока мой противник допивал только второй стакан."
    "Я быстро проглотил третий, и запив четвёртым, принялся за пятый и шестой."
    "Я не чувствовал ничего кроме адреналина в венах, и вкуса персикового компота."
    "Можно сказать, что я сам в этот момент будто состоял из компота."
    tolpa "Пей!{w} Пей!{w} Пей!.."
    "Кричала толпа, то ли мне, то ли моему противнику, постоянно повторяя."
    tolpa "Раз!{w} Два!{w} Три!"
    "Я выпил восьмую кружку, и взял девятую в руку."
    "Я опустошил её, но не полностью.{w} Часть компота невольно осталась в полости рта."
    "На десятой у меня начала кружиться голова, но..."
    window hide

    $ renpy.pause (1)

    window show
    "Проглотив компот из последней и предпоследней кружки, я поставил последний стакан на стол, и не задумываясь решил прокричать что-то эпичное своему противнику."
    nd_il "За твоё здоровье!"
    "Он, остановившийся на половине восьмой кружки, недоумевающе посмотрел на меня."
    "Фатальная победа над пионером и теперь уже точно \"наши столы\" - всё это не могло меня не радовать."

    scene bg int_dining_hall_people_day
    show prologue_dream

    hide blink
    show unblink

    stop music fadeout 5

    "Я встал из-за стола, толпа разошлась, пропустив меня ближе к пионерам из моего отряда."

    show us surp2 pioneer at left behind prologue_dream with dspr

    us "Илья, всё хорошо?"
    "Спросила Ульяна."
    "Я до конца не понял, имела ли она ввиду моё физическое или психическое состояние, поэтому я подобрал обобщённую фразу к тому, что только что произошло."
    nd_il "Я сделал это!"

    show us grin pioneer at left behind prologue_dream with dspr

    us "Ага. За пятнадцать секунд."
    "Улыбнувшись произнесла девушка."
    window hide

    show blink

    $ renpy.pause (1)

    window show
    "Я сел за одно из отвоёванных мест за столом."
    "Тут уже сидело большинство знакомых мне пионеров и пионерок."
    window hide

    hide us
    hide prologue_dream
    hide blink
    show unblink
    $ renpy.pause (1)
    
    window show
    "Возможно, они даже не подозревали, что я сражался в этой компотопролитной войне за них и их место быть здесь в эту секунду."
    "У меня в голове сейчас творилось что-то странное. В голову лезли странные мысли."
    "Но мною было принято решение отложить их на более позднее время.{w} Сейчас им было не место в моей голове."
    window hide

    $ renpy.pause (1)
    show sl surprise pioneer at center with dspr

    window show
    sl "Илья, я не думала, что ты можешь столько выпить."
    nd_il "Да я и сам не думал…"
    window hide

    show vst smile pioneer at left with dspr

    window show
    vst_lar "Илюх, всё нормально?{w} Ты как столько компота смог выпить?"
    nd_il "Я {w}{i}*ик*{/i}{w} не знаю."
    window hide

    hide sl
    hide vst smile pioneer
    with dspr

    $ renpy.pause (1)

    show rost normal pioneer at center with dspr

    window show
    th "О, а вот и мой противник пришёл посмотреть на меня."
    window hide

    $ renpy.pause (1)
    
    window show
    pi "Пацан, ты как?"
    nd_il "Пойдёт..."
    pi "Ладно, я пойду тогда, своему отряду место найду."
    pi "Тебя как зовут?"
    nd_il "Ильёй. А тебя?"
    show rost smile pioneer at center with dspr
    rost "Меня Ростиславом.{w} Можно просто Ростян."
    window hide

    hide rost with dspr
    $ renpy.pause (1)
    
    window show
    "Мы пожали друг другу руки, и Ростислав пошёл на поиски новых свободных мест."
    window hide

    $ renpy.pause (1)

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause (5, hard=True)
    play ambience ambience_dining_hall_empty
    scene bg int_dining_hall_day with dissolve2 
    $ renpy.pause (1, hard=True)

    window show
    "Спустя десять минут почти все пионеры из нашего отряда поели и пошли переодеваться к пляжным играм."
    "В столовой остались только я, Ульяна, и ещё какие-то пионеры в малом количестве."
    "Они не создавали большого шума, поэтому в столовой было относительно тихо."
    window hide

    $ renpy.pause (1)
    
    window show
    "Обедать после устроенного \"компотного испытания\" мне совсем не хотелось,{w} поэтому я просто сидел рядом с Ульяной, пока та ела порцию второго."
    window hide

    $ renpy.pause (2, hard=True)

    window show
    "Когда она доела и пошла относить тарелки за собой, я невольно бросил взгляд на двадцать стаканов за соседним столом."
    nd_il "Уля, давай уберём то, что мы устроили."

    show us grin pioneer at center with dspr
    
    us "Не мы, а ты."
    "Улыбнувшись сказала Ульяна и кинула тряпку ко мне на стол."
    nd_il "Ну и ладно."
    
    hide us with dspr
    
    "Смолвил я, и принялся вытирать крошки со столов и относить все двадцать кружек."
    window hide

    $ renpy.pause (1)

    window show
    th "Хорошо, что нас Ольга Дмитриевна не видела.{w} Так бы я такой нагоняй от неё получил бы..."
    window hide

    show black with dissolve
    $ renpy.pause (2)
    hide black with dissolve
    $ renpy.pause (1)

    window show
    nd_il "Ульяна!"

    show us normal pioneer at center with dspr

    us "Ась?"
    nd_il "Ты на какие оценки учишься?"
    us "На пятёрки. Учу много, книги читаю."
    us "Скоро у меня выпускной. Ну как скоро... Через год.{w} А мне ещё экзамены сдавать."
    us "Но думаю, что я всё сдам. Я ведь отличница."
    window hide

    $ renpy.pause (1)
    hide us with dspr

    window show
    "Насколько я знаю, в то время в школе учились максимум до десятого класса."
    "Забавно, что в России добавили ещё один год обучения, хотя по факту система образования никак не изменилась."
    nd_il "По твоему характеру этого не скажешь, если честно."
    nd_il "Хулиганка и одновременно отличница. Странненько, знаешь ли."
    us "Да ну тебя..."
    show us sad pioneer at center with dspr
    us "На всё есть причина."
    window hide


    play music ndm_list['tamsp14'] fadein 6
    $ renpy.pause (2, hard=True)

    show prologue_dream with dissolve2

    window show
    "Эмоция на лице у Ульяны превратилась во что-то неопределённое."
    "Мне стало как-то не по себе от этого.{w} Я понял, к чему она произнесла последнюю фразу."
    "Ребёнок, которого ограничивают в активностях и потребностях всё равно будет выплёскивать свою энергию. Пусть и не дома, а в других местах."
    "И сейчас я видел в Ульяне именно такого человека. Неправильное воспитание привело к этому."
    "Наверняка ей сложно даётся учёба, но по другому она не может, иначе за любые оценки ниже \"отлично\" можно пострадать физически."
    "Во всём виновато садистское воспитание детей доисторических времён и заблуждение,{w} что без насилия не вырастить хорошего человека."
    "От такого меня тошнит, но это жизнь.{w} В ней всегда будет место безответственным и пьющим родителям, раннему взрослению подростков и подобным вещам."
    "Я не знал, прав ли я насчёт Ульяны и её родителей в этом аспекте, но мысль об этом пугала и бросала в неприятную дрожь. К тому же её последняя фраза:{w} \"на всё есть причина\"."
    window hide

    $ renpy.pause (1)

    window show
    nd_il "Прости."

    show us normal pioneer at center with dspr
    
    us "Ничего страшного, проехали."
    "Сердце сжалось.{w} Я оказался прав."
    "Глядя в глаза этой девушке, я хотел задушить себя.{w} Я в очередной раз полез туда,{w} куда меня не просили. И сколько я помню, это постоянно выходило мне боком."
    window hide

    hide prologue_dream with dissolve
    hide us with dspr
    
    window show
    nd_il "Да, давай перейдём к какой-нибудь другой теме..."
    window hide

    $ renpy.pause (1)
    
    window show
    "Была идея выехать из этой ситуации на юмористической теме, как-то пошутить. Но никаких шуток в голову мне не лезло.{w} Кроме плоского юмора с тупых имиджбордов."
    nd_il "Вот к примеру, у тебя есть одноклассница с именем Даздрасмыгда?"
    vg "Других нормальных тем для разговора ты не знаешь..."
    
    show us normal pioneer at center with dspr
    
    us "Нет.{w} Что это за имя такое?"
    nd_il "Ну это как сокращение \"Да здравствует смещение города и деревни\"."
    nd_il "По моему без сокращения немного лучше."

    show us smile pioneer at center with dspr
    
    stop music fadeout 4

    us "А лучше всего вообще без этого имени. Ха-ха."
    window hide

    hide us with dspr

    $ renpy.pause (1)
    stop ambience fadeout 2
    show black with dissolve
    $ renpy.pause(3)
    play ambience ambience_dining_hall_empty fadein 2
    hide black with dissolve

    window show
    "Закончив с уборкой столовой, я вытер пот со лба и сел за один из свежеубранных столов."
    "Теперь помещение было практически пустым в плане людей, не считая вожатых с других отрядов."
    "К примеру, за самым дальним столом сидели Ольга Дмитриевна и Виола.{w} Похоже, они просто не могут отказаться от посиделок в столовой и от горячего сладкого чая."
    window hide

    $ renpy.pause(1)
    show us smile pioneer at center with dspr

    window show
    "Вскоре ко мне подошла Ульяна с двумя стаканами чая, и сев рядом, плавно подвинула один из них мне."
    "Она выглядела веселее чем обычно."
    "И вскоре мне предстало узнать причину её радости."

    show us grin pioneer at center with dspr
    us "А вот это нам за работу."

    "Ульяна вытащила из кармана шесть конфет."
    "Я не знал, откуда она их взяла,{w} но у меня были догадки."
    nd_il "Украла?"
    "Шёпотом спросил я."
    us "Нет, что ты!"
    us "Одолжила."
    window hide

    $ renpy.pause(1)    
    
    window show
    nd_il "А если серьёзно?"
    
    show us surp1 pioneer at center with dspr
    
    us "Какой ты скучный!"
    
    show us smile pioneer at center with dspr
    
    us "У поваров взяла."
    nd_il "Всё, понял."
    us "Как будто сам такой правильный."
    nd_il "Я не правильный, просто любопытный.{w} Как и ты, кстати."
    
    show us surp1 pioneer at center with dspr
    
    us "Ещё чего."
    nd_il "Того."

    hide us with dspr

    "Я взял одну из конфет и отправил себе в рот."
    "Мне не особо хотелось запивать её чаем, дабы лучше прочувствовать вкус советских конфет."
    "Но после просто невозможно отказаться от того, чтобы запить конфету."
    "Так обычно бывает, когда ешь шоколад, которого в этой конфете было довольно много."
    "Но может, так бывает только у меня."
    window hide

    $ renpy.pause(1)
    
    show us smile pioneer with dspr

    window show
    us "Ты ещё будешь?"
    nd_il "Не, я только одну."
    window hide

    hide us with dspr

    $ renpy.pause(2, hard=True)

    window show
    "Рядом с моим плакатом в столовой висели часы, которые показывали двадцать минут первого."
    "Я кинул взгляд сначала на эти часы, потом на наполовину пустой стакан с чаем и задумался."
    th "Что имела ввиду та вчерашняя девушка?{w} Какая опасность?{w} Что мне нужно делать?"
    th "Слишком много вопросов, на которые у меня нет ответов.{w} Может пойти поискать эти ответы? Наверняка ведь на вчерашнем пляже что-то есть, чего я не заметил.{w} Что-то, что даст мне хотя бы один ответ."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Краем глаза я увидел, как Ольга Дмитриевна отнесла свой стакан с чаем и направилась к нашему с Ульяной столу."
    
    show mt smile pioneer at left with dspr

    mt "Приветствую, работнички.{w} А чего вы тут сидите?{w} Вы пойдёте сегодня на пляж?"
    "Ольга Дмитриевна подкралась настолько незаметно, что Ульяна слегка вздрогнула."

    show us smile pioneer at right with dspr

    us "Конечно пойдём.{w} Да, Илья?"
    window hide

    hide us
    hide mt 
    with dspr
    
    $ renpy.pause(1, hard=True)
    
    window show
    "И тут я задумался.{w} Плавать мне было не в чем. У меня попросту нет плавок."
    th "А в чём мне плавать-то?{w} В обычных трусах что-ли?"
    nd_il "Мне ведь даже толком нечего надеть на эти ваши плавания."

    show mt grin pioneer at left with dspr

    mt "Не отчаивайся.{w} Пойдём ко мне. Найдём тебе плавки."
    nd_il "Спасибо Ольга Дмитриевна. Но...{nw=1}"

    show us surp1 pioneer at right with dspr

    us "Ура, Илья идёт купаться!"
    us "Я буду с девочками ждать тебя на пляже."
    nd_il "Подожди..."

    window hide

    hide us with dspr
    $ renpy.pause(1)
    hide mt with dspr
    $ renpy.pause(1)

    window show
    "Ульяна встала и побежала на выход из столовой.{w} Через окно можно было проводить её взглядом."
    "Я хотел сказать им обоим, что надевать чужие плавки это странно. Тем более из домика вожатой.{w} Но мне стал открыт только один путь, лежащий через плавание."
    "Нам с вожатой ничего не оставалось, кроме как пойти за плавками для купания к ней в домик."
    window hide

    $ renpy.pause(1)
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_dining_hall_near_day with dissolve
    play sound sfx_close_door_1

    $ renpy.pause(2, hard=True)
    show black with dissolve
    $ renpy.pause(1, hard=True)

    window show
    th "У Ольги Дмитриевны наверное там целый магазин одежды."
    th "А как ещё объяснить то, что вся одежда, которой у меня нет, есть у этой вожатой?"
    th "Но если серьезно, то это всё выглядит о-о-очень странно и неестественно.{w} Но удобно."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    th "Однако, если немного задуматься, то вся одежда для пионеров мужского пола находится у Семёна, а не у вожатой."
    th "Спросить у неё об этом я так и не решался.{w} А вдруг поймёт меня не так?{w} Я уже вел себя достаточно странно в этом лагере, а своими вопросами могу только усугубить это."
    th "Но если это окажутся плавки Семёна, мне придётся вежливо отказаться от этой услуги."
    window hide

    $ renpy.pause(1, hard=True)
    scene bg ext_house_of_mt_day with dissolve2
    $ renpy.pause(2, hard=True)

    play sound sfx_open_door_1
    show black with dissolve
    stop ambience fadeout 2
    $ renpy.pause(1)
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_mt_day with dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1)

    window show
    "Зайдя внутрь домика вожатой, я увидел уже привычную мне обстановку."
    window hide

    $ renpy.pause(1)
    play sound sfx_open_cupboard
    $ renpy.pause(1)
    
    window show
    "Но помимо всего перечисленного мною ранее по поводу этого домика, не могу не отметить его второго жителя - Семёна."
    "Он лежал на своей кровати и читал книгу, на обложке которой было написано: \"Унесённые ветром\". Довольно популярный роман писательницы Маргарет Митчелл."
    "Его вкус в книгах меня немного удивил.{w} Такой человек как он должен фантастику, экшен какой-нибудь читать.{w} Но кто я такой, чтобы судить его вкусы?"
    window hide

    $ renpy.pause(1)

    show pi2 grin pioneer at left with dspr

    window show
    me "Ну привет, победитель-алкоголик."
    nd_il "Привет, романтик-тунеядец."
    me "Кстати, не знал что ты ещё и музыкант."
    nd_il "Ну музыкантом меня назвать сложно."
    nd_il "Я скорее меломан."
    me "Кто?"
    nd_il "Конь в пальто."
    window hide

    hide pi2 grin pioneer with dspr

    $ renpy.pause(1)

    window show
    "Ольга Дмитриевна покопалась в своём шкафчике, и ничего не найдя принялась искать плавки в большом шкафу."

    show pi2 normal pioneer at left with dspr

    me "А что она ищет?"
    nd_il "Плавки.{w} Мне."
    me "Так ты идёшь на пляж?{w} Не ожидал."
    nd_il "Я за всю смену даже не поплавал ни разу.{w} А сегодня такой шанс появился."
    
    hide pi2 smile pioneer with dspr

    show mt normal pioneer at center with dspr

    mt "Илья, я нашла тебе плавки."
    "Произнесла вожатая и протянула мне предмет наших общих поисков."
    nd_il "А это не Семёна случайно?"
    me "Эм... Ольга Дмитриевна, я их даже ни разу не надел."
    mt "Семён, успокойся, это не твои плавки."
    mt "Это новые, со склада."
    me "А, тогда пусть берёт."
    nd_il "А они не ношенные?.."
    mt "Илья, что за вопросы?{w} Нет."
    "Сказала вожатая и отдала плавки мне в руки."
    nd_il "Тогда спасибо..."

    show pi2 grin pioneer at fleft with dspr 
    
    me "Ну, удачи тебе, водолаз."

    play sound sfx_open_door_1
    show black with dissolve
    
    nd_il "Благодарствую."
    "Произнес я, и вышел из домика на улицу."
    window hide

    $ renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1)
    show black with dissolve2
    $ renpy.pause(2, hard=True)
    scene bg ext_houses_day with dissolve2

    window show
    "У меня появилось время, чтобы разглядеть плавки, которые мне дала Ольга Дмитриевна."
    "Они выглядели как обычные чёрные труселя для плавания."
    th "Всё-таки, Ольга Дмитриевна искала эти плавки в своём шкафчике, значит вариант с одеждой Семёна отпадает."
    th "Интересно, а откуда у вожатой в шкафчике мужское бельё? Специально для какого-нибудь пионера их хранила? Навряд ли."
    th "И эта книга у Семёна... \"Унесённые ветром\". Хм... Где-то я такую уже видел."
    th "Точно, я видел Лену с этой книгой у здания клубов, когда я только приехал в этот лагерь."
    th "Его вчерашняя помощь Лене в медпункте, роман, который читала Лена.{w} Причинно-следственная связь стала ясна. Кто-то вчера очень хорошо погулял."
    vg "Пока ты сидел на поле под дождём и...{nw=1}"
    th "Молчать, пёс."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    "Проходя через весь лагерь, казалось, что он опустел."
    "Лишь изредка можно было увидеть какого-нибудь пионера."
    "Это свидетельствовало о том, что большая часть лагеря сейчас купается на пляже и ждёт организатора."
    window hide

    stop ambience fadeout 3
    $ renpy.pause(2, hard=True)

    play ambience ambience_lake_shore_day fadein 3
    play music music_list["so_good_to_be_careless"] fadein 3
    scene bg ext_beach_day with dissolve2

    window show
    "Придя на пляж, который уже был наполнен огромным количеством пионеров, я почувствовал какую-то необыкновенно приятную атмосферу для себя."
    "Не помню, когда я последний раз ездил на море или речку купаться.{w} Либо это было в моём уж слишком глубоком детстве, либо этого не происходило вообще никогда."
    th "Так, теперь надо найти своих."
    "Я оглянул пляж в поиске знакомых лиц. Вроде бы никого из моего отряда здесь не было."
    "Они определённо спрятались куда-нибудь в тенёк, или наоборот, решили позагорать.{w} Но всё же их нигде не было видно."
    "И только когда я присмотрелся, я увидел как мне помахала девушка издалека.{w} Это была Маша из моего отряда, а рядом с ней и Алиса с Ульяной."
    "Я помахал ей в ответ и поспешил к ним."
    window hide

    $ renpy.pause(2)
    show cg us_dv_mi_beach_d4 with dissolve

    window show
    nd_il "Привет всем!"
    mi "Привет!"
    dv "Привет, водохлёб."
    us "Долго ты. Мы думали, что ты уже потерялся."
    us "Арбуз будешь?"
    nd_il "Не откажусь…"
    "Я присел рядом с девушками на большое полосатое полотенце."
    "Ульяна улыбнувшись протянула мне с блюдца дольку арбуза, которую я не мог не принять."
    window hide

    $ renpy.pause(1)
    
    window show
    dv "Не уссышься?"
    nd_il "Не..."
    window hide

    $ renpy.pause(1)
    
    window show
    mi "Илья, а ты будешь принимать участие в конкурсах? Пляжный волейбол там, плавание. Просто я вижу, ты плавки взял."
    dv "О, Илья у нас, оказывается, и плавать будет."
    nd_il "Вот не знаю. Пока не решил..."
    "Я легонько надкусил дольку арбуза.{w} Он показался мне достаточно спелым и сладким."
    window hide

    scene black 
    hide us_dv_mi_beach_d4
    with dissolve

    $ set_mode_nvl()
    
    window show
    "Последний раз я покупал арбуз летом, а он оказался не сладким.{w} Я тогда ещё подумал: \"Ну не пропадать же добру\".{w} Как уже стало понятно, ничем хорошим для меня эта инициатива не закончилась."
    "Интересно, как там Йося поживает?{w} Скучает, наверное.{w} Со школы с ним дружим и, сколько себя помню, ни разу не ссорились."
    "Хотя зачем мне о прошлой жизни-то думать?{w} Я - в отпуске."
    window hide

    $ set_mode_adv()

    $ renpy.pause(1)

    window show
    "После своих раздумий я лёг на песок и посмотрел на небо."
    window hide

    scene bg clouds_day with dissolve2

    window show
    "На голубом полотне неба плавно и почти незаметно плыли облака."
    "В этот день в лагере было довольно жарко.{w} И в этот жаркий день было бы приятно искупаться."
    "Хорошо, что вожатая решила устроить пляжное мероприятие."
    window hide

    $ renpy.pause(1)
    
    window show
    dv "Илья, ты будешь в волейбол играть?"
    "Отвлекла меня от раздумий Алиса."
    nd_il "Не знаю. Двое против двух будем играть?"
    dv "Не-а, три на три.{w} Вожатая и Лена тоже будут участвовать."
    window hide

    show black with dissolve
    show cg us_dv_mi_beach_d4 with dissolve

    window show
    nd_il "А что после волейбола?"
    "Спросил я у девушек."
    us "Мы с Алисой купаться пойдём...{nw=1}"
    "Сказала Ульяна, и хотела что-то добавить, но её перебила Алиса."
    dv "Будешь с нами купаться?{w} Только учти, на этот раз ты так просто не отделаешься."
    nd_il "Вот это мы и посмотрим."
    window hide

    stop music fadeout 3
    show black with dissolve

    window show
    "Тем временем на пляж пришёл главный организатор — Ольга Дмитриевна с листком бумаги в руке,{w} на котором, видимо, будут записываться то-ли результаты конкурсов, то-ли росписи пионеров,{w} то-ли ещё что-нибудь…"
    window hide

    scene bg ext_beach_day with dissolve

    window show
    "Вожатая подошла к микрофону рядом с колонками..."
    window hide

    $ renpy.pause(1)

    play music music_list["went_fishing_caught_a_girl"] fadein 5

    window show
    mt "Привет, лагерь!"
    "Все пионеры сразу же прокричали что-то вразнобой.{w} Пока кто-то кричал \"здравствуйте\", другие кричали \"привет\"."
    mt "Сегодня мы будем играть в игры на пляже и в воде." 
    mt "Вы можете участвовать, а можете просто купаться.{w} Для этого пляж был разделен на две части буйками."
    window hide

    $ renpy.pause(1)

    window show
    "Все пионеры (в том числе и я) после слов нашей вожатой сразу же обратили внимание на буйки в воде и на самом пляже."
    mt "Весёлого времяпрепровождения на пляже лагеря \"Совёнок\"!"
    "Сказала Ольга Дмитриевна под не напрягающую лагерную музыку..."
    window hide

    $ renpy.pause(1)

    show us grin swim at right with dspr

    show dv normal swim at center
    show mi normal swim at left 
    with dspr

    window show
    us "Ну что, пошли в волейбол?"
    all "Пошли."
    window hide

    hide us
    hide dv
    hide mi
    with dspr

    window show
    "Согласившись с Ульяной, мы неспеша встали с песка и направились к волейбольной сетке."
    window hide

    show black with dissolve
    $ renpy.pause(2)
    hide black with dissolve
    $ renpy.pause(1)

    window show
    "Там стояли Ольга Дмитриевна и Лена."
    "Видимо, они ждали именно нас."
    window hide

    $ renpy.pause(1)
    
    show mt normal panama pioneer far at right
    show un smile swim far at left
    with dspr
    
    window show
    "В отличие от Лены, на Ольге Дмитриевне была обычная лагерная одежда, а не купальник.{w} Оно и понятно, у вожатых нет времени на всякие купания."
    "А на волейбол есть."
    window hide

    hide mt
    hide un
    with dissolve
    $ renpy.pause(1)

    show mt normal panama pioneer at cright
    show un smile swim at fright
    with dspr

    show us smile swim at left with dspr

    window show
    us "Мы в волейбол играть пришли."
    "Весело произнесла Ульяна."

    show mt smile panama pioneer at cright with dspr
    
    mt "А мы вас ждём."

    hide us with dspr
    show us smile swim at cleft with dspr
    show mi smile swim at fleft with dspr
    
    mi "Давайте разделимся на команды, чтобы честно было! Три в одну, три в другую!"
    mt "Прекрасная идея, Мику. Кто в какую команду идёт?"

    show us grin swim at cleft with dspr

    us "Мы с Алисой вместе будем."

    hide us
    with dspr

    "Сказала Ульяна, и они вместе встали на правую сторону от сетки."

    hide mi
    hide un
    with dspr

    "Маша и Лена встали на другую сторону."
    window hide

    stop music fadeout 6

    $ renpy.pause(1)

    hide mt with dspr
    show mt smile panama pioneer at center with dspr

    window show
    mt "Илья, выбирай, куда пойдёшь."
    "Сказала Ольга Дмитриевна и посмотрела на меня, ожидая моего решения."
    "По её взгляду, ей было не принципиально, за какую команду она будет играть."
    window hide

    $ renpy.pause(1)
    hide mt with dspr

    window show
    "Справа от сетки мне рукой помахала Ульяна."
    th "Ну уж ладно, поиграю на стороне рыжих."
    window hide

    $ renpy.pause(1)

    window show
    "Я прошёл по песку на сторону к Ульяне и Алисе."
    "Ольга Дмитриевна сразу зашла за команду Маши и Лены."
    "Ольга Дмитриевна отдала мне мячик."
    us "Давай Илья, сделаем их."
    "Произнесла мне шёпотом Ульяна.{w} Признаться, это неплохо подбодрило и придало решимости."
    nd_il "Сделаем."
    "Улыбнувшись ответил я Ульяне так же шёпотом."
    window hide

    play music ndm_list['016mt'] fadein 4
    
    $ renpy.pause(1)

    window show
    nd_il "Начинаем."
    "Огласил я, и подбросив мячик вверх отбил его в воздухе на сторону противника."
    window hide

    show cg beach_play with dissolve

    $ renpy.pause(1)

    window show
    "Лена отбила мячик, и он уже летел на нашу сторону, но Ульяна вовремя отбила его обратно к противнику."
    "В этот раз наш мяч отбила Ольга Дмитриевна, и Алиса, отбив подачу вожатой закинула мяч на сторону противника.{w} Счёт стал ноль-один в нашу пользу."
    "Следующий раз выбивала Ольга Дмитриевна.{w} Она подбросила мяч в воздух и совершила по нему удар ладонью."
    "Когда мяч залетел на нашу сторону, я отправил мяч обратно, но Лена отбила его." 
    "Мяч почти приземлился на песок, но Ульяна подбросила его вверх, а удар за неё продолжил я..."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(2)

    window show
    "Таким образом мы отыграли четыре-шесть в нашу пользу.{w} Под палящим солнцем играть, как оказалось, не такая уж и плохая идея."
    "А ещё оказалось, Ольга Дмитриевна не плохо играет в волейбол."
    "В отличие от меня.{w} Хотя опыта у меня в этом виде спорта вообще не было."
    window hide

    jump original_road_us
    

label original_road_us:

    play ambience ambience_lake_shore_day fadein 4
    scene bg ext_beach_day with dissolve2

    $ renpy.pause(1)

    show mt smile pioneer at center with dspr

    window show
    mt "Хорошо поиграли."
    "Дала свой комментарий Ольга Дмитриевна."

    show mt smile pioneer at center with dspr

    mt "Будете ещё во что-нибудь играть?"

    show dv normal swim at right with dspr

    dv "Не, я пас."

    hide dv with dspr

    "Мне тоже не особо хотелось играть.{w} Я больше хотел искупаться в воде, потому что как я уже говорил, я не отдыхал на водоёмах уже о-очень давно."
    window hide

    $ renpy.pause(1)
    
    window show
    nd_il "Я тоже откажусь.{w} Хочется искупаться."
    mt "Ладно, как хотите."

    stop music fadeout 3
    
    hide mt with dspr
    
    "Сказала вожатая и, записав что-то на листочке, куда-то ушла."
    window hide

    $ renpy.pause(1)
    play music music_list["went_fishing_caught_a_girl"] fadein 6
    window show
    "Ульяна же вместе со своей подругой, по-видимому, пошли барахтаться в воде."
    "Я уже было хотел присоединиться к ним, но вспомнил, что перед этим мне нужно переодеться в плавки."
    window hide

    $ renpy.pause(1)

    window show
    "Взяв их рядом с тем местом, где мы с девушками ели арбуз и где я вёл свои размышления по поводу своей жизни, я оглянулся в поисках раздевалки или чего-то подобного."
    "Благо такая на пляже была, и не одна. Одним из этих маленьких сооружений для переодевания я и решил воспользоваться."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    play sound nds_list['applysuit']
    $ renpy.pause(1)

    $ renpy.pause(1)
    scene bg ext_beach_day with dissolve

    $ renpy.pause(1)

    window show
    "Переодевшись в новые плавки,{w} по крайней мере мне хотелось в это верить,{w} я поспешил присоединиться к пионеркам."
    window hide

    show black with dissolve
    $ renpy.pause(1)
    show cg ussrr_dv_p_d4 with dissolve2

    $ renpy.pause(1)

    window show
    us "Смотри, Илья идёт!"
    "Прокричала Ульяна своей подруге."
    dv "И правда. Решил сам в плен сдаться?"
    nd_il "Не-а.{w} Я пришел взять реванш."
    play sound sfx_water_splash
    "Алиса тут-же обрызгала меня водой.{w} Я же в свою очередь не упустил шанса обрызгать её в ответ."
    play sound sfx_water_splash
    us "Ну всё, сам напросился!"
    us "Лови его! Сейчас он точно от нас не уйдёт!"
    dv "Давай! Держи!"
    window hide

    scene black with dissolve

    window show
    play sound sfx_water_splash
    "Объединив свои силы они начали брызгаться в меня вдвое больше, и спастись я мог только ныряя в воду, что тоже не особо мне и помогало."
    dv "Он сейчас под воду скроется, лови!"
    us "Ловлю..."
    window hide

    stop ambience fadeout 2
    stop music fadeout 2
    play sound sfx_shoulder_dive_water
    scene black with flash
    $ renpy.pause(2)

    play music music_list["drown"] fadein 1
    scene bg nd_4_underwater with dissolve2
    $ renpy.pause(3, hard=True)
    
    window show
    "Спрятавшись под воду я задержал дыхание. Девочки точно не могли меня найти в гуще вспененной воды."
    "Я почувствовал, как девушки перестали брызгаться, вода стихла."
    "Видимо они поняли, что надо дать вспененной воде уйти, и тогда они смогут найти меня."
    "Хотя признаться, здесь было достаточно глубоко, так что было не так легко меня увидеть через воду с их стороны."
    "Но тем не менее, я все равно умел быстро плавать под водой, и легко ускользнул бы от них, если бы они меня нашли.{w} И я даже не помню, откуда у меня это умение. Возможно, в детстве я часто плавал..."
    "И опять я встречаюсь лишь с догадками о своей прошлой жизни."
    "А ведь серьёзно, почему? Почему я ничего не помню? Я не помню из своего детства ничего кроме Даши. Она была для меня дороже родителей. Да и до сих пор..."
    "Что-то должно было вернуть меня в реальный мир до того, как из глаз опять пойдут слёзы. Хорошо, что под водой не будет этого видно. Кстати, в ней я находился уже достаточно долго."
    "В один момент сердце одолело странное чувство тревоги. Может быть им надоело и они давно ушли? А может я сам того не понимая заплыл слишком далеко?"
    "Это имело смысл, поэтому я начал поспешно всплывать на поверхность."
    window hide

    stop sound_loop fadeout 5
    show black with dissolve2
    $ renpy.pause(1, hard=True)
    play ambience ambience_lake_shore_day fadein 5
    play sound sfx_water_emerge
    scene bg ussrr_m_p4 with dissolve

    window show
    "Вынырнув из воды, вместо двух пионерок я увидел только лишь переполошенную Алису с бегающими от волнения глазами.{w} И даже когда я появился у неё в поле зрения ничего не изменилось.{w} Я смутился."
    nd_il "Что случилось?"
    nd_il "И где Ульяна?"
    
    show dv scared swim at center with dspr
    
    dv "Она прыгнула в воду за тобой, и до сих пор не появилась."
    nd_il "Да ладно тебе!{w} Где она нырнула?"
    
    hide dv with dspr
    
    dv "Тут."
    "Алиса показала пальцем на место ныряния Ульяны в воду."
    "После указания Алисы я набрал как можно больше воздуха в лёгкие и без раздумий отправился на погружение..."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    play sound nds_list['watersplash']
    $ renpy.pause(2, hard=True)
    scene bg nd_4_underwater with dissolve2
    $ renpy.pause(3, hard=True)

    window show
    "Я нырнул на максимально возможную для себя глубину и начал водить руками, пытаясь найти руку Ульяны и...{w} Удача!"
    th "Как же ты так глубоко, родная...{w} Ничего, я вытащу тебя."
    window hide

    $ renpy.pause(2, hard=True)
    stop sound_loop fadeout 3
    show black with dissolve2
    $ renpy.pause(2, hard=True)
    play ambience ambience_lake_shore_day
    scene bg ussrr_m_p4 with flash
    $ renpy.pause(2, hard=True)
    show black with dissolve
    scene bg ext_beach_day with dissolve
    $ renpy.pause(2, hard=True)

    window show
    "Вынырнув вместе с девочкой я побежал к берегу, и положив её на полотенце посмотрел на неё."
    vg "Илья, не тупи. Давай откачивай."
    th "Так, чему там нас в школе учили?{w} Нужно воду из лёгких откачать."
    "Я принялся поступательно надавливать девушке на грудь, дабы она смогла откашляться, когда придёт в себя..."
    "Ко мне подбежала Алиса, Ольга Дмитриевна, Славя, Маша, Лена и другие пионеры."
    window hide

    $ renpy.pause(1, hard=True)
    
    window show
    th "Не помогает.{w} Не помогает!{w} НЕ ПОМОГАЕТ!"
    vg "Делай искусственное дыхание, идиот."
    th "Подожди.{w} Если воды в легких у неё уже нет, нужно просто привести её в сознание..."
    th "Но как? Не буду же я её бить?"
    th "Черт-черт-черт."
    window hide

    $ renpy.pause(2, hard=True)
    
    stop music fadeout 6

    window show
    "Внезапно Ульяна открыла глаза, поднялась с песка и откашлялась"
    "Большинство пионеров мягко говоря пребывали в лёгком шоке.{w} Как и я."
    "Я смог спокойно выдохнуть, ведь мне показалось, что этот случай станет для меня последним."
    window hide

    play music ndm_list["notdreamovsky_saspens_1"] fadein 6

    $ renpy.pause(2, hard=True)

    show us sad swim at center with dspr

    window show
    nd_il "Всё хорошо?"
    us "Ты меня спас?"
    nd_il "Третий раз за смену."
    nd_il "Рассказывай, что случилось?"
    
    show us cry swim at center with dspr

    us "Я прыгнула за тобой…{w} А потом я хотела…{w} меня кто-то…{w} тянул вниз…{w} Я не могла…"
    us "Я думала это ты, но..."
    "Ульяна заплакала..."
    "В груди всё сжалось. Я смотрел на этот рыжий комок, который ещё недавно был полон радости, а сейчас убивался в слезах."
    "Ему было очень страшно. Я не мог всё так оставить.{w} Я чувствовал свою вину.{w} Я должен был её успокоить."
    nd_il "Всё хорошо. Ты в безопасности."
    
    hide us with dspr

    "Я обнял Ульяну.{w} Она прижалась ко мне.{w} Вся дрожала.{w} Я почувствовал скатывающуюся капельку по своему плечу и её теплое дыхание."
    "И с каждым её всхлипыванием она прижимала меня всё ближе."
    th "Кто мог её тянуть ко дну?"
    th "Может это та самая опасность, о которой предупреждала Даша?"
    th "А может это и есть предупреждение..."
    th "Плевать.{w} Главное, что Ульяна жива…"
    window hide

    show black with dissolve

    window show
    mt "Не ходите в воду без разрешения."
    "Послышался сзади поучительный голос Ольги Дмитриевны к остальным пионерам."
    mt "Если не умеете плавать также воздержитесь от купания…"
    th "Уверен, что Ульяна умеет плавать. Иначе бы она не нырнула за мной."
    window hide
    
    stop ambience fadeout 3

    $ renpy.pause(4, hard=True)

    play ambience ambience_lake_shore_day fadein 3

    scene bg ext_beach_day with dissolve

    $ renpy.pause(1, hard=True)

    window show
    "Пионеры начали расходиться."
    "Я всё также сидел на песке в обнимку с Ульяной, которая постепенно успокаивалась."
    "Когда она отпустила меня из объятий и вытерла слёзки, я опустил свой взгляд вниз."
    th "Прости что впутываю тебя в это, Ульяна."
    th "Уверен, что всё это из-за меня. И если бы я ушел вчера вечером после танцев ничего бы этого не случилось."
    "Ольга Дмитриевна похлопала меня по плечу, прервав мои раздумья."
    "Я медленно повернулся к ней."
    
    show mt normal pioneer at center with dspr

    mt "Илья, подойди ко мне, когда успокоишь Ульяну и..{w} управишься с делами..."

    hide mt with dspr

    "Указательным тоном произнесла вожатая, и отвернувшись, направилась в сторону другого пляжа следить за пионерами."
    "..."
    "Алиса подоспела к своей подруге и тоже обняла её."
    "По-видимому, меня ждал с ней очень долгий разговор.{w} Потому что я чувствовал себя ответственным за этих двух девушек. Всё-таки я старше их обеих пусть и не физически."
    "И Ольга Дмитриевна наверняка думала обо мне подобным образом."
    "С этой мыслью я кинул взгляд на Ульяну и на Алису, которая пыталась её успокоить."

    show us sad swim at left
    show dv normal swim at right
    with dspr

    nd_il "Алис. Ты следи что ли за своей подругой…"
    dv "Спасибо, что спас её."
    us "И ещё прости меня за то, что донимаем тебя иногда."
    "Сквозь слёзы проговаривала Ульяна.{w} Орган внутри моей груди сжался.{w} Передо мной извинялись за то, что в каком-то смысле и держит меня в этом лагере - внимание этих девушек к какому-то новенькому."
    nd_il "Я не сильно обижаюсь на это. Без вас в лагере было бы скучно."

    show us normal swim at left
    show dv smile swim at right
    with dspr

    "Ульяна улыбнулась мне сквозь слёзы. В её волшебно-голубых глазах читалось не менее волшебное \"спасибо\"."
    "Я бы и дальше продолжил смотреть в них, но от боязни, что это покажется пионерке неестественным, отвел взгляд в сторону."
    nd_il "Ну что-ж.{w} Я пойду, наверное."
    "Сказал я, взяв за пазуху свою пионерскую форму."
    dv "Давай.{w} Ещё увидимся."
    "Подмигнув, сказала Алиса."
    us "Удачи."

    hide dv
    hide us
    with dspr

    "Я развернулся и пошёл к раздевалке, чтобы переодеться в пионерскую форму."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve2

    window show
    "Меня терзали смешанные чувства.{w} Словно это я был виноват во всём произошедшем."
    "Это я остался в лагере, поддался каким-то мыслям внутри своей головы."
    "А ведь в глазах этих девушек я - герой. Но это не так. И никак им этого не скажешь, не донесёшь до них истины, что я корень всего, что с ними сейчас происходит..."
    window hide

    $ renpy.pause(1, hard=True)

    play sound nds_list['applysuit'] 
    
    stop music fadeout 5

    $ renpy.pause(1, hard=True)

    hide black with dissolve

    window show
    "Переодевшись в пионерскую форму я выжал воду из плавок и, положив их высыхать, отправился к вожатой."
    "Она стояла рядом с осмотрительным пунктом вместе с пионеркой Славей."
    "Они что-то обсуждали, но как только увидели меня, идущего к ним навстречу, повесили молчание в своем диалоге."
    window hide
    

    $ renpy.pause(1)

    show mt normal panama pioneer at right
    show sl normal pioneer at left 
    with dspr

    window show
    nd_il "Вы говорили, чтобы я к вам подошёл после всех своих дел."
    mt "Да. Пойдём ко мне в домик."
    "Сказала Ольга Дмитриевна, а потом повернулась к Славе."
    mt "Следи, чтобы никто не утонул и не пострадал, я сейчас вернусь."
    show sl smile pioneer at left with dspr
    "Славя кивнула Ольге Дмитриевне и улыбнулась мне, скрывая что-то в своей улыбке."
    "Я отвел взгляд от её лица в левый нижний угол."
    window hide

    hide sl
    hide mt
    with dspr

    $ renpy.pause(1, hard=True)
    stop ambience fadeout 3
    show black with dissolve
    $ renpy.pause(1, hard=True)

    window show
    "Не прошло десяти секунд, как мы с вожатой шли в направлении её домика."
    window hide

    $ renpy.pause(2, hard=True)

    play ambience ambience_camp_center_day fadein 3
    scene bg ext_houses_day with dissolve2

    $ renpy.pause(1, hard=True)

    show mt normal panama pioneer at left with dspr

    window show
    "Мы шли тихо, пока Ольга Дмитриевна не нарушила молчание своим следующим вопросом."
    mt "Объясни, что там у вас случилось с Ульяной."
    nd_il "Ну… Мы играли с девочками в воде, брызгались друг на друга. Потом я нырнул, чтобы спрятаться."
    nd_il "Попрятался в воде, выныриваю и обнаруживаю Алису с обеспокоенным видом."
    nd_il "Я у неё спрашиваю мол: \"что случилось?\", а она в ответ мне, что Ульяна нырнула за мной и не вынырнула."
    nd_il "Ну я и бросился в воду.{w} Нащупал её руку, потащил вверх..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Ольга Дмитриевна слушала мой рассказ с заинтересованной эмоцией на лице, постоянно утвердительно кивая."
    "И когда я закончил, она ещё несколько секунд обрабатывала у себя в голове мною сказанное."
    "Но мы все также продолжали идти до её домика, ни на секунду не останавливаясь."
    "Пока она думала над мною сказанным мне следовало понять, что мне делать дальше, что со мной будет, чего мне стоит бояться дальше."
    "Если Ульяна не просто тонула, а её действительно кто-то тянул ко дну."
    mt "Понятно. Так она ещё говорила, что её кто-то вниз тянул. Я сначала думала, что это ты."
    nd_il "Да что вы.{w} Я не знаю, кто её тянул. Может пионер какой-то."
    nd_il "Ульяна над ним пошутила, и он может тоже решил так \"пошутить\"..."
    mt "У нас в лагере на Ульяну обычно никто долго зла не держит. Интересно у вас получается."
    mt "Да и ты правда думал, что Ульяна не нырнёт за тобой, если увидит что ты прячешься от неё в воде?"
    "Я незаметно вдохнул много воздуха в свою грудь и также незаметно выдохнул."
    nd_il "Своей вины я тоже не скрываю.{w} Виноват."
    window hide
    
    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(3, hard=True)
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_mt_day with dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1, hard=True)

    window show
    "Мы дошли до домика вожатой и вошли внутрь."
    "Семёна в её домике не было.{w} Да и он был бы здесь лишним, если бы меня отчитывали при нём.{w} А так хоть об этом будем знать только мы да эта вожатая..."
    "Ольга Дмитриевна залезла в свой шкафчик, и достала оттуда что-то блестящее."
    window hide

    $ renpy.pause(1, hard=True)
    
    show mt smile pioneer at center with dspr

    window show
    "Она показала мне бронзовый значок с надписью \"Спасатель лагеря Совёнок\" и закрепила его мне на груди."
    "По-видимому, это был специальный значок, коим награждались пионеры определенного лагеря."
    "И я не знал, гордиться мне этим, или всё таки отдать этот значок обратно вожатой и сказать, что никакой я не спасатель, а жалкий трус и заложник собственных желаний..."
    nd_il "Спасибо Оль Дмитриевна."
    "Проговорил я с необъяснимой тяжестью."
    "Если бы я сказал что-то другое, скорее всего, было бы только хуже для меня."
    mt "Это ещё не всё.{w} У меня к тебе есть предложение."
    
    hide mt with dspr

    "Сказала вожатая и села на свою кровать."
    th "Неужели вот он - тот разговор, которого я боялся?"
    window hide
    
    $ renpy.pause(1, hard=True)

    window show
    "Я сел перед ней на кровать Семёна."
    mt "Тебе чай налить?"
    nd_il "Нет, спасибо большое."
    nd_il "Так о каком предложении идет речь?"
    
    show mt normal pioneer at center with dspr
    
    mt "Ты не хотел бы стать настоящим спасателем на пляже нашего лагеря?"
    "На этом моменте я сглотнул.{w} Как такому безответственному, после того что я сделал, могли предложить такое?"

    show mt smile pioneer at center with dspr

    mt "Ты бы мог выручать пионеров."
    mt "Не волнуйся, перерывы тоже будут."
    window hide

    hide mt with dspr
    
    $ renpy.pause(1, hard=True)

    window show
    th "А если я не услежу и кто-нибудь, не дай бог, утонет?"
    nd_il "Ольга Дмитриевна. Боюсь, это слишком ответственная работа для меня…"
    
    show mt normal pioneer at center with dspr

    mt "Илья, ты показал себя очень хорошо в спасении людей. Ты своего товарища три раза спасал."
    th "И, уверен, ещё не раз придётся это сделать."
    nd_il "Можно я ещё подумаю?"
    "Обычно я отвечал так только тогда, когда не хотел напрямую давать отказ. Сейчас мне было сложно просто так отказать вожатой."
    "Я сам не заметил, как начал действительно её уважать, как реального человека из Советского Союза."
    mt "Конечно можешь."
    window hide
    
    $ renpy.pause(2, hard=True)

    window show
    "И на этом моменте в домике наступила короткая тишина."
    "Которую Ольга Дмитриевна решила в очередной раз нарушить."
    
    show mt normal pioneer at center with dspr
    
    mt "А ты не видел сегодня Шурика?"
    th "Думаю, вожатой-то можно сказать."
    nd_il "Я его видел утром. Он сказал, что идёт в старый лагерь за деталями для изобретения какого-то…"
    show mt shocked pioneer at center with dspr
    mt "Как в старый лагерь?! Он ведь ещё не вернулся!.."
    hide mt with dspr

    "Ольга Дмитриевна не по-детски всполошилась."
    "Её можно было понять. Она ведь волнуется за пионеров, за которых отвечает."
    "Но до этого момента я думал, что кибернетики как-то согласовали это с ней. И похоже, я заблуждался."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Я думаю, с этим кибернетиком всё будет нормально.{w} Может деталей много, и он их в клуб перетаскивает весь день, и никому не говорит."
    show mt normal pioneer at center with dspr
    mt "И то верно. Надо спросить об этом у Электроника."
    "Ольга Дмитриевна встала со своей кровати.{w} Я также последовал её примеру и встал с кровати Семёна."
    mt "Ладно, можешь пойти, отдохнуть, а мне нужно ещё за порядком на пляже следить."
    window hide

    hide mt with dspr
    $ renpy.pause(1, hard=True)
    
    window show
    "Сказала Ольга Дмитриевна, и вышла из домика, оставив меня здесь одного."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Может мне необходим отдых?"
    th "Устал что-то.{w} Да и голова побаливает от случившегося за весь день."
    th "Обычно, хороший сон решает такие проблемы."
    th "Но хороших снов у меня давно не было,{w} поэтому не мне об этом говорить."
    window hide

    $ renpy.pause(1, hard=True)
    
    show black with dissolve
    $ renpy.pause(1)
    play ambience ambience_camp_center_day
    scene bg ext_house_of_mt_day with dissolve
    play sound sfx_close_door_1

    window show
    "Подумал я, и выйдя из домика вожатой, отправился к своему домику, находящемуся почти на другом конце лагеря."
    window hide
    
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Со стороны пляжа доносились голоса ребят.{w} Разобрать их я не мог, так как и вправду был очень уставшим."
    "Мозг уже не позволял обрабатывать информацию, которая сочится вокруг изо всех щелей."
    "Похоже мне действительно напекло голову за всё время, проведённое тут."
    "Возможно даже, что меня хватил солнечный удар."
    window hide

    $ renpy.pause(2, hard=True)
    stop ambience fadeout 3
    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_day fadein 3
    scene bg int_house_of_gg_day with dissolve

    $ renpy.pause(1)
    
    play sound sfx_close_door_1
    
    window show
    "Завалившись в свой домик, я положил телефон под подушку, предварительно поставив беззвучный режим."
    "Упав на кровать, я полностью растворился в,{w} как мне показалось в эту секунду,{w} пуховом матрасе."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "М-да, вот так и искупались. А если бы я не успел спасти Ульяну?.."
    th "Интересно, зачем она узнала насчёт Маши и меня на пляже? Может, она меня действительно ревнует к ней?"
    th "Это странно, я никогда даже не думал, что она может ревновать.{w} Особенно меня, и тем более в подобных вещах."
    th "Как я и предполагал, она ещё во многом сможет удивить меня в сложности своего характера, как раньше могла удивлять его простотой..."
    window hide

    $ renpy.pause(1)
    stop ambience fadeout 3
    show blink

    window show
    "Я закрыл глаза, но беспокойное чувство меня не покидало."
    "Я словно цепями был привязан к нему, я боялся, что усну вместе с этим чувством. Поэтому много ворочался."
    "И как бы старательно я не пытался отвлечься, мне всё равно пришлось уснуть вместе с ним."
    window hide
    
    $ renpy.pause(3, hard=True)
    play sound sfx_alisa_lighter
    $ renpy.pause(1, hard=True)
    play sound sfx_alisa_lighter
    $ renpy.pause(2, hard=True)
    play sound sfx_light_candle
    play sound_loop sfx_torch
    $ renpy.pause(1, hard=True)
    play sound sfx_intro_bus_stop_sigh
    show zdes_moi_glaz with dissolve2
    $ renpy.pause(3, hard=True)
    stop sound_loop fadeout 1
    show blink

    $ renpy.pause(1, hard=True)
    play sound_loop sfx_head_heartbeat fadein 3
    scene bg int_house_of_gg_sunset
    with flash

    window show
    "Я в одно мгновение вскочил с кровати."
    "Сердце колотилось.{w} В глазах темнело.{w} Я не мог успокоится.{w} Вся кровь будто перешла в мозг и начала интенсивно там пульсировать."
    "Беспокойное чувство не покидало меня ещё несколько секунд после моего сна,{w} звуки вокруг были полностью заглушены."
    "Я посмотрел на свои руки, осмотрелся вокруг,{w} сердце успокаивалось.{w} Вдох-выдох.{w} Вдох-выдох."

    stop sound_loop fadeout 3
    play ambience ambience_int_cabin_evening fadein 3

    th "Фу-ух…{w} Это всего лишь сон…"
    th "Черт его возьми...{w} Кошмар какой-то."
    th "Зато...{w} У меня теперь не так сильно болит голова..."
    th "Надо свериться со временем."
    window hide

    $renpy.pause(1)

    window show
    "Я достал из-под подушки свой телефон и включив экран взглянул на него."
    "Оно говорило о том, что мне пора на полдник."
    "Хоть мне и не особо хотелось есть, прийти в столовую мне все-таки нужно было, дабы Ульяна с Ольгой Дмитриевной меня случаем не потеряли."
    "Мне нужен был этот сон, пусть его и не назовёшь приятным."
    "Его нужно воспринять как обычный бред, снящийся мне по несколько раз в неделю.{w} И в моем случае сложно удивляться подобному явлению."
    "Несмотря на него, сейчас я чувствовал себя бодро. Можно даже сказать, именно благодаря этому сну я себя и чувствовал таким."
    window hide

    $renpy.pause(1)
    show black with dissolve
    stop ambience fadeout 2
    play sound sfx_open_door_1
    $renpy.pause(1)
    play ambience ambience_camp_center_day fadein 3
    scene bg ext_house_of_sl_day with dissolve2
    $renpy.pause(2)
    show black with dissolve
    $renpy.pause(1)
    scene bg ext_houses_day with dissolve
    $renpy.pause(1)
    show black with dissolve
    $renpy.pause(1)
    scene bg ext_dining_hall_away_day with dissolve2
    $renpy.pause(1)
    show black with dissolve
    scene bg ext_dining_hall_near_day with dissolve
    $renpy.pause(1)

    show mt smile pioneer at center with dspr

    window show
    "Дойдя до столовой на входе меня встретила вожатая."
    "На её лице виднелась добрая улыбка."
    hide mt with dspr
    "Она отошла от двери и впустила меня в столовую."
    window hide

    stop ambience fadeout 3
    play sound sfx_open_door_clubs
    show black with dissolve
    $renpy.pause(1)
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_day with dissolve
    play sound sfx_close_door_1

    window show
    th "Похоже, она тоже вздремнула в попытках отвлечься от того инцидента."
    th "Сложно отказаться ото сна, когда вокруг происходят подобные вещи."
    window hide

    $renpy.pause(2)

    window show
    "Взяв поднос с едой, я приземлился за один из свободных столов неподалёку."
    "Нам подавали булки с сахаром, конфеты с птичьим молоком, а также на моем подносе присутствовал стакан с обычным коровьим молоком."
    window hide

    $renpy.pause(1)

    window show
    "Факт того, что в советском союзе так много еды полностью шёл вразрез всему, что я знал о СССР раньше."
    "Он мне представлялся длинными очередями за едой, алкоголем, мебелью и другими продуктами потребления."
    "Может это лагерь для детей богатых родителей?{w} Возможно, но сколько себя помню, я был не из богатой семьи.{w} И это подтверждает тот факт, что в восемнадцатом году я ещё не уехал из России за лучшей жизнью."
    window hide

    $renpy.pause(1)

    show el normal pioneer at center with dspr

    window show
    "Вдруг мои размышления прервал Электроник, сев на стул передо мной."
    "Он выглядел каким-то необыкновенно обеспокоенным."
    nd_il "Привет. Шурик ещё не вернулся?"
    el "Привет.{w} Да.{w} Ты тоже его не видел?"
    nd_il "Нет, я его не видел."
    show el surprise pioneer at center with dspr
    el "Значит он потерялся."
    "Всё также обеспокоенно говорил Электроник."
    show el normal pioneer at center with dspr
    el "Нам нужно его найти."
    th "Вот это уже странно.{w} Думаю, за день можно было уже все детали перетаскать или по кирпичикам этот старый лагерь разобрать."
    nd_il "А разве он ещё не появлялся в лагере?"
    show el normal pioneer at center with dspr
    el "Нет. Ты поможешь мне найти его? Ты вроде как у нас спасатель."
    "Сказал Электроник и показал взглядом на мой значок."
    nd_il "Хорошо, вот только закончу с полдником. Где встречаемся?"
    hide el with dspr
    show el normal pioneer far at center with dspr
    "Электроник встал из-за стола."
    el "На площади."
    nd_il "Подожди, Ольгу Дмитриевну предупреди."
    el "Она уже знает. "

    hide el with dspr
    
    "Сказал Электроник и пошёл на поиски своего товарища, а я принялся доедать свой полдник."
    "Молоко было прохладным. Я запивал им сладкую булку."
    "Конфету я сразу целиком закинул в рот и прожевал."
    window hide

    $renpy.pause(2)

    window show
    "Вдруг ко мне кто-то подбежал сзади и похлопал по плечу."
    "Обернувшись я увидел человека, которого ожидал увидеть в столовой как никого другого."
    show us normal pioneer at center with dspr
    us "Илья, ты почему помогать мне не пришёл?"
    nd_il "У меня голова болела сильно."
    show us smile pioneer at center with dspr
    us "Ладно, но сейчас ты должен остаться."
    us "А не то я... Тебя проучу."
    nd_il "Проучишь своего спасителя?"
    "Эту фразу я произнес с неширокой улыбкой."
    show us shy pioneer at center with dspr
    us "Дурак."
    nd_il "Солидарен..."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $renpy.pause(3, hard=True)
    play ambience ambience_dining_hall_empty fadein 3
    scene bg int_dining_hall_day with dissolve2

    $renpy.pause(1)

    window show
    "Вскоре столовая опустела."
    "И естественно, мы с Ульяной начали уборку за пионерами."
    "По правде сказать, продлилась она недолго. Видимо многие считали, что в этом лагере на полдник приходить нет особого смысла."
    "Но вскоре нам однообразная работа начала надоедать. К счастью это случилось позже, чем нам с Ульяной осталось протереть последний стол."
    "И когда всё было закончено, Ульяна побежала на переговоры к поварам, а я вовремя заметил за самым дальним столом уже известного мне Толяна."
    window hide

    $renpy.pause(1)
    
    window show
    "Я сел за один из свободных столов и принялся рассматривать его издалека."
    "О его пионерстве напоминала только пионерская форма. Он был слишком стар для вожатого, слишком странным для дворника или санитара."
    "Это определенно должен был быть какой-то пионер, застрявший тут лет примерно на пятьдесят."
    "Погодите-ка... Может он такой же как и я? Может он попал сюда также через автобус-призрак? И застрял здесь..."
    "Внутри меня всё сжалось до атомов. Всё сходилось. Все считают его пионером, и даже пионерскую форму ему достали. А на вид ему гораздо больше лет, чем пионерам тех лет."
    "Боже мой... Так я, получается, для него выгляжу также? А может в этом лагере все меня так видят?"
    "Все пионеры здесь существуют и в реальной жизни, но застряли здесь. Просто кто-то раньше, а кто-то позже."
    "Значит конца смены никогда не наступит? Я останусь здесь навсегда? Возможно со всеми этими пионерами мы будем расти именно здесь. Как лабораторные мыши в клетке под властью каких-то безумных учёных."
    window hide

    $renpy.pause(2, hard=True)

    show us smile pioneer at center with dspr
    
    window show
    us "Илья, ты чего тут один сидишь и грустишь? Держи."
    "Сказала Ульяна, и достав из-за спины два брикета мороженого протянула мне одно из них."
    nd_il "Спасибо."
    show us grin pioneer at center with dspr
    us "Ну так что? Скучаешь?"
    "Я хотел ей показать на того самого Толяна в конце столовой, но кинув туда взгляд я его там не обнаружил."
    nd_il "Я хотел тебе человека одного показать."
    show us surp2 pioneer at center with dspr
    us "Какого?"
    window hide
    
    hide us with dspr

    show prologue_dream with dissolve
    show tl_1_pioneer at center behind prologue_dream with dspr
    
    window show
    nd_il "Ну… Такого, с лысиной ещё, в костюме пионера и с каменным лицом."
    nd_il "Неразговорчивый ещё он."
    window hide
    
    hide tl_1_pioneer
    hide prologue_dream
    with dissolve

    window show
    show us smile pioneer at center with dspr
    us "Как ты описал, подходит только наш охранник."
    us "Ха-ха-ха. Где ты его видел в пионерской форме?..."
    hide us with dspr
    "Ульяна засмеялась."
    us "...Ему же лет под шестьдесят..."
    "В этот момент я невольно почувствовал себя дураком."
    "Может это было всего лишь моим видением?{w} Миражом?{w} Галлюцинацией?"
    "Ульяна продолжала смеяться во весь голос, но мне сейчас было не совсем смешно."
    "Похоже, с каждым днем в этом лагере я схожу с ума."

    show us grin pioneer at center with dspr

    us "...Ну ты и шутник. Перегрелся что ли? Давай я к твоей головушке пустой мороженое приложу."
    "Сказала Ульяна и сделала то, о чём только что говорила."
    "Я усмехнулся."
    nd_il "Надеюсь это поможет."
    window hide

    $renpy.pause(1, hard=True)
    hide us with dspr
    $renpy.pause(2, hard=True)

    window show
    "Когда я доел мороженое, я вспомнил за помощь Электронику в поисках Шурика по всему лагерю. И пока вожатая не начала трубить тревогу, нам необходимо было найти последнего."
    "Я встал из-за стола и вытер рот чистой стороной упаковки от мороженого,{w} а потом ещё раз ладонью."
    nd_il "Ладно, я пойду с Электроником Шурика искать."
    show us normal pioneer at center with dspr
    us "Стой."
    "Сказала Ульяна и встала на носочки, чтобы что-то сказать мне на ухо."
    us "Ты не забыл про записку? Ту которая с фокусом."
    window hide

    stop ambience fadeout 4
    $renpy.pause(1, hard=True)

    hide us
    show prologue_dream
    scene bg ext_path2_night 
    with dissolve

    show zapiska_d4_o with dissolve

    $renpy.pause(3, hard=True)
    
    scene bg int_dining_hall_day with flash

    show us normal pioneer at center with dspr
    
    window show
    nd_il "Спасибо что напомнила."
    nd_il "Я ещё не решил, что буду с ней делать."
    us "Не за что. Я побежала..."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    th "Всё, заговорился я. Нужно на площадь к Электронику идти."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    play sound sfx_open_door_1
    $renpy.pause(1, hard=True)

    $ nd_change_time('sunset')

    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_dining_hall_near_sunset with dissolve
    play sound sfx_close_door_1
    $renpy.pause(1, hard=True)
    show black with dissolve
    scene bg ext_dining_hall_away_sunset with dissolve
    $renpy.pause(1, hard=True)
    show black with dissolve

    $renpy.pause(3, hard=True)

    scene bg ext_square_sunset with dissolve2

    show el normal pioneer at center with dspr

    window show
    "Увидев кибернетика у статуи Генды, я подбежал к нему."
    nd_il "Ну что? Пошли искать?"
    el "Пошли, только давай разделимся, чтобы быстрее было."
    nd_il "Хорошо.{w} Тогда я посмотрю за лагерем, а ты в лагере."
    el "Договорились."
    window hide

    hide el with dspr

    $renpy.pause(1)

    stop ambience fadeout 3
    show black with dissolve
    $renpy.pause(3)
    scene bg ext_clubs_sunset with dissolve


    window show
    "Проходя рядом со зданием кружка кибернетики, я невольно вспоминал события своего первого дня в этом лагере."
    window hide

    stop ambience fadeout 3

    show prologue_dream
    scene bg ext_bus behind prologue_dream with dissolve

    window show
    "Автобус без водителя..."
    window hide

    show black with dissolve

    show cg d1_grasshopper_nd 
    show prologue_dream
    with dissolve

    window show
    "Ульянка, напугавшая Лену..."
    window hide

    show black with dissolve
    play ambience ambience_camp_center_evening fadein 2
    scene bg ext_clubs_sunset with dissolve

    window show
    "Странно, что на меня нашло только что в столовой?"
    "Этот лагерь с самого начала показался каким-то дружелюбным."
    show prologue_dream with dissolve
    "Но вместе с этим из головы не выходили слова Даши и сомнения в правильности моего вчерашнего выбора."
    "Ульяна, наверное, расстроилась, если бы я не пришёл смотреть с ней на рассвет."
    "А могу ли я её расстраивать? А подвергать опасности? А распоряжаться её судьбой? Правильный ответ — нет."
    "Значит было бы лучше, чтобы я ушёл.{w} Тогда, возможно, она бы не начала тонуть на пляже."
    "А если бы я ушёл, и она всё равно бы?.."
    "Не хочу об этом думать."
    "Если выбрал путь — значит иди вперёд, несмотря ни на что."
    "Так я поступал всегда, и буду поступать дальше, пока что-нибудь не заставит изменить эту черту моего характера."
    window hide

    stop ambience fadeout 3
    hide prologue_dream
    show black
    with dissolve

    $renpy.pause(3, hard=True)

    play ambience ambience_camp_entrance_evening fadein 4
    scene bg ext_camp_entrance_sunset_wahf with dissolve2
    $ volume(0.3, "music")
    play music ndm_list['guitar_song_nd_4'] fadein 4

    window show
    "С этими мыслями я вышел за ворота лагеря.{w} И сразу же услышал еле слышные струны гитары."
    "На бордюрчике сидела Маша, и играла на гитаре свою очередную волшебную, завораживающую слух и разум мелодию."
    "Она была такой волшебной, что было сложно сфокусировать внимание на чем-то другом."
    "Казалось, что даже матушка природа прекратила дышать, дабы дать места игре на гитаре в исполнении этой девушки с аквамариновыми хвостами."
    "И в таком случае, природу можно было понять."
    window hide

    $renpy.pause(1, hard=True)

    window show
    "Я оглянулся по сторонам, в надежде увидеть какого-нибудь кибернетика, но надежды имеют свойство рушиться."
    window hide
    
    $renpy.pause(2, hard=True)

    window show
    th "Ладно. Если я заслушаюсь, то Шурика даже к ночи не найду."
    th "Но как сладостно звучат струны, которых касается Маша..."
    window hide

    show black with dissolve

    window show
    "Я слушал эту мелодию, и в голову лезло большое количество мыслей."
    "Но я не успевал на них зациклиться и погрязнуть в них до конца."
    "Каждая новая струна рождала в моей голове несравнимое ни с чем чувство.{w} Я бы назвал это ностальгией по старым временам, но боюсь, что это чувство не имеет с этим определением ничего общего."
    "Если прислушаться повнимательнее, можно услышать скрытый смысл в каждой ноте, в каждом аккорде. Будто исполнитель общается со слушателем на каком-то своём языке.{w} Который, кажется, поймёт только избранный, либо сам исполнитель."
    "В любом случае шла уже пятая минута моего вслушивания, и Мику не собиралась останавливаться."
    "Это было похоже на её попытку медитировать.{w} Мне сейчас это было противопоказано."
    "Я обещал Электронику заняться поисками Шурика. И для этого необходимо оторваться от до странности волшебной мелодии."
    "И я, мысленно похвалив Машу за прекрасную игру, нехотя зашёл за ворота обратно в лагерь."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3 
    show black with dissolve
    scene bg ext_clubs_sunset with dissolve
    play ambience ambience_camp_center_day fadein 3

    window show
    "Следующим местом я решил проверить клуб кибернетики."
    th "Может Шурик сейчас сидит там, попивает чай и залипает в паянии каких-то своих приборов?"
    "Я поднялся по лестнице к железной двери здания клубов."
    th "Хотя навряд ли он там будет, но..."
    window hide

    play sound sfx_open_door_clubs
    stop ambience fadeout 3
    show black with dissolve
    play ambience ambience_int_cabin_evening fadein 3
    scene bg int_clubs_male_sunset with dissolve
    play sound sfx_close_door_1

    $renpy.pause(2, hard=True)

    window show
    nd_il "Есть кто?!"
    "Ответа не последовало. Я принялся тщательно осматривать помещение."
    "На столе лежали брошенные инструменты и какой-то чертёж."
    window hide

    $renpy.pause(1, hard=True)

    window show
    "Что странно, во всём помещении адски смердело химией.{w} Будто кто-то жёг здесь покрышки или занимался чем-то подобным."
    "Я открыл окно, чтобы этот воздух смог выйти наружу, иначе можно было задохнуться."
    window hide

    play sound sfx_open_window

    $renpy.pause(2, hard=True)

    window show
    "Вдруг из подсобки донеслись шуршащие и шипящие звуки."
    "Я вздрогнул от неожиданности и принял решение в страхе закричать что-то угрожающее, если бы это был кто-то из грабителей."
    nd_il "Кто там? Я буду стрелять!"
    "Не знаю, какую цель я преследовал, выкинув эту фразу.{w} Навряд ли бы грабитель полез сначала именно в здание клубов."
    dvp "Чё сказал?! Сейчас выйду. Бойся..."
    "Голос отдался эхом по помещению, вырываясь из подсобки с повышенным тоном."
    "На этом моменте я понял, что зря выкрикнул что-то в страхе, и теперь может случится что-то непоправимое..."
    "Голос был мне знаком, я его уже где-то слышал. Но возможно, я путаюсь."
    "Это может быть грабитель или просто техничка, которой я сгоряча нагрубил."
    "Из подсобки с металлической палкой в руках вышла Алиса..."
    window hide

    show dv grin pioneer at center with dspr

    window show
    "Поняв, что это я, она сняла защитную маску и улыбнулась своей фирменной ухмылкой."
    nd_il "А, это ты, привет Алис."
    dv "Ты что, больной так орать?"
    nd_il "Нет, я думал там бандит какой-то…"
    dv "Сам ты бандит."
    nd_il "…Но дело вообще не в этом, ты не видела Шурика?"
    show dv smile pioneer at center with dspr
    dv "Нет, не видела."
    nd_il "И ещё, что тут так химией воняет? Ты что, самогон бадяжишь?"
    dv "Только никому, ладно?.."
    nd_il "Что, серьёзно?"
    dv "Нет. Зачем бадяжить самогон, если есть водка?"
    nd_il "Действительно."
    show dv normal pioneer at center with dspr
    dv "На самом деле я просто испачкала форму, и решила пятно растворителем оттереть."
    nd_il "А, ну ладно тогда."
    nd_il "Ты если Шурика найдёшь, обязательно расскажи вожатой."
    hide dv with dspr
    "Алиса положительно кивнула, и ушла обратно в подсобку."
    window hide

    $renpy.pause(1, hard=True)

    window show
    "Я уже собирался выходить из кружка."
    play sound sfx_open_door_clubs 
    "Толкнув входную дверь я крикнул Алисе на прощание:"
    nd_il "Форму не прожги!"
    window hide

    stop ambience fadeout 3
    show black with dissolve
    $renpy.pause(1, hard=True)
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_clubs_sunset with dissolve

    window show
    "Алиса что-то прокричала мне в ответ, но я уже был на улице."
    window hide

    $renpy.pause(2, hard=True)

    window show
    "Так, в смысле \"если есть водка\"?"
    "У Алисы есть бутылка водки? А как же Ульяна?"
    "Надеюсь Алиса в своем уме и не будет своей подруге предлагать выпить."
    "Хотя чего я боюсь?{w} Навряд ли Ульяна захочет пить что-то, что не имеет сладкого вкуса."
    "Поэтому перейдём к плану... А по плану теперь мне нужно проверить домик этих самых кибернетиков. Может Шурик всё это время, сколько мы его ищем, там на кровати лежит и десятый сон видит."
    window hide

    $ renpy.pause(1, hard=True)
    play sound sfx_dinner_horn_processed 
    
    window show
    "Мои размышления были прерваны мелодичным сигналом из динамиков, видимо, призывающим пионеров на площадь."
    th "Похоже вожатая всё-таки решила всех собрать..."
    "Я глубоко вздохнул, и мои ноги понесли меня к площади."
    window hide

    show black with dissolve
    $renpy.pause(2, hard=True)
    scene bg ext_square_sunset with dissolve2

    window show
    "Там уже собралось большинство пионеров лагеря. Из моего отряда пришли абсолютно все кроме Алисы."
    "Ольга Дмитриевна стояла перед пионерами, и видимо, ждала прихода большего их количества."
    "Или именно меня..."
    window hide

    $ renpy.pause (2, hard=True)

    window show
    "Когда я встал в линейку, Ольга Дмитриевна начала свою речь."
    window hide

    show mt normal pioneer at center with dspr

    $renpy.pause (1)

    window show
    mt "Здравствуйте, пионеры."
    mt "Я собрала вас здесь чтобы сообщить о неприятном происшествии."
    mt "У нас в лагере пропал пионер из старшего отряда, и нам необходимо его найти…"
    th "Вожатая дело говорит."
    mt "Илья, а где Электроник? Вы вроде как с ним Шурика ходили искать."
    nd_il "Он побежал искать Шурика в…"

    hide mt with dspr

    "Но мой ответ перебил бегущий Электроник, махающий обувью и довольно крича что-то, что начало превращаться в слова только тогда, когда он подбегал к площади ближе."
    window hide

    $renpy.pause (2)


    show el normal pioneer at left with dspr
    window show
    el "Я нашёл! Я нашёл его ботинок!"
    "Среди пионеров в линейке повисла тишина. Все были в ожидании того, что скажет Электроник и Ольга Дмитриевна."
    mt "Где ты его нашёл?"
    el "Там где пролесок...{w} К старому лагерю."
    "Между пионерами пошёл довольно громкий шёпот.{w} Они все повторяли:"
    all "Старый лагерь..."
    all "Он в старом лагере..."
    all "Старый корпус..."
    th "Неужели этот старый лагерь и вправду настолько мистическое место?"
    th "Сильно сомневаюсь."

    show mt normal pioneer at center with dspr

    mt "Я так и знала…"

    hide el with dspr

    mt "Итак, кто-то должен отправиться на поиски товарища."
    mt "Мы волнуемся за безопасность пионеров, и соберем вас так, чтобы вы в процессе поисков не потерялись сами."
    mt "Итак, желающие, сделайте шаг вперед."
    th "Ну раз уж я спасатель, к тому же сегодня ещё и добрый..."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    "Я неуверенно и невысоко поднял руку, но этого оказалось достаточно, чтобы Ольга Дмитриевна это заметила."
    
    show mt normal pioneer at center with dspr

    mt "Илья. Подойди ко мне."

    hide mt with dspr

    "Сказала вожатая."
    "Я выполнил её указание и повернулся лицом к линейке пионеров."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    nd_il "Я найду Шурика."
    mt "Вот это настрой."
    mt "Ты можешь взять с собой ещё кого-нибудь."
    window hide

    $ renpy.pause (3, hard=True)

    window show
    "И тут я задумался."
    th "Кого я хочу взять с собой?"

    show sl normal pioneer far at fleft
    show un smile pioneer far at left
    show us normal pioneer far at center
    show el normal pioneer far at right
    with dspr

    th "Тут есть все. — Славя, Лена, Ульяна, Маша, Электроник, Алиса вдалеке бежит…"

    show mz normal glasses pioneer far at fright with dspr

    th "Даже библиотекарша здесь."
    th "Но идти с ней — это, наверное, самоубийство.{w} Поэтому либо одному, либо с Ульяной.{w} А захочет ли она?"
    window hide

    $ renpy.pause (2, hard=True)

    window show

    hide us
    hide un
    hide el
    hide mz
    hide sl
    with dspr
    
    window show
    nd_il "Ульяна, можно взять тебя с собой?"
    show us surp2 pioneer at center with dspr
    us "Меня?"
    "С удивлением спросила Ульяна. В её глазах смешались удивление, энтузиазм и жажда приключений."
    nd_il "Да."
    "Тихо сказал я и кивнул."
    mt "Ладно, можешь взять с собой Ульяну."
    mt "Только следи за ней."

    hide us with dspr

    nd_il "Хорошо."
    "Ульяна после слов вожатой недовольно цыкнула, но вмиг её лицо преобразилось."
    "Вероятно, она думала, что это всё игра, что мы идем не искать Шурика а на экскурсию по таинственному месту."
    "Таинственному потому, что он здесь у всех на слуху."
    window hide

    $ renpy.pause (2, hard=True)

    window show
    "Я отправился обратно в строй."
    "Ольга Дмитриевна начала объяснять правила техники безопасности."
    window hide

    show black with dissolve2
    
    window show
    "А точнее запреты, которые, как мне кажется, все пионеры даже помнить не хотят."
    "Если даже порядочный кибернетик отправился за пределы лагеря ради своих каких-то целей."
    "А точнее - за деталями, которые по любому потратит на что-то, что не продвинет науку ни на шаг."
    "Но это идет вразрез его словам.{w} Может я слишком сильно их недооцениваю? Они же всё-таки сделали зарядное устройство для аккумулятора из будущего."
    "Хотя может я ошибаюсь, и его новое изобретение даст рывок советской науке.{w} Если я его найду, конечно..."
    window hide

    $ renpy.pause (2, hard=True)

    scene bg ext_square_sunset with dissolve2

    window show
    "В конце концов линейка закончилась, и пионеры начали расходиться."
    window hide

    play music ndm_list['mood_play'] fadein 4

    $ renpy.pause (1, hard=True)

    show us surp2 pioneer at center with dspr

    window show
    "Ульяна подошла ко мне и переполнившись радостью закричала:"
    us "Ура! Мы идем в старый лагерь!"
    nd_il "Тише. Да, идём. Но не думай, что это просто увеселительная прогулка."
    
    show us dontlike pioneer at center with dspr

    us "Ой зану-уда."
    "Недовольно протянула Ульяна."

    hide us with dspr

    "Она выглядит милой, когда злится.{w} Милой и в тоже время опасной."
    nd_il "Да не зануда я."
    vg "Ой, хоть сам себе не ври."
    nd_il "Просто я волнуюсь. А вдруг не найдём."
    
    show us grin pioneer at center with dspr

    us "Электроник же сказал, что нашёл его башмак на тропинке к старому лагерю."
    window hide
    
    $ renpy.pause (1, hard=True)

    show dv grin pioneer at right with dspr

    window show
    "В этот момент к нам подошла Алиса и присоединилась к диалогу."
    dv "Не ссыте в старый лагерь идти?"
    us "Я нет, а вот Илья…"
    nd_il "Я этого не говорил!"
    "Возмутился я, а потом задумался..."
    window hide

    hide dv
    hide us
    with dspr

    $ renpy.music.set_volume(0, delay=3, channel="music")
    $ renpy.pause(3)
    $ renpy.music.set_pause(1, channel='music')
    
    window show
    th "Если я собираюсь идти в старый лагерь, то нужно хорошо подготовиться. Взять фонарик, батарейки к нему, возможно, еды…"
    vg "Ахах, еды он захотел.{w} В поход идёшь что ли?"
    th "А кто знает, может этот лагерь огромный."
    th "Кстати, надо ещё оружие какое-нибудь взять.{w} Вдруг нападёт зверь какой-нибудь по дороге…"
    vg "Или какой-то пионер мутировавший, ну ты и гений..."
    th "На твоем месте я бы вообще молчал, учитывая, что ты мой посттравматический синдром..."
    window hide

    $ renpy.pause(2, hard=True)

    $ renpy.music.set_volume(1.0, delay=3, channel="music")
    $ renpy.music.set_pause(0, channel='music')

    window show
    "Я вышел из раздумий в реальный мир."
    
    show us grin pioneer at left
    show dv normal pioneer at right
    with dspr

    us "А вдруг у него проблемы какие-то?"
    "Спросила Ульяна свою подругу шёпотом на ухо."
    
    show dv grin pioneer at right with dspr

    dv "Ну не знаю, не знаю..."
    dv "С головой разве что."
    th "Чего?"
    nd_il "Какие к чёрту проблемы? Пошли собираться в старый лагерь."
    show us smile pioneer at left with dspr
    us "Да что там собираться? Раз, и пошли."
    nd_il "Нет, нужно ещё фонарик взять, оружие, провизию."
    vg "Про провизию-то он не забыл.{w} Лишь бы поесть бесплатно, честное слово"
    show dv smile pioneer at right with dspr
    dv "Ладно, заговорилась я с вами.{w} Мне пора."
    nd_il "Пойдёшь свои грязные делишки планировать?"
    show dv normal pioneer at right with dspr
    dv "Да ну тебя."
    hide dv with dspr
    "Сказала Алиса, и отправилась в сторону музыкального кружка."
    window hide

    $renpy.pause (2)

    window show
    nd_il "Ульяна, у тебя нет фонарика в домике?"
    us "Был вроде."
    show us grin pioneer at left with dspr
    us "Побежали!"
    hide us with dspr
    "Сказала Ульяна, и рванула с низкого старта к своему домику, а мне оставалось её кое-как догонять..."
    window hide

    stop ambience fadeout 4
    stop music fadeout 4
    show black with dissolve2

    $renpy.pause (2)
    
    window show
    "И зачем она постоянно бегает... И самое что удивительное - не устаёт."
    "Как батарейка какая-то нескончаемая.{w} Хах."
    "Батарейка \"Ульяна\".{w} Разрядилась?{w} Да и пофигу..."
    window hide

    $renpy.pause (2)

    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_house_of_dv_sunset with dissolve2

    
    show us normal pioneer far at center with dspr
    
    window show
    "Когда я прибежал к домику, Ульяна уже стояла перед дверьми."
    window hide

    $ volume (0.3, "sound")    
    play sound sfx_open_door_1
    hide us with dspr
    
    window show
    "Увидев меня, она открыла дверь и махнув рукой пригласила меня в домик."
    window hide

    stop ambience fadeout 3 
    show black with dissolve
    $renpy.pause (1)
    $ volume (1, "sound")
    play ambience ambience_int_cabin_evening fadein 3
    scene bg int_house_of_dv_sunset with dissolve
    play sound sfx_close_door_1

    $renpy.pause (2)

    play music ndm_list['USSR_1'] fadein 5

    window show
    "Войдя в него, мы закрыли за собой дверь, и принялись искать фонарик, а также разные полезные вещи для похода в старый лагерь."
    window hide

    $renpy.pause (1)

    window show
    "В вещи Алисы без её разрешения я соваться не стал. Мало ли что."
    "Перерыв весь домик мы всё-таки нашли этот несчастный фонарик (Который лежал всё это время в укромном месте на шкафу)."
    "Ульяна достала свой рюкзачок, и сложила туда фонарик."
    "Невольно мне вспомнился мультик про Дашу-путешественницу, который так и назывался."
    nd_il "Что ещё положим?"
    "Спросил я Ульяну."

    show us grin pioneer at center with dspr
    
    us "А мы положим…"
    
    hide us with dspr

    "Протянула пионерка, и подойдя к шкафчику своей подруги достала оттуда предмет нижнего белья, а точнее лифчик."
    "Не знаю, какое из её действий я пропустил, но этот предмет уже летел в мою сторону."
    with hpunch
    nd_il "А-а-а."
    "Закричал я и попятился в угол подальше от белья Алисы и..."
    "...И тут я опять вспомнил про свои плавки на пляже."
    th "Точно, там же мои плавки всё ещё на пляже лежат. Или уже не лежат…"
    
    show us laugh pioneer at center with dspr

    "В это время Ульяна заливалась заразительным хохотом, который напоминал пулемётный залп."
    "Я сделал из пальцев автомат и принялся расстреливать Ульяну её же смехом."
    "Та посмотрела на меня и стала смеяться ещё сильнее.{w} Казалось, что она сейчас лопнет."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    
    window show
    nd_il "Всё, подруга,{w} хватит."    
    "Сказал я и взяв лифчик Алисы двумя пальцами аккуратно закинул его обратно в шкафчик."
    window hide

    $ renpy.music.set_volume(0, delay=2, channel="music")
    $ renpy.pause(2)
    $ renpy.music.set_pause(1, channel='music')

    window show
    "Когда Ульяна перестала хохотать, мы продолжили искать что-нибудь, что можно положить в её рюкзак."
    
    show us normal pioneer at center with dspr

    nd_il "Что у нас дальше по плану,{w} Самооборона?"
    "Я произнёс это предложение так, будто сам не задумывался над его смысловым значением."

    hide us with dspr
    
    "Та молча залезла в свой шкафчик,{w} и достав оттуда выкидной охотничий нож, одним легким движением оголила лезвие,{w} подбросила,{w} и зачехлив обратно положила в сумку."
    window hide    

    $ renpy.pause (3)

    window show
    th "Что это только что было?"
    nd_il "Это был охотничий нож?!"
    
    show us smile pioneer at center with dspr

    us "Тсс… Тише…"
    "..."
    "...."
    nd_il "Ну... Хорошо."
    
    hide us with dspr

    "Тихо, как и просила Ульяна, сказал я приглядевшись в пустоту, непроизвольно намеченную моими глазами."
    "Непонятно, откуда у пионерки охотничий нож, который по сравнению с ней - настоящий тесак?"
    "Хотя, может я гиперболизирую? Не тесак, конечно, но скажем, этим лезвием можно было разделать тушу какой-нибудь белки."
    "И как она его крутила прямо на моих глазах, не опасаясь за свою жизнь?"

    show us smile pioneer at center with dspr

    $ renpy.music.set_volume(1.0, delay=2, channel="music")
    $ renpy.music.set_pause(0, channel='music')

    us "Видел бы ты своё лицо."
    "Улыбнувшись сказала Ульяна, и продолжила собирать вещи в сумку."
    window hide
    
    hide us with dspr

    $ renpy.pause (2, hard=True)

    window show
    nd_il "Ладно. Теперь вопрос о провизии."
    "Ульяна опять залезла в шкафчик, и достав оттуда пакет с печеньем закинула его в сумку."
    "Я же сделал вид, что не удивляюсь, но в голове у меня творилась вакханалия из мыслей и разрыв шаблона в понятии о среднестатистической пионерке."
    th "Если у неё охотничий нож, то что дальше?"
    window hide

    $ renpy.pause (2)

    window show
    "Пока я размышлял о происходящем, Ульяна достала из шкафчика Счётчик Гейгера и положила его в боковой карман сумки."
    "Глубоко вдохнув и выдохнув,{w} я знал,{w} этому было разумное объяснение."
    window hide

    $ renpy.pause (2)

    window show
    nd_il "Тебя папа собирал в лагерь?"
    show us normal pioneer at center with dspr
    us "Нет, мама."
    nd_il "Не думаю, что твоя мама одобрила бы {i}*шёпотом*{/i} ножик"
    show us grin pioneer at center with dspr
    us "Ножик я сама положила."
    window hide

    play sound sfx_inhale
    $ renpy.pause (2)

    window show
    "Я глубоко вдохнул воздух, подержал его в лёгких и выдохнул."
    nd_il "Мы готовы?"
    show us smile pioneer at center with dspr
    us "Готовы, гражданин-начальник."
    "Отдав честь, сказала Ульяна, закинула рюкзак на плечо и мы пошли на выход из её домика на улицу."
    window hide

    stop music fadeout 4
    stop ambience fadeout 3
    play sound sfx_open_door_1
    show black with dissolve
    $ renpy.pause (1)
    play ambience ambience_camp_center_evening fadein 3
    scene bg ext_house_of_dv_sunset with dissolve
    play sound sfx_close_door_1

    window show
    "Выйдя из домика Ульяны я достал телефон и посмотрел на время."
    "Оно показывало почти шесть часов вечера."
    "На встречу с таинственным незнакомцем я успею, но успею ли спасти Шурика при этом?"
    "К чёрту эти чертовы записки."
    window hide

    $ renpy.pause (2)

    window show
    nd_il "Ну что, пойдем на поиски этого несчастного Шурика?"
    
    show us normal pioneer at center with dspr

    us "Пойдём."
    "Сказала Ульяна, и мы отправились к старому лагерю."
    window hide

    show black with dissolve2
    $ renpy.pause (1)
    scene bg ext_houses_sunset with dissolve2

    window show
    "Так как я не знал, где этот лагерь, то вперёд меня вела Ульяна."
    "Мы шли по каменной дорожке к выходу из лагеря, или скорее, к какому-нибудь тайному проходу через ограду."
    "Я был уверен, что цивильного способа выбраться из лагеря не через главные ворота попросту нет."
    "Да даже если бы он и был, если старый лагерь заброшен, в проходе туда нет никакого смысла. Точнее не было бы, если бы какому-то кибернетику не приспичило отправиться туда за деталями."
    window hide

    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause (3, hard=True)

    window show
    "Как и ожидалось, на пути нам встретилась ограда, которую с виду можно было без труда перелезть сверху."
    "Но было в этой ограде и отверстие снизу."
    "В него я бы, конечно, не пролез.{w} А вот через верх - запросто, правда последний раз я перелазил через подобные препятствия не вспомню когда, поэтому в себя верил не до конца."
    "Моя напарница смогла без проблем пролезть под воротами. Настала и моя очередь..."
    "Я подпрыгнул и схватился за каменный уступ обеими руками,{w} затем попытался поднять ноги на него, что у меня благополучно получилось..."
    window hide

    $ renpy.pause (1, hard=True)
    play ambience ambience_forest_evening fadein 3
    scene bg ext_path_sunset with dissolve2

    window show
    "Как я и думал, перелезть этот кирпичный забор не составило особого труда, да и Ульяна проблем с этим не испытала."
    "Что же за этими воротами? Дорога... Глубокий лес, полный опасностей и приключений."
    "И находится в этом лесу старый лагерь, окутанный множеством мистики и легенд, которыми наполнялось моё воображение."
    "И это чувство первобытного интереса с каждой секундой значительно усиливалось."
    show us normal pioneer at right with dspr
    us "Ну вот, нам вперёд..."
    hide us with dspr
    play sound_loop sfx_far_steps fadein 3
    window show
    "Тихо проговорила рыжеволосая, и взяв меня за руку повела в лес навстречу...{w} Приключениям?"
    window hide

    play music ndm_list['GW_pyramid'] fadein 5

    $ renpy.pause (2)

    window show
    nd_il "А сколько нам вообще идти до этого лагеря?"
    show us normal pioneer at right with dspr
    us "Не знаю, долго."
    nd_il "Сколько?"
    us "Минут сорок."
    show us surp2 pioneer at right with dspr
    us "Но если ты будешь так плестись, то мы даже к отбою не успеем."
    nd_il "Надо выбирать пути покороче."
    show us smile pioneer at right with dspr
    us "Если бы мы шли по короткому пути, ты бы вообще не дошёл."
    nd_il "Я так не думаю."
    show us grin pioneer at right with dspr
    us "Потому что по короткому мы бы шли через овраги и ямы."
    nd_il "Я когда два дня назад тебя искал, хуже дороги не видел."
    us "И почему же?"
    hide us with dspr
    "Я опустил голову вниз."
    nd_il "Потому что я ударился обо что-то и пролежал около часа в отключке на поляне."
    th "Лучше уж поздно, чем никогда."
    window hide

    stop music fadeout 4

    $ renpy.pause(1, hard=True)
    stop sound_loop fadeout 3
    $ renpy.pause(1, hard=True)

    window show
    "Мы остановились на одном месте.{w} Пионерка посмотрела мне в глаза."
    show us sad pioneer at center with dspr
    us "Ты сейчас не шутишь?"
    nd_il "Ни капельки."
    us "Прости, я не знала что так произойдёт..."
    show us normal pioneer at center with dspr
    nd_il "Я уже давно всё тебе простил."
    us "Правда?"
    nd_il "Угу, с сегодняшнего утра."
    show us shy pioneer at center with dspr
    us "Дурак."
    hide us with dspr
    play sound sfx_far_steps fadein 5
    "Ульяна отвернулась, и мы вновь продолжили свой путь."
    "И я не жалел о том, что сообщил ей об этом моменте."
    "Тогда мне попросту было стыдно ей это сказать. Что я мог найти её ещё часом ранее, но из-за своей тупости не удержал равновесие и ударился так, что... До сих пор сложно вспоминать без боли."
    window hide

    $ renpy.pause (3, hard=True)

    window show
    "Мы шли ещё несколько минут молча, пока меня не начало это молчание \"убивать\" изнутри."
    "Было принято решение хоть как-то разбавить это самое молчание. И моим следующим вопросом должен был стать вопрос о месте, в которое мы идём."
    "О его пропитанной загадочностью истории, как я ожидал."
    "Думаю, она должна была мне рассказать о каких-то, возможно, секретных разработках,{w} о подпольных испытаниях советских учёных,{w} которые погубили это место, передав власть прошлой его администрации ей{w} - матушке природе."
    window hide

    $ renpy.pause (1)

    window show
    nd_il "Ульяна, а расскажи об этом старом лагере."
    nd_il "Сегодня утром, как я помню, ты обещала рассказать мне о нём."
    show us normal pioneer at right with dspr
    us "Сейчас расскажу. Слушай..."
    window hide

    stop music fadeout 4
    $ renpy.pause (2, hard=True)

    play music ndm_list['nd_horror_raskaz_us'] fadein 4
    show prologue_dream with dissolve

    window show
    us "Легенда гласит, что там раньше жили обычные пионеры."
    us "А ещё была там одна вожатая, которая любила одного из пионеров, но когда тот отверг её любовь, та повесилась в подвале лагеря."
    us "Как только пионер узнал, что из-за него умерла вожатая, он повесился вместе с ней в том же месте."
    us "Вожатые других отрядов скрывали это, но после того, как в лагере стали пропадать дети, пришлось всё всем рассказать."
    us "После этого все поняли, что лагерь проклят, и ушли оттуда."
    us "А ещё говорят, что там всё ещё водятся духи вожатой и пропавших пионеров,{w} а те кто попадают в лагерь спустя несколько часов сходят с ума."
    window hide

    hide prologue_dream with dissolve
    $ renpy.pause(1, hard=True)

    window show
    nd_il "Жуткая история."
    "Признаться, я ожидал услышать что-то более загадочное и мистичное, чем заезженную историю, которую можно приплести к любому заброшенному объекту советских времён."
    "Тем не менее, история Ульяны действительно показалась мне пугающей."
    us "Это точно, мне её Алиса рассказала."
    us "Но я этого лагеря ещё никогда не видела, а сегодня появился такой шанс."
    nd_il "И ты ни капельки не боишься?"
    show us smile pioneer at right with dspr
    us "Не-а. Не боюсь."
    us "А ты, наверное, боишься."
    nd_il "Это, конечно, жутко, но пока я не увижу лагерь собственными глазами, не буду верить в эти ваши страшные истории."
    show us grin pioneer at right with dspr
    us "Ну-ну."
    window hide

    $ renpy.pause (1, hard=True)
    hide us with dspr
    stop music fadeout 4
    show black with dissolve2
    $ renpy.pause (3, hard=True)
    scene bg ext_path2_sunset with dissolve2

    stop sound_loop fadeout 3

    window show
    "Пройдя ещё немного, нас встретила развилка."
    "Было две дороги. На одной из них были относительно свежие следы, ведущие прямо."
    "Ульяна осмотрела их и показала пальцем вглубь леса, куда вела эта дорожка."
    show us normal pioneer at left with dspr
    us "Нам туда."
    nd_il "Понял."
    window hide
    
    hide us with dspr
    play sound_loop sfx_far_steps fadein 2
    $ renpy.pause (1, hard=True)
    show black with dissolve2

    window show
    th "А вдруг мы потом заблудимся?"
    vg "Не заблудимся, если ты перестанешь придумывать поводы не идти в этот \"страшный лагерь\"."
    th "Внутренние голоса никто не спрашивал."
    window hide

    $ renpy.pause (2, hard=True)
    scene bg ext_path2_sunset with dissolve2

    window show
    nd_il "Ульяна, а когда мы придём туда?"
    us "Вот уже.{w} Сейчас..."
    window hide

    show black with dissolve
    $ renpy.pause (2, hard=True)

    window show
    "Вскоре из-за деревьев начало проглядываться что-то достаточно высокое."
    "Я в предвкушении чего-то большого прибавил шаг. До того, чтобы увидеть лагерь оставалось всего ничего."
    "Три...{w} Два...{w} Один..."
    window hide
    stop ambience fadeout 3
    stop sound_loop fadeout 3
    $ renpy.pause (2, hard=True)
    play music ambience_old_camp_outside fadein 3
    play ambience ambience_forest_evening fadein 3
    scene bg ext_old_building_sunset_red with dissolve2

    window show
    nd_il "Ва-ау. Какое оно огромное..."
    us "Ага..."
    nd_il "Подожди, так ты разве не была тут раньше?"
    us "Нет, мне рассказывали друзья из другого отряда..."
    window hide

    $ renpy.pause (2, hard=True)

    window show
    "Это здание выглядело достаточно старым."
    "Доски, из которых было оно сделано, находились в ужасном состоянии."
    "Тем не менее, выглядело это здание крепким, словно и не собиралось отправляться на покой."
    "А если учитывать вечернее время и рассказы Ульяны, то оно было ещё и жутким."
    "Честно сказать, я думал это будет целый комплекс из зданий, абсолютно вымерший и захваченный природой под свои безграничные нужды."
    window hide

    window show
    us "Ура! Пойдем осмотрим что внутри?"
    nd_il "Конечно. Мы ведь за этим и пришли."
    "Сказал я, и мы подошли к лагерю поближе."
    "Окрестности его напоминали богом забытое болото, которое только навеивало жуткую атмосферу."
    "Проходя по этим местам, мы подошли к самому входу в здание."
    "Меня тут же невольно бросило в дрожь."
    "Мы стояли прямо под ним. И оно с каждой минутой всё больше манило своим видом."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    nd_il "Ульяна, возьми мою руку, чтобы не потеряться."
    us "Хорошо."
    "Ульяна взяла меня за руку, и мы медленно вошли в старое здание."
    window hide

    stop music fadeout 3
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause (3, hard=True)
    play ambience ambience_catacombs fadein 3
    play music ndm_list['old_camp_inside_music'] fadein 3
    scene bg int_old_building_day with dissolve2

    window show
    "Перед моими глазами показалось помещение, отдалённо напоминающее прихожую."
    "Разобрать назначение этой комнаты было очень трудно, так как в ней был только ковёр и провалившийся гнилой стол."
    "В углу была лестница, которая вела наверх. Она выглядела не очень крепкой, а её ступеньки, казалось были готовы развалиться от одного лишь прикосновения."
    "Из щелей в стенах этого здания просачивался красный свет, открывая вид на солнце, прячущееся за деревьями."
    "Меня охватило чувство дежавю.{w} Я как будто уже видел это место."
    "Это чувство с каждой секундой было всё сильнее. Все сильнее хотелось погрузиться в него."
    "Это был первобытный интерес, смешанный с энтузиазмом и жаждой новых ощущений."
    "Подобного чувства я не испытывал уже очень давно."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    nd_il "Ульяна, сейчас мы тихонько пойдём осматривать здание."
    nd_il "Полы могут провалится в любой момент, поэтому крепко держи меня за руку."
    "Сказал я шёпотом."
    "Ульяна посмотрела мне в глаза и положительно кивнула."
    window hide

    $ renpy.pause (2, hard=True)
    
    window show
    "Мы отправились исследовать это место."
    "Я осмотрел стол, старые потрёпанные диваны, какой-то деревянный стул…"
    show us normal pioneer far at right with dspr
    us "Илья, там какой-то люк."
    hide us with dspr
    "Шёпотом сказала Ульяна, и показала пальцем в угол, где под стулом можно было увидеть проход куда-то, закрытый деревяшками."
    nd_il "Молодец, давай проверим что там?"
    "Сказал я и аккуратно подошёл к этому проходу."
    us "Давай, только аккуратно."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    "Доски на полу очень сильно скрипели, и издавали сильный шум, давящий на нервы."
    "Если взять историю Ульяны за реальность, то под этим люком лежат мёртвые трупы пионера и вожатой."
    "От этих мыслей моё сердце начало биться сильнее.{w} Я сжал руку Ульяны, и аккуратно убрал деревянный стул."
    "Там и вправду был деревянный люк, пребывающий здесь не в самом лучшем состоянии.{w} Концы его уже давно сгнили, а петли поржавели от влажности воздуха внутри этого помещения."
    us "Пошли туда?"
    "Вполголоса спросила меня пионерка."
    "Казалось, что ей совсем не страшна та обстановка, в которой мы сейчас находимся.{w} Признаться, я думал, что она будет хоть сколько-то напугана."
    vg "Илья, ты просто ссыкло, признай это."
    nd_il "Пошли."
    "Сказал я, бросив вызов самому себе и временно поборов инстинкт самосохранения."
    window hide

    $ renpy.pause (1, hard=True)

    window show
    "Казалось, что его уже открывали недавно. Оно и понятно - здесь был Шурик."
    "Но тогда в голове возникал вопрос: почему люк был прикрыт стулом и другими деревяшками?"
    "Аккуратно присев на корточки, я взялся за металлическую ручку и потянул за неё вверх..."
    window hide

    $ renpy.pause (2, hard=True)
    play sound nds_list['open_wooden_door']

    window show
    "Люк со скрипом открылся, показав за собой металлическую лестницу, уходящую вниз - в беспроглядную темноту."
    nd_il "Дай, пожалуйста, фонарик."
    us "Держи."
    play sound sfx_drop_alisa_bag
    "Сказала Ульяна, открывая рюкзак и доставая оттуда предмет, с которым я и собирался спустится вниз."
    window hide

    $ renpy.pause (1, hard=True)
    play sound nds_list['nd_flashlight_on']

    window show
    "Нажав на кнопку свет пронзил темноту, и внизу можно было разглядеть бетонный пол."
    nd_il "Я спускаюсь первым, чтобы проверить обстановку."
    us "Хорошо. Я жду тебя тут..."
    window hide

    stop music fadeout 6
    stop ambience fadeout 3
    show black with dissolve2

    window show
    "...И я полез вниз, раздвигая темноту ярким и немного желтоватым светом."
    window hide

    $ renpy.pause (2, hard=True)
    
    play ambience ambience_catacombs fadein 3

    $ nd_change_time('night')

    window show
    "Встав на бетонный пол я позвал Ульяну:"
    nd_il "Залезай сюда!"
    "Но мне никто не ответил.{w} Сердце было готово выпрыгнуть из груди и пуститься в пляс вместе с человеческими силуэтами, мерещившимся в темноте."
    nd_il "Ульяна!"
    us "Илья, там что-то было."
    nd_il "Залезай сюда, тут спокойней."
    play sound nds_list['metallic_stair']
    "Спустя пару секунд я услышал звуки спуска по этой металлической лестнице..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Когда моя напарница окончательно спустилась вниз, я взял её за руку и решил-таки осветить комнату, в которой мы оказались."
    window hide

    $ renpy.pause (1, hard=True)
    play music ndm_list['nd_in_catacombs'] fadein 4
    scene bg int_mine_door with flash
    $ renpy.pause (1, hard=True)

    window show
    "Это помещение было похоже на подвал."
    "У стенок стояли вёдра, лопаты, канистры с бензином. А на стене висели не заправленные фонари."
    "Впереди была деревянная дверь с какими-то железными заплатками и замками."
    us "Илья, чего ты встал, пошли вперёд."
    "Сказала Ульяна и повела меня к двери."
    "Рассмотрев эту дверь, я заметил открытый замок."
    th "То есть дверь уже открывалась."
    "Этот факт придал мне сил идти дальше."
    window hide 

    show black with dissolve
    play sound sfx_open_door_mines 
    $ renpy.pause (1, hard=True)

    window show
    "Мы с Ульяной открыли дверь, и пошли вперёд по бетонному коридору, попутно освещая комнаты фонариком."
    "Слева виднелся какой-то проход. Света в нём не было, он был абсолютно тёмным, и только фонарик мог нам помочь."
    "Именно в этот момент у меня в голове промелькнула мысль о том, что это может быть какой-нибудь бункер."
    "И естественно, в нём должна была быть радиация, на которую лучше не натыкаться."
    nd_il "Думаю, нам нужен Счётчик Гейгера."
    nd_il "Здесь может быть достаточно много радиации."
    us "Поняла, сейчас достану."
    "Сказала Ульяна, и покопавшись в рюкзачке вынула оттуда нужный мне инструмент."
    window hide

    $ renpy.pause (1, hard=True)
    play sound nds_list['nd_flashlight_on']
    $ renpy.pause (1, hard=True)
    show cg d4_catac_us with dissolve2
    
    window show
    "Я включил его и положил в одну руку с фонариком. Другая рука держала Ульяну, чтобы та не уходила далеко, поскольку я всё-таки отвечаю за неё."
    window hide

    $ renpy.pause (3, hard=True)

    scene black with dissolve

    window show
    "Пройдя ко входу в новый коридор, я незамедлительно осветил его фонариком."
    window hide

    scene bg int_catacombs_hole with dissolve
    
    $ renpy.pause (2, hard=True)

    show nd_dozimer_nocifr:
        xalign 0.1 yalign 5.0
        linear 1.0 yalign 0.8
    with dissolve

    window show
    "В нём были два отверстия, в одном из которых с потолка падали капельки воды в уже имеющуюся, разлитую на полу."
    "У меня не было никаких предположений, откуда здесь может быть вода, но тем не менее, она была тут, и явно не безвредная."
    "И здесь мне бы пригодился инструмент у меня в руках."
    window hide

    $ renpy.pause (1, hard=True)

    show nd_dozimer_cifr:
        xalign 0.1 yalign 0.8
    with dissolve

    play sound nds_list['sfx_catac_rad'] fadein 3
    
    $ renpy.pause (2, hard=True)

    window show
    "Проходя рядом с отверстием в стене с водой, счётчик Гейгера затрещал и показал на своем экранчике цифру."
    th "Хорошо, что Ульяна догадалась взять с собой счётчик,{w} иначе мы бы даже не знали, что находимся в радиоактивной зоне."
    stop sound fadeout 5
    show us surp2 pioneer at right with dspr
    us "Ничего себе. Настоящая радиация?"
    nd_il "Угу.{w} Не советую задерживаться, а то тебя облучит и вырастет третья рука."
    us "Да ну. Ничего такого не будет."
    nd_il "Хочешь проверить?"
    hide nd_dozimer_nocifr with dissolve
    show us normal pioneer at right with dspr
    "Рыжая пионерка посмотрела на меня взглядом, который будто бы спрашивал у меня:{w} \"совсем дурак?\"."
    show black with dissolve
    "Я решил промолчать и продолжить путь дальше."
    window hide
    
    $ renpy.pause (1, hard=True)

    show d4_catac_us_2 with dissolve2
    $ renpy.pause (1, hard=True)
    show cg d4_catac_us with dspr
    window show
    nd_il "Как думаешь, мы найдем Шурика?"
    us "Конечно найдём..."
    nd_il "Лишь бы нас никто сейчас не нашёл."
    nd_il "Знаешь же, в таких заброшенных зданиях могут проживать сектанты какие-нибудь."
    us "...Зато какое приключение!"
    nd_il "Не думаю. Мы же просто ищем Шурика."
    us "Опять ты как зануда."
    us "Хотя уже лучше, чем было в первый день твоего приезда."
    us "Видно, почувствовал себя как дома."
    "Сказала Ульяна веселым тоном. Я не смотрел на неё, потому о её настроении судил только по голосу."
    nd_il "В этом есть своя правда.{w} Может даже с тобой сейчас разыграем Шурика."
    nd_il "Скажем, что он тут двадцать лет просидел, и мы из двухтысячного года пришли, чтобы его найти."
    us "Ха-ха-ха-ха.{w} Точно.{w} Хорошо у тебя голова по части приколов варит..."
    window hide

    scene black with dissolve2

    window show
    "Я был рад присутствию Ульяны рядом с собой."
    "Мне было как-то спокойней, когда она рядом и поддерживает диалог своим позитивным настроением."
    "Не знаю.{w} Может, без неё, моя адаптация к лагерю шла бы больше недели."
    "Как она и сказала: \"почувствовал себя дома\"."
    window hide

    stop music fadeout 4

    $ renpy.pause (2, hard=True)

    scene bg int_mine with dissolve2

    play music ndm_list['White_Atlantis'] fadein 4

    window show
    "В процессе нашего продолжительного диалога я не заметил, как каменные стены сменились деревянными досками."
    nd_il "Всё хорошо?{w} Тебе не страшно?"
    us "Нет.{w} Пошли туда."
    us "Там точно должен быть Шурик."
    "Подбодрила меня Ульяна."
    "Я посмотрел в глубину этого коридора, и увидел через темноту развилку из двух путей. Мы с ней прибавили шаг..."
    window hide

    show int_mine_crossroad with dissolve

    window show
    "Мы дошли до развилки и остановились."
    "Понятно, что нам придётся выбирать один из этих путей.{w} Вопрос был в том, как не запутаться и не сойти с ума в случае, если мы будем ходить по кругу."
    "На этот и множество других случаев у Ульяны был охотничий нож."
    nd_il "У меня идея."
    us "Какая?"
    nd_il "Достань свой ножик и делай надрезы перед развилками."
    us "Так точно, капитан."
    "Сказала Ульяна, и достав из рюкзака ножик, вытащила его из чехла и сделала надрез на бревне."
    nd_il "Теперь нужна тактика.{w} Предлагаю поочерёдно выбирать пути - сначала налево, и потом направо."
    nd_il "Если, конечно, это не единственная развилка."
    us "Поняла."
    window hide

    stop ambience fadeout 3
    scene black with dissolve2

    $ renpy.pause (3, hard=True)

    play ambience ambience_catacombs fadein 5
    scene bg int_catacombs_door with dissolve2

    window show
    "Вскоре результаты дали о себе знать."
    "Мы с Ульяной пришли к какой-то металлической двери с красным вентилем и знаком радиации на ней."
    "В этом помещении с каждой секундой становилось более жутко. Мысли о том, что могло быть за той дверью пугали своей загадочностью."
    "Честно говоря, даже я был немного напуган, что уж говорить о девочке, сейчас крепко держащей меня за руку."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    us "Илья, можно я в лагерь обратно пойду?"
    nd_il "Серьезно? Мы же так много прошли.{w} К тому же если ты заблудишься то мне придется кроме Шурика ещё и тебя искать"
    us "Не волнуйся.{w} Я помню как мы шли."
    "Мне было как-то страшно отпускать её одну.{w} Даже если она помнит весь путь с поверхности досюда."
    "Чем может обернуться моё доверие ей?{w} А если она не выберется?"
    window hide

    menu:
        "Отпустить":
            
            $ nd_us_flaggs += 1

            window show
            nd_il "Хорошо, только это..."
            nd_il "Береги себя."

            show us smile pioneer at right with dspr
            
            us "Тебе не о чем волноваться."
            window hide

            $ renpy.pause(1)

            hide us with dspr

            window show
            "Я отдал Ульяне счётчик Гейгера и фонарик, но последний она не приняла."
            "Сказала что у неё есть свой."
            $ old_camp_sh_cheese = True
            "Я же попросил у неё пару пакет с печеньем на всякий случай."
            "Она отдала мне пакет с печеньем и направилась к выходу из шахт,{w} а мне ничего не оставалось, кроме как открыть эту железную дверь с вентилем, дабы продолжить свой путь ещё глубже."
            window hide

        "Не отпускать":

            $ old_camp_sh_cheese = False

            window show
            nd_il "Ульяна, я не могу тебя сейчас отпустить."
            nd_il "Тут может быть опасно.{w} К тому же если потеряешься ещё и ты..."
            
            show us normal pioneer at right with dspr
            
            us "Тебе не о чем волноваться, честно."
            nd_il "Я не могу сейчас рисковать, пойми."
            us "Вечно ты драматизируешь."
            us "Всё, давай, я пошла.{w} Фонарик у меня есть."
            window hide

            hide us with dspr
            $ renpy.pause(1)

            window show
            nd_il "Подожди."
            "Но ульяна уже скрылась в темноте глубокой деревянной шахты."
            th "Надеюсь она найдет выход."
            "Мне больше ничего не оставалось, кроме как открыть эту железную дверь с вентилем, дабы продолжить свой путь ещё глубже."
            window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_mines_metal
    $ renpy.pause(1, hard=True)
    scene bg int_mine_room with dissolve
    
    window show
    "Прокрутив вентиль и открыв дверь меня встретила какая-то комната с трубами, вентилями, и \"приятными\" словами на бетонной стене."
    th "\"Ленка - дура\". Интересно, о Лене из нашего отряда на этой стене идет речь?{w} Если она читает книги то навряд ли её можно считать дурой.{w} Скорее здесь речь вообще о другой смене."
    th "Господи, да на кой мне эта надпись сдалась."
    th "Боже, ну и запах здесь.{w} Вонища.{w} Не иначе, как скунс сдох..."
    th "Так, погодите... Там в углу комнаты что-то есть!{w} И это что-то громко и зловеще дышит!"
    "В углу этой комнаты сидел кто-то, кто был похож на свернувшуюся калачиком спящую собаку."
    "Аккуратно наведя на силуэт фонариком, тем самым рассеяв тьму, это что-то мгновенно дернулось, от чего я невольно вздрогнул."
    stop music fadeout 3
    "Теперь силуэт собаки превратился в Шурика, жующего пальцы."
    window hide

    show cg d4_sh_sit with dissolve2

    $ renpy.pause(1)

    window show
    nd_il "Господи..."
    "Разглядев меня он бросил свой оскал и завопил."
    sh "Не надо! Я не могу больше ходить по этим развилка-а-ам!"
    "Его крик отразился от стен этой комнаты эхом, надавив на мои ушные барабанные перепонки."
    th "Господи, не кричи так..."
    nd_il "Шурик, это я, Илья.{w} Помнишь ты мне зарядник делал?"
    "Но Шурик не ответил."
    window hide

    play music ndm_list['nd_fighting_withsh'] fadein 3
    scene black with dissolve
    scene bg int_mine_room with dissolve

    window show
    "Он зарычал на меня как собака, и встав с колен бросился на меня, опираясь на стену одной рукой."
    "Он медленно полз по стенке но мне. Мне нужно было быстро выбирать пути борьбы за свою жизнь."
    window hide

    menu:
    
        "Попробовать напугать":
            $ nd_stoic += 1

            with hpunch
            window show
            nd_il "А-а-а!"
            "Я неистово закричал на Шурика.{w} Он слегка опешил и упал на бетонный пол,{w} но спустя пару секунд пополз ко мне, набирая скорость."
            "И здесь я уже не знал что делать. Был вариант отпнуть его ногой. Но вдруг он это вспомнит?"
            "Хотя если бы от этого зависела моя жизнь..."
            window hide

        "Ждать":
            $ nd_scept += 1

            window show
            "Я решил ждать нападения Шурика, забившись в угол, чтобы потом попытаться контратаковать его, если он нападёт."
            window hide

        "Кинуть печенье" if old_camp_sh_cheese == True:
            $ nd_stoic += 1

            window show        
            "Я кинул ему несколько печенек, которые замедлили его на секунду..."
            th "Черт его возьми, и что мне делать?"
            "...но после съедения этого злакового лакомства он, хромая на одну ногу, отправился ко мне с каким-то куском арматуры в руке."
            window hide

    $ renpy.pause(1, hard=True)

    show cg d4_sh_stay with vpunch
    stop ambience fadeout 6
    $ renpy.pause(1, hard=True)
    show black with flash
    $ renpy.pause(2, hard=True)

    scene bg int_mine_room with dissolve2
    
    window show
    "Я уже был готов увернутся от его удара, как дверь открылась, сшибив с ног несчастного Шурика."
    "Тот рефлекторно отскочил к стенке, и бросив ломик убежал куда глаза глядят, крича что-то нечленораздельное."
    window hide

    stop music fadeout 6
    play ambience ambience_catacombs fadein 5

    $ renpy.pause(1, hard=True)
    show us normal pioneer at left with dspr
    

    window show
    "Из двери вышла Ульяна."
    us "Что случилось? Я кого-то убила?"
    nd_il "Спасла. От Шурика."
    "Сказал я с улыбкой."
    us "Ты его нашёл?"
    nd_il "Да, но он меня чуть не ударил и убежал в ту дверь."
    "Сказал я и указал на выход из комнаты пальцем."
    
    play music ndm_list['nd_fighting_withsh'] fadein 3
    show sh rage far at right with dspr
    show us fear pioneer at left with dspr

    "В этот момент оттуда опять выскочил Шурик, рыча и завывая."
    us "Аа-а!"
    "Закричала Ульяна. Её крик отразился от бетонных стен, создав внутри комнаты высокочастотное эхо."
    hide us with dspr
    "Она спряталась ко мне за спину."
    th "Господи, Шурик, как тебя жизнь потрепала.{w} Голодный наверное."
    us "Сделай что-нибудь, дурак!{w} Он нас съест сейчас!"

    if old_camp_sh_cheese == True:
        "Я вытащил из кармана несколько печенек из пакета с печеньем, и кинул Шурику."
    else:
        nd_il "Ульяна, кинь ему печеньев."
        nd_il "Вдруг поест и успокоится."
        show us normal pioneer at left with dspr
        us "Хорошо..."
        "Ульяна достала из своего рюкзачка печенье и кинула рядом с Шуриком на пол."

    hide sh with dspr

    "Тот поднял их с пола своими руками, сгрыз их и бросился наутёк с места преступления."
    window hide

    stop music fadeout 5
    $ renpy.pause(1, hard=True)

    window show
    th "Ты не ты, когда голоден…"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    us "Что это с ним?"
    nd_il "Понятия не имею.{w} Одичал наверное за всё время пребывания в этом старом лагере."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    us "Я тут пока выйти пыталась, какую-то дверь нашла железную, посмотри."
    "После короткой паузы сказала Ульяна,{w} и повела меня в комнату, из которой только что вышла."
    window hide

    show black with dissolve2
    $ renpy.pause(1, hard=True)
    scene bg int_catacombs_door with dissolve

    window show
    "Там и вправду была железная дверь, на которой был нарисован знак радиации и огромный вентиль, открывающий её."
    "Она очень была похожа на ту, что я видел в начале своего пути по этим катакомбам. Что бы это могло значить."
    "Но на этой синяя краска уже облезала, скорее всего из-за сырости.."
    nd_il "Давай откроем её."
    "Сказал я, потёр руки и принялся за дело."
    "Вентиль никак не хотел поддаваться, поэтому я попросил помощи у Ульяны."
    "Правда помощь Ульяны в этом деле хоть и казалась поначалу бесполезной..."
    window hide    

    scene black with dissolve
    $ renpy.pause(2, hard=True)
    play sound sfx_open_door_mines_metal
    $ renpy.pause(1, hard=True)
    show int_catacombs_living_dark with dissolve
    $ renpy.pause(1, hard=True)
    window show
    "...Но нам все же удалось провернуть вентиль и дверь с металлическим скрипом открылась, показав нам темноту, через которую едва можно было заметить очертания комнаты."
    window hide

    $ renpy.pause(1, hard=True)
    
    play sound nds_list['nd_light_tumbler_on']

    scene black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg int_catacombs_living with dissolve

    $ renpy.pause(1, hard=True)

    window show
    "Нащупав за дверью переключатель и включив его, лампочки загорелись и осветили помещение желтоватым светом."
    "Знак радиации на двери свидетельствовал о том, что это, скорее всего, бомбоубежище, которое использовалось ещё во время второй мировой."
    "У стены стояли металлические шкафчики, в которых должна была храниться одежда."
    "Одна двухъярусная кровать, на которой жильцы этого убежища должны были спать."
    "Шкаф, стоящий в углу, на полках которого были разные коробки, электроприборы и железные ящики."
    "На столе стояло радио, устройство, своим видом напоминающее микроволновку или старый телевизор, и разные провода."
    "Такие места навевают ужас."
    us "Это бомбоубежище."
    "Заметила Ульяна, и мы стали оглядывать помещение."
    window hide

    $ renpy.pause(2, hard=True)

    show us normal pioneer at right with dspr

    window show
    us "Интересно, сколько всему этому лет?"
    nd_il "Думаю не более пятидесяти."
    
    hide us with dspr
    show us surp1 pioneer far at center with dspr
    
    us "Смотри! Радио."
    nd_il "Я бы тут ничего не трогал."
    show us normal pioneer far at center with dspr
    us "Да ладно тебе. Тут же никого кроме нас нет."
    nd_il "Для своей же безопасности..."
    window hide

    $ renpy.pause(2, hard=True)
    hide us with dspr

    window show
    "Вскоре в глаза начал бросаться старый ковёр на стене."
    "Попытавшись облокотиться на него я заметил, что за ним пустота."
    nd_il "Там тайный проход за ковром."
    us "Дай посмотреть."
    "Ульяна оттолкнула меня, и сняла ковёр.{w} Я посветил фонариком в новое помещение и оглядел его."
    window hide

    stop ambience fadeout 5

    scene black with dissolve
    $ renpy.pause(2, hard=True)

    window show
    "Справа была какая-то пещера, заваленная камнями. Сверху светил какой-то яркий свет, напоминающий лунный."
    "В дальнем углу что-то зашуршало."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Стоять не рыпаца!{w} Выходите с поднятыми руками!"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_da "Ну вот, мышь спугнул."
    nd_da "Нельзя ли хоть раз встретить меня без кривляний?"
    nd_il "Даша? Это ты?"
    nd_da "Я,{w} наверное."
    window hide

    play music ndm_list['escape'] fadein 4

    show black with dissolve2
    
    "Посветив на неё, я разглядел вчерашнюю девушку, вышедшую из-за кустов."
    window hide

    $ renpy.pause(1, hard=True)

    show black with dissolve 

    $ renpy.pause(1, hard=True)

    window show
    us "Девочка-енот!"
    "Закричала Ульяна, подбежала к девушке и погладила её."
    us "Оказывается это не легенда."
    "Я не знал, о какой легенде говорит Ульяна. Тем не менее, мне нужно было многое узнать у Даши."
    nd_il "Даш, у меня есть много вопросов, которые я хочу тебе задать."
    "Меня абсолютно не удивляло то, что я сейчас вижу, так как вся энергия была потрачена на Ульяну и развилки."
    "И на сражение с этим поехавшим за время, проведенное тут, кибернетиком."
    window hide

    scene black with dissolve2

    $ renpy.pause(1, hard=True)

    scene bg int_mine_exit_light
    show da smile at center 
    with dissolve2

    window show
    nd_da "Задавай любые вопросы, которые тебя интересуют.{w} На все я тебе, конечно, ответить не смогу."
    nd_il "Для начала мне интересно, кто ты такая?"
    nd_da "Можешь считать меня хранительницей этого лагеря.{w} Я слежу за порядком в лагере и охраняю это место и его обитателей…"
    nd_da "И да, ты верно знаешь кем я тебе приходилась раньше."
    "Я почему-то не был уверен последней реплике девочки-енота. Она звучала подозрительно, но вместе с тем тепло."
    "Придав этому значение, я решил плавно изменить тему."
    nd_il "Хорошо. Вот ещё вопрос. Сегодня утром Шурик дал мне записку, в которой было написано о встрече у пристани. А потом, когда я её прочёл она превратилась в песок."
    nd_il "Это ты мне писала?"

    show da normal at center with dspr

    nd_da "Нет, я не знаю кто тебе писал эту записку. Но помни, что это ни к чему хорошему не приведёт…"
    "Ульяна также продолжала разглядывать девушку-енота."
    nd_il "Понятно, а к чему оно может привести?"
    nd_da "Я точно не знаю, но моё чувство подсказывает, что что-то плохое уже случилось, и может быть ещё хуже."
    nd_il "Это из-за того, что я остался в лагере?"
    nd_da "Не знаю. Такое чувство у меня было и до твоего появления здесь."
    nd_da "Отчасти, благодаря мне ты попал в этот лагерь…"
    th "Точно. А как же я попал сюда?"
    nd_il "Даша, а как я сюда попал?{w} Что случилось в тот момент, когда я..."
    nd_da "Илья, я не могу тебе больше отвечать.{w} Мне нужно идти."
    nd_da "Но помни, я буду защищать тебя и следить за тобой в лагере. Главное не разводи панику и ничего не бойся."
    nd_il "Хорошо…"
    nd_da "Ульяна, отойди пожалуйста."
    "Ульяна послушно отошла от девушки."
    window hide

    $ renpy.pause(1, hard=True)

    show blink

    $ renpy.pause(1, hard=True)
    hide da
    hide blink
    show unblink

    window show
    "И только я смел моргнуть, та магическим образом исчезла."
    nd_il "Как она так быстро исчезла?"
    us "Ты её знаешь?"
    "Сказала Ульяна, повернувшись ко мне."
    nd_il "Да... Она вчера предложила мне либо остаться, либо уйти из лагеря."
    nd_il "Как видишь, я тут."
    us "...А почему ты остался в лагере?.."
    "Вдумчиво произнесла она.{w} Я решил ей незамедлительно ответить что-либо, что могло бы отсрочить мой ответ на вопрос, который я сам точно ещё не знал."
    nd_il "Возможно, скоро ты сама это поймёшь."
    "Впрочем, как это вскоре должен был понять и я."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Было принято решение осмотреть помещение, в котором мы находимся."
    "Похоже, это было что-то вроде котельной этого самого бункера, по совместительству конечной его комнатой."
    "Конечной, потому что выхода в другие комнаты отсюда уже не было, но был лунный свет, пробивающийся из-за какого-то решетчатого предмета наверху."
    "Его тень отражалась на стене этого помещения."
    window hide

    scene bg int_mine_exit_night_light with dissolve
    
    window show
    "Заметив лестницу наверх и решётку, я приподнял её и полез на свежий воздух.{w} Ульяна молча проследовала за мной."
    window hide

    scene bg int_mine_exit_night_nolight with dissolve2
    stop music fadeout 3
    stop ambience fadeout 3
    show black with dissolve2 

    window show
    th "Так всё-таки, почему именно благодаря ей я попал сюда?"
    th "Вчера она мне сказала, что это лагерь захотел, чтобы я оказался тут."
    th "Это очередной раз доказывает что она хранительница этого лагеря..."
    window hide

    $ renpy.pause(1, hard=True)

    play ambience nda_list['ambience_forest_nd_night'] fadein 3
    scene bg ext_path_night with dissolve2

    $ renpy.pause(1, hard=True)

    window show
    th "А ведь я просто одним вечером сел в автобус и уснул..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Внезапно сзади меня кто-то сильно ударил по плечу."
    show pi smile at center with dissolve
    "Я повернулся, и увидел какого-то пионера, сильно напоминающего мне моё отражение в зеркале."
    "Словно передо мной стояла моя копия."
    "Его чёлка закрывала глаза, и я не мог их разглядеть."
    "На его лице была ехидная ухмылка, которую невозможно ни с чем сравнить."
    "Меня охватило первобытное чувство тревоги."
    play music ndm_list['nd_fuckyou_music'] fadein 6
    pi "Привет, Илья."
    show us normal pioneer close at fleft with dspr
    us "Илья, кто это?"
    nd_il "Кто ты? И откуда ты знаешь моё имя?"
    pi "Как вижу, ты выбрал поход по жуткому старому лагерю вместо тёплой беседы со своим старым другом."
    "Пионер абсолютно проигнорировал мой вопрос, сохраняя свою безумную ухмылку."
    hide us with dspr
    nd_il "Какая тебе разница, что я выбрал? Разве это не моя жизнь, которой я вправе распоряжаться сам?"
    "Дерзко спросил я, закрывая Ульяну рукой."
    window hide

    show pi smile with dissolve

    window show
    "Пионер залился истерическим смехом."
    "Этот смех эхом отозвался внутри моей головы."
    pi "Она тебе уже промыла мозги своими выборами, не так ли? Можешь не отвечать."
    pi "Я знаю о тебе больше, чем ты сам."
    "Сказал пионер, а затем взглянул на Ульяну за моей спиной."
    window hide

    $ renpy.pause(1, hard=True)

    show pi with dissolve

    window show
    pi "А твоя девчушка должна идти, она мешает нам разговаривать."
    nd_il "Я не собираюсь продолжать диалог с сумасшедшим!"
    "Сказал я грубым тоном."
    pi "Ты меня, кажется, не услышал."
    pi "Убери свою девочку, и ничего плохого с ней не случится."
    window hide

    $ renpy.pause(1, hard=True)

    show us normal pioneer at fleft with dspr

    window show
    us "Ладно, у меня кажется дела, я пойду."
    hide us with dspr
    "Сказала Ульяна и поспешно удалилась, оставив нас с этим пионером наедине."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "А теперь напомни, пожалуйста, зачем ты здесь?"
    pi "Ты, наверное, ещё не понял, что попал в этот лагерь по чистой случайности."
    show pi smile with dspr
    pi "Гляди, даже девушку себе нашёл. Было бы у тебя так же в реальной жизни..."
    pi "Правда ей даже шестнадцати нет..."
    pi "Но это и не важно.{w} Ведь она не больше, чем просто марионетка, шестерёнка всего механизма лагеря и твоего восприятия к нему."
    pi "Видел бы ты себя со стороны, когда спасал её из воды."
    
    hide pi with dspr
    "Пионер снова захохотал.{w} Его голос приобрёл более низкий и в то же время жуткий тон."
    show pi smile with dspr
    pi "Не обращай внимания.{w} Я просто решил повеселиться тогда."
    pi "Признаться, у меня бы всё получилось, если бы ты не успел её вытащить из воды."
    hide pi with dspr
    "Он снова захохотал.{w} С каждой секундой в этом лесу наедине с ним мне становилось не по себе."
    nd_il "Это ты сделал?!{w} Кто ты такой?!{w} Что тебе от меня нужно?!"
    show pi smile with dspr
    pi "Не торопи события.{w} Я тебе не враг, и честно говоря даже не друг."
    pi "Я просто хочу помочь тебе в твоём выборе. Ты должен уходить из этого лагеря, и если не сейчас, то никогда."
    nd_il "Почему? Я же должен уехать со всеми пионерами…"
    pi "Да, ты уедешь с пионерами, начнёшь новую жизнь… Но вот только ты не учёл одного факта, ты — не пионер, и даже не гражданин этой страны."
    pi "Всё, что ты здесь делаешь, это просто существуешь, дружишь с пионерами, с Ульяной."
    pi "А представь, что она просто кукла, манекен, программа, код. Воспринимай как угодно.{w} И с каждым твоим влиянием в этом мире части кода просто стираются."
    pi "И если ты не хочешь, чтобы весь этот лагерь начал отсчёт до конца своего существования, то тебе следует уехать отсюда как можно быстрее."
    pi "Если захочешь, то автобус будет ждать тебя на остановке этим вечером."
    nd_il "Пионеры в этом лагере не манекены!{w} Так мне сказала Даша.{w} Я не верю твоим бредням!"
    pi "Придётся поверить,{w} дружок.{w} Неужели ты нашёл логичное объяснение твоему попаданию сюда?"
    pi "Сомневаюсь. Так что лучший выход для тебя сейчас - воспользоваться последним шансом и уехать."
    pi "Автобус будет ждать тебя."
    pi "Ты успеешь попрощаться со всеми."
    nd_il "Я никуда не уйду из этого лагеря."
    
    hide pi smile
    show pi normal
    with dspr
    
    "Лицо пионера изменилось."
    nd_il "Можешь сам собираться и уходить, если тебе не нравится моё присутствие в нём."
    pi "А ведь я думал, что мы взрослые люди и сможем договориться нормально."
    window hide
    $ renpy.pause(1, hard=True)

    scene black with dissolve
    show cg nd_pioneer_d4 with flash

    window show
    pi "Ты действительно хочешь остаться в этом лагере?{w} Так уж и быть."
    pi "Но тогда тебе придется занять место одного из пионеров, чтобы ты стал полноценной ячейкой советского общества."
    pi "Понимаешь о чем я?"
    nd_il "Не совсем..."
    pi "Тогда давай я лучше тебе покажу."
    "Достав из штанов нож, пионер лезвием вверх протянул его мне."
    pi "Убей самого дорогого тебе человека в этом лагере, и можешь оставаться сколько хочешь."
    window hide

    stop music fadeout 3

    scene black with dissolve

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Да пошёл ты!"
    window hide

    $ renpy.pause(1, hard=True)

    play music ndm_list['nd_losing_you'] fadein 3
    scene bg ext_path_night with dissolve
    show pi smile with dspr

    window show
    pi "Ай-ай-ай. А я думал мы договоримся мирно."
    "Сказал пионер и выпрямил руку с ножом, надеясь проткнуть меня."
    "Я быстро отскочил от ножа, но в меня уже летел железный кулак его второй руки."
    window hide

    play sound sfx_lena_hits_alisa
    hide pi with flash

    window show
    "Удар пришёлся мне в живот."
    window hide
    
    stop sound fadeout 3
    

    show pi smile with dspr
    $ renpy.pause(1, hard=True)
    play sound sfx_thunder_rumble
    hide pi smile
    show pi eyelight at center 
    with flash

    window show
    "В этот момент сверкнула молния. Пионер сделался полностью тёмным, а глаза его наполнились синим словно от флюоресцентной лампы светом."
    "Но скорее это было синее пламя, явно намекающее на то, что я вряд ли останусь живым после этого рандеву."

    stop sound fadeout 3

    "Я лежал на холодной траве, прижимая сделанную им рану рукой."
    pi "Тогда тебе не жить..."
    with hpunch
    play sound sfx_lena_hits_alisa
    "Он ударил меня по челюсти и прижал свою руку к моему горлу так, чтобы я не мог кричать."
    "Я хотел его ударить, но мои руки и ноги полностью отказывались меня слушаться."
    window hide

    $ renpy.pause(1, hard=True)
    
    play sound sfx_hiding_in_bush
    show da angry at right behind pi with dspr
    
    $ renpy.pause(1, hard=True)

    hide pi eyelight
    hide da
    with dspr
    play sound sfx_bush_body_fall

label new_scenario_d4_end:

    window show 
    "Но внезапно из кустов выскочила Даша, и с животным криком набросилась на пионера."
    nd_da "Беги-и..."
    "Сидя у него на спине, она стала царапать его и кусать, тем самым отодвигаясь глубоко в лес."
    window hide

    play sound sfx_hiding_in_bush
    show us sad pioneer at center with dspr

    window show
    "Из кустов в тот же момент выбежала Ульянка, держа в руках свой охотничий нож.{w} Вид у нее был такой, что сердце от чего то защемило."
    us "Илья?{w} Ты в порядке?"
    "Говорила она это с трудом."
    us "Он хотел тебя...{w}{cps=8} Убить?!{/cps}"
    "Я был настолько в растерянности что лишь сумел вымолвить."
    nd_il "Не..."

    show us angry pioneer at center with dspr

    us "Дурак! А если бы он убил тебя?!"
    show us cry2 pioneer at center with dspr
    us "Дурак! А если бы он убил тебя?!{fast} Что бы я делала?"

    hide us with dspr

    "Ульяна едва не плача выронила из рук нож, чуть не упав на землю весь мир остановился в этот момент..."
    "Не думая ни секунды я кинулся к ней, взяв ее за плечи придерживая поставил обратно, попутно подобрав нож."
    
    show us shy pioneer at center with dspr

    us "{cps=20}Извини, пожалуйста, я...{/cps}"
    
    hide us with dspr

    "Она не успела договорить, ее робкий монолог прервали вопли из леса."
    pi "Уберите!{w} УБЕРИТЕ!"
    "Судя по звуку с истошного крика который переходил в истерику."
    "Я не знал что в такой ситуации делать. Определенно нужно было уводить отсюда Ульяну, заодно и свои ноги."
    "Взглянув на неё, через секунду я вынес предложение..."
    show us sad pioneer at center with dspr
    nd_il "Надо отсюда уходить, я бы даже сказал бежать."
    "Ульяна до сих пор была немного в прострации, но уже реагировала на мои действия."
    us "Побежали."
    "Взяв Ульяну за руку мы с ней побежали по направлению в лагерь."
    window hide

    stop ambience fadeout 4
    stop music fadeout 6
    show black with dissolve2
    
    window show
    "Бежать пришлось не очень далеко, вскоре мы увидели ограду лагеря, в которой было отверстие."
    "Ульяна полезла под забором.{w} Я же на сколько это возможно было спешно перескочил через него."
    window hide

    $ renpy.pause(2, hard=True)

    play ambience ambience_camp_center_night fadein 3
    scene bg ext_square_night with dissolve2

    window show
    "Спустя некоторое время бега, мы с Ульяной, минуя любые ворота, ведущие в лагерь."
    "Вот он - прилив адреналина.{w} И не верится, что я только что мог попрощаться со своей жизнью."
    "А появление на площади было мимолётным, словно между перемещением с тропинки в лесу прошло несколько секунд."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Сев на одну из лавок, мы с моей напарницей смогли спокойно отдышаться."
    "Я даже не думал, что могу так быстро бегать. Даже за Ульяной успел."
    "Впрочем на то возможно повлиял не один фактор, так что останавливать на этом внимания я не хотел."
    nd_il "Фу-ух, ну и вечер…"
    "Адреналин давал о себе знать ранее, но с падением его уровня мысли стали приобретать многовекторность мышления."
    th "А что же с Дашей? С ней всё в порядке?"
    "Подумав об этом, меня по неволе бросило в дрожь."
    th "Должно...{w} Я не верю.{w} Я... трус? Так?"
    "Мысли метались в голове со скоростью метеора."
    "Возможно такими самокопаниями я бы себя заставил прямо сейчас в одиночку бежать обратно но..."
    us "Это...{w} Точно..."
    "С немного надломленным голосом вымолвила Ульяна."

    show us sad pioneer at left with dspr 
    
    "...Переведя взгляд на неё, я заметил на щеке что-то влажное, поблёскивающее от лунного света."
    "Казалось, ещё немного, и она заплачет."
    window hide

    $ renpy.pause(1, hard=True)

    play music ndm_list['piano3'] fadein 4

    window show
    th "Нет, нет, нет, этого не должно быть, ни за что."
    "Я не понимал, что это за чувство, хотя, возможно, сам себя обманывал."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr

    window show
    "В ту же секунду не говоря ничего, я обнял это красноволосое, неуёмное, вечно позитивное чудо, которое сейчас в этом нуждалось."
    "Она молча уткнулась мне в плечо и зарыдала."
    "В этой ситуации мои руки сами потянулись к ее макушке, но я унял себя, опустив вторую руку обратно на скамейку."
    nd_il "Всё хорошо, Уль, мы здесь в безопасности."
    "Впервые на моей памяти я произнес уменьшительно-ласкательную форму этого имени по отношению к этой девочке."
    "Сейчас я никак не хотел её выпускать из своих объятий."
    "Она всегда была сильной, жизнерадостной, весёлой, и я хочу что бы она оставалась такой."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Что же это?"
    th "Неужели я так привязался к ней?"
    th "Ранее я презирал такие действия и мысли в целом.{w} Скорее потому что никогда не испытывал их по настоящему?.."
    th "На этот вопрос я не мог найти ответа,{w} или пока не мог."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Мое плечо чувствовало тёплую влагу от слёз девушки."
    "В то время, как она видимо начала успокаиваться, но отпускать меня видимо не хотела."
    "Поскольку только сильнее сжала объятия..."
    nd_il "Всё, будет хорошо, обещаю."
    nd_il "Всё в порядке, я здесь."
    "Сам не ведал того что говорил, но говорил я это с чувством, что делаю что-то правильно."
    "Возможно впервые за долгое время."
    window hide

    $ renpy.pause(2, hard=True)
    show us sad pioneer at left with dspr


    window show
    "Ульяна разжала объятия и мы перенесли взгляд друг на друга."
    "В её глазах можно было утонуть."
    "Они были словно два океана, в которых недавно прошёл шторм, но штиль ещё не наступил."
    stop music fadeout 4
    "Они притягивали и тянули в себя, правда, ранее я не верил, что сетчатка глаза простого человека может выражать подобные эмоции."


    if nepodhod_87 == False and nd_us_flaggs >= 1:
        "Но сейчас я явно видел в них надежду,{w} доверие,{w} и...{w} Что-то ещё?"
        us "Спасибо тебе...{w} Большое...{w} За всё..."
        "Сказала она с расстановкой, медленно-медленно, глядя прямо в душу."
        window hide

        $ renpy.pause(1, hard=True)

        hide us with dspr

        play sound ndm_list["kossandra_part_1"] fadein 4

        window show
        "Я ничего не ответил, просто опустил голову вниз, чувствуя вину за всё, что происходит сейчас..."
        th "Ульяна, ты не понимаешь, что во всём виноват я."
        th "Что я просто трус и обманщик.{w} Что тем, что остался в лагере, подверг опасности тебя и себя..."
        "Я сделал глубокий вдох и прерывисто выдохнул.{w} Я знал, что уже сделанное никак не исправить."
        stop sound fadeout 4
        nd_il "Прости..."
        window hide

        stop ambience fadeout 3
        show blink

        window show
        "И только я прикрыл глаза, как тут же почувствовал, как Ульяна пододвинулась ко мне ближе и..."
        window hide

        $ renpy.pause(2, hard=True)
        play music ndm_list["kossandra_part_2"] fadein 2
        $ renpy.pause(2, hard=True)

        show cg nd_unbelievable_art:
            xalign 0.6 yalign 0.4 zoom 1.5 rotate 4.0
            ease 6.5 zoom 1.0 xalign 0.5 yalign 0.5 rotate 0.0

        with flash

        $ renpy.pause(20, hard=True)

        show black with dissolve3

        window show
        "...И поцеловала меня в мою щеку..."
        window hide
        
        hide us

        $ renpy.pause(1, hard=True)

        hide blink
        scene bg ext_square_night
        show unblink


        window show
        "Я на секунду впал в ступор."
        "Мысли сами шли в голову и останавливались на моем языке..."
        show us shy pioneer at left with dspr
        nd_il "Тебе спасибо но...{w} Благодарить тут должен только я тебя."
        nd_il "Я никогда ничего подобного не испытывал и всегда был абсолютно забитым в себе человеком."
        nd_il "Уже давно, до приезда в лагерь."
        "Лучше уж пусть сейчас, ведь рано или поздно...{w} А может лучше оставить всё как есть?"
        show us shy2 pioneer at left with dspr
    
    else:

        stop music fadeout 3

        hide us with dspr
        "Мы молча сидели и...{w} Ульяна отвернула от меня взгляд и посмотрела на асфальт."
        nd_il "Знаешь, я всегда был абсолютно забитым в себе человеком."
        nd_il "Уже давно, до приезда в лагерь."
        "Лучше уж пусть сейчас, ведь рано или поздно...{w} А может лучше оставить всё как есть?"
        play music ndm_list['piano3'] fadein 4
    

    nd_il "Ни с кем не общался, сидел за...{w} Своим рабочим местом, делал...{w} Какую никакую работу...{w} За что получал деньги."
    "Она внимательно меня слушала, уже приобретя заинтересованный взгляд."
    "На душе даже теплее стало."
    nd_il "С своими сверстниками или же другими людьми...{w} В живую..."
    "Я замер, в попытках подобрать нужные слова, дабы продолжить свою мысль."
    nd_il "...Гулял, общался так давно, что себя и не помню."
    nd_il "Последние года так три, точно сидел безвылазно,{w} и ничего не делал,{w} всё больше погружаясь в уныние."
    "Моё лицо уж приобрело грустноватый вид, я вспомнил свой мир и себя и уже наверняка, я понимал, что не хочу обратно."
    "Что же этот лагерь со мной сделал?"
    window hide
    
    $ renpy.pause(2, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)
    
    window show
    "Уже несколько секунд я молчал, мы оба молчали, но внезапно Ульяна нарушила это молчание."
    show us shy pioneer at left with dspr
    us "П... Правда?"
    "Её тон был таким, словно я ей рассказал о зверствах режима, который описывали в моём понимании современные \"эксперты\"."
    "Я лишь молча кивнул головой, которую не спешил поднимать."
    "Вместе с тем мне не верилось, что Ульяна может быть не настоящей. Этот пионер мне определенно врал."
    "Я так надеялся, что больше его не увижу..."
    nd_il "Спасибо, что выслушиваешь это..."
    "Проглотив, произнес я."
    "Сначала я даже не думал, что с Ульяной мы сможем как-то поговорить.{w} Но пришлось."
    "И сейчас я видел в ней человека, который понимает всё, что я говорю, и сожалеет мне."
    "Это было понятно по её мучительному молчанию."
    window hide

    hide us with dissolve
    stop music fadeout 3
    play ambience ambience_camp_center_night fadein 3
    $ renpy.pause(3, hard=True)

    window show
    "Возможно, это могло продолжаться ещё целую вечность, но просидев так пару минут, со стороны соседней лавочки мы услышали какое то шуршание."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Оказалось, что это был спящий Шурик."
    show us surp3 pioneer at left with dspr
    us "Ой..."
    hide us with dspr
    "Мы с Ульяной переглянулись, видимо она уже была в своём привычном настроении, что поднимало таковое и мне."
    "Мы уже хотели встать и подойти поближе, как данный организм ворча принял сидячее положение и начал оглядываться."
    "Ульяна это увидела и немного надулась, и это показалось мне очень милым."
    "Тем временем, данный субъект, увидав нас, встал и направился к нам."
    show us normal pioneer at left with dspr
    show sh scared pioneer far at right with dspr
    us "О, проснулся.{w} Ты зачем в старом лагере на нас рычал?"
    "Тут же припомнила ему это Ульяна."
    sh "Ульяна, ты о чём вообще? И почему у меня болит голова?"
    "Я нервно про себя чуть ли не засмеялся вспомнив как в эту самую головушку прилетела дверь от Ульяны."
    "Видимо не один я так посчитал, я заметил на лице Ульяны короткую улыбку."
    "Но Ульяна не хотела отступать."
    show us dontlike pioneer at left with dspr
    us "Ты нас съесть хотел в старом лагере. Не помнишь?"
    show sh normal pioneer far at right with dspr
    sh "Я... Я вообще не помню, что произошло."
    sh "Помню шахту, потом силуэт какой-то. Я подошёл к нему, а дальше всё.{w} Провал в памяти."
    th "Даша? Или мы?"
    th "Я опять о ней задумался."
    th "Интересно, что с ней?{w} Она меня спасла,{w} а я?"
    "Не успел я продолжить мысль, как светило советской науки вывело умозаключение."
    
    show sh scared pioneer far at right
    show us normal pioneer at left 
    with dspr

    sh "И вообще это всё не научно.{w} Не{w} на{w}у{w}чно!"
    window hide

    $ renpy.pause(2, hard=True)

    hide sh with dspr
    
    window show
    "Шурик почесал голову, и отправился куда-то, немного похрамывая на ногу."
    nd_il "Зато мы его спасли."
    "Перестроил как внешний, так и внутренний диалог я."
    "Тут же болью отдала рана, видимо он всё-таки знатно меня саданул.{w} Ух..."
    "Постарался не подать виду я, когда адреналин и эмоции ушли, пришла боль."
    us "Интересно, а мне дадут такой же значок, как у тебя?"
    show us surp2 pioneer at left with dspr
    us "Ой, а где он?"
    "Я пощупал то место, где должен быть значок, но его там не оказалось."
    th "Странно, возможно в пылу боя с Шуриком или пионером. И даже значения этому не придал..."
    th "Да и катись оно к чёрту."
    show us normal pioneer at left with dspr
    nd_il "Кажется в старом лагере потерял."
    "Привёл более спокойное умозаключение я."
    "Ульяна видимо что то обдумывала, смотря то на меня, то на домики."
    window hide

    hide us with dspr
    $ renpy.pause(2, hard=True)

    window show
    "Опять минута тишины.{w} Я задумался оглядывая свою форму."
    th "Так, на значок всё равно, но форме - почти кирдык."
    th "Ну конечно спасти ее можно но это дело долгое и муторное настолько, что уж я переоденусь в новую, а старую спрячу где-нибудь в лесу."
    "Осмотрев себя ещё раз сделал умозаключение я."
    "И сразу же понял, что неплохо было бы мне помыться.{w} Да и день всё-таки не очень задался."
    show us normal pioneer at center with dspr
    nd_il "Уль, а где тут обмыться можно? Ну кроме речки."
    nd_il "Не горю желанием идти на пляж. А вот душ был бы в самый раз."
    "Ульяна непонимающе взглянула на меня."
    us "Не доходя до здания администрации есть душевые."
    show us surp2 pioneer at center with dspr
    us "А ты, что, не знал что ли?"
    "В этот момент я почувствовал себя каким-то экспонатом в музее."
    "Или будто я в лагере месяц, и должен все вокруг знать."
    nd_il "Не знал, конечно."
    nd_il "А должен."
    show us smile pioneer at center with dspr
    us "Обязан."
    us "Иди в душ, а я побегу до вожатой, расскажу ей всё."
    nd_il "Хорошо."
    window hide

    hide us with dspr
    $ renpy.pause(2, hard=True)

    window show
    "Я развернулся и было хотел сделать первый шаг на пути к умывальникам, но вспомнил за нож, который мне давала Ульяна."
    "Однако не помнил, куда я его положил."
    th "Возможно в карманах..."
    "Подумал я, и нащупал этот самый складной нож в шортах, не имея представления о том, как он там оказался."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я окрикнул уходящую вдали Ульяну."
    window hide

    $ renpy.pause(1, hard=True)
    show us normal pioneer far at center with dspr
    $ renpy.pause(1, hard=True)
    show us normal pioneer at center with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Та остановилась, подошла ко мне и забрала свой нож, быстро положив его в сумку."
    nd_il "Кстати, может уже поздно? Вожатая наверняка спит уже, десятый сон видит..."
    "Она немного удивилась,{w} её глаза забегали."
    show us sad pioneer at center with dspr
    us "Ну может быть, но проверить надо. Она же волнуется за нас."
    "В этом я не мог с ней не согласиться."
    nd_il "Ладно, будь тогда аккуратнее."
    hide us with dspr
    "Ульяна кивнула головой и продолжила свой путь до домика вожатой."
    "А в моих планах было взять полотенца, и пойти наконец помыться."
    "Нужно было найти полотенца, свои умывальные принадлежности и мочалку.{w} И по идее, все это было у меня в домике в пакете со всеми умывальными принадлежностями."
    "Туда-то мне и предстояло сейчас отправиться."
    window hide
    
    $ renpy.pause(1, hard=True)
    
    stop ambience fadeout 3
    show black with dissolve2
    $ renpy.pause(3, hard=True)

    play sound sfx_open_door_1
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_gg_night_1 with dissolve2
    play sound sfx_close_door_1

    window show
    "Открыв дверь в свой домик я зашёл в него и подошел к своему шкафчику."
    play sound sfx_open_cupboard
    "В нём я быстро разыскал свои умывальные принадлежности и пару полотенец."
    "Какие-то из них были для лица, какие-то для тела, но это меня не особо волновало."
    "Я схватил то, что первое попалось мне под руку, а также пакет с мылом и мочалкой."
    "В общем - полный набор для того, чтобы хорошо отдохнуть под струёй воды.{w} И ещё повезет, если она будет более-менее тёплой."
    "Взяв весь этот \"набор\" за пазуху, я отправился на выход из домика."
    window hide
    
    stop ambience fadeout 2
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1, hard=True)
    play ambience ambience_camp_center_night fadein 3
    scene bg ext_home_night with dissolve
    play sound sfx_close_door_1

    window show
    "Облака на небе предвещали не очень хорошую погоду, поэтому в моих планах было помыться очень быстро."
    th "Итак, куда мне сказала идти Ульяна?{w} За административным корпусом..."
    th "Карты у меня нет но, по моему, административный корпус находится чуть дальше площади."
    "Сейчас я надеялся на свою интуицию как никогда. Поэтому направился глубже в лагерь, чтобы постараться как-нибудь выйти к душевым кабинкам, которые я так и представлял."
    window hide

    show black with dissolve

    $ renpy.pause(3, hard=True)

    scene bg ext_shower_night with dissolve2
    
    window show
    "К счастью, я нашел душевые кабины быстрее, чем смог бы заблудиться в лагере."
    "Они сильно выделялись, поэтому их легко было увидеть даже издалека."
    "Они выглядели достаточно чистыми, убранными. Видимо, технички тут очень хорошо выполняют свою работу."
    th "Или пионеры."
    "Додумал в уме свое умозаключение я."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve2
    $ renpy.pause(1, hard=True)
    
    window show
    "Я зашел в одну из душевых кабин."
    "Здесь была полочка, на которой очень удобно можно было расположить свои умывальные принадлежности."
    "На стене даже был крючок. Но вешать на него полотенца я не решился. Ведь я мог просто их намочить. А тогда толку от них было бы чуть больше, чем от той же самой мочалки."
    "Поэтому я повесил полотенца на одну из стенок этой красной кабинки."
    window hide

    $ renpy.pause(2, hard=True)

    play sound_loop nds_list['sfx_shower_stream'] fadein 2
    
    window show
    "Теплые струи воды прикоснулись к моему телу из душа.{w} Меня бросило в дрожь."
    "Неужели вода так нагрелась за этот день, что сохранила эту температуру до позднего вечера?"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Пока я умывался под ещё не кончившейся теплой водой, в голову лезли мысли о произошедшем в шахте, и невольно я окунулся в них."
    th "Почему этот пионер хотел, чтобы я ушёл?{w} Даша...{w} Она...{w} Это действительно была она?"
    th "Не понимаю, почему я сам у себя это спрашиваю, но..."
    th "И что с ней сейчас? Хотел бы я узнать... Возможно стоит, как только я закончу."
    th "Возможно, я действительно сделал что-то неправильно. Но все выглядело так, будто он пытается от меня избавиться ради своих грязных дел."
    th "А что если бы он притворился мной? Если бы я уехал, он натворил бы таких делов, что...."
    th "Чёрт, надеюсь, все будет хорошо, чего бы мне это не стоило."
    th "Впервые за всё время, которое я себя помню, я хоть в чём то решителен."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Что этот пионер вообще себе позволял?"
    th "Даже для шутки его предложение звучит максимально низко."
    th "По сравнению с ним, мне кажется, я самый психически здоровый человек. Хотя и, как мне кажется, ненадолго."
    th "Мне попросту не хватает знаний о том, что происходит в этом лагере и во что я вляпался, оставшись тут..."
    window hide

    $ renpy.pause(2, hard=True)

    stop sound_loop fadeout 3

    window show
    "Когда вода стала ощущаться холоднее по сравнению с первыми моими ощущениями от неё, я закончил обмываться и потянулся за полотенцами..."
    window hide

    $ renpy.pause(1, hard=True)   

    window show
    "...Но, не нащупав их я, кажется, вразумил очередную шутку Ульяны."
    "Стало впервые немного... Обидно?{w} В любой бы другой ситуации я принял бы это как должное, но сейчас это показалось мне совсем не к месту."
    "Снаружи послышалось тихое хихиканье."
    "Не смотря на свою подавленность, я постарался сыграть настолько нейтрально, что любой зритель этого театра мог ощутить все те чувства, завязавшиеся в клубок внутри моей головы."
    nd_il "Ну всё, Ульяна.{w} Доигралась ты."
    window hide

    scene bg ext_shower_night with dissolve

    window show
    "Я быстро надел пионерскую форму на мокрое тело, и выбежав из кабинки увидел Ульяну, вдалеке махающую моими полотенцами."
    us "Ты не это случайно ищешь?"
    "Хихикая она удалялась на площадь."
    nd_il "Ну держись."
    "Сказал я и бросился вслед за Ульяной."
    window hide

    play sound_loop sfx_run_forest fadein 1
    show black with dissolve2
    $ renpy.pause(4, hard=True)
    stop sound_loop fadeout 3
    $ renpy.pause(1, hard=True)

    scene bg ext_volley_court_night with dissolve2
    
    window show
    "…Вскоре я выбежал на поле для игры в бадминтон. Вокруг не было ни души, лишь сверчки вдалеке напевали свою мелодию. Ульяны также здесь не оказалось."
    nd_il "Усвистала!.. С моими… Полотенцами!"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    pi "{font=mods/notdream/fonts/notes.ttf};{/font} Стремясь за солнцем, ты пришёл {font=mods/notdream/fonts/notes.ttf};{/font}"
    pi "{font=mods/notdream/fonts/notes.ttf};{/font} На безымянный остров. {font=mods/notdream/fonts/notes.ttf};{/font}"
    pi "{font=mods/notdream/fonts/notes.ttf};{/font} Стремясь за солнцем, ты пришёл, {font=mods/notdream/fonts/notes.ttf};{/font}"
    pi "{font=mods/notdream/fonts/notes.ttf};{/font} Туда, откуда нет пути... {font=mods/notdream/fonts/notes.ttf};{/font}"
    window hide

    $ renpy.pause(1, hard=True)
    
    play music ndm_list['nd_sp_r'] fadein 5

    show pi smile with dissolve
    
    window show
    "Прослушав отдалённо знакомым голосом напетые строки, я моментально смог понять их обладателя."
    "Повернувшись и увидев этого пионера, я отступил на два шага назад."
    "Сейчас он мог вполне стать моим потенциальным убийцей."
    "Я уже представлял, как завтра утром кто-то найдет моё тело, абсолютно обездвиженное."
    pi "Хочешь, мы вместе проучим её?"
    "Спросил меня пионер с такой же ухмылкой."
    "Внутри я был зол на него. Но страх не давал вырваться всему, о чём я думал."
    "И отступать было некуда..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Что ты сделал с Дашей?!"
    
    show pi with dspr

    "Выдавил я так, что судя по выражению его лица он на секунда растерялся."
    "Главное сейчас было не терять бдительность."
    "Кто знает, сколько ещё ножей спрятано у него в рукаве?"

    pi "Что она со мной сделала."
    show pi smile with dspr
    pi "Да и черт бы с ним.{w} Маленькие раны на моём теле быстро заживают, когда на небе полнолуние."
    "От этого бреда, мне было только сложнее держать себя в руках."
    "Тем не менее он ещё раз усмехнулся, будто прочитав мои мысли."
    pi "Ну так что думаешь насчёт того, чтобы проучить эту непослушную девчонку?"
    nd_il "Если ты её ещё хоть раз тронешь..."
    "Дерзко сказал я, сделав шаг в его сторону.{w} Он даже сделал шаг назад, но выдержав паузу..."
    pi "Ха-ха-ха-ха-ха..."
    "Пионер залился истерическим смехом."
    pi "И что же ты сделаешь?{w} Пустишь нюни, как ты обычно делаешь?{w} \"Я тебя никому в обиду не дам…\". Самому не противно?"
    nd_il "Кто ты такой, чтобы лезть в мою личную жизнь?"
    "Чуть ли не в упор говорил с ним я."
    window hide

    $ renpy.pause(1, hard=True)

    show pi with dspr

    window show
    pi "Возможно ты прав."

    show pi smile with dspr

    pi "Но всё-таки, что ты думаешь насчёт моего предложения?{w} Признай, она тебя уже не первый раз злит своими тупыми розыгрышами."
    nd_il "О чём ты?{w} Я не могу на неё злиться..."
    pi "Ладно, я шучу.{w} Твой ответ на этот вопрос был предсказуем."
    pi "Конечно не можешь. Думаешь, я не слышу, как стучит твоё сердце, когда я говорю её имя?"
    pi "Приятное чувство, когда всё внутри сжимается, лишь только заходит речь о её особе..."
    pi "Я прав?"
    window hide

    $ renpy.pause(1, hard=True)
    hide pi with dspr

    window show
    "Я молча опустил свой взгляд вниз."
    "Вокруг повисла тишина. Я не мог ничего сказать на этот счет."
    "Краем глаза я наблюдал за его действиями, на случай чего."
    "Возможно я действительно влюбился в неё, пусть и любовью это особо не назвать."
    "Но чувства к ней... Неужели я могу её любить?"
    "Любить маленькую девочку...{w} Боже, да что со мной не так? Я не могу..."
    "В реальном мире эта мечта разрушилась бы о запреты общества. Но что здесь?"
    "Если вспомнить песню Цоя про восьмиклассницу...{w} Это мило."
    "Отношения, разницей в два или три года могут быть нормальными в этом мире. Да и даже если так — этому телу сейчас лет шестнадцать."
    "Боже, да он похоже просто пытается усыпить мою бдительность.{w} К счастью, я это быстро заметил и не дам ему такой возможности."
    window hide
    
    $ renpy.pause(2, hard=True)

    show pi normal
    with dspr

    window show
    nd_il "У меня нет никакого желания разговаривать с тобой."
    "Резко нарушил тишину я."
    "Не знаю отчего я вспомнил Дашу, даже если она в порядке - где она?{w} Цела ли?{w} Нужна ли помощь?"
    nd_il "Ты только и делаешь, что заставляешь меня свалить из лагеря любыми способами. И кто ты вообще такой?"
    pi "Я тот, кто помогает тебе на протяжении всего твоего пребывания в лагере."
    nd_il "Интересная у тебя помощь."
    nd_il "Так вот, катись с этой помощью. Я не хочу тебя больше видеть."
    "Процедил сквозь зубы я последнее предложение."
    nd_il "Сгинь, нечисть."
    window hide

    hide pi with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Сказал я и отвернулся очень халатно.{w} Но не знаю почему,{w} я чувствовал что буду в безопасности."
    "Тишина со звуками сверчков прорвалась в мои уши.{w} Неужели он и вправду исчез?"
    window hide

    $ renpy.pause(3, hard=True)

    window show
    "Повернувшись обратно я вновь увидел этого пионера, который смотрит на небо."
    pi "А ведь и вправду хорошее место.{w} Согласись, здесь можно жить вечно."
    pi "Просто сел на травку, смотришь в небо и думаешь: \"как же хорошо тут\". Не правда ли?"
    pi "Словно этот лагерь был создан самой матушкой природой..."
    window hide

    $ renpy.pause(1, hard=True)
    show pi normal with dissolve

    window show
    pi "А ещё лучше дома.{w} У тебя ведь там лучшие друзья, подруги…"
    nd_il "Насколько я помню, у меня дома нет ничего, что заставило бы меня вернуться обратно."
    pi "Ошибаешься.{w} А что насчёт твоего компьютера? А может тебя ждут твои заказчики?"
    nd_il "Я выполнил все заказы.{w} Проживу до конца смены, и уеду домой."
    "Вставил едкую и не менее правдивую шпильку в его монолог я."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    pi "Ладно."
    "Я поднял глаза на него."
    pi "Как я вижу, уговаривать тебя бесполезно."
    pi "Просто помни, что может случиться что-то плохое, и готовься к этому."
    
    hide pi with dspr

    "Пионер собрался уже уходить, но внезапно остановился и посмотрел на меня."
    show pi normal with dspr
    pi "И ещё.{w} Я сегодня сам уезжаю, и меня завтра не будет."
    pi "А это прими в знак моих извинений или как подарок."
    "Сказал пионер, и протянул мне пять рублей времён СССР."
    hide pi with dspr
    "Я неутвердительно взял в руки купюру,{w} одним глазом смотря на нее, а другим на пионера."
    th "Сначала хочет убить, угрожает, запугивает, это не считая случая на пляже, если он про это не шутил..."
    "Я ещё раз хотел посмотреть на этого урода, но тот уже уходил куда-то глубоко в лес, скрываясь за стволами деревьев."
    "А мне только и оставалось провожать его взглядом."
    th "Биполярный какой-то он." 
    window hide

    stop music fadeout 4

    $ renpy.pause(1, hard=True)

    show nd_5_rubasov:
        xalign 0.5 yalign 1.0
        linear 2.0 yalign 0.5

    with dissolve2

    window show
    th "И что можно купить в Советском Союзе за пять рублей?"
    "Задумался я, разглядывая эту купюру."
    th "Сто двадцать пять пачек эскимо стоимостью в двадцать пять копеек."
    th "А это три тысячи семьсот пятьдесят рублей.{w} Учитывая, что эскимо в Российской Федерации стоит тридцать рублей."
    th "Конечно, люди в Советском Союзе питались не только эскимо, поэтому мои расчеты были не совсем корректными."
    th "На кой мне деньги?{w} Для чего?"
    th "Может в райцентр попроситься поехать?"
    window hide

    hide nd_5_rubasov with dissolve

    $ renpy.pause(1, hard=True)
    play sound sfx_hiding_in_bush

    window show
    th "Пока я размышлял на эту тему, кусты слева от меня странно зашуршали."
    th "Может это был просто ветер,{w} а может кто-то за мной подглядывал."
    th "Ну-ка..."
    "Я сделал вид, что ничего не замечаю, но потом..."
    window hide

    show black with dissolve
    with vpunch
    play sound sfx_bush_body_fall
    
    window show
    "...Я резко кинулся в кусты, в надежде поймать незнакомца или то, что там было.{w} Но там никого не оказалось."
    window hide

    $ renpy.pause(2, hard=True)
    scene bg ext_volley_court_night with dissolve2

    window show
    "Когда я понял, что никого не поймал, я встал с земли и почувствовал, как на руки падают холодные капельки дождя."
    "Вся моя форма была мокрая. А после моего последнего действия ещё и грязная."
    "Зря я это сделал. Очень зря. Мне вдруг стало до того обидно, что в ту же секунду меня переполнила злоба."
    nd_il "Вот напасть!{w} Проклятье!{w} Ненавижу!"
    window hide

    show black with dissolve
    
    $ renpy.pause(1, hard=True)

    window show
    "Закричал я и двинулся прочь от этого места на площадь."
    window hide


    $ renpy.pause(2, hard=True)
    scene ext_path2_night with dissolve

    window show
    "Но через пару секунд резко остановился.{w} Вспомнил про Дашу."
    "Сегодня её нужно было найти во что бы то ни стало и в каком бы виде я не был."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Рефлекторно перед какими либо решениями, проверяя карманы, я нащупал фонарик."
    nd_il "Оу..."
    window hide

    $ renpy.pause(2, hard=True) 

    play sound nds_list['nd_flashlight_on']
    scene bg ext_path2_night_light

    window show
    "Нажав на переключатель немного темная дорога к лагерю озарилась спектральным заревом."
    th "Отлично.{w} Он мне по-любому пригодится."

    play sound nds_list['nd_flashlight_on']
    scene bg ext_path2_night

    "Подумал я, выключив его.{w} Советская техника на века."
    "Положив фонарик обратно в карман, я продолжил свой путь к лагерю.{w} Так как дождь ещё лишь слабо накрапывал, у меня было время..."
    window hide

    show black with dissolve2
    $ renpy.pause(2, hard=True)
    scene bg ext_houses_night_1 with dissolve2

    window show
    "Я свернул к домикам."
    "Мысли метались в голове. От Дашки до розыгрыша Ульяны."
    "Признаться честно сейчас он был не к месту, но я старался свои эмоции держать под контролем."
    th "Так, необходим план, что мне делать и куда идти."
    show prologue_dream with dissolve
    "Я попытался вспомнить.{w} В последний раз мы видели её, когда она сверху, царапая пионера, отводила его в лес."
    th "Вот уж умница..."
    "Невольно улыбнулся я."
    window hide

    show black with dissolve

    window show
    "С этими мыслями я проходил мимо своего домика и, почему-то не обратил внимания на свет, который в нем горел."
    "Значит так, фонарик{w} - есть, далеко отходить не планирую. Хотя она наверное где-то отцепилась от него в лесу и убежала обратно в катакомбы."
    "Помню, он как-то нелестно о ней отзывался.{w} Возможно, она часто проводит время именно там."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Я уже подходил к воротам..."
    window hide

    $ renpy.pause(1, hard=True)

    play sound sfx_jump_into_hole_2

    $ renpy.pause(1, hard=True)
    
    scene bg ext_path_night
    show unblink

    $ renpy.pause(1, hard=True)

    window show
    "Сиганув через них не без труда,{w} в этот раз едва не лишившись шорт,{w} я оказался за пределами лагеря."
    th "Итак, вот план \"А\"."
    "Я ненадолго задумался."
    th "Значит так,{w} идём к тому месту,{w} ищем вокруг - возможно стоит позвать.{w} Если нет - спускаться вниз и искать там."
    th "Интересно, а как звать? \"Даша\"? Или просто \"кыс-кыс\"?"
    "Я оглянулся вокруг в поисках каких-либо ориентиров, дабы не потеряться при поисках. И заметил..."
    th "Погодите, а не это ли та самая дорога с входом в бункер?.."
    th "Возможно, нужно лишь пройти слегка дальше..."

    play sound nds_list['nd_flashlight_on']
    scene bg ext_path_night_light
    
    "Подумав об этом я включил фонарик и направив его на протоптанную тропинку пошел по ней всё глубже в лес..."
    window hide

    $ renpy.pause(1, hard=True)
    play sound_loop sfx_far_steps fadein 3

    window show
    "До старого лагеря идти мне не особо хотелось.{w} Я надеялся, что вот-вот увижу этот спрятанный люк."
    "Хотя даже и не помню, закрывал его или нет."
    "В любом случае, на тропинке виднелись следы от ботинок вперемешку со следами лесной живности."
    "В грязи сложно было их различать. Но это меня не останавливало или скорее почти не интересовало...{w} Я просто шёл..."
    window hide
    
    stop sound_loop fadeout 5

label nd_c1_p4_securate:

    show black with dissolve2
    $ renpy.pause(1, hard=True)
    "Неопределенное время спустя..."
    $ renpy.pause(1, hard=True)
    scene bg ext_path_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Люк был найден совершенно спонтанно."
    "Я выронил фонарик из-за напугавшей меня совы и, поднимая его, заметил перед собой люк и крышку в метре от него."
    "Я вспомнил, как вылазил отсюда вместе с Ульяной, как нас встретил тот самый злой пионер."
    "И в этот момент стало немного страшно залезать обратно."
    "Но как говорится, у страха глаза велики."
    "Поэтому, стараясь не загружать себя лишними мыслями, я начал спускаться вниз..."
    window hide

    stop ambience fadeout 3
    stop music fadeout 3

    $ renpy.pause(1, hard=True)
    
    show black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg int_mine_exit_night_light_forest_opened with dissolve
    play sound nds_list['metallic_stair']
    $ renpy.pause(2, hard=True)
    stop sound fadeout 2
    $ renpy.pause(1, hard=True)
    show blink
    play sound nds_list['podskolz_1']
    $ renpy.pause(1, hard=True)
    play sound sfx_bodyfall_1
    $ renpy.pause(1, hard=True)

    if persistent.fall_stair_bunker == 2:
        window show
        "...И видимо это и стало моей неоднократной ошибкой..."
        window hide
    
    elif persistent.fall_stair_bunker == 3:

        window show
        "...И видимо это и стало моей критически-неоднократной ошибкой..."
        nd_il "Oh shit, here we go again..."
        window hide

    elif persistent.fall_stair_bunker == 4:

        window show
        "...И видимо это и стало моей критически-неоднократной ошибкой..."
        nd_il "Уверен, это необходимая мера, чтобы выйти на её рут..."
        window hide

    elif persistent.fall_stair_bunker == 5:

        window show
        "...И видимо это было и стало моей ошибкой."
        window hide

        show vlad_pavlenko_pizza at center with dissolve
        
        window show
        nd_il "Я обязательно выживу."
        "Эх... Ничему тебя жизнь не учит, Илья..."
        window hide
        
        hide vlad_pavlenko_pizza at center with dissolve

    if persistent.fall_stair_bunker <= 1: 
        window show
        "...И видимо это и стало моей ошибкой..."
        window hide


    $ renpy.pause(1, hard=True)

    window show 
    "Я упал вниз, подскользнувшись на одной из ступенек."
    "Хоть эта лестница и не была такой высокой, я все-таки умудрился зацепится своей одеждой за что-то, пока падал."
    window hide
    
    $ persistent.fall_stair_bunker += 1

    stop ambience fadeout 3
    stop music fadeout 3
    scene black with dissolve2

    window show
    nd_il "Ох чёрт!"
    window hide

    $ renpy.pause(3, hard=True)
    play ambience ambience_catacombs_stones fadein 4
    $ renpy.pause(1, hard=True)
    scene bg int_mine_exit
    hide blink
    show unblink
    
    $ persistent.fall_stair_bunker = 0

    $ renpy.pause(2, hard=True)

    window show
    "Спустя несколько секунд я через силу встал и отряхнулся."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Осматривая тыльные стороны рук я заметил, что они были изрезаны."
    th "Рубашке конец... Но да ладно."
    th "Стоило отдать ей должное,{w} она хотя бы немного смогла спасти мое тело от порезов."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg int_mine_exit_light with dissolve
    $ renpy.pause(1, hard=True)

    window show
    "Я осмотрел бетонный пол помещения."
    "Битая стеклотара на полу, которую я не заметил в первый раз, заблестела от света фонарика, лежавшего там же."
    "Отряхиваясь и держась за плечо, я вставал на ноги."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я поднял фонарик, потом осветил ту часть комнаты, которая была закрыта большим ковром."
    th "Если Даши здесь нет, то может быть она в бункере?"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я подошёл к ковру и принялся решительно толкать его левой рукой, держа фонарик в правой."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(3, hard=True)
    scene bg int_catacombs_living with dissolve2

    window show
    "Освещению предстали внутренности комнаты и Даша..."
    
    play music ndm_list['forever_smile'] fadein 5

    show da surprise far at center with dspr
    nd_da "Что ты здесь..."
    "Не успела она договорить как посмотрела на мои руки."
    "Я же в свою очередь оглядел её..."
    "Немного исцарапанная, но целая, некоторые участки кожи перебинтованы. На бинтах были пятна."
    "Йод, зелёнка или всё вместе, в свете грязной лампочки было не разобрать."
    show da guilty far at center with dspr
    nd_da "Ты как тут оказался?"
    nd_da "Зачем ты здесь?"
    "Беспокойно и удивлённо начала проговаривать она."
    window hide
    
    hide da with dspr
    $ renpy.pause(3, hard=True)

    window show
    "Я без слов подошёл к оцепеневшей Даше и обнял ее."
    "Она непонимающе взглянула на меня, но после в ее глазах появились слёзы, она уткнулась мне в плечо..."
    nd_il "Спасибо тебе, Даш, за то что спасла от этого пионера."
    show da shocked close at center with dspr
    nd_da "Это же не он сделал?"
    "И тут я вспомнил кусты...{w} Это она сидела там?"
    "После этого, возможно, ещё вся в ссадинах, царапинах и наблюдала за мной?"
    hide da with dspr
    "От этих мыслей я только крепче ее прижал и начал гладить по голове..."
    nd_il "Это ведь ты была? В кустах? На площадке?"
    "Она ничего не отвечая лишь кивнула."
    window hide

    $ renpy.pause(1, hard=True)

    show blink

    $ renpy.pause(3, hard=True)

    window show
    "Мы простояли так минуты две. После чего..."
    window hide

    $ renpy.pause(1, hard=True)

    show da shocked at center
    hide blink
    show unblink
    
    $ renpy.pause(1, hard=True)

    window show
    nd_da "Как ты так-то?"
    "Она кивнула головой на мои руки."
    nd_il "С лестницы упал."
    "Махнул я рукой в сторону лестницы."
    nd_il "Скользкой оказалась."
    show da sad at center with dspr
    nd_da "Похоже, моя вина. Мои лапки были влажные после травы, и я тоже, когда сама спускалась..."
    nd_il "Всё хорошо, Даш, главное все целы."
    hide da with dspr
    "Я ещё раз обхватил руками Дашу..."
    "Не сколько из за того, что я пытаюсь сгладить боль внутри, сколько просто соскучился по своей сестре..."
    "Даша также приобняла меня, прижав поближе к себе."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Вскоре послышалось тихое урчание."
    "Я немного удивлённо на нее посмотрел, но найдя логику в этом, отбросил сомнения.{w} Отчасти."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Даша разжала объятия отошла от меня к столику."
    "На столике рядом стояли баночки с этикетками."
    "Что на них было написано прочитать было сложно, но понять не трудно."
    show da normal at center with dspr
    nd_da "Садись, вон на ту кровать. И не ворчи."
    hide da with dspr
    "Сказала она более мягким голосом, впрочем о том, чтобы ворчать я думал в последнюю очередь."
    window hide

    play sound sfx_bed_squeak1

    window show
    "Я послушно сел на кровать."
    show da normal far at left with dspr
    "Тем временем Даша взяла в руки пузырьки, что-то на них читая, потом палочки и подошла ко мне."
    hide da with dspr
    "Села рядом, открыла их, сказала снять рубашку."
    "Впрочем, рубашкой это можно было назвать лишь с натяжкой."
    "Как только я ее снял, Даша бросила на неё взгляд."
    window hide

    $ renpy.pause(1, hard=True)
    show da sad close at center with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Она не сказала ничего, но этот взгляд стоил тысячи слов."
    "Несложно было понять о чём она думает."
    nd_da "Потерпи, братик, всё будет хорошо."
    show da guilty close at center with dspr
    nd_da "Повернись спиной, пожалуйста."
    "Попросила она, что я и сделал..."
    window hide

    hide da with dspr

    $ renpy.pause(2, hard=True)

    window show
    "С её стороны послышался вдох удивления и грусти."
    "После чего она принялась за работу."
    "Мне было больно. Но что поделать, сам ведь упал."
    nd_il "Даш, извини за такой тупой вопрос но...{w} Ты же помнишь меня, так?"
    play sound sfx_bed_squeak2
    "Звуки кровати, которая качалась под весом, качая заодно и меня, прорвались через тишину в мозг."
    "Руки Даши замерли на одном месте, будто парализовались."
    nd_il "Понял, извини..."
    "Не успел я договорить как она меня перебила."
    nd_da "Конечно помню."
    "Сказала она как-то нерешительно и вместе с тем уверенно."
    "Хотел я было продолжить, но она перебила меня вопросом."
    nd_da "А что {i}ты{/i} помнишь?"
    "Спросила она."
    "Впрочем скрывать от неё правду смысла нету, поэтому я решил сказать всё сразу, как оно есть."
    nd_il "Знаешь... Я мало что помню..."
    "Пока я это говорил, она продолжала возиться с моей спиной."
    "Я тяжело и прерывисто выдохнул."
    nd_il "Некоторые вещи и места я как будто помню, но вместе с тем понимаю, что не помню ничего."
    nd_il "Почти ничего до попадания в лагерь. Лишь несколько смутных образов..."
    nd_il "Психотерапевт говорил, что у меня какая-то травма, которая со временем вызвала у меня амнезию."
    play sound sfx_bed_squeak2
    "Кровать снова издала тяжелый скрип."
    stop music fadeout 4
    nd_da "А ты помнишь что со мной... Было?"
    "Сказала она с горечью и расстановкой такой слов, что даже моё сердце вновь замерло."
    nd_il "Да... Я это в полной мере вновь испытал вчера, после встречи с тобой, я это помнил и до этого..."
    "Она лишь приобняла меня за плечи, положив свою голову рядом с моей, говоря на ухо."
    show da smile at center with dspr
    nd_da "Всё хорошо, я здесь с тобой. Всё хорошо..."
    hide da with dspr
    "Я повернулся и обнял ее, она мучительно замолчала."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    nd_il "А как, это...{w} Произошло?"
    "Даша немного опустила взгляд, я думал она уже не начнёт говорить, но..."
    show da guilty close at center with dspr
    nd_da "Да, ты должен знать, ты имеешь право знать, но я не хочу чтобы ты снова..."
    "Я ее перебил."
    nd_il "Даша, посмотри на меня."
    nd_il "Я похож на того кто не переживёт такой рассказ?"
    "Сказал я с наигранной улыбкой, стараясь разрядить обстановку."
    "Впрочем со стороны это, должно быть, выглядело странно."
    "Максимально странно я бы сказал, человек с улыбкой, приободряя, просит свою сестру рассказать, как она..."
    show da normal close at center with dspr
    "Вернувшись из своих раздумий, я увидел, что это помогло, Даша посмотрела мне в глаза и начала рассказ."
    window hide

    play music ndm_list['nd_1219_music'] fadein 5
    show prologue_dream with dissolve2
    $ renpy.pause(2, hard=True)

    window show
    nd_da "Это уже было поздней ночью, мы с моими подругами, разошлись минут десять назад."
    nd_da "Я уже направлялась в сторону дома, так как мы довольно рано закончили отмечать."
    nd_da "Я ничего не пила, была абсолютно чиста."
    "Про себя я думал: \"Как же так вышло-то?{w} Трезвая шла уже домой...{w} Неужели?..\""
    "Тем временем она продолжала рассказ."
    nd_da "Уже подходя к одному из переходов, тихо напевая песенку, я ждала зелёный свет."
    nd_da "Спустя минуту он загорелся, всё было тихо или же возможно я была не очень внимательной."
    nd_da "Пошла на зелёный, только дошла до середины, а дальше сильный удар..."
    "В груди кольнуло. Звуки вокруг потеряли краски. Я чувствовал, будто сию минуту упаду в обморок."
    nd_da "Помню, как лежала на асфальте..."
    window hide

    hide prologue_dream with dissolve2
    $ renpy.pause(2, hard=True)

    window show
    "Но видя её перед собой... Я снова заключаю её в объятия и успокаиваю как могу. То ли себя, то ли её..."
    nd_il "Извини, это моя вина..."
    show da guilty close at center with dspr
    nd_da "Нет, всё правильно, ты должен был знать, ты единственный, кто имеет на это право."
    "Она по тёплому улыбнулась мне, так как когда-то."
    "Меня опять взяли за шкирку воспоминания и чувство дежавю."
    "Но не успели они захватить меня, как из глубины помещения прозвучало..."
    show da normal close at center with dspr
    nd_da "Дай левую руку."
    hide da with dspr
    "Скомандовала Даша, я послушно выполнил ее просьбу."
    "И тут я вспомнил насчёт одного персонажа, нужно, как говорится, знать врага в лицо."
    nd_il "Извини, если опять лезу куда не стоит, но что насчёт..."
    show da normal close at center with dspr
    nd_da "Пионера?"
    "Вкрадчиво переспросила меня Даша, отчего я даже удивился."
    nd_il "Да."
    show da smile close at center with dspr
    nd_da "Хорошо, так и быть."
    show da normal close at center with dspr
    "Сказала она с небольшим лукавством, после чего приняла серьёзный вид."
    nd_da "Этот пионер - тот, кто случайно попал сюда, узнал больше чем должен знать, а потом возомнил себя знающим всё."
    nd_da "Он просто думает, что знает достаточно много, чтобы считать себя наблюдателем." 
    nd_il "Наблюдатель? Это кто?"
    nd_da "Наблюдатели, это такие существа, которые присматривают за всем, что происходит, но не могут вмешиваться."
    nd_il "То есть ты наблюдательница?"
    show da smile close at center with dspr
    "Я недоумевающе посмотрел на Дашу, но та лишь отвела взгляд."
    nd_da "Нет, я же говорила, что наблюдатели не могут вмешиваться. Я - хранительница лагеря."
    "Голова потихоньку начинала вскипать."
    nd_il "То есть хранительница..."
    show da normal close at center with dspr
    nd_da "Илья, я хранительница лагеря, и присматриваю конкретно за ним и могу вмешиваться в него и контактировать с его обитателями, а наблюдатели присматривают за всем и всеми."
    th "Понятно... Если они присматривают за всеми, то..."
    nd_il "И за мной?"
    nd_da "Не знаю. Скорее всего да."
    nd_il "И зачем им это?"
    "Задал я ей вопрос, подняв левую бровь вверх."
    show da smile close at center with dspr
    nd_da "Дай вторую руку."
    "Я протянул правую руку наполовину, и снова под порывом боли прерывисто выдохнул."
    show da normal close at center with dspr
    nd_da "Отвечая на твой вопрос - не знаю."
    nd_da "И помни, ничего не бойся. Пока я рядом, с тобой ничего плохого не случится."
    nd_da "Но всё равно будь аккуратен, я не смогу тебе помочь в твоем сне.{w} В спящем состоянии твое тело слишком уязвимо."
    nd_da "Особенно если у тебя проблемы с сердцем."
    nd_il "Хорошо, спасибо за предостережение."
    show da laugh close at center with dspr
    nd_da "А ещё тебе следует смотреть за своей девушкой."
    "Даша мне подмигнула и захихикала.{w} От этого я даже почувствовал себя не ловко. Но это чувство быстро отпустило меня."
    "Come on, это же моя сестра..."
    window hide

    stop music fadeout 20
    hide us with dspr
    $ renpy.pause(2, hard=True)

    window show
    "После этого она продолжила домазывать мне вторую руку."
    show da normal close at center with dspr
    nd_da "Так, а это что?"
    "Спросила она указывая на ушиб на туловище."
    nd_il "Это меня тот пионер в лесу так..."
    hide da with dspr
    "Даша стала похожа на кошку которую гладили против шерсти."
    "Взгляд, уши, хвост...{w} Даже волосы дыбом встали."
    "Странно, разве так себя должен вести енот?{w} Похоже на то."
    "Этот вопрос встал у меня на лице гримасой то-ли страха, то-ли удивления."
    show da guilty close at center with dspr
    nd_da "Извини, не хотела напугать..."
    nd_il "Всё хорошо, Даш."
    "Сказал я и рефлекторно погладил её по голове, отчего тихо заурчала."
    window hide
    
    hide da with dspr
    $ renpy.pause(2, hard=True)
    
    window show
    "Встав, она пошла к столу, взяв какую-то другую баночку, и спустя секунду вернулась ко мне."
    "Намазывая меня этой субстанцией, которая странно пахла, она приговаривала что-то себе под нос."
    "Закончив с этим, она жестом разрешила мне одеваться."
    window hide

    $ renpy.pause(1, hard=True)

    show prologue_dream with dissolve
    
    window show
    "После мы некоторое время за общением просидели на той самой кровати."
    "Общались обо всём,  мне было трудно говорить про себя, но я пытался."
    "Даша, казалось, всё понимает, даже больше чем я иногда, сочувствовала, иногда хмурилась."
    "Но я ее не виню, я сам себя часто осуждаю за многое. И реже всего хвалю."
    "Так же мы говорили и про Дашу, про запасы какие-то, а так же про лунный сахар.{w} Ума не приложу при чём тут он."
    window hide

    hide prologue_dream with dissolve
    $ renpy.pause(1, hard=True)

    show da smile at center with dspr
    
    window show
    nd_da "Знаешь, наверное тебе уже пора, поздно, скоро спать пора, да и мало ли, вдруг Ульяна тебя потеряет."
    "С тёплой улыбкой сказала Даша."
    nd_da "А я буду рядом."
    nd_il "Ты всегда мне помогала, во всём и даже сейчас."
    nd_il "Спасибо тебе за всё, сестра."
    hide da with dspr
    "Я заключил ее в объятия."
    "Мы на прощание перебросились парой слов.{w} Она обещала, что мы ещё встретимся, и вновь бросила фразу \"всё будет хорошо\"."
    "Это мне что-то напомнило..."
    window hide

    show black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg int_mine_exit_light with dissolve

    window show
    "После немного затянувшегося прощания, я отодвинул тот самый ковер и пробрался в комнату с выходом."
    "По приблизительным расчетам, я здесь с Дашей просидел около часа."
    "Подходя к лестнице я предварительно набирал силы для моей следующей вылазки наверх по этой лестнице."
    "Опять подметив странности, связанные с мыслями о сахаре, я начал своё восхождение наверх..."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg int_mine_exit_night_light_forest_opened with dissolve
    play sound nds_list['metallic_stair']
    $ renpy.pause(3, hard=True)
    stop ambience fadeout 3
    stop sound fadeout 2
    show black with dissolve
    $ renpy.pause(2, hard=True)
    play ambience ambience_forest_night fadein 3
    scene bg ext_path_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Вылезя из данного отверстия, я осмотрел округу.{w} С моего последнего появления на открытом воздухе тут очень потемнело."
    "Дождь накрапывал не ливнем, но было ощутимо."
    "Лишь выбравшись наверх и набрав в лёгкие ночного воздуха, я смог осознать, что уже изрядно устал за этот день."
    th "Да уж, он был не из простых."
    "Про себя отметил я."
    th "Но всё таки, всё хорошо, что хорошо начинается."
    "С повышенным настроением сам себе вторил я."
    play sound nds_list['nd_flashlight_on']
    scene bg ext_path_night_light
    "Я включил фонарик, и уже с неплохим настроением, напевая одну из каких-то известных мне песен, пошёл к тропинке."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg ext_path2_night_light with dissolve
    $ renpy.pause(1, hard=True)

    window show
    "Через минуту я был на ней, двинулся в лагерь."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    
    $ renpy.pause(1, hard=True)

    play sound sfx_jump_into_hole_2

    $ renpy.pause(1, hard=True)
    
    scene bg ext_houses_night
    show unblink

    window show
    "Подойдя к воротам, я перепрыгнул через них и под аккомпанемент дождя медленным шагом пошёл к своему домику."
    window hide
    
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    scene bg ext_house_of_gg_night2 with dissolve2
    
    window show
    "Через пару минут я был там."
    "Фонарик над моим домиком светился. Внутри него также горел свет. Аналогично, как он горел, когда я проходил рядом с ним в первый раз."
    "Я выключил фонарик, и начал подходить к своему 24-му домику."
    "Мне казалось там кто-то есть и думаю не без причины."
    window hide

    show black with dissolve
    
    window show
    "Я очень аккуратно обошёл домик и заглянул в окно."
    window hide

    scene bg int_house_of_gg_night
    show prologue_dream
    with dissolve
    
    $ renpy.pause(1, hard=True)

    show us normal pioneer far at right behind prologue_dream with dspr

    window show
    "На кровати сидела Ульяна, шкафчик рядом с моей кроватью был слегка приоткрыт.{w} Помнится мне, что я его закрывал."
    th "Ладно, сделаем вид что я тут только пришёл."
    window hide

    scene black with dissolve
    $ renpy.pause(1, hard=True)
    scene bg ext_house_of_gg_night2 with dissolve

    window show
    "Я снова обошёл свой домик, сунув фонарик в карман."
    "После подошёл уже нормальным шагом к зданию и не стесняясь зашел по двум из трёх ступенек."
    "После открыл на себя дверь."
    window hide

    stop ambience fadeout 3
    show black with dissolve
    play sound sfx_open_door_1
    $ renpy.pause(1, hard=True)
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_gg_night with dissolve
    play sound sfx_close_door_1
    $ renpy.pause(1, hard=True)
    show us shy2 pioneer far at right with dspr
    window show
    
    "И тут же увидел сидящую и смотрящую на эти самые двери Ульяну, через окно я не мог рассмотреть её полностью, но сейчас..."
    "Она повернула ко мне своё лицо, и я заметил два синих глаза, от которых шли дорожки."
    th "Она плакала?"
    hide us with dspr
    "В ту же секунду она соскочила с кровати и пулей влетела в меня."
    "По ощущением меня обнимали, но кулачки бьющие по спине говорили о том, что имело место и покушение на мою жизнь."
    nd_il "Что случилось?{w} Ты плакала?"
    "Девочка не ответила.{w} Она перестала меня бить и просто уткнулась мне в грудь, дав её приобнять..."
    window hide

    $ renpy.pause(2, hard=True)

    window show    
    "В такой позе мы простояли минуту, после чего она подняла на меня свои глаза."
    show us sad pioneer close at center with dspr
    us "Где ты был? Я уже полотенца сложила, одежду погладила, искала тебя по всему лагерю."
    "Я удивлённо посмотрел на эту девушку."
    th "Погладила? Сложила?"
    "Сказать что я удивился - ничего не сказать."
    "Трудно было описать мои эмоции в этот момент."
    "Пока я обдумывал это, Ульяна осматривала моё состояние и состояние моей одежды."
    hide us with dspr
    show us normal pioneer at center with dspr
    us "Ой, а что...{w} Это?"
    "Спросила Ульяна, остановившись на моих руках."
    nd_il "Упал."
    "Кратко и честно констатировал я."
    show us surp2 pioneer at center with dspr
    us "Как так можно было упасть?"
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)
    play sound sfx_inhale
    $ renpy.pause(1, hard=True)

    window show
    "Я сделал глубокий вдох и прерывисто выдохнул."
    nd_il "Давай сначала присядем что ли."
    hide us with dspr
    "Ульяна согласилась со мной, и спустя пару мгновений мы сидели рядом на кровати."
    "Я уже было хотел начать рассказ, но Ульяна меня прервала своим глубоким вдохом."
    show us surp2 pioneer at left with dspr
    us "Ах!"
    us "Что с одеждой?!"
    hide us with dspr
    "Она хотела прилечь, но наклонив голову с туловищем назад, увидела мою спину."
    "Её зрачки в миг расширились от удивления, от увиденного."
    "Не знал, как это выглядело со стороны, но по собственным ощущениям, моя рубашка была решетом."
    show us surp3 pioneer at left with dspr
    us "Мамочки..."
    us "А что со спиной?!"
    nd_il "Тоже упал..."
    "Она вернулась в первичное положение."
    show us shy pioneer at left with dspr
    us "Как это произошло?"
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Я сделал секундную паузу, дабы прочистить горло, и всё таки решился начать удивлять..."
    nd_il "После того, как я побежал от душевых за тобой, хотел срезать путь, дабы поймать тебя."
    nd_il "Но выбежал к какой-то волейбольной площадке."
    show us normal pioneer at left with dspr
    nd_il "Простояв пару секунд в недоумении, сзади послышался напев смутно знакомой мне песни не менее смутно знакомым голосом."
    nd_il "И в тот момент, когда этот кто-то закончил..."
    show us surp2 pioneer at left with dspr
    nd_il "Я повернулся и увидел пионера.{w} Того самого, который хотел со мной расправиться на выходе из катакомб."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Глаза у Ульяны стали с пять полновесных советских копеек, таких, которыми расплачиваются пионеры в столовом буфете."
    us "И что случилось?{w} Это {i}он{/i} сделал?"
    "Выделив личное местоимение, девочка обвела ладонью мои поврежденные руки и спину."
    nd_il "Нет, не он..."
    show us normal pioneer at left with dspr
    us "Тогда что он хотел?"
    "Голос Ульяны приобрёл ноты искренней обеспокоенности, и пока эта обеспокоенность не переросла в нечто большее, надуманное ею, я незамедлительно продолжил, неспециально перебив её следующий вопрос..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Сначала он предложил мне вместе с ним тебя проучить за розыгрыш, на что я разумеется ответил отказом."
    nd_il "Также он упомянул о Даше, и у меня возникло желание найти её."
    nd_il "Забегая вперёд, я был слишком решителен тогда, и не знаю, к чему бы это могло меня привести."
    hide us with dspr
    "Я виновато опустил голову вниз, погрузив наш с девочкой диалог в короткое молчание."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    nd_il "Он так же хотел, чтобы я ушёл из лагеря."
    "Наконец собравшись с мыслями я продолжил."
    nd_il "Но в конце поняв, что упрашивать меня об этом бесполезно, решил со мной примириться."
    nd_il "Вместе с этим ещё сказал, что может случиться что-то очень плохое, но никакой конкретики от него не было."
    show us normal pioneer at left with dspr
    nd_il "Не знаю угрожал он мне или нет, но думаю, что это звучало больше как предупреждение о чём-то."
    nd_il "И после своего предупреждения он отправился в глубину леса."
    window hide

    $ renpy.pause(2, hard=True)
    show us surp2 pioneer at left with dspr
    
    window show
    us "И что было дальше?"
    "Не выдержав очередной моей паузы, девочка бесцеремонно нарушила её."
    show us normal pioneer at left with dspr
    "Я рассказал о шорохах, о том спуске в катакомбы, лестница которого меня изрядно изувечила..."
    show us surp2 pioneer at left with dspr
    us "Это там ты так упал?"
    show us normal pioneer at left with dspr
    nd_il "Да, и думаю, если бы не разбитое стекло, то отделался бы куда легче..."
    window hide

    $ renpy.pause(1, hard=True)

    window show    
    "Сделав паузу я кинул свой многозначительный взгляд на Ульяну.{w} Девочка выглядела поникшей, тихо сидела, опустив взгляд в пол."
    "Я пододвинулся к ней и слегка приобнял, пропустив через горло свой следующий вопрос."
    nd_il "Что случилось?"
    us "Это всё из-за меня."
    nd_il "Уля, ты о чём?"
    "Я посмотрел на неё с непониманием, отчего та нарочно спрятала свой взгляд."
    us "Если бы я опять не устроила очередной розыгрыш, ты бы не встретился с ним и не полез бы потом в катакомбы..."
    us "Я тут не могла себе найти место, даже по лагерю ходила и искала тебя..."
    us "Если бы не я, всё было бы по-другому..."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Ульяна отвернулась и издала короткое шмыгание носом, будто уже была готова заплакать."
    nd_il "Я не злюсь на тебя."
    nd_il "Я же говорил вам с Алисой, что ваши розыгрыши...{w} Не мешают."
    th "Почти..."
    show us sad pioneer at center with dspr
    us "Я просто хотела тебя развеселить."
    us "Обещаю, буду меньше тебя разыгрывать."
    "Она опять посмотрела в мои глаза, так искренне, словно она сделала ошибку в тесте и извиняется за это перед учителем."
    hide us with dspr
    "Но я не учитель. Я не считал, что ей нужно за это извиняться, но и я не должен её ругать."
    "Поэтому моё следующее согласие показалось мне оптимальным выходом из сложившейся ситуации."
    nd_il "Хорошо, верю. Давай..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я замешкался, очередной раз встретившись с девочкой взглядом."
    nd_il "...Давай сменим тему."
    show us normal pioneer at center with dspr
    nd_il "Расскажи, откуда ты знаешь про Дашу?"
    window hide

    $ renpy.pause(1, hard=True)
    show us grin pioneer at center with dspr

    window show
    "Ульяна улыбнулась, посеяв невообразимое спокойствие внутри меня."
    us "Девочка-енот?"
    us "Да Алиса о ней как-то рассказывала."
    us "Местная легенда."
    nd_il "Местная легенда..."
    hide us with dspr
    "Вторил я рыжей пионерке и опустил взгляд в пол, проматывая только что сложившийся между нами разговор..."
    "Возможно, в нём я сказал не всё так, как хотел, что-то не договорил."
    "Но тем не менее, результат впечатлил - Ульяне лучше."
    "И это для меня самое главное..."
    window hide

    $ renpy.pause(1, hard=True)
    show us normal pioneer at center with dspr
    
    window show
    us "Переоденешься?"
    nd_il "Да знаешь..."
    "Вдумчиво произнес я, а потом скорчил свою многозначительную улыбку."
    nd_il "В целом не помешало бы."
    show us grin pioneer at center with dspr
    us "Странный ты какой-то."
    us "Подожду пока на улице, поохраняю, чтобы никто не подглядывал."
    window hide

    play sound sfx_open_door_1
    $ renpy.pause (1, hard=True)
    hide us with dspr
    $ renpy.pause (1, hard=True)
    play sound sfx_close_door_1 

    window show
    "Ульяна выпорхнула из домика, аккуратно и в какой-то степени грациозно закрыв за собой входную дверь."
    "В ту минуту меня посетило несколько странных мыслей по поводу Ульяны и её поведения, но я не оставил им ни единого шанса."
    "У меня был план."
    "Мне нужно было только достать из шкафчика сложенную ею форму и осмотреть её..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    th "Поглажена идеально. Не думал, что она такая хозяйственная..."
    window hide

    $ renpy.pause(1, hard=True)
    show black with dissolve
    $ renpy.pause(3, hard=True)
    play sound nds_list['applysuit']
    hide black with dissolve
    $ renpy.pause(1, hard=True)

    window show
    "Наскоро переодевшись я бросил взгляд на форму, которая лежала на периле кровати."
    "Чего стоили шорты, удивляющие своей степенью повреждений, а рубашка..."
    "Вся она чёрная будто в ней работал не один шахтер на протяжение месяца без ухода и стирки."
    "Комментарии здесь были бы излишними, но я всё-таки попытался выдавить из себя что-то подходящее под вышеизложенное описание одежды."
    th "Жалкое зрелище..."
    window hide

    $ renpy.pause (1, hard=True)
    play sound sfx_open_door_1
    stop ambience fadeout 3
    $ renpy.pause (1, hard=True)
    play ambience ambience_camp_center_night fadein 3
    play music ndm_list['RF_club_music_1'] fadein 5
    scene bg ext_house_of_gg_night2 with dissolve
    $ renpy.pause (1, hard=True)
    play sound sfx_close_door_1 
    $ renpy.pause (1, hard=True)

    show us angry pioneer far at right
    show dv angry pioneer far at left 
    with dspr

    $ renpy.pause (1, hard=True)

    window hide
    "Закончив с подготовками и расправившись с ещё парой возникших мыслей, я решился наконец выйти на улицу."
    "И снаружи меня ждали Ульяна с Алисой, видимо, забывшие об этом в активном споре о чем-то своём."
    "Признаться, Алису я совсем не ожидал здесь увидеть. С ухода Ульяны из моего домика не так уж много времени успело пройти."
    dv "Так ты мне расскажешь...{w} О, Илья."
    hide dv with dspr
    show dv angry pioneer at left with dspr 
    "Обратив внимание на вышедшего из домика меня, Алиса подошла ко мне."
    dv "Может ты мне расскажешь, где вы с Ульяной были?"
    show dv rage pioneer at left with dspr 
    dv "Потому что кому-то сейчас может не поздоровиться."
    show us upset pioneer far at right with dspr
    us "Алис, да отстань ты от него!"
    us "Хочешь чаепитие - будет чаепитие."
    "Алиса перевела взгляд на Ульяну, потом посмотрела на меня, потом снова на Ульяну..."
    "Я не знал, что взбредет Алисе в голову дальше. Меня слишком быстро перенесло из обстановки с Ульяной наедине к обществу Алисы."
    show dv angry pioneer at left with dspr 
    dv "Ладно, тогда будет чаепитие у Ильи."
    hide dv with dspr
    "Алиса обошла меня стороной, тем самым дав себе возможность впустить себя в домик."
    "Поднявшись по небольшой лестнице она открыла дверь и не поворачиваясь добавила."
    dv "Ульяна, принеси конфеты нам с Ильёй, кипятильник, кружки,{w} чайные пакеты не забудь."
    "Сказала Алиса, закрыв дверь в мой домик."
    show us dontlike pioneer far at right with dspr
    us "Ну и ладно!"
    us "Ну и пожалуйста!"
    hide us with dspr
    "Ульяна показала язык и демонстративно отвернулась, направившись к своему домику."
    "Не знаю о чем мне нужно было сейчас думать, но я пошел за ней..."
    window hide

    stop ambience fadeout 3
    scene black with dissolve2
    $ renpy.pause (1, hard=True)
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_dv_night with dissolve
    play sound sfx_close_door_1

    window show
    "Я зашел в домик за Ульяной."
    show us dontlike pioneer at center with dspr
    nd_il "Что случилось то?"
    us "Да ничего."
    us "Алиса задолбала со своими вопросами."
    us "Без неё даже с места сдвинуться нельзя, везде свой нос суёт."
    hide us with dspr
    "Говорила Ульяна, попутно обыскивая домик в поисках кухонных принадлежностей, описанных Алисой ранее."
    nd_il "Ну так давай поступим с ней так же?"
    show us surp1 pioneer at center with dspr
    us "Как?!"
    "Вскрикнула Ульяна, достав из шкафчика однолитровую бутылку воды."
    hide us with dspr
    nd_il "Перевернём игру.{w} Заставим её рассказывать, что с ней сегодня было."
    nd_il "К тому же нас численно больше."
    show us normal pioneer at center with dspr
    "Ульяна замерла с кипятильником в руке."
    show us smile pioneer at center with dspr
    us "О, хорошая идея."
    show us grin pioneer at center with dspr
    us "Возьми пожалуйста вот это..."
    "Говорила Ульяна, протягивая мне бутылку воды, кипятильник и упаковку с пакетиками чая."
    us "...А я возьму всё остальное."
    "Мы битком набили свои руки этими предметами и уже выходили из домика, едва открыв входную дверь."
    window hide

    stop ambience fadeout 3
    play sound sfx_open_door_1
    scene black with dissolve2
    $ renpy.pause(3, hard=True)
    play ambience ambience_int_cabin_night fadein 3
    play sound sfx_close_door_1
    $ renpy.pause(1, hard=True)
    scene bg int_house_of_gg_night with dissolve2

    window show
    "Мы отворили дверь и увидели Алису, развалившуюся на моей кровати и рассматривающую зарядник для телефона, который мне спаяли кибернетики."
    show dv grin pioneer far at left with dspr
    dv "А, вы уже? Так быстро?"
    "Алиса уже не выглядела такой злой."
    "Видимо, решила сменить тактику, либо ещё что-то задумала."
    "Мне нужно было срочно что-то решать с этим, пока она не начала вытаскивать из своих рукавов все козыри первой."
    dv "Илюх, а что это такое?"
    th "Лазает в моих вещах, лежит на моей кровати, что ей ответить?"
    nd_il "Алис, а чем ты сегодня занималась?"
    hide dv with dspr
    "Проигнорировал её вопрос я, подойдя к столу, положив кипятильники с пол ладони размером, бутылку воды и остальные вещи аккуратно на стол."
    show dv surprise pioneer at left with dspr
    "Алиса замешкалась, не услышав ответа на свой вопрос."
    "Видимо думала, что я буду проще."
    nd_il "Ладно, поговорим об этом за чашечкой горячего чая."
    nd_il "А сейчас: как вы встретились с Ульяной на улице? Что можешь сказать про сегодняшний случай с Семёном?"
    "Сказал я первое, что пришло в голову в надежде, что это сработает."
    show dv shocked pioneer at left with dspr
    dv "Откуда ты?.."
    "И к моему большому удивлению - это действительно сработало."
    "В домике повисла пауза между мной и Алисой.{w} Ульяна раскладывала кружки с блюдцами на стол."
    "Похоже они обе были достаточно удивлены от случившегося."
    "Похоже я попал в самую точку, сам того не желая."
    "И в моих планах было зацепиться за это в дальнейшем."
    "Я взглянул на Ульяну и дважды поднял брови."
    "Кажется, она меня поняла."
    "Через несколько секунд Ульяна нарушила тишину."
    show us smile pioneer at right with dspr
    us "Да, Алиса, нельзя же так."
    show dv guilty pioneer at left with dspr
    us "Сама обо мне все спрашиваешь, а о себе и не расскажешь."
    window hide

    stop music fadeout 4

    $ renpy.pause(2, hard=True)

    hide us
    hide dv 
    with dspr

    $ renpy.pause(2, hard=True)
    play music ndm_list['i_crash_u_crash'] fadein 6
    $ renpy.pause(1, hard=True)

    window show
    "Алисе было нечего ответить на это, как и мне.{w} Похоже желание расспрашивать что-то у неё точно отпало."
    "Мы сидели за столом, ждали пока кипятильники заварят воду в наших кружках."
    "И никак не могли завести разговор, после того как задушили Алису своими высказываниями."
    "Но зато хоть кто-то должен был её проучить..."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    nd_il "Алис..."
    show dv guilty pioneer at center with dspr
    dv "Ладно, ладно. Расскажу что там у меня сегодня было."
    dv "Семён просто назвал меня так, как меня называть не стоит."
    nd_il "Как?"
    show us normal pioneer at fright with dspr 
    us "Илья..."
    hide us with dspr
    show dv angry pioneer at center with dspr
    dv "Он назвал меня Два-Че..."
    dv "Бррр...{w} Ненавижу когда меня так называют..."
    "Сказала она с раздраженностью, непомерной злостью. Такой, что у меня отбилось желание вообще называть её по имени."
    show us normal pioneer at fright with dspr 
    us "И что ты с ним сделала на этот раз?"
    th "Да, судя по всему парня жизнь совсем не учит."
    dv "Я хотела его проучить, но он дал дёру как только заметил меня."
    dv "Завтра утром я с ним разберусь."
    th "Жалко пацана."
    if persistent.semen_dancelesson >= 1:
        th "Он же меня плясать учил..."
    
    hide us with dspr

    dv "Хотя может...{w} Сегодня ночью?"
    th "Надо его как-то предупредить."
    nd_il "Ладно, фиг-то с ним с Семёном. А что у вас с Ульяной случилось?"
    "Сделал я паузу, как будто не знал, что произошло."
    show dv guilty pioneer at center with dspr
    dv "Она отказывается рассказывать мне о своих задумках для розыгрышей. Постоянно уходит куда-то и не говорит куда..."
    nd_il "Алис, Ульяна не обязана рассказывать тебе это..."
    show us sad pioneer at fright with dspr 
    us "Да."
    nd_il "...И ты не обязана за ней следить и контролировать."

    hide us
    hide dv
    with dspr

    "Алиса замолчала и опустила голову вниз."
    "Тем временем кипятильники в наших чашках уже вскипятили воду."
    "Мы отключили их от сети и, достав пакетики с чаем, принялись его заваривать."
    "Аромат зеленого чая разлетелся по всему домику. Помогал ему в этом ветер, залетавший из открытой форточки."
    "Удивительно, что я только что заметил, что она открыта."
    "Похоже Алиса в мое отсутствие решила заодно проветрить комнату.{w} Хотя скорее всего форточка заранее была открыта Ульяной."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    nd_il "А что случилось с Семёном в первый раз? Ну, когда он сказал это..."
    show us grin pioneer at fright with dspr
    us "Ему не поздоровилось..."
    "Произнесла Ульяна, проведя большим пальцем с зажатым кулаком по шее."
    "От этого мне стало слегка не по себе."
    show dv normal pioneer at center with dspr
    dv "Да что мы всё о Семёне?"
    dv "Давайте о чем-нибудь другом."
    nd_il "Почему бы и нет?"
    hide us with dspr
    stop music fadeout 6
    dv "Кстати я давно спросить хотела..."
    th "Интересно, что она мне сейчас скажет?"
    th "Ожидаемо, что она начнет мне мстить."
    th "И если отвечу на её вопрос неправильно..."
    show dv smile pioneer at center with dspr
    dv "В первый день, когда двое неизвестных ограбили столовую..."
    play music ndm_list['mma_there'] fadein 5
    "Ульяна остановила руку на половине пути к пакету с конфетами и вернула её обратно к чашке чая, слегка отводя взгляд."
    "Эту реакцию Ульяны я заметил своим боковым зрением. Но Алиса не обращала на неё внимания. Её интересовал лишь я."
    nd_il "Это насчёт того, что мы не вернулись?.."
    dv "Да,{w} но вообще-то нет."
    show dv grin pioneer at center with dspr
    dv "Просто вас двоих не было тогда. А тех воров тоже было двое..."
    "Алиса улыбнулась, видимо в предвкушении моих дальнейших слов."
    "В ответ на это я вопросительно приподнял одну бровь, внутренне решив играть на опережение."
    nd_il "Ты намекаешь, что мы с Ульяной взломали столовую и ограбили её?"
    nd_il "Это было бы странно. К тому же я не умею взламывать замки."
    show dv normal pioneer at center with dspr
    nd_il "Да и Ульяна вряд ли обладает подобными навыками."
    "Алиса замолчала на пару секунд, потом сказала:"
    show dv smile pioneer at center with dspr
    dv "Ага, тогда это я взломала столовую?"
    nd_il "А может быть ты была с ними?"
    show dv normal pioneer at center with dspr
    dv "Я не была с ними."
    nd_il "А где ты тогда была?"
    dv "Рядом проходила и заметила одного из них."
    th "Интересная уловка."
    "Подумал я и отхлебнул немного чая."
    "Девочки повторили это действие за мной."
    nd_il "И совсем ему не помешала?"
    show dv guilty pioneer at center with dspr
    dv "Я испугалась!"
    nd_il "И поэтому помогла ему взломать эту столовую."
    dv "Он мне угрожал!"
    us "Он тебе не угрожал!"
    "Ульяна резко вмешалась в диалог."
    show us normal pioneer at fright with dspr 
    us "Ты сама открыла ему столовую."
    "Закинув конфету в рот она продолжила."
    show us dontlike pioneer at fright with dspr 
    us "А потом выбежал ещё один и забрал все булки из буфета."
    us "Ты соучастница."
    show dv scared pioneer at center with dspr
    dv "Стоп! Откуда вы..."
    show us grin pioneer at fright with dspr 
    us "И врунишка!"
    nd_il "Алиса, мы понимаем, что ты испугалась, и под испугом открыла им столовую."
    nd_il "Но ты понимаешь, что являешься в этом деле соучастницей?"
    show dv shocked pioneer at center with dspr
    dv "Да но..."
    nd_il "И не можешь рассказать об этом ни администрации лагеря, ни вожатой."
    nd_il "Это мы ограбили столовую!"
    show us smile pioneer at fright with dspr 
    us "И нам за это не стыдно!"
    window hide

    stop music fadeout 5
    $ renpy.pause(1, hard=True)
    show black with dissolve2
    $ renpy.pause(3, hard=True)
    hide us
    hide dv
    $ renpy.pause(1, hard=True)
    hide black with dissolve 

    window show
    "Ульяна потянула руку к конфетам и взяла одну, самую-самую большую."
    show dv grin pioneer at center with dspr
    dv "Ладно, ребят я, конечно, догадывалась, что это вы."
    dv "Но вы бы хотя бы долей со мной поделились."
    show dv normal pioneer at center with dspr
    nd_il "Этого не входило в наши планы..."
    show us smile pioneer at fright with dspr 
    us "Может быть, если будешь хорошо себя вести, то в следующий раз мы пойдем на ограбление вместе."
    hide us
    show dv guilty pioneer at center
    with dspr
    dv "Да ты вообще молчи."
    "Фыркнула на Ульяну Алиса."
    dv "С самого начала все одна делала, мне не доверяла."
    dv "А с ним прямо в первый же день взяла и на ограбление пошла."
    dv "Забыв про свою лучшую подругу."
    show us surp1 pioneer at fright with dspr
    us "Тебе надо было себя нормально вести."
    us "Если бы ты хотя бы себя так не вела."
    us "И не пила эту свою...{w} Водку..."
    window hide

    hide us
    hide dv 
    with dspr

    $ renpy.pause(3, hard=True)

    show prologue_dream with dissolve2

    $ renpy.pause(1, hard=True)
    
    window show
    "Через некоторое время спор утих."
    "Между делом мы выпили не одну кружку чая,{w} съели не одну конфету,{w} начали не одну тему и не одну закончили."
    "Время уже переваливало за полночь."
    "Мы с девочками выпили всю воду.{w} Ульяна съела почти все девяносто процентов от всех конфет.{w} В пакете не осталось ни одной."
    window hide

    $ renpy.pause(1, hard=True)
    stop ambience fadeout 3
    show black with dissolve
    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_1
    $ renpy.pause(1, hard=True)
    play sound sfx_close_door_1
    $ renpy.pause(1, hard=True)

    window show
    "Потихоньку мы начали собираться относить всё в домик Алисы и Ульяны."
    "Поделив весь груз на троих, мы вышли из домика..."
    window hide

    $ renpy.pause(4, hard=True)
    
    window show
    "Когда весь груз был отнесён, Алиса попросила Ульяну проводить меня..."
    window hide
    
    play sound sfx_open_door_1
    $ renpy.pause(2, hard=True)
    play ambience ambience_camp_center_night fadein 4
    play sound sfx_close_door_1
    $ renpy.pause(3, hard=True)

    $ pixellate2 = Pixellate(1.0, 5)
    scene bg ext_home_night with pixellate2
    $ renpy.pause(1, hard=True)
    show us normal pioneer at center with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Мы стояли друг напротив друга.{w} Я разглядывал радужку глаз Ульяны, попутно понимая, что я не хочу терять её взгляда."
    
    play music ndm_list['nd_crybaby'] fadein 4

    "Мне будто не хватает времени, проводимого рядом с ней."
    "Я понял, что ещё многого ей не рассказал, о многом с ней не поговорил."
    "Безусловно, завтра будет новый день. Но где гарантии, что этот вечер не станет для меня последним в этом лагере?"
    "В том самом, из которого я недавно хотел бежать, и который теперь не могу избавить от своего существования."
    "Когда-нибудь я начну здесь выживать, если не смогу уехать отсюда или если не произойдет чего-то плохого."
    "Я застряну тут, словно в книге про Робинзона Крузо авторства Даниеля Дефо."
    "Одна из книг, потерявшая свой смысл при переводе Чуковским на великий и могучий."
    window hide

    $ renpy.pause(2, hard=True)
    show us shy pioneer at center with dspr

    window show
    us "Спасибо, что составил компанию на этот вечер."
    us "И там, в старом лагере... И в общении с тем пионером..."
    us "Ты вёл себя прям так..."
    "Было заметно,{w} что она пытается подобрать правильные слова к своим мыслям."
    us "Прости за мой розыгрыш,{w} ещё раз."
    us "Я постараюсь меньше тебя разыгрывать..."
    nd_il "Ульяна, не стоит за это извиняться..."
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Ульяна подошла ко мне ближе и крепко, очень нежно объяла руками."
    show blink
    "Дыхание стало прерывистым. Я рефлекторно прижал её к себе и закрыл глаза."
    "Запах её духов вперемешку с свежим, слегка влажным ночным воздухом прорвался ко мне в лёгкие."
    "По ощущениям сердцебиение существенно замедлилось."
    "Я почувствовал то, чего не чувствовал ранее."
    "Это было похоже на нирвану. Но не в общепринятом её понятии."
    "Ведь для её достижения потребовалось всего лишь появиться в неизвестном месте в неудобное для меня время."
    "От меня потребовалось только быть рядом с этой красноволосой милой девочкой."
    "Той, которую я не хотел больше отпускать из этих объятий никогда..."
    window hide

    $ renpy.pause(1, hard=True)
    
    show us shy2 pioneer at center
    hide blink
    show unblink

    window show
    nd_il "И тебе спасибо."
    us "Завтра увидимся..."
    nd_il "Обязательно."
    window hide

    $ renpy.pause(2, hard=True)
    hide us with dspr
    $ renpy.pause(3, hard=True)

    window show
    "Когда Ульяна уходила к своему домику, и даже когда скрылась за углом, я всё ещё стоял и смотрел на неё будто через стены."
    "Меня одолевали чувства, однако мозг отбрасывал их в сторону, будто защищаясь от своей перегрузки."
    nd_il "Увидимся завтра..."
    window hide

    stop ambience fadeout 4
    show black with dissolve2
    $ renpy.pause(2, hard=True)
    play sound sfx_open_door_1
    play ambience ambience_int_cabin_night fadein 3
    scene bg int_house_of_gg_night_1 with dissolve2
    play sound sfx_close_door_1

    window show
    "Зайдя на автопилоте по лестнице и завалившись в домик, я почти сразу же начал готовиться ко сну."
    "Я разделся, аккуратно повесил свою пионерскую форму на спинку кровати (так как утром мой домик проверяла Ольга Дмитриевна, разбрасывать свои вещи не очень хотелось)."
    "Расправив кровать, я достал из тумбочки свой телефон и решил перед сном (от нечего делать) упорядочить альбомы с фотографиями. "
    "Пока я это делал, в голову лезли навязчивые мысли о произошедшем сегодня, о жутких шахтах, стрёмном старом лагере.{w} Но самое главное о ней{w} - Ульяне."
    "Я не понимал, к чему я иду, ради чего я в этом лагере. Но мне не хотелось отсюда уезжать."
    "Я за эти четыре дня так привык к его обитателям. И уже невозможно было сделать ход назад.{w} Словно я нахожусь на шахматном поле среди черных и белых плиток и фигур."
    "Поначалу было непривычно быть пешкой среди всего механизма, но потом ты вживаешься в роль, находишь в этом что-то, и уже не в состоянии остановиться."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Внезапно среди своих фото я заметил одно очень пугающее."
    "Это было моё селфи с тем, уже {i}мёртвым{/i} пионером."
    "Я попытался открыть это фото, но меня встретила ошибка «Фото по заданному пути не найдено или отсутствует»."
    "Вернувшись в галерею, я вновь увидел миниатюру этого фото."
    "Я принялся судорожно протирать свои глаза, и после этой процедуры фото исчезло из галереи."
    th "Всё, надо спать. Точно спать."
    "Подумал я и, вытащив аккумулятор, поставил его на зарядку."
    "Повернувшись на правый бок, я укрылся одеялом и закрыл глаза."
    "Я вспомнил тот случай с Алисой во время чаепития, и он отразился улыбкой на моем лице."
    window hide

    $ renpy.pause(1, hard=True)

    stop music fadeout 3
    stop ambience fadeout 3
    show blink

    $ renpy.pause(3, hard=True)

    window show
    "Но всё же беспокойное чувство никак не хотело покидать меня."
    "Вскоре от него меня избавило воспоминание об объятиях Ульяны..."
    "Запах её духов вновь прорвался ко мне в грудь, словно она сидела со мной рядом."
    "Было ли это предсонным состоянием, или она действительно сидела рядом с спящим мной - было не ясно."
    "Но что точно ясно - это чувство мне нравилось."
    "И вновь я проваливался в сон..."
    window hide

    $ renpy.pause(2, hard=True)

    jump nd_day_5_start

    # Ульяша <3