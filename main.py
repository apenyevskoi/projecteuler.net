import numpy as np
from flask import Flask
from flask_restful import Api, Resource, reqparse

problemNums = range(1,5,1)


class Problem(Resource):
    def get(self, problem=0):
        if problem == 0:
            return problemTasks(int(np.random.choice(problemNums,1))), 200
        if problem in problemNums:
            return problemTasks(problem), 200
        return print('Problem not found'), 404

class textoutput:
    BOLD_UNDERLINE = '\033[1m' + '\033[4m'
    END = '\033[0m'

def problem1():
    return 'problem 1: sum of numbers below 1000 are multiple by 3 and 5 is ' + \
                 str(sum([ num for num in range(1,1000,1) if (num % 3 == 0) or (num % 5 == 0) ]))

def problem2():
    lst = [1, 2]
    num = 1
    while True:
        if lst[num-1] + lst[num] < 4000000:
            lst.append(lst[num-1] + lst[num])
            num += 1
        else:
            return 'problem 2: sum of Fibonacci elements which last element do not exceed 4mln is' + \
                          textoutput.BOLD_UNDERLINE + \
                          str( sum(lst) ) + textoutput.END

def problem3():
    primeFactors = []
    test = 2
    num = 100
    orig = 100
    while test <= num:
        if (num % test == 0):
            primeFactors.append(test)
            num = int(num / test)
            test = 2
        else:
            test += 1
    return 'problem 3: the largest prime factor of number '+ str(orig)+ ' is ' + \
           str(max(primeFactors))
           #textoutput.END

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
    return 'problem 4: the largest polindromic of 3-digit numbers is ' + \
          str(max(palindromic.keys())) + '=' + str(palindromic[max(palindromic.keys())][0]) + 'x' + \
          str(palindromic[max(palindromic.keys())][1])

def problem7():
    primeLst = []
    tmpLst = []
    test = 1
    rng = 10
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

def problem78_recurtion(circles, i, iter, trigger):
    if iter == len(circles)+1:
        # print(circles)
        return circles.count('*'), iter+1
    if circles[len(circles) - i - 1] == '*' and  circles[len(circles) - i] == '*':
        circles = circles[0:len(circles) - i] + [' '] + circles[len(circles) - i: len(circles)]
        iter += 1
        if iter == len( circles )-1:
            # print(circles)
            return circles.count('*'), iter
        # print(circles, iter, i, 'two circles')
        return problem78_recurtion(circles, i, iter, trigger)
    elif circles[len(circles) - i - 1] == ' ' and circles[len(circles) - i] == '*' and circles[len(circles) - i-3] == '*' and trigger[0] == 0:
        circles[len( circles ) - i - 1] = '*'
        circles[len( circles ) - i - 2] = ' '
        iter += 1
        # print(circles, iter, i, 'space and circle')
        if i > 1:
            trigger[0] = 1
            trigger[1] = i
            i -= 2
        return problem78_recurtion(circles, i, iter, trigger)
    elif circles[len(circles) - i - 1] == ' ' and circles[len(circles) - i] == '*' and circles[len(circles) - i-3] == '*' and trigger[0] == 1:
        circles = circles[0:len( circles ) - trigger[1]] + [' '] + circles[len(circles) - trigger[1]: len(circles)]
        iter += 1
        # print(circles, iter, i, 'space and circle and trigger[0] == 1')
        trigger[0] = 0
        trigger[1] = 1
        if i > 1:
            i = 1
        return problem78_recurtion(circles, i, iter, trigger)
    else:
        if iter + 1 == len(circles):
            # print(circles)
            return circles.count('*'), iter+1
        i += 1
        if len( circles ) - i == 3:
            circles = ['*'] + [' '] + circles[1: len( circles )]
            # print(circles)
            return circles.count('*'), iter+1
        return problem78_recurtion(circles, i, iter, trigger)

def problem78(circles):
    rec = []
    count = len(circles) - 1
    flag = True
    iter = 0
    trigger = [0,1]
    # print(circles)
    while flag:
        #print('iter', iter, len(circles), count)
        if iter == len( circles ) + 2:
            return circles.count('*'), iter + 1
        if circles[count - 1] == '*' and circles[count] == '*':
            circles = circles[:count] + [' '] + circles[count: len( circles )]
            iter += 1
            # print(circles, count,'**')
            count += 2
            if iter == len( circles ) - 2:
                return circles.count('*'), iter + 1
        elif circles[count - 3] == '*' and circles[count - 1] == ' ' and circles[count] == '*' and trigger[0] == 0:
            if len(circles) - iter == 3:
                circles = ['*'] + [' '] + circles[1: len( circles )]
                # print( circles )
                iter += 1
                return circles.count('*'), iter + 1
            else:
                circles[count - 1] = '*'
                circles[count - 2] = ' '
                iter += 1
                # print( circles, count, iter, ' here')
            # if count > 1:
            #     trigger[0] = 1
            #     trigger[1] = count
            #     count += 1
            count += 1
        # elif  circles[count - 3] == '*' and circles[count - 1] == ' ' and circles[count] == '*' and trigger[0] == 1:
        #     circles = circles[0:len(circles) - trigger[1]] + [' '] + ['*'] + circles[len( circles ) - trigger[1]+2: len( circles )]
        #     iter += 1
        #     print(circles, count, 'trigger0=1')
        #     trigger[0] = 0
        #     trigger[1] = 1
        #     count = len(circles) - 1
        else:
            pass
            # if iter + 1 == len( circles ):
            #     return circles, iter
            # if len( circles ) - count == 3:
            #     circles = ['*'] + [' '] + circles[1: len( circles )]
            #     print(circles)
            #     iter += 1
            #     return circles, iter
        count -= 1
        if count == 0:
            flag = False


def problem78_1():
    table = np.zeros((3,3))
    print( table )
    y = table.shape[0]
    x = table.shape[1]
    i = table.shape[0] - 1
    while i >= 0:
        print(i)
                        
        i -= 1

def problemTasks(n):
    return eval('problem' + str(n) + '()')


#FLASK REST
app = Flask(__name__)
api = Api(app)
api.add_resource(Problem, '/<int:problem>')
if __name__ == '__main__':
    app.run(debug=True, port=80)

# if __name__ == '__main__':
    # problem1()
    # problem2()
    # findPrimeFactors( 600851475143 )
    # problem4()
    # time-spending task
    # problem7(150000)
    # problem26()
    # problem78_1()