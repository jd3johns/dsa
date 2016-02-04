###
#
# IBM Ponder This, February 2016
# https://www.research.ibm.com/haifa/ponderthis/challenges/February2016.html
#
# A set of four equations (pieces of evidence) are given, albeit the digits
# have been replaced with letters from the word "interconnect", along with
# the letter 'a' and 'b'. The goal is to assign each of the 10 letters a digit
# in order for the equations to be true.
#
# Each piece of evidence is defined as a single function to calculate
# the possibilities for the value of each letter:
#     a, b, c, e, i, m, n, o, t, r
#
# Solution Notes:
#   1. Letters used as first digits cannot be zero.
#   2. n**i = ban is an easy first pass by checking for 3 digit 'ban' result
#   3. Narrow down results with results from step 2 into a**connect % inter = c
#      as there is less calculation and less modulus operations.
#   4. Ignore equation 3 (mod at) as there's no new info. Find 'm' to complete.
#   5. Remove digits that are taken when doing permutations.
#
# Author: Jonathan Johnston
# Date: 2016/2/3
#
###
import time

#
# Problem Equations
#
def satisfies_eq_one(a, c, o, n, e, t, i, r):
    connect = int("{c}{o}{n}{n}{e}{c}{t}".format(
        c=c,o=o,n=n,e=e,t=t))
    inter = int("{i}{n}{t}{e}{r}".format(
        i=i,n=n,t=t,e=e,r=r))
    return (a**connect % inter) == (c % inter)

def satisfies_eq_two(a, c, o, n, e, t):
    connect = int("{c}{o}{n}{n}{e}{c}{t}".format(
        c=c,o=o,n=n,e=e,t=t))
    at = int("{a}{t}".format(a=a,t=t))
    toe = int("{t}{o}{e}".format(t=t,o=o,e=e))
    return (a**connect % at) == (a**toe % at)

def satisfies_eq_three(a, c, o, n, e, t, m):
    connect = int("{c}{o}{n}{n}{e}{c}{t}".format(
        c=c,o=o,n=n,e=e,t=t))
    cm = int("{c}{m}".format(c=c,m=m))
    toe = int("{t}{o}{e}".format(t=t,o=o,e=e))
    return (a**connect % cm) == (a**toe % cm)

def satisfies_eq_four(n, i, b, a):
    ban = int("{b}{a}{n}".format(b=b,a=a,n=n))
    return (n**i) == ban

def run_tests(a, b, c, e, i, m, n, o, r, t):
    ''' run tests on single solution '''
    print "####"
    print "Testing potential solution:"
    print "a, b, c, e, i, m, n, o, r, t"
    print a, b, c, e, i, m, n, o, r, t
    print "####"

    if satisfies_eq_one(a, c, o, n, e, t, i, r):
        print "[Pass] Equation one"
    else:
        print "[Fail] Equation one"

    if satisfies_eq_two(a, c, o, n, e, t):
        print "[Pass] Equation two"
    else:
        print "[Fail] Equation two"

    if satisfies_eq_three(a, c, o, n, e, t, m):
        print "[Pass] Equation three"
    else:
        print "[Fail] Equation three"

    if satisfies_eq_four(n, i, b, a):
        print "[Pass] Equation four"
    else:
        print "[Fail] Equation four"


#
# Calculations
#
def evidence_one():
    ''' n**i = ban '''
    print "####"
    print "Based on the previous calculations,"
    print "begin assessing possible values for equation four:"
    print "n**i = ban"
    print "n, i, b, a"
    print "####"

    # n, i, b, a
    possibilities = []
    for n in range(10):
        for i in range(10):
            if n == i:
                continue
            val = n**i

            # result is three digits
            if val < 1000 and val > 99:
                ban = str(val)

                # n is final digit
                if str(n) == ban[2]:
                    b = int(ban[0])
                    a = int(ban[1])
                    # no repeats in set
                    if a in [n, i, b] or b in [n, i]:
                        continue

                    possibilities.append([n,i,b,a])

    return possibilities

def evidence_two(niba_vals):
    ''' a**connect = c (mod inter) '''
    print "####"
    print "Based on the previous calculations,"
    print "begin assessing possible values for equation one:"
    print "a**connect = c (mod inter)"
    print "a, c, o, n, e, t, i, r, b"
    print "####"
    x = [i for i in range(10)] # digit values
    # a, c, o, n, e, t, i, r
    possibilities = []
    for niba in niba_vals:
        n, i, b, a = niba
        exclude = niba

        for c in x:
            if c in exclude or c == 0:
                continue # not possible
            exclude.append(c)
            for o in x:
                if o in exclude:
                    continue
                exclude.append(o)
                for e in x:
                    if e in exclude:
                        continue
                    exclude.append(e)
                    for t in x:
                        if t in exclude or t == 0: # not possible
                            continue
                        exclude.append(t)
                        for r in x:
                            if r in exclude:
                                continue
                            if satisfies_eq_one(a,c,o,n,e,t,i,r):
                                vals = [a,c,o,n,e,t,i,r,b]
                                possibilities.append(vals)
                        exclude.pop()
                    exclude.pop()
                exclude.pop()
            exclude.pop()

    return possibilities


def evidence_three(aconetirb):
    ''' a**connect = a**toe (mod cm) '''
    print "####"
    print "Based on the previous calculations,"
    print "begin assessing possibilities for equation three:"
    print "a**connect = a**toe (mod cm)"
    print "a, b, c, e, i, m, n, o, r, t"
    print "####"

    x = [i for i in range(10)]
    digit_set = [set(x) - set(i) for i in aconetirb]
    possibilities = []
    for idx, digits in enumerate(digit_set):
        a,c,o,n,e,t,i,r,b = aconetirb[idx]
        for m in digits:
            if satisfies_eq_three(a,c,o,n,e,t,m):
                possibilities.append([a,b,c,e,i,m,n,o,r,t])
    
    return possibilities


# Run the program
fullstart = time.time()
start = time.time()
niba = evidence_one()
print niba
end = time.time()
print "Runtime: {}s\n".format(end - start)

start = time.time()
aconetirb = evidence_two(niba)
print aconetirb
end = time.time()
print "Runtime: {}s\n".format(end - start)

start = time.time()
abceimnort = evidence_three(aconetirb)
print abceimnort

end = time.time()
print "Runtime: {}s\n".format(end - start)

fullend = time.time()
print "Full runtime: {}s\n".format(fullend - fullstart)

# Run tests
for result in abceimnort:
    run_tests(*result)
