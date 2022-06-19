label minion2:

 show Masmorra
 show Braxton at left
 with dissolve

 stop music fadeout 1.0

 play music "audio/YL.ogg"

 chB "Eita! Temos uma estrela fugitiva aqui."
 chB "Ouvi dizer que a rainha Selyna está atrás de você."
 chB "Ela ficaria muito feliz em descobrir sobre sua visita repentina."
 chB "Agora, eu poderia também te ajudar com a sua fuga."
 chB "Claro, tudo por um preço."

 hide Braxton
 $ rei = True
 with dissolve
 
 menu:
  "correr":
   jump castle_TalkQueen
   return
  "atacar":
   jump casaMinion
   return
    
label B_E:
   show BGCastle
   show Queen at left
   with dissolve

   stop music fadeout 1.0

   play music "audio/SWIntro.ogg"
   queue  music "audio/SWLoop.ogg"
   
   if fugabr == True:
     chS "Querida estrela perdida, você criou muita comoção no meu reino."
     chS "Imagino que vamos nos divertir muito com os planos que criei para nós duas."

     hide Queen
     show Anna at trueright
     with moveinright

     anna "Espera, não-"

     hide Anna
     with dissolve

     pass
   if fugabr == False:
     chS "Ótimo! Acredito que vamos nos divertir muito de agora em diante!"

     hide Queen
     show Anna at trueright
     with moveinright

     anna "Como assim?"

     hide Anna
     with dissolve
     
     pass
   #Cutscene:
   #selyna toma posse da mente de anna
   #Anna luta contra as gêmeas
   #Bad Ending

   "[anna] foi enfeitiçada pelo poder da rainha."
   "A profecia nunca poderá se realizar desse jeito."
   "Tente novamente."

   hide BGCastle
   return

