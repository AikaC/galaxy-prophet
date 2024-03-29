label prophecy:

 show Anna AMA at trueright
 with dissolve

 anna "Obrigada por me soltarem."

 hide Anna
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chL "Ainda estamos de olho."

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chY "Você é muito suspeita."

 hide Lucy
 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Lucy, Yvvy. {i}A garota{/i} é uma convidada agora."
 chG "Por favor, comportem-se."

 hide GBody
 hide GAngry
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chYL "Sim, vovó..."

 hide Yvvy
 hide Lucy
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Então, {i}garota{/i}-"
 
 hide GBody
 hide GHappy
 show Anna AMA at trueright
 with dissolve

 anna "[anna]."

 hide Anna
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chY "Você é uma \“garota\” ou uma \“[anna]\”?"

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chL "Poderia, por favor se decidir, {i}querida convidada?{/i}"

 hide Lucy
 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "..."

 hide GBody
 hide GAngry
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chYL "Desculpa, vovó..."

 hide Yvvy
 hide Lucy
 show GBody
 show GHappy
 with dissolve

 chG "Então... [anna]."

 stop music fadeout 1.0

 hide GBody
 hide GHappy
 hide screen noframe_moral
 with dissolve

 #cutscene start

 play music "audio/CutsceneIntro.ogg"
 queue music "audio/CutsceneLoop.ogg"

 show BGctscn01 at zoom
 with fade

 chG "Incontáveis eras atrás quando ainda não tinha muito o que ver por aqui..."
 chG "Um ser brilhante apareceu durante uma noite sem lua e disse..."

 show seirei at floating
 with zoomin

 chNull "Uma era sombria está por vir.{p}Chame o salvador desse lar.{p}Lute contra a loucura que uma vez ajudou{p}Certo viajante sob uma pedra."

 hide seirei
 with zoomout

 chG "Antes que sequer pudéssemos reagir, uma luz nos cegou."

 show BGctscn01
 with flashbulb

 chG "E a árvore sagrada a pareceu naquele mesmo lugar."

 show TreeCtscn
 with zoomin

 chG "Como se ela sempre estivesse lá."
 chG "Tentamos perguntar o significado de tudo aquilo."

 hide BGctscn01
 hide TreeCtscn
 show arvore brilha at move
 with fade

 chG "Feiticeiros e fadas vieram de longe tentar ajudar."
 chG "Mas nada mais aconteceu."
 chG "Então decidimos esperar."

 hide arvore brilha
 show BGctscn01
 show Templectscn
 with fade

 chG "Famílias começaram a crescer, {w}clãs se tornaram vilas..."

 show BGctscn02
 with dissolve

 chG "reinos foram trazidos à vida, {w}mas a árvore continuou em silêncio."
 chG "Quando estávamos quase desistindo... {w}Um novo sinal apareceu."

 hide BGctscn02
 hide Templectscn
 hide BGctscn01
 hide BGGrandma
 show Colar at truecenter
 with dissolve

 pause 1.0

 stop music fadeout 1.0
 hide Colar
 
 with dissolve
 #cutscene end
 
 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"

 show screen noframe_moral
 show BGGrandma
 show GBody at left
 show GAngry at left
 with fade

 chG "Não muito tempo depois, descobrimos que nosso reino possuía uma nova soberana que tomou o lugar do antigo rei."
 chG "Eu não posso ir muito longe da árvore já que os guardiões lincaram a energia vital com o templo secreto."

 hide GAngry
 show GHappy at left

 chG "Mas isso é história para outro dia."

 hide GHappy
 show GAngry at left

 chG "Vai nos ajudar?"

 hide GBody
 hide GAngry
 with dissolve

 menu:
  "Como pode ter tanta certeza?":
   $extra = True
   jump so_sure
  "Sim":
   jump yhelp
  "Não":
   $moral -= 10
   jump nhelp
 return

