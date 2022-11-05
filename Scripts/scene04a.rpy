label route_01:

 show Anna AScared AMA at trueright

 anna "O que a gente faz agora?"

 hide Anna
 show GBody at left
 show GHappy at left
 with dissolve

 chG "Agora a gente volta para o Templo Secreto."
 chG "É onde nossas respostas nos esperam...{p}Pelo menos é o que eu espero."

 hide GBody
 hide GHappy
 show Anna AMA at trueright
 with dissolve

 anna "Então elas não poderiam só ter te chamado ao invés de me trazer aqui?"

 hide Anna
 show Yvvy LMY at trueright
 with moveinright

 chY "Tsk, tsk, tsk."

 show Yvvy DMY at SilenceRight
 show Lucy LML at trueleft
 with dissolve

 chL "Assim não tem graça."

 hide Lucy
 hide Yvvy
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
   show Anna AMH at trueright
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

 show Anna AMA at trueright
 with moveinright

 anna "Sim... {w}Não percebi da primeira vez que vi,"

 show Anna AHappy AMH at trueright

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

 show Anna AScared AMA at trueright
 with dissolve

 anna "Quem está falando?"

 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with dissolve

 chY "O quê?"

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chL "Ninguém está aqui."

 hide Lucy
 hide Yvvy
 with dissolve

 chNull "[anna]!"

 show Anna AScared at trueright
 with dissolve

 anna "..."

 show Anna AEmpty at trueright
 with dissolve
 pause

 hide Anna
 show Yvvy ScaredEyes_Yvvy AMY at trueright
 with dissolve
 
 chY "Espera, [anna]!"

 show Yvvy DMY at SilenceRight
 show Lucy ScaredEyes_Lucy AML at trueleft
 with dissolve

 chL "Aonde vai, garota?"

 hide Lucy
 hide Yvvy
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
