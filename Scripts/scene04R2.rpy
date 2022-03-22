label route_02:

 if extra == True:

  #play music "audio/YL.ogg" fadeout 1.0

  #show BGExtra
  #show Twins ClosedMouth_Lucy
  #with dissolve

  jump star

 else:
  #show bgblack
  #hide BGGrandma
  #with dissolve

  jump meet_Paithyn
 return

label star:

 chY "Ei, [anna]."

 #show Twins ClosedMouth_Yvvy
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Sim?"

 #show Twins DefaultLucy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chL "De onde você é?"

 #show Twins ClosedMouth_Lucy
 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Bem, eu sou da Terra."

 #show Twins DefaultYvvy
 #show Anna ACMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chY "Terra? {w}Nunca ouvi falar."

 #show Twins DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Que tipo de estrela é essa? {w}É muito longe?"

 #show Twins ClosedMouth_Lucy
 #show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Estrela?! Estamos em uma estrela?!"

 #show Twins ClosedHappyEyes_Yvvy DefaultYvvy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chY "Claro que sim, bobinha."

 #show Twins ClosedHappyEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Onde mais poderíamos estar?"

 #show Twins ClosedMouth_Lucy
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Em um planeta…?"

 #show Twins DefaultEyes_Lucy DefaultEyes_Yvvy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chYL "..."

 #show Twins AngryEyes_Yvvy DefaultYvvy
 #with dissolve

 chY "{color=F4C2C2}*sussurra*{i}Tem certeza que devemos levar ela para a vovó Paithyn?"
 chY "{color=F4C2C2}*sussurra*{i}Ela bate com a segunda parte da-"

 #show Twins AngryEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "*sussurra*{color=F4C2C2}{i}Shh… {w}Ela vai te ouvir!"
 chL "*sussurra*{color=F4C2C2}{i}Vamos so fazer o que a vovó pediu primeiro."

 #show Twins ClosedMouth_Lucy
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Ahh… Alô...?"

 #show Twins DefaultEyes_Yvvy DefaultYvvy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chY "É…{w} Um planeta.{p}Já ouvi falar antes…"

 #show Twins DefaultEyes_Lucy DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "É bem longe daqui. "

 #show Twins DefaultYvvy ClosedMouth_Lucy
 #with dissolve

 chY "Centenas de galáxias distantes."

 #show Twins ClosedMouth_Yvvy
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "E onde estamos?"

 #show Twins ClosedHappyEyes_Lucy DefaultLucy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chL "Galáxia M-13."

 #show Twins ClosedMouth_Lucy
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Longe assim?!"

 #show Twins ClosedHappyEyes_Yvvy DefaultYvvy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chY "Você conhece esse lugar?"

 #show Twins DefaultEyes_Lucy DefaultEyes_Yvvy ClosedMouth_Yvvy
 #show Anna AEyes_Happy AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "A gente chama aqui de galáxia de Andrômeda."
 anna "Lucy, Yvvy"

 #show Twins DefaultLucy DefaultYvvy
 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chYL "Yes?"

 #hide Twins
 #hide Anna onlayer over_screens
 #window hide
 #with dissolve

menu:
 "Vocês trabalharam no castelo?":
  window show
  jump castle
 "Falem mais sobre o rei.":
  window show
  jump last_king
 "Deixa para lá...":

  #window show
  #show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
  # size (245,318.5)
  # left
  #with dissolve

  anna "Vamos continuar."

  #hide Anna onlayer over_screens
  #with dissolve

  jump meet_Paithyn
 
  return

label castle:

 #show Anna AOMouth_Worried onlayer over_screens:
 #size (245,318.5)
 #left
 #with dissolve

 #anna "You worked in the castle?"
 anna "Como era lá?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins
 #with dissolve

 chL "Era bem pacífico."

 #show Twins ClosedHappyEyes_Yvvy
 #with dissolve

 chY "Não era?"

 #show Twins DefaultEyes_Yvvy
 #with dissolve

 chY "Nosso trabalho era deixar as coisas mais divertidas."

 #show Anna AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "De que forma?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins ClosedHappyEyes_Lucy LaughingLucy
 #with dissolve

 chL "Com música!"

 #show Twins ClosedHappyEyes_Yvvy LaughingYvvy
 #with dissolve

 chY "Quer ouvir?"

 #show Twins ClosedMouth_Lucy ClosedMouth_Yvvy
 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Sim!"

 #show Anna AEyes_Tedio ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins DefaultEyes_Yvvy DefaultYvvy
 #with dissolve

 chY "Então você terá que nos visitar mais uma vez."

 #show Twins DefaultEyes_Lucy DefaultLucy
 #with dissolve

 chL "Estaremos esperando."

 #hide Twins
 #hide Anna onlayer over_screens
 #window hide
 #with dissolve

 jump meet_Paithyn
 return

label last_king:

 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Vocês viam o último rei com frequência?"
 anna "Como ele era?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins AngryEyes_Yvvy AngryEyes_Lucy
 #with dissolve

 chY "Não diga isso no passado!"
 chl "O rei ainda está vivo, só está preso."
 chY "Ainda nos falamos em segredo."
 chL "Ele é como um pai para nós."

 #hide Twins
 #hide Anna onlayer over_screens
 #window hide
 #with dissolve
 
 jump meet_Paithyn
 return

label meet_Paithyn:

 #play music "audio/SWIntro.ogg" fadeout 1.0
 #queue  music "audio/SWLoop.ogg"

 $ extra == True

 #show BGPaithyn
 #hide BGGrandma
 #show Twins
 #with dissolve

 chYL "Chegamos."

 #hide Twins
 #show PBody
 #show PHappy
 #with dissolve

 chP "Há quanto tempo."
 chP "Khaleesi me disse que você viriam."

 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Quem?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 
 #hide PBody
 #hide PHappy
 #show Twins
 #with dissolve

 chYL "Vovó."

 #hide Twins
 #show PBody
 #show PHappy
 #with dissolve

 chP "E voce deve ser [anna]."
 chP "É um prazer te conhecer."

 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Igualmente."

 #show Anna ACMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 chP "Khaleesi me disse que você quer voltar para casa."
 chP "Posso tentar te ajudar mas..."
 chP "Abrir um portal entre galáxias é bem complicado."
 chP "Voce deverá coletar alguns ingredientes por conta própria."
 chP "Isso rque também iremos precisar da sua própria energia infundida nas plantas."
 anna "Como eu faço isso?"
 chP "Essa parte é fácil, você só precisa passar um temp sozinha com os ingredientes."
 chP "O tempo que vi levar para oletar tudo e voltar aqui é o suficiente."
 anna "Ok! Mole, mole!"
 chP "Bom!{w} Eu vou precisar destes ingredientes."
 #lista de ingredientes
 anna "O quê?"
 chP "Lucy e Yvvy terão que ficar."
 chP "Boa sorte!"
 anna "Espera o que são es-{w} e se foram..."
 anna "Belza! Hora de fazer as malas!"

 #jump minion
 return
