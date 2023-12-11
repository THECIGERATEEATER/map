namespace SpriteKind {
    export const Player_2 = SpriteKind.create()
    export const Projectile_2 = SpriteKind.create()
    export const Arrow_1 = SpriteKind.create()
    export const Arrow_2 = SpriteKind.create()
    export const Health_1 = SpriteKind.create()
    export const sword = SpriteKind.create()
    export const Player_4 = SpriteKind.create()
    export const Arrow_4 = SpriteKind.create()
    export const player3 = SpriteKind.create()
    export const Arrow3 = SpriteKind.create()
}

//  Todo: Make health pickups
sprites.onOverlap(SpriteKind.Player_2, SpriteKind.Projectile, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    info.player2.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
controller.player4.onEvent(ControllerEvent.Connected, function on_player4_connected() {
    controller.player4.moveSprite(Player4)
})
controller.player3.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player3_button_b_pressed() {
    
    if (p3_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, player32, p3_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, player32, p3_b * 5, 0)
    }
    
    sword2.x += p3_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player2_button_b_pressed() {
    
    if (p2_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    }
    
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player4_button_b_pressed() {
    
    if (p4_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    }
    
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player2_button_b_pressed2() {
    
    if (p2_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    }
    
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player4_button_b_pressed2() {
    
    if (p4_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    }
    
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player2_button_b_pressed3() {
    
    if (p2_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    }
    
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player4_button_b_pressed3() {
    
    if (p4_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    }
    
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player2_button_b_pressed4() {
    
    if (p2_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player2, p2_b * 5, 0)
    }
    
    sword2.x += p2_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player4.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player4_button_b_pressed4() {
    
    if (p4_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player4, p4_b * 5, 0)
    }
    
    sword2.x += p4_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player2_button_a_pressed() {
    
    if (p2_b > 0) {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player2, p2_a, 0)
    } else {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player2, p2_a, 0)
    }
    
    Arrow.x += p2_b
})
info.player4.onLifeZero(function on_player4_life_zero() {
    sprites.destroy(Pointer_4)
    Send_Player_4_to_the_shadow_realm3()
})
function Send_Player_2_to_the_shadow_realm() {
    for (let index = 0; index < 15; index++) {
        Player2.x += 1e+21
    }
}

//  Todo: Make health pickups
sprites.onOverlap(SpriteKind.Player_4, SpriteKind.Projectile, function on_on_overlap2(sprite2: Sprite, otherSprite2: Sprite) {
    info.player4.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
function Send_Player_1_to_the_shadow_realm2() {
    for (let index2 = 0; index2 < 15; index2++) {
        Player1.x += 1e+21
    }
}

function Send_Player_4_to_the_shadow_realm3() {
    for (let index3 = 0; index3 < 15; index3++) {
        Player4.x += 1e+21
    }
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function on_on_overlap3(sprite22: Sprite, otherSprite22: Sprite) {
    info.player1.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
controller.player3.onEvent(ControllerEvent.Connected, function on_player3_connected() {
    controller.player3.moveSprite(player32)
})
controller.player3.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_player3_button_right_pressed() {
    
    p3_a = 50
    p3_b = 15
})
//  Todo: Make health pickups
sprites.onOverlap(SpriteKind.player3, SpriteKind.Projectile, function on_on_overlap4(sprite3: Sprite, otherSprite3: Sprite) {
    info.player3.changeLifeBy(-1)
    sprites.destroy(Arrow)
    sprites.destroy(sword2)
})
controller.player2.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_player2_button_right_pressed() {
    
    p2_a = 50
    p2_b = 15
})
controller.player4.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player4_button_a_pressed() {
    
    if (p4_b > 0) {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player4, p4_a, 0)
    } else {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player4, p4_a, 0)
    }
    
    Arrow.x += p4_b
})
controller.player2.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_player2_button_left_pressed() {
    
    p2_a = -50
    p2_b = -15
})
controller.player1.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_player1_button_right_pressed() {
    
    P1_a = 50
    P1_b = 15
})
controller.player1.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player1_button_a_pressed() {
    
    if (P1_b > 0) {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player1, P1_a, 0)
    } else {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            `, Player1, P1_a, 0)
    }
    
    Arrow.x += P1_b
})
controller.player4.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_player4_button_left_pressed() {
    
    p4_a = -50
    p4_b = -15
})
info.player1.onLifeZero(function on_player1_life_zero() {
    sprites.destroy(Pointer_1)
    Send_Player_1_to_the_shadow_realm2()
})
controller.player3.onButtonEvent(ControllerButton.A, ControllerButtonEvent.Pressed, function on_player3_button_a_pressed() {
    
    if (p3_b > 0) {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            b . . . . . . . 
                            . b . . . . 1 . 
                            . . e e e e 1 1 
                            . b . . . . 1 . 
                            b . . . . . . . 
                            . . . . . . . . 
                            . . . . . . . .
            `, player32, p3_a, 0)
    } else {
        Arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . 
                            . . . . . . . b 
                            . 1 . . . . b . 
                            1 1 e e e e . . 
                            . 1 . . . . b . 
                            . . . . . . . b 
                            . . . . . . . . 
                            . . . . . . . .
            `, player32, p3_a, 0)
    }
    
    Arrow.x += p3_b
})
info.player2.onLifeZero(function on_player2_life_zero() {
    sprites.destroy(Pointer_2)
    Send_Player_2_to_the_shadow_realm()
})
controller.player2.onEvent(ControllerEvent.Connected, function on_player2_connected() {
    controller.player2.moveSprite(Player2)
})
controller.player1.onButtonEvent(ControllerButton.B, ControllerButtonEvent.Pressed, function on_player1_button_b_pressed() {
    
    if (P1_b > 0) {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player1, P1_b * 5, 0)
    } else {
        sword2 = sprites.createProjectileFromSprite(img`
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
            `, Player1, P1_b * 5, 0)
    }
    
    sword2.x += P1_b
    pause(100)
    sprites.destroy(sword2)
})
controller.player1.onEvent(ControllerEvent.Connected, function on_player1_connected() {
    controller.player1.moveSprite(Player1)
})
controller.player4.onButtonEvent(ControllerButton.Right, ControllerButtonEvent.Pressed, function on_player4_button_right_pressed() {
    
    p4_a = 50
    p4_b = 15
})
controller.player3.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_player3_button_left_pressed() {
    
    p3_a = -50
    p3_b = -15
})
controller.player1.onButtonEvent(ControllerButton.Left, ControllerButtonEvent.Pressed, function on_player1_button_left_pressed() {
    
    P1_a = -50
    P1_b = -15
})
let p4_a = 0
let p3_a = 0
let p4_b = 0
let p3_b = 0
let P1_a = 0
let P1_b = 0
let p2_a = 0
let p2_b = 0
let sword2 : Sprite = null
let Pointer_4 : Sprite = null
let Pointer_2 : Sprite = null
let Pointer_1 : Sprite = null
let Player4 : Sprite = null
let player32 : Sprite = null
let Player2 : Sprite = null
let Player1 : Sprite = null
let Arrow : Sprite = null
tiles.setCurrentTilemap(tilemap`
    level2
`)
Arrow = sprites.create(img`
        . . . . . . . . 
            b . . . . . . . 
            . b . . . . 1 . 
            . . e e e e 1 1 
            . b . . . . 1 . 
            b . . . . . . . 
            . . . . . . . . 
            . . . . . . . .
    `, SpriteKind.Projectile)
let Arrow_22 = sprites.create(img`
        . . . . . . . . 
            b . . . . . . . 
            . b . . . . 1 . 
            . . e e e e 1 1 
            . b . . . . 1 . 
            b . . . . . . . 
            . . . . . . . . 
            . . . . . . . .
    `, SpriteKind.Projectile_2)
Player1 = sprites.create(img`
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
    `, SpriteKind.Player)
Player2 = sprites.create(img`
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
    `, SpriteKind.Player_2)
player32 = sprites.create(img`
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
    `, SpriteKind.player3)
Player4 = sprites.create(img`
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
    `, SpriteKind.Player_4)
sprites.destroy(Arrow)
sprites.destroy(Arrow_22)
Pointer_1 = sprites.create(img`
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    `, SpriteKind.Arrow_1)
Pointer_2 = sprites.create(img`
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    `, SpriteKind.Arrow_2)
let Pointer_3 = sprites.create(img`
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    `, SpriteKind.Arrow3)
Pointer_4 = sprites.create(img`
        . . 7 . . 
            . . 7 . . 
            7 7 7 7 7 
            . . 7 . . 
            . . 7 . .
    `, SpriteKind.Arrow_4)
info.player2.setLife(3)
info.player1.setLife(3)
info.player4.setLife(3)
sword2 = sprites.create(img`
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
    `, SpriteKind.sword)
p2_b = 99999999
p2_a = 99999990
P1_b = 9999999
P1_a = 999999999
forever(function on_forever() {
    Pointer_1.setPosition(Player1.x + P1_b, Player1.y)
})
forever(function on_forever2() {
    
})
forever(function on_forever3() {
    Pointer_4.setPosition(Player4.x + p4_b, Player4.y)
    Pointer_4.setPosition(Player4.x + p4_b, Player4.y)
})
forever(function on_forever4() {
    Pointer_3.setPosition(player32.x + p3_b, player32.y)
})
