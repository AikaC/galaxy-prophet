label route_02:

 hide BGGrandma
 hide star

 if extra == True:

  show BGExtra
  show Yvvy at right
  with dissolve

  jump star

 else:
  show bgblack
  with dissolve

  jump meet_Paithyn
 return

label star:

 stop music fadeout 1.0

 play music "audio/SWIntro.ogg"
 queue  music "audio/SWLoop.ogg"

 chY "Ei, [anna]."

 hide Yvvy
 show Anna at trueright
 with moveinright

 anna "Sim?"

 hide Anna
 show Lucy at left
 with moveinleft

 chL "De onde você é?"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Bem, eu sou da Terra."

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Terra? {w}Nunca ouvi falar."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Que tipo de estrela é essa? {w}É muito longe?"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Estrela?! Estamos em uma estrela?!"

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Claro que sim, bobinha."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Onde mais poderíamos estar?"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Em um planeta...?"

 hide Anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "..."

 #show Twins AngryEyes_Yvvy DefaultYvvy
 #with dissolve

 chY "\*sussurra\*{color=F4C2C2}{i}Tem certeza que devemos levar ela para a vovó Paithyn?"
 chY "\*sussurra\*{color=F4C2C2}{i}Ela bate com a segunda parte da-"

 #show Twins AngryEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "\*sussurra\*{color=F4C2C2}{i}Shh... {w}Ela vai te ouvir!"
 chL "\*sussurra\*{color=F4C2C2}{i}Vamos só fazer o que a vovó pediu primeiro."

 hide Yvvy
 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Ahh... Alô...?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "É...{w} Um planeta.{p}Já ouvi falar antes..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "É bem longe daqui. "

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Centenas de galáxias distantes."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "E onde estamos?"

 hide Anna
 show Lucy at left with dissolve

 chL "Galáxia M-13."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Longe assim?!"

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Você conhece esse lugar?"

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "A gente chama aqui de galáxia de Andrômeda."
 anna "Lucy, Yvvy"

 hide Anna
 show Lucy at left
 show Yvvy at right
 with dissolve

 chYL "Sim?"

 hide Lucy
 hide Yvvy
 with dissolve

menu:
 "Vocês trabalharam no castelo?":
  jump castle_his
 "Falem mais sobre o rei.":
  jump last_king
 "Deixa para lá...":

  show Anna at trueright
  with moveinright

  anna "Vamos continuar."

  hide Anna
  with dissolve

  jump meet_Paithyn
 
  return


 $ extra == True

 show BGPaithyn
 show Yvvy at right
 show Lucy at left
 with dissolve

 stop music fadeout 1.0

 play music "audio/AnnaArp.ogg"
 queue  music "audio/AnnaLoop.ogg"

 chYL "Chegamos!"

 hide Lucy
 hide Yvvy
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Yvvy, Lucy, há quanto tempo!"
 chP "Khaleesi me disse que você viriam."

 hide PBody
 hide PHappy
 hide PMove
 show Anna at trueright
 with dissolve

 anna "Quem?"

 hide Anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Vovó."

 hide Lucy
 hide Yvvy
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "E você deve ser [anna]."
 chP "É um prazer te conhecer."

 hide PBody
 hide PHappy
 hide PMove
 show Anna at trueright
 with dissolve

 anna "Igualmente."

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Khaleesi me disse que você quer voltar para casa."
 chP "Posso tentar te ajudar mas..."
 chP "Abrir um portal entre galáxias é bem complicado."
 chP "Você deverá coletar um ingrediente por conta própria."
 chP "Isso quer dizer que também iremos precisar da sua própria energia infundida na planta."

 hide PBody
 hide PHappy
 hide PMove
 show Anna at trueright
 with dissolve

 anna "Como eu faço isso?"

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Essa parte é fácil, você só precisa passar um temp sozinha com o ingrediente."
 chP "O tempo que vai levar para coletar tudo e voltar aqui é o suficiente."

 hide PBody
 hide PHappy
 hide PMove
 show Anna at trueright
 with dissolve

 anna "Ok! Mole, mole!"

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Bom!{w} Eu vou precisar de um ingrediente raro."

 hide PBody
 hide PHappy
 hide PMove
 show ingrediente at truecenter
 with dissolve

 anna "O quê?"

 hide ingrediente
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Lucy e Yvvy terão que ficar."
 chP "Boa sorte!"

 hide PBody
 hide PHappy
 hide PMove
 show Anna at trueright
 with dissolve

 anna "Espera o que é is-{w} e se foram..."
 anna "Beleza! Hora de fazer as malas!"

 $key = False
 $ancientDragon = False

 hide BGPaithyn
 hide Anna
 with dissolve

 call screen colheita
 return
