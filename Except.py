def divide42by(divider):
    try:
        return 42 / divider
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

def catAmount():
    print('How many cats do you have?')
    numCats = input()
    try:
        if int(numCats) > 0:
            if int(numCats)>4:
                print('Crazy.')
            else:
                print('get more.')
    except ValueError:
        print('That\'s not an applicable number.')





catAmount()



for i in range(0,10,2):
    print(str(divide42by(i)))



