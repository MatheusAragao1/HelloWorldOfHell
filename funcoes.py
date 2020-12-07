from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.gameobject import *
from PPlay.window import *

def teveColisao(personagem, plataforma1, plataforma2, plataforma3, plataforma4):
    return (personagem.collided(plataforma1) or personagem.collided(plataforma2) or personagem.collided(plataforma3) or personagem.collided(plataforma4))

def gerarInimigos(inimigosNoMapa,mapa):
    totem = Sprite("images/inimigos/Totem.png")
    esqueleto = Sprite("images/inimigos/esqueleto_direita.png")
    esqueleto2 = Sprite("images/inimigos/esqueleto_esquerda.png")
    minotauro = Sprite("images/inimigos/minotauro_direita.png")
    minotauro2 = Sprite("images/inimigos/minotauro_esquerda.png")
    mago = Sprite("images/inimigos/boss_direita.png")

    if(mapa == 1):
        return
    elif(mapa == 2):
        esqueleto.x = 1000
        esqueleto.y = 520
        esqueleto.life = 3
        esqueleto.tipo = 'esqueleto'
        esqueleto.estado = 'normal'
        esqueleto.direcao = 'right'
        inimigosNoMapa.append(esqueleto)

        esqueleto2.x = 800
        esqueleto2.y = 520
        esqueleto2.life = 3
        esqueleto2.tipo = 'esqueleto'
        esqueleto2.estado = 'normal'
        esqueleto2.direcao = 'left'
        inimigosNoMapa.append(esqueleto2)
    elif(mapa == 3):
        esqueleto.x = 1000
        esqueleto.y = 450
        esqueleto.life = 3
        esqueleto.tipo = 'esqueleto'
        esqueleto.estado = 'normal'
        esqueleto.direcao = 'right'
        inimigosNoMapa.append(esqueleto)

        esqueleto2.x = 800
        esqueleto2.y = 450
        esqueleto2.life = 3
        esqueleto2.tipo = 'esqueleto'
        esqueleto2.estado = 'normal'
        esqueleto2.direcao = 'left'
        inimigosNoMapa.append(esqueleto2)

        minotauro.x = 500
        minotauro.y = 450
        minotauro.life = 4
        minotauro.tipo = 'minotauro'
        minotauro.estado = 'normal'
        minotauro.direcao = 'right'
        inimigosNoMapa.append(minotauro)
        return
    elif(mapa == 4):
        totem.x = 1150
        totem.y = 10
        totem.life = 2
        totem.tipo = 'totem'
        totem.estado = 'normal'
        totem.direcao = 'right'
        inimigosNoMapa.append(totem)

        minotauro.x = 500
        minotauro.y = 650
        minotauro.life = 4
        minotauro.tipo = 'minotauro'
        minotauro.estado = 'normal'
        minotauro.direcao = 'right'
        inimigosNoMapa.append(minotauro)

        minotauro2.x = 100
        minotauro2.y = 650
        minotauro2.life = 4
        minotauro2.tipo = 'minotauro'
        minotauro2.estado = 'normal'
        minotauro2.direcao = 'left'
        inimigosNoMapa.append(minotauro2)

    elif(mapa == 5):
        totem.x = -100
        totem.y = -100
        totem.life = 1
        totem.tipo = 'totem'
        totem.estado = 'normal'
        totem.direcao = 'right'
        inimigosNoMapa.append(totem)

        mago.x = 1000
        mago.y = 100
        mago.life = 10
        mago.tipo = 'mago'
        mago.estado = 'normal'
        mago.direcao = 'left'
        inimigosNoMapa.append(mago)       


    return None

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
        janela.draw_text("Aperte a seta para cima para voar", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("up"):
            return estagio - 1
    elif estagio == 1:
        janela.draw_text("Aperte a tecla z para atirar", 200, 50, 50, (126, 25, 27), "Calibri", True)
        if teclado.key_pressed("z"):
            return estagio - 1
    
    if(mapa == 1):
        janela.draw_text("Derrote todos os inimigos no mapa e avance para a direita ->", 200, 100, 30, (126, 25, 27), "Calibri", True)
    return estagio

def voar(personagem, teclado, energia,ultimaDirecao, plataforma1, plataforma2, plataforma3, plataforma4):

    fogo_voar = {"esquerda": Sprite ("images/personagem/fogo_voar_esquerda.png") , "direita": Sprite ("images/personagem/fogo_voar_direita.png")}

    if (teclado.key_pressed("up") and energia >= 2):
            personagem.y -= 26
            energia -= 2
            if(ultimaDirecao == 'right'):
                fogo_voar['direita'].x = personagem.x + 6
                fogo_voar['direita'].y = personagem.y + 88
                fogo_voar['direita'].draw()
            else:
                fogo_voar['esquerda'].x = personagem.x + 70
                fogo_voar['esquerda'].y = personagem.y + 88
                fogo_voar['esquerda'].draw()

    elif(energia < 100):
        energia += 1

    if (not teveColisao(personagem, plataforma1, plataforma2, plataforma3, plataforma4)):
        personagem.y += 15

    return energia



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


    # dicion�rio com os sprites do personagem parado
    parado = {'right': personagem, 'left': personagemParadoEsquerda}

    # dicion�rio com os sprites do personagem correndo
    correndo = {'right': [correndoDireita1, correndoDireita2, correndoDireita3, correndoDireita4, correndoDireita5,
                          correndoDireita6],
                'left': [correndoEsquerda1, correndoEsquerda2, correndoEsquerda3, correndoEsquerda4, correndoEsquerda5,
                         correndoEsquerda6]}

    cronometroIndice += 1

    # muda o sprite de corrida a cada 5 gameloops (1 gameloop so a mudanca e mt rapida e quase imperceptivel)
    if cronometroIndice == 5:
        ultimoIndiceCorrida += 1
        cronometroIndice = 0

    # ao chegar no ultimo sprite de corrida retorna ao primeiro sprite de corrida da lista
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

    if dificuldade == 3:
        return [vida1]

    elif dificuldade == 2:
        return [vida1, vida2]

    else:
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
            tiro.x += 20            
        else:
            tiro.x -= 20            

        if (tiro.x > janela.width):
            tiros.remove(tiro)
        elif (tiro.x < 0):
            tiros.remove(tiro)

    for tiro in tiros:
        tiro.draw()

def desenharDanificado(inimigo):
    totemDanificado = Sprite("images/inimigos/totem_dano.png")
    esqueletoDanificado = Sprite("images/inimigos/esqueleto_dano.png")
    minotauroDanificado = Sprite("images/inimigos/minotauro_dano.png")
    if(inimigo.tipo == 'totem'):
        totemDanificado.x = inimigo.x
        totemDanificado.y = inimigo.y
        totemDanificado.draw()
    if(inimigo.tipo == 'esqueleto'):
        esqueletoDanificado.x = inimigo.x
        esqueletoDanificado.y = inimigo.y
        esqueletoDanificado.draw()
    if(inimigo.tipo == 'minotauro'):
        minotauroDanificado.x = inimigo.x
        minotauroDanificado.y = inimigo.y
        minotauroDanificado.draw()

def invocarInimigos(inimigosNoMapa):
    esqueleto = Sprite("images/inimigos/esqueleto_direita.png")
    minotauro = Sprite("images/inimigos/minotauro_direita.png")

    esqueleto.x = 1000
    esqueleto.y = 720
    esqueleto.life = 3
    esqueleto.tipo = 'esqueleto'
    esqueleto.estado = 'normal'
    esqueleto.direcao = 'right'
    inimigosNoMapa.append(esqueleto)

    minotauro.x = 1000
    minotauro.y = 720
    minotauro.life = 4
    minotauro.tipo = 'minotauro'
    minotauro.estado = 'normal'
    minotauro.direcao = 'left'
    inimigosNoMapa.append(minotauro)


    return None

def desenharInimigos(inimigosNoMapa,tiros,janela):
    colidiu = False
    for tiro in tiros:
        for inimigo in inimigosNoMapa:
            if tiro.collided(inimigo):
                    colidiu = True
                    inimigo.estado = 'danificado'
                    inimigo.life -= 1
                    desenharDanificado(inimigo)
                    if(inimigo.tipo == 'mago' and len(inimigosNoMapa) < 8):
                        invocarInimigos(inimigosNoMapa)
                    if(inimigo.life == 0 and inimigo.tipo == 'mago'):
                        return True
                    if(inimigo.life == 0):
                        inimigosNoMapa.remove(inimigo)
        if colidiu == True:
            tiros.remove(tiro)
            colidiu = False
    for inimigo in inimigosNoMapa:
        if inimigo.estado != 'normal':
            inimigo.estado = 'normal'
        else:
            if(inimigo.tipo == 'totem'):
                inimigo.draw()
            elif(inimigo.tipo == 'esqueleto'):
                if inimigo.direcao == 'right':
                    temp = Sprite("images/inimigos/esqueleto_direita.png")
                    inimigo.x += 7
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()
                elif inimigo.direcao == 'left':
                    temp = Sprite("images/inimigos/esqueleto_esquerda.png")
                    inimigo.x -= 7
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()

                if inimigo.x > 1300:
                    inimigo.direcao = 'left'
                elif inimigo.x < 10:
                    inimigo.direcao = 'right'
            elif(inimigo.tipo == 'minotauro'):
               if inimigo.direcao == 'right':
                    temp = Sprite("images/inimigos/minotauro_direita.png")
                    inimigo.x += 10
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()
               elif inimigo.direcao == 'left':
                    temp = Sprite("images/inimigos/minotauro_esquerda.png")
                    inimigo.x -= 10
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()

               if inimigo.x > 1300:
                    inimigo.direcao = 'left'
               elif inimigo.x < 10:
                    inimigo.direcao = 'right'
            elif(inimigo.tipo == 'mago'):
               janela.draw_text("Vidas do Mago: %d"%(inimigo.life), 500,80, 35, (255,211,0), "Roboto", True)
               if inimigo.direcao == 'right':
                    temp = Sprite("images/inimigos/boss_direita.png")
                    inimigo.x += 10
                    inimigo.y += 10
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()
               elif inimigo.direcao == 'left':
                    temp = Sprite("images/inimigos/boss_esquerda.png")
                    inimigo.x -= 10
                    inimigo.y += 10
                    temp.x = inimigo.x
                    temp.y = inimigo.y
                    temp.draw()

               if inimigo.x > 1300:
                    inimigo.direcao = 'left'
               elif inimigo.x < 10:
                    inimigo.direcao = 'right'
               

               if inimigo.y > 950:
                   inimigo.y = -100
                               
              


def efeitoTotem(inimigosNoMapa,ultimoMeteoro,listaMeteoros,personagem):
    meteoro = Sprite ("images/inimigos/pedra.png")
    meteoro.x = personagem.x
    meteoro.y = 0
    for inimigo in inimigosNoMapa:
        if inimigo.tipo == 'totem':
            if ultimoMeteoro > 150:
                listaMeteoros.append(meteoro)
                return 0
    return ultimoMeteoro + 1

def desenharMeteorosEinimigos(personagem,listaMeteoros,vidas,inimigosNoMapa):
    for meteoro in listaMeteoros:
        meteoro.y += 10
        if(meteoro.collided(personagem)):
           vidas -= 1
           listaMeteoros.remove(meteoro)
        else:
            meteoro.draw()
    for inimigo in inimigosNoMapa:
        if personagem.collided(inimigo):
            vidas -= 1
            personagem.y = 0
    return vidas