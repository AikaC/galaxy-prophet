label minion:
 if key == True:
  
  show Anna at trueright
  with moveinright

  anna "Vovó...?{w} Yvvy, Lucy? {w}Onde vocês estão?"
  $key = False
 if key == False:

  hide Anna

  #anna se esbarra com o minion/efeito de tela tremendo
  chNull "Você..."

  show Anna at trueright
  with moveinright

  anna "Eu?"

  hide Anna
  with dissolve

  chNull "Nunca te vi por aqui antes."

  show Anna at trueright
  with moveinright

  anna "Eu... estou só de visita."

  hide Anna
  with dissolve

  chNull "Todos os visitantes devem se reportar-"
  chNull "!"
  chNull "Isso é..."
  if ancientDragon = True:
   chNull "Uhg... Minha cabeça."

   show Anna at trueright
   with moveinright

   anna "{color=F4C2C2}Espera um segundinho!"
   anna "{color=F4C2C2}Ele é... Braxton, o dragão ancião?"

   hide Anna
   with dissolve

  else:
   pass
  chNull "Venha comigo. Precisamos nos reportar à rainha."

 menu:
  "Uh... Tá.":
   $ moral -= 10
   $ prision = False
   $ rei = False
   jump castle_TalkQueen
  "Fugir.":
   if extra == True:
    $ extra = False
    jump back_Paithyn
   if extra == False:
    $ prision = True
    jump prision
 return

label back_Paithyn:

 show BGPaithynA
 show BGPaithynB
 with dissolve

 chP "Bem vinda de volta!"
 chP "Como foi?"

 show Anna at trueright
 with moveinright

 anna "Mole como gelatina!"

 hide Anna
 with dissolve

 chP "Bom saber."

 show Lucy at left
 with moveinleft

 chL "O caldeirão está pronto!"

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Hora de mexer tudo!"

 hide Yvvy

 #cutscene caldeirao, ingredientes girando
 chP "Agora,{w} beba isso."
 chP "Como se sente?"

 show Anna at trueright
 with dissolve

 anna "Eu sinto..."

 hide Anna
 show Lucy at left
 with dissolve

 chL "Se sente..."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Se sente..."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "nada"

 hide Anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Ugh..."

 hide Yvvy
 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Como isso deveria funcionar?"

 hide Anna
 with dissolve

 chP "Esse chá é feito com ingredientes mágicos de propriedades dos sonhos..."
 chP "Era para você ter tido um sonho lúcido da sua casa,"
 chP "Assim eu conseguiria lançar um feitiço e te mandar para casa."
 chP "Se o chá não funcionou,"
 chP "... quer dizer que uma energia poderosa está te mantendo aqui."
 chP "Como você chegou aqui?"

 show Anna at trueright
 with dissolve

 anna "Não faço ideia."

 hide Anna
 with dissolve

 chP "Vamos achar alguma solução."
 chP "A má notícia para você é que..."
 chP "Se você não consegue volta usando o meu poder..."
 chP "Isso quer dizer quer você é parte da profecia de alguma forma."

 show Yvvy at right
 with dissolve

 chY "De volta à vovó pelo que parece!"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Parece que você se prendeu com a gente por um tempo, [anna]!"

 hide Lucy
 show BGGrandma
 hide BGPaithyn
 with dissolve

 $intel += 1
 chG "Olá, como foi a jornada?"
 chL "Nada de novo..."
 chY "Entediante..."
 anna "O feitiço não funcionou."
 anna "A senhora Paithyn disse que era porque eu faço parte da profecia."
 chG "Entendo..."
 anna "E também me encontrei com alguém enquanto colhia os ingredientes."
 chYL "Quem?"
 if ancientDragon == True:
  anna "Braxton."
  pass
 else:
  anna "Alguém que trabalhava para a rainha."
  chY "Oh não! Só pode ser uma criatura."
  chL "Como ele era?"
  anna "Um guarda de cabelo comprido e olhos assustadores."
  chYL "É o Braxton!"
  pass
 chY "Por que não nos disse Isso antes?"
 chL "Ou melhor! O que {i}você{/i} disse para {i}ele?{/i}"
 anna "Nada... Eu só fugi."
 chG "Agora que ele te viu, nossa melhor escolha é te mandar para Ivan imediatamente."
 chY "Partiu!"
 chL "Para o vovô!"
 chG "Não dessa vez.{w} Preciso de vocês duas aqui."
 chY "Booo..."
 chL "Sem graça!"
 chG "[anna] pode ir sozinha. Não é longe daqui e o caminho é tão seguro quanto o templo secreto."
 anna "Tudo bem. Vejo vocês mais tarde!"
 
 hide BGGrandma
 with dissolve
 jump training
 return
