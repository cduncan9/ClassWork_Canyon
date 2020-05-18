# calculator.py

a = input("Enter the first number: ")
b = input("Enter the second number: ")
a = int(a)
b = int(b)
print("The number you entered is {} and {}".format(a, b))

c = input("Enter a command: ")

if c == 'a':
    print("Add")
    answer = a + b
    print("{} + {} = {}".format(a, b, answer))
    print("Finished")
elif c == 's':
    print("Subtract")
    answer = a - b
    print("{} - {} = {}".format(a, b, answer))
    print("Finished")
elif c == 'm':
    print("Multiply")
    answer = a * b
    print("{} * {} = {}".format(a, b, answer))
    print("Finished")
elif c == 'd':
    print("Divide")
    answer = a / b
    print("{} / {} = {}".format(a, b, answer))
    print("Finished")
else:
    print("Error: Not a valid command")