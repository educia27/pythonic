
def myfunc(num1, num2):
    ''' multiline string , this is important info regarding the function. \n
      this function takes one number to the power of another and returns the result

    :param num1: base value

    :param num2: exponent

    :return: the result of the calculation 
    '''
    return num1 ** num2

#print(myfunc.__doc__)

print(myfunc(2,5))