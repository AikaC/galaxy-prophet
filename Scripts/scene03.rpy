label prophecy:

 show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Thank you for releasing me."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins AngryEyes_Lucy AngryEyes_Yvvy
 with dissolve

 lucy "We are still watching you."
 yvvy "You are too suspicious."

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "Lucy, Yvvy. {i}The girl{/i} is a guest now."
 grandma "Please, behave yourselves."

 hide GBody
 hide GAngry
 show Twins
 with dissolve

 yl "Yes, grandma…"

 hide Twins
 show GBody
 show GHappy
 with dissolve

 grandma "So, {i}girl{/i}-"

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "[anna]."

 hide GBody
 hide GHappy

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins AngryEyes_Lucy AngryEyes_Yvvy
 with dissolve

 yvvy "Are you a \“Girl\” or a \“[anna]\”?"
 lucy "Could you please make up your mind, {i}dear guest?{/i}"

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "..."

 hide GBody
 hide GAngry
 show Twins
 with dissolve

 yl "Sorry, grandma…"

 hide Twins
 show GBody
 show GHappy
 with dissolve

 grandma "So... [anna]."

 stop music fadeout 1.0

 hide GBody
 hide GHappy
 with dissolve

 #cutscene start

 play music "audio/CutsceneIntro.ogg"
 queue music "audio/CutsceneLoop.ogg"

 grandma "Countless ages ago when this place didn’t have much to see…"
 grandma "A shiny being appeared during a moonless night and said..."

 show BG01 onlayer over_screens
 show textc onlayer over_screens
 window hide
 with dissolve
 pause

 hide BG01 onlayer over_screens
 hide textc onlayer over_screens
 window show

 grandma "Before we could even react, it’s light blinded us"
 grandma "And the sacred tree appeared in that same spot"
 grandma "As if it always had been there."
 grandma "We tried to ask for the meaning of that."
 grandma "Warlocks and fairies came from distance trying to help."
 grandma "But nothing else happened."
 grandma "We decided then to wait."
 grandma "Families started to grow,"
 grandma "clans turned into villages,"
 grandma "kingdoms were brought to life,"
 grandma "but the tree remained in silence."
 grandma "When we were almost giving up…"
 grandma "A new sign showed up."

 stop music fadeout 1.0

 #cutscene end
 
 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"

 show GBody
 show GHappy
 with dissolve

 grandma "Not so much time after, we learned that our kingdom had a new queen."
 grandma "I can’t go too far from the tree since the guardians linked their lifespan with the temple at some point."

 hide GHappy
 show GClosedEyes
 with dissolve

 grandma "But that’s history for another day."

 hide GClosedEyes
 show GAngry
 with dissolve

 grandma "Will you help us?"

 hide GBody
 hide GAngry
 window hide
 hide Anna onlayer over_screens
 with dissolve

 menu:
  "How can you be so sure?":
   $extra = True
   window show
   jump so_sure
  "Yes":
   if moral == 100:
    window show
    jump yhelp
   else:
    $moral += 10
    window show
    jump yhelp
  "No":
   $moral -= 10
   window show
   jump nhelp
 return

