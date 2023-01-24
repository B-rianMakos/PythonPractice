
import math


#################
#Question 2.1
#################

def sum_odd_divisor(n):
    accum = 0
    if n == 0:
        return None
    else:
        for x in range(1,(abs(n)+1),2):
            if abs(n)%x == 0:
                accum = accum + x
        print(accum)


#################
#Question 2.2
#################

#################
#Question 2.3
#################
#ans = (((1 + math.sqrt(2))**n) - (1 - math.sqrt(2))**n)/(2*math.sqrt(2))
#ans = 2*pell(n-1) + pell(n-2)

def pell(n):
    '''
    (int) ---> None or number
    '''
    if n < 0:
        return None
    elif n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        x = pell(n-1)
        y = pell(n-2)
        for ans in range(1734,1735):
            ans = 2*x + y
            return round(ans)


#################
#Question 2.4
#################


#################
#Question 2.5
#################



#################
#Question 2.6
#################

def alienNumbers(s):
    a = s.count("T")
    b = s.count("y")
    c = s.count("!")
    d = s.count("a")
    e = s.count("N")
    f = s.count("U")
    ans = (a*1024)+(b*598)+(c*121)+(d*42)+(e*6)+(f*1)
    return ans
    
#################
#Question 2.7
#################

def alienNumbersAgain(s):
    ans = 0
    for c in s :
        if c in "T":
            ans += 1 * 1024
        elif c in "y":
            ans += 1 * 598
        elif c in "!":
            ans += 1 * 121
        elif c in "a":
            ans += 1 * 42
        elif c in "N":
            ans += 1 * 6
        elif c in "U":
            ans += 1 * 1
    return ans
                            
#################
#Question 2.8
#################

import math
def encrypt(s):
    
    ans = -1
    ans2 = 0
    if len(s)>1 and len(s) != 3:
        newstring = s[ans] + s[ans2]
    
        if len(s)%2 == 0: 
            for x in range(math.floor((len(s)/2)-1)):
            
                while x in range(math.floor((len(s)/2))):
            
                    if x%2 == 0:
                        ans = ans -1
                        ans2 = ans2 +1
                        string = s[ans] + s[ans2]
                
                        break
                    else:
                        ans2 = ans2 +1
                        ans = ans -1
                        string = s[ans] + s[ans2]
           
                        break
                newstring = newstring + string
            print(newstring)
        else:
            for x in range(math.ceil((len(s)/2))):
        
                while x in range(math.ceil(len(s)/2)):
            
                    if x%2 == 0:
                        ans = ans -1
                        
                        string = s[ans]
                
                        break
                    else:
                        ans2 = ans2 +1
                    
                        string = s[ans2]
               
                        break
                newstring = newstring + string
            print(newstring)
        
    elif len(s)<=1:
        newstring = s[ans]
        print(newstring)

    elif len(s) == 3:
        newstring = s[ans] + s[ans2]
        for x in range(math.floor((len(s)/2))):
        
            while x in range(math.floor(len(s)/2)):
            
                if x%2 == 0:
                    ans = ans -1
                        
                    string = s[ans]
                
                    break
                else:
                    ans2 = ans2 +1
                    
                    string = s[ans2]
               
                    break
            newstring = newstring + string 
            print(newstring)
