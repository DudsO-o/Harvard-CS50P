# [Lecture 1 - Conditionals](htttps://youtu.be/_b6NgY_pMdw?si=xP9L_WPyuzPLbjNY)
- [Conditionals](#conditionals)
- [if Statements](#if-statements)
- [Control Flow, elif, and else](#control-flow-elif-and-else)
- [or]()
- [and]()
- [Modulo]()
- [Creating Our Own Parity Function]()
- [Pythonic]()
- [match]()
    - [Summing Up]()
<br>

# Conditionals
- Conditionals allow you, the programmer, to allow your program to make decisions: As if your program has the choice between taking the left-hand road or the right-hand road based upon certain conditions.

- Built within Python are a set of “operators” that are used to ask mathematical questions.
- ```>``` and ```<``` symbols are probably quite familiar to you.
- ```>=``` denotes “greater than or equal to.”
- ```<=``` denotes “less than or equal to.”
- ```==``` denotes “equals, though do notice the double equal sign! A single equal sign would assign a value. Double equal signs are used to compare variables.
- ```!=``` denotes “not equal to.
- Conditional statements compare a left-hand term to a right-hand term.

# if Statements
- In your terminal window, type ```code compare.py```. This will create a brand new file called “compare.”

- In the text editor window, begin with the following:
```
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```
Notice how your program takes the input of the user for both x and y, casting them as integers and saving them into their respective x and y variables. Then, the ```if``` statement compares x and y. If the condition of ```x < y``` is met, the ```print``` statement is executed.

- ```if``` statements use ```bool``` or boolean values (true or false) to decide whether or not to execute. If the statement of ```x > y``` is true, the compiler will register it as ```true``` and execute the code.
<br>

# Control Flow, elif, and else
- Further revise your code as follows:
```
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```
Notice how you are providing a series of ```if``` statements. First, the first ```if``` statement is evaluated. Then, the second ```if``` statement runs its evaluation. Finally, the last ```if``` statement runs its evaluation. This flow of decisions is called “control flow.”

Our code can be represented as follows:<br>
![image](https://github.com/DudsO-o/Harvard-CS50P/blob/main/Lecture1%20-%20Conditionals/Images/image.png)


- This program can be improved by not asking three consecutive questions. After all, not all three questions can have an outcome of ```true```! Revise your program as follows:
```
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
```
Notice how the use of ```elif``` allows the program to make fewer decisions. First, the ```if``` statement is evaluated. If this statement is found to be true, all the ```elif``` statements will not be run at all. However, if the ```if``` statement is evaluated and found to be false, the first ```elif``` will be evaluated. If this is true, it will not run the final evaluation.

- Our code can be represented as follows:<br>
