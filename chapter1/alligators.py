def alligators(num1, num2):
    if num1 > num2:
        print(num1, 'is greater than', num2, 'by', (num1 - num2))
    elif num1 < num2:
        print(num2, 'is greater than', num1, 'by', (num2 - num1))
    elif num1 == num2:
        print(num1, 'is equal to itself')

alligators(10, 2)
alligators(1, 29)
alligators(10, 10)