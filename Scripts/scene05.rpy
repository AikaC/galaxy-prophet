label minion:
 if key == True:
  ana "Grandma...?{w} Yvvy, Lucy? {w}Where are you?"
  $key = False
 if key == False:
  #anna se esbarra com o minion/efeito de tela tremendo
  c "You..."
  anna "Me?"
  c "I've never seen you around before."
  anna "I'm... just a visitor."
  c "Any new visitors must report-"
  c "!"

  window hide
  show Colar at colar_foco onlayer over_screens
  with dissolve
  pause

  hide Colar onlayer over_screens
  window show

  c "That is..."
  if ancientDragon = True:
   c "Uhg... My head."
   anna "{color=F4C2C2}Hold on a minute!"
   anna "{color=F4C2C2}Is he... Braxton, the ancient dragon?"
   $ ancientDragon == False
  else:
   pass
  c "Come with me. We need to report to the queen."

 menu:
  "Uh... sure.":
   $ moral -= 10
   jump castle_TalkQueen
  "Run away.":
   if extra = True:
    $ extra == False
    jump back_Paithyn
   if extra = False:
    jump prision
 return

label back_Paithyn:

 paithyn "Welcome back!"
 paithyn "How was it?"
 anna "Easy Peasy!"
 paithyn "Good to know."
 #lucy "The caldron is ready!
 yvvy "Time to mix everything!"
 #cutscene caldeirao, ingredientes girando
 paithyn "Now,{w} drink this."
 paithyn "How do you feel?"
 anna "I feel..."
 lucy "You feel..."
 yvvy "You feel..."
 anna "nothing"
 yl "Ugh..."
 anna "How was it supposed to work?"
 paithyn "This tea is made with magical ingredients with dreamy properties..."
 paithyn "You were supposed to dream vividly about your home,"
 paithyn "so I would be able to cast a spell and send you back."
 paithyn "If the tea didn't work,"
 paithyn "That means a powerful energy is keeping you here."
 paithyn "How did you come here?"
 anna "I have no idea."
 anna "Sorry..."
 paithyn "You don't need to be."
 paithyn "We will find a way somehow."
 paithyn "The bad news is..."
 paithyn "If you can't go back now with my power..."
 paithyn "That probably means that you're somehow part of the prophecy."
 yvvy "Back to grandma, it seems!"
 lucy "You're stuck with us for a little while [anna]!"

 show BGGrandma
 hide BGPaithyn
 with dissolve

 $intel = 1
 grandma "Hello, how was the journey?"
 lucy "Nothing new..."
 yvvy "Boring..."
 anna "The spell did'nt work."
 anna "Miss Paithyn said it was likely because of the prophecy."
 grandma "I see..."
 anna "I also saw someone while picking the ingredients"
 yl "Who?"
 if ancientDragon = True:
  anna "Braxton."
  $ ancientDragon == False
  pass
 else:
  anna "Someone who worked for the queen."
  yvvy "Oh no! It can be just one creature"
  lucy "How was he like?"
  anna "A guard with long hair and scary eyes."
  yl "That's Braxton!"
  pass
 yvvy "Why haven't you told us that?"
 lucy "Better! What have {i}you{/i} told {i}him?{/i}"
 anna "Nothing... I just run away."
 grandma "Our better choice now that he saw you is sending you to Ivan."
 yvvy "Off we go!"
 lucy "To grandpa!"
 grandma "Not this time.{w} I need you both here."
 yvvy "Booo..."
 lucy "Not fun!"
 grandma "[anna] can go on her own. Is not far away and the road is as safe as the ancient tree."
 anna "Alright. See you soon!"
 
 jump training

 return
