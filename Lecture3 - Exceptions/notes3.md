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
