label talk_tree:

 if moral < 80:
  jump grandma_again
 else:
  pass

 sc "Olá, [anna]."
 anna "Quem é você?"
 sc "Quem eu sou não importa."
 sc "O que você precisa sabe é que estou aqui para ajudar."
 sc "{b}Nós{\b} estamos aqui para ajudar."
 anna "Nós?{w} O que você quer dizer?"
 sc "Quando a hora chegar, pegue a {i}chave{\i}."
 sc "O verdadeiro salvador saberá o que fazer."
 anna "Que chave?"
 $ key = True
 #imagem da chave
 chG "Bem vinda de volta."
 chY "Entãoooo..."
 chL "O que aconteceu?"
 anna "A árvore me disse para pegar a chave quando a hora chegasse,"
 anna "o verdadeiro salvador saberá o que fazer."
 chL "Você falou {i}mesmo{/i} com a árvore?"
 chY "[anna] {i}é{/i} nossa salvadora."
 anna "Mas a árvore disse /'o salvador/' não eu."
 chG "[anna] está certa. Não temos certeza de nada ainda."
 chL "Mas ela falou com a árvore. Nem os magos mais poderosos conseguiram."
 chY "{i}E{/i} ela tem aquela coisa pendurada no pescoço... Quais são as chances?"
 chG "Ainda temos muito o que fazer. Vamos para casa primeiro."
 #jump minion
 return

label grandma_again:
 chY "..."
 chL "Não aconteceu nada."
 chY "Alguma coisa deve ter dado errado."
 chL "Talvez ela não faça parte da profecia."
 chY "Mas o colar..."
 anna "Talvez eu não seja quem vocês precisem."
 anna "Sinto muito..."
 chG "Não precisa se desculpar."
 chG "Vamos descobrir o que fazer..."
 chG "Tanto com a profecia quanto com arrumar um meio para você voltar para casa."
 anna "Obrigada."
 chG "Ainda temos muito o que fazer. Vamos para casa primeiro."
 #jump minion
 return
