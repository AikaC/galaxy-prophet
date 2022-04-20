label prophecy:

 show Anna AEyes_Tedio at trueright
 with dissolve

 anna "Obrigada por me soltarem."

 hide Anna
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chL "Ainda estamos de olho."

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with moveinleft

 chY "Você é muito suspeita."

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Lucy, Yvvy. {i}A garota{/i} é uma convidada agora."
 chG "Por favor, comportem-se."

 hide GBody
 hide GAngry
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Sim, vovó..."

 hide Yvvy
 hide Lucy
 show GBody
 show GHappy
 with dissolve

 chG "Então, {i}garota{/i}-"
 
 hide GBody
 hide GHappy
 show Anna at trueright
 with dissolve

 anna "[anna]."

 hide Anna
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Você é uma \“garota\” ou uma \“[anna]\”?"

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with moveinleft

 chL "Poderia, por favor se decidir, {i}querida convidada?{/i}"

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "..."

 hide GBody
 hide GAngry
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Desculpa, vovó..."

 hide Yvvy
 hide Lucy
 show GBody
 show GHappy
 with dissolve

 chG "Então... [anna]."

 #stop music fadeout 1.0

 hide GBody
 hide GHappy
 with dissolve

 #cutscene start

 #play music "audio/CutsceneIntro.ogg"
 #queue music "audio/CutsceneLoop.ogg"

 chG "Incontáveis eras atrás quando ainda não tinha muito o que ver por aqui..."
 chG "Um ser brilhante apareceu durante uma noite sem lua e disse..."

 #show BG01 onlayer over_screens
 #show textc onlayer over_screens
 #window hide
 #with dissolve
 #pause

 #hide BG01 onlayer over_screens
 #hide textc onlayer over_screens
 #window show

 chG "Antes que sequer pudéssemos reagir, uma luz nos cegou."
 chG "E a árvore sagrada a pareceu naquele mesmo lugar."
 chG "Como se ela sempre estivesse lá."
 chG "Tentamos perguntar o significado de tudo aquilo."
 chG "Feiticeiros e fadas vieram de longe tentar ajudar."
 chG "Mas nada mais aconteceu."
 chG "Então decidimos esperar."
 chG "Famílias começaram a crescer, {w}clãs se tornaram vilas..."
 chG "reinos foram trazidos à vida, {w}mas a árvore continuou em silêncio."
 chG "Quando estávamos quase desistindo... {w}Um novo sinal apareceu."

 #stop music fadeout 1.0

 #cutscene end
 
 play music "audio/AnnaArp.ogg"
 queue music "audio/AnnaLoop.ogg"

 show GBody at left
 show GAngry at left
 with moveinleft

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
   if moral == 100:
    jump yhelp
   else:
    $moral += 10
    jump yhelp
  "Não":
   $moral -= 10
   jump nhelp
 return

