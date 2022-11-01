label yhelp:

 show Anna AHappy AMH at trueright
 with dissolve

 anna "Claro, por que não?"

 show Anna AMA at trueright
 
 anna "Não é como se eu conseguisse voltar para casa mesmo."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Obrigada, [anna]."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Você é uma boa garota\/[anna], ou sejá lá o que for."

 hide Lucy
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
 show Yvvy at right
 with moveinright

 chY "Isso é verdade mas..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Tem que ter alguma coisa..."

 hide Lucy
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
 show Yvvy at right
 with moveinright

 chY "Mas..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Sim... Vovó."

 show Lucy AngryEyes_Lucy at left

 chL "*sussurro* {color=F4C2C2}{i}Se [anna] faz mesmo parte da profecia, ela não vai voltar."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with dissolve

 chY "Ugh..."
 chY "Então vamos."

 hide Yvvy
 with dissolve

 jump route_02
 return
