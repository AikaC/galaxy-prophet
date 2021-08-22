label prophecy:

 show ABody
 show ATedio
 with dissolve

 anna "Thank you for releasing me."

 hide ABody
 hide ATedio
 show Twins Body
 show LA
 show YA
 with dissolve

 lucy "We are still watching you."
 yvvy "You are too suspicious."

 hide Twins Body
 hide LA
 hide YA
 show GBody
 show GAngry
 with dissolve

 grandma "Lucy, Yvvy. {i}The girl{/i} is a guest now."
 grandma "Please, behave yourselves."

 hide GBody
 hide GAngry
 show Twins Body
 show LD
 show YD
 with dissolve

 yl "Yes, grandma…"

 hide Twins Body
 hide LD
 hide YD
 show GBody
 show GHappy
 with dissolve

 grandma "So, {i}girl{/i}-"

 hide GBody
 hide GHappy
 show ABody
 show ATedio
 with dissolve

 anna "[anna]."

 hide ABody
 hide ATedio
 show Twins Body
 show LA
 show YA
 with dissolve

 yvvy "Are you a \“Girl\” or a \“[anna]\”?"
 lucy "Could you please make up your mind, {i}dear guest?{/i}"

 hide Twins Body
 hide LA
 hide YA
 show GBody
 show GAngry
 with dissolve

 grandma "..."

 hide GBody
 hide GAngry
 show Twins Body
 show LD
 show YD
 with dissolve

 yl "Sorry, grandma…"

 hide Twins Body
 hide LD
 hide YD
 show GBody
 show GHappy
 with dissolve

 grandma "So... [anna]."

 stop music fadeout 1.0

 #hide GBody
 hide GHappy
 show GAngry
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
 
 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "We tried to ask for the meaning of that."
 grandma "Warlocks and fairies came from distance trying to help."
 grandma "But nothing else happened."

 hide GClosedEyes
 show GAngry
 with dissolve

 grandma "We decided then to wait."
 grandma "Families started to grow,"
 grandma "clans turned into villages,"
 grandma "kingdoms were brought to life,"

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "but the tree remained in silence."
 grandma "When we were almost giving up…"
 grandma "A new sign showed up."

 stop music fadeout 1.0

 #cutscene end
 
 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"

 hide GClosedEyes
 #show GBody
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
 with dissolve

 menu:
  "How can you be so sure?":
   $extra = True
   jump so_sure
  "Yes":
   if moral == 100:
    jump yhelp
   else:
    $moral += 10
    jump yhelp
  "No":
   $moral -= 10
   jump nhelp
 return

label so_sure:
 
 show ABody
 show AWorried
 with dissolve

 anna "Despite the oddly fitting time, I don’t see how the new queen is related to this prophecy."
 anna "How long has she been ruling this place?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "Half generation for now…"

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "Has she done something evil after taking the crown?"

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 lucy "Not yet…"

 hide YD
 show YA
 with dissolve

 yvvy "Isn’t locking the old king evil enough?"

 hide Twins Body
 hide YA
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "It is… {w}But I don’t see a dark era coming from just this."

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "This we can explain."
 lucy "We served the last king, so we were there when everything happened."
 yvvy "We still don’t know how queen Selyna and that awful creature ended together, though."

 stop music fadeout 1.0

 #cutscene start

 
 play music "audio/CutsceneIntro.ogg"
 queue music "audio/CutsceneLoop.ogg"

 lucy "It all started with a surprise attack."

 hide YD
 show YA
 with dissolve

 yvvy "And I’m gonna tell you, we were really surprised."

 hide LD
 show LA

 lucy "You’re right, sis. Not cute at all."
 yvvy "I don't know how an outsider made a deal with such a powerful creature,"
 yvvy "but they managed to conquer the castle in no time."
 lucy "We didn’t have that much protection anyways..."
 lucy "... since it’s not common to enter others houses..."
 yvvy "… Or castles… "
 lucy "Without being invited."

 hide YA
 show YD
 with dissolve

 yvvy "Me and Lucy managed to hide on time,"

 hide LA
 show LD
 with dissolve

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

 yvvy "That wouldn’t be a surprise, though."
 lucy "True.{p}The last king used to travel to other galaxies a lot."
 yvvy "We don’t know how, before you ask."
 lucy "Queen Selyna clearly has personal issues here to deal with."
 yvvy "Who knows what she is planning to do with the last king?"
 lucy "… Or even with us."
 yl "Will you help us?"

 hide Twins Body
 hide YD
 hide LD
 with dissolve

 menu:
  "I'll help":
   jump yhelp
  "I'm not helping":
   jump nhelp
 return

label yhelp:

 show ABody
 show AHappy
 with dissolve

 anna "Sure, why not?"

 hide AHappy
 show ATedio
 with dissolve

 anna "It’s not like I can go back home that soon anyway."

 hide ABody
 hide ATedio
 show Twins Body
 show YL
 show LD
 with dissolve

 yvvy "Thank you, [anna]."

 hide LD
 show LL
 with dissolve

 lucy "You are a nice girl\/[anna] or whatever you want to be."

 hide Twins Body
 hide YL
 hide LL
 show ABody
 show AWorried
 with dissolve

 anna "…"

 hide AWorried
 show AHappy
 with dissolve

 anna "Thanks?"

 jump route_01
 return

label nhelp:

 show ABody
 show AAngry
 with dissolve

 anna "Why should I?"
 anna "You said yourselves \“I’m too early\”."
 anna "So, I’m clearly not the one you need."

 hide AAngry
 show AWorried
 with dissolve

 anna "I’m no warrior nor from this home."

 hide ABody
 hide AWorried
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "You’re right but…"
 lucy "There must be something…"

 hide Twins Body
 hide YD
 hide LD
 show ABody
 show AWorried
 with dissolve

 anna "Look, I’m sorry for the dark era you’re about to face."
 anna "But I just want to go back to my dimension."

 hide ABody
 hide AWorried
 show GBody
 show GClosedEyes
 with dissolve

 grandma "If you are really part of this, there is no way home, child."

 hide GBody
 hide GClosedEyes
 show ABody
 show AWorried
 with dissolve

 anna "..."

 hide ABody
 hide AWorried
 show GBody
 show GClosedEyes
 with dissolve

 grandma "Sigh."

 hide GClosedEyes
 show GAngry
 with dissolve

 grandma "You may try talking with the other guardian."
 grandma "But don’t take it for granted."

 hide GBody
 hide GAngry
 show ABody
 show AHappy
 with dissolve

 anna "Thank you very much!"

 hide ABody
 hide AHappy
 show GBody
 show GAngry
 with dissolve
 
 grandma "Yvvy, Lucy, take Anna to Paithyn."

 hide GBody
 hide GAngry
 show Twins Body
 show YD
 show LD
 with dissolve

 yvvy "But…"
 lucy "Yes… Grandma."

 hide LD
 show LA
 with dissolve

 lucy "{color=F4C2C2}{i}If [anna]’s really from the prophecy, she’s not going back."

 hide YD
 show YA
 with dissolve

 yvvy "Ugh..."
 yvvy "Let’s go then."

 hide Twins Body
 hide YA
 hide LA
 with dissolve

 jump route_02
 return