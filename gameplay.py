from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *


def teveColisao(personagem, plataforma1, plataforma2, plataforma3, plataforma4):
    return (personagem.collided(plataforma1) or personagem.collided(plataforma2) or personagem.collided(plataforma3) or personagem.collided(plataforma4))

def desenharMapa(mapa,plataforma1,plataforma2,plataforma3,plataforma4):
    if mapa == 1:
        background = GameImage("images/mapa_1/mapa_1.png")

    elif mapa == 2:
        background = GameImage("images/mapa_1/mapa_2.png")

        plataforma1.width = 1400
        plataforma1.height = 1
        plataforma1.x = 0
        plataforma1.y = 630

        plataforma2.width = 40
        plataforma2.height = 1
        plataforma2.x = 1000
        plataforma2.y = 550

        plataforma3.width = 40
        plataforma3.height = 1
        plataforma3.x = 1100
        plataforma3.y = 470

        plataforma4.width = 100
        plataforma4.height = 1
        plataforma4.x = 1200
        plataforma4.y = 400

    elif mapa == 3:
        background = GameImage("images/mapa_1/mapa_3.png")

        plataforma1.width = 1400
        plataforma1.height = 1
        plataforma1.x = 0
        plataforma1.y = 560

        plataforma2.width = 100
        plataforma2.height = 1
        plataforma2.x = 0
        plataforma2.y = 200

        plataforma3.width = 0
        plataforma3.height = 0
        plataforma3.x = 0
        plataforma3.y = 0

        plataforma4.width = 0
        plataforma4.height = 0
        plataforma4.x = 0
        plataforma4.y = 0


    elif mapa == 4:
        background = GameImage("images/mapa_1/mapa_4.png")

        plataforma1.width = 1400
        plataforma1.height = 1
        plataforma1.x = 0
        plataforma1.y = 755

        plataforma2.width = 100
        plataforma2.height = 1
        plataforma2.x = 0
        plataforma2.y = 440

        plataforma3.width = 0
        plataforma3.height = 0
        plataforma3.x = 0
        plataforma3.y = 0

        plataforma4.width = 0
        plataforma4.height = 0
        plataforma4.x = 0
        plataforma4.y = 0

    else:
        background = GameImage("images/mapa_1/mapa_5.png")

        plataforma1.width = 1400
        plataforma1.height = 1
        plataforma1.x = 0
        plataforma1.y = 820

        plataforma2.width = 40
        plataforma2.height = 1
        plataforma2.x = 400
        plataforma2.y = 670

        plataforma3.width = 100
        plataforma3.height = 1
        plataforma3.x = 550
        plataforma3.y = 530

        plataforma4.width = 40
        plataforma4.height = 1
        plataforma4.x = 800
        plataforma4.y = 660

    return background.draw()