label so_sure:
 
 show Anna at trueright
 with dissolve

 anna "Apesar dessa coincidência de tempo, não vejo a relação da rainha com a profecia."
 anna "Há quanto tempo ela reina aqui?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Meia geração até agora..."

 hide Yvvy
 show Anna AEyes_Angry at trueright
 with dissolve

 anna "Ela já fez algo de ruim {b}depois{/b} de pegar a coroa?"

 hide Anna
 show Lucy at left
 with moveinleft

 chL "Ainda não..."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Aprisionar o rei já não é ruim o bastante?"

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "É... {w}Mas eu não vejo um período sombrio saindo só disso."

 hide Anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Isso nós podemos explicar."

 hide Yvvy
 with dissolve

 chL "Nós servíamos ao antigo rei, então estávamos lá quando tudo aconteceu."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Mas ainda não sabemos como a rainha Selyna e aquela criatura terrível terminaram juntos."

 hide Yvvy
 with dissolve

 #stop music fadeout 1.0

 #cutscene start

 
 #play music "audio/CutsceneIntro.ogg"
 #queue music "audio/CutsceneLoop.ogg"

 chL "Tudo começou com um ataque surpresa."
 chY "E vou te falar, a gente ficou mesmo supreendido."
 chL "Verdade, irmã. Nem um pouco legal."
 chY "Não sei como alguém de fora fez um acordo com uma criatura tão temível,"
 chY "mas eles conseguiram conquistar o castelo em pouco tempo."
 chL "Não estávamos tão protegidos assim..."
 chL "... já que não é comum entra na casa dos outros..."
 chY "... Ou castelo dos outros... "
 chL "... sem ser convidado."
 chY "Eu e Lucy conseguimos nos esconder a tempo,"
 chL "Mas ouvimos tudo."
 chY "Só não conseguimos ouvir direito..."

 #show BG01 onlayer over_screens
 #show textc2 onlayer over_screens
 #window hide
 #with dissolve
 #pause

 #hide BG01 onlayer over_screens
 #hide textc2 onlayer over_screens
 #window show
 #cutscene end

 show Lucy at left
 with moveinleft

 chL "Parece que a rainha Selyna e o antigo rei já se conheciam."

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Mas isso não seria uma surpresa."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Verdade.{p}O antigo rei costumava andar muito por outras galáxias."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Não sabemos como, antes que você pergunte."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "A rainha Selyna com certeza fez aquilo por vingança."

 hide Lucy
 show Yvvy at right
 with dissolve


 chY "Quem sabe o que ela planeja fazer com o antigo rei?"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "... Ou mesmo conosco."

 show Yvvy at right
 with dissolve

 chYL "Vai nos ajudar?"

 hide Yvvy
 hide Lucy
 with dissolve

 menu:
  "Sim.":
   $ routeA = True
   jump yhelp
  "Não.":
   $ routeA = False
   jump nhelp
 return

label yhelp:

 show Anna at trueright
 with dissolve

 anna "Claro, por que não?"

 #show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Não é como se eu conseguisse voltar para casa mesmo."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Obrigada, [anna]."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Você uma garota\/[anna], ou sejá lá o que for, legal."

 hide Lucy
 show Anna at trueright
 with moveinright

 anna "..."

 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Obrigada?"

 hide Anna
 jump route_01
 return

label nhelp:

 show Anna AEyes_Angry at trueright
 with dissolve

 anna "Porque eu deveria?"
 anna "Vocês mesmas falaram \“cheguei cedo demais\”."
 anna "Então eu claramente não sou quem vocês precisam."

 show Anna AEyes_Open at trueright

 anna "Não sou nenhuma guerreira nem nasci aqui."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Isso é verdade mas..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Tem que ter alguma coisa..."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Olha, eu sinto muito sobre a era sombria que vocês estão para enfrentar."
 anna "Mas eu só quero voltar para a minha dimensão."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Se você é mesmo parte disso, não existe uma maneira de voltar, criança."

 hide GBody
 hide GAngry
 show Anna ACMouth at trueright
 with dissolve

 anna "..."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Suspira."

 #hide GClosedEyes
 #show GAngry
 #with dissolve

 chG "Pode tentar falar com Paithyn."
 chG "Ela é outra guardiã da árvore e é especialista em portais."
 chG "Mas não tenha muitas esperanças."

 hide GBody
 hide GAngry
 show Anna at trueright
 with dissolve

 anna "Obrigada, de verdade!"

 hide Anna
 show GBody at left
 show GHappy at left
 with dissolve
 
 chG "Yvvy, Lucy, levem [anna] para Paithyn."

 hide GBody
 hide GHappy
 show Yvvy at right
 with moveinright

 chY "Mas..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Sim... Vovó."

 show Lucy AngryEyes_Lucy at left

 chL "{color=F4C2C2}*sussurro* {i}Se [anna] faz mesmo parte da profecia, ela não vai voltar."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with dissolve

 chY "Ugh..."
 chY "Então vamos."

 hide Yvvy
 with dissolve

 jump route_02
 return
