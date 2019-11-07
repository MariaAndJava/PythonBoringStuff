

"""


"""
import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('The symbol needs to be a string of length 1.')
    if (width<2) or (height<2):
        raise Exception('Width and height need to be greater than 2.')
    print(str(symbol)*width)
    for i in range(height-2):
        print(str(symbol)+' '*(width-2)+str(symbol))
    print(str(symbol) * width)

try:
    raise Exception('This is wrong.')
except:
    errorFile = open(r'X:\Daten\Desktop\error_log.txt','a') #mode 'a' is append
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written into error_log.txt')

# boxPrint('*',40,5)

# assert False, 'this is the assertion error message'