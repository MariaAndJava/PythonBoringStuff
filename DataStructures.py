import pprint
theBoard = {'top1':'', 'top2':'','top3':'','mid1':'', 'mid2':'','mid3':'', 'low1':'', 'low2':'','low3':''}

def printBoard(board):
    print(board['top1']+ '  |  ' + board['top2']+ '  |  ' + board['top3'])
    print('__________')
    print(board['mid1'] + '  |  ' + board['mid2'] + '  |  ' + board['mid3'])
    print('__________')
    print(board['low1'] + '  |  ' + board['low2'] + '  |  ' + board['low3'])

printBoard(theBoard)


print(type(42))
print(type(theBoard))

print('Hello'.isupper())

import pyperclip
pyperclip.copy('testtesttest')