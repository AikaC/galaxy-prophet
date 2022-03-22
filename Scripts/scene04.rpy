label route_01:

 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "O que a gente faz agora?"

 #show Anna ACMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #show GBody
 #show GHappy
 #with dissolve

 chG "Agora a gente volta para o Templo Secreto."
 chG "É onde nossas respostas nos esperam…{p}Pelo menos é o que eu espero."

 #show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Então elas não poderiam só ter te chamado ao invés de me trazer aqui?"

 #hide GBody
 #hide GHappy

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedMouth_Lucy
 #with dissolve

 chY "Hehe…"

 #show Twins ClosedHappyEyes_Lucy LaughingLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Assim não tem graça."

 #hide Twins
 #show GBody
 #show GAngry
 #with dissolve

 chG "Vocês duas…"

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Só vamos logo."

 #hide GBody
 #hide GClosedEyes
 #hide BGGrandma
 #show bgblack
 #with dissolve

 #jump route_01menu
 return

label route_01menu:

 if extra == True:

  #show BGExtra
  #show Anna AOMouth_Worried onlayer over_screens:
  # size (245,318.5)
  # left
  #with dissolve

  anna "A propósito..." 

  #hide Anna onlayer over_screens
  #window hide
  #with dissolve

  menu:
   "Onde estamos?":
    jump m31
    #join label translator
   "Quem é o ajudante da rainha?":
    jump ancient_dragon
   "Você ligou sua vida a uma árvore?":
    jump tree_barrier
   #"Travel between galaxies?":
    #jump friend
   #"Why do we understand each other?":
    #jump translator
   "Vamos continuar":
    #hide BGExtra
    #jump route_01p02
    return

 else:
  #show bgblack
  jump route_01p02
  return

label route_01p02:

 #stop music fadeout 1.0

 #play music "audio/SWIntro.ogg" fadeout 1.0
 #queue  music "audio/SWLoop.ogg"

 $ extra == False
 show arvore brilha
 with dissolve

 chG "Consegue ver a árvore?"

 #show Anna AEyes_Happy AOMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Sim... {w}Não percebi da primeira vez que vi,"
 anna "... mas ela é linda."

 #show Anna ACMouth_Happy onlayer over_screens:
 # size (245,318.5)
 # left
 #show GBody
 #show GHappy
 #with dissolve

 chG "De fato."

 #hide Anna onlayer over_screens
 #hide GBody
 #hide GHappy
 #with dissolve

 chNull "[anna]."

 #show Anna AOMouth_Worried
 #with dissolve

 anna "Quem está falando?"

 #hide Anna
 #show Twins
 #with dissolve

 chY "O quê?"
 chL "Ninguém está aqui."

 #hide Twins
 #with dissolve

 chNull "[anna]!"

 #show Anna
 #with dissolve

 anna "..."

 #show Anna AEyes_Empty
 #with dissolve
 #pause

 #hide Anna
 #show Twins
 #with dissolve
 
 chY "Espera, [anna]!"
 chL "Aonde vai, garota?"

 #hide Twins
 #show GBody
 #show GAngry
 #with dissolve

 chG "Deixem ela.{p}A árvore sagrada está chamando."
 chG "Posso sentir."

 #hide GBody
 #hide GAngry
 #with dissolve

 #call screen bar_nav
 return

label m31:

 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Aqui não parece nem um pouquinho com a minha casa…"
 anna "O que é esse lugar?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show GBody
 #show GHappy
 #with dissolve

 chG "Julgando pela sua aparência, você não é dessa galáxia."

 #hide GBody
 #hide GHappy
 #show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedHappyEyes_Lucy ClosedMouth_Lucy
 #with dissolve

 chY "Nós recebemos muitos viajantes."

 #show Twins DefaultLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Mas nenhum deles se parecem com você."

 #hide Twins
 #show GBody
 #show GHappy
 #with dissolve

 chG "Pode ser um poco tarde mas bem-vinda à Faellyx."

 #hide GBody
 #hide GHappy
 #show Twins ClosedHappyEyes_Yvvy LaughingYvvy ClosedHappyEyes_Lucy ClosedMouth_Lucy
 #with dissolve

 chY "Galáxia M-31!"

 #show Twins LaughingLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Estamos dentro de uma estrela!"

 anna "{color=F4C2C2}{i}Andrômeda? Então não estou em outra dimensão?{\i}"
 anna "{color=F4C2C2}{i}Como eu chguei tão longe?{\i}"

 #hide Twins
 #hide Anna onlayer over_screens
 #with dissolve

 #window hide
 #jump route_01menu
 return

