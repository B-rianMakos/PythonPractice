import cmath
import math
import random

def elementary_school_quiz(flag, n):
    if flag == 0 :
        correct = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1-n2
            ans = int(input(f" What is {n1} - {n2}? "))
            if ans == question :
                print("You are correct")
                correct = correct +1
            else :
                print("That is not correct")
    if flag == 1 :
        correct = 0
        for n in range(n):
            n1 = random.randint(0,9)
            n2 = random.randint(0,9)
            question = n1**n2
            ans = int(input(f" What is {n1}^{n2}? "))
            if ans == question :
                print("You are correct")
                correct = correct +1
            else :
                print("That is not correct")

    print(f"You answered {correct} answers correctly!")
            
def high_school_quiz(a,b,c):
    disc = (b**2) - (4*a*c)
    if disc <0 :
        root1 = (-b + cmath.sqrt(disc))/(2*a)
        root2 = (-b - cmath.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following complexe roots : {root1} and {root2}")   
    elif disc <0:
        root1 = (-b + math.sqrt(disc))/(2*a)
        root2 = (-b - math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"has the following real roots : {root1} \n and {root2}")
    elif a == 0 :
        print("There are no roots for this equation")
    else :
        root1 = (-b + math.sqrt(disc))/(2*a)
        print(f"The quadratic equation {a}*x^2 + {b}*x + {c} ")
        print(f"only has one real root : {root1}")


def start():
    print("*************************************************")
    print("*        WELCOME TO THE CUM ZONE                *")
    print("*************************************************")
    name = input("What is your name? ")
    split1 = int(input(f"Hello {name}! Please enter 1 if you are in elementary school, enter 2 if you are in highschool or enter 3 if none of these apply to you. "))
    if split1 == 1 :
        split2 = input(f"{name} would you like to practise your substraction? Yes or No?" )
        if split2.lower() ==  "yes":
            flag = 0
            n = int(input("How many questions would you like?"))
            elementary_school_quiz(flag, n)
        elif split2.lower() == "no":
            split3 = input(f"{name} would you like to practise your exponentiation? Yes or No?" )
            if split3.lower() == "yes":
                flag = 1
                n = int(input("How many questions would you like?"))
                elementary_school_quiz(flag, n)
            elif split3 == "no":
                print(f"No options were chosen. If you wish to try again type 'start()'. Goodbye {name}!")
    if split1 == 2 :
        print("*************************************************")
        print("* Quadratic equation (a*x^2 + b*x + c) solver!  *")
        print("*************************************************")
        split4 = input(f"{name} would you like to solve a quadratic equation? Yes or No?" )
        if split4.lower().strip() == "yes" :
            a =float(input("Please input coefficient a"))
            b =float(input("Please input coefficient b"))
            c =float(input("Please input coefficient c"))
            high_school_quiz(a,b,c)
        elif split4.lower().strip() == "no" :
            print(f"Okay! Thank you for using our program {name}. Feel free to try it again!")
    if split1 == 3 :
        print("This program is to test elementary school kids and help highschool students. This program will most likely not have any use for you. If it does feel free to use this proram again by typing start()")


