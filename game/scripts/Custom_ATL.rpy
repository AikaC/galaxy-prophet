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

transform giragira:
 block:
        xalign 0.5 yalign 0.5
        rotate 0 zoom 1.1
        linear 20.0 rotate 360.0
        repeat

transform floating:
 block:
        xalign 0.5 yalign 0.5
        linear 2 yalign 0.0
        linear 2 yalign 0.5
        repeat

# lista de transições
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

transform zoom:
 block:
        xalign 0.5 yalign 0.5
        rotate 0 zoom 1
        linear 5.0 zoom 1.2

transform move:
 block:
        xalign 0.8 yalign 0.5
        rotate 0 zoom 1.4
        linear 3.0 xalign 0.5

transform desaparece:
 block:
        rotate 0 zoom 1.2
        linear 10.0 alpha 0

#lista de posições
transform trueright:
 xalign 1.1 yalign 1.3