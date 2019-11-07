import logging
#logging.disable(logging.CRITICAL)
logging.basicConfig(filename=r'X:\Daten\Desktop\error_log.txt',level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program.')

def factorial(number):
    logging.debug('Start of factorial (%s).' % (number))
    factorial = number
    while number > 2:
        number -=1
        factorial = factorial * number
        logging.debug('number is %s, total is %s.'%(number,factorial))
    return factorial


print(factorial(5))
logging.debug('End of program.')