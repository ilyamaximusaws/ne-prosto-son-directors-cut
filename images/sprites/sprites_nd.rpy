init:

    $ nd_tint = {
        "sunset":im.matrix.tint(0.94, 0.82, 1.0),
        "night":im.matrix.tint(0.63, 0.78, 0.82)
    }
#Семен - Пионерская форма

    image pi2 angry pioneer = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png") )
    

    image pi2 grin pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png") )
    

    image pi2 normal pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png") )
    

    image pi2 serious pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png") )
    

    image pi2 shocked pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png") )
    

    image pi2 smile pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png") )
    

    image pi2 surprise pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png") )
    

    image pi2 upset pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_pioneer.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png") )

#Пионер - В черной рубашке

    image pi2 angry shirt = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_angry.png") )
    

    image pi2 grin shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_grin.png") )
    

    image pi2 normal shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png") )
    

    image pi2 serious shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_serious.png") )
    

    image pi2 shocked shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_shocked.png") )
    

    image pi2 smile shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_smile.png") )
    

    image pi2 surprise shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_surprise.png") )
    

    image pi2 upset shirt = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png",(0,0), "mods/notdream/images/sprites/pi2/pi_2_upset.png") )

#Физрук

    image ba ev = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_ev.png") )
    

    image ba normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_norm.png") )
    

    image ba sm = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi2/pi_2_shirt.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png",(0,0), "mods/notdream/images/sprites/ba/ba_1_sm.png") )

#Алиса

    # Алиса в пальто - Ночь
    image dv surprise coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_1_coat_n.png") )
    

    image dv smile coat = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png",(0,0), "mods/notdream/images/sprites/dv_coat/dv_3_coat_n.png") )


    # - Алиса в вечернем платье
    image dv grin dance = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_grin.png") )
    

    image dv normal dance = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png",(0,0), "mods/notdream/images/sprites/dv_alice/dv_dance_normal.png") )

#Василий

    # - Василий (в РФ)    
    image vsb rf = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((6900,1080), (0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png",(0,0), "mods/notdream/images/sprites/vas/vsb.png") )
    
    image vsc rf = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png",(0,0), "mods/notdream/images/sprites/vas/vsc.png") )

    image vscl rf = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png",(0,0), "mods/notdream/images/sprites/vas/vscl.png") )
    
    image vsm rf = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png",(0,0), "mods/notdream/images/sprites/vas/vsm.png") )
    
#Талян
    
    image tl_1_pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png",(0,0), "mods/notdream/images/sprites/tl/tl_1_pioneer.png") )

#Ульяна с телефоном в руке

    image us_smile_sport_phone = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png",(0,0), "mods/notdream/images/sprites/us/us_smile_sport_phone.png") )

#Пионер который глазюками синими своими светит
    
    image pi eyelight = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png",(0,0), "mods/notdream/images/sprites/pi/pi_lightening.png") )

#Васлий лагерный | normal

    image vst normal pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_normal.png"), nd_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_normal.png"), nd_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_normal.png"))

    image vst sad pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_sad.png"), nd_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_sad.png"), nd_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_sad.png"))

    image vst shy pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_shy.png"), nd_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_shy.png"), nd_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_shy.png"))

    image vst smile pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_smile.png"), nd_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_smile.png"), nd_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_smile.png"))

    image vst surprise pioneer = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_surprise.png"), nd_tint["sunset"]),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_surprise.png"), nd_tint["night"]),
        True, im.Composite((900, 1080), (0, 0), "mods/notdream/images/sprites/vst/vst_surprise.png"))

#Ростян
    
    image rost laugh hike = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_hike.png', im.matrix.tint(0.94, 0.82, 1.0)), 
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_hike.png', im.matrix.tint(0.63, 0.78, 0.82)), 
        True, 'mods/notdream/images/sprites/rost/rost_laugh_hike.png')

    image rost laugh pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_pioneer.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_pioneer.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_laugh_pioneer.png')
    
    image rost laugh sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_sport.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_sport.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_laugh_sport.png')

    image rost laugh swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_swim.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_laugh_swim.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_laugh_swim.png')

    image rost normal hike = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_hike.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_hike.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_normal_hike.png')
    
    image rost normal pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_pioneer.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_pioneer.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_normal_pioneer.png')
    
    image rost normal sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_sport.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_sport.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_normal_sport.png')

    image rost normal swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_swim.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_normal_swim.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_normal_swim.png')

    image rost sad hike = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_hike.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_hike.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_sad_hike.png')

    image rost sad pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_pioneer.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_pioneer.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_sad_pioneer.png')

    image rost sad sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_sport.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_sport.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_sad_sport.png')

    image rost sad swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_swim.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_sad_swim.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_sad_swim.png')

    image rost serious hike = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_hike.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_hike.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_serious_hike.png')

    image rost serious pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_pioneer.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_pioneer.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_serious_pioneer.png')
    
    image rost serious sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_sport.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_sport.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_serious_sport.png')

    image rost serious swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_swim.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_serious_swim.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_serious_swim.png')
    
    image rost smile hike = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_hike.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_hike.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_smile_hike.png')

    image rost smile pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_pioneer.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_pioneer.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_smile_pioneer.png')

    image rost smile sport = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_sport.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_sport.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_smile_sport.png')

    image rost smile swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_swim.png', im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time=='night'", im.MatrixColor('mods/notdream/images/sprites/rost/rost_smile_swim.png', im.matrix.tint(0.63, 0.78, 0.82)),
        True, 'mods/notdream/images/sprites/rost/rost_smile_swim.png')