def desenharTutorial(estagio,janela,teclado,mapa):
    if estagio == 4:
        janela.draw_text("Aperte a seta para direita para se movimentar", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("right"):
            return estagio - 1
    elif estagio == 3:
        janela.draw_text("Aperte a seta para esquerda para se movimentar", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("left"):
            return estagio - 1
    elif estagio == 2:
        janela.draw_text("Aperte a seta para cima para pular", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("up"):
            return estagio - 1
    elif estagio == 1:
        janela.draw_text("Aperte a tecla z para atirar", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("z"):
            return estagio - 1
    
    if(mapa == 1):
        janela.draw_text("Derrote todos os inimigos no mapa e avance para a direita ->", 200, 100, 30, (126, 25, 27), "Calibri", True)
    return estagio


def pular(personagem, teclado, tempoPulo, plataforma1, plataforma2, plataforma3, plataforma4):
    if (tempoPulo > 0):
        personagem.y -= 26

    if (teclado.key_pressed("up") and teveColisao(personagem, plataforma1, plataforma2, plataforma3, plataforma4)):
        tempoPulo = 20

    if (not teveColisao(personagem, plataforma1, plataforma2, plataforma3, plataforma4)):
        personagem.y += 15

    tempoPulo -= 1

    return tempoPulo


def desenharMovimentos(personagem, teclado, ultimaDirecao, cronometroIndice, ultimoIndiceCorrida):
    personagemParadoEsquerda = Sprite("images/personagem/personagem_parado_esquerda.png")

    correndoDireita1 = Sprite("images/personagem/correndo_direita_1.png")
    correndoDireita2 = Sprite("images/personagem/correndo_direita_2.png")
    correndoDireita3 = Sprite("images/personagem/correndo_direita_3.png")
    correndoDireita4 = Sprite("images/personagem/correndo_direita_4.png")
    correndoDireita5 = Sprite("images/personagem/correndo_direita_5.png")
    correndoDireita6 = Sprite("images/personagem/correndo_direita_6.png")

    correndoEsquerda1 = Sprite("images/personagem/correndo_esquerda_1.png")
    correndoEsquerda2 = Sprite("images/personagem/correndo_esquerda_2.png")
    correndoEsquerda3 = Sprite("images/personagem/correndo_esquerda_3.png")
    correndoEsquerda4 = Sprite("images/personagem/correndo_esquerda_4.png")
    correndoEsquerda5 = Sprite("images/personagem/correndo_esquerda_5.png")
    correndoEsquerda6 = Sprite("images/personagem/correndo_esquerda_6.png")


    # dicionário com os sprites do personagem parado
    parado = {'right': personagem, 'left': personagemParadoEsquerda}

    # dicionário com os sprites do personagem correndo
    correndo = {'right': [correndoDireita1, correndoDireita2, correndoDireita3, correndoDireita4, correndoDireita5,
                          correndoDireita6],
                'left': [correndoEsquerda1, correndoEsquerda2, correndoEsquerda3, correndoEsquerda4, correndoEsquerda5,
                         correndoEsquerda6]}

    cronometroIndice += 1

    # muda o sprite de corrida a cada 5 gameloops (1 gameloop só a mudança é mt rápida e quase imperceptivel)
    if cronometroIndice == 5:
        ultimoIndiceCorrida += 1
        cronometroIndice = 0

    # ao chegar no último sprite de corrida retorna ao primeiro sprite de corrida da lista
    if ultimoIndiceCorrida == 6:
        ultimoIndiceCorrida = 0

    if (teclado.key_pressed("left")):
        ultimaDirecao = 'left'
        personagem.x -= 8
        move = 1

    elif (teclado.key_pressed("right")):
        ultimaDirecao = 'right'
        personagem.x += 8
        move = 1

    else:
        move = 0

    if move: #checa se alguma das teclas de movimento foram usadas
        correndo[ultimaDirecao][ultimoIndiceCorrida].x = personagem.x
        correndo[ultimaDirecao][ultimoIndiceCorrida].y = personagem.y
        correndo[ultimaDirecao][ultimoIndiceCorrida].draw()

    else:
        parado[ultimaDirecao].x = personagem.x
        parado[ultimaDirecao].y = personagem.y
        parado[ultimaDirecao].draw()

    return ultimaDirecao, cronometroIndice, ultimoIndiceCorrida


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


def cronometroECriacaoTiros(cronometroTiro, tiros, personagem, teclado, ultimaDirecao):

    if (teclado.key_pressed("z") and cronometroTiro > 40):

        bullet = Sprite("images/personagem/bullet.png")
        bullet.y = personagem.y + personagem.height / 2

        if (ultimaDirecao == 'right'):
            bullet.direction = 'right'
            bullet.x = personagem.x + personagem.width
        else:
            bullet.direction = 'left'
            bullet.x = personagem.x

        tiros.append(bullet)
        cronometroTiro = 0

    cronometroTiro += 1

    return cronometroTiro


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

    #ensina o jogador os primeiros comandos do jogo
    estagioTutorial = 4

    vidas = 3

    #carrega o mapa inicial
    mapa = 1

    #inimigos no mapa
    inimigosNoMapa = []

    #Movimentos do personagem e pulo
    tempoPulo = 0

    ultimaDirecao = 'right'

    cronometroIndice = 0

    ultimoIndiceCorrida = 0

    #tiros
    tiros = []
    cronometroTiro = 0

    # Controles
    teclado = Window.get_keyboard()

    # Imagens e Sprites

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

    plataforma4 = GameObject()
    plataforma4.x = 0
    plataforma4.y = 0
    plataforma4.width = 0
    plataforma4.height = 0

    # posicaoInicial
    personagem.move_x(200)
    personagem.move_y(220)

    while (True):

        if (vidas == 0):
            return

        if (personagem.y > janela.height):
            personagem.y = 0
            vidas -= 1

        if (personagem.x < 0):
            personagem.x = 10
        
        # limita o personagem para nao voltar ao mapa anterior e controla a posicao inicial do personagem em cada mapa.
        if personagem.x > janela.width:
            if mapa < 5:
                mapa += 1
                personagem.x = 10
            else:
                personagem.x = janela.width - 100
            if(mapa == 3):
                personagem.y = 100
            elif(mapa == 4):
                personagem.y = 200

        cronometroTiro = cronometroECriacaoTiros(cronometroTiro, tiros, personagem, teclado, ultimaDirecao)

        tempoPulo = pular(personagem, teclado, tempoPulo, plataforma1, plataforma2, plataforma3, plataforma4)

        desenharMapa(mapa,plataforma1,plataforma2,plataforma3,plataforma4)

        #desenha a movimentacao do personagem
        ultimaDirecao, cronometroIndice, ultimoIndiceCorrida = desenharMovimentos(personagem, teclado, ultimaDirecao,cronometroIndice,ultimoIndiceCorrida)

        desenharTiros(tiros, janela)

        for x in range(vidas):
            listaVidas[x].draw()

        janela.draw_text("Vidas", 35, 5, 30, (126, 25, 27), "Calibri", True)

        estagioTutorial = desenharTutorial(estagioTutorial,janela,teclado,mapa) if estagioTutorial > 0 else 0

        janela.update()

    Return