label nd_c2_partFive:

    $ new_chapter(1, u"Фикционализм\nЧасть V - Костюм")
    $ renpy.pause(2, hard=True)
    play ambience nda_list['ambience_empty_street'] fadein 5
    scene nd_g_2_part_5 with dissolve2
    $ renpy.pause(2, hard=True)
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    scene bg mnog_ext_evening with dissolve3

    window show
    nd_il "Я никому тебя не отдам…"
    "Я успокаивал Ульяну, гладил её плечи и смахивал скатывающиеся с щёчек слёзы."
    "Я обещал ей, что всё это позади, что старая глава нашей с ней истории закончилась, и в какой-то момент даже подумал, что мои объятия подействовали."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "С её поцелуем в щёчку немногое изменилось."
    "Мысли в моей голове никак не укладывались, а отголоски воспоминаний били по голове."
    "Это сравнимо с последствиями амнезии."
    "Голова не болела, но было чувство, что я сам не свой, что это тело принадлежит не мне, что этот «я» совсем не я."
    "Однако внешность, строение тела, конечности – всё это говорило об обратном."
    "Эти мысли не давали мне покоя, и я решился поставить точку в них, спрятав запястья под костюм."
    window hide

    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(2, hard=True)
    $ nd_change_time('night')
    play ambience nda_list['ambience_street_night'] fadein 4
    scene bg mnog_ext_night with dissolve3

    window show
    "Вечерело. Ульяна успокоилась и просто сидела рядом со мной на скамеечке, опустив голову мне на плечо."
    nd_il "Уля…"
    show us normal nd_dress close at right with dspr
    us "Умм?"
    nd_il "Если бы ты влюбилась в шахтёра и он сказал бы тебе, что добудет тебе любой драгоценный камень, который ты попросишь, что бы ты ему ответила?"
    us "Ну..."
    show us smile nd_dress close at right with dspr 
    us "Я бы ему ответила что люблю не его а Илюшу."
    us "Илюша мне что угодно принесёт, хоть алмаз, хоть рубин."
    nd_il "Ты абсолютно права..."
    hide us with dspr
    "Ульяна опять положила на меня голову и вздохнула. Я приобнял её и прижал к себе."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    us "Колечко хочешь мне подарить?"
    "Украдкой спросила она."
    th "Увидишь…"
    "Проговорил я у себя в уме, впоследствии выставив себе же обвинения в том, что так неосторожно сдал свой план."
    "Я люблю её и не могу перестать дарить ей подарки, если это делает её счастливой."
    "В чём же я не прав?"
    window hide

    $ renpy.pause(1, hard=True)

    show us shy nd_dress close at center with dspr

    window show
    us "А купи мне сникерс."
    "Произнесла вдруг она и посмотрела на меня своим голубыми глазками-алмазами."
    nd_il "Всё для тебя, солнышко."
    hide us with dspr
    "Сказал я вставая со скамейки. Ульяна встала вслед за мной."
    "Обняла меня за руку и положила голову на мое предплечье."
    "Только теперь я cмог ощутить приятный ветер, создающий мурашки на моей коже."
    nd_il "Магазин недалеко отсюда. Буквально в двух шагах, пошли..."
    window hide

    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(4, hard=True)
    $ nd_change_time('day')
    play ambience nda_list['ambience_int_shop_n'] fadein 4
    scene bg int_shop_neutrall with dissolve2

    window show
    "Мы гуляли по этому магазину, среди закрытых стеклом полок и холодильников."
    "Это было медитативное действо, поскольку я прежде никогда бесцельно не блуждал по магазинам."
    "Всегда была вещь, которую нужно купить. А тут..."
    "...Мы просто зашли купить сникерс."
    window hide
    
    $ renpy.pause(2, hard=True)
    show us shy2 nd_dress at right with dspr
    $ renpy.pause(0.5, hard=True)

    window show
    us "Илюш, нужно купить для меня ещё кое-что."
    us "Ты не забыл?"
    us "Мы обсуждали..."
    hide us with dspr
    nd_il "Да, я помню."
    nd_il "Давай купим {i}это{/i} ближе к дому."
    show us shy nd_dress at right with dspr
    us "Хорошо, просто боюсь, что оно опять может...{w=0.4} {i}Потечь...{/i}"
    hide us with dspr
    "Я ненадолго задумался, затем отмахнулся от лишних мыслей и продолжил путешествие по магазину."
    nd_il "Всё будет хорошо, мы погуляем ещё немного и пойдем домой..."
    us "Угу..."
    "Ульяна всё это время держала меня за руку."
    th "В такой сложный для неё период важно быть рядом с ней..."
    th "Я буду стараться придерживаться этому правилу..."
    window hide

    $ renpy.pause(3, hard=True)

    window show
    "Прошло около пяти минут. Ничего полезного в этом минимаркете я не нашел."
    "То что можно было сейчас быстро съесть лежало у кассы. На такие товары распространялась скидка,{w} но сейчас мне об этом не нужно было даже думать."
    nd_il "Батончики у кассы."
    "Нарушив тишину констатировал я."
    show us normal nd_dress at right with dspr
    us "А зачем мы тут тогда гуляли?"
    nd_il "Я думал, тогда ты предложишь купить тебе ещё что-то."
    us "Илюш, всё что мне нужно у меня уже есть."
    hide us with dspr
    "Сказала Ульяна и тыкнула в мою грудь пальчиком."
    "Я улыбнулся, скрывая внутреннее волнение."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Я взял с полки сначала один батончик для Ульяны, а потом второй для себя."
    th "Не мир вокруг меня изменился.{w} Изменился я."
    th "И город не так уж плох.{w} Только каким было бы моё мнение, если бы не девочка, которую я держу за ручку?"
    cassw "С вас 104 рубля."
    nd_il "Картой..."
    window hide
    
    $ renpy.pause(1, hard=True)
    play sound sfx_inhale
    $ renpy.pause(2, hard=True)
    play sound nds_list['nd_pluck_cas']

    window show
    "Сглотнув необъяснимое волнение, я поднёс свою карту к устройству на кассе, и оно издало противный короткий писк."
    "Мне показалось на секундочку, что у меня недостаточно средств, но улыбка кассирши развеяла эти мысли."
    cassw "Спасибо за покупку.{w} Приятного вечера!"
    nd_il "Спасибо..."
    "Тихо проговорил я..."
    us "Вам тоже приятного вечера!"
    "...и восторженно прокричала Ульяна."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Ловя за спиной удивленный взгляд кассирши, мы выходили на улицу..."
    window hide

    $ renpy.pause(1, hard=True)
    stop ambience fadeout 3
    scene black with dissolve
    $ renpy.pause(3, hard=True)
    $ nd_change_time('night')
    play ambience nda_list['ext_store_nn'] fadein 4
    scene bg ext_shop_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Один батончик сникерса я отдал Ульяне, а второй оставил себе, раскрыл и сделал надкус."
    show us normal nd_dress at center with dspr
    us "Илья, что-то случилось?"
    nd_il "Уля, ты пойдешь со мной?"
    show us smile nd_dress at center with dspr
    us "А почему нет?"
    th "Действительно, почему?"
    nd_il "Хорошо, поможешь выбрать тебе следующий твой подарок..."
    show us surp3 nd_dress at center with dspr
    us "Подарок?"
    nd_il "Да, он тебе точно понравится."
    show us shy2 nd_dress at center with dspr
    us "Это то что я думаю?"
    "Я слегка улыбнулся, видя то, как она смущается."
    nd_il "Возможно и то, что ты думаешь.{w} Пошли..."
    window hide

    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(3, hard=True)
    play ambience nda_list['ambience_pereu_city_night'] fadein 4
    play sound_loop sfx_far_steps fadein 4
    play back_ambience nds_list['sfx_far_steps_asph'] fadein 4
    scene bg nd_ext_pereuu_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Идя по освещенной фонарями плитке, сложно не окунуться в себя и не задумываться над чем-то."
    "Тот факт, что мы идём с Ульяной в полной тишине уже по меньшей мере 3 минуты, меня немного смущал."
    "Я ждал пока она нарушит это молчание, сам этого сделать я не мог."
    "Я посмотрел на неё..."
    "Она тоже думала о чём-то своём."
    "Эта магия никогда не растворится."
    "Разве что только тогда, когда мы подойдём к ювелирному магазину."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Когда любимый человек держит тебя за руку - любые слова излишни."
    "А когда ты думаешь о нём - сердце разгоняется..."
    "Всё это называется одним словом - любовь."
    th "Всего одним словом?"
    th "Всё что я чувствую сейчас это всего-лишь одно слово? Нет... Это должно быть что-то больше, чем термин."
    th "Чувства влюблённости по сути же бывают разные. У всех свои."
    nd_il "Ульяна, я сейчас подумал..."
    nd_il "Ни в одном языке нет слова чтобы описать мои чувства к тебе."
    window hide
    
    stop sound_loop fadeout 1
    stop back_ambience fadeout 1
    $ renpy.pause(1, hard=True)

    window show
    "Ульяна остановилась. И я вместе с ней..."
    show us shy2 nd_dress close at center with dspr 
    us "Я сейчас заплачу, это так мило."
    window hide

    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)

    window show
    "Ульяна медленно прильнула ко мне и обняла, прижав к себе настолько, насколько смогла."
    nd_il "Я бы тоже расплакался, солнышко."
    nd_il "Всё что мне нужно было всё это время - это ты."
    us "И мне...{w=0.5} ты..."
    window hide

    stop ambience fadeout 4
    $ renpy.pause(3, hard=True)
    play music ndm_list['nd_nachalo_1'] fadein 4
    scene black
    show splatter_notdream 
    with dissolve3

    window show
    nd_il "Уль, какое колечко ты хочешь?"
    us "Какое-нибудь ак-куратное, крас-сивое. Во-о-от это!"
    je_stor "Вот, девушка, примерьте. Оно должно вам подойти."
    us "Красивое, Илья, купи!"
    nd_il "Всё для тебя, солнышко..."
    us "Спасибо!"
    nd_il "Мы берём его, картой можно оплатить?"
    je_stor "Конечно..."
    nd_il "И ещё колечко для меня, какое-нибудь попроще..."
    window hide

    $ renpy.pause(1, hard=True)
    stop music fadeout 4
    scene black with dissolve2
    $ renpy.pause(4, hard=True)
    play ambience nda_list['ambience_pereu_city_night'] fadein 4
    scene bg nd_park_night with dissolve2
    $ renpy.pause(2, hard=True)

    window show
    "Мы шли по улице, где не было никого. Только фонари освещали нам путь."
    "Такая атмосфера показалась мне романтичной."
    "С моего лица не слазила улыбка."
    nd_il "Покажи как колечко на тебе смотрится."
    show us surp3 nd_dress at center with dspr
    us "И ты тогда своё!"
    "На наших безымянных пальцах были два красивейших колечка. Моё, конечно, попроще, но мне нравилось."
    show us shy2 nd_dress at center with dspr
    us "Мы прямо как муж и жена."
    nd_il "Да, только чего-то не хватает для этого..."
    us "Чего?"
    window hide

    play music ndm_list['pyro_days_n_nights'] fadein 3
    $ renpy.pause(1, hard=True)
    hide us with dspr
    $ renpy.pause(1, hard=True)
    
    window show
    "Я останавливаюсь, слегка приобнимаю Ульяну и целую её."
    "Она кладет руки на мои плечи и прижимается ко мне."
    "Я вновь ловлю аромат её духов и волос.{w} Это может продолжаться вечность..."
    "По крайней мере я хотел бы, чтобы этот поцелуй длился именно столько."
    window hide

    $ renpy.pause(1, hard=True)
    scene bg nd_park_night_blur with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Я почувствовал, как её рука сжимает мой пиджак на спине, потом аккуратно ложится на волосы."
    "Ладонь проходит по шее и останавливается там, где был оставлен след от укуса."
    nd_il "Я боюсь тебя потерять."
    show us shy nd_dress close at center with dspr
    us "А я боюсь остаться тут одной."
    hide us with dspr
    "Рука Ульяны проходит по пуговицам моей рубашки и падает."
    "Наши ладони соприкасаются друг с другом,{w} пальцы разъединяются,{w} проходят друг в друга..."
    show us shy2 nd_dress close at center with dspr
    nd_il "Никогда не останешься."
    nd_il "Мы всегда будем вместе."
    "Я почувствовал мятный привкус спустя пару тройку секунд, как мы прекратили поцелуй."
    us "Навеки вечные..."
    "Её глаза сверкают.{w} Я вижу в них своё отражение."
    "Если бы мы стояли на льду, то он бы уже давно растаял от обилия любви между нами."
    window hide

    hide us with dspr
    $ renpy.pause(2, hard=True)
    with vpunch

    window show
    "Ульяна врезалась в мою грудь, обхватила меня одной рукой и прижала к себе."
    "Наши ладони остаются в объятиях друг друга."
    show us shy2 nd_dress close at center with dspr
    us "Не отпускай...{w} Ты у меня самый лучший!"
    nd_il "Ты моя единственная..."
    window hide

    hide us with dspr
    $ renpy.pause(1, hard=True)
    scene bg nd_park_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Уже спустя секунду мы садимся на скамейку и продолжаем наши объятия."
    "Она не просто обнимала меня.{w} Она гладила свою щеку о мою,{w} а когда я провел рукой вдоль её спины, её всю бросило в дрожь."
    "Но это её не остановило."
    "Она издала тяжелый вдох, на выдохе проговорив:"
    show us shy2 nd_dress close at center with dspr
    us "Я люблю тебя, Илюш..."
    nd_il "Я тебя тоже люблю,{w} моя звёздочка..."
    window hide

    hide us with dspr
    stop music fadeout 7
    $ renpy.pause(2, hard=True)

    window show
    "Даже спустя время она не хотела выпускать меня из объятий.{w} Мы почти лежали на скамейке."
    "Я слышал её тихое сопение, пока та не решила нарушить тишину..."
    us "Сейчас посидим чуть-чуть и вызовем такси."
    nd_il "Угу..."
    "В этот момент я поймал себя на мысли, что всё, к чему я шёл, было не зря."
    th "А к чему я шёл?"
    th "Рядом с ней - уже не важно.{w} Ничего не важно.{w} В этом мире только мы вдвоем..."
    window hide
    
    $ renpy.pause(1, hard=True)
    stop ambience fadeout 3
    scene black with dissolve3
    $ renpy.pause(4, hard=True)
    ###
    $ volume(0.1, 'back_ambience')
    ###
    play ambience nda_list['ambience_int_apartaments_neutral'] fadein 3
    play back_ambience nda_list['backambience_city_loud'] fadein 3
    play music ndm_list['lizer_younger'] fadein 4
    scene bg nd_ext_cv_night with dissolve2

    window show
    "Вот мы вновь рядом..."
    "Я согреваюсь рядом с ней в тёплой кроватке."
    show blink
    "Окно в моей комнате открыто.{w} Оттуда веет необыкновенной прохладой и...{w} Звуками какого-то Готема или Комптона..."
    "Тем не менее, они совсем не мешают. Мне всё равно не спится."
    window hide

    $ renpy.pause(2, hard=True)

