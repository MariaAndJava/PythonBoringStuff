reachPeakOfProgramming = False

def printHelloWorld():
    print('Hello world!')
    global reachPeakOfProgramming
    reachPeakOfProgramming = True

def learnNewProgrammingLanguage(name):
    printHelloWorld()

print('What programming language are you attempting to learn next?')
name = str(input())
print(name + '? Wow! Let\'s get started! First Lesson:')

while not reachPeakOfProgramming:
    learnNewProgrammingLanguage(name)
print('You\'re done. You mastered '+ name+'.')