from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from gameplay import *
from conf import *

janela = Window(1351, 901)
mouse1 = Window.get_mouse()

background = GameImage ("images/menu/backgroundMenu.png")

#botões
botaoNewGame = Sprite ("images/menu/botaoNovoJogo.png")
botaoRanking = Sprite ("images/menu/botaoRanking.png")
botaoConf = Sprite ("images/menu/botaoConf.png")
botaoSair = Sprite ("images/menu/botaoSair.png")

botaoNewGameHover = Sprite ("images/menu/botaoNovoJogoHover.png")
botaoRankingHover = Sprite ("images/menu/botaoRankingHover.png")
botaoConfHover = Sprite ("images/menu/botaoConfHover.png")
botaoSairHover = Sprite ("images/menu/botaoSairHover.png")

#configuracaoBotoes
botaoNewGame.x = (janela.width - botaoNewGame.width)/2
#botaoRanking.x = (janela.width - botaoNewGame.width)/2
botaoConf.x = (janela.width - botaoNewGame.width)/2
botaoSair.x = (janela.width - botaoNewGame.width)/2

botaoNewGame.y = ((janela.height - botaoNewGame.height)/2) - 200
#botaoRanking.y = botaoNewGame.y + 150
botaoConf.y = botaoNewGame.y + 150
botaoSair.y = botaoConf.y + 150

botaoNewGameHover.x = (janela.width - botaoNewGameHover.width)/2
#botaoRankingHover.x = (janela.width - botaoNewGameHover.width)/2
botaoConfHover.x = (janela.width - botaoNewGameHover.width)/2
botaoSairHover.x = (janela.width - botaoNewGameHover.width)/2

botaoNewGameHover.y = ((janela.height - botaoNewGameHover.height)/2) - 200
#botaoRankingHover.y = botaoNewGameHover.y + 150
botaoConfHover.y = botaoNewGameHover.y + 150
botaoSairHover.y = botaoConfHover.y + 150

#configuracaoJogo

dificuldade = 1
ganhou = False

while(True):                               

 background.draw()

 if mouse1.is_over_area((botaoNewGame.x, botaoNewGame.y), (botaoNewGame.x + 450, botaoNewGame.y + 100)):
    botaoNewGameHover.draw()
    if mouse1.is_button_pressed(1):
        ganhou = iniciarNovoJogo(dificuldade,janela);
 else:
    botaoNewGame.draw()

 #if mouse1.is_over_area((botaoRanking.x, botaoRanking.y), (botaoRanking.x + 450, botaoRanking.y + 100)):
 #   botaoRankingHover.draw()
 #else:
 #   botaoRanking.draw()

 if mouse1.is_over_area((botaoConf.x, botaoConf.y), (botaoConf.x + 450, botaoConf.y + 100)):
    botaoConfHover.draw()
    if mouse1.is_button_pressed(1):
        dificuldade = configurar(dificuldade,janela,background,mouse1)
 else:
    botaoConf.draw()

 if mouse1.is_over_area((botaoSair.x, botaoSair.y), (botaoSair.x + 450, botaoSair.y + 100)):
    botaoSairHover.draw()
    if mouse1.is_button_pressed(1):
        janela.close()
 else:
    botaoSair.draw()

 janela.draw_text("Hello World of hell", 300,30, 104, (255,211,0), "Roboto", True)
 if ganhou:
     janela.draw_text("Parabéns por finalizar o jogo", 300,100, 70, (255,211,0), "Roboto", True)
 janela.update()