@namespace
class SpriteKind:
    Player_2 = SpriteKind.create()
    Projectile_2 = SpriteKind.create()
    Arrow_1 = SpriteKind.create()
    Arrow_2 = SpriteKind.create()
    Health_1 = SpriteKind.create()
    sword = SpriteKind.create()
    Player_4 = SpriteKind.create()
    Arrow_4 = SpriteKind.create()
    player3 = SpriteKind.create()
    Arrow3 = SpriteKind.create()
# Todo: Make health pickups

def on_on_overlap(sprite, otherSprite):
    info.player2.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.Player_2, SpriteKind.projectile, on_on_overlap)

def on_player4_connected():
    controller.player4.move_sprite(Player4)
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_player3_button_b_pressed():
    global sword2
    if p3_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . e . . . . . . . . . . 
                            f f f f f e 1 1 1 1 1 1 1 1 . . 
                            f f f f f e 1 1 1 1 1 1 . . . . 
                            . . . . . e . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            player32,
            p3_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . e . . . . . 
                            . . 1 1 1 1 1 1 1 1 e f f 3 f f 
                            . . . . 1 1 1 1 1 1 e f f f f f 
                            . . . . . . . . . . e . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            player32,
            p3_b * 5,
            0)
    sword2.x += p3_b
    pause(100)
    sprites.destroy(sword2)
controller.player3.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player3_button_b_pressed)

def on_player2_button_b_pressed():
    global sword2
    if p2_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . e . . . . . . . . . .
                            f f f f f e 1 1 1 1 1 1 1 1 . .
                            f f f f f e 1 1 1 1 1 1 . . . .
                            . . . . . e . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            Player2,
            p2_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . e . . . . . 
                            . . 1 1 1 1 1 1 1 1 e f f 3 f f 
                            . . . . 1 1 1 1 1 1 e f f f f f 
                            . . . . . . . . . . e . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player2,
            p2_b * 5,
            0)
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_player4_button_b_pressed():
    global sword2
    if p4_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . e . . . . . . . . . . 
                            f f f f f e 1 1 1 1 1 1 1 1 . . 
                            f f f f f e 1 1 1 1 1 1 . . . . 
                            . . . . . e . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player4,
            p4_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . e . . . . . 
                            . . 1 1 1 1 1 1 1 1 e f f 3 f f 
                            . . . . 1 1 1 1 1 1 e f f f f f 
                            . . . . . . . . . . e . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player4,
            p4_b * 5,
            0)
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed)

def on_player2_button_b_pressed2():
    global sword2
    if p2_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player2,
            p2_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player2,
            p2_b * 5,
            0)
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed2)

def on_player4_button_b_pressed2():
    global sword2
    if p4_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player4,
            p4_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player4,
            p4_b * 5,
            0)
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed2)

def on_player2_button_b_pressed3():
    global sword2
    if p2_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player2,
            p2_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player2,
            p2_b * 5,
            0)
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed3)

def on_player4_button_b_pressed3():
    global sword2
    if p4_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player4,
            p4_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player4,
            p4_b * 5,
            0)
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed3)

def on_player2_button_b_pressed4():
    global sword2
    if p2_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player2,
            p2_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player2,
            p2_b * 5,
            0)
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed4)

def on_player4_button_b_pressed4():
    global sword2
    if p4_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . f f f 
                            . . . . . . . . . . . . f 9 9 f 
                            . . . . . . . . . . . f 9 6 9 f 
                            . . . . . . . . . . f 9 6 9 f . 
                            . . . . . . . . . f 9 6 9 f . . 
                            . . . . . . . . f 9 6 9 f . . . 
                            . . f f . . . f 9 6 9 f . . . . 
                            . . f 9 f . f 9 6 9 f . . . . . 
                            . . . f 9 f 9 6 9 f . . . . . . 
                            . . . f 9 9 f 9 f . . . . . . . 
                            . . . . f 9 9 f . . . . . . . . 
                            . . . e e f 9 9 f . . . . . . . 
                            . . e e e . f f 9 f . . . . . . 
                            f f e e . . . . f f . . . . . . 
                            f 9 f . . . . . . . . . . . . . 
                            f f f . . . . . . . . . . . . .
            """),
            Player4,
            p4_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                f f f . . . . . . . . . . . . . 
                            f 9 9 f . . . . . . . . . . . . 
                            f 9 6 9 f . . . . . . . . . . . 
                            . f 9 6 9 f . . . . . . . . . . 
                            . . f 9 6 9 f . . . . . . . . . 
                            . . . f 9 6 9 f . . . . . . . . 
                            . . . . f 9 6 9 f . . . f f . . 
                            . . . . . f 9 6 9 f . f 9 f . . 
                            . . . . . . f 9 6 9 f 9 f . . . 
                            . . . . . . . f 9 f 9 9 f . . . 
                            . . . . . . . . f 9 9 f . . . . 
                            . . . . . . . f 9 9 f e e . . . 
                            . . . . . . f 9 f f . e e e . . 
                            . . . . . . f f . . . . e e f f 
                            . . . . . . . . . . . . . f 9 f 
                            . . . . . . . . . . . . . f f f
            """),
            Player4,
            p4_b * 5,
            0)
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
controller.player4.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player4_button_b_pressed4)

