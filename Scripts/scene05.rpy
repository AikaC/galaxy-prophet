label minion:
 if key == True
  ana "Grandma...?{w} Yvvy, Lucy? {w}Where are you?"
  $key = False
 if key == False
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
  if ancientDragon = True
   c "Uhg... My head."
   anna "{color=F4C2C2}Hold on a minute!"
   anna "{color=F4C2C2}Is he... Braxton, the ancient dragon?"
   $ ancientDragon == False
  elif pass
  c "Come with me. We need to report to the queen."

 menu:
  "Uh... sure.":
   $ moral -= 10
   jump castle_TalkQueen
  "Run away.":
   if extra = True
    $ extra == False
    jump back_Paithyn
   if extra = False
    jump prision
 return

label back_Paithyn:

 return