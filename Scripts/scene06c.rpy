label TreeFalse:
     stop music fadeout 1.0

     play music "audio/chirp.ogg"
     show BGExtra
     show Braxton at left
     with dissolve

     chB "Por quanto tempo mais vamos caminhar?"

     hide Braxton
     show Anna at trueright
     with moveinright
     
     anna "Primeiramente eu nem sou daqui,"
     anna "eu já acho incrível conseguir me guiar em um lugar que mal tive contato ainda."
     anna "\*sussurra\*{color=F4C2C2}É como se algo estivesse me puxando para lá..."
     anna "E algo me diz que já estamos chegando."

     hide Anna
     with dissolve
     #tela treme
     anna "Braxton?{p}Braxton!"
     #braxton desmaiado
     if ancientDragon == True:
         show Anna at trueright
         show screen noframe_RouteWarning
         with dissolve

         anna "O que eu disse? Você desmaiou!"

         hide Anna
         hide screen noframe_RouteWarning
         with dissolve

         pass
     menu:
         "Fugir":
             $fugabr = True
              
             show Anna at trueright
             with dissolve
     
             anna "Se eu correr agora, talvez eu consiga voltar em segurança para a vovó..."

             hide Anna
             with dissolve

             hide BGExtra
             with dissolve

             jump prision
             return
         "Ajudar":
          
             show Anna at trueright
             with dissolve
     
             anna "Ótimo! Vai ser divertido arrastar ele até a cabana..."

             hide Anna
             hide BGExtra
             with dissolve

             jump casaMinion2
             return
         #"Olhar de perto":
             #Braxton desmaiado
         #    anna "Olhando de perto, ele quase parece humano..."
         #    anna "Não fosse por esses olhos estranhos..."
         #    anna "Espera... O que eu estou fazendo?"
         #    anna "Fique agradecido já que eu vou te arrastar de volta para a cabana."
         #    anna "Eu poderia ter tentado fugir..."
         #    jump casaMinion2
             return

label casaMinion2:
 #efeito olhos abrindo

 stop music fadeout 1.0

 play music "audio/AnnaArp.ogg"
 queue  music "audio/AnnaLoop.ogg"

 show BGBraxton
 with flashbulb

 chB "Ugh... O quê...?"
 
 show Anna at trueright
 with dissolve
     
 anna "Você desmaiou, isso que aconteceu."

 hide Anna
 show Braxton at left
 with dissolve

 chB "Como?"

 hide Braxton
 show Anna at trueright
 with dissolve
 
 anna "Deve ser a barreira protetora da árvore."
 anna "Chegando lá ou não, eu te levei como você queria."
 anna "De todo modo, por que faz tanta questão de procurar pela árvore sagrada?"
 anna "O que você realmente quer?"

 hide Anna
 show Braxton at left
 with dissolve

 chB "Lembranças não são algo importante para mim."
 chB "Eu já vivi muita coisa, esquecer de certas aventuras é natural."
 chB "Nunca me importei com colunas faltantes na memória."
 chB "Mas há algum tempo, eu sinto como se tivesse esquecido alguma coisa muito importante."
 chB "Bem na época em que conheci Selyna, eu estava andando sem rumo pelo reino."
 chB "À procura de algo que sequer sabia onde procurar."
 chB "Eu vi nela o mesmo olhar perdido que eu sentia, então formamos um trato."
 chB "Eu a ajudava a se vingar do rei,"
 chB "Ela me ajudava a encontrar minhas respostas."
 chB "Mas Selyna estava tão obcecada com o rei que não conseguia pensar em mais nada."
 chB "Tão obcecada que até {i}eu{/i} parei de procurar minhas respostas..."
 chB "Isso até você aparecer."
 chB "Eu sinto que esse colar é uma chave fundamental para eu finalmente descobrir a peça que falta desse quebra-cabeça."
 
 hide Braxton
 show Anna at trueright
 with dissolve
 
 anna "Chave?"
 if key == True:
     anna "Você está procurando por uma chave."

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não no sentido literal."

     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Não, {w}talvez seja."
     $key = False

     hide Anna
     with dissolve

     show Power at desaparece
     with dissolve
     pause 0.1

     show Braxton at left
     with dissolve

     if ancientDragon == False:
         chB "Entendo."
         chB "Eu estava lá quando a profecia foi recitada pela primeira vez."
         chB "Quando desvendei a profecia por conta própria não quis acreditar no que estava para acontecer."
         chB "Um dos meus companheiros, sem saber da miséria que havia caído sobre nós..."
         chB "... tentou me impedir de destruir a árvore."
         chB "Infelizmente isso custou a vida dele."
         pass
     if ancientDragon == True:
         $ancientDragon=False
         pass
     chB "Eu finalmente lembrei do que precisava."
     chB "Pelo menos quase tudo."
     chB "Ainda não sei o que a profecia realmente quer dizer."
     chB "Mas o que eu sei é que eu fazia parte dela desde de o começo."
     chB "E você também."
     
     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Impossível!"

     hide Anna
     show Braxton at left
     with dissolve
     
     chB "Pelo pouco que eu sei sobre o seu povo, também era impossível que você viajasse para outra galáxia."
     chB "E ainda assim, aqui está você."
     
     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Então, eu realmente devo salvar os habitantes."

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não, o seu papel é outro."
     
     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Qual, então?"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não sei,{w} mas vamos descobrir."
     chB "Vamos para a árvore sagrada."
     
     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Você não desiste mesmo, não é?"

     hide Anna
     show Braxton at left
     with dissolve

     chB "Não. {w}Mas dessa vez eu sei onde ela está."

     hide Braxton
     show Anna at trueright
     with dissolve
 
     anna "Ah é?"

     hide Anna
     hide BGBraxton
     with dissolve

     jump Final
     return
 if key == False:
     chNull "Abram a porta!"
     anna "!"

     hide Anna
     hide BGBraxton
     with dissolve
     
     $fugabr = True
     jump prision
     return

label Final:
     show arvore sagrada
     show ASbody at left
     show AS_OMouth at left
     with dissolve

     chAS "Uuuggh..."
     chAS "Eles estão tão perto de descobrir a verdade..."
     chAS "Tão perto..."
     chAS "E você, caro jogador, parabéns por ter chegado até aqui."
     chAS "Eu vou te mandar de volta ao seu mundo por hora,"
     chAS "... mas lembre-se de voltar mais tarde para seguir com o próximo capítulo."
     chAS "E não esqueça de salvar seu progresso para continuar de onde parou."
     chAS "Até mais tarde."

     hide arvore sagrada
     hide ASbody at left
     hide AS_OMouth at left
     with dissolve
     #cena crétidos
     return