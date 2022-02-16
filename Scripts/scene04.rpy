label route_01:

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "What do we do now?"

 show Anna ACMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 show GBody
 show GHappy
 with dissolve

 grandma "Now we need to go back to the sacred temple."
 grandma "That’s where our answers await us…{p}At least, I believe so."

 show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Couldn’t they just have called you instead of bringing me here then?"

 hide GBody
 hide GHappy

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedMouth_Lucy
 with dissolve

 yvvy "Hehe…"

 show Twins ClosedHappyEyes_Lucy LaughingLucy ClosedMouth_Yvvy
 with dissolve

 lucy "Not funny this way."

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "You two…"

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "Let’s just go."

 hide GBody
 hide GClosedEyes
 hide BGGrandma
 show bgblack
 with dissolve

 jump route_01menu
 return

label route_01menu:

 if extra == True:

  show BGExtra
  show Anna AOMouth_Worried onlayer over_screens:
   size (245,318.5)
   left
  with dissolve

  anna "By the way..." 

  hide Anna onlayer over_screens
  window hide
  with dissolve

  menu:
   "Where are we?":
    window show
    jump m31
   "The queen’s right hand?":
    window show
    jump ancient_dragon
   "You linked your life to a tree?":
    window show
    jump tree_barrier
   "Travel between galaxies?":
    window show
    jump friend
   "Why do we understand each other?":
    window show
    jump translator
   "Let’s just go":
    hide BGExtra
    window show
    jump route_01p02

 else:
  show bgblack
  jump route_01p02
  return

label route_01p02:

 stop music fadeout 1.0

 play music "audio/SWIntro.ogg" fadeout 1.0
 queue  music "audio/SWLoop.ogg"

 $ extra == False
 show arvore brilha
 with dissolve

 grandma "Can you see the tree?"

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Yes... {w}I didn’t notice when I first arrived."
 anna "But it's gorgeous."

 show Anna ACMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 show GBody
 show GHappy
 with dissolve

 grandma "It is, indeed."

 hide Anna onlayer over_screens
 hide GBody
 hide GHappy
 with dissolve

 a "[anna]."

 show Anna AOMouth_Worried
 with dissolve

 anna "Who is that?"

 hide Anna
 show Twins
 with dissolve

 yvvy "What?"
 lucy "No one’s here."

 hide Twins
 with dissolve

 a "[anna]!"

 show Anna
 with dissolve

 anna "..."

 show Anna AEyes_Empty
 with dissolve
 pause

 hide Anna
 show Twins
 with dissolve
 
 yvvy "Wait, [anna]!"
 lucy "Where are you going, girl?"

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "Leave her be.{p}Is the sacred tree calling her."
 grandma "I can feel it."

 hide GBody
 hide GAngry
 with dissolve

 call screen bar_nav
 return

label m31:

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "This doesn’t look even a tiny bit like home…"
 anna "What is this place?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show GBody
 show GHappy
 with dissolve

 grandma "Judging by your looks, this is a different galaxy from yours."

 hide GBody
 hide GHappy
 show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedHappyEyes_Lucy ClosedMouth_Lucy
 with dissolve

 yvvy "We have a lot of travellers here."

 show Twins DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "But none of them look like you."

 hide Twins
 show GBody
 show GHappy
 with dissolve

 grandma "It can be a little bit late, but welcome to Faellyx."

 hide GBody
 hide GHappy
 show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedHappyEyes_Lucy ClosedMouth_Lucy
 with dissolve

 yvvy "Galaxy M-31!"

 show Twins LaughingLucy ClosedMouth_Yvvy
 with dissolve

 lucy "We’re inside a star!"

 anna "{color=F4C2C2}{i}Andromeda? So I’m not in another dimension?{\i}"
 anna "{color=F4C2C2}{i}How did I get so far?{\i}"

 hide Twins
 hide Anna onlayer over_screens
 with dissolve

 window hide
 jump route_01menu
 return

