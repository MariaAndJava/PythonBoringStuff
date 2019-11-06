import os, pprint

print(os.path.join(os.getcwd(),'file.txt'))
print(os.path.abspath('..\\..\\file.txt'))

totalSize = 0
for filename in os.listdir(r'X:\Daten\Desktop'):
    if not os.path.isfile(os.path.join(r'X:\Daten\Desktop', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(r'X:\Daten\Desktop', filename))
print(totalSize)

# os.makedirs()    #to create folders

import shelve

shelfFile = shelve.open('myData')
shelfFile['persons']=['Maria', 'Johanna','Memo', 'Mama', 'Sebastian', 'Alex']
shelfFile['animals']=['Java', 'Zamara', 'Philia']
shelfFile.close()

shelfFile = shelve.open('myData')
for i in shelfFile.keys():
    pprint.pprint(shelfFile[i])