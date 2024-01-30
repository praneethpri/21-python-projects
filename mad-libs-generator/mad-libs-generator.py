adjective = input('''
\u001b[1m Adjective: \u001b[0m type something silly.

                  ''')
noun = input('''
\u001b[1m Noun (plural): \u001b[0m Something you\'d find in a bakery.
            
             ''')
number = input('''
\u001b[1m Number: \u001b[0m Any number between 2 and 10.

               ''')
verb = input('''
\u001b[1m Verb: \u001b[0m Somthing sneaky.

             ''')
adverb = input('''
\u001b[1m Adverb: \u001b[0m Something descriptive.

               ''')
famous_person = input('''
\u001b[1m Famous Person: \u001b[0m Living or dead.

                       ''')
place = input('''
\u001b[1m Place: \u001b[0m Somewhere Unexpected.

              ''')
food = input('''
\u001b[1m Food: \u001b[0m Something sweet and sticky.
        
             ''')

story = f'''
Once upon a time, in a {adjective} little village nestled among rolling hills, lived a baker named Bartholomew Bigglesworth. Bartholomew was famous for his {noun}, which were so delicious they could make a grumpy gargoyle giggle.

One morning, Bartholomew arrived at his bakery to find a terrible sight. The shelves were bare! Every last {noun} had vanished, leaving only crumbs and a faint scent of {verb} in the air. Bartholomew, {adverb}, ran into the street, shouting, "Who stole my scrumptious sweets?!"

A crowd gathered, including the village gossip, Gladys Grumbleton, who immediately suspected her neighbor, the grumpy postman, Percy Pipsqueak. But Percy, with his pockets full of {famous_person} stamps, swore his innocence. The mystery deepened!

Bartholomew, determined to solve the case, followed a trail of {food} to the most unlikely place: the abandoned windmill on the edge of town. Creaking open the door, he gasped. There, perched atop a pile of stolen {noun}, sat... Gladys Grumbleton!

"Aha!" cried Bartholomew. "I knew it!"

But Gladys, with a sly grin, explained that she hadn't {noun} the {noun}. She had simply borrowed them to create a giant gingerbread village for the village children! Bartholomew, touched by her kindness, helped her finish the project.

The next day, the children of the village feasted on gingerbread houses and {noun}, celebrating the case of the curious cookie caper. And Bartholomew, though he never regained his full stock, learned that sometimes, the sweetest things in life are shared.

The End!

'''

print(story)
