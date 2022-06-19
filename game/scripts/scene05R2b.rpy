label talk_tree2:
 if pc == False:
   $ sc05 = True
   call screen bar_nav
   return
 else:
   $ pc = False
   $sc05 = False
   jump did_it

label did_it:
 show arvore brilha
 show ASbody at left
 show AS_OMouth at left
 with dissolve

 stop music fadeout 1.0

 play music "audio/SWIntro.ogg"
 queue  music "audio/SWLoop.ogg"

 chAS "As engrenagens do universo funcionam por leis desconhecidas até por mim."
 chAS "É verdade, temos o direito de escolha e o livre arbítrio sobre nossas ações."
 chAS "Mesmo assim, algumas coisas acontecem simplesmente porque devem acontecer."
 chAS "Não se pode fugir do destino. {w}Pode-se tomar o caminho mais longo,{w=0.3} fugir jamais."

 hide ASbody at left
 hide AS_OMouth at left
 show Anna at trueright
 with moveinright

 anna "O que isso quer dizer?"

 hide Anna
 show ASbody at left
 show AS_OMouth at left
 with dissolve

 chAS "Tentou voltar para casa não foi?"
 chAS "Você tem um papel importante a cumprir aqui antes de tomar a ecolha de voltar para sua casa..."
 chAS "... Ou fazer daqui, o seu lar. {w}Consegue perceber isso?"

 hide ASbody at left
 hide AS_OMouth at left
 with dissolve
 
 menu:
  "Não...":

     show Anna at trueright
     with moveinright

     anna "Isso tudo parece complicado demais para mim..."
     anna "No fim das contas eu faço mesmo parte da profecia?"
     anna "Eu sou realmente a salvadora? Quem decidiu isso?"
     anna "Com certeza não foi a minha decisão."
     anna "Ninguém pode me obrigar a nada!"

     hide Anna
     show ASbody at left
     show AS_OMouth at left
     with dissolve

     chAS "*Suspira* É uma pena você não conseguir ver a situação como um todo."
     chAS "Vamos tomar o caminho mais longo então..."

     hide ASbody at left
     hide AS_OMouth at left
     hide arvore brilha
     with dissolve

     $ moral -= 5
     $ prision = True

     jump prision
     return
  "Acho que sim...":
     show Anna at trueright
     with moveinright

     anna "E no fim das contas eu faço mesmo parte da profecia?"
     anna "Eu sou realmente a salvadora?"

     hide Anna
     show ASbody at left
     show AS_OMouth at left
     with moveinleft

     chAS "Aprecio a sua curiosidade, {w}mas está me fazendo as perguntas erradas."
     chAS "Seu objetivo aqui comigo hojé é outro, não é mesmo?"

     hide ASbody at left
     hide AS_OMouth at left
     show Anna at trueright
     with dissolve

     anna "Sim!{p}O rei!"
     anna "A rainha Selyna é \'o mal\' citado na profecia?{w} Eu devo derrotá-la?"

     hide Anna
     show ASbody at left
     show AS_OMouth at left
     with dissolve

     chAS "A profecia é mais complexa que isso."
     chAS "A rainha estrangeira não faz parte dela, isso eu posso te dizer."
     chAS "Mas é verdade que seu caminho deve se cruzar com o dela algum dia."
     chAS "Procure o rei sob uma pedra, é lá que você vai o encontrar."

     hide ASbody at left
     hide AS_OMouth at left
     show Anna at trueright
     with dissolve

     anna "\'Sob uma pedra\'?"

     hide Anna
     show ASbody at left
     show AS_OMouth at left
     with dissolve

     chAS "Boa sorte [anna]."

     hide ASbody at left
     hide AS_OMouth at left
     show Anna at trueright
     with dissolve

     anna "Espera, eu-"

     hide Anna
     hide arvore brilha
     with dissolve

     if moral -- 100:
       $ moral += 5
       $ prision = False

       jump castle
     else:
       $ prision = False
       jump castle
     return

