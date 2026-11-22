init python:
    class nd_FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)
                
    def nd_on_load_callback(slot):
        try:
            if persistent.nd_on_save_timeofday[slot]:
                persistent.timeofday = persistent.nd_on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.nd_on_save_timeofday[slot][1]
                persistent.font_size = persistent.nd_on_save_timeofday[slot][2]
                    
                _preferences.volumes['music'] = persistent.nd_on_save_timeofday[slot][4]
                _preferences.volumes['sfx'] = persistent.nd_on_save_timeofday[slot][5]
                _preferences.volumes['voice'] = persistent.nd_on_save_timeofday[slot][6]
        
        except:
            pass
        
    def nd_on_save_callback(slot):
        if not persistent.nd_on_save_timeofday:
            persistent.nd_on_save_timeofday={}
        persistent.nd_on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, persistent.hentai, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])

    def nd_screen_act():
        config.window_title = u"Это не просто сон, верно?"
        config.name = "notdream"
        config.version = "1.0.0"
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("nd_say", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("nd_game_menu_selector", None)]
        persistent._file_page = "nd_FilePage_1"

    def nd_save_screen_old():

        renpy.display.screen.screens[("nd_say_old", None)] = renpy.display.screen.screens[("say", None)]
        renpy.display.screen.screens[("nd_game_menu_selector_old", None)] =  renpy.display.screen.screens[("game_menu_selector", None)]

    def nd_screens_diact():
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting_Summer"
        config.version = "1.2"
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("nd_say_old", None)]
        renpy.display.screen.screens[("game_menu_selector", None)] = renpy.display.screen.screens[("nd_game_menu_selector_old", None)]

            
    def nd_screens_save_act():
        nd_save_screen_old()
        nd_screen_act()



init 10 python:

    def nd_after_save_screens_act_un():
        global save_name
        #if save_name.find(u'Это не просто сон, верно?') != -1:
        #    renpy.display.screen.screens[("say", None)] =                     renpy.display.screen.screens[("nd_say", None)]

    config.after_load_callbacks.append(nd_after_save_screens_act_un)