label nd_c2_partSix:

    $ new_chapter(1, u"Фикционализм\nЧасть VI - Возьми меня обратно...")

    hide blink
    scene bg nd_ext_cv_night
    show unblink

    window show
    "Я вспоминал парк,{w} Ульяну с её тонкими плечами и извилистыми волосами, укутывающими меня перед тем, как мы легли в кровать.{w} Сегодня мы \"поженились\"..."
    nd_il "Хорошо погуляли."
    "В дребезги разрушив молчание, пролепетал я своей девочке на ушко."
    us "Угу..."
    "Уставшая Ульяна не понимает, что творится сейчас у меня в голове."
    "Это мысли, которые я не мог себе никак допустить раньше."
    "Но этот мир напомнил мне о том, как это было..."
    "Как я, примеряя свой костюм там, в примерочной, буквально сходил с ума от надвигающейся на меня бури."
    "С виду я выглядел обычным человеком, что не скажешь о моей предыдущей жизни, но внутри меня полыхал огонь."
    "Целый космос внутри моей комнаты, укрывающий нас с Ульяной словно тёплый плед."
    "Как мне описать свою любовь?{w} Это чувство сжимает мою грудь, руки невольно прижимают Ульяну ко мне."
    "Я один чувствую любовь именно так?{w} Или каждый человек чувствует её по разному?"
    window hide

    $ renpy.pause(1, hard=True)
    play sound nds_list['sfx_bed_squeak_2']
    $ renpy.pause(1, hard=True)
    
    window show
    "Ульяна повернулась на другой бок, отпустив мою руку, а потом снова положила её на свою талию."
    th "Не спит..."
    th "Никогда не сказал бы ей что она маленькая, но внутри себя понимаю это."
    th "Она ещё ребёнок. Что я нашёл в ней?{w} А она во мне?{w} Чёрт, я уже начинаю уставать."
    stop music fadeout 4
    th "Заткнись внутренний голос."
    th "На кой черт ты теперь предаешь меня анафеме?"
    th "Ладно...{w} Продолжай."
    th "Ты уже близко к своему прошлому."
    th "Ты возвращаешься в тот вечер..."
    window hide

    $ renpy.pause(1, hard=True)
    stop back_ambience fadeout 4
    stop ambience fadeout 4
    $ renpy.pause(2, hard=True)
    show blink
    $ renpy.pause(2, hard=True)
    scene black
    hide blink
    $ nd_change_time('prolog')
    play sound_loop sfx_bus_interior_moving fadein 3
    scene bg int_bus_black at nd_bus_vpunch
    show prologue_dream
    show unblink
    
    $ renpy.pause(2, hard=True)

    window show
    strange_g "Скучаешь по ней?.."
    nd_il "Даша, как ты думаешь, мы с ней ещё увидимся?"
    nd_da "Не знаю, Илья. Вы в лагере так хорошо общались. Ты любил её?"
    nd_il "Да."
    nd_da "Тогда почему ты не признался ей?"
    nd_il "Я боялся..."
    nd_da "Что не ответит взаимностью?"
    nd_da "Она всегда хотела быть рядом с тобой, приходила к твоему домику по утрам."
    nd_da "Думаешь это просто так?"
    nd_il "Я уже ни о чем не думаю."
    "Я держал эту прощальную записку у себя в руках."
    "Хотелось плакать - не было слез.{w} Я не рассчитывал когда-либо увидеть её.{w} Какое же у неё имя?"
    "Ульяна?"
    "Эта смена так быстро закончилась. Я не успел ей ещё многое сказать."
    "Я скажу...{w} Когда-нибудь, но не сейчас..."
    window hide
    
    $ renpy.pause(1, hard=True)
    stop sound_loop fadeout 4
    show blink
    $ renpy.pause(3, hard=True)
    scene black
    play ambience nda_list['ambience_int_apartaments_neutral'] fadein 3
    play back_ambience nda_list['backambience_city_loud'] fadein 3
    scene bg nd_ext_cv_night with dissolve2

    $ renpy.pause(1, hard=True)

    window show
    th "Оставил ещё одну непрожитую жизнь за своей спиной..."
    th "Что это за видения такие?..."
    th "Кажется... Я начинаю понимать их природу. Нужно выйти на кухню и попить..."
    th "А для этого нужно встать, да так, чтобы не разбудить Улю."
    "Я взглянул на мирно спящую, изредка сладко сопящую девочку."
    "Когда она спит, даже лишнее движение сделать страшно..."
    "До того не хотелось мне её случайно разбудить..."
    window hide

    $ renpy.pause(2, hard=True)
    $ volume(0.1, 'sound')
    play sound sfx_knock_door_closed_hard1
    $ renpy.pause(1, hard=True)
    play sound sfx_knock_door2
    $ renpy.pause(0.5, hard=True)

    window show
    "Неназойливый стук в дверь моей квартиры окончательно привёл мои мысли в порядок."
    "Ульяна спала уже крепким сном, моя рука была свободна."
    window hide
    
    $ renpy.pause(1, hard=True)
    stop back_ambience fadeout 4

    scene black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg nd_kvart_pr_night with dissolve

    window show
    "Я аккуратно поднялся с кровати и прошёл в коридор, чтобы взглянуть в дверной глазок."
    "Беглый взгляд на Ульяну - не проснулась, всё в порядке."
    "Через дверь послышался гулкий знакомый голос."
    fx_pe "Илья, я знаю что ты тут. Мне нужна помощь."
    "Моя рука сама легла на замок, когда я увидел, кто стоит за дверью..."
    fx_pe "Помоги!"
    window hide

    $ renpy.pause(0.5, hard=True)
    $ volume(1.0, 'sound')
    $ volume(1.0, 'back_ambience')
    play sound sfx_lock_open_close_1
    $ renpy.pause(1, hard=True)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1, hard=True)
    play sound sfx_lock_open_close_1
    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_mines
    $ renpy.pause(2, hard=True)
    play music music_list['no_tresspassing'] fadein 3
    show pi2 normal shirt at center with dissolve2
    $ renpy.pause(1, hard=True)
    play sound sfx_close_door_1

    window show
    "Земля раскололась под моими ногами."
    "Он тяжело дышал. Видимо, торопился сюда."
    nd_il "Кто ты?"
    show pi2 serious shirt at center with dspr
    fx_pe "Я уже не представляю, кем я могу быть."
    fx_il "Раз уж мы так с тобой похожи, давай называть меня Ильёй, как и тебя, наверное..."
    "Мы выглядели одинаково.{w} Я хотел начать задавать ему свои вопросы, но он не дал для них пространства в разговоре."
    fx_il "Мне нужно найти Вику."
    fx_il "Человек в моём сне мне сказал, что нужно прийти сюда и с твоей помощью я смогу её найти."
    fx_il "Ты не поймёшь, но она умерла в моем сне, когда мы перенеслись в этот мир.{w=1} А потом выжила..."
    "Я завис на одном месте. Его слова растворились внутри моей головы."
    th "Вика? Что значит \"она умерла\"?"
    th "Что происходит?"
    show pi2 shocked shirt at center with dspr
    nd_il "Я понятия не имею про какую Вику ты говоришь."
    fx_il "Мы познакомились с ней... В лагере...."
    fx_il "Я понимаю, что звучит безумно, но..."
    fx_il "Получается тот человек меня обманул?"
    nd_il "Я... Не знаю..."
    show pi2 serious shirt at center with dspr
    fx_il "Он ещё дал мне координаты, я записал их на листок."
    "Сказал он и, достав из кармана смятый листочек размером с билет, протянул его мне."
    window hide
    
    show nd_g_2_part_6_text with dissolve2
    $ renpy.pause(1, hard=True)
    hide nd_g_2_part_6_text with flash

    window show
    "Там были две большие цифры через запятую."
    nd_il "Я, кажется, понимаю, о чём ты."
    show pi2 shocked shirt at center with dspr
    fx_il "Правда? Ты выглядишь ровно как я..."
    fx_il "Мы сможем найти Вику?"
    nd_il "Только при условии, если я смогу сохранить рядом с собой Ульяну."
    fx_il "Не переживай, всё получится, у каждого из нас своё драгоценное счастье."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я посмотрел на него.{w} Его взгляд пронзил мою грудь."
    "Я забыл навык дыхания. Казалось, что я вот-вот умру."
    nd_il "Я знаю что хотел человек из твоего сна..."
    nd_il "Мы садимся в машину и едем на место."
    nd_il "Я чувствую, что мой конец близок как никогда..."
    window hide

    $ renpy.pause(2, hard=True)
    hide pi2 with dissolve
    $ renpy.pause(1, hard=True)
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    play sound sfx_open_door_mines
    stop ambience fadeout 4
    $ renpy.pause(1, hard=True)

    play ambience nda_list['ambience_int_elevator'] fadein 3
    scene bg nd_int_elevator with flash

    $ renpy.pause(1, hard=True)

    window show
    "Я понимал, в какой-то мере моё решение было довольно необдуманным, возможно, неправильным."
    "Я оставил Ульяну в своей квартире и пошел вслед за этим Ильёй."
    "Но что-то внутри меня подсказывало - так и должно быть."
    "У всего должен быть свой конец. Конец моей любви, конец моим страданиям, конец..."
    "А что такое конец? Возможно это только начало чего-то нового..."
    "Именно к такому концу я и стремлюсь."
    "Мой конец не должен стать для меня смертью, разочарованием, или другой негативной эмоцией, утратой."
    "Если я твёрдо решил покончить с этой симуляцией, я обязан вернуться туда, где меня ждёт Ульяна...{w} Моя Ульяна..."
    window hide

    $ renpy.pause(2, hard=True)
    stop music fadeout 4
    stop ambience fadeout 4
    scene black with dissolve3
    $ renpy.pause(3, hard=True)
    $ volume(0.01, 'ambience')
    play ambience nda_list['ambience_city_ambient'] fadein 4
    play music ndm_list['сoconuts_silver_lights'] fadein 4
    scene bg nd_park_zone_fix with dissolve2

    window show
    "Мы вышли за многоэтажку, где я жил.{w} На парковку."
    "Казалось бы, сколько живу в этом месте, а на парковку ни разу не заходил."
    th "Неужели нам предстоит сейчас вот так просто угнать авто?"
    "Я осмотрелся."
    "Между белыми полосами стояли несколько машин. Илья из другой вселенной подошёл к одной из них и отпер дверь."
    th "Н-да, неожидал что вопрос решится так просто..."
    nd_il "У тебя есть машина?"
    fx_il "Да, залезай. Я подготовился заранее."
    "Передо мной стояла Toyota Sprinter. Так, по крайней мере, было написано на ней."
    nd_il "Ты её украл?"
    fx_il "Одолжил. Все равно мы тут последний день. Так ведь?"
    fx_il "Этой ночью нас уже никто не сможет найти, все спят и никому дела нет до того, что происходит на этой парковке."
    fx_il "Завтра это уже потеряет смысл.{w=1} Живи моментом!"
    th "Как подло по отношению к автовладельцу..."
    th "Подло, но в то же время, ситуация безвыходная.{w} Надо действовать."
    window hide
    
    $ renpy.pause(2, hard=True)

    window show
    "Не придумав, что ему ответить на это, я молча подошел к машине."
    "Двери были разблокированы заранее. Он постарался... Как будто знал, что я соглашусь..."
    window hide

    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    play sound nds_list['nd_car_seat']
    scene bg bg_int_car_magn with flash

    window show
    "Через секунду я плюхнулся на переднее сиденье. То же самое движение повторил и \"водитель\"."
    "Он вытянул провода из под руля и замкнул их."
    "Ничего не произошло."
    fx_il "Теперь дай что-нибудь плоское."
    play sound sfx_keys_rattle
    "Я порылся в карманах и достал металлическую пластину, которую нашел сегодня утром перед дверью в свою квартиру."
    fx_il "Пойдет."
    window hide

    $ renpy.pause(1, hard=True)
    play sound sfx_break_grid

    window show
    "Он забрал её у меня из рук и буквально затолкал её в место, где должен быть ключ от машины."
    window hide

    play sound nds_list['nd_engine_start']
    play sound_loop nds_list['nd_engine_working'] fadein 4
    $ renpy.pause(3, hard=True)
    
    window show
    nd_il "Делов-то..."
    fx_il "Пф... Ты мог так же."
    nd_il "Просто в себя не верил..."
    "Видимо, я предсказал следующую реплику Ильи из параллельной вселенной, раз после сказанного мной он замолчал."
    "Чтобы поставить точку в диалоге, я нажал на кнопку включения радио."
    window hide

    play sound nds_list['nd_radio_on']
    $ renpy.pause(1, hard=True)
    play music ndm_list['kavinsky_night_call'] fadein 3

    window show
    "Из колонок, встроенных в двери машины, тут же заиграла музыка."
    fx_il "О! Не переключай! Это моя любимая."
    nd_il "Я и не собирался."
    fx_il "Времени у нас в обрез, а если быть точным, до полуночи. Не будем же медлить."
    nd_il "Согласен."
    window hide

    play sound nds_list['nd_open_car_window']

    window show
    "Я открыл окно у себя, предвкушая, как свежо будет, когда мы будем лететь по дорогам..."
    window hide

    stop ambience fadeout 4
    scene black with dissolve2
    $ renpy.pause(3, hard=True)
    $ volume(1, 'ambience')
    scene bg nd_road_1 with dissolve2

    $ renpy.pause(1, hard=True)

    window show
    "Картинка размывалась перед глазами от мыслей, что скоро всё это закончится."
    "Что скоро мне не придется мучаться, что я вернусь. Вернусь вместе с Ульяной."
    "Я верю Пророку. Пусть мы и в симуляции, я хочу провести жизнь в ней вместе с Ульяной."
    "Я так боюсь её потерять..."
    "Это любовь? Или я просто дурак, который слишком всё гиперболизирует и попросту рефлексирует?"
    "Ульяна бы ответила, наверное..."
    "\"Это любовь, зай\"..."
    "Но для Ульяны эта любовь - первая."
    "У неё недостаточно много опыта, чтобы разбираться в таком сложном понятии \"любовь\"."
    "Вернее, возможно у неё были незатейливые отношения и до встречи со мной, однако такие серьёзные - нет."
    "Иронично, что и я ранее не познавал такой уровень серьёзности отношений."
    "Получается, я тоже не имею права рассуждать на эту тему и делать какие-либо умозаключения?"
    "Тогда..."
    "Что же такое любовь?"
    window hide

    $ renpy.pause(1, hard=True)
    scene black with dissolve2
    $ renpy.pause(3, hard=True)

    play ambience nda_list['ambience_driving_inside_car'] fadein 5
    scene bg bg_int_car_city_night with dissolve2

    window show
    nd_il "Где ты научился водить?"
    fx_il "В автошколе, где же ещё."
    fx_il "В моей жизни как-то нашлось место для этого.{w=0.5} Хотя она и полна разочарований..."
    nd_il "Понимаю тебя...{w} Только моя жизнь состояла из совсем другого."
    fx_il "Программирование?"
    nd_il "Да... Так всё и было, пока это не изменил лагерь..."
    fx_il "То же самое."
    fx_il "Я был вожатым. И в моем отряде была одна девочка с длинными волосами... Прилежная такая."
    fx_il "Ну я и понял тогда, что влюбился. И ничего с собой поделать не мог."
    fx_il "Мне на тот момент было семнадцать, а ей пятнадцать."
    fx_il "Ну мы с ней разговорились, тогда вечером я не сдержался и поцеловал её..."
    fx_il "А она ответила взаимностью. Всё закончилось с концом смены. Я приехал в город. Мы поддерживали общение через интернет."
    fx_il "Она собиралась ехать в мой город. А потом пропала... Её не было неделю, пока я не смирился с тем, что больше никогда её не увижу и не услышу..."
    fx_il "Это были очень тяжёлые дни, от одних только воспоминаний того времени становится грустно."
    nd_il "Моя история не менее примечательна...{w} Но её развязка...{w} Слушай..."
    window hide

    $ renpy.pause(1, hard=True)
    stop music fadeout 4
    scene black with dissolve2
    $ renpy.pause(4, hard=True)
    play music ndm_list['jasper_byrne_miami'] fadein 4
    scene bg bg_int_car_road_night with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    fx_il "Значит я - это ты, но из другой вселенной..."
    nd_il "Моя Ульяна не умерла."
    fx_il "Моя Вика, наверное, умерла..."
    fx_il "Мне без неё плохо.{w=0.5} Как только я подумал, что могу быть счастливым, судьба меня послала на хуй."
    nd_il "Мы всё исправим, не делай поспешных выводов."
    nd_il "Я прекрасно понимаю твою боль, и говорю тебе, что ты не должен думать, что её уже нет."
    nd_il "Выход всегда есть, ты найдешь её. Она жива."
    nd_il "А если же перестанешь верить и ежеминутно добиваться своего - то никогда её не найдёшь."
    fx_il "Думаешь тому придурку можно доверять?"
    nd_il "Если я здесь, значит, наверное, можно..."
    "Машин кроме нашей не было, мы ехали с огромной скоростью по дороге, проезжая деревья и отдалённые домики."
    "В темноте казалось, что они то пропадали, то появлялись...{w} На спидометре красовалась цифра в 140 километров в час."
    "Я ощущал всем телом, как растягиваюсь под таким ускорением."
    "Это ощущение подходило лучше всего, чтобы думать о своей смерти."
    "Пророк никогда не ошибался. Надеюсь, и я не ошибусь в последний раз."
    "Я пожертвую собой, я отключусь, перейду в другой мир, вернусь в прошлое, что угодно."
    "Только Ульяна... Что будет с ней? Надеюсь я не убью своим поступком и её."
    "А может я и не умру, что мало вероятно. Но она должна жить."
    "Жить не с надеждой что я рано или поздно вернусь, но с надеждой на лучшее будущее."
    "А ещё лучше, чтобы она просто в миг забыла обо мне в этом сломанном мире."
    "Ведь если всё это - симуляция, то и Ульяна не может быть здесь настоящей."
    "Соответственно, если мне удастся найти свою девочку живой в нужном мире, то в этом..."
    "Я запутался."
    "Я запутался во всех этих мирах и симуляциях, мне кажется, я скоро сойду с ума."
    "Всё должно быть куда проще..."
    window hide 

    $ renpy.pause(1, hard=True)    

    window show
    fx_il "{font=mods/notdream/fonts/notes.ttf};{/font} Longing for the sun you will come {font=mods/notdream/fonts/notes.ttf};{/font}"
    fx_il "{font=mods/notdream/fonts/notes.ttf};{/font} To the island without name {font=mods/notdream/fonts/notes.ttf};{/font}"
    fx_il "{font=mods/notdream/fonts/notes.ttf};{/font} Longing for the sun be welcome {font=mods/notdream/fonts/notes.ttf};{/font}"
    fx_il "{font=mods/notdream/fonts/notes.ttf};{/font} On the island many miles away from home... {font=mods/notdream/fonts/notes.ttf};{/font}"
    nd_il "Что ты напеваешь?"
    fx_il "Да так... Песня одна. В голове засела..."
    nd_il "Почему она у меня вызывает тревожные мысли?"
    fx_il "Без понятия..."
    "Я замолчал, окунувшись в себя."
    "Возможно, этот Илья меня с ума сведёт...{w} Хотя..."
    window hide
    
    $ renpy.pause(1, hard=True)

    window show
    "Я совсем не заметил, как молчание в машине сопровождалось каким-то ретровейвом на заднем фоне моих мыслей."
    nd_il "А я останусь с Ульяной там?"
    "На этот вопрос Илья за рулём лишь глубоко вздохнул."
    "Было бы странно, если бы он знал ответ на этот вопрос."
    "Удивительно, как меня может волновать моя любовь, когда на кону стоит моя жизнь?"
    "Ей без меня было бы очень плохо...{w} Я делаю это во благо нас с ней.{w} Но что если нет?"
    "Тогда я просто конченый предатель..."
    "Тогда я без чьей-либо помощи отойду в мир иной, даже если в предстоящей передряге выживу."
    "Мне не нужен мир, в котором нет Ульяны."
    "Не нужен в нём и я сам себе."
    window hide
    
    $ renpy.pause(1, hard=True)
    scene black with dissolve2
    $ renpy.pause(3, hard=True)
    scene bg ext_ae86_povorot with dissolve2
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg ext_akina_povorot3 with dissolve2
    $ renpy.pause(2, hard=True)
    scene black with dissolve
    $ renpy.pause(2, hard=True)
    scene bg ext_akina_ae86_end:
        xalign 0.5 yalign 0.5 zoom 1.5
        ease 5.0 xalign 0.5 yalign 0.5 zoom 1.0
    with dissolve2
    $ renpy.pause(4, hard=True)
    stop music fadeout 4
    stop ambience fadeout 4
    stop back_ambience fadeout 4
    stop sound_loop fadeout 4
    scene black with dissolve3

    $ renpy.pause(6, hard=True)

    play ambience nda_list['nd_ambience_town_road'] fadein 3
    play sound nds_list['ext_car_engine_off'] fadein 2
    $ renpy.pause(2, hard=True)
    scene bg nd_doroga_sel with dissolve2
    $ renpy.pause(1, hard=True)
    play sound nds_list['nd_cardoor_openclose']

    $ renpy.pause(1, hard=True)

    window show
    "Мой водитель привез меня туда, где заканчивается асфальтированная дорога и начинается моё последнее приключение."
    show pi2 normal shirt at center with dspr
    fx_il "Дальше придётся тебе идти самому."
    "Сказал он и посмотрел на меня сочувствующим взглядом.{w} Вздохнул."
    fx_il "А мне нужно завершить своё последнее дело."
    fx_il "Сегодня день рождения моей сестры, я не могу облажаться."
    nd_il "Она умрёт под колесами фуры..."
    show pi2 serious shirt at center with dspr
    fx_il "Не в мою, сука, смену."
    window hide

    hide pi2 with dspr
    $ renpy.pause(1, hard=True)
    play sound nds_list['nd_cardoor_openclose']
    $ renpy.pause(1, hard=True)

    window show
    "Он залез обратно в машину и достал из бардачка нож."
    show pi2 normal shirt at center with dspr
    play sound nds_list['butterfly_knife_flip']
    "Вышел из машины и протянул его мне вместе с листком, где были записаны координаты."
    play sound nds_list['butterfly_knife_grab']
    "Я молча принял подарок, ввёл корды в приложение карт и поблагодарил его."
    fx_il "Сегодня мы сделаем это."
    fx_il "Я не могу тебе врать в лицо."
    fx_il "Не могу молчать. Я знаю что происходит."
    fx_il "Время в разных уголках этой дыры идёт по-разному."
    fx_il "Я не уйду отсюда, но ты..."
    show pi2 normal shirt at center with dspr
    fx_il "Я знаю что тебя ждет, и я не хочу назад."
    nd_il "Что меня ждёт?"
    fx_il "Беззаботное прошлое без будущего.{w=0.4} Ты, наверное, будешь счастлив."
    fx_il "Но у меня другие цели."
    fx_il "У тебя мало времени."
    fx_il "Насчет твоей сестры...{w=0.4} Я не знаю, что мне делать с этой информацией.{w} Мне нужно спасти свою."
    fx_il "Ты не знаешь, какого это,{w=0.1} жить с незнакомым тебе человеком и думать, что это что-то родное для тебя."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    nd_il "Всё равно спасибо тебе за всё."
    fx_il "Поблагодаришь, когда всё завершится."
    play sound sfx_inhale
    hide pi2 with dspr
    "После сказанного им я сделал глубокий вдох,{w} а затем,{w} медленно выдохнув,{w} успокоился,{w} привёл мысли у себя в голове в порядок."
    play sound nds_list['nd_handsup']
    "Рукопожатие стало чем-то завершающим в нашем разговоре."
    "{i}Мы оба заключили сделку с судьбой{/i}."
    window hide

    $ renpy.pause(1, hard=True)
    show pi2 smile shirt at center with dspr
    $ renpy.pause(1, hard=True)
    
    window show
    nd_il "Было приятно познакомиться, Илья."
    fx_il "Взаимно."
    window hide

    hide pi2 with dspr
    $ renpy.pause(2, hard=True)
    play sound nds_list['nd_cardoor_openclose']
    $ renpy.pause(3, hard=True)
    play sound nds_list['nd_car_away']
    $ renpy.pause(1, hard=True)

    window show
    "Он вдавил газ в пол и позже скрылся за поворотом."
    th "Ну... Сейчас или никогда."
    play sound nds_list['butterfly_knife_lock']
    "Я спрятал нож в карман, разблокировал телефон и осмотрел место, к которому мне нужно держать путь."
    "Необходимо было сделать всё до полуночи,{w} времени оставалось двадцать минут..."
    window hide

    $ renpy.pause(2, hard=True)
    play sound_loop sfx_far_steps fadein 1

    window show
    "Двадцать секунд и я уже направлялся к месту, указанному на карте."
    "В голове блуждало множество догадок насчет Ильи."
    "Альтернативный я приходит к моей квартире вечером и просит помочь, потому что так сказал ему Пророк."
    "Это не может быть совпадением."
    "Всё как будто уже продумано кем-то или чем-то, не обязательно Пророком."
    "До сих пор не верится, что это так…{w} Его слова про \"родного\" незнакомого человека, что они могут значить?"
    "Он что-то знает, определенно, если не про вселенную, но про миры точно…"
    "Почему я не догадался спросить его об этом?"
    window hide

    $ renpy.pause(2, hard=True)
    play sound nds_list['nd_vibro_sms']

    window show
    "Сообщение, пришедшее на мой телефон, разбудило меня от мыслей."
    "\"Ульяна рядом, торопись.{w} Преграды больше нет, закончи это дело до конца.\""
    "Я уже не забивал этим голову. Просто принял как факт. Факт, что дело – это спасение Ульяны и…"
    "Переход из одного мира в другой, возвращение в прошлое, возвращение моей памяти, моей сестры..."
    "Шанс всё исправить с вероятностью, как выйграть в казино, только вместо фишек моей ставкой будет моя жизнь."
    "И ставка уже принята..."
    window hide

    stop ambience fadeout 3
    scene black with dissolve2
    $ renpy.pause(5, hard=True)
    play ambience ambience_camp_entrance_night fadein 4
    scene bg ext_road_night2 with dissolve2
    $ renpy.pause(1, hard=True)

    window show
    "Спустя несколько минут, дойдя наконец до ровной трассы, я понял, что мне без машины никуда."
    th "Придётся вспоминать навыки угона автотранспорта, которые я лицезрел буквально полчаса назад?"
    th "Только в данном случае, этот автотранспорт ещё нужно найти."
    "На обочинах дороги, вдалеке у горизонта - не было ни одной машины, на которой я смог бы добраться до места назначения."
    "Оставался лишь вариант бежать дальше по дороге, но вряд ли я в таком случае успею. Тем более времени у меня оставалось совсем немного."
    "Ничтожные пятнадцать минут на ещё один километр."
    "Кажется, мне придётся вспомнить уроки физкультуры и напрячь все свои мышцы, чтобы заслужить счастье."
    window hide

    stop sound_loop fadeout 2
    stop ambience fadeout 3
    $ renpy.pause(2, hard=True)
    show blink

    $ renpy.pause(3, hard=True)

    window show
    "Я закрыл глаза и присел на колени, ощутив хрустящий под ними белый снег, умыл своё лицо…"
    "Стоп. Снег?! Откуда?!"
    window hide

    $ renpy.pause(1, hard=True)
    play ambience nda_list['1nd_snow_forest'] fadein 4
    hide blink
    scene bg nd_ext_path_snow_night
    show unblink

    window show
    "Я открыл глаза. Дорога, по которой я собирался идти, тут же оказалась усыпана белым пухом в виде холодного снега."
    "И моя новая курточка здесь не могла меня спасти."
    "По ощущениям, температура не изменилась, но казалось, что должна была это сделать уже в скором времени."
    show blink
    "Я ещё раз протёр глаза, вспомнив, что у меня остаётся пятнадцать минут."
    "Одно дело - успеть пробежать километр по ровному, летнему асфальту, совсем другое - пробиваться через толщу снега."
    "В летней обуви!"
    "Уже через секунду я начал ощущать сырость в ботинках."
    "То был снег, который успел просочиться через вентиляционные отверстия и таял,{w} неумолимо таял,{w} создавая лишний дискомфорт."
    hide blink
    show unblink
    "Так, мысли в порядок."
    "Цель - жизнь. {w} Ульяна."
    "К чёрту все неудобства! Правда или ложь, я спасу нас, Уля!"
    window hide

    play sound_loop nds_list['frost_footsteps'] fadein 3

    window show
    "И я рванул..."
    "Получив порцию адреналина в кровь, ноги двинулись одна за другой, расталкивая снег..."
    "Да, это нелегко."
    "Но куда сложнее - остаться валяться здесь, между мирами, убивая своё прошлое и будущее."
    "А после - настоящее."
    window hide

    $ renpy.pause(2, hard=True)
    stop sound_loop fadeout 1
    $ renpy.pause(1, hard=True)

    window show
    "Осознав, что просто перебирать ноги слишком медленно, я начал предпринимать попытки перейти на бег."
    play sound_loop nds_list['frost_footsteps_run'] fadein 1
    "Я бежал по снегу, стараясь смотреть вдаль и пытался что-то увидеть в кромешной тьме – безрезультатно."
    "Дорога тянулась и тянулась на многие метры, если не километры."
    th "Я смогу...{w} Я сделаю это...{w} Я не подведу сегодня никого..."
    "Я старался подбадривать себя, чтобы бежать активнее, но через поднимающуюся метель это сделать было очень сложно."
    "Зато я согревался, но какой ценой..."
    "Тратил свои драгоценные силы, которые к концу дня итак уже были на исходе."
    "Зачем я только ввязался во все это?.."
    th "Нет, прочь такие мысли!"
    window hide

    $ renpy.pause(5, hard=True)
    stop sound_loop fadeout 2
    $ renpy.pause(2, hard=True)
    play sound sfx_bush_body_fall
    with vpunch
    $ renpy.pause(1, hard=True)
    show blink
    $ renpy.pause(3, hard=True)
    
    window show
    "Ощущая сильную усталость, я уронил своё тело на снег в попытках отдохнуть. Осталось девять минут, мне нельзя опоздать..."
    "Я сжал телефон в руках и ощутил ужасное сопротивление."
    th "Что?.."
    window hide

    $ renpy.pause(2, hard=True)
    play sound sfx_pat_shoulder_hard
    show nd_fix_snowfall with flash

    window show
    "Кто-то выхватил у меня телефон из руки и тут же жёстко прижал голову в снег, заломав руки."
    window hide

    window show
    nd_pe1 "Шныряй его…"
    nd_pe2 "А мобила?" 
    nd_pe1 "Мобилу забирай…"
    window hide

    $ renpy.pause(2, hard=True)
    play sound nds_list['nd_phone_ringtone']

    window show
    "В ушах громом раздался рингтон моего телефона."
    "Сердце в груди в тот же момент сварилось и ужалось до размеров атома, и одновременно увеличилось до размеров вселенной."
    "Скорее всего, это была Ульяна."
    nd_pe2 "…Чё скажем ей?"
    nd_pe1 "Ничего, вытаскивай симку и ложи телефон в карман."
    th "Чёрт, кажется это точно была Ульяна!.."
    #th "Правильно не \"ложи\", а \"клади\". Идиоты..."
    nd_il "Не трогайте!"
    play sound nds_list['butterfly_knife_flip']
    "Закричал я, но почувствовал какой-то холодный предмет, упирающийся мне в затылок."
    nd_pe1 "Заткнись, блядь!"
    "Грубый мужской голос заткнул меня.{w} Я терпеливо расслабил голову."
    nd_pe2 "Слыш, а не он ли это... На нас вчера нарвался?"
    nd_pe1 "Да хер его знает."
    nd_pe1 "Телом похож, хлебальником не очень."
    window hide

    $ renpy.pause(2, hard=True)
    play music ndm_list['20tokens_pink_dreams'] fadein 3

    window show
    nd_il "Отпустите, суки!"
    play sound sfx_pat_shoulder_hard
    with hpunch
    "Закричал я и попытался встать… и получил ногой по затылку."
    th "Твари..."
    window hide

    $ renpy.pause(1, hard=True)
    play sound sfx_pat_shoulder_hard
    with hpunch
    $ renpy.pause(1, hard=True)
    play sound sfx_pat_shoulder_hard
    with flash
    $ renpy.pause(1, hard=True)

    window show
    th "Вся жизнь пронеслась перед глазами..."
    "Через мгновение на моё тело снова обрушилась пара ударов, снег под моей тяжелой головой окрапился."
    th "Шесть минут…{w} Я не успею…"
    "В моей голове смешалась вся гамма эмоций."
    "Рядом с моей кровью, на снег начали капать слёзы."
    "Это очень больно, это очень сложно - пробиваться через толщу снега, так ещё и параллельно рассуждая, как избавиться от гопоты."
    "Следующая волна отчаяния уже захлестнула меня."
    "Казалось, я уже умер..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "В один момент кулаки сжались.{w} Я бы подумал, что они это заметили, если бы он не полез ко мне в карман."
    "Я почувствовал, как его нож царапает его внутренности."
    "А может, это и не нож вовсе.{w} А может это мой нож?"
    "Я глубоко вздохнул, задержал дыхание, и как только почувствовал руку одного из них рядом со своей рукой чтобы обыскать наружный карман, я резко схватился за неё."
    window hide

    $ renpy.pause(1, hard=True)
    scene bg nd_ext_path_snow_night
    show pi normal
    with flash
    $ renpy.pause(1, hard=True)

    window show
    "По ладони прошлось его лезвие, но не оставило пореза."
    "Резкий переход в положение стоя, и охотничий нож этого бандита оказался на снегу."
    "Левой я вытер кровь из-под носа, правой вцепился в свой нож-бабочку в кармане."
    "Холодный пот изливался по моему телу, руки дрожали как при первом поцелуе, но я стоял."
    show pi smile with dspr
    nd_pe1 "Ах ты тварь!"
    hide pi with dspr
    "Только он накинулся на меня, нож врезался в его глотку, заставив меня в тот же миг убрать от него свои руки."
    "Когда на кону две жизни и вечное счастье - приходится приносить в жертву другую жизнь."
    "Он сам это заслужил."
    show prologue_dream with flash
    "Его лицо отпечаталось в моем сознании. Он выглядел точно так же, как тот пионер в лагере..."
    nd_il "Ублюдок!{w} Так и должно было закончится наше рандеву в лагере!{w} А, сука?!"
    nd_il "Харкай кровью..."
    window hide

    $ renpy.pause(1, hard=True)
    show bg nd_c2_pendsm behind prologue_dream with flash
    $ renpy.pause(3, hard=True)

    play sound_loop nds_list['frost_footsteps_run'] fadein 1
    play back_ambience sfx_head_heartbeat fadein 4

    scene bg nd_ext_path_snow_night_2:
        zoom 1.05
        anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    with flash

    $ renpy.pause(1, hard=True)

    window show
    "Это последнее, что я видел, перед тем как забыть про телефон, про карту и координаты, и по памяти бежать к месту назначения."
    "Я боялся, что не успею, боялся опоздать, и мой страх был более чем оправдан."
    "Я не хотел терять шанс. Терять Ульяну. Тем более, мне казалось, что за мной бежали."
    "Какое-то существо, в моем сознании напоминавшее человека-кошку, бежало за мной по пятам, будто гнав меня к тому самому месту."
    "Обернусь - и кто знает, может быть уже через секунду я буду валяться в грязном снегу и не смогу открестить от себя страх."
    "А драгоценные минуты, или даже секунды безвозвратно уйдут, а допускать мне этого нельзя."
    "Скорее всего я просто сошёл с ума. Это многое бы объяснило."
    "Я ощущаю постоянную панику, резкие перепады настроения."
    "Да что там говорить, я даже думаю как будто об одних и тех же вещах по разному, хотя не должен."
    "Я клялся Ульяне из этого мира, что не оставлю её, но что тогда я делаю сейчас?"
    "Почему я здесь, в непонятном даже мне самому месте, а не лежу с ней в обнимку в тёплой кроватке?"
    "Я спасаю нас обоих или я иду по пути жестокого предательства?"
    "Я первый раз в своей жизни убил человека, пусть и плохого, но всё равно человека. Кровь на снеге растворится, а на моих руках останется навечно…"    
    window hide
    $ renpy.pause(1, hard=True)

    window show
    "Если в конце пути окажется, что зря я столько наломал дров..."
    "Я не смогу себя простить."
    window hide

    $ renpy.pause(2, hard=True)
    scene black with dissolve2

    window show
    "В сознании шаги позади меня превратились в топот лошадей, в голове пульсировала кровь.{w} Оставалось три минуты."
    "Вдалеке показались очертания сооружения, и с каждым моим шагом они приобретали всё больше деталей."
    "Чем ближе я был к этому месту, тем сильнее во мне просыпалось необоснованное чувство ностальгии."
    "Мне показалось, что на этом месте произошло что-то…{w} Что-то значимое для меня."
    "Оно казалось для меня убежищем от тех монстров, что периодически посещали моё сознание, или тех, которые гнались за мной прямо сейчас."
    "Когда мои руки коснулись низкого ограждения, я ощутил наконец жуткую метель, что снегом обжигала кожу моего лица."
    "Качающиеся деревья стали наблюдателями."
    "Я нащупал ручку низкой металлической двери и, дернув её на себя, прорвался внутрь.{w} Туда, где меня бы никто не достал..."
    window hide

    stop music fadeout 4
    stop back_ambience fadeout 4
    stop sound_loop fadeout 4
    stop ambience fadeout 4
    $ renpy.pause(6, hard=True)

    window show
    "За стенами этого воображаемого купола едва были слышны звуки метели."
    "Я пытался отдышаться, слушая биение собственного сердца, убеждаясь в том, что до сих пор живой, и преследователи никак меня не задели."
    "Только спустя пару мгновений я догадался разомкнуть веки чтобы понять, где я нахожусь..."
    window hide

    $ renpy.pause(1, hard=True)
    play ambience nda_list['cemetry_close_night'] fadein 4
    scene bg nd_graves_bg_night
    show unblink
    $ renpy.pause(4, hard=True)

    play sound nds_list['nd_sfx_ograde_door']

    window show
    th "Вот моё место..."
    "Отскочило в висок от моего сознания."
    "То, с чего всё началось... Кладбище."
    "Удручающее и тихое место, от которого у человека порой бесконтрольно идут мурашки по коже. "
    "Прям как у меня сейчас..."
    "Я не понимал, почему оказался сейчас именно здесь."
    "Это место не было крепким бункером, броня которого выдержит снаряд из пушки."
    "Не было оно и партизанским лагерем, который даже если захочешь - не увидишь."
    "Но при всём при этом... Я не чувствовал в этом месте непреодолимого страха, мне казалось, что я в безопасности."
    th "Кажется, меня здесь кто-то ждёт..."
    th "Кто-то, кто уже отошёл в мир иной, или же наоборт, находится на грани жизни и смерти."
    "Все мои воспоминания должны вернуться, пройди я до могилы... Но какой..."
    "Чьё захоронение я должен найти?"
    window hide

    $ renpy.pause(3, hard=True)

    play sound_loop nds_list['frost_footsteps'] fadein 2

    window show
    "Я начал прогулку по этому зловещему месту."
    "Тут не было ни души. В буквальном смысле. Только вороны каркали вдалеке, нагнетая и без того мрачную атмосферу."
    th "Что я должен тут найти?"
    th "Зачем координаты вообще вели меня сюда? Может..."
    th "Может я должен умереть?{w} Но как же Ульяна?{w} Я не оставлю её одну..."
    th "Должен быть какой-то другой выход..."
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я чувствовал, что должен идти дальше."
    "Первая могила, третья, десятая - всё не то!"
    "Мне нужно найти именно {i} ту самую {/i} могилу."
    "В голове из ниоткуда начали всплывать воспоминания."
    th "Я уже бывал здесь однажды..." 
    "А ноги всё продолжали вести меня прямо. Через голые ветки деревьев, через многочисленные могилы, эпитафии на которых я не мог разглядеть."
    "Они были слишком старыми.{w} Слишком потёртыми.{w} Слишком мёртвыми."
    "Я готов был выстрелить себе в висок чтобы доказать, что это сон. Но понимал, что в таком случае мой сон станет вечным."
    "Нет. Я уже мёртв... То о чем говорил Пророк...{w} Всё это правда..."
    "Вот почему тот Илья не хотел назад..."
    window hide

    $ renpy.pause(10, hard=True)
    stop sound_loop fadeout 2

    window show
    "Наконец я увидел могилу, которую должен был найти."
    "Каждый раз, когда я видел это надгробие, или даже просто вспоминал его - сердце сжималось до размера детского кулачка."
    "Здесь я проливал больше всего слёз, отсюда я часами не хотел уходить."
    "Здесь похоронена она..."
    "{i}\"Здесь похоронена Дарья ██████\"{/i}"
    window hide

    $ renpy.pause(1, hard=True)
    play music ndm_list['bass_i_love_you_too'] fadein 4

    window show
    nd_il "Я снова рядом с тобой, сестрёнка."
    "Я склонился над могилой.{w} Цветочки,{w} врытые в землю,{w} давно уже завяли."
    nd_il "Привет...{w} Моя милая..."
    nd_il "Дашуль..."
    nd_il "Ты спишь?"
    nd_il "Я... Я не успел тебе многое сказать при жизни."
    nd_il "Если бы ты была рядом..."
    nd_il "Господи, почему нельзя вернуть жизнь одного единственного человека?"
    nd_il "Если ты существуешь, Всевышний, почему заставляешь из раза в раз страдать меня?"
    nd_il "Не ты ли должен оберегать людей от жестоких мук и страданий, а?"
    nd_il "Ответь мне!"
    window hide

    $ renpy.pause(2, hard=True)    

    window show
    "Тишина была моим ответом."
    "Как и всегда, мёртвая и зловещая тишина."
    th "Если богу похуй, то так для чего пытали?.."
    window hide

    $ renpy.pause(2, hard=True)
    play sound sfx_inhale
    $ renpy.pause(2, hard=True)

    window show
    "Мои глаза потяжелели..."
    nd_il "Я...{w} Я не могу без тебя.{w} Я скучаю..."
    nd_il "Без твоей поддержки мне очень тяжело, порой я могу ходить из угла в угол, так и не найдя себе покоя."
    nd_il "Ты направляла мою жизнь по правильному течению, ты всегда была опорой и поддержкой."
    nd_il "Как же я по тебе скучаю, Даша..."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    nd_il "Прости меня пожалуйста."
    nd_il "Это я виноват в том, что случилось..."
    nd_il "Если бы я тогда был внимательнее, если бы больше ценил каждую минуту нашего семейного очага, ты была бы рядом."
    nd_il "Я бы смог спасти тебя от злой судьбы, и жили бы мы вместе долго и счастливо, как в сказке."
    th "Так почему же... Судьба лишила нас этой сказки?"
    th "Поменяла концовку с \"долго и счастливо\" на \"мучительно и страшно\"?"
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Мою грудь будто разрубили катаной, а в глазные яблоки воткнули иглу."
    nd_il "Я не могу без тебя."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    "Из губы кровь капнула на засыпанную снегом землю.{w} Её разбили, либо я настолько сильно её раскусил от волнения и печали."
    nd_il "Я...{w} Я не могу так жить!"
    "Каждый раз в этом месте я задумываюсь об прерывании своей жизни, чтобы лечь рядом с тобой."
    "Когда-нибудь я в итоге сорвусь и мы будем вместе..."
    window hide

    $ renpy.pause(2, hard=True)
    play sound nds_list['butterfly_knife_flip']
    $ renpy.pause(1, hard=True)

    window show
    "Я достал из кармана нож бабочку и раскрыл его."
    "Отодвинув рукав костюма, я через призму времени увидел раны от порезов вдоль своих вен."
    "Я сделаю это прямо сейчас.{w} Попытаюсь сделать это до конца.{w} У меня не было ничего дороже тебя..."
    "Не было, но я это потерял..."
    nd_il "Я хочу...{w} Вернуться...{w} Возьми меня обратно..."
    window hide

    stop music fadeout 3
    $ renpy.pause(3, hard=True)
    play sound sfx_pat_shoulder_hard
    with vpunch

    window show
    "Только лезвие коснулось моего запястья, сделав небольшой порез, в мою спину что-то врезалось."
    "Что-то теплое,{w} мягкое,{w} что-то обхватило меня."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    us "Илья, ты..."
    us "Ты нормальный!?"
    "В моём горле застрял воздух, вдоль щёк полились слёзы."
    nd_il "Моя милая..."
    window hide

    $ renpy.pause(2, hard=True)

    stop ambience fadeout 4
    play music ndm_list['Save_Our_Souls_SOS'] fadein 3

    $ renpy.pause(2, hard=True)
    show us cry nd_dress close at center with dspr

    window show
    us "Неужели ты забыл, что своими действиями загоняешь в гроб ещё одного человека?"
    us "Я тебя люблю больше всего на свете."
    us "Не оставляй меня тут одну!"
    show us shy2 nd_dress close at center with dspr
    us "Мои слова не были пустыми, когда я говорила о том, что не выживу в этом мире в одиночку."
    show us cry nd_dress close at center with dspr
    us "Сейчас ты порежешь свои вены, истечёшь здесь кровью, тебя никто не сможет спасти."
    us "До этих мест не доедет скорая помощь, никакие бинты не спасут тебя от потери крови."
    us "Ты умрёшь в холодном снегу, ещё более мучительной смертью, потому что будешь чувстовать каждую капельку крови, что будет покидать твоё тело."
    us "Вместе с этим, последнее, что ты будешь видеть - это не надгробие Даши, а меня, залитую океаном слёз и попытками привести тебя в чувства."
    us "Но у меня не хватит ни сил ни средств этого сделать - я просто буду кричать и наблюдать за твоей смертью."
    us "Ты пережил смерть любимой сестры и прекрасно понимаешь, насколько это больно - потерять близкого человека."
    us "Так почему же сейчас ты не подумал про меня?"
    us "Порезав свои вены, ты умрёшь прямо у меня на руках..."
    show us cry2 nd_dress close at center with dspr
    us "ТЫ ХОТЬ ПОНИМАЕШЬ, ЧТО Я БУДУ ЧУВСТВОВАТЬ В ЭТОТ МОМЕНТ?"
    show us cry nd_dress close at center with dspr
    us "Понимаешь, я это знаю."
    show us shy2 nd_dress close at center with dspr
    us "Я же с ума сойду от этого, Илья!"
    show us cry nd_dress close at center with dspr
    us "И через мгновение отправлюсь вслед за тобой, используя то же орудие самоубийства."
    us "Этого ты хочешь?"
    window hide

    $ renpy.pause(1, hard=True)

    window show
    "Я смотрел на Ульяну, которая уже успела покрыться слоем горьких слёз."
    "Я не видел её лицо полностью - слёзы мне не давали этого сделать."
    hide us with dspr
    "Они скатывались из моих глаз нескончаемым потоком, а я ничего не мог с этим поделать."
    "Психика Ульяны испытывала сейчас сумашедшее потрясение..."
    "А мой мозг постепенно отрезвлялся после её слов и начал понимать, на краю какой пропасти я стоял минуту назад."
    window hide

    $ renpy.pause(2, hard=True)
    play sound nds_list['butterfly_knife_flip']
    
    window show
    "Лезвие ножа раскрутилось и упало на снег."
    window hide

    $ renpy.pause(2, hard=True)

    window show
    th "Она здесь..."
    nd_il "Уля..."
    nd_il "Милая моя..."
    show us cry nd_dress close at center with dspr
    us "Зай, не уходи пожалуйста..."
    us "Мне страшно."
    "Это была девочка моего сердца."
    us "Я просто хочу чтобы ты был рядом!"
    nd_il "Мышонок..."
    nd_il "Только что...{w} Ты спасла мою жизнь."
    "Ясное сознание продолжало заполнять мой мозг."
    hide us with dspr
    "Я обхватил её мягкое тело руками."
    nd_il "Я тебя никогда не отпущу..."
    nd_il "Ты - всё, что у меня есть..."
    nd_il "Я устал находится в этом мире..."
    nd_il "Я повёл себя совершенно неправильно, но на то была причина{w} - я сломан."
    nd_il "Слишком тяжело это - нести нелёгкий груз горькой утраты."
    nd_il "Ты стала моим спасителем."
    nd_il "Светом в конце туннеля, огоньком в кромешной тьме - называй как хочешь."
    window hide

    $ renpy.pause(2, hard=True)
    show blink
    $ renpy.pause(1, hard=True)

    window show
    "Я закрыл глаза. Нос был заложен. Я не чувствовал больше запаха волос девочки."
    "Я плакал... Слезы лились из моих глаз одна за одной."
    "Одного дорогого мне человека уже нет в живых."
    "Но она... Она всегда рядом,{w} когда мне плохо,{w} чтобы сделать меня хоть немножко счастливым."
    "Я её очень люблю за это..."
    nd_il "Мне страшно, зай."
    nd_il "Не отпускай меня..."
    us "Никогда не отпущу.{w} Ты только мой..."
    window hide
    
    $ renpy.pause(3, hard=True)
    show us shy2 nd_dress close at center with dspr
    $ renpy.pause(1, hard=True)
    
    window show
    us "Я должна тебе признаться."
    us "Мы всегда были так далеко."
    us "Но давай сегодня сократим расстояние?"
    nd_il "Ч-ч-что?"
    us "Я устала тебя ждать..."
    nd_il "Я тебя люблю..."
    show us shy nd_dress close at center with dspr
    us "А я тебя люблю больше!"
    "На наших лицах впервые за долгое время появилась улыбка."
    "Пока ещё очень неказистая и неопределённая, но всяко лучше, чем гримаса печали."
    nd_il "Ты готова, милая?"
    us "Я готова.{w=0.3} Всё будет хорошо."
    window hide

    show prologue_dream 
    hide us with dspr
    with dissolve
    
    window show
    nd_il "Я на вокзале.{w} Буду,{w} как только узнаю,{w} где ты все таки живёшь..."
    us "Ты всё ещё на меня злишься?"
    nd_il "Ты вытащила меня с того света, как можно на тебя злиться?"
    us "Жду тебя...{w} И...{w} Скучаю..."
    "Мы заключили крепчайшие объятия, но при этом будто перестали чувствовать тела друг друга."
    "Это было похоже на невесомость..."
    window hide
    
    $ renpy.pause(3, hard=True)
    play ambience nda_list['ambience_nothing'] fadein 4
    $ renpy.pause(2, hard=True)
    
    window show
    "Я наклонился назад в её объятиях и начал падать..."
    "Пустота укутала меня."
    "Я не смог пошевелится, когда так хотел это сделать."
    "Сначала было страшно, но потом я прижал Ульяну к себе сильнее.{w} Это настолько просто было сделать, будто мы не летели на всей скорости вниз, а лежали на кровати."
    "Я не слышал ничего, даже собственного дыхания.{w} Все звуки поглотились этим местом."
    "Но меня уже ничего не волновало."
    "Если мы упадем и разобьемся через несколько секунд, я хочу прожить эти секунды как всю свою жизнь."
    "Моя жизнь сейчас в моих руках, в буквальном смысле."
    "Я поцеловал Ульяну. Так сильно, что мы, казалось, перевернулись в воздухе."
    "Она завела свою руку за мою голову и сжала мои волосы."
    "Её губки показались мне настолько сахарными, что я бы вмиг вернулся в детство, в воспоминания, когда съел весь кулек конфет, ни с кем не поделившись."
    "Но вот я чувствую, как с нами сталкиваются фотоны света. Я отпускаю наш поцелуй, но не объятия."
    "Я боюсь её отпустить, вдруг она улетит и мы никогда не встретимся..."
    "Рассвет близко. Мы падаем на солнце, застрявшее в черной дыре. Я чувствую, как умираю, вновь..."
    window hide

    stop music fadeout 5
    stop ambience fadeout 5
    scene black with dissolve2
    $ renpy.pause(6, hard=True)

    jump nd_c2_epilogue
