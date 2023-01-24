#Family Name : Brian Makos
#Student number : 300194563
#Class : ITI 1100
#Assigment2 part 1
#Year 2020 

import math
import random

def test():
    print("**************************************")
    print("*                                    *")
    print("*   Welcome to my math help tool!    *")
    print("*                                    *")
    print("**************************************")
    print(" ")
    name = input("What is your name? ")
    drop1 = int(input(f"Hello {name}! Please enter : 1 if you are in elementary school 2 if you are in highschool 3 if none of these apply to you. "))
    if drop1 == 1 :
        drop2 = input(f"{name} would you like to practice substractions? Yes or No?" )
        if drop2.lower().strip()==  "yes":
            flag = 0
            print("*************************************************")
            print("*                                               *")
            print("*              Substraction Quiz                *")
            print("*                                               *")
            print("*************************************************")
            n = int(input("How many questions would you like to do?"))
            print(f"Below are your {n} question : ")
            elementary_school_quiz(flag, n)
        elif drop2.lower() == "no":
            drop3 = input(f"{name} would you like to practise doing exponenent? Yes or No?" )
            if drop3.lower().strip() == "yes":
                flag = 1
                print("*************************************************")
                print("*                                               *")
                print("*              Exponential Quiz                 *")
                print("*                                               *")
                print("*************************************************")
                n = int(input("How many questions would you like?"))
                print(f"Below are your {n} question : ")
                elementary_school_quiz(flag, n)
               
            elif drop3.lower().strip() == "no":
                print(f"No options were chosen. type 'test()' to try again. Goodbye {name}!")
    if drop1 == 2 :
        print("*************************************************")
        print("*                                               *")
        print("*           Quadratic equation solver           *")
        print("*                                               *")
        print("*************************************************")
        drop4 = input(f"{name} would you like to solve a quadratic equation? Yes or No?" )
        if drop4.lower().strip() == "yes" :
            while drop4.lower().strip()== "yes" :
                a =float(input("Please input the value of a"))
                b =float(input("Please input the value of b"))
                c =float(input("Please input the value of c"))
                high_school_quiz(a,b,c)
                print("")
                drop4 = input("Would you like to solve another quadratic equation? Yes or no? ")
            else :
                print(f"Thank you for using our math program {name}. Feel free to use it again.")
              
        elif drop4.lower().strip() == "no" :
            print(f"Okay! Thank you for using our math program {name}. Feel free to try it again!")
    if drop1 == 3 :
        print("You are not the target audience for this program")
    elif drop1 > 3 :
        print("Only 1 , 2 and 3 are accepted as values. Please input one of those values")
        print(f"Goodbye {name}")


def high_school_quiz(a,b,c):
    disc = (b**2) - (4*a*c)
    if a != int and disc <0 :
        part1 = -b/(2*a)
        zero1 = (f" {part1}" +"+"+"i*" +str(math.sqrt(abs(disc))/(2*a)))
        zero2 = (f" {part1}" +"-"+"i*" +str(math.sqrt(abs(disc))/(2*a)))
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following complexe roots : {zero1} and {zero2}")   
    elif a != 0 and disc > 0:
        zero1 = (-b + math.sqrt(disc))/(2*a)
        zero2 = (-b - math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following real roots : {zero1} \n and {zero2}")
    
    elif a != 0 and disc == 0:
        zero1 = (-b + math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"only has one real root : {zero1}")

    elif a == 0 and b== 0 and c == 0 :
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print("is satisfied by all number for x") 

    elif a == 0 and b == 0 :
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(" The equation is satisfied for no number for x")

    elif a == 0 :
        line1 = -c /b
        print(f"the linear function : {b}*x + {c}")
        print(f"has the following root/solution x={line1}")
      

def elementary_school_quiz(flag, n):
    if flag == 0 :
        rightans = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1-n2
            print(f"question {n+1} :")
            answer = int(input(f" What is {n1} - {n2}? "))
            if answer == question :
                print("You are correct.")
                rightans = rightans +1
            
            else :
                print("That is not correct.")
        ratio =  rightans / (n +1)
        print(f"You answered {rightans}/{n +1} answers correctly!")
        if 1 > ratio >= 0.50 :
            print(f"Good job, but I know you can do better! Feel free to try again.")
        elif ratio == 1 :
            print(f"Good job, You will probably get an A tommorow! Goodbye.")
        elif ratio >= 0 <= 0.5 :
            print(f"I think you might need a little more practise! Feel free to try again. Bye.")

    if flag == 1 :
        rightans = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1**n2
            print(f"question {n+1} :")
            answer = int(input(f"What is {n1}^{n2}? "))
            if answer == question :
                print("You are correct.")
                rightans = rightans +1
    
            else :
                print("That is not correct")
        ratio =  rightans / (n +1)
        print(f"You answered {rightans}/{n +1} answers correctly!")
        if 1 > ratio >= 0.50 :
            print(f"Good job, but I know you can do better! Feel free to try again.")
        elif ratio == 1 :
            print(f"Good job, You will probably get an A tommorow! Goodbye")
        elif ratio >= 0 <= 0.5 :
            print(f"I think you might need a little more practise! Feel free to try again. Bye")
    elif flag >2 :
        print("Sorry but you must select either 1 or 2")
        print("Goodbye.")
