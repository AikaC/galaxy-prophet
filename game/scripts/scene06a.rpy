﻿label historia_rei:
 #barulho de baque

 stop music fadeout 1.0

 play music "audio/AnnaArp.ogg"
 queue  music "audio/AnnaLoop.ogg"

 show Masmorra
 with dissolve

 chNull "Alguém está aí?"

 show Anna at trueright
 with dissolve
    
 anna "Sua majestade? É você?"

 hide Anna
 show GR
 with dissolve

 chR "Já fazem alguns anos que não me chamam assim."
 chR "Quem está falando?"

 hide GR
 show Anna at trueright
 with dissolve

 anna "meu nome é [anna], Yvvy e Lucy me enviaram para te salvar."

 hide Anna
 show GR
 with dissolve

 chR "Eu já disse a elas que isso não é necessário..."

 hide GR
 show Anna at trueright
 with dissolve

 anna "Na verdade, elas não foram as únicas..."
 anna "... A árvore sagrada também me instruiu a te encontrar."

 hide Anna
 show GR
 with dissolve

 chR "A árvore sagrada?"

 hide GR
 show Anna at trueright
 with dissolve

 anna "É uma longa história.{p}Vamos te soltar primeiro e então te conto tudo."
 #minijogo point and click, abrir a porta da cela

 hide Anna
 with flashbulb

 chR "Entendo."

 show GR
 with dissolve

 chR "Então a profecia finalmente começou a andar."

 hide GR
 show Anna at trueright
 with dissolve

 anna "Você sabe alguma coisa sobre isso?"

 hide Anna
 show GR
 with dissolve

 chR "Não muito mais que você, com certeza."
 chR "Você disse que Selyna não faz parte da profecia, certo?"

 hide GR
 show Anna at trueright
 with dissolve

 anna "Ao que parece..."

 hide Anna
 show GR
 with dissolve

 chR "Mas seu primeiro dever era me encontrar."
 chR "Então talvez saber o que aconteceu entre eu e ela possa te ajudar em alguma coisa."
 chR "Vamos andando por aqui, poucas pessoas conhecem essa passagem."
 chR "Eu te conto tudo no caminho."
 
 #cutscene start
 chR "A história na verdade não começa com Selyna, e sim com a irmã dela."
 chR "Quando jovem, eu tinha muito o costume de viajar para galáxias distantes."
 chR "Certo dia, parei em um lugar que me fascinou bastante."
 chR "Terra, era o nome do lugar, como fui descobrir mais tarde."
 chR "Era incrível como um lugar sem magia conseguiu se desenvolver tanto."
 chR "As pessoas, despertaram meu interesse também."
 chR "O lado negativo, principalmente."
 chR "Eu não entendia como eles podiam ser tão individualistas mesmo tendo tanto à sua volta."
 chR "Meu lado curioso despertou e eu comecei a visitar a Terra com mais frequência."
 chR "Foi então que conheci a linda Camélia."
 chR "Uma dançarina de rua cativante."
 chR "Passei a vê-la com mais frequência do que diva, admito."
 chR "E com o tempo, começamos a nos relacionar, mesmo quando nós dois sabíamos que era um relacionamento passageiro."
 chR "A irmã dela, Selyna era claramente contra isso tudo."
 chR "Eu deveria tê-la ouvido, mas estava cego de paixão."
 chR "Um dia as duas tiveram um grande desentendimento."
 chR "As coisas saíram de controle..."
 chR "... E o destino tomou a vida de Camélia."
 chR "Selyna se culpou e me culpou pelo ocorrido."
 chR "Ela jurou vingança e disse que iria até os confins dos universos atrás de mim."
 chR "E parece que conseguiu."
 chR "Até hoje quando fecho os olhos, vejo Camélia sorrindo para mim."

 #cutscene end
 chR "Eu não te culparia se você também achasse que a culpa foi minha."

 hide GR
 with dissolve
 
 menu:
  "Foi apenas um acidente":#sim
    $ rei = True
    jump castle_ataque
    return
  "Concordo com Selyna":#não
    jump minion2
    return
 
label castle_ataque:

 show Castle01
 show Lucy at left
 with dissolve

 stop music fadeout 1.0

 play music "audio/YL.ogg"

 chL "Garota! Aqui!"

 hide Lucy
 show Yvvy at right
 with moveinright

 chY "Vossa majestade! Fico feliz que esteja bem!"

 hide Yvvy
 show Ivan at left
 with moveinleft

 chI "Devemos deixar os cumprimentos para mais tarde."
 chI "Vamos sair daqui antes que-"

 hide Ivan
 show GR
 with dissolve

 chGR "Alto lá!"

 hide GR
 show Ivan at left
 with dissolve

 chI "Macacos me mordam!"

 hide Ivan
 show GR
 with dissolve

 chGR "Em nome da rainha Selyna, ordeno que devolvam os prisioneiros."

 hide GR
 show Lucy at left
 with moveinleft

 chL "Não vai rolar..."

 hide Lucy
 show Yvvy at left
 with dissolve

 chY "Desculpa, falou alguma coisa? Não consigo ouvir dessa distância."

 hide Yvvy
 show Ivan at left
 with dissolve

 chI "Preparem-se, eles estão vindo."

 hide Ivan
 with dissolve
 jump Luta
 return
  
 label Luta:

  if rei == False:
   hide Castle01
   show BGCastle
   with dissolve

   pass
  if rei == True:
   pass
  
  #minijogo luta, ultima opção impossível de vencer
  show Braxton at left
  with moveinleft

  chB "Você não vai me escapar!"

  hide Braxton
  hide Castle01
  with dissolve
  
  jump casaMinion
  return