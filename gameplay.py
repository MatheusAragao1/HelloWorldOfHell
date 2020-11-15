from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *

def desenhar(personagem, teclado, ultimaDirecao,ultimoIndiceCorrida,cronometroIndice):

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

    #dicionário com os sprites do personagem parado
    parado = {'right': personagem, 'left': personagemParadoEsquerda}

    #dicionário com os sprites do personagem correndo
    correndo = {'right': [correndoDireita1,correndoDireita2,correndoDireita3,correndoDireita4,correndoDireita5,correndoDireita6],'left': [correndoEsquerda1,correndoEsquerda2,correndoEsquerda3,correndoEsquerda4,correndoEsquerda5,correndoEsquerda6]}

    #muda o sprite de corrida a cada 5 gameloops (1 gameloop só a mudança é mt rápida e quase imperceptivel)
    if cronometroIndice == 5:
        ultimoIndiceCorrida += 1
        cronometroIndice = 0

    #ao chegar no último sprite de corrida retorna ao primeiro sprite de corrida da lista
    if ultimoIndiceCorrida == 6:
        ultimoIndiceCorrida = 0


    if (teclado.key_pressed("left")):
        personagem.x -= 6
        correndo['left'][ultimoIndiceCorrida].x = personagem.x
        correndo['left'][ultimoIndiceCorrida].y = personagem.y
        return [correndo['left'][ultimoIndiceCorrida].draw(),'left',ultimoIndiceCorrida,cronometroIndice]


    if (teclado.key_pressed("right")):
        personagem.x += 6
        correndo['right'][ultimoIndiceCorrida].x = personagem.x
        correndo['right'][ultimoIndiceCorrida].y = personagem.y
        return [correndo['right'][ultimoIndiceCorrida].draw(),'right',ultimoIndiceCorrida,cronometroIndice]


    #reseta o desenho caso o personagem esteja parado
    if ultimaDirecao == 'right':
       controlarPosicao = 0 
       parado['right'].x = personagem.x
       parado['right'].y = personagem.y
       return [parado['right'].draw(),'right',ultimoIndiceCorrida,cronometroIndice]
    else:
       controlarPosicao = 0
       parado['left'].x = personagem.x
       parado['left'].y = personagem.y
       return [parado['left'].draw(),'left',ultimoIndiceCorrida,cronometroIndice]

def configurar_vidas():
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

def teveColisao(personagem, plataforma1, plataforma2, plataforma3):
    return (personagem.collided(plataforma1) or personagem.collided(plataforma2) or personagem.collided(plataforma3))

def iniciarNovoJogo(dificuldade,janela):

    vidas = 3
    tempoPulo = 0
    ultimaDirecao = 'right'
    tiros = []
    cronometro = 0
    cronometroIndice = 0
    ultimoIndiceCorrida = 0

    teclado = Window.get_keyboard()

    # Imagens e Sprites
    background1 = GameImage ("images/mapa_1/mapa_1_pt1.png")

    personagem = Sprite ("images/personagem/personagem_parado.png")

     # Uma coisa que pensei usando uma funcao foi poder ajustar a quantidade de vidas com a dificuldade
    listaVidas = configurar_vidas()

    #gameObjects mapa_1_pt1
    plataforma1 = GameObject ()
    plataforma1.x = 215
    plataforma1.y = 310
    plataforma1.width = 200
    plataforma1.height = 1

    plataforma2 = GameObject ()
    plataforma2.x = 480
    plataforma2.y = 600
    plataforma2.width = 60
    plataforma2.height = 1

    plataforma3 = GameObject ()
    plataforma3.x = 665
    plataforma3.y = 462
    plataforma3.width = 800
    plataforma3.height = 1

   #posicaoInicial
    personagem.move_x(200)
    personagem.move_y(220)

    while(True):      

        if(vidas == 0):
            return

        if(tempoPulo > 0):
            personagem.y -= 25

        if(teclado.key_pressed("z") and cronometro > 30):
            bullet = Sprite ("images/personagem/bullet.png")
            bullet.y = personagem.y + personagem.height/2
            if(ultimaDirecao == 'right'):
                bullet.direction = 'right'
                bullet.x = personagem.x + personagem.width
            else:
                bullet.direction = 'left'
                bullet.x = personagem.x
            tiros.append(bullet)
            cronometro = 0

        for tiro in tiros:
            if(tiro.direction == 'right'):
                tiro.x += 25
            else:
                tiro.x -= 25
            if(tiro.x > janela.width):
                tiros.remove(tiro)
            elif(tiro.x < 0):
                tiros.remove(tiro)

        if(personagem.y > janela.height):
            personagem.y = 0
            vidas -= 1

        if (teclado.key_pressed("up") and teveColisao(personagem, plataforma1, plataforma2, plataforma3)):
            tempoPulo = 20

        if (not teveColisao(personagem, plataforma1, plataforma2, plataforma3)):
            personagem.y += 15
        
        #cronometro para contar a frequencia possível de tiro
        cronometro += 1
        #cronometro para contar a frequencia possível de mudança de sprite de corrida
        cronometroIndice += 1

        tempoPulo -= 1

        background1.draw()

        #desenha o personagem
        #recebe a última direção do personagem desenhado
        #recebe o indice do último sprite de corrida desenhado
        #recebe o valor do cronometro 0 caso ele seja zerado pelo controlador de sprites
        desenho,ultimaDirecao,ultimoIndiceCorrida,cronometroIndice = desenhar(personagem,teclado,ultimaDirecao,ultimoIndiceCorrida,cronometroIndice)

        for x in range(vidas):
            listaVidas[x].draw()

        for tiro in tiros:
            tiro.draw()

        janela.draw_text("Vidas", 35,5, 30, (126,25,27), "Calibri", True)
        janela.update()
    return None