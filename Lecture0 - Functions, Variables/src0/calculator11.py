# Demonstrates defining a function with a return value

'''
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
'''

# Playing with it
def square(n):
    return n * n

x = int(input("What's x? "))
print(f"{x}² =", square(x))