label casaMinion:

 hide Masmorra
 show BGBraxton
 show Anna at trueright
 with dissolve

 anna "E então... {w}O que você quer?"

 hide Anna
 show Braxton at left
 with dissolve
 
 chB "Respostas."

 hide Braxton
 show Anna at trueright
 with dissolve

 anna "Acho que você está perguntando para a pessoa errada."
 anna "Ando em busca de respostas desde que pisei nessas terras."

 hide Anna
 show Braxton at left
 with dissolve

 chB "Talvez."
 chB "Mas algo me diz que você faz parte delas."

 hide Braxton
 show Anna at trueright
 with dissolve

 anna "Algo?"

 hide Anna
 show Braxton at left
 with dissolve

 chB "Esse colar, por exemplo.{p}Onde o conseguiu?"

 hide Braxton
 show Anna at trueright
 with dissolve

 anna "De novo isso?"

 hide Anna
 show Braxton at left
 with dissolve

 chB "De novo?"
 chB "Quem mais te perguntou sobre ele?"
 if ancientDragon == True:

     hide Braxton
     show Anna at trueright
     show screen noframe_RouteWarning
     with dissolve

     anna "Khalessi. {w}Sua antiga companheira, se lembra dela?"

     hide screen noframe_RouteWarning
     hide Anna
     show Braxton at left
     with dissolve

     chB "Kha-{w=0.5}lessi?"
     #efeito dor de cabeça
     hide Braxton
     show Anna at trueright
     with dissolve
         
     anna "Muito tempo atrás vocês eram companheiros."
     #efeito dor de cabeça
     anna "Protetores de uma árvore sagrada."
     #efeito dor de cabeça

     hide Anna
     show Braxton at left
     with dissolve

     chB "Chega!"

     hide Braxton
     show Anna at trueright
     with dissolve
         
     anna "O que aconteceu com você?"
     anna "..."
     anna "\'suspira\'"
     pass
 else:
     pass
     
 show Anna at trueright
 with dissolve
         
 anna "É só um objeto comum de onde venho."
 anna "Não fiz nada de especial para consegui-lo."
 anna "Era só isso que queria perguntar?"
 anna "Não podia ter feito isso no castelo?"

 hide Anna
 show Braxton at left
 with dissolve
 chB "Preferiria ter ficado nas masmorras?"

 hide Braxton
 show Anna at trueright
 with dissolve
   
 anna "{i}Touché."

 hide Anna
 show Braxton at left
 with dissolve

 chB "Descanse por hora. {w}Seu dia foi cansativo, tenho certeza."

 hide Braxton
 show Anna at trueright
 with dissolve
      
 anna "Muito bem. Boa noite, então."

 hide Anna
 show Braxton at left
 with dissolve

 chB "E eu não tentaria fugir se fosse você."

 hide Braxton
 show Anna at trueright
 with dissolve
      
 anna "..."
 
 hide Anna
 with flashbulb
 pause 0.1

 show Anna at trueright
 with moveinright
 anna "E então..."

 hide Anna
 show Braxton at left
 with dissolve

 chB "Então o quê?"
   
 hide Braxton
 show Anna at trueright
 with dissolve
      
 anna "Sou sua prisioneira ou sua convidada?"

 hide Anna
 show Braxton at left
 with dissolve

 chB "Isso vai depender de você."
 chB "Eu ainda acredito que você tenha as resposta que procuro."
     
 hide Braxton
 show Anna at trueright
 with dissolve
      
 anna "O que te faz ter tanta certeza?"

 hide Anna
 show Braxton at left
 with dissolve

 chB "Esse colar."
 chB "Ele pode não ser especial para você..."
 chB "Mas tem alguma coisa me incomodando."

 hide Braxton
 with dissolve
 if ancientDragon == False:
     show Anna at trueright
     with dissolve
    
     anna "Talvez você só não goste dessa cor?"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não, não é isso."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Qual o problema desse lugar? Todo mundo leva ironia a sério!"

     hide Anna
     show Braxton at left
     with dissolve

     chB "\'Ironia\'?"

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Sinceramente, eu já não sei mais o que fazer."
     anna "Quer minhas informações?"
     anna "Aqui está o que sei:"

     hide Anna
     with flashbulb
     pause 0.1

     show Braxton at left
     with dissolve
     chB "Não faz sentido."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Eu sei! Tentei dizer isso para todo mundo!"
     anna "Mas todos parecem acreditar que eu tenho algum papel nisso!"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não. {w}Não isso."
     chB "Não faz sentido uma árvore dessas existir por tanto tempo e eu não ter nenhum conhecimento."
     chB "Me leve até lá."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Eu não posso."

     hide Anna
     show Braxton at left
     with dissolve

     chB "Isso não foi um pedido."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "E isso não foi uma recusa voluntária."
     anna "A árvore tem uma barreira contra você, ou alguma coisa assim."

     hide Anna
     show Braxton at left
     with dissolve

     chB "{i}Contra mim?{/i} Acho impossível."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Já conseguiu chegar nela alguma vez?"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não..."
     chB "Mas também nunca tentei."
     chB "Me leve até lá."

     hide Braxton
     show Anna at trueright
     with dissolve
      
     anna "Como quiser, ó grandioso dragão."

     hide Anna
     hide BGBraxton
     with dissolve
         
     jump TreeFalse
     return

 if ancientDragon == True:
     show screen noframe_RouteWarning
         
     show Anna at trueright
     with dissolve

     anna "Acho que sei o que te incomoda, {w}{i}Dragão Ancião."

     hide screen noframe_RouteWarning
     hide Anna
     show Braxton at left
     with dissolve

     chB "Como sabe disso?"
         
     hide Braxton
     show Anna at trueright
     with dissolve
         
     anna "Talvez as respostas que procura entajam dentro de você."
     anna "Por que tentou destruir a árvore sagrada quando seu dever era protegê-la?"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Como eu protegeria algo que nem sequer sabia da existência?"
      
     hide Braxton
     show Anna at trueright
     with dissolve
         
     anna "Não sabia? {w}Ou não consegue se lembrar?"
     anna "Se é tão poderoso assim,"
     anna "tente se lembrar do seu companheiro que deu a própria vida para salvar a árvore sagrada do seu surto de raiva."

     hide Anna
     show Braxton at left
     with dissolve
         
 if intel == 1:
      show Power at desaparece
      with dissolve

      chB "Eu..."

      hide Power
      pass
 else:
     pass

 chB "Já chega!"
 chB "Me leve até lá!"
   
 hide Braxton
 show Anna at trueright
 with dissolve
          
 anna "Você não vai conseguir, {w}sua própria mente o impede de se aproximar da árvore."
 anna "Acho que foi a culpa reinando no seu inconsciente."
     
 hide Anna
 show Braxton at left
 with dissolve

 chB "Está insinuando que eu sou fraco?"
 chB "Me{w} leve{w} até {w}lá."

 hide Braxton
 show Anna at trueright
 with dissolve
     
 anna "Depois não diga que eu não avisei."

 hide Anna
 hide BGBraxton
 with dissolve
     
 jump TreeFalse
 return