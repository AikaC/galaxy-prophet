label to_grandma:

 show GBody
 show GAngry
 with dissolve

 grandma "So..."
 grandma "Anyone cares to explain what is going on?"

 hide GBody
 hide GAngry
 show ABody
 show ATedio
 show ARope
 with dissolve

 anna "I-"

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve

 lucy "We were at the secret temple and {i}this thing{/i}..."
 
 hide Twins Body
 hide LD
 hide YD
 show ABody
 show ATedio
 show ARope
 with dissolve

 anna "Girl… I’m a girl…"

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve

 lucy "What’s a girl?"
 yvvy "Anyway, {i} this girl{/i} showed up from literally nowhere."

 hide LD
 show LA
 with dissolve

 lucy "And look at this!"

 hide Twins Body
 hide LA
 hide YD
 with dissolve

 window hide
 show Colar at colar_foco onlayer over_screens
 pause

 hide Colar onlayer over_screens
 window show
 show GBody
 show GAngry
 with dissolve


 grandma "Now…{w} That’s a rare sight."
 grandma "How did you get this, child?"

 hide GBody
 hide GAngry
 with dissolve

 menu:
  "No, me first.":
   $ moral -= 5
   jump first
  "I bought it.":
   jump store
  "…":
   $ moral -= 10
   jump release

label first:
 show ABody
 show AAngry
 show ARope
 with dissolve

 anna "I want some answers first."

 hide ABody
 hide AAngry
 hide ARope
 show Twins Body
 show LD
 show YL
 with dissolve

 yvvy "{i}The girl{\i} has courage."

 hide LD
 show LL
 with dissolve

 lucy "I have to acknowledge that."

 hide Twins Body
 hide LL
 hide YL
 show GBody
 show GAngry
 with dissolve

 grandma "…"

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "Fair enough. {w}What do you want to know?"

 hide GBody
 hide GClosedEyes
 with dissolve

 show ABody
 show AWorried
 show ARope
 with dissolve

 anna "Who is this evil queen that you always talk about?"

 hide ABody
 hide AWorried
 hide ARope
 show Twins Body
 show LA
 show YA
 with dissolve

 yvvy "Lower..."
 lucy "They might hear you..."

 hide Twins Body
 hide LA
 hide YA
 show GBody
 show GHappy
 with dissolve

 grandma "Don't worry, we are safe here."
 grandma "I don't recommend keeping using the word \"evil\" to describe her, though."

 hide GBody
 hide GHappy
 show Twins Body
 show LA
 show YA
 with dissolve

 yvvy "Even though she {b}is {/b}the evil queen."
 lucy "..."

 hide Twins Body
 hide LA
 hide YA
 show GBody
 show GAngry
 with dissolve

 grandma "Not long ago, a creature appeared in our world, just like you."
 grandma "I am not aware of the details..."
 grandma "But she managed to conquer the throne after sealing a deal with her current right hand."

 hide GBody
 hide GAngry
 show Twins Body
 show LA
 show YA
 with dissolve

 lucy "We've been scared of her since then."

 hide YA
 show YD
 with dissolve

 yvvy "You must be our hero who came to defeat the evil that plague us."
 
 hide LA
 show LD
 with dissolve

 lucy "But that's odd, she didn't do anything yet. Why are you here?"

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show ATedio
 show ARope
 with dissolve
 
 anna "That's what I'm dying to know..."

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "Wait, please don't die..."
 lucy "... Yet."

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show ATedio
 show ARope
 with dissolve

 anna "Anyway, if you say she didn’t do anything yet, then why call her the evil queen?"

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve
 
 lucy "Because she threw the real king in the dungeon."
 yvvy "He didn't deserve that."

 hide Twins Body
 hide LD
 hide YD
 show GBody
 show GAngry
 with dissolve

 grandma "I will explain everything."
 grandma "You two, please release {i}the girl{/i} now."

 hide GBody
 hide GAngry
 with dissolve

 jump prophecy

 return

label store:
 show ABody
 show AWorried
 show ARope
 with dissolve

 anna "I bought it at a store. It’s a pretty popular item where I live."

 hide ABody
 hide AWorried
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve

 yvvy "Bought? Store? {i}This girl{/i} is weird."

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show ATedio
 show ARope
 with dissolve

 anna "…"
 anna "Are we really speaking the same language?"

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YD
 with dissolve

 lucy "What’s a language?"

 hide Twins Body
 hide LD
 hide YD
 show ABody
 show ATedio
 show ARope
 with dissolve

 anna "Can I go home already?"

 hide ABody
 hide ATedio
 hide ARope
 show Twins Body
 show LD
 show YA
 with dissolve

 yvvy "No! We need to know more about the prophecy first!"

 hide Twins Body
 hide LD
 hide YA
 show ABody
 show AWorried
 show ARope
 with dissolve

 anna "What prophecy?"

 hide ABody
 hide AWorried
 hide ARope
 show GBody
 show GHappy
 with dissolve

 grandma "I'm going to explain everything."
 grandma "You two… Release {i}the girl{/i}."

 hide GBody
 hide GHappy
 with dissolve

 jump prophecy

 return

label release:
 show Twins Body
 show LD
 show YA
 with dissolve

 yvvy "Why are you not saying anything?"

 hide LD
 show LA
 with dissolve

 lucy "So, do you work for the queen?"
 yvvy "Did the queen’s menial send you to find our secret temple?"

 hide LA
 show LD
 with dissolve

 lucy "Oh, no! What if they already know about it?"

 hide YA
 show YD
 with dissolve

 yvvy "What if they are already coming?"

 hide Twins Body
 hide LD
 hide YD
 show GBody
 show GAngry
 with dissolve

 grandma "Calm down, you two!"
 grandma "I’m sure that is not the case… {w}Probably…"

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "First off… Release {i}the girl{/i}."

 hide GBody
 hide GClosedEyes
 with dissolve

 jump prophecy

 return