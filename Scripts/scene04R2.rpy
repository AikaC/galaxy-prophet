label route_02:

 if extra == True:

  play music "audio/YL.ogg" fadeout 1.0

  show BGExtra
  show Twins Body
  show YD
  show LD
  with dissolve

  jump star

 else:
  show bgblack
  hide BGGrandma
  with dissolve

  jump meet_Paithyn
 return

label star:

 yvvy "Hey, [anna]."

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "Yes?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 lucy "Where are you from?"

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AHappy
 with dissolve

 anna "Well, I’m from the Earth."

 hide ABody
 hide AHappy
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "Earth? {w}Never heard about it."
 lucy "What kind of star is that? {w}Is it too far away?"

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "Star!? We’re in a star!?"

 hide ABody
 hide AWorried
 show Twins Body
 show YL
 show LD
 with dissolve

 yvvy "Of course, dummy."

 hide LD
 show LL
 with dissolve

 lucy "Where else should we be?"

 hide Twins Body
 hide YL
 hide LL
 show ABody
 show AWorried
 with dissolve

 anna "On a planet…?"

 hide ABody
 hide AWorried
 show Twins Body
 show YA
 show LA
 with dissolve

 yl "..."
 yvvy "{color=F4C2C2}{i}Are you sure we should take her to granny Paithyn?"
 yvvy "{color=F4C2C2}{i}She mats with the second part of-"
 lucy "{color=F4C2C2}{i}Shh… {w}She might hear you!"
 lucy "{color=F4C2C2}{i}Let’s just make what grandma said first."

 hide Twins Body
 hide YA
 hide LA
 show ABody
 show AWorried
 with dissolve

 anna "Ahh… Hello...?"

 hide ABody
 hide AWorried
 show Twins Body
 show YL
 show LL
 with dissolve

 yvvy "Yeah…{w} A planet.{p}I’ve heard about it before…"
 lucy "It’s far away from here. "
 yvvy "Hundreds of galaxies away."

 hide Twins Body
 hide YL
 hide LL
 show ABody
 show AWorried
 with dissolve

 anna "And where are we?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 lucy "Galaxy M-13."

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "That far!?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "You know this place?"

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "We call it the Andromeda galaxy…"
 #anna "That means…"
 anna "Lucy, Yvvy"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 yl "Yes?"

 hide Twins Body
 hide YD
 hide LD
 with dissolve

 jump menu_provisorio

 #menu:
 # "There’s no way back?":
 #  jump no_way
 # "Can I go back home?":
 #  jump a_way
 return
 
label menu_provisorio: 
menu:
 "The castle?":
  jump castle
 "The last king?":
  jump last_king
 "Queen\'s menial?":
  jump menial
 "Nevermind...":

  show ABody
  show ATedio
  with dissolve

  anna "Let’s just keep going."

  hide ABody
  hide ATedio
  with dissolve

  jump meet_Paithyn
 
  return

label castle:

 show ABody
 show AWorried
 with dissolve

 anna "You worked in the castle?"
 anna "How was there?"

 hide ABody
 hide AWorried
 show Twins Body
 show LD
 show YD
 with dissolve

 lucy "It was quite peaceful."
 yvvy "Right?"
 yvvy "That’s why our job was to make things funnier."

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show AWorried
 with dissolve

 anna "How so?"

 hide ABody
 hide AWorried
 show Twins Body
 show LL
 show YD
 with dissolve

 lucy "With music!"

 hide YD
 show YL
 with dissolve

 yvvy "Wanna see?"

 hide Twins Body
 hide LL
 hide YL
 show ABody
 show AHappy
 with dissolve

 anna "I do."

 hide ABody
 hide AHappy
 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "Then you’ll have to come back later."
 lucy "We’ll be waiting."

 hide Twins Body
 hide LD
 hide YD
 with dissolve

 jump menu_provisorio
 return

label last_king:

 show ABody
 show AWorried
 with dissolve

 anna "Did you see the last king frequently?"
 anna "How was he?"

 hide ABody
 hide AWorried
 show Twins Body
 show YA
 show LA
 with dissolve

 yvvy "Don’t say that in the past!"
 lucy "The king is still alive, he’s just imprisoned."
 yvvy "We still communicate in secret."
 lucy "He’s like a father to us."

 hide Twins Body
 hide YA
 hide LA
 with dissolve
 
 jump menu_provisorio
 return

label menial:

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
 yvvy "The reason why we decided to make the secret temple secret in the first place."
 lucy "Don’t go near him!"

 hide Twins Body
 hide LD
 hide YD
 with dissolve


 jump menu_provisorio
 return
#label no_way:
#
# $ extra == False
# return

#label a_way:
# $ extra == False
# return

label meet_Paithyn:

 play music "audio/SWIntro.ogg" fadeout 1.0
 queue  music "audio/SWLoop.ogg"

 $ extra == False

 show BGPaithyn
 hide BGGrandma
 show Twins Body
 show LD
 show YD
 with dissolve

 yl "We're here."

 hide Twins Body
 hide LD
 hide YD
 show PBody
 show PHappy
 with dissolve

 paithyn "Long time no see."
 paithyn "Khaleesi told me you were coming."

 hide PBody
 hide PHappy
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

 yl "Grandma."

 hide Twins Body
 hide LD
 hide YD
 show PBody
 show PHappy
 with dissolve

 paithyn "And you must be [anna]."
 paithyn "It's a pleasure to meet you."

 hide PBody
 hide PHappy
 show ABody
 show AHappy
 with dissolve

 anna "Nice to meet you too."

 hide ABody
 hide AHappy
 show PBody
 show PHappy
 with dissolve

 paithyn "Khaleesi told me that you want to go back, home."
 paithyn "I can try helping you, but here's the thing..."
 paithyn "The dev only had time to make the game until here."
 paithyn "So you’ve reached the end of the demo."
 paithyn "Why don't you try another route in the meantime?"
 paithyn "There’s also secret scenes that tell more about this universe's story."
 paithyn "Try to find them"
 paithyn "See you soon."

 jump credits
 return