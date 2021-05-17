import re
print("My messy calculator")
print("type 'quit' to exit")
previous = 0
run = True
def performMath():
    global run
    global previous
equation = input("enter the equation: ")
if equation == 'quit':
    run = False;
else:
    equation = re.sub('[a-zA-Z,.:" "]','',equation)
    previous = eval(equation)
    print("your result",previous)
while run:
    performMath()


