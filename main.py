import re
class textoutput:
    BOLD_UNDERLINE = '\033[1m' + '\033[4m'
    END = '\033[0m'

def problem1():
    return print('problem 1: sum of numbers below 1000 are multiples by 3 and 5 is',
                 textoutput.BOLD_UNDERLINE +
                 str(sum([ num for num in range(1,1000,1) if (num % 3 == 0) or (num % 5 == 0) ])) +
                 textoutput.END)

def problem2():
    lst = [1, 2]
    num = 1
    while True:
        if lst[num-1] + lst[num] < 4000000:
            lst.append(lst[num-1] + lst[num])
            num += 1
        else:
            return print( 'problem 2: sum of Fibonacci elements which last element do not exceed 4mln is',
                          textoutput.BOLD_UNDERLINE +
                          str( sum(lst) ) + textoutput.END)

def findPrimeFactors(num):
    primeFactors = []
    test = 2
    while test <= num:
        if (num % test == 0):
            primeFactors.append(test)
            num = int(num / test)
            test = 2
        else:
            test += 1
    print( 'problem 3: the largest prime factor of number 600851475143 is ',
           textoutput.BOLD_UNDERLINE +
           str(max(primeFactors)) +
           textoutput.END
           )
    return primeFactors

def problem4():
    rng1 = list(range(100,1000,1))
    rng2 = list(range(100,1000,1))
    palindromic = {}
    for num1 in rng1:
        for num2 in rng2:
            numStr = num1*num2
            if numStr >= 100000:
                s1 = str(numStr)[0:3]
                s2 = str(numStr)[3:6]
                if int(s1) == int(s2[::-1]):
                    palindromic[numStr] = [num1,num2]
    print('problem 4: the largest polindromic of 3-digit numbers is',
          textoutput.BOLD_UNDERLINE +
          str(max(palindromic.keys())), '=', str(palindromic[max(palindromic.keys())][0]), 'x',
          str(palindromic[max(palindromic.keys())][1]) +
          textoutput.END)

def problem7(rng):
    primeLst = []
    tmpLst = []
    test = 1
    for i in range(0, rng+1, 1):
        while i >= test:
            if i % test == 0:
                tmpLst.append(test)
            test += 1
        if len(tmpLst) == 2:
            primeLst.append(i)
        test = 1
        tmpLst = []
        if len(primeLst) == 10010:
            print( 'problem 7: prime number, which has index = 10001, is',
                   textoutput.BOLD_UNDERLINE +
                   str(primeLst[10001-1]) +
                   textoutput.END )
            return True

def problem26():
    def get_key(d, value):
        for k,v in d.items():
            if v == value:
                return k

    fractionDict = {}
    saved1 = []
    saved2 = []
    for d in range(2,1001,1):
        fraction = str(1/d).split('.')[1]
        if len(fraction) <= 4:
            pass
        else:
            if fraction.count(fraction[0]) == 16:
                #fractionDict[d] = fraction[0]  # length 1
                fractionDict[d] = 1
            elif fraction.count(fraction[1]) >= 15:
                fractionDict[d] = 1
                # fractionDict[d] = fraction[1]   # length 1
            elif fraction.count(fraction[3]) >= 15:
                fractionDict[d] = 1
                # fractionDict[d] = fraction[3]  # length 1
            elif fraction.count(fraction[4]) >= 14:
                fractionDict[d] = 1
                # fractionDict[d] = fraction[4]  # length 1
            else:
                # define recurring value
                # define length of recurring value
                if len(fraction.split( fraction[0] )) > 2:
                    if fraction.split(fraction[0])[1] == fraction.split(fraction[0])[2]:
                        fractionDict[d] = len(fraction[0] + fraction.split( fraction[0] )[1])
                if len(fraction.split( fraction[1] )) > 2:
                    if fraction.split(fraction[1])[1] == fraction.split(fraction[1])[2]:
                        #print(d, fraction.split( fraction[1] ))
                        fractionDict[d] = len(fraction[1] + fraction.split( fraction[1] )[1])

    print( 'problem 26: value of d which 1/d contains the longest recurring cycle is',
           textoutput.BOLD_UNDERLINE +
           str(get_key( fractionDict, max( fractionDict.values( ) ) )) +
           textoutput.END )


if __name__ == '__main__':
    # problem1()
    # problem2()
    # findPrimeFactors( 600851475143 )
    # problem4()
    # time-spending task
    # problem7(150000)
    problem26()
