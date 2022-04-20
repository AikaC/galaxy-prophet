label route_02:

 hide BGGrandma
 hide star

 if extra == True:

  #play music "audio/YL.ogg" fadeout 1.0

  #show BGExtra
  show Yvvy at right
  with moveinright

  jump star

 else:
  show bgblack
  with dissolve

  jump meet_Paithyn
 return

label star:

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

 hide anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "..."

 #show Twins AngryEyes_Yvvy DefaultYvvy
 #with dissolve

 chY "{color=F4C2C2}\*sussurra\*{i}Tem certeza que devemos levar ela para a vovó Paithyn?"
 chY "{color=F4C2C2}\*sussurra\*{i}Ela bate com a segunda parte da-"

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

 hide anna
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

label castle_his:

 show Anna at trueright
 with moveinright

 anna "Como era lá?"

 hide anna
 show Lucy at left
 with moveinleft

 chL "Era bem pacífico."

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Não era?"

 #show Twins DefaultEyes_Yvvy
 #with dissolve

 chY "Nosso trabalho era deixar as coisas mais divertidas."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "De que forma?"

 hide Anna
 show Lucy at left
 with dissolve

 chL "Com música!"

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Quer ouvir?"

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "Sim!"

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Então você terá que nos visitar mais uma vez."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Estaremos esperando."

 hide Lucy

 jump meet_Paithyn
 return

label last_king:

 show Anna at trueright
 with moveinright

 anna "Vocês viam o último rei com frequência?"
 anna "Como ele era?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Não diga isso no passado!"

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "O rei ainda está vivo, só está preso."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Ainda nos falamos em segredo."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Ele é como um pai para nós."

 hide Lucy
 with dissolve
 
 jump meet_Paithyn
 return

label meet_Paithyn:

 #play music "audio/SWIntro.ogg" fadeout 1.0
 #queue  music "audio/SWLoop.ogg"

 $ extra == True

 show BGPaithynA
 show BGPaithynB
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Chegamos!"

 hide Lucy
 hide Yvvy
 #show PBody
 #show PHappy
 with dissolve

 chP "Yvvy, Lucy, há quanto tempo!"
 chP "Khaleesi me disse que você viriam."

 show Anna at trueright
 with dissolve

 anna "Quem?"

 hide Anna
 
 #hide PBody
 #hide PHappy
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Vovó."

 hide Lucy
 hide Yvvy
 #show PBody
 #show PHappy
 with dissolve

 chP "E você deve ser [anna]."
 chP "É um prazer te conhecer."

 show Anna at trueright
 with dissolve

 anna "Igualmente."

 hide Anna
 with dissolve

 chP "Khaleesi me disse que você quer voltar para casa."
 chP "Posso tentar te ajudar mas..."
 chP "Abrir um portal entre galáxias é bem complicado."
 chP "Você deverá coletar alguns ingredientes por conta própria."
 chP "Isso quer dizer que também iremos precisar da sua própria energia infundida nas plantas."

 show Anna at trueright
 with dissolve

 anna "Como eu faço isso?"

 hide Anna
 with dissolve

 chP "Essa parte é fácil, você só precisa passar um temp sozinha com os ingredientes."
 chP "O tempo que vai levar para coletar tudo e voltar aqui é o suficiente."

 show Anna at trueright
 with dissolve

 anna "Ok! Mole, mole!"

 hide Anna
 with dissolve

 chP "Bom!{w} Eu vou precisar destes ingredientes."
 #lista de ingredientes
 anna "O quê?"
 chP "Lucy e Yvvy terão que ficar."
 chP "Boa sorte!"

 show Anna at trueright
 with dissolve

 anna "Espera o que são es-{w} e se foram..."
 anna "Beleza! Hora de fazer as malas!"

 hide BGPaithynA
 hide BGPaithynB
 hide Anna
 with dissolve

 jump minion
 return
