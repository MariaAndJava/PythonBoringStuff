import HelloAndNameInput
import WhileBreakContinue

while True:
    print('Choose the program to be started. Type 1 or 2')
    if input() == 1:
        HelloAndNameInput.helloAndName()
        break
    elif input () == 3:
        WhileBreakContinue.start()
        break