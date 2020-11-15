from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *


def teveColisao(personagem, plataforma1, plataforma2, plataforma3):
    return (personagem.collided(plataforma1) or personagem.collided(plataforma2) or personagem.collided(plataforma3))


def pular(personagem, teclado, tempoPulo, plataforma1, plataforma2, plataforma3):
    if (tempoPulo > 0):
        personagem.y -= 20

    if (teclado.key_pressed("up") and teveColisao(personagem, plataforma1, plataforma2, plataforma3)):
        tempoPulo = 20

    if (not teveColisao(personagem, plataforma1, plataforma2, plataforma3)):
        personagem.y += 10

    tempoPulo -= 1

    return tempoPulo


def desenharMovimentos(personagem, teclado, ultimaDirecao):
    personagemParadoEsquerda = Sprite("images/personagem/personagem_parado_esquerda.png")

    direcoes = {'right': personagem, 'left': personagemParadoEsquerda}

    if (teclado.key_pressed("left")):
        ultimaDirecao = 'left'
        personagem.x -= 4

    if (teclado.key_pressed("right")):
        ultimaDirecao = 'right'
        personagem.x += 4

    direcoes[ultimaDirecao].x = personagem.x
    direcoes[ultimaDirecao].y = personagem.y
    direcoes[ultimaDirecao].draw()

    return ultimaDirecao


def configurarVidas(dificuldade):
    vida1 = Sprite("images/personagem/vida.png")
    vida2 = Sprite("images/personagem/vida.png")
    vida3 = Sprite("images/personagem/vida.png")

    # configurarVidas
    vida1.x = 30
    vida1.y = 30
    vida2.x = 60
    vida2.y = 30
    vida3.x = 90
    vida3.y = 30

    return [vida1, vida2, vida3]


def cronometroECriacaoTiros(cronometro, tiros, personagem, teclado, ultimaDirecao):

    if (teclado.key_pressed("z") and cronometro > 40):

        bullet = Sprite("images/personagem/bullet.png")
        bullet.y = personagem.y + personagem.height / 2

        if (ultimaDirecao == 'right'):
            bullet.direction = 'right'
            bullet.x = personagem.x + personagem.width
        else:
            bullet.direction = 'left'
            bullet.x = personagem.x

        tiros.append(bullet)
        cronometro = 0

    cronometro += 1

    return cronometro


def desenharTiros(tiros, janela):
    for tiro in tiros:

        if (tiro.direction == 'right'):
            tiro.x += 15
        else:
            tiro.x -= 15

        if (tiro.x > janela.width):
            tiros.remove(tiro)
        elif (tiro.x < 0):
            tiros.remove(tiro)

    for tiro in tiros:
        tiro.draw()


def iniciarNovoJogo(dificuldade, janela):
    vidas = 3

    tempoPulo = 0

    ultimaDirecao = 'right'

    tiros = []

    cronometro = 0

    # Controles
    teclado = Window.get_keyboard()

    # Imagens e Sprites
    background1 = GameImage("images/mapa_1/mapa_1_pt1.png")

    personagem = Sprite("images/personagem/personagem_parado.png")

    listaVidas = configurarVidas(dificuldade)

    plataforma1 = GameObject()
    plataforma1.x = 215
    plataforma1.y = 310
    plataforma1.width = 200
    plataforma1.height = 1

    plataforma2 = GameObject()
    plataforma2.x = 480
    plataforma2.y = 600
    plataforma2.width = 60
    plataforma2.height = 1

    plataforma3 = GameObject()
    plataforma3.x = 665
    plataforma3.y = 462
    plataforma3.width = 800
    plataforma3.height = 1

    # posicaoInicial
    personagem.move_x(200)
    personagem.move_y(220)

    while (True):

        if (vidas == 0):
            return

        if (personagem.y > janela.height):
            personagem.y = 0
            vidas -= 1

        cronometro = cronometroECriacaoTiros(cronometro, tiros, personagem, teclado, ultimaDirecao)

        tempoPulo = pular(personagem, teclado, tempoPulo, plataforma1, plataforma2, plataforma3)

        background1.draw()

        ultimaDirecao = desenharMovimentos(personagem, teclado, ultimaDirecao)

        desenharTiros(tiros, janela)

        for x in range(vidas):
            listaVidas[x].draw()

        janela.draw_text("Vidas", 35, 5, 30, (126, 25, 27), "Calibri", True)

        janela.update()

    Return
