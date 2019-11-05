import HelloAndNameInput
import WhileBreakContinue

while True:
    print('Choose the program to be started. Type 1 or 2')
    choice = input()
    if int(choice) == 1:
        HelloAndNameInput.helloAndName()
        break
    elif int(choice) == 2:
        WhileBreakContinue.start()
        break
    else:
        print('wrong')