def on_player2_button_a_pressed():
    global Arrow
    if p2_b > 0:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player2,
            p2_a,
            0)
    else:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player2,
            p2_a,
            0)
    Arrow.x += p2_b
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player4_life_zero():
    sprites.destroy(Pointer_4)
    Send_Player_4_to_the_shadow_realm3()
info.player4.on_life_zero(on_player4_life_zero)

def Send_Player_2_to_the_shadow_realm():
    for index in range(15):
        Player2.x += 1e+21
# Todo: Make health pickups

def on_on_overlap2(sprite2, otherSprite2):
    info.player4.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.Player_4, SpriteKind.projectile, on_on_overlap2)

def Send_Player_1_to_the_shadow_realm2():
    for index2 in range(15):
        Player1.x += 1e+21
def Send_Player_4_to_the_shadow_realm3():
    for index3 in range(15):
        Player4.x += 1e+21

def on_on_overlap3(sprite22, otherSprite22):
    info.player1.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap3)

def on_player3_connected():
    controller.player3.move_sprite(player32)
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_player3_button_right_pressed():
    global p3_a, p3_b
    p3_a = 50
    p3_b = 15
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_right_pressed)

# Todo: Make health pickups

def on_on_overlap4(sprite3, otherSprite3):
    info.player3.change_life_by(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
sprites.on_overlap(SpriteKind.player3, SpriteKind.projectile, on_on_overlap4)

def on_player2_button_right_pressed():
    global p2_a, p2_b
    p2_a = 50
    p2_b = 15
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player4_button_a_pressed():
    global Arrow
    if p4_b > 0:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player4,
            p4_a,
            0)
    else:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player4,
            p4_a,
            0)
    Arrow.x += p4_b
controller.player4.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player4_button_a_pressed)

def on_player2_button_left_pressed():
    global p2_a, p2_b
    p2_a = -50
    p2_b = -15
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player1_button_right_pressed():
    global P1_a, P1_b
    P1_a = 50
    P1_b = 15
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_a_pressed():
    global Arrow
    if P1_b > 0:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player1,
            P1_a,
            0)
    else:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            Player1,
            P1_a,
            0)
    Arrow.x += P1_b
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player4_button_left_pressed():
    global p4_a, p4_b
    p4_a = -50
    p4_b = -15
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_left_pressed)

def on_player1_life_zero():
    sprites.destroy(Pointer_1)
    Send_Player_1_to_the_shadow_realm2()
info.player1.on_life_zero(on_player1_life_zero)

def on_player3_button_a_pressed():
    global Arrow
    if p3_b > 0:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            player32,
            p3_a,
            0)
    else:
        Arrow = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            """),
            player32,
            p3_a,
            0)
    Arrow.x += p3_b
controller.player3.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player3_button_a_pressed)

def on_player2_life_zero():
    sprites.destroy(Pointer_2)
    Send_Player_2_to_the_shadow_realm()
info.player2.on_life_zero(on_player2_life_zero)

def on_player2_connected():
    controller.player2.move_sprite(Player2)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player1_button_b_pressed():
    global sword2
    if P1_b > 0:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . e . . . . . . . . . . 
                            f f f f f e 1 1 1 1 1 1 1 1 . . 
                            f f f f f e 1 1 1 1 1 1 . . . . 
                            . . . . . e . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player1,
            P1_b * 5,
            0)
    else:
        sword2 = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . e . . . . . 
                            . . 1 1 1 1 1 1 1 1 e f f 3 f f 
                            . . . . 1 1 1 1 1 1 e f f f f f 
                            . . . . . . . . . . e . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            Player1,
            P1_b * 5,
            0)
    sword2.x += P1_b
    pause(100)
    sprites.destroy(sword2)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_player1_connected():
    controller.player1.move_sprite(Player1)
controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

def on_player4_button_right_pressed():
    global p4_a, p4_b
    p4_a = 50
    p4_b = 15
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_right_pressed)

def on_player3_button_left_pressed():
    global p3_a, p3_b
    p3_a = -50
    p3_b = -15
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_left_pressed)

def on_player1_button_left_pressed():
    global P1_a, P1_b
    P1_a = -50
    P1_b = -15
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

p4_a = 0
p3_a = 0
p4_b = 0
p3_b = 0
P1_a = 0
P1_b = 0
p2_a = 0
p2_b = 0
sword2: Sprite = None
Pointer_4: Sprite = None
Pointer_2: Sprite = None
Pointer_1: Sprite = None
Player4: Sprite = None
player32: Sprite = None
Player2: Sprite = None
Player1: Sprite = None
Arrow: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level2
"""))
Arrow = sprites.create(img("""
        . . . . . . . . 
            b . . . . . . . 
            . b . . . . 1 . 
            . . e e e e 1 1 
            . b . . . . 1 . 
            b . . . . . . . 
            . . . . . . . . 
            . . . . . . . .
    """),
    SpriteKind.projectile)
