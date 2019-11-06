myList = ['cat', 'bat', 'fat', 'mat', 'java', 'maria']
listOfList = [myList, [10,20,30,40,50]]
helloList= list('Hello')

myList[:3] = ['a', 'b', 'c']

print(myList, myList[2], myList[1:3], myList[-3:-1] #slice ab start bis ende-1
      , listOfList[0][1])

del myList[0]
print(myList, myList+[1,2,3], myList*3)
print('java' not in myList)
print(helloList)

for i in range(len(myList)):
    print('Item '+str(i)+' in stock: '+myList[i])

#further list operations: .remove, .append, .insert, .sort(), .sort(reverse=True)
#ascibetical-order upperCase before all lawer case
spam = ['a', 'A', 'c', 'B']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)