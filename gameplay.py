from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *

def desenhar(personagem, teclado, ultimaDirecao):

    personagemParadoEsquerda = Sprite("images/personagem/personagem_parado_esquerda.png")

    direcoes = {'right': personagem, 'left': personagemParadoEsquerda}

    if (teclado.key_pressed("left")):
        personagem.x -= 4
        direcoes['left'].x = personagem.x
        direcoes['left'].y = personagem.y
        return [direcoes['left'].draw(),'left']


    if (teclado.key_pressed("right")):
        personagem.x += 4
        direcoes['right'].x = personagem.x
        direcoes['right'].y = personagem.y
        return [direcoes['right'].draw(),'right']


    if ultimaDirecao == 'right':    
       direcoes['right'].x = personagem.x
       direcoes['right'].y = personagem.y
       return [direcoes['right'].draw(),'right']
    else:
       direcoes['left'].x = personagem.x
       direcoes['left'].y = personagem.y
       return [direcoes['left'].draw(),'left']

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
            personagem.y -= 20

        if(teclado.key_pressed("z") and cronometro > 40):
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
                tiro.x += 15
            else:
                tiro.x -= 15
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
            personagem.y += 10
        
        cronometro += 1
        tempoPulo -= 1

        background1.draw()

        desenhar(personagem,teclado,ultimaDirecao)[0]
        ultimaDirecao = desenhar(personagem,teclado,ultimaDirecao)[1]

        # nao sei se um loop seria mais eficiente do que os ifs mas achei interessante como alternativa
        for x in range(vidas):
            listaVidas[x].draw()

        for tiro in tiros:
            tiro.draw()

        janela.draw_text("Vidas", 35,5, 30, (126,25,27), "Calibri", True)
        janela.update()
    return None