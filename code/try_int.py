
something = input('Type something:')
try:
    isomething = int(something)
except ValueError:
    print("Leave it a string!")
else:
    print("Use the int value.")
