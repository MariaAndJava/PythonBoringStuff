import HelloAndNameInput
import WhileBreakContinue
import RangeLoop
import random, sys



while True:
    print('Choose the program to be started. Type smth from 1 to 6')
    choice = input()
    if int(choice) == 1:
        HelloAndNameInput.helloAndName()
        break
    elif int(choice) == 2:
        WhileBreakContinue.start()
        break
    elif int(choice) == 3:
        RangeLoop.rangeLoop(4,10,2)
    elif int(choice) == 4:
        print(random.randint(1,100))
    elif int(choice) == 5:
        sys.exit()
    elif int(choice) == 6:
        sys.exit()
    else:
        print('wrong')

