# Hangman
Hangman is a paper and pencil guessing game for two or more players. One player thinks of a word, phrase or
sentence and the other(s) tries to guess it by suggesting letters within a certain number of guesses.

## Understand
For this problem, you will implement a variation of the classic wordgame Hangman. For those of you who are unfamiliar with the rules, you may read all about it here. In this problem, the second player will always be the computer, who will be picking a word at random.

In this problem, you will implement a function, called hangman, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to get you going.

For this problem, you will need the code files ps3_hangman.py and words.txt. Right-click on each and hit "Save Link As". Be sure to save them in same directory. Open and run the file ps3_hangman.py without making any modifications to it, in order to ensure that everything is set up correctly. By "open and run" we mean do the following:

Go to your IDE. From the File menu, choose "Open".
Find the file ps3_hangman.py and choose it.
The template ps3_hangman.py file should now be open. Run the file.
The code we have given you loads in a list of words from a file. If everything is working okay, after a small delay, you should see the following printed out:


Loading word list from file...
55909 words loaded.
If you see an IOError instead (e.g., "No such file or directory"), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.

For example, if you saved ps3_hangman.py and words.txt in the directory "C:/Users/Ana/" change the line: 

WORDLIST_FILENAME = "words.txt"  to something like

WORDLIST_FILENAME = "C:/Users/Ana/words.txt"

This folder will vary depending on where you saved the files.

The file ps3_hangman.py has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function by reading the docstrings:


 
