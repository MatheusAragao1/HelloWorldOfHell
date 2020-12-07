from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def configurar(dificuldade,janela,background,mouse1):
    botaoVeryHard = Sprite ("images/menu/veryHard.png")
    botaoHard = Sprite ("images/menu/Hard.png")
    botaoNormal = Sprite ("images/menu/normal.png")

    #configuracaoBotoes
    botaoVeryHard.x = 50
    botaoHard.x = 50
    botaoNormal.x = 50


    botaoVeryHard.y = 200
    botaoHard.y = 400
    botaoNormal.y = 600



    while(True):

        if mouse1.is_over_area((botaoVeryHard.x, botaoVeryHard.y), (botaoVeryHard.x + 450, botaoVeryHard.y + 100)):
           if mouse1.is_button_pressed(1):
               return 3

        if mouse1.is_over_area((botaoHard.x, botaoHard.y), (botaoHard.x + 450, botaoHard.y + 100)):
           if mouse1.is_button_pressed(1):
               return 2

        if mouse1.is_over_area((botaoNormal.x, botaoNormal.y), (botaoNormal.x + 450, botaoNormal.y + 100)):
           if mouse1.is_button_pressed(1):
               return 1

        background.draw()
        janela.draw_text("Configurar", 300,30, 104, (255,211,0), "Roboto", True)
        botaoVeryHard.draw()
        botaoHard.draw()
        botaoNormal.draw()
        janela.update()
    return dificuldade