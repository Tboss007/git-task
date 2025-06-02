# a program for displaying a random joke every time the code runs

import random       # module for generating random activities
# a list of generating random jokes out of 6 everytime the code runs
jokes = ["\nWhy can’t you hear a pterodactyl going to the bathroom?\n Because the “P” is silent.",
         " \nWhy did the bicycle fall over? \nBecause it was two tired.",
         " \nI ordered a chicken and an egg online.\n I’ll let you know what comes first.",
         "\nWhy was Cinderella so bad at soccer?\n She kept running away from the ball!",
         "\nWhat do you call a sad strawberry? \n A blueberry!",
         " \nHow many computer programmers does it take to change a light bulb? \n None, that's a hardware problem!"
         ]

value = random.choice(jokes)
print(value)