label prision:
   show BGExtra
   show GR
   with dissolve

   stop music fadeout 1.0

   play music "audio/chirp.ogg"
   
   chNull "Alto lá!"
   chNull "Sua presença está sendo requisitada diante da rainha!"
   chNull "Qualquer tipo de fuga será contado como traição, sua punição seria a morte!"

   hide GR
   hide BGExtra
   with dissolve

   if fugabr == False:
     jump castle_TalkQueen
   else:
     jump B_E
   return

label castle:
 
 show arvore brilha
 show Lucy at left
 with moveinleft

 stop music fadeout 1.0

 play music "audio/AnnaArp.ogg"
 queue  music "audio/AnnaLoop.ogg"

 chL "Conseguiu falar com a árvore?"

 hide Lucy
 show Anna at trueright
 with moveinright

 anna "Sim."

 hide Anna
 show Yvvy at right
 with moveinright

 chY "O que ela disse?"

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "Que a rainha não faz parte da profecia..."
 anna "Mas eu devo procurar o rei sob uma pedra."

 hide Anna
 show Lucy at left
 with dissolve

 chL "Sob uma pedra? Como a profecia?"

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "\'Lute contra a loucura que uma vez ajudou certo viajante sob uma pedra.\'"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "[anna] é uma viajante..."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "E o rei está sob uma pedra... {w=1}nas masmorras."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Acho que finalmente estamos chegando em algum lugar!"

 hide Lucy
 show Anna at trueright
 with dissolve
 
 anna "Ainda assim, a rainha..."

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Um passo de cada vez."

 hide Yvvy
 show Lucy at left
 with dissolve
 
 chL "Primeiro vamos salvar o rei."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "E como vamos entrar lá?"

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Deixe os disfarces comigo!"
 chY "A rainha costuma deixar sua guarda baixa durante a noite."

 hide Yvvy
 show Lucy at left
 with dissolve
 
 chL "Vamos entrar lá e pegar o rei antes que alguém consiga sequer notar alguma coisa."

 hide Lucy

 #call screen king_frame

 #show Lucy at left
 #with dissolve
 
 #chL "Mas por via das dúvidas, por favor lembre-se desse mapa."

 hide arvore brilha
 show BGCastle
 show GR
 with dissolve
 
 chGR "Tudo está como o usual, minha rainha."
 chGR "Nada a relatar por hoje também."

 hide GR
 show Queen at left
 with moveinleft

 chS "Ótimo. {w}Dispensados, voltem aos seus postos."
 chS "Não quero ser incomodada essa noite."

 hide Queen
 
 chGR "Sim, senhora."

 #todas estão disfarçadas
 show Yvvy Ymascara at right
 with dissolve

 chY "{color=F4C2C2}\*Sussurra\* As masmorras são por aqui."

 hide Yvvy
 show Lucy Lmascara at left
 with dissolve
 
 chL "Eles deixam o rei na cela mais distante."

 show Yvvy Ymascara at right
 with dissolve

 #chYL "Consegue se lembrar do mapa que recebeu?"

 hide Lucy
 hide Yvvy
 with dissolve

# menu:
#  "Sim":
#
#   show Lucy Lmascara at left
#   with moveinleft
# 
#   chL "Ótimo."
#
#   hide Lucy
#   show Yvvy Ymascara at right
#   with dissolve
   
#   chY "Que os jogos comecem!"
#
#   show Lucy Lmascara at left
#   with dissolve
#
#   chYL "Hehehe"
#
#   hide Lucy
#   hide Yvvy
hide BGCastle
with dissolve

jump historia_rei
return
#  "Não":
#   call screen king_frame
#
#   chL "Lembre-se bem disso, por favor."
#   chY "Estamos aqui para te ajudar, mas nunca se sabe o que pode acontecer."
#   
#   show Lucy Lmascara at left
#   show Yvvy Ymascara at right
#   with dissolve
#   
#   chYL "Vamos nessa."
#
#   hide Yvvy
#   hide Lucy
#   hide BGCastle
#   with dissolve
#   return
