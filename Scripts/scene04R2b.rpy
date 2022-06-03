label castle_his:

 show Anna at trueright
 with moveinright

 anna "Como era lá?"

 hide Anna
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