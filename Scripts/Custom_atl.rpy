# cor pensamento : {color=F4C2C2}

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define chNull = Character("???")
define chG = Character("Vovó")#Khaleesi
define chP = Character("Paithyn")
define chI = Character("Ivan")
define chL = Character("Lucy")
define chY = Character("Yvvy")
define chYL = Character ("Yvvy e Lucy")
define chAS = Character("Árvore Sagrada")
define chB = Character("Braxton")
define chGR = Character("Guarda Real")
define chS = Character("Rainha Selyna")
define chR = Character("Rei")

# lista de animações
transform rodando:
 block:
        xalign 0.5 yalign 0.5
        rotate 0 zoom 1
        linear 20.0 rotate 360.0 zoom .2

transform floating:
 block:
        xalign 0.5 yalign 0.5
        linear 1.0 yalign 0.0
        linear 1.0 yalign 0.5
        repeat

#lista de posições
transform trueright:
 xalign 1.1 yalign 1.3

#Lista de cutscenes
image star = Movie(play="00_BG/star_bg.ogv")

#lista de imagens

#BG
image BGGrandma:
 "00_BG/GrandmaHouse.png" with Dissolve(0.5, alpha=True)
 zoom 0.4


image BGExtra = "BG_Extra.png"

image BGPaithynA:
 "00_BG/PaythHouseA.png"
 zoom 0.4
image BGPaithynB:
 "00_BG/PaythHouseB.png" with Dissolve(0.5, alpha=True)
 zoom 0.4

image Last = "creditos.jpg"
image TreeBG = "pandc.png"

image BGctscn01:
 "00_BG/ctscn_Nothing"
 zoom 0.4

#Grandma
image GAngry = "Khalessi/AngryGrandma.png"
image GBody = "Khalessi/Body.png"
image GClosedEyes = "ch_Grandma/CEyesGrandma.png"
image GHappy = "Khalessi/HappyGrandma.png"
#Paithyn
image PBody = "Paithyn900x700.png"
image PHappy = "PaithynHappy.png"

image Colar:
 "00_BG/Pingente.png"
 zoom 3.0

image arvore brilha:
 "00_BG/C01.jpg"
 zoom 0.4

image BG01:
 "cutscenefundo.png"

image caindo:
 "cutscene01.png"

image seirei:
 #Sacred tree
 "Seirei.png"

image textc:
 "textc.png"

image textc2:
 "textc2.png"

#Layered image

#Anna
layeredimage Anna:
 always:
  "Anna/Body.png"

 group eyes:
  attribute AEyes_Open default:
   "Anna/AEyes_Open.png"
  attribute AEyes_Angry:
   "Anna/AEyes_Angry.png"
  attribute AEyes_Empty:
   "ch_Anna/AnnaTranse.png"
  attribute AEyes_Happy:
   "ch_Anna/AEyes_Happy.png"
  attribute AEyes_Tedio:
   "Anna/AEyes_Tedio.png"

 group mouth:
  attribute AMouth_Worried default:
   "Anna/AMouth_Worried.png"
  attribute AOMouth_Happy:
   "ch_Anna/AOMouth_Happy.png"
  attribute ACMouth:
   "Anna/ACMouth.png"

 group acessories:
  attribute none default:
   "None.png"
  attribute rope:
   "ch_Anna/AnnaRope.png"

#Lucy
layeredimage Lucy:
 always:
  "LY/BodyLucy.png"
  xzoom -1

 group LEyes:
  attribute DefaultEyes_Lucy default:
   "LY/DefaultEyes.png"
   xzoom -1
  attribute ClosedEyes_Lucy:
   "LY/EyesClosed.png"
   xzoom -1
  attribute AngryEyes_Lucy:
   "LY/EyesAngry.png"
   xzoom -1

 group LMouth:
  attribute DefaultMouth_Lucy default:
   "LY/DefaultMouth.png"
   xzoom -1
  attribute LaughingLucy:
   "LY/Laughing.png"
   xzoom -1
  attribute ClosedMouth_Lucy:
   "LY/ClosedMouth.png"
   xzoom -1

#Yvvy
layeredimage Yvvy:
 always:
  "LY/BodyYvvy.png"

 group YEyes:
  attribute DefaultEyes_Yvvy default:
   "LY/DefaultEyes.png"
  attribute ClosedEyes_Yvvy:
   "LY/EyesClosed.png"
  attribute AngryEyes_Yvvy:
   "LY/EyesAngry.png"

 group YMouth:
  attribute DefaultMouth_Yvvy default:
   "LY/DefaultMouth.png"
  attribute LaughingYvvy:
   "LY/Laughing.png"
  attribute ClosedMouth_Yvvy:
   "LY/ClosedMouth.png"
