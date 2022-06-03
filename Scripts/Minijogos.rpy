#Os minijogos ficam aqui

## Point and click screen ################################################################
##  Jogo da árvore
## This screen creates a button for the point and click game
screen bar_nav:
   add "TreeBG"
   $pc = True
   modal True

   hbox:
     spacing 6
     xalign 0.0 yalign 0.05

     text _("Alguma dessas flores deve ser a chave...")
  
   imagebutton auto "locker_%s":
     focus_mask True
     xpos 0.35
     ypos 0.3
     hovered SetVariable("screen_tooltip", "???")
     unhovered SetVariable("screen_tooltip", "")
   
     if sc04 == True:
       action Jump("talk_tree")
   
     if sc05 == True:
       action Jump("did_it")

##  Jogo dos ingredientes
screen colheita:
   add "BGExtra"
   modal True

   hbox:
     spacing 6
     xalign 0.0 yalign 0.05

     text _("O ingrediente deve estar por aqui")
  
   imagebutton auto "nut_%s":
     focus_mask True
     xpos 0.8
     ypos 0.1
     hovered SetVariable("screen_tooltip", "???")
     unhovered SetVariable("screen_tooltip", "")
     
     action Jump("minion")     

## Message screen ################################################################
##  Notificações
## Essas janelas notificam o jogador de alguma consequência

##Notificação capítulos

#Capítulo 01 
screen noframe_ch01:
  modal True

  hbox:
    spacing 50
    xalign 0.35 yalign 0.5

    text _("{color=b2c1d6}{size=+30}{font=KAMIKZOM.ttf}Capítulo 01")

##  Notificação achievements
screen noframe_dragonRoute:
  hbox:
    spacing 6
    xalign 0.0 yalign 0.05

    text _("Rota \"Dragão Ancião\" desbloqueada")

# Rota Secreta
screen noframe_special:
  hbox:
    spacing 6
    xalign 0.0 yalign 0.05

    text _("Rota Secreta desbloqueada")

screen getKey:
  hbox:
    spacing 6
    xalign 0.0 yalign 0.05

    text _("Chave adquirida")

##  Notificação Jogador inicia uma rota específica

#Rota Dragão Ancião
screen noframe_RouteWarning:
  hbox:
    spacing 6
    xalign 0.0 yalign 0.05

    text _("Rota \"Dragão Ancião\"")

# Rota Secreta
screen noframe_secret:
  hbox:
    spacing 6
    xalign 0.0 yalign 0.05

    text _("Rota Secreta")

##  Barra de Moral
screen noframe_moral:
 text _("Moral")

 bar:
   value moral
   range 100
   left_bar "gui/bar/MoralB.png"
   right_bar "gui/bar/MoralF.png"
   xysize(200,25)
   xalign 0.05

##  Resposta caminho do rei
screen king_frame:
    frame:
        xalign 0.5 ypos 50
        vbox:
            text _("Esquerda, Direita, Direita, Esquerda")
            textbutton _("Entendi"):
                action Return(True)
 
 