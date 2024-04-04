# [Lecture 3 - Exceptions](https://youtu.be/LW7g1169v7w?si=eJw7zBrSyKSDGzUc)
- [Exceptions](#)
- [Runtime Errors](#)
- [```try```](#)
- [```else```](#)
- [Creating a Function to Get an Integer](#)
- [```pass```](#)
- [Summing Up](#)
<br>

# Exceptions
- Exceptions are things that go wrong within our coding.

- In our text editor, type ```code hello.py``` to create a new file. Type as follows (with the intentional errors included):
```
print("hello, world)
```
Notice that we intentionally left out a quotation mark.

- Running ```python hello.py``` in our terminal window, an error is outputted. The compiler states that it is a “syntax error". Syntax errors are those that require you to double-check that you typed in your code correction.

- You can learn more in Python’s documentation of [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html).
<br>

# Runtime Errors
- Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.

- In your terminal window, run ```code number.py```. Code as follows in your text editor:
```
x = int(input("What's x? "))
print(f"x is {x}")
```
Notice that by including the ```f```, we tell Python to interpolate what is in the curly braces as the value of ```x```. Further, testing out your code, you can imagine how one could easily type in a string or a character instead of a number. Even still, a user could type nothing at all – simply hitting the enter key.

- As programmers, we should be defensive to ensure that our users are entering what we expected. We might consider “corner cases” such as ```-1```, ```0```, or ```cat```.

- If we run this program and type in “cat”, we’ll suddenly see ```ValueError: invalid literal for int() with base 10: 'cat'``` Essentially, the Python interpreter does not like that we passed “cat” to the ```print``` function.
- An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.
- You can learn more in Python’s documentation of [```Errors and Exceptions```](https://docs.python.org/3/tutorial/errors.html).
<br>

# ```try```
- In Python ```try``` and ```except``` are ways of testing out user input before something goes wrong. Modify your code as follows:
```
try:
    x = int(input("What's x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
Notice how, running this code, inputting ```50``` will be accepted. However, typing in ```cat``` will produce an error visible to the user, instructing them why their input was not accepted.

- This is still not the best way to implement this code. Notice that we are trying to do two lines of code. For best practice, we should only ```try``` the fewest lines of code possible that we are concerned could fail. Adjust your code as follows:
```
try:
    x = int(input("What's x?"))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```
Notice that while this accomplishes our goal of trying as few lines as possible, we now face a new error! We face a ```NameError``` where ```x is not defined```. Look at this code and consider: Why is x not defined in some cases?

- Indeed, if you examine the order of operations in ```x = int(input("What's x?"))```, working right to left, it could take an incorrectly inputted character and attempt to assign it as an integer. If this fails, the assignment of the value of ```x``` never occurs. Therefore, there is no x to print on our final line of code.
<br>
<br>

# ```else```