label so_sure:

 show Anna AScared AMA at trueright
 show screen noframe_special
 with dissolve

 anna "Apesar dessa coincidência de tempo, não vejo a relação da rainha com a profecia."
 anna "Há quanto tempo ela reina aqui?"

 hide Anna
 hide screen noframe_special
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with moveinright

 chY "Meia geração até agora..."

 hide Yvvy
 show Anna AMA at trueright
 with dissolve

 anna "Ela já fez algo de ruim {b}depois{/b} de pegar a coroa?"

 hide Anna
 show Lucy ScaredEyes_Lucy AML at trueleft
 with moveinleft

 chL "Ainda não..."

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chY "Aprisionar o rei já não é ruim o bastante?"

 hide Yvvy
 hide Lucy
 show Anna AScared AMA at trueright
 with dissolve

 anna "É... {w}Mas eu não vejo um período sombrio saindo só disso."

 hide Anna
 show Yvvy LMY at trueright
 show Lucy LML at trueleft
 with dissolve

 chYL "Isso nós podemos explicar."

 show Yvvy DMY at SilenceRight

 chL "Nós servíamos ao antigo rei, então estávamos lá quando tudo aconteceu."

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at TalkingRight

 chY "Mas ainda não sabemos como a rainha Selyna e aquela criatura terrível terminaram juntos."

 hide screen noframe_moral
 hide Yvvy
 hide Lucy
 with dissolve

 stop music fadeout 1.0

 #cutscene start

 play music "audio/CutsceneIntro.ogg"
 queue music "audio/CutsceneLoop.ogg"

 show Castle01
 with dissolve

 chL "Tudo começou com um ataque surpresa."
 chY "E vou te falar, a gente ficou mesmo supreendido."
 chL "Verdade, irmã. Nem um pouco legal."

 show Silhueta at zoom
 with dissolve

 chY "Não sei como alguém de fora fez um acordo com uma criatura tão temível,"
 chY "mas a atual rainha e o dragão ancião conseguiram conquistar o castelo em pouco tempo."

 show Silhueta at desaparece

 chL "Não estávamos tão protegidos assim..."
 chY "... já que não é comum entrar na casa dos outros..."
 chL "... Ou castelo dos outros, sem ser convidado."

 hide Castle01
 show BGCastle
 with dissolve

 chY "Eu e Lucy conseguimos nos esconder a tempo,"

 show Silhueta2
 with dissolve

 chL "Mas ouvimos tudo... {w=0.5}Ou quase..."

 show Silhueta3
 with dissolve

 chY "Nós não conseguimos ouvir direito..."

 chS "... tempo... {w=0.2}sentiu saudades?"
 chS "... lembranças... {w=0.2}minha irmã."

 hide Silhueta2
 hide Silhueta3
 hide BGCastle
 with dissolve

 #cutscene end

 stop music fadeout 1.0
 
 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"

 show screen noframe_moral
 show Lucy ScaredEyes_Lucy AML at trueleft
 with moveinleft

 chL "Parece que a rainha Selyna e o antigo rei já se conheciam."

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chY "Mas isso não seria uma surpresa."

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at TalkingLeft

 chL "Verdade.{p}O antigo rei costumava andar muito por outras galáxias."

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at TalkingRight

 chY "Não sabemos como, antes que você pergunte."

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at TalkingLeft

 chL "A rainha Selyna com certeza fez aquilo por vingança."

 show Lucy DML at SilenceLeft
 show Yvvy ScaredEyes_Yvvy AMY at TalkingRight

 chY "Quem sabe o que ela planeja fazer com o antigo rei?"

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at TalkingLeft
 with dissolve

 chL "... Ou mesmo conosco."

 show Yvvy AMY at TalkingRight
 with dissolve

 chYL "Vai nos ajudar?"

 hide Yvvy
 hide Lucy
 with dissolve

 menu:
  "Sim.":
   jump yhelp
  "Não.":
   $ routeA = False
   $moral -= 10
   jump nhelp
 return
