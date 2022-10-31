##Lista de imagens######################################################

##Assets
image caindo = "Anna/cutscene01.png"
image CalCima =  "00_BG/caldeirão cima.png"
image CalBaixo =  "00_BG/caldeirão baixo.png"
image Colar = "00_BG/Pingente.png"
image ingrediente = "00_BG/ingrediente.png"
image locker_idle = "gui/button/locker_idle.png"
image locker_hover = "gui/button/locker_hover.png"
image nut_idle = "gui/button/nut_idle.png"
image nut_hover = "gui/button/nut_hover.png"
image Power = "00_BG/Anna power.png"

#Lista de cutscenes
image star = Movie(play="00_BG/star_bg.ogv")
image BGPaithyn = Movie(play="00_BG/BGpaithyn_house.ogv")

#Imagens capítulos
image CH01 = "00_BG/CH01.jpg"

##BG
image BGGrandma:
 "00_BG/GrandmaHouse.png" with Dissolve(0.5, alpha=True)
 zoom 0.4

image Last = "creditos.jpg"
image BGBraxton = "00_BG/salem.jpg"
image BGExtra = "00_BG/BGExtra.jpg"
image TreeBG = "00_BG/gameTree.jpg"
image BGCastle = "00_BG/Castle.jpg"
image BGIvan = "00_BG/BGIvan.jpg"
image Castle01 = "00_BG/castleCtscn.jpg"
image Masmorra = "00_BG/tunel.jpg"
image Silhueta = "00_BG/Silhueta.jpg"
image Silhueta2 = "00_BG/yl_castle.png"
image Silhueta3 = "00_BG/castleCtscn2.png"

image BGctscn01:
 "00_BG/ctscn_Nothing.jpg"
 zoom 0.4

image BGctscn02:
 "00_BG/ctscn_Nothing2.png"
 zoom 0.4

image TreeCtscn:
 "00_BG/BGtree.png"
 xalign 0.45 yalign 0.55
 zoom 0.2

image Templectscn:
 "00_BG/temple01.png"
 xalign 0.56 yalign 0.6
 zoom 0.6

#Guarda Real
image GR = "Queen/Guarda Real.png"
#Grandma
image GAngry = "Khalessi/AngryGrandma.png"
image GBody = "Khalessi/Body.png"
image GClosedEyes = "ch_Grandma/CEyesGrandma.png"
image GHappy = "Khalessi/HappyGrandma.png"
#Paithyn
image PBody = "Paithyn/Body_Paithyn.png"
image PHappy = "Paithyn/FaceHappy_Paithyn.png"
image PMove = "Paithyn/Move_Paithyn.png"
#Árvore Sagrada
image seirei = "Seirei/Seirei.png"
image ASbody = "Seirei/SeireiBody.png"
image AS_OMouth = "Seirei/SeireiOMouth.png"

image arvore brilha:
 "00_BG/C01.jpg"
 zoom 0.4

image BG01:
 "cutscenefundo.png"

##Layered images

#Anna
layeredimage Anna:
 always:
  "Anna/Body.png"

 group face:
  attribute AWorryFace default:
   "Anna/ADefault.png"
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
   "Anna/AnnaRope.png"
  attribute Amascara:
   "Anna/mascara.png"

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

 group Lacessories:
  attribute none default:
   "None.png"
   xzoom -1
  attribute Lmascara:
   "LY/Mascara.png"
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

 group Yacessories:
  attribute none default:
   "None.png"
  attribute Ymascara:
   "LY/Mascara.png"

#Ivan
layeredimage Ivan:
 always:
  "Ivan/IvanBody.png"

 group BFace:
   attribute DefaultFace_Van default:
    "Ivan/IvanFaceDefault.png"

#Braxton
layeredimage Braxton:
 always:
  "Braxton/BraxtonBody.png"

 group BFace:
   attribute DefaultFace_Brax default:
    "Braxton/BraxtonFaceDefault.png"

#Queen
layeredimage Queen:
 always:
  "Queen/SelynnaBody.png"

 group BFace:
   attribute DefaultFace_Brax default:
    "Queen/SelynnaDMouth.png"
