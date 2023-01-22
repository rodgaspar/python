# This is my second python program

# Operators
num = 10 + 20
print("The result is: " , num)

num = 10 - 20
print("The result is: " , num)

num = 10 * 20
print("The result is: " , num)

num = 10 / 5 
print("The result is: " , num)

# Boolean
cond = False
print(cond)

# Conditional
if cond:
    print("This condition is true")
else:
    print("This condition is false")
    
# Looping
numbers = { 10, 20, 30, 40, 50, 60}
for number in numbers:
    if number == 10:
        print("Number 10")
    if number == 60:
        print("Number 60")
    
# Functions
def sum(x, y):
    print(x)
    print(y)
    return x + y
    
num = sum(5, 20)
print("The sum result is ", num)
