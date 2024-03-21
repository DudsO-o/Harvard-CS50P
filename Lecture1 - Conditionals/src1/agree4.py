# Compares multiple strings

# The .startswith() method in Python is used to check if a string starts with a specified prefix. It returns True if the string starts with the prefix and False otherwise.
# The method can also take optional start and end parameters to specify the portion of the string to search for the prefix.

# The method can also be used with a tuple of prefixes to check if the string starts with any of the prefixes.

# The method is useful in situations where you want to check if a string starts with a specific pattern or substring.
# For example, it can be used to check if a file name starts with a specific prefix or to check if a URL starts with a specific protocol.

answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not agreed")
