init python:
    ## Тонировка изображений

    # в соответствии со временем суток

    nd_tint = {
        "sunset":im.matrix.tint(0.94, 0.82, 1.0),
        "night":im.matrix.tint(0.63, 0.78, 0.82)
    }

    # и в конкретный цвет (для простоты — через функцию)

    def nd_make_tint_img(imgf, color):
        tc = {
            "red":(1.0, 0.35, 0.35),
            "green_yellow":(0.91, 1.0, 0.59),
            "yellow":(0.91, 1.0, 0.09),
            "cyan":(0.0, 1.0, 0.8),
            "purple":(0.87, 0.28, 0.74),
            "orange":(0.94, 0.52, 0.32),
        }
        r, g, b = tc[color]
        return im.MatrixColor(imgf, im.matrix.tint(r, g, b))

init 2:

    python:



        ##    Спрайты    ##

        # Эмоции спрайтов старых персонажей и их отношение к позе

        nd_emotion_to_pose = {
            'us': { 'grin': 1, 'laugh': 1, 'laugh2': 1, 'evsmile': 1, 'normal': 1, 'normal_dontlike': 1, 'sad': 1, 'smile': 1, 'yawn': 1, 'angry': 2, 'calml': 2, 'dontlike': 2, 'fear': 2, 'upset': 2, 'cry': 3, 'cry2': 3, 'shy': 3, 'shy2': 3, 'surp1': 3, 'surp2': 3, 'surp3': 3, 'shys': 3, 'surp1s': 3, 'surp2s': 3, 'surp3s': 3},
        }

        distance_to_position = {
            "far": (630, 1080),
            "normal": (900, 1080),
            "close": (1050, 1080)
        }

        def _sprite_for_all_times(full_sprite_name, composite_image):
            """
            Объявляем спрайт для всех времен суток
            """
            renpy.image(
                full_sprite_name,
                ConditionSwitch(
                    "persistent.sprite_time == 'sunset'", im.MatrixColor(composite_image, nd_tint["sunset"]),
                    "persistent.sprite_time == 'night'", im.MatrixColor(composite_image, nd_tint["night"]),
                    True, composite_image,
                )
            )

        def _dark_sprite(full_sprite_name, composite_image):
            """
            Спрайт в темноте
            """
            renpy.image(full_sprite_name, im.MatrixColor(composite_image, im.matrix.brightness(-0.99)))

        # Генератор новых спрайтов для персонажей из оригинального БЛ

        def make_sprites_for(character, sprite_name, layers, emotions=None, distances=None, exclude=None, sprite_define_func=None, default=True):
            """
            Позволяет объявить почти любой спрайт, состоящий из нескольких слоев,
            каждый слой может идти либо из мода, либо из оригинала.
            Картинки должны класться в папки строго как в оригинале, чтобы это работало.
            """

            if emotions is None:
                emotions = nd_emotion_to_pose[character].keys()
            if distances is None:
                distances = distance_to_position.keys()
            if sprite_define_func is None:
                sprite_define_func = _sprite_for_all_times

            for emotion in emotions:
                if exclude and emotion in exclude:
                    continue

                pose = nd_emotion_to_pose[character][emotion]

                for distance in distances:
                    # Получаем название спрайта, например dv angry bkrr_sport far
                    full_sprite_name = '%s %s %s' % (character, emotion, sprite_name)
                    if not sprite_name:
                        full_sprite_name = '%s %s' % (character, emotion)  # Не у всех есть одежда
                    if distance != 'normal':
                        full_sprite_name += ' ' + distance

                    # Комбинируем изображение
                    image_parts = [distance_to_position[distance]]
                    for layer in layers:
                        source, file_name = layer.split(':')
                        base_path = 'mods/notdream/images/' if source == 'mod' else 'mods/notdream/images/'
                        if default:
                            image_path = base_path + "sprites/%s/%s/%s_%s_%s.png" % (
                                character, distance, character, pose, file_name if file_name != '<emotion>' else emotion,
                            )
                        else:
                            image_path = base_path + "sprites/%s/%s/old/%s_%s_%s.png" % (
                                character, distance, character, pose, file_name if file_name != '<emotion>' else emotion,
                            )
                        image_parts += [(0, 0), image_path]
                    composite_image = im.Composite(*image_parts)

                    # Объявляем спрайт
                    sprite_define_func(full_sprite_name, composite_image)


        def make_sprites_with_custom_emotions(custom_emotions, *args):
            """
            Удобно, когда нужно объявить новую эмоцию
            """
            args = list(args)
            assert args[-1][-1] == 'es:<emotion>'
            make_sprites_for(*args, exclude=custom_emotions)
            args[-1][-1] = 'mod:<emotion>'
            make_sprites_for(*args, emotions=custom_emotions)

        # Объявляем спрайты
        make_sprites_for('us', 'bra', ['es:body', 'mod:bra', 'es:<emotion>'])
        make_sprites_for('us', 'nd_dress', ['mod:dress', 'es:<emotion>'])
        make_sprites_for('us', 'night_shirt', ['mod:night_shirt', 'es:<emotion>'])
        make_sprites_for('us', 'night_shirt', ['mod:night_shirt', 'mod:<emotion>'], emotions=['yawn', 'shys'])
        make_sprites_for('us', 'backpack sport', ['es:body', 'es:sport', 'mod:backpack', 'es:<emotion>'], distances=['normal'])
        make_sprites_for('us', 'naked', ['mod:body', 'es:<emotion>'])