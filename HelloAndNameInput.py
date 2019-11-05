# This program says hello and asks for my name

def helloAndName():
    print('Hello!')
    myName = ""

    while myName == '':
        print('What is your name?')  # ask for the name
        myName = input()
    if myName == 'Maria':
        print('This is a very nice name, ' + myName)
    elif myName == 'Java':
        print('Oh... Java. Du süße Maus' + 2 * '! :) ')
    else:
        print('This isn\'t a name, ' + myName)
    print('The length of your name is: ' + str(len(myName)))
    print('What is your age?')
    myAge = input()
    print('You will be ' + str(int(myAge) + 1) + ' in a year. Maybe.')