#Мужчина в 5-м дне в городе

    image nd_muz normal shirt = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'))
    image nd_muz smile shirt = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_shirt.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png'))
    image nd_muz normal sweater = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_normal.png'))
    image nd_muz smile sweater = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 2100), (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_sweater.png', (0, 0), 'mods/notdream/images/sprites/nd_muz/nd_muz_smile.png')) 

#Девушка в 4м дне в столовой
    image nd_rey normal pioneer = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1355,2024), (0,0), "mods/notdream/images/sprites/nd_rey/nd_rey_normal_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1355,2024), (0,0), "mods/notdream/images/sprites/nd_rey/nd_rey_normal_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1355,2024), (0,0), "mods/notdream/images/sprites/nd_rey/nd_rey_normal_pioneer.png"))

# Пионер 3 версия в куртке
    image pi3 normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_normal.png") )
    
    image pi3 annoyed = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png",(0,0), "mods/notdream/images/sprites/pi3/nd_pi3_annoyed.png") )

# OWN Даша normal
    image da normal = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_normal_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_normal_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_normal_1.png") )

    image da smile = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_smile_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_smile_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_smile_1.png") )

    image da grin = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_grin_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_grin_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_grin_1.png") )

    image da upset = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_upset_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_upset_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_upset_1.png") )

    image da guilty = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_guilty_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_guilty_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_guilty_1.png") )

    image da laugh = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_laugh_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_laugh_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_laugh_2.png") )

    image da surprise = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_surprise_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_surprise_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_surprise_2.png") )

    image da shocked = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_shocked_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_shocked_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_shocked_2.png") )

    image da sad = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_sad_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_sad_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_sad_2.png") )

    image da angry = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_angry_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_angry_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_angry_3.png") )

    image da dontlike = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_dontlike_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_dontlike_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_dontlike_3.png") )

# OWN Даша far
    image da normal far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_normal_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_normal_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_normal_1.png") )

    image da smile far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_smile_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_smile_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_smile_1.png") )

    image da grin far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_grin_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_grin_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_grin_1.png") )

    image da upset far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_upset_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_upset_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_upset_1.png") )

    image da guilty far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_guilty_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_guilty_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_guilty_1.png") )

    image da laugh far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_laugh_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_laugh_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_laugh_2.png") )

    image da surprise far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_surprise_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_surprise_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_surprise_2.png") )

    image da shocked far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_shocked_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_shocked_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_shocked_2.png") )

    image da sad far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_sad_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_sad_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_sad_2.png") )

    image da angry far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_angry_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_angry_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_angry_3.png") )

    image da dontlike far = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_dontlike_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_dontlike_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((675,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/far/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_dontlike_3.png") )

# OWN Даша close

    image da normal close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_normal_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_normal_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_normal_1.png") )

    image da smile close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_smile_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_smile_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_smile_1.png") )

    image da grin close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_grin_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_grin_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_grin_1.png") )

    image da upset close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_upset_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_upset_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_upset_1.png") )

    image da guilty close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_guilty_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_guilty_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_1.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_guilty_1.png") )

    image da laugh close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_laugh_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_laugh_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_laugh_2.png") )

    image da surprise close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_surprise_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_surprise_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_surprise_2.png") )

    image da shocked close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_shocked_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_shocked_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_shocked_2.png") )

    image da sad close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_sad_2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_sad_2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_2.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_sad_2.png") )

    image da angry close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_angry_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_angry_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_angry_3.png") )

    image da dontlike close = ConditionSwitch( 
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_dontlike_3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_dontlike_3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1125,1080), (0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_body_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/close/da_clothing_3.png",(0,0), "mods/notdream/images/sprites/own_sprites/nda/normal/da_dontlike_3.png") )
    
#Аделина - спортивная форма

    image adl normal sport = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_normal.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_normal.png") )
  
    image adl fear sport = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_fear.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_fear.png") )  
    
    image adl smile sport = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/sport/body_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/clothes_smile.png",(0,0), "mods/notdream/images/sprites/adl_new/sport/liso_smile.png") )  
    
#Аделина - пионерская форма

    image adl vina pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_vina.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_vina.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_vina.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_vina.png") )     
  
    image adl normal pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_normal_pf.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_normal_pf.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_normal_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_normal_pf.png") )       
    
    image adl laugh pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_laugh.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_laugh.png") )      

    image adl shy pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_shy.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_shy.png") )           
    
    image adl fear pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_fear_pf.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_fear_pf.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_fear_pf.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_fear_pf.png") )   
    
    image adl surprise pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_surprise.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_surprise.png") )        
    
    image adl smile1 pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png") )   
    
    image adl smile2 pioneer = ConditionSwitch( "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/body_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/clothes_smile_1.png",(0,0), "mods/notdream/images/sprites/adl_new/pioneer_f/liso_smile_1.png") )