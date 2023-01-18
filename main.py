import pandas as pd
class textoutput:
    BOLD_UNDERLINE = '\033[1m' + '\033[4m'
    END = '\033[0m'

def problem1():
    return print('problem 1: sum of numbers below 1000 are multiples by 3 and 5 is',
                 textoutput.BOLD_UNDERLINE +
                 str(sum([ num for num in range(1,1000,1) if (num % 3 == 0) or (num % 5 == 0) ])))

def problem2():
    lst = [1, 2]
    num = 1
    while True:
        if lst[num-1] + lst[num] < 4000000:
            lst.append(lst[num-1] + lst[num])
            num += 1
        else:
            return print( textoutput.END +
                          'problem 2: sum of Fibonacci elements which last element do not exceed 4mln is',
                          textoutput.BOLD_UNDERLINE +
                          str( sum(lst) ) + textoutput.END)

def prime(ser, mod):
    if len(ser) == 2:
        return list([1,2])
    elif len(ser) == 1:
        return list([1])
    elif ser.empty:
        return print('empty parameter')
    if mod == 2:
        ser = ser[(ser % mod != 0) | (ser == mod)]
        ser = ser.reset_index( drop=True )
    if ser[mod] < max( ser ):
        ser = ser[(ser % ser[mod] != 0) | (ser == ser[mod])]
        ser = ser.reset_index( drop=True )
        mod += 1
    else:
        return list(ser)
    return list(prime( ser, mod ))


def findPrimeFactors(num):
    primeFactors = []
    test = 2
    while test <= 10:
        if (num % test == 0):
            primeFactors.append(test)
            num = int(num / test)
            test = 2
            ser = pd.Series( range(1, num+1))
            print(prime(ser, 2))
            if num in prime(ser, 2):
                primeFactors.append(num)
        else:
            test += 1
    print(primeFactors)


if __name__ == '__main__':
    problem1()
    problem2()
    ser = pd.Series( range( 1, 3 ) )
    print(prime(ser, 2))
    findPrimeFactors(32)