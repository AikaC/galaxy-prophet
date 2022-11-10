label minion:

 play music "audio/chirp.ogg" fadeout 1.0

 show BGExtra
 with dissolve

 if key == True: 
    show Anna AScared AMA at trueright
    with moveinright

    anna "Vovó...?{w} Yvvy, Lucy? {w}Onde vocês estão?"
    $key = False
 if key == False:

    hide Anna

    show Braxton at left
    with hpunch

    chNull "Você..."

    hide Braxton
    show Anna AScared AMA at trueright
    with moveinright

    anna "Eu?"

    hide Anna
    show Braxton at left
    with dissolve

    chNull "Nunca te vi por aqui antes."

    hide Braxton
    show Anna AAwkward AMH at trueright
    with moveinright

    anna "Eu... estou só de visita."

    hide Anna
    show Braxton at left
    with dissolve

    chNull "Todos os visitantes devem se reportar-"
    chNull "!"
    chNull "Isso é..."
    if ancientDragon == True:
       chNull "Uhg... Minha cabeça."

       hide Braxton
       show Anna AAngry at trueright
       with dissolve

       anna "{color=F4C2C2}Espera um segundinho!"
       
       show Anna AScared at trueright
       with dissolve

       anna "{color=F4C2C2}Ele é... Braxton, o dragão ancião?"

       hide Anna
       show Braxton at left

    else:
       pass
 chNull "Venha comigo. Precisamos nos reportar à rainha."

 hide Braxton
 with dissolve

 menu:
    "Uh... Tá.":
       $ moral -= 10
       $ prision = False
       $ rei = False

       hide BGExtra
       with dissolve

       jump castle_TalkQueen
    "Fugir.":
       if extra == True:
          $ extra = False

          hide BGExtra
          with dissolve

          jump back_Paithyn
       if extra == False:
          $ prision = True
          jump prision
 return

