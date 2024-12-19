def collatz(number):
    if number == 1:
        return number
    elif number % 2 == 0:
        return number//2
    else:
        return 3*number+1


try:
    number = int(input("Enter a number: "))
    while number != 1:
        print(number)
        number = collatz(number)
    print(number)
except:
    print("You must enter a valid input!")
