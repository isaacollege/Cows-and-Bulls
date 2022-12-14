Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Each digit must be unique. Ask the user to guess the 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

```py
Welcome to the Cows and Bulls Game!
Enter a number:
>>> 1234
2 cows, 0 bulls
>>> 1283
1 cow, 2 bulls
...
```

This continues until the user guesses the correct number (4 bulls). At that point tell them they have got it right and how many guesses it took them.

You need to create a function called count_cows and another called count_bulls. These should each take 2 parameters, a string containing the user's guess and another containing the answer. Each function should return an integer that represents the number of cows or bulls found. These two functions should be in their own module. The main program will be in its own file which will import the module you have created so that you can use your functions in the program logic.

Hint: if you are stuck on how to create a random number with unique digits then just hard code a value and come back to that later. e.g:
secret_number = "7934" # switch to random later