label back_Paithyn:

 play music "audio/AnnaArp.ogg" fadeout 1.0
 queue music "audio/AnnaLoop.ogg"

 show BGPaithyn
 show PBody
 show PHappy
 show PMove at floating
 show screen noframe_secret
 with dissolve

 chP "Bem vinda de volta!"
 chP "Como foi?"

 hide PBody
 hide PHappy
 hide PMove
 hide screen noframe_secret
 show Anna AAwkward AMH at trueright
 with moveinright

 anna "Mole como gelatina!"

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Bom saber."

 hide PBody
 hide PHappy
 hide PMove
 show Lucy ClosedEyes_Lucy LML at trueleft
 with moveinleft

 chL "O caldeirão está pronto!"

 hide Lucy
 show CalBaixo at giragira
 show CalCima at truecenter
 with dissolve

 chY "Hora de mexer tudo!"

 hide CalBaixo
 hide CalCima
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Agora,{w} beba isso."
 chP "Como se sente?"

 hide PBody
 hide PHappy
 hide PMove
 show Anna AAngry AMA at trueright
 with dissolve

 anna "Eu sinto..."

 hide Anna
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chL "Se sente..."

 show Lucy DML at SilenceLeft
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with dissolve

 chY "Se sente..."

 hide Yvvy
 hide Lucy
 show Anna AScared AMA at trueright
 with dissolve

 anna "Nada."

 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chYL "Ugh..."

 hide Yvvy
 hide Lucy
 show Anna AScared AMA at trueright
 with dissolve

 anna "Como isso deveria funcionar?"

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Esse chá é feito com ingredientes mágicos de propriedades dos sonhos..."
 chP "Era para você ter tido um sonho lúcido da sua casa,"
 chP "Assim eu conseguiria lançar um feitiço e te mandar para casa."
 chP "Se o chá não funcionou,"
 chP "... quer dizer que uma energia poderosa está te mantendo aqui."
 chP "Como você chegou aqui?"

 hide PBody
 hide PHappy
 hide PMove
 show Anna AScared AMA at trueright
 with dissolve

 anna "Não faço ideia."

 hide Anna
 show PBody
 show PHappy
 show PMove at floating
 with dissolve

 chP "Vamos achar alguma solução."
 chP "A má notícia para você é que..."
 chP "Se você não consegue volta usando o meu poder..."
 chP "Isso quer dizer quer você é parte da profecia de alguma forma."

 hide PBody
 hide PHappy
 hide PMove
 show Yvvy ScaredEyes_Yvvy LMY at trueright
 with dissolve

 chY "De volta à vovó pelo que parece!"

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy LML at trueleft
 with dissolve

 chL "Parece que você se prendeu com a gente por um tempo, [anna]!"

 hide Lucy
 hide Yvvy
 hide BGPaithyn
 show star
 show BGGrandma
 with dissolve

 $intel += 1

 show GBody at left
 show GHappy at left
 with moveinleft

 chG "Olá, como foi a jornada?"

 hide GBody
 hide GHappy
 show Lucy AngryEyes_Lucy AML at trueleft
 with moveinleft

 chL "Nada de novo..."
 
 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve
 
 chY "Entediante..."
 
 hide Yvvy
 hide Lucy
 show Anna AScared AMA at trueright
 with moveinright

 anna "O feitiço não funcionou."
 anna "A senhora Paithyn disse que era porque eu faço parte da profecia."
 
 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Entendo..."
 
 hide GBody
 hide GAngry
 show Anna AAwkward AMA at trueright
 with dissolve

 anna "E também me encontrei com alguém enquanto colhia os ingredientes."
 
 hide Anna
 show Yvvy AngryEyes_Yvvy AMY at trueright
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chYL "Quem?"
 
 hide Yvvy
 hide Lucy
 show Anna AScared AMA at trueright
 with dissolve

 if ancientDragon == True:
  anna "Braxton."
  pass
 else:
  anna "Alguém que trabalhava para a rainha."
  
  hide Anna
  show Yvvy ScaredEyes_Yvvy AMY at trueright
  with dissolve

  chY "Oh não! Só pode ser uma criatura."
  
  show Yvvy DMY at SilenceRight
  show Lucy AngryEyes_Lucy AML at trueleft
  with dissolve

  chL "Como ele era?"
  
  hide Lucy
  hide Yvvy
  show Anna AScared AMA at trueright
  with dissolve

  anna "Um guarda de cabelo comprido e olhos assustadores."
  
  hide Anna
  show Yvvy ScaredEyes_Yvvy AMY at trueright
  show Lucy ScaredEyes_Lucy AML at trueleft
  with dissolve

  chYL "É o Braxton!"
  
  hide Yvvy
  hide Lucy
  with dissolve

  pass
 
 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with dissolve

 chY "Por que não nos disse isso antes?"
 
 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chL "Ou melhor! O que {i}você{/i} disse para {i}ele?{/i}"
 
 hide Lucy
 hide Yvvy
 show Anna AAngry AMA at trueright
 with dissolve

 anna "Nada... Eu só fugi."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Agora que ele te viu, nossa melhor escolha é te mandar para Ivan imediatamente."
 
 hide GBody
 hide GAngry
 show Yvvy ClosedEyes_Yvvy LMY at trueright
 with dissolve

 chY "Partiu!"

 show Yvvy DMY at SilenceRight
 show Lucy ClosedEyes_Lucy LML at trueleft
 with dissolve

 chL "Para o vovô!"

 hide Lucy
 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Não dessa vez.{w} Preciso de vocês duas aqui."
 
 hide GBody
 hide GAngry
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chY "Booo..."

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chL "Sem graça!"
 
 hide Lucy
 hide Yvvy
 show GBody at left
 show GHappy at left
 with dissolve

 chG "[anna] pode ir sozinha. Não é longe daqui e o caminho é tão seguro quanto o templo secreto."
 
 hide GBody
 hide GHappy
 show Anna AScared AMH at trueright
 with dissolve

 anna "Tudo bem. Vejo vocês mais tarde!"
 
 hide BGGrandma
 hide star
 hide Anna
 with dissolve

 jump training
 return
