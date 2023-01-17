class textoutput:
    BOLD_UNDERLINE = '\033[1m' + '\033[4m'
    END = '\033[0m'

def problem1():
    return print('problem 1: sum of numbers below 1000 are multiples by 3 and 5 is',
                 textoutput.BOLD_UNDERLINE + str(sum([ num for num in range(1,1000,1) if (num % 3 == 0) or (num % 5 == 0) ])))


if __name__ == '__main__':
    problem1()
