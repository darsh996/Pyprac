# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("Lets play")
print("I'll tell if number is odd or even")
num = int(input("Give me any number: "))

if num % 2 == 0:
    print(num," is even number")   
else:
    print(num," is odd number")

if num % 4 == 0:
    print(num," is multiple of 4 lets divide it")   
    check = int(input("Give me another number to divide"))
    if num % check == 0:
        print(num," divides evenly by ",check)
else:
    print("Bye Bye")
    