label so_sure:
 
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Despite the oddly fitting time, I don’t see how the new queen is related to this prophecy."
 anna "How long has she been ruling this place?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins
 with dissolve

 yvvy "Half generation for now…"

 show Twins ClosedMouth_Yvvy ClosedMouth_Lucy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Has she done something evil after taking the crown?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultLucy
 with dissolve

 lucy "Not yet…"

 show Twins ClosedMouth_Lucy AngryEyes_Yvvy DefaultYvvy
 with dissolve

 yvvy "Isn’t locking the old king evil enough?"

 show Twins ClosedMouth_Yvvy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "It is… {w}But I don’t see a dark era coming from just this."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultEyes_Yvvy DefaultYvvy DefaultEyes_Lucy DefaultLucy
 with dissolve

 yl "This we can explain."
 lucy "We served the last king, so we were there when everything happened."
 yvvy "We still don’t know how queen Selyna and that awful creature ended together, though."

 hide Twins
 hide Anna onlayer over_screens

 stop music fadeout 1.0

 #cutscene start

 
 play music "audio/CutsceneIntro.ogg"
 queue music "audio/CutsceneLoop.ogg"

 lucy "It all started with a surprise attack."
 yvvy "And I’m gonna tell you, we were really surprised."
 lucy "You’re right, sis. Not cute at all."
 yvvy "I don't know how an outsider made a deal with such a powerful creature,"
 yvvy "but they managed to conquer the castle in no time."
 lucy "We didn’t have that much protection anyways..."
 lucy "... since it’s not common to enter others houses..."
 yvvy "… Or castles… "
 lucy "Without being invited."
 yvvy "Me and Lucy managed to hide on time,"
 lucy "But we saw everything."
 yvvy "We couldn’t hear well though…"

 show BG01 onlayer over_screens
 show textc2 onlayer over_screens
 window hide
 with dissolve
 pause

 hide BG01 onlayer over_screens
 hide textc2 onlayer over_screens
 window show

 lucy "It looked like queen Selyna and the last king already knew eachother."

 #cutscene end

 show Twins
 with dissolve

 yvvy "That wouldn’t be a surprise, though."
 lucy "True.{p}The last king used to travel to other galaxies a lot."
 yvvy "We don’t know how, before you ask."

 show Twins AngryEyes_Lucy
 with dissolve

 lucy "Queen Selyna clearly has personal issues here to deal with."

 show Twins AngryEyes_Yvvy
 with dissolve

 yvvy "Who knows what she is planning to do with the last king?"

 show Twins DefaultEyes_Lucy
 with dissolve

 lucy "… Or even with us."

 show Twins DefaultEyes_Yvvy
 with dissolve

 yl "Will you help us?"

 hide Twins
 window hide
 with dissolve

 menu:
  "I'll help":
   window show
   jump yhelp
  "I'm not helping":
   window show
   jump nhelp
 return

label yhelp:

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Sure, why not?"

 show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "It’s not like I can go back home that soon anyway."

 show Anna AEyes_Tedio ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedHappyEyes_Yvvy LaughingYvvy
 with dissolve

 yvvy "Thank you, [anna]."

 show Twins ClosedHappyEyes_Lucy LaughingLucy
 with dissolve

 lucy "You are a nice girl\/[anna] or whatever you want to be."

 show Twins ClosedMouth_Yvvy ClosedMouth_Lucy
 show Anna AEyes_Worried ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "…"

 show Twins ClosedMouth_Yvvy ClosedMouth_Lucy
 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Thanks?"

 hide Twins
 hide Anna onlayer over_screens
 jump route_01
 return

label nhelp:

 show Anna AEyes_Angry AOMouth_Angry onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Why should I?"
 anna "You said yourselves \“I’m too early\”."
 anna "So, I’m clearly not the one you need."

 show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left

 anna "I’m no warrior nor from this home."

 show Anna AEyes_Worried ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins
 with dissolve

 yvvy "You’re right but…"
 lucy "There must be something…"

 show Twins ClosedMouth_Lucy ClosedMouth_Yvvy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Look, I’m sorry for the dark era you’re about to face."
 anna "But I just want to go back to my dimension."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 
 hide Twins
 show GBody
 show GClosedEyes
 with dissolve

 grandma "If you are really part of this, there is no way home, child."

 anna "..."

 grandma "Sigh."

 hide GClosedEyes
 show GAngry
 with dissolve

 grandma "You may try talking with the other guardian."
 grandma "But don’t take it for granted."

 show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Thank you very much!"

 show Anna ACMouth_Happy onlayer over_screens:
  size (245,318.5)
  left
 with dissolve
 
 grandma "Yvvy, Lucy, take Anna to Paithyn."

 hide GBody
 hide GAngry
 show Twins ClosedMouth_Lucy
 with dissolve

 yvvy "But…"

 show Twins ClosedMouth_Yvvy DefaultLucy
 with dissolve

 lucy "Yes… Grandma."

 show Twins AngryEyes_Lucy
 with dissolve

 lucy "{color=F4C2C2}{i}If [anna]’s really from the prophecy, she’s not going back."

 show Twins AngryEyes_Yvvy ClosedMouth_Lucy DefaultYvvy
 with dissolve

 yvvy "Ugh..."
 yvvy "Let’s go then."

 hide Twins
 hide Anna onlayer over_screens
 with dissolve

 jump route_02
 return
