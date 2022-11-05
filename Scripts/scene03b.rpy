label yhelp:

 show Anna AHappy AMH at trueright
 with dissolve

 anna "Claro, por que não?"

 show Anna AMA at trueright

 anna "Não é como se eu conseguisse voltar para casa mesmo."

 hide Anna
 show Yvvy ClosedEyes_Yvvy LMY at trueright
 with moveinright

 chY "Obrigada, [anna]."

 show Yvvy DMY at SilenceRight
 show Lucy ClosedEyes_Lucy LML at trueleft
 with dissolve

 chL "Você é uma boa garota\/[anna], ou sejá lá o que for."

 hide Lucy
 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "..."

 show Anna AHappy AMH at trueright

 anna "Obrigada?"

 hide Anna
 jump route_01
 return

label nhelp:

 stop music fadeout 1.0

 show Anna AAngry AMA at trueright
 with dissolve

 play music "audio/YL.ogg"
 
 anna "Porque eu deveria?"
 anna "Vocês mesmas falaram \“cheguei cedo demais\”."
 anna "Então eu claramente não sou quem vocês precisam."

 show Anna AScared AMA at trueright

 anna "Não sou nenhuma guerreira, nem nasci aqui."

 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with moveinright

 chY "Isso é verdade mas..."

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chL "Tem que ter alguma coisa..."

 hide Lucy
 hide Yvvy
 show Anna AScared AMA at trueright
 with dissolve

 anna "Olha, eu sinto muito sobre a \"era sombria\" que vocês estão para enfrentar."
 anna "Mas eu só quero voltar para a minha dimensão."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Se você faz mesmo parte disso, não existe uma maneira de voltar, criança."

 hide GBody
 hide GAngry
 show Anna AScared at trueright
 with dissolve

 anna "..."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "*Suspira.*"

 #hide GClosedEyes
 #show GAngry
 #with dissolve

 chG "Pode tentar falar com Paithyn."
 chG "Ela é outra guardiã da árvore e é especialista em portais."
 chG "Mas não tenha muitas esperanças."

 hide GBody
 hide GAngry
 show Anna AHappy AMH at trueright
 with dissolve

 anna "Obrigada, de verdade!"

 hide Anna
 show GBody at left
 show GHappy at left
 with dissolve
 
 chG "Yvvy, Lucy, levem [anna] para Paithyn."

 hide GBody
 hide GHappy
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with moveinright

 chY "Mas..."

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chL "Sim... Vovó."

 show Lucy AngryEyes_Lucy at trueleft

 chL "*sussurro* {color=F4C2C2}{i}Se [anna] faz mesmo parte da profecia, ela não vai voltar."

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at TalkingRight
 with dissolve

 chY "Ugh..."
 chY "Então vamos."

 hide Yvvy
 hide Lucy
 with dissolve

 jump route_02
 return
