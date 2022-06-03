label to_grandma:

 show GBody at left
 show GAngry at left
 show screen noframe_moral
 with moveinleft

 chG "Então..."
 chG "Alguém pode me explicar o que está acontecendo?"

 hide GBody
 hide GAngry
 show Anna AEyes_Tedio rope at trueright
 with dissolve

 anna "Eu-"

 hide Anna
 show Lucy at left
 with moveinleft

 chL "Estávamos no templo secreto e {i}essa coisa{/i}..."
 
 hide Lucy
 show Anna AEyes_Tedio rope at trueright
 with dissolve

 anna "Garota... sou uma garota..."

 hide Anna
 show Lucy at left
 with moveinleft

 chL "O que é uma garota?"

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Enfim, {i} essa garota{/i} apareceu literalmente do nada."

 hide Yvvy
 show Colar at truecenter

 chY "E olha isso!"

 hide Colar
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Agora...{w} Essa é uma visão rara."
 chG "Onde conseguiu isso, criança?"

 hide GBody
 hide GAngry
 with dissolve

 menu:
    "Não, eu primeiro.":
       $ moral -= 5
       jump first
    "Eu comprei.":
       jump store
    "...":
       $ moral -= 10
       jump release

label first:
 
 show Anna AEyes_Angry rope at trueright
 with dissolve

 anna "Eu quero algumas respostas primeiro."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "{i}A garota{\i} tem coragem."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Devemos reconhecer isso."

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "..."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Justo. {w}O que quer saber?"

 hide GBody
 hide GAngry
 show Anna rope at trueright
 with dissolve

 anna "Quem é essa rainha má que vocês falam o tempo todo?"

 hide Anna
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Fala baixo..."

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with moveinleft

 chL "Eles podem te ouvir..."

 hide Lucy
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Não se preocupem, estamos a salvo aqui."

 hide GHappy
 show GAngry at left

 chG "Mas eu não recomendo continuar o uso da palavra \"má\" para descrevê-la."

 hide GBody
 hide GAngry
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Mesmo que ela {b}seja {/b}a rainha má."

 hide Yvvy
 show Lucy AngryEyes_Lucy ClosedMouth_Lucy at left
 with moveinleft

 chL "..."

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Não muito tempo atrás, uma criatura aparaceu no nosso mundo, assim como você."
 chG "Não sei os detalhes..."
 chG "Mas ela conseguiu conquistar o trono depois de um acordo com o atual ajudante dela."

 hide GBody
 hide GAngry
 show Lucy at left
 with moveinleft

 chL "Temos medo dela desde então."

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Você deve ser a heroína que veio nos salvar do mal que nos assombra."
 
 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with dissolve

 chL "Mas isso é estranho, ela não fez nada ainda. Por que você está aqui?"

 hide Lucy
 show Anna AEyes_Tedio rope at trueright
 with dissolve
 
 anna "Estou morrendo de vontade de saber também..."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Calma, por favor, não morra..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "... ainda."

 hide Lucy
 show Anna rope at trueright
 with dissolve

 anna "Enfim, se você disse que ela não fez nada ainda..."
 anna "Por que a chamam de rainha má?"

 hide Anna
 show Lucy AngryEyes_Lucy at left
 with moveinleft
 
 chL "Porque ela jogou o rei de verdade na masmorra."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Ele não merecia isso."

 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Eu vou explicar tudo."
 chG "Vocês duas, por favor, soltem {i}a garota{/i} agora."

 hide GBody
 hide GAngry
 with dissolve

 jump prophecy
 return
