label store:

 show Anna AMA rope at trueright
 with dissolve

 anna "Eu comprei em uma loja. É um item bem comum onde vivo."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Comprou? Loja? {i}Essa garota{/i} é estranha."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "..."

 show Anna AMA rope at trueright

 anna "Estamos mesmo falando o mesmo idioma?"

 hide Anna
 show Lucy at left
 with moveinleft

 chL "O que é um idioma?"

 hide Lucy
 show Anna AMA rope at trueright
 with dissolve

 anna "Já posso ir para casa?"

 hide Anna
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

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

 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "Por que você não está dizendo nada?"

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with moveinleft

 chL "Você trabalha para a rainha?"

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with dissolve

 chY "O ajudante da rainha te enviou aqui para encontrar nosso templo secreto?"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Oh, não! E se eles já descobriram?"

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "E se eles já estiverem vindo?"

 hide Yvvy
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
