def add(a,b):
    return a+b

if __name__== '__main__':

    try:

        a = int(input('Enter first number : '))
        b = int(input('Enter second number : '))
        print('Sum of {} + {} =  {} '.format(a, b, add(a,b)) )

    except ValueError:
        print('invalid value given in the input')