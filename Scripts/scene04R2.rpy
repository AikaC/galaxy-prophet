label route_02:

 if extra == True:

  play music "audio/YL.ogg" fadeout 1.0

  show BGExtra
  show Twins ClosedMouth_Lucy
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

 show Twins ClosedMouth_Yvvy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Yes?"

 show Twins DefaultLucy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 lucy "Where are you from?"

 show Twins ClosedMouth_Lucy
 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Well, I’m from the Earth."

 show Twins DefaultYvvy
 show Anna ACMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yvvy "Earth? {w}Never heard about it."

 show Twins DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "What kind of star is that? {w}Is it too far away?"

 show Twins ClosedMouth_Lucy
 show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Star!? We’re in a star!?"

 show Twins ClosedHappyEyes_Yvvy DefaultYvvy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yvvy "Of course, dummy."

 show Twins ClosedHappyEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "Where else should we be?"

 show Twins ClosedMouth_Lucy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "On a planet…?"

 show Twins DefaultEyes_Lucy DefaultEyes_Yvvy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yl "..."

 show Twins AngryEyes_Yvvy DefaultYvvy
 with dissolve

 yvvy "{color=F4C2C2}{i}Are you sure we should take her to granny Paithyn?"
 yvvy "{color=F4C2C2}{i}She mats with the second part of-"

 show Twins AngryEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "{color=F4C2C2}{i}Shh… {w}She might hear you!"
 lucy "{color=F4C2C2}{i}Let’s just make what grandma said first."

 show Twins ClosedMouth_Lucy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Ahh… Hello...?"

 show Twins DefaultEyes_Yvvy DefaultYvvy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yvvy "Yeah…{w} A planet.{p}I’ve heard about it before…"

 show Twins DefaultEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "It’s far away from here. "

 show Twins DefaultYvvy ClosedMouth_Lucy
 with dissolve

 yvvy "Hundreds of galaxies away."

 show Twins ClosedMouth_Yvvy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "And where are we?"

 show Twins ClosedHappyEyes_Lucy DefaultLucy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 lucy "Galaxy M-13."

 show Twins ClosedMouth_Lucy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "That far!?"

 show Twins ClosedHappyEyes_Yvvy DefaultYvvy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yvvy "You know this place?"

 show Twins DefaultEyes_Lucy DefaultEyes_Yvvy ClosedMouth_Yvvy
 show Anna AEyes_Happy AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "We call it the Andromeda galaxy…"
 #anna "That means…"
 anna "Lucy, Yvvy"

 show Twins DefaultLucy DefaultYvvy
 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 yl "Yes?"

 hide Twins
 hide Anna onlayer over_screens
 window hide
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
  window show
  jump castle
 "The last king?":
  window show
  jump last_king
 "Nevermind...":

  window show
  show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
   size (245,318.5)
   left
  with dissolve

  anna "Let’s just keep going."

  hide Anna onlayer over_screens
  with dissolve

  jump meet_Paithyn
 
  return

label castle:

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "You worked in the castle?"
 anna "How was there?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins
 with dissolve

 lucy "It was quite peaceful."

 show Twins ClosedHappyEyes_Yvvy
 with dissolve

 yvvy "Right?"

 show Twins DefaultEyes_Yvvy
 with dissolve

 yvvy "That’s why our job was to make things funnier."

 show Anna AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "How so?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedHappyEyes_Lucy LaughingLucy
 with dissolve

 lucy "With music!"

 show Twins ClosedHappyEyes_Yvvy LaughingYvvy
 with dissolve

 yvvy "Wanna see?"

 show Twins ClosedMouth_Lucy ClosedMouth_Yvvy
 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "I do."

 show Anna AEyes_Tedio ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultEyes_Yvvy DefaultYvvy
 with dissolve

 yvvy "Then you’ll have to come back later."

 show Twins DefaultEyes_Lucy DefaultLucy
 with dissolve

 lucy "We’ll be waiting."

 hide Twins
 hide Anna onlayer over_screens
 window hide
 with dissolve

 jump menu_provisorio
 return

label last_king:

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Did you see the last king frequently?"
 anna "How was he?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins AngryEyes_Yvvy AngryEyes_Lucy
 with dissolve

 yvvy "Don’t say that in the past!"
 lucy "The king is still alive, he’s just imprisoned."
 yvvy "We still communicate in secret."
 lucy "He’s like a father to us."

 hide Twins
 hide Anna onlayer over_screens
 window hide
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

 $ extra == True

 show BGPaithyn
 hide BGGrandma
 show Twins
 with dissolve

 yl "We're here."

 hide Twins
 show PBody
 show PHappy
 with dissolve

 paithyn "Long time no see."
 paithyn "Khaleesi told me you were coming."

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Who?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 
 hide PBody
 hide PHappy
 show Twins
 with dissolve

 yl "Grandma."

 hide Twins
 show PBody
 show PHappy
 with dissolve

 paithyn "And you must be [anna]."
 paithyn "It's a pleasure to meet you."

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Nice to meet you too."

 show Anna ACMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 paithyn "Khaleesi told me that you want to go back, home."
 paithyn "I can try helping you, but here's the thing..."
 paithyn "Opening a portal to another dimension is really tricky."
 paithyn "You'll have to collect some ingredients by yourself."
 paithyn "That's because we also need you energy inlaid in the plants."
 anna "How do I do that?"
 paithyn "No worries, you just need to spend some time with it."
 paithyn "The time you'll take to collect everything and come back here is enough."
 anna "Ok! Easy Peasy!"
 paithyn "Good!{w} I'll need these ingredients."
 #lista de ingredientes
 anna "What?"
 paithyn "Lucy and Yvvy will have to stay."
 paithyn "Good luck!"
 anna "Wait what are thos-{w} and they left..."
 anna "Alright! Time to go home!"

 jump minion
 return
