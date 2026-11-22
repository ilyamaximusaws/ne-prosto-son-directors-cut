init python:

    def nd_test_font(fimod):
        if fimod == "nd":
            nd_screens_save_act()
            renpy.say(nd_il, "Однажды съев {b}фейхоа{/b}, я, {i}как зацикленный{/i}, ностальгирую всё {color=#0095b9}чаще{/color} и больше по этому чуду.")
            renpy.say(us, "Твёрдый, как ъ, но и мягкий, словно ь, юноша из Бухары ищет фемину-москвичку для просмотра цветного экрана жизни.")
        else:
            renpy.notify("this modificator is not indented")
     