# The script of the game goes in this file.

image bgblack = "bgblack.png"

#moral system
init python:
 moral = 100

#flags
default extra = False

# choose main character name
$ anna = "", #F076B5

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define grandma = Character("Grandma", color="#652B46")
define lucy = Character("Lucy", color="#280D08")
define paithyn = Character("Paithyn", color="#23681D")
define sc = Character("Sacred Tree", color = "#CC8105")
define yvvy = Character("Yvvy", color="#312E60")
define yl = Character ("Yvvy and Lucy", color="2F1037")
define a = Character("???", color="#652B46")
define b = Character("???", color="#312E60")
define c = Character("???", color="#2F1037")


# The game starts here.

label start:
 
 hide Last onlayer over_screens

 $ anna = renpy.input("Please, type your name.")
 $ anna = anna.strip()
 if anna == "":
  $ anna = "Anna"

 stop music

 # Show a background. This uses a placeholder by default, but you can
 # add a file (named either "bg room.png" or "bg room.jpg") to the
 # images directory to show it.

 scene cutscenefundo

 # This shows a character sprite. A placeholder is used, but you can

 show caindo at rodando

 play sound "audio/61031__davinci79__darkbell.wav"

 # These display lines of dialogue.
    
 "Sometimes…"

 "Destiny works in mysterious ways…"

 show arvore brilha with fade
 hide cutscenefundo
 hide caindo

 play music "audio/AnnaArp.ogg"
 anna "..."

 show ABody
 show AWorried
 with dissolve

 anna "Where am I? {w} How did I get here?"
 anna "What was I doing before...?"

 play music "audio/YL.ogg" fadeout 1.0

 hide ABody
 hide AWorried
 show Twins Body
 show LD
 show YD
 with moveinright

 a "Who is that? Who is that?"
 b "Clearly not someone from here!"
 a "I’ve never seen such an ugly creature in my life!"

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show AAngry
 with dissolve

 anna "Excuse me!?"

 hide ABody
 hide AAngry
 show Twins Body
 show LD
 show YD
 with dissolve

 b "I have seen! I have seen!"
 a "Yes, you’re right!"

 hide LD
 hide YD
 show LL
 show YL
 with dissolve

 c "{i}The evil queen’s right hand!{/i}"
 b "hahahaha!"

 hide LL
 show LD
 with dissolve

 a "Shh... They might hear us!"

 hide Twins Body
 hide YL
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "Who?"

 hide ABody
 hide AWorried
 show Twins Body
 show LD
 show YD
 with dissolve

 b "The evil queen and her menial, of course!"
 a "{i}This thing{/i} doesn’t look smart, Yvvy."
 yvvy "Not even a tiny bit, Lucy."

 hide LD
 show LA
 with dissolve

 lucy "Wait... {w}What is that?!"

 hide Twins Body
 hide YD
 hide LA

 window hide
 show Colar at colar_foco onlayer over_screens
 pause

 hide Colar onlayer over_screens
 window show

 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "That’s… from the prophecy!"
 lucy "No way! {w}Is too early for that!"
 yvvy "It doesn’t matter! The evil queen must definitely {b}not{/b} see this!"
 yl "Let’s take it to grandma!"

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show AWorried
 with dissolve

 anna "Wait! No-"

 hide ABody
 hide AWorried
 hide arvore brilha
 show BGGrandma
 with fade

 jump to_grandma

 # This ends the game.

 return
