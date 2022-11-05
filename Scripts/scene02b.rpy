label store:

 show Anna AMA rope at trueright
 with dissolve

 anna "Eu comprei em uma loja. É um item bem comum onde vivo."

 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with moveinright

 chY "Comprou? Loja? {i}Essa garota{/i} é estranha."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "..."

 show Anna AMA rope at trueright

 anna "Estamos mesmo falando o mesmo idioma?"

 hide Anna
 show Lucy ScaredEyes_Lucy AML at trueleft
 with moveinleft

 chL "O que é um idioma?"

 hide Lucy
 show Anna AMA rope at trueright
 with dissolve

 anna "Já posso ir para casa?"

 hide Anna
 show Yvvy AngryEyes_Yvvy AMY at trueright
 with dissolve

 chY "Não! Precisamos saber mais sobre a profecia primeiro!"

 hide Yvvy
 show Anna AScared AMA rope at trueright
 with dissolve

 anna "Que profecia?"

 hide Anna
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Eu vou explicar tudo."
 chG "Vocês duas... Soltem {i}a garota{/i}."

 hide GBody
 hide GHappy
 with dissolve

 jump prophecy

 return

label release:

 show Yvvy AngryEyes_Yvvy AMY at trueright
 with moveinright

 chY "Por que você não está dizendo nada?"

 show Yvvy DMY at SilenceRight
 show Lucy AngryEyes_Lucy AML at trueleft
 with dissolve

 chL "Você trabalha para a rainha?"

 show Lucy DML at SilenceLeft
 show Yvvy AngryEyes_Yvvy AMY at TalkingRight

 chY "O ajudante da rainha te enviou aqui para encontrar nosso templo secreto?"

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at TalkingLeft

 chL "Oh, não! E se eles já descobriram?"

 show Lucy DML at SilenceLeft
 show Yvvy ScaredEyes_Yvvy AMY at TalkingRight

 chY "E se eles já estiverem vindo?"

 hide Yvvy
 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Acalmem-se, as duas!"
 chG "Tenho certeza que esse não é o caso... {w}Provavelmente..."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Antes de tudo... Soltem {i}a garota{/i}."

 hide GBody
 hide GAngry
 with dissolve

 jump prophecy

 return
