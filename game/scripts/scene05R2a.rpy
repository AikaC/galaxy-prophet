﻿label training:

 play music "audio/chirp.ogg" fadeout 1.0 

 show BGExtra
 show Anna at trueright
 with dissolve

 anna "Que dia maluco..."
 anna "Primeiro, eu acabo em uma galáxia distante de uma forma misteriosa,"
 anna "só para descobrir que é tudo parte de uma profecia."
 if pc == True:
  anna "E depois, uma árvore falante que deveria dormir para sempre acorda e fala comigo."
 else:
  pass
 anna "E ainda por cima, um guarda da rainha aparece do nada..."
 anna "e eu quase sou presa."
 anna "..."
 anna "aha"
 anna "ahahaha"
 anna "Eu acho que vou surtar."
 anna "Já pode acordar, [anna]."

 hide Anna
 with dissolve
 
 if moral < 75:
  jump prision
 else:
  pass
 
 chNull "Lamento acabar com suas esperanças."
 chNull "Mas isso não é um sonho."

 show Ivan at left
 with moveinleft

 chNull "Você deve ser [anna], nossa futura salvadora."
 chNull "É um prazer te conhecer, meu nome é Ivan."
 chI "Eu também sou um guardião da árvore sagrada."

 hide Ivan
 show Anna at trueright
 with moveinright

 anna "Eu não sou a-"
 anna "Ah... esquece."
 anna "As notícias se espalham {i}mesmo{/i} rápido por aqui."
 anna "Prazer em te conhecer, Ivan."
 anna "Pode me dizer o motivo de eu estar na sua casa?"

 hide Anna
 show Ivan at left
 with dissolve

 chI "Você deve treinar comigo."
 chI "Agora que a rainha sabe sobre você, nós devemo pelo menos te dar uma chance de autodefesa,"
 chI "Já que não conseguimos de ajudar a voltar para casa."
 chI "É o mínimo que podemos fazer por você."
 chI "Já praticou algum estilo de luta antes, [anna]?"

 hide Ivan
 show Anna at trueright
 with dissolve

 anna "Espera...{w} Isso é sério?"
 anna "Videogame conta?"

 hide Anna
 show Ivan at left
 with dissolve

 chI "Muito sério."
 chI "Eu não conheço o estilo do {i}videogame{/i} mas deve ser útil para alguma coisa."

 hide Ivan
 show Anna at trueright
 with dissolve

 anna "Não, esquece..."
 anna "Vamos começar logo."

 hide Anna
 show Ivan at left
 with dissolve

 chI "Muito bem..."
 
 hide BGExtra
 hide Ivan
 with flashbulb
 pause 0.1

 #passagem de tempo, gêmas vêm visitar após alguns meses
 play music "audio/AnnaArp.ogg" fadeout 1.0
 queue music "audio/AnnaLoop.ogg"

 show BGIvan
 show Yvvy at right
 with dissolve

 chY "Garota! Quanto tempo!"

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Meses!"

 show Yvvy at right
 with dissolve

 chYL "Sentimos saudades!"

 hide Yvvy
 hide Lucy
 show Anna at trueright
 with dissolve

 anna "O tempo voa rápido quando se está ocupado."
 anna "Como vocês estão?"

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Tão ocupadas quanto você."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "O ajudante da rainha está te procurando por todos os lados."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Tivemos um trabalhão para despistar ele."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Ele é muito assustador..."

 hide Lucy
 show Yvvy at right
 with dissolve
 
 chY "Vovó mandou a gente perguntar como você está."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Sem querer te apressar..."

 hide Lucy
 show Yvvy at right
 with dissolve
 
 chY "Mas estamos com pressa."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Quando você volta?"

 hide Lucy
 show Ivan at left
 with dissolve

 chI "[anna] está pronta para ir."
 chI "Eu não acho que possa fazer mais que isso com o tempo que temos."
 chI "Você fez um trabalho excelente, [anna]."

 hide Ivan
 show Anna at trueright
 with dissolve

 anna "Obrigada."

 hide Anna
 show Yvvy at right
 with dissolve

 chY "Você aprendeu a lutar?"

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Já?!"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Só o básico..."
 anna "Viu?"

 hide Anna
 with dissolve
 
 show Colar
 show Power at desaparece
 with dissolve

 $intel += 1

 chY "Uau!"
 
 hide Colar
 hide Power
 with flashbulb

 show Lucy at left
 with moveinleft

 chL  "Legal!"

 hide Lucy
 show Anna at trueright
 with moveinright

 anna "De volta para a vovó?"

 hide Anna
 show Yvvy at right
 show Lucy at left
 with dissolve

 chYL "Não."

 hide Lucy
 with dissolve

 chY "Vamos ver a árvore sagrada primeiro."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Também precisamos conversar no caminho."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Ok..."
 
 hide BGIvan
 show BGExtra
 with fade
 
 anna "Então... O que era?"

 hide Anna
 show Yvvy at right
 with moveinright

 chY "Bem...{w} Braxton, o ajudante da rainha, acabou descobrindo sobre o seu colar."

 hide Yvvy
 show Lucy at left
 with moveinleft

 chL "Isso quer dizer que a rainha Selyna também sabe sobre a profecia."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Oh..."

 hide Anna
 show Lucy at left
 with dissolve

 chL "Sim, \'oh...\'"

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Quão ruim isso é?"

 hide Anna
 show Lucy at left
 show Yvvy at right
 with dissolve

 chL "Só temos duas escolhas agora..."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Salvar o rei em segredo..."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Ou derrotar a rainha."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Vovó disse que é muito cedo para enfrentar a rainha Selyna."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Então vamos invadir o castelo para salvar o rei."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Quando estivermos todos a salvo, poderemos planejar os próxios passos."

 hide Yvvy
 show Anna at trueright
 with dissolve

 anna "\'Nós\' como em nós três?"

 hide Anna
 show Lucy at left
 with dissolve

 chL "É claro, bobinha."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Você é parte da profecia."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Deve vir conosco dessa vez."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Por isso estamos indo ver a árvore sagrada primeiro."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "Você precisa da ajuda dela."

 hide Lucy
 show Yvvy at right
 with dissolve

 chY "Sabe como é, essa parada de comunicação com a natureza e tals."

 hide Yvvy
 show Lucy at left
 with dissolve

 chL "é só fazer o seu lance."

 hide Lucy
 show Anna at trueright
 with dissolve

 anna "Ahã, o meu lance."

 hide Anna
 hide BGExtra
 with dissolve

 $ sc04 = False
 jump talk_tree2
 return