label ancient_dragon:

 $ ancientDragon == True
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "You told me about queen Selyna."
 anna "But you didn’t say anything about the other one."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedMouth_Lucy
 with dissolve

 yvvy "Just thinking about him gives me chills."

 show Twins ClosedMouth_Yvvy DefaultLucy
 with dissolve

 lucy "He’s the last one of his kind."

 show Twins AngryEyes_Yvvy ClosedMouth_Lucy DefaultYvvy
 with dissolve

 yvvy "The reason why we decided to make the secret temple secret in the first place."

 show Twins AngryEyes_Lucy ClosedMouth_Yvvy DefaultLucy
 with dissolve

 lucy "Don’t go near him!"

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "Braxton was with us when the prophecy was first known."
 grandma "Oh well, he was here way before our existence."
 grandma "He told me once that his type was named “Ancient Dragon”..."
 grandma "... and it was one of the first living beings to be on this star."

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "But you said before that he and the queen must not know about the tree."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 grandma "That’s because later on he turned against us."
 grandma "It was terrible, Braxton tried to destroy the sacred tree when no one was around."

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "He said it was necessary and the prophecy meaningless."
 grandma "One of our friends tried to stop him and they started to fight."

 hide GClosedEyes
 show GAngry
 with dissolve

 grandma "All he could do was erase Braxton memories, but that cost his life in exchange."
 grandma "Even though the ancient dragon doesn't remember us anymore,"
 grandma "that fight somehow was marked in his being."
 grandma "So he never approached us again."

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "There’s nothing we can do about it."

 hide GBody
 hide GClosedEyes
 hide Anna onlayer over_screens
 with dissolve

 window hide
 jump route_01menu
 return

label tree_barrier:

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "I know you said that's a story for another day, but I can't take that off of my mind."
 anna "You linked your life to a tree?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show GBody
 show GAngry
 with dissolve

 grandma "Me and two other friends."
 grandma "We created the secret temple after our comrade's death."
 grandma "To build a powerful barrier against any possible damage the sacred tree could receive, our lifespan was used."

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "We’ll live as long as this barrier exists."

 hide GBody
 hide GClosedEyes
 hide Anna onlayer over_screens
 with dissolve

 window hide
 jump route_01menu
 return

label friend:

 show Anna AEyes_Angry AOMouth_Angry onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "You said it’s possible to travel between galaxies…"

 show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Can I go home?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show GBody
 show GAngry
 with dissolve

 grandma "As I said earlier, if you are part of the prophecy there’s no way home until everything is done."

 hide GAngry
 show GHappy
 with dissolve

 grandma "But I do have a friend who can help you later, if that’s what you really want."

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Really?!"

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 anna "Thank you very much!"

 hide GBody
 hide GHappy
 hide Anna onlayer over_screens
 with dissolve

 window hide
 jump route_01menu
 return

label translator:

 show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "We clearly don’t speak the same language."

 show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "How do we understand each other?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins AngryEyes_Lucy LaughingLucy ClosedMouth_Yvvy
 with dissolve

 lucy "There you go with this \“language\” thing again…"

 show Twins ClosedMouth_Lucy AngryEyes_Yvvy LaughingYvvy
 with dissolve

 yvvy "What is that?"

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "Since there’s a lot of travellers from different stars..."
 grandma "... the mages of this place created a spell that translates everything to an equivalent word in each idiom."
 grandma "But that doesn’t always work, like this \“language\” you say."

 hide GAngry
 show GHappy
 with dissolve

 grandma "We don’t have anything like this here, so for us it is just a bunch of sounds."

 hide GBody
 hide GHappy
 hide Anna onlayer over_screens
 with dissolve

 window hide
 jump route_01menu
 return

label demo01:

 play music "audio/SWIntro.ogg" fadeout 1.0
 queue  music "audio/SWLoop.ogg"

 scene cutscenefundo
 show seirei at floating
 with dissolve

 sc "Hello, Anna."
 sc "Unfortunately, the dev only had time to make the game until here, so..."
 sc "You’ve reached the end of the demo."
 sc "Wanna know why I called you?"
 sc "Please come back later <3"
 sc "Oh, by the way…"
 sc "Have you tried other routes?"
 sc "There’s also secret scenes that tell more about this universe's story."
 sc "See you soon."

 hide cutscenefundo
 hide seirei

 jump credits
 return
