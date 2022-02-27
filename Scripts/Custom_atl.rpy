# Declare characters used by this game. The color argument colorizes the
# name of the character.
define grandma = Character("Grandma", color="#652B46")#Khaleesi
define ivan = Character("Ivan")
define lucy = Character("Lucy", color="#280D08")
define paithyn = Character("Paithyn", color="#23681D")
define sc = Character("Sacred Tree", color = "#CC8105")
define yvvy = Character("Yvvy", color="#312E60")
define yl = Character ("Yvvy and Lucy", color="2F1037")
define a = Character("???", color="#652B46")
define b = Character("???", color="#312E60")
define c = Character("???", color="#2F1037")

# lista de animações
transform rodando:
 block:
        xalign 0.5 yalign 0.5
        rotate 0 zoom 1
        linear 20.0 rotate 360.0 zoom .2

transform colar_foco:
 block:
        zoom 2.0
        xalign 0.5 yalign 0.5
        linear 1.0 yalign 0.5

transform floating:
 block:
        xalign 0.5 yalign 0.5
        linear 1.0 yalign 0.0
        linear 1.0 yalign 0.5
        repeat

#lista de imagens
#Anna
image ABody = "ch_Anna/AnnaBody500x650.png"
image ARope = "ch_Anna/AnnaRope.png"
image ATedio = "ch_Anna/AnnaTedio.png"
image AWorried = "ch_Anna/AnnaWorried.png"
image Colar = "ch_Anna/AnnaBody2.png"

#BG
image BGGrandma = "GrandmaHouse.jpg"
image BGExtra = "BG_Extra.png"
image BGPaithyn = "PaythHouse.jpg"
image Last = "creditos.jpg"
image MENU = "choice_menu.png"
image TreeBG = "pandc.png"
#Grandma
image GAngry = "ch_Grandma/AngryGrandma.png"
image GBody = "ch_Grandma/GrandmaBody.png"
image GClosedEyes = "ch_Grandma/CEyesGrandma.png"
image GHappy = "ch_Grandma/HappyGrandma.png"
#Paithyn
image PBody = "Paithyn900x700.png"
image PHappy = "PaithynHappy.png"
#Twins
image LA = "ch_Twins/AngryLucy.png"
image YA = "ch_Twins/AngryYvvy.png"
image LD = "ch_Twins/DefaultLucy.png"
image YD = "ch_Twins/DefaultYvvy.png"
image LL = "ch_Twins/LaughingLucy.png"

image arvore brilha:
 "C01.jpg"

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
  "ch_Anna/AnnaBody500x650.png"

 group eyes:
  attribute AEyes_Worried default:
   "ch_Anna/AEyes_Worried.png"
  attribute AEyes_Angry:
   "ch_Anna/AEyes_Angry.png"
  attribute AEyes_Empty:
   "ch_Anna/AnnaTranse.png"
  attribute AEyes_Happy:
   "ch_Anna/AEyes_Happy.png"
  attribute AEyes_Tedio:
   "ch_Anna/AEyes_Tedio.png"

 group mouth:
  attribute ACMouth_Worried default:
   "ch_Anna/ACMouth_Worried.png"
  attribute AOMouth_Worried:
   "ch_Anna/AOMouth_Worried.png"
  attribute ACMouth_Happy:
   "ch_Anna/ACMouth_Happy.png"
  attribute AOMouth_Happy:
   "ch_Anna/AOMouth_Happy.png"
  attribute AOMouth_Angry:
   "ch_Anna/AOMouth_Angry.png"

 group acessories:
  attribute none default:
   "ch_Anna/None.png"
  attribute rope:
   "ch_Anna/AnnaRope.png"

#Twins
layeredimage Twins:
 always:
  "ch_Twins/TwinsBody.png"

 group YEyes:
  attribute DefaultEyes_Yvvy default:
   "ch_Twins/DefaultEyes.png"
  attribute AngryEyes_Yvvy:
   "ch_Twins/AngryEyes.png"
  attribute ClosedHappyEyes_Yvvy:
   "ch_Twins/ClosedHappyEyes.png"

 group YMouth:
  attribute DefaultYvvy default:
   "ch_Twins/DefaultMouth.png"
  attribute LaughingYvvy:
   "ch_Twins/Laughing.png"
  attribute ClosedMouth_Yvvy:
   "ch_Twins/ClosedMouth.png"

 group LEyes:
  attribute DefaultEyes_Lucy default:
   "ch_Twins/DefaultEyes.png"
   xzoom -1
  attribute ClosedHappyEyes_Lucy:
   "ch_Twins/ClosedHappyEyes.png"
   xzoom -1
  attribute AngryEyes_Lucy:
   "ch_Twins/AngryEyes.png"
   xzoom -1

 group LMouth:
  attribute DefaultLucy default:
   "ch_Twins/DefaultMouth.png"
   xzoom -1
  attribute LaughingLucy:
   "ch_Twins/Laughing.png"
   xzoom -1
  attribute ClosedMouth_Lucy:
   "ch_Twins/ClosedMouth.png"
   xzoom -1
