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


if __name__ == '__main__':
    problem1()
    problem2()
    findPrimeFactors( 600851475143 )
    problem4()
