label route_01:
 anna "What do we do now?"

 hide ABody
 hide AHappy
 show GBody
 show GHappy
 with dissolve

 grandma "Now we need to go back to the sacred temple."
 grandma "That’s where our answers await us…{p}At least, I believe so."

 hide GBody
 hide GHappy
 show ABody
 show ATedio
 with dissolve

 anna "Couldn’t they just have called you instead of bringing me here then?"

 hide ABody
 hide ATedio
 show Twins Body
 show LD
 show YL
 with dissolve

 yvvy "Hehe…"

 hide LD
 show LL
 with dissolve

 lucy "Not funny this way."

 hide Twins Body
 hide LL
 hide YL
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
 with dissolve

 jump route_01menu
 return

label route_01menu:

 if extra == True:

  show BGExtra
  show ABody
  show AWorried
  with dissolve

  anna "By the way..." 

  hide ABody
  hide AWorried
  with dissolve

  menu:
   "Where are we?":
    jump m31
   "The queen’s right hand?":
    jump ancient_dragon
   "You linked your life to a tree?":
    jump tree_barrier
   "Travel between galaxies?":
    jump friend
   "Why do we understand each other?":
    jump translator
   "Let’s just go":
    hide BGExtra
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

 show ABody
 show AHappy
 with dissolve

 anna "Yes... {w}I didn’t notice when I first arrived."
 anna "But it's gorgeous."

 hide ABody
 hide AHappy
 show GBody
 show GHappy
 with dissolve

 grandma "It is, indeed."

 hide GBody
 hide GHappy
 with dissolve

 a "[anna]."

 show ABody
 show AWorried
 with dissolve

 anna "Who is that?"

 hide ABody
 hide AWorried
 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "What?"
 lucy "No one’s here."

 hide Twins Body
 hide LD
 hide YD
 with dissolve

 a "[anna]!"

 show ABody
 show ATedio
 with dissolve

 anna "..."

 hide ATedio
 show AEmpty
 with dissolve
 pause

 hide ABody
 hide AEmpty
 show Twins Body
 show LD
 show YD
 with dissolve
 
 yvvy "Wait, [anna]!"
 lucy "Where are you going, girl?"

 hide Twins Body
 hide LD
 hide YD
 show GBody
 show GAngry
 with dissolve

 grandma "Leave her be.{p}Is the sacred tree calling her."
 grandma "I can feel it."

 hide GBody
 hide GAngry
 with dissolve
 #sc "Hi, [anna.]"

 jump demo01
 return

label m31:

 show ABody
 show AWorried
 with dissolve

 anna "This doesn’t look even a tiny bit like home…"
 anna "What is this place?"

 hide ABody
 hide AWorried
 show GBody
 show GHappy
 with dissolve

 grandma "Judging by your looks, this is a different galaxy from yours."

 hide GBody
 hide GHappy
 show Twins Body
 show LL
 show YL
 with dissolve

 yvvy "We have a lot of travellers here."
 lucy "But none of them look like you."

 hide Twins Body
 hide LL
 hide YL
 show GBody
 show GHappy
 with dissolve

 grandma "It can be a little bit late, but welcome to Faellyx."

 hide GBody
 hide GHappy
 show Twins Body
 show LL
 show YL
 with dissolve

 yvvy "Galaxy M-31!"
 lucy "We’re inside a star!"

 hide Twins Body
 hide LL
 hide YL
 show ABody
 show AWorried
 with dissolve

 anna "{color=F4C2C2}{i}Andromeda? So I’m not in another dimension?{\i}"
 anna "{color=F4C2C2}{i}How did I get so far?{\i}"

 hide ABody
 hide AWorried
 with dissolve

 jump route_01menu
 return

label ancient_dragon:

 show ABody
 show AWorried
 with dissolve

 anna "You told me about queen Selyna."
 anna "But you didn’t say anything about the other one."

 hide ABody
 hide AWorried
 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "Just thinking about him gives me chills."
 lucy "He’s the last one of his kind."

 hide YD
 show YA
 with dissolve

 yvvy "The reason why we decided to make the secret temple secret in the first place."

 hide LD
 show LA
 with dissolve

 lucy "Don’t go near him!"

 hide Twins Body
 hide YA
 hide LA
 show GBody
 show GAngry
 with dissolve

 grandma "Braxton was with us when the prophecy was first known."
 grandma "Oh well, he was here way before our existence."
 grandma "He told me once that his type was named “Ancient Dragon” and it was one of the first living beings to be on this star."

 hide GBody
 hide GAngry
 show ABody
 show AWorried
 with dissolve

 anna "But you said before that he and the queen must not know about the tree."

 hide ABody
 hide AWorried
 show GBody
 show GAngry
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
 grandma "Even though the ancient dragon doesn't remember us anymore, that fight somehow was marked in his being."
 grandma "So he never approached us again."

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "There’s nothing we can do about it."

 hide GBody
 hide GClosedEyes
 with dissolve

 jump route_01menu
 return

label tree_barrier:

 show ABody
 show AWorried
 with dissolve

 anna "I know you said that's a story for another day, but I can't take that off of my mind."
 anna "You linked your life to a tree?"

 hide ABody
 hide AWorried
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
 with dissolve

 jump route_01menu
 return

label friend:

 show ABody
 show AAngry
 with dissolve

 anna "You said it’s possible to travel between galaxies…"

 hide AAngry
 show AWorried
 with dissolve

 anna "Can I go home?"

 hide ABody
 hide AWorried
 show GBody
 show GAngry
 with dissolve

 grandma "As I said earlier, if you are part of the prophecy there’s no way home until everything is done."

 hide GAngry
 show GHappy
 with dissolve

 grandma "But I do have a friend who can help you later, if that’s what you really want."

 hide GBody
 hide GHappy
 show ABody
 show AHappy
 with dissolve

 anna "Really?!"
 anna "Thank you very much!"

 hide ABody
 hide AHappy
 with dissolve

 jump route_01menu
 return

label translator:

 show ABody
 show ATedio
 with dissolve

 anna "We clearly don’t speak the same language."

 hide ATedio
 show AWorried
 with dissolve

 anna "How do we understand each other?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LA
 with dissolve

 lucy "There you go with this \“language\” thing again…"

 hide YD
 show YA
 with dissolve

 yvvy "What is that?"

 hide Twins Body
 hide YA
 hide LA
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
 with dissolve

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