from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *

def desenhar(personagem,personagemParadoEsquerda,ultimaDirecao,teclado):
    if(ultimaDirecao == 'left'):
        personagemParadoEsquerda.x = personagem.x
        personagemParadoEsquerda.y = personagem.y
        personagemParadoEsquerda.draw()
    else:
        personagem.draw()
    return

def iniciarNovoJogo(dificuldade,janela):

    tempoPulo = 0
    ultimaDirecao = 'right'

    teclado = Window.get_keyboard()

    background1 = GameImage ("images/mapa_1/mapa_1_pt1.png")
    personagem = Sprite ("images/personagem/personagem_parado.png")
    personagemParadoEsquerda = Sprite ("images/personagem/personagem_parado_esquerda.png")

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
        teveColisao = False

        if(tempoPulo > 0):
            personagem.y -= 20

        if(personagem.y > janela.height):
            personagem.y = 0

        if(personagem.collided(plataforma1)):
            teveColisao = True            

        if(personagem.collided(plataforma2)):
            teveColisao = True    
         
        if(personagem.collided(plataforma3)):
            teveColisao = True

        if(teclado.key_pressed("right")):
            personagem.x += 5
            ultimaDirecao = 'right'
        if(teclado.key_pressed("left")):
            personagem.x -= 5
            ultimaDirecao = 'left'
        if(teclado.key_pressed("up") and teveColisao == True):
            tempoPulo = 20

        if(teveColisao == False):
           personagem.y += 10
        
        tempoPulo -= 1;
        background1.draw()
        desenhar(personagem,personagemParadoEsquerda,ultimaDirecao,teclado)
        janela.update()
    return