from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *
from funcoes import *


def iniciarNovoJogo(dificuldade, janela):

    #ensina o jogador os primeiros comandos do jogo
    estagioTutorial = 4

    vidas = 3

    #carrega o mapa inicial
    mapa = 1

    #inimigos no mapa
    inimigosNoMapa = []

    #Movimentos do personagem e voar
    energia = 100

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


        desenharMapa(mapa,plataforma1,plataforma2,plataforma3,plataforma4)

        energia = voar(personagem, teclado, energia, plataforma1, plataforma2, plataforma3, plataforma4)

        #desenha a movimentacao do personagem
        ultimaDirecao, cronometroIndice, ultimoIndiceCorrida = desenharMovimentos(personagem, teclado, ultimaDirecao,cronometroIndice,ultimoIndiceCorrida)

        desenharTiros(tiros, janela)

        for x in range(vidas):
            listaVidas[x].draw()

        janela.draw_text("Vidas", 35, 5, 30, (126, 25, 27), "Calibri", True)

        janela.draw_text("Energia: %d"%(energia), 1100, 10, 30, (126, 25, 27), "Calibri", True)

        estagioTutorial = desenharTutorial(estagioTutorial,janela,teclado,mapa) if estagioTutorial > 0 else 0

        janela.update()

    Return