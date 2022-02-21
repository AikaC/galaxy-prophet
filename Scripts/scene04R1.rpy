label talk_tree:

 if moral < 80:
  jump grandma_again
 elif:
  pass

 sc "Hi there, [anna]."
 anna "Who are you?"
 sc "Who I am is not important."
 sc "What you have to know is that I am here to help."
 sc "We are here to help."
 anna "We?{w} What do you mean?"
 sc "When the time comes, reach the {i}key{\i}."
 sc "The true savior will know what to do."
 anna "Which key?"
 $ key = True
 #imagem da chave
 grandma "Welcome back."
 yvvy "Sooo..."
 lucy "What happened?"
 anna "The tree told me to reach for the key when the time comes,"
 anna "the savior would know what to do from then on."
 lucy "You {i}really{/i} talked to the tree?"
 yvvy "[anna] {i}is{/i} the savior."
 anna "But it said /'the savior/' not me."
 grandma "[anna]'s right. We don't know for sure yet if she's the savior."
 lucy "But she talked with the tree. No one else could do it."
 yvvy "{i}And{/i} she has that thing on her neck... What are the odds?"
 grandma "We still have a lot to do. Let's go home first."
 jump minion

label grandma_again:
 yvvy "..."
 lucy "Nothing happened."
 yvvy "Maybe something went wrong."
 lucy "Maybe she's not from the prophecy."
 yvvy "But the necklace..."
 anna "Maybe I'm not who you need."
 anna "I'm sorry..."
 grandma "There's nothing to feel sorry about."
 grandma "We'll figure out what to do..."
 grandma "With the prophecy and finding a way back to your home."
 anna "Thank you."
 grandma "We still have a lot to do. Let's go home first."
 jump minion
 return
