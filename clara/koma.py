#import math
#import random 

# mit was ich am Ende getestet habe-------------------------------------------------
#
#def find_a_and_b(n):
#    for a in range(int((n/2)**(1/3)), int(math.sqrt(n))+1)[::-1]:
#        print(a)
#        if n % a == 0:
#            print(a)
#            b1 = -a/2 + math.sqrt((a**2)/4 + n/a)
#            b2 = -a/2 - math.sqrt((a**2)/4 + n/a)
#            if b1 > 0 and (n % b1) == 0 and (n % (a+b1)) == 0:
#                return a, b1
#            if b2 > 0 and (n % b2) == 0 and (n % (a+b2)) == 0:
#                return a, b2
#    return None 
#
#
#print(find_a_and_b(102123161417560384731360000))
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

#def ab(n):
#    for a in range(int((n/2)**(1/3)), int(n**(1/2))):
#        for b in range(1, int((n/2*a)**(1/2))):
#            if n == a*b*(a+b):
#                return a,b
#    return 0,0
#
#ab(102123161417560384731360000)
#    


