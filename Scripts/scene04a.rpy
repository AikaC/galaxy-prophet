label route_01:

 show Anna at trueright
 with moveinright

 anna "O que a gente faz agora?"

 hide Anna
 show GBody at left
 show GHappy at left
 with moveinleft

 chG "Agora a gente volta para o Templo Secreto."
 chG "É onde nossas respostas nos esperam...{p}Pelo menos é o que eu espero."

 hide GBody
 hide GHappy
 show Anna AEyes_Tedio at trueright
 with dissolve

 anna "Então elas não poderiam só ter te chamado ao invés de me trazer aqui?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Hehe..."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Assim não tem graça."

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Vocês duas..."

 #hide GAngry
 #show GClosedEyes
 #with dissolve

 chG "Só vamos logo."

 hide GBody
 hide GAngry
 hide BGGrandma
 hide star
 with dissolve

 jump route_01menu
 return

label route_01menu:

 if extra == True:
   show BGExtra
   show Anna at trueright
   with dissolve

   anna "A propósito..."

   hide Anna
   with dissolve

   menu:
     "Onde estamos?":
       call m31 from _call_m31
     "Quem é o ajudante da rainha?":
       jump ancient_dragon
     "Você ligou sua vida a uma árvore?":
       call tree_barrier from _call_tree_barrier
     "Vamos continuar":
       hide BGExtra
       if routeA == False:
         jump route_02
       if routeA == True:
         jump route_01p02
   return

 else:
  #show bgblack
  jump route_01p02
  return

label route_01p02:

 $ extra = False
 $ sc04 = True
 show arvore brilha
 with dissolve

 chG "Consegue ver a árvore?"

 show Anna at trueright
 with moveinright

 anna "Sim... {w}Não percebi da primeira vez que vi,"
 anna "... mas ela é linda."

 hide Anna
 show GBody at left
 show GHappy at left
 with moveinleft

 chG "De fato."

 hide GBody
 hide GHappy
 with dissolve

 chNull "[anna]."

 show Anna at trueright
 with dissolve

 anna "Quem está falando?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "O quê?"

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Ninguém está aqui."

 hide Lucy
 with dissolve

 chNull "[anna]!"

 show Anna ACMouth at trueright
 with dissolve

 anna "..."

 #show Anna AEyes_Empty
 #with dissolve
 #pause

 hide Anna
 show Yvvy at right
 with moveinright
 
 chY "Espera, [anna]!"

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Aonde vai, garota?"

 hide Lucy
 show GBody at left
 show GAngry at left
 with dissolve

 chG "Deixem ela.{p}A árvore sagrada está chamando."
 chG "Posso sentir."

 hide GBody
 hide GAngry
 with dissolve

 $ sc05 = False
 call screen bar_nav
 return


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
