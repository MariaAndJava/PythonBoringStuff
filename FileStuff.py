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

import shutil, os, send2trash

def copyMoveRenameFile():
    shutil.copy('C:\\spam.txt', 'C:\\desktop\\misc')#from first folder to right folder
    shutil.copy('file to copy', 'to this path with eg new name \\spam_2.txt')
    shutil.copytree('see', 'above') #all subfolders and files
    shutil.move('from', 'to')
    shutil.move('to rename copy to the same folder','but with a new name')

def removeDeleteFile():
    shutil.rmtree('path') #removes non empty folders with all files
    os.rmdir('path') #removes empty files
    os.unlink('remove file')

def send2trashInsteadOfDeleting():
    send2trash.send2trash('path\\file.txt')