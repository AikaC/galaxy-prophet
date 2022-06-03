label m31:

 show Anna at trueright
 with moveinright

 anna "Aqui não parece nem um pouquinho com a minha casa..."
 anna "O que é esse lugar?"

 hide Anna
 show GBody at left
 show GHappy at left
 with moveinleft

 chG "Julgando pela sua aparência, você não é dessa galáxia."

 hide GBody
 hide GHappy
 show Yvvy at right
 with dissolve

 chY "Nós recebemos muitos viajantes."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Mas nenhum deles se parecem com você."

 hide Lucy
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Pode ser um pouco tarde mas bem-vinda à Faellyx."

 hide GBody
 hide GHappy
 show Yvvy at right
 with moveinright

 chY "Galáxia M-31!"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Estamos dentro de uma estrela!"

 hide Lucy
 with dissolve

 anna "{color=F4C2C2}{i}Andrômeda? Então não estou em outra dimensão?{\i}"
 anna "{color=F4C2C2}{i}Como eu cheguei tão longe?{\i}"

 show Anna at trueright
 with moveinright

 anna "Parando para pensar..."
 anna "Nós clarammente não falamos o mesmo idioma."
 anna "Como a gente se entende?"

 hide Anna
 show Lucy AngryEyes_Lucy at left
 with moveinleft

 chL "Lá vai você com esse negócio de /“idioma/” de novo..."

 hide Lucy
 show Yvvy AngryEyes_Yvvy at right
 with moveinright

 chY "O que é isso?"

 hide Yvvy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Já que existem visitantes de várias galáxias..."
 chG "... os magos desse lugar criaram um feitiço que traduz tudo para uma palavra equivalente para os dois lados."
 chG "Mas isso nem sempre funciona, como esse /“idioma/” que você diz."

 hide GAngry
 show GHappy
 
 chG "Não temos nada assim aqui, então para nós, é só um monte de sons."

 hide GBody
 hide GHappy
 with dissolve

 jump route_01menu

 return

label ancient_dragon:

 show screen noframe_dragonRoute

 $ ancientDragon = True
 show Anna at trueright
 with moveinright

 anna "Vocês me falaram sobre a rainha Selyna."

 hide screen noframe_dragonRoute

 anna "Mas não me disseram nada sobre o ajudante."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Só de pensar nele já me sobe um frio na espinha."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Ele é o último da espécie."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "A razão de termos feito do templo secreto um templo secreto para incício de conversa."

 hide Yvvy
 show Lucy AngryEyes_Lucy at left
 with dissolve

 chL "Não chegue perto dele!"

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Braxton estava conosco quando a profecia foi recitada pela primeira vez."
 chG "Bem, ele estava aqui bem antes da nossa existência."
 chG "Uma vez ele me disse que seu povo se chamava \“Dragão Ancião\”..."
 chG "... e foi um dos primeiros seres vivos a habitarem essa estrela."

 hide GBody
 hide GAngry
 show Anna at trueright
 with dissolve

 anna "Mas vocês disseram antes que ele e a rainha não podem saber sobre a árvore."

 hide Anna
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Isso é porque eventualmente ele se voltou contra nós."
 chG "Foi terrível, Braxton tentou destruir a árvore quando ninguém estava por perto."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Ele disse que era necessário e a profecia, sem sentido."
 chG "Um dos nossos amigos tentou parar ele e começou uma luta."

 #hide GClosedEyes
 #show GAngry
 #with dissolve

 chG "Tudo o que ele conseguiu fazer foi apagar as memórias de Braxton, mas a custo da própria vida."
 chG "Mesmo que o dragão ancião não se lembre mais da gente,"
 chG "aquela luta, de algum modo, ficou marcado na sua essência."
 chG "Então ele nunca mais se aproximou da gente."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Não há nada que podemos fazer sobre isso."

 hide BGExtra
 hide GBody
 hide GAngry
 with dissolve

 jump route_01menu
 return

label tree_barrier:

 show Anna at trueright
 with moveinright

 anna "Eu sei que você disse que era história para outro dia, mas não consigo tirar isso da cabeça."
 anna "Você lincou sua vida com uma árvore?"

 hide Anna
 show GBody
 show GAngry
 with dissolve

 chG "Eu e mais dois amigos."
 chG "Criamos o templo secreto depois da morte do nosso amigo."
 chG "Para construir uma barreira que impedisse qualquer dano à árvore, nossa vida foi usada."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Iremos viver contanto que a árvore viva."

 hide GBody
 hide GAngry
 with dissolve

 jump route_01menu

 return