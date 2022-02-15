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
 show Twins ClosedMouth_Yvvy
 with dissolve

 lucy "We were at the secret temple and {i}this thing{/i}..."
 
 show Anna AEyes_Tedio AOMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Girl… I’m a girl…"

 show Anna AEyes_Tedio ACMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left

 lucy "What’s a girl?"

 show Twins DefaultYvvy ClosedMouth_Lucy
 with dissolve

 yvvy "Anyway, {i} this girl{/i} showed up from literally nowhere."

 show Twins AngryEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 with dissolve

 lucy "And look at this!"

 hide Twins
 hide Anna onlayer over_screens
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
 window hide
 show MENU
 with dissolve

 menu:
  "No, me first.":
   $ moral -= 5
   hide MENU
   window show
   jump first
  "I bought it.":
   hide MENU
   window show
   jump store
  "…":
   $ moral -= 10
   hide MENU
   window show
   jump release

label first:
 
 show Anna AEyes_Angry AOMouth_Angry rope onlayer over_screens:
  size (245,318.5)
  left

 anna "I want some answers first."

 show Anna ACMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedHappyEyes_Yvvy LaughingYvvy
 with dissolve

 yvvy "{i}The girl{\i} has courage."

 show Twins ClosedMouth_Yvvy ClosedHappyEyes_Lucy LaughingLucy
 with dissolve

 lucy "I have to acknowledge that."

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "…"

 hide GAngry
 show GClosedEyes
 with dissolve

 grandma "Fair enough. {w}What do you want to know?"

 show Anna AOMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left

 anna "Who is this evil queen that you always talk about?"

 hide GBody
 hide GClosedEyes
 show Anna ACMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 show Twins AngryEyes_Yvvy AngryEyes_Lucy
 with dissolve

 yvvy "Lower..."
 lucy "They might hear you..."

 hide Twins
 show GBody
 show GHappy
 with dissolve

 grandma "Don't worry, we are safe here."
 grandma "I don't recommend keeping using the word \"evil\" to describe her, though."

 hide GBody
 hide GHappy
 show Twins AngryEyes_Yvvy AngryEyes_Lucy ClosedMouth_Lucy
 with dissolve

 yvvy "Even though she {b}is {/b}the evil queen."
 lucy "..."

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "Not long ago, a creature appeared in our world, just like you."
 grandma "I am not aware of the details..."
 grandma "But she managed to conquer the throne after sealing a deal with her current right hand."

 hide GBody
 hide GAngry
 show Twins AngryEyes_Yvvy AngryEyes_Lucy ClosedMouth_Yvvy
 with dissolve

 lucy "We've been scared of her since then."

 show Twins DefaultYvvy ClosedMouth_Lucy
 with dissolve

 yvvy "You must be our hero who came to defeat the evil that plague us."
 
 show Twins DefaultLucy ClosedMouth_Yvvy DefaultEyes_Lucy
 with dissolve

 lucy "But that's odd, she didn't do anything yet. Why are you here?"

 show Twins ClosedMouth_Lucy DefaultEyes_Yvvy
 show Anna AEyes_Tedio AOMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 with dissolve
 
 anna "That's what I'm dying to know..."

 show Anna ACMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultYvvy
 with dissolve

 yvvy "Wait, please don't die..."

 show Twins ClosedMouth_Yvvy DefaultLucy
 with dissolve

 lucy "... Yet."

 show Twins ClosedMouth_Lucy
 show Anna AEyes_Tedio AOMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Anyway, if you say she didn’t do anything yet, then why call her the evil queen?"

 show Twins DefaultLucy
 show Anna ACMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 show Twins
 with dissolve
 
 lucy "Because she threw the real king in the dungeon."

 show Twins DefaultYvvy ClosedMouth_Lucy
 yvvy "He didn't deserve that."

 hide Twins
 show GBody
 show GAngry
 with dissolve

 grandma "I will explain everything."
 grandma "You two, please release {i}the girl{/i} now."

 hide GBody
 hide GAngry
 hide Anna onlayer over_screens
 with dissolve

 jump prophecy

 return

label store:

 show Anna AOMouth_Worried rope onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "I bought it at a store. It’s a pretty popular item where I live."

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins ClosedMouth_Lucy
 with dissolve

 yvvy "Bought? Store? {i}This girl{/i} is weird."

 show Twins ClosedMouth_Yvvy
 show Anna AEyes_Tedio onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "…"

 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left

 anna "Are we really speaking the same language?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultLucy
 with dissolve

 lucy "What’s a language?"

 show Twins ClosedMouth_Lucy
 show Anna AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "Can I go home already?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 show Twins DefaultYvvy AngryEyes_Yvvy
 with dissolve

 yvvy "No! We need to know more about the prophecy first!"

 show Twins ClosedMouth_Yvvy
 show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 with dissolve

 anna "What prophecy?"

 show Anna ACMouth_Worried onlayer over_screens:
  size (245,318.5)
  left
 hide Twins
 show GBody
 show GHappy
 with dissolve

 grandma "I'm going to explain everything."
 grandma "You two… Release {i}the girl{/i}."

 hide GBody
 hide GHappy
 hide Anna onlayer over_screens
 with dissolve

 jump prophecy

 return

label release:
 show Twins ClosedMouth_Lucy AngryEyes_Yvvy
 with dissolve

 yvvy "Why are you not saying anything?"

 show Twins DefaultLucy AngryEyes_Lucy
 with dissolve

 lucy "Do you work for the queen?"
 yvvy "Did the queen’s menial send you to find our secret temple?"

 show Twins DefaultEyes_Lucy
 with dissolve

 lucy "Oh, no! What if they already know about it?"

 show Twins DefaultEyes_Yvvy
 with dissolve

 yvvy "What if they are already coming?"

 hide Twins
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
