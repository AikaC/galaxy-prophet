label minion:
 if key = True:
  anna "Vovó...?{w} Yvvy, Lucy? {w}Onde vocês estão?"
  $key == False
 if key = False:
  #anna se esbarra com o minion/efeito de tela tremendo
  chNull "Você..."
  anna "Eu?"
  chNull "Nunca te vi por aqui antes."
  anna "Eu... estou só de visita."
  chNull "Todos os visitantes devem se reportar-"
  chNull "!"
  chNull "Isso é..."
  if ancientDragon = True:
   chNull "Uhg... Minha cabeça."
   anna "{color=F4C2C2}Espera um segundinho!"
   anna "{color=F4C2C2}Ele é... Braxton, o dragão ancião?"
   $ ancientDragon == False
  else:
   pass
  chNull "Venha comigo. Precisamos nos reportar à rainha."

 menu:
  "Uh... Tá.":
   $ moral -= 10
   jump castle_TalkQueen
  "Fugir.":
   if extra = True:
    $ extra == False
    jump back_Paithyn
   if extra = False:
    jump prision
 return

label back_Paithyn:

 chP "Bem vinda de volta!"
 chP "Como foi?"
 anna "Mole como gelatina!"
 chP "Bom saber."
 chL "O caldeirão está pronto!
 chY "Hora de mexer tudo!"
 #cutscene caldeirao, ingredientes girando
 chP "Agora,{w} beba isso."
 chP "Como se sente?"
 anna "Eu sinto..."
 chL "Se sente..."
 chY "Se sente..."
 anna "nada"
 chYL "Ugh..."
 anna "Como isso deveria funcionar?"
 chP "Esse chá é feito com ingredientes mágicos de propriedades dos sonhos..."
 chP "Era para você ter tido um sonho lúcido da sua casa,"
 chP "Assim eu conseguiria lançar um feitiço e te mandar para casa."
 chP "Se o chá não funcionou,"
 chP "... quer dizer que uma energia poderosa está te mantendo aqui."
 chP "Como você chegou aqui?"
 anna "Não faço ideia."
 chP "Vamos achar alguma solução."
 chP "A má notícia para você é que..."
 chP "Se você não consegue volta usando o meu poder..."
 chP "Isso quer dizer quer você é parte da profecia de alguma forma."
 chY "De volta à vovó pelo que parece!"
 chL "Parece que você se prendeu com a gente por um tempo, [anna]!"

 show BGGrandma
 #hide BGPaithyn
 #with dissolve

 $intel == 1
 chG "Olá, como foi a jornada?"
 chL "Nada de novo..."
 chY "Entediante..."
 anna "O feitiço não funcionou."
 anna "A senhora Paithyn disse que era porque eu faço parte da profecia."
 chG "Entendo..."
 anna "E também me enconrei com lguém enquanto colhia os ingredientes."
 chYL "Quem?"
 if ancientDragon = True:
  anna "Braxton."
  $ ancientDragon == False
  pass
 else:
  anna "Alguém que trabalhava para a rainha."
  chY "Oh não! Só pode ser uma criatura."
  chL "Como ele era?"
  anna "Um guarda de cabelo comprido e olhos assustadores."
  chYL "É o Braxton!"
  pass
 chY "Por que não nos disse isse antes?"
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
 
 #jump training

 return
