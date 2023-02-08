import time
import numpy as np
import datetime as dt
from flask import Flask
import matplotlib.pyplot as plt
from flask_restful import Api, Resource, reqparse



problemNums = range(1,100,1)


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

def problem3(num):
    primeFactors = []
    test = 2
    #num = 100
    orig = num
    while test <= num:
        if (num % test == 0):
            primeFactors.append(test)
            num = int(num / test)
            test = 2
        else:
            test += 1
    return 'problem 3: the largest prime factor of number '+ str(orig)+ ' is ' + \
           str(max(primeFactors)) + ' ' + str(primeFactors)
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

# def problem7():
#     primeLst = []
#     tmpLst = []
#     test = 1
#     rng = 1000000
#     for i in range(0, rng+1, 1):
#         while i >= test:
#             if i % test == 0:
#                 tmpLst.append(test)
#             test += 1
#         if len(tmpLst) == 2:
#             primeLst.append(i)
#         test = 1
#         tmpLst = []
#         if len(primeLst) == 10010:
#             return 'problem 7: prime number, which has index = 10001, is' + str( primeLst[10001 - 1] )

def problem7():
    num = 120000
    prime = list( range( 1, num + 1 ) )
    mod = 2
    tmp = []
    index = 0
    while mod**2 < max(prime):
        for i in prime:
            if i % mod != 0 or i == mod:
                tmp.append( i )
        prime = tmp
        tmp = []
        index += 1
        mod = prime[index]
    return 'Problem 7: prime number with index 10001 is ' + str(prime[10001])


def problem19():
    #import datetime
    date0 = dt.datetime(year=1901, month=1, day=1)
    date000 = dt.datetime(year=2000, month=12, day=31)
    dateLst = []
    day = 0
    dateN = dt.datetime.today()
    count = 0
    while dateN != date0:
        dateN = date000 - dt.timedelta(days=day)
        if dt.datetime.weekday(dateN) == 6 and dateN.day == 1:
            #dateLst.append( dateN )
            count += 1
        day += 1
    #print(dateLst)
    return 'Problem 19: quantity of Sundays and 1st day of month is ' + str(count)

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

    # print( 'problem 26: value of d which 1/d contains the longest recurring cycle is',
    #        textoutput.BOLD_UNDERLINE +
    #        str(get_key( fractionDict, max( fractionDict.values( ) ) )) +
    #        textoutput.END )
    return 'problem 26: value of d which 1/d contains the longest recurring cycle is ' + \
           str(get_key( fractionDict, max( fractionDict.values( ) ) ))

def problem36():
    integerNum = 1
    concatProd = ''
    concatProdLst = []
    for num in range(1, 400):
        while len(concatProd) < 10:
            if len(concatProd) == 9:
                print(concatProd)
                concatProdLst.append(int(concatProd))
            pandigit = num * integerNum
            concatProd += str(pandigit)
            integerNum += 1
        integerNum = 1
        concatProd = ''
    print(max(concatProdLst))

def problem50():
    num = 9
    prime = list( range(1, num + 1 ) )
    mod = 2
    tmp = []
    index = 0
    while mod**2 < max(prime):
        for i in prime:
            if i % mod != 0 or i == mod:
                tmp.append(i)
        prime = tmp
        tmp = []
        index += 1
        mod = prime[index]
    prime.remove(1)
    sum = 0
    sumLst = []
    sumDict = {}
    print(prime)
    prev = []
    for i in prime:
        sum += i
        sumDict[sum] = prev + [i]
        prev = sumDict[sum]
    for i in range(1,len(prime)):
        prev = []
        sum = 0
        for j in prime[i:len(prime)]:
            sum += j
            sumDict[sum] = prev + [j]
            prev = sumDict[sum]
            print(sumDict)
    for key in sumDict.keys():
        if key in prime:
            print(key, sumDict[key])


def problemTasks(n):
    return eval('problem' + str(n) + '()')

#FLASK REST
# app = Flask(__name__)
# api = Api(app)
# api.add_resource(Problem, '/<int:problem>')
# if __name__ == '__main__':
#     app.run(debug=True, port=80)

if __name__ == '__main__':
    # problem1()
    # problem2()
    # print(problem3( 1000 ))
    # problem4()
    # print(problem7())
    # print(problem19())
    # problem26()
    #problem36()
    problem50()