Arrow_22 = sprites.create(img("""
        . . . . . . . . 
            b . . . . . . . 
            . b . . . . 1 . 
            . . e e e e 1 1 
            . b . . . . 1 . 
            b . . . . . . . 
            . . . . . . . . 
            . . . . . . . .
    """),
    SpriteKind.Projectile_2)
Player1 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . e e e e e e . . . . . 
            . . . . e e e e e e e e . . . . 
            . . . . e e d d d d e e . . . . 
            . . . . e d f d d f d e . . . . 
            . . . . e d d d d d d e e . . . 
            . . . . e e d d d d e e e . . . 
            . . . . . f f f f f f . e e . . 
            . . . . . d f f f f d . . e . . 
            . . . . . d f f f f d . . . . . 
            . . . . . d f f f f d . . . . . 
            . . . . . . f f f f . . . . . . 
            . . . . . . f . . f . . . . . . 
            . . . . . . f . . f . . . . . .
    """),
    SpriteKind.player)
Player2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . 5 5 5 5 5 5 . . . . . 
            . . . . 5 5 5 5 5 5 5 5 . . . . 
            . . . . 5 5 d d d d 5 5 . . . . 
            . . . . 5 d f d d f d 5 . . . . 
            . . . . . d f d d f d . . . . . 
            . . . . . . d d d d . . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . . . f f f f f f . . . . . 
            . . . . . d f f f f d . . . . . 
            . . . . . d f f f f d . . . . . 
            . . . . . . f . . f . . . . . . 
            . . . . . . f . . f . . . . . . 
            . . . . . f f . f f . . . . . . 
            . . . . . f f . f f . . . . . .
    """),
    SpriteKind.Player_2)
player32 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . 7 7 7 7 . . . . . 
            . . . . . . 7 7 . . 7 . . . . . 
            . . . . . . 7 7 . . 7 . . . . . 
            . . . . . . 7 7 7 7 7 . . . . . 
            . . . . . . . 7 7 7 . . . . . . 
            . . . . . . 7 . 7 . 7 . . . . . 
            . . . . . . 7 . 7 . 7 7 . . . . 
            . . . . . . . . 7 . . . . . . . 
            . . . . . . . . 7 . . . . . . . 
            . . . . . . . 7 . 7 . . . . . . 
            . . . . . . . 7 . 7 . . . . . . 
            . . . . . . 7 . . 7 7 . . . . . 
            . . . . . . 7 . . . 7 . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player3)
Player4 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . 4 4 4 4 . . . . . . 
            . . . . . 4 4 4 4 4 4 . . . . . 
            . . . . 4 4 d d d d 4 4 . . . . 
            . . . . 4 d f d d f d 4 . . . . 
            . . . . . d d d d d d . . . . . 
            . . . . . . d d d d . . . . . . 
            . . . . 2 2 2 2 2 2 2 2 . . . . 
            . . . . d 2 2 2 2 2 2 d . . . . 
            . . . . d d 2 2 2 2 d d . . . . 
            . . . . d d 2 2 2 2 d d . . . . 
            . . . . d . e . . e . d . . . . 
            . . . . . . e . . e . . . . . . 
            . . . . . . e . . e . . . . . . 
            . . . . . f f . . f f . . . . .
    """),
    SpriteKind.Player_4)
sprites.destroy(Arrow)
sprites.destroy(Arrow_22)
Pointer_1 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow_1)
Pointer_2 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow_2)
Pointer_3 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow3)
Pointer_4 = sprites.create(img("""
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    """),
    SpriteKind.Arrow_4)
info.player2.set_life(3)
info.player1.set_life(3)
info.player4.set_life(3)
sword2 = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.sword)
p2_b = 99999999
p2_a = 99999990
P1_b = 9999999
P1_a = 999999999

def on_forever():
    Pointer_1.set_position(Player1.x + P1_b, Player1.y)
forever(on_forever)

def on_forever2():
    pass
forever(on_forever2)

def on_forever3():
    Pointer_4.set_position(Player4.x + p4_b, Player4.y)
    Pointer_4.set_position(Player4.x + p4_b, Player4.y)
forever(on_forever3)

def on_forever4():
    Pointer_3.set_position(player32.x + p3_b, player32.y)
forever(on_forever4)