label ancient_dragon:

 $ ancientDragon == True
 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Vocês me falaram sobre a rainha Selyna."
 anna "Mas não me disseram nada sobre o ajudante."

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins ClosedMouth_Lucy
 #with dissolve

 chY "Só de pensar nele já me sobe um frio na espinha."

 #show Twins ClosedMouth_Yvvy DefaultLucy
 #with dissolve

 chL "Ele é o último da espécie."

 #show Twins AngryEyes_Yvvy ClosedMouth_Lucy DefaultYvvy
 #with dissolve

 chY "A razão de termos feito do templo secreto um templo secreto para incício de conversa."

 #show Twins AngryEyes_Lucy ClosedMouth_Yvvy DefaultLucy
 #with dissolve

 chL "Não chegue perto dele!"

 #hide Twins
 #show GBody
 #show GAngry
 #with dissolve

 chG "Braxton estava conosco quando a profecia foi recitada pela primeira vez."
 chG "Bem, ele estava aqui bem antes da nossa existência."
 chG "Uma vez ele me disse que seu povo se chamava /“Dragão Ancião/”..."
 chG "... e foi um dos primeiros seres vivos a habitarem essa estrel."

 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Mas vocês disseram antes que ele e a rainha não podem saber sobre a árvore."

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

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

 #hide GBody
 #hide GClosedEyes
 #hide Anna onlayer over_screens
 #with dissolve

 #window hide
 #jump route_01menu
 return

label tree_barrier:

 #show Anna AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Eu sei que você disse que era história para outro dia, mas não consigo tirar isso da cabeça."
 anna "Você licou sua vida com uma árvore?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show GBody
 #show GAngry
 #with dissolve

 chG "Eu e mais dois amigos."
 chG "Criamos o templo secreto depois da morte do nosso amigo."
 chG "Para construir uma bareira que impedisse qualquer dano à árvore, nossa vida foi usada."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Iremos viver contanto que a árvore viva."

 #hide GBody
 #hide GClosedEyes
 #hide Anna onlayer over_screens
 #with dissolve

 #window hide
 #jump route_01menu
 return

label translator:

 #show Anna AEyes_Tedio AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Nós clarammente não falamos o mesmo idioma."

 #show Anna AEyes_Worried AOMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #with dissolve

 anna "Como a gente se entende?"

 #show Anna ACMouth_Worried onlayer over_screens:
 # size (245,318.5)
 # left
 #show Twins AngryEyes_Lucy LaughingLucy ClosedMouth_Yvvy
 #with dissolve

 chL "Lá vai você com esse negócio de /“idioma/” de novo…"

 #show Twins ClosedMouth_Lucy AngryEyes_Yvvy LaughingYvvy
 #with dissolve

 chY "O que é isso?"

 #hide Twins
 #show GBody
 #show GAngry
 #with dissolve

 chG "Já que existem visitantes de várias galáxias..."
 chG "... os magos desse lugar criaram um feitiço que traduz tudo para uma palavra equivalente para os dois lados."
 chG "Mas isso nem sempre funciona, como esse /“idioma/” que você diz."

 #hide GAngry
 #show GHappy
 #with dissolve

 chG "Não temo nada assim aqui, então para nós, é só um monte de sons."

 #hide GBody
 #hide GHappy
 #hide Anna onlayer over_screens
 #with dissolve

 #window hide
 #jump route_01menu
 return
