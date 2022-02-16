# The script of the game goes in this file.
image bgblack = "bgblack.png"

#moral system
init python:
 moral = 100

#flags
default extra = False

# choose main character name
$ anna = "", #F076B5



# The game starts here.

label start:
 
 hide Last onlayer over_screens
 pc = False

 $ anna = renpy.input("Please, type your name.")
 $ anna = anna.strip()
 if anna == "":
  $ anna = "Anna"

 stop music
 
 # Show a background. This uses a placeholder by default, but you can
 # add a file (named either "bg room.png" or "bg room.jpg") to the
 # images directory to show it.

 scene cutscenefundo
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
 anna "What was I even doing before...?"

 play music "audio/YL.ogg" fadeout 1.0

 hide ABody
 hide AWorried
 show Twins
 with moveinright

 a "Who is that? Who is that?"
 b "Clearly not someone from here!"
 a "I’ve never seen such an ugly creature in my life!"

 show Twins ClosedMouth_Yvvy ClosedMouth_Lucy
 show Anna AEyes_Angry AOMouth_Angry onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Excuse me!?"

 show Anna AEyes_Angry ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultYvvy DefaultLucy with dissolve

 b "I have seen! I have seen!"
 a "Yes, you’re right!"

 show Twins LaughingLucy ClosedHappyEyes_Lucy LaughingYvvy ClosedHappyEyes_Yvvy
 with dissolve

 c "{i}The evil queen’s right hand!{/i}"
 b "hahahaha!"

 show Twins AngryEyes_Lucy DefaultLucy
 with dissolve

 a "Shh... They might hear us!"

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left

 anna "Who?"

 show Anna AEyes_Angry ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left

 show Twins AngryEyes_Lucy DefaultLucy AngryEyes_Yvvy DefaultYvvy with dissolve

 b "The evil queen and her menial, of course!"

 show Twins DefaultEyes_Lucy DefaultLucy AngryEyes_Yvvy DefaultYvvy
 with dissolve

 a "{i}This thing{/i} doesn’t look smart, Yvvy."

 show Twins DefaultEyes_Lucy DefaultLucy DefaultEyes_Yvvy DefaultYvvy
 with dissolve

 yvvy "Not even a tiny bit, Lucy."

 show Twins AngryEyes_Lucy ClosedMouth_Yvvy
 with dissolve

 lucy "Wait... {w}What is that?!"

 hide Twins
 hide Anna onlayer over_screens
 with dissolve

 window hide
 show Colar at colar_foco onlayer over_screens
 with dissolve
 pause

 hide Colar onlayer over_screens
 window show

 show Twins
 with dissolve

 yvvy "That’s… {w}from the prophecy!"
 lucy "No way! {p}Is too early for that!"
 yvvy "It doesn’t matter! The evil queen must definitely {b}not{/b} see this!"
 yl "Let’s take it to grandma!"

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left

 anna "Wait! No-"

 hide Anna onlayer over_screens
 hide Twins
 hide arvore brilha
 show BGGrandma
 with fade

 jump to_grandma

 # This ends the game.

 return
