import math
import timeit
import itertools as it
#import random 

# mit was ich am Ende getestet habe-------------------------------------------------
#
    #for a in range(int((n/2)**(1/3)), int(math.sqrt(n))+1)[::-1]:
    #for a in range(544949140000, int(math.sqrt(n))+1):
def find_a_and_b(n):
#        print(a)
    #for a in list:
    for a in range(int((n/2)**(1/3)), int(math.sqrt(n))+1):
        if n % a == 0:
            b1 = -a/2 + math.sqrt((a**2)/4 + n/a)
            b2 = -a/2 - math.sqrt((a**2)/4 + n/a)
            if b1 > 0 and (n % b1) == 0 and (n % (a+b1)) == 0:
                return a, b1
            if b2 > 0 and (n % b2) == 0 and (n % (a+b2)) == 0:
                return a, b2
    return None 


#print(find_a_and_b(102123161417560384731360000))
for b in range(2, 27):
    start = timeit.default_timer()
    print(b,": ",find_a_and_b(10**b))
    stop = timeit.default_timer()
    print("Time for 10^", b, ": ", stop-start)
#_break = True
#
#while _break:
#    rand = random.randrange(10000, 999999999)
#    print(rand)
#    print(find_a_and_b(rand))
#    if find_a_and_b(rand):
#        _break = False





#------Der Algo aus der Vorlesung-------------------------------
#n=a*b*(a+b)
#n=102123161417560384731360000
#finde a und b (a,b) Element der natürlichen Zahlen

def ab(n):
    for a in range(int((n/2)**(1/3)), int(n**(1/2))):
        for b in range(1, int((n/2*a)**(1/2))):
            if n == a*b*(a+b):
                return a,b
    return 0,0

#for b in range(2, 27):
#print(": ",ab(10**17))

#ab(102123161417560384731360000)
#    


