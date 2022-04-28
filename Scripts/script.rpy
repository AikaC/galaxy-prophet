# The script of the game goes in this file.
image bgblack = "bgblack.png"

#moral system
init python:
 moral = 100

#intel
init python:
 intel = 0

#flags
default extra = False
$fugabr = False
$ancientDragon=False

# choose main character name
$ anna = "",

# The game starts here.

label start:
 
 #hide Last onlayer over_screens
 $pc = False

 $ anna = renpy.input("Meu nome é...")
 $ anna = anna.strip()
 if anna == "":
  $ anna = "Anna"
 
 # Show a background. This uses a placeholder by default, but you can
 # add a file (named either "bg room.png" or "bg room.jpg") to the
 # images directory to show it.

 #scene cutscenefundo
 #show caindo at rodando

 #play sound "audio/61031__davinci79__darkbell.wav"

 # These display lines of dialogue.
    
 "Algumas vezes..."

 "O destino trabalha por meios misteriosos..."

 show arvore brilha with fade
 #hide cutscenefundo
 #hide caindo

 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"
 
 anna "..."

 show Anna at trueright
 with dissolve

 anna "Onde estou? {w} Como cheguei aqui?"
 anna "O que eu sequer estava fazendo antes...?"

 hide Anna
 show Lucy at left
 with moveinleft

 chNull "Quem é essa? Quem é essa?"#Lucy

 hide Lucy
 show Yvvy at right
 with moveinright

 chNull "Claramente alguém de fora!"

 hide Yvvy
 show Lucy at left
 with dissolve

 chNull "Nunca vi uma criatura tão feia na minha vida!"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Como é!?"

 hide Anna
 show Yvvy at right
 with moveinright

 chNull "Eu já! Eu já!" #Yvvy

 hide Yvvy
 show Lucy at left
 with moveinleft

 chNull "Sim, você está certa!"

 show Yvvy at right
 with dissolve

 chNull "{i}O ajudante da rainha má!{/i}"

 show Lucy ClosedEyes_Lucy at left
 show Yvvy ClosedEyes_Yvvy at right

 chNull "hahahaha!"

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with dissolve

 chNull "Shh... Eles podem nos ouvir!" #lucy

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Quem?"

 hide Anna
 show Yvvy AngryEyes_Yvvy at right
 with dissolve

 chNull "A rainha má e o ajudante dela, é claro!" #Yvvy

 show Lucy AngryEyes_Lucy at left
 hide Yvvy
 with moveinleft

 chNull "{i}Essa coisa{/i} não parece inteligente, Yvvy."

 show Yvvy AngryEyes_Yvvy at right
 hide Lucy
 with moveinright

 chY "Nem um pouquinho, Lucy."

 show Lucy AngryEyes_Lucy at left
 hide Yvvy
 with dissolve

 chL "Espera... {w}O que é isso?!" #Lucy

 hide Lucy
 with dissolve

 show Colar at truecenter

 chY "Isso é... {w}da profecia!"

 hide Colar
 show Lucy AngryEyes_Lucy at left
 hide Yvvy
 with moveinleft

 chL "Sem chance! {p}É cedo demais para isso!"

 show Yvvy AngryEyes_Yvvy at right
 hide Lucy
 with moveinright

 chY "Não importa! A rainha má definitivamente {b}não{/b} pode ver isso!"

 show Lucy AngryEyes_Lucy at left
 with dissolve

 chYL "Vamos levar para a vovó!"

 hide Lucy
 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "Espera! Não-"

 play music "audio/YL.ogg" fadeout 1.0

 hide Anna
 hide arvore brilha
 show star
 show BGGrandma
 with fade

 jump to_grandma

 # This ends the game.
 return
