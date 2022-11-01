label talk_tree:

 $sc04 = False
 
 if moral < 90:
  jump grandma_again
 else:
  pass

 stop music fadeout 1.0

 play music "audio/SWIntro.ogg"
 queue music "audio/SWLoop.ogg"

 show ASbody at left
 show AS_OMouth at left
 with dissolve
  
 chAS "Olá, [anna]."

 hide ASbody at left
 hide AS_OMouth at left
 show Anna AScared AMA at trueright
 with moveinright

 anna "Quem é você?"

 hide Anna
 show ASbody at left
 show AS_OMouth at left
 with dissolve

 chAS "Quem eu sou não importa."
 chAS "O que você precisa sabe é que estou aqui para ajudar."
 chAS "{b}Nós{/b} estamos aqui para ajudar."

 hide ASbody at left
 hide AS_OMouth at left
 show Anna AScared AMA at trueright
 with moveinright

 anna "Nós?{w} O que você quer dizer?"

 hide Anna
 show ASbody at left
 show AS_OMouth at left
 with dissolve

 chAS "Quando a hora chegar, pegue a {i}chave{\i}."
 chAS "O verdadeiro salvador saberá o que fazer."

 hide ASbody at left
 hide AS_OMouth at left
 show Anna AScared AMA at trueright
 with moveinright

 anna "Que chave?"

 show screen getKey

 hide Anna
 $ key = True

 stop music fadeout 1.0

 play music "audio/AnnaArp.ogg"
 queue  music "audio/AnnaLoop.ogg"

 show GBody at left
 show GHappy at left
 hide screen getKey
 with flashbulb

 chG "Bem vinda de volta."

 hide GBody
 hide GHappy
 show Yvvy at right
 with moveinright

 chY "Entãoooo..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "O que aconteceu?"

 hide Lucy
 show Anna AAngry AMA at trueright
 with dissolve

 anna "A árvore me disse para pegar a chave quando a hora chegasse,"
 anna "o verdadeiro salvador saberá o que fazer."

 hide Anna
 show Lucy at left
 with dissolve

 chL "Você falou {i}mesmo{/i} com a árvore?"

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "[anna] {i}é{/i} nossa salvadora."

 hide Yvvy
 show Anna AScared AMA at trueright
 with dissolve

 anna "Mas a árvore disse \'o salvador\' não eu."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "[anna] está certa. Não temos certeza de nada ainda."

 hide GBody
 hide GAngry
 show Lucy at left
 with dissolve

 chL "Mas ela falou com a árvore. Nem os magos mais poderosos conseguiram."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "{i}E{/i} ela tem aquela coisa amarrada no pescoço... Quais são as chances?"

 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Ainda temos muito o que fazer. Vamos para casa primeiro."

 hide GBody
 hide GAngry

 jump minion
 return

label grandma_again:

 show Yvvy at right
 with moveinright

 chY "..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Não aconteceu nada."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with dissolve

 chY "Alguma coisa deve ter dado errado."

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with dissolve

 chL "Talvez ela não faça parte da profecia."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Mas o colar..."

 hide Yvvy
 show Anna AScared AMA at trueright
 with moveinright

 anna "Talvez eu não seja quem vocês precisem."
 anna "Sinto muito..."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Não precisa se desculpar."
 chG "Vamos descobrir o que fazer..."

 hide GAngry
 show GHappy at left
 with dissolve

 chG "Tanto com a profecia quanto com arrumar um meio para você voltar para casa."

 hide GBody
 hide GHappy
 show Anna AHappy AMH at trueright
 with dissolve

 anna "Obrigada."

 hide Anna
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Ainda temos muito o que fazer. Vamos para casa primeiro."

 hide GBody
 hide GHappy
 with dissolve

 jump minion
 return
