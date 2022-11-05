label castle_his:

 show Anna AHappy AMH at trueright
 with moveinright

 anna "Como era lá?"

 hide Anna
 show Lucy ScaredEyes_Lucy LML at trueleft
 with moveinleft

 chL "Era bem pacífico."

 show Lucy DML at SilenceLeft
 show Yvvy ClosedEyes_Yvvy LMY at trueright
 with dissolve

 chY "Não era?"

 show Yvvy FaceYvvy at trueright with dissolve

 chY "Nosso trabalho era deixar as coisas mais divertidas."

 hide Yvvy
 hide Lucy
 show Anna AMH at trueright
 with dissolve

 anna "De que forma?"

 hide Anna
 show Lucy LML ClosedEyes_Lucy at trueleft
 with dissolve

 chL "Com música!"

 show Lucy DML at SilenceLeft
 show Yvvy LMY ClosedEyes_Yvvy at trueright
 with dissolve

 chY "Quer ouvir?"

 hide Yvvy
 hide Lucy
 show Anna AHappy AMH at trueright
 with dissolve

 anna "Sim!"

 hide Anna
 show Yvvy LMY at trueright
 with dissolve

 chY "Então você terá que nos visitar mais uma vez."

 show Yvvy DMY at SilenceRight
 show Lucy LML at trueleft
 with dissolve

 chL "Estaremos esperando."

 hide Lucy

 jump meet_Paithyn
 return

label last_king:

 show Anna AMA at trueright
 with moveinright

 anna "Vocês viam o último rei com frequência?"
 anna "Como ele era?"

 hide Anna
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with moveinright

 chY "Não diga isso no passado!"

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chL "O rei ainda está vivo, só está preso."

 show Lucy DML at SilenceLeft
 show Yvvy AMY at TalkingRight

 chY "Ainda nos falamos em segredo."

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at TalkingLeft

 chL "Ele é como um pai para nós."

 hide Lucy
 hide Yvvy
 with dissolve
 
 jump meet_Paithyn
 return

label meet_Paithyn:

 $ extra == True

 show BGPaithyn
 show Yvvy LMY at trueright
 show Lucy LML at trueleft
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
 show Anna AMA at trueright
 with dissolve

 anna "Quem?"

 hide Anna
 show Yvvy AMY at trueright
 show Lucy AML at trueleft
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
 show Anna AHappy AMH at trueright
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
 show Anna AMA at trueright
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
 show Anna AHappy AMH at trueright
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
 show Anna AScared AMA at trueright
 with dissolve

 anna "Espera o que é is-{w} e se foram..."

 show Anna AHappy AMH at trueright

 anna "Beleza! Hora de fazer as malas!"

 $key = False
 $ancientDragon = False

 hide BGPaithyn
 hide Anna
 with dissolve

 call screen colheita
 return
