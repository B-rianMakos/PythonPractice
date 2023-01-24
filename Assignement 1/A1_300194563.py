# Family name: Brian Makos
# Student number 300194563
# Course: IT1 1120
# Assignment number 1
#Year: 2020



import math
import turtle

####################
#Question 1
####################

def f_to_k(x):
    '''
    (number) ---> number
    Precondition: Must input an integer
    Function that converts a temperature in farhenheit to Kelvin 
    '''
    return (x - 32) * 5/9 + 273.15



####################
#Question 2
####################

def poem_generator():
    '''
    (string, string) ---> string
    Precondition: must input name = string and city = string
    Function that takes you name and city of birth and returns a poem
    '''
    city = input("Please enter your city of birth. ").capitalize()
    name = input("Please enter your name ").capitalize()
    print("")
    print(city + " where he got his name")
    print("with not an ounce of pity")
    print(name + " claims the fame")
    print("seeking to escape the city")


###################
#Question 3
###################

def impl2loz(w):
    '''
    number ---> (int, float)
    Precondition: w has to be bigger then 0
    Returns values l and o where l is the int inputed and o is it's decimals 
    '''
    l = int(w)
    o= (w-l)*16

    return(l,o)
    

###################   
#Question 4
###################

def pale(n):
    '''
    number ---> bool
    Preconditions : n has to have 4 digits and n has to be bigger then 0
    Returns True if the number is a pale number otherwise it returns false
    '''
    a = n//1000 %10
    b = n//100%10
    c = n//10%10
    d = n%10
    pale_test= not(a == b == 3 or b == c == 3 or c == d == 3 ) and not(d % 4 == 0)
    return pale_test

###################
#Question 5
###################

def bibformat(author,title,city,publisher,year):
    '''
    (string, string, string, string, string, string) ---> string
    Precondition: Must input the author, title, city, publisher and year published of a book in that order
    Function that takes a books information and writes a bibliography
    '''
    return(f"{author}({year}). {title}. {city}: {publisher}.")



##################
#Question 6
##################

def bibformat_display():
    '''
    (string, string, string, string, string, string) ---> none
    Precondition: Must input the author, title, city, publisher and year published of a book in that order
    Function that makes the user input the information of a book and then takes that information and writes a bibliography
    '''
    title =input("What is the title of your book? ")
    author = input("Whos is the author of that book? ")
    year = input("What year was it published? ")
    pub = input("Who published that book? ")
    city = input("What is the headquarter city of the publisher? ")
    print("")
    print(f"{author}({year}). {title}. {city}: {pub}.")



###################
#Question 7
###################

def compound(x,y,z):
    '''
    (int,int,int) ---> bool
    Preconditions: Must input 3 integers
    Takes 3 integers and returns True if x, the first int is the only even number and if at least one pair of the integers adds up to a number greater then 100. Otherwise the function returns False
    '''
    return((x + y > 100 or z+x > 100 or y + z > 100) and x%2 == 0 and y%2 != 0 and z%2 != 0)
    


###################
#Question 8
###################



def funct(p):
    '''
    (num) --> num
    Precondition: Number inputed must be positive and greater or equal to 11
    Function that soves for "r" in the following equation: 5^r^2− p + 10 = 0
    '''
    n = (p-10)
    m = math.log(n,5)
    r =(math.sqrt(m))
    print(f"The solution is {r}")
   
    


###################
#Question 9
###################

def gol(n):
    '''
    (number) ---> num
    Precondition: n has to be greater or equal to 1
    Function that checks how many times n had to be divided by two to give a number smaller then 1
    '''
    m = math.log2(n)
    f = math.ceil(m)
    print(f)



###################
#Question 10
###################


def draw_rocket():
    '''
    (none) ---> none

    Function that draws a rocketship
    '''
    s=turtle.Screen()
    t=turtle.Turtle() 
    t.pensize(2)
    t.speed(0)
    s.bgcolor("white")
    t.pencolor("black")
    #rocket nose

    t.penup()
    t.goto(100,100)
    t.pendown()
    t.setheading(90)
    t.circle(100, 90)
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.setheading(180)
    t.circle(100, 90)

    #rocket body
    t.penup()
    t.goto(100,100)
    t.pendown()
    t.setheading(-90)
    t.forward(300)
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.setheading(-90)
    t.forward(300)
    t.setheading(0)
    t.forward(200)

    #rocket wings
    t.penup()
    t.goto(100,-125)
    t.pendown()
    t.setheading(-70)
    t.forward(150)
    t.setheading(127)
    t.forward(88)
    
    t.penup()
    t.goto(-100,-125)
    t.pendown()
    t.setheading(250)
    t.forward(150)
    t.setheading(53)
    t.forward(88)

    #antenna
    t.penup()
    t.goto(0,200)
    t.pendown()
    t.setheading(90)
    t.pensize(2)
    t.forward(80)
    t.penup()
    t.goto(20,300)
    t.pendown()
    t.pencolor("red")
    t.circle(20)

    #windows
    t.pencolor("black")
    t.penup()
    t.goto(45,100)
    t.pendown()
    t.circle(45)
    t.penup()
    t.goto(45,0)
    t.pendown()
    t.circle(45)

    #burner
    t.penup()
    t.goto(50,-200)
    t.pendown()
    t.setheading(-60)
    t.forward(30)
    t.setheading(180)
    t.forward(120)
    t.setheading(60)
    t.forward(30)

    #flames
    t.pencolor("orange")
    t.penup()
    t.goto(33,-226)
    t.pendown()
    t.setheading(255)
    t.forward(50)
    t.setheading(100)
    t.forward(20)
    t.setheading(255)
    t.forward(40)
    t.setheading(105)
    t.forward(40)
    t.setheading(260)
    t.forward(20)
    t.setheading(105)
    t.forward(50)
    

    #moon
    t.pencolor("yellow")
    t.penup()
    t.goto(250,250)
    t.pendown()
    t.dot(102,"gray")
    t.penup()
    t.goto(245,260)
    t.pendown()
    t.pencolor("black")
    t.circle(10)
    t.penup()
    t.goto(299,263)
    t.pendown()
    t.circle(51)

###################
#Question 11
###################

def cad_cashier(price,payment):
    '''
    (number, number) ---> number
    
    paramaters must be positive, be real numbers and have two decimals and payment must be bigger or equal to the price
    
    Returns exact change to the closest fifth cent
    '''
    a = (payment - price) 
    d = math.trunc(a*10)
    b = round(a*100%10) 
    c = 5*(3<= b <= 7) 
    e = round(((d/10) + (c/100) + 0.1*(b>=8)),2)
    
    return e



###################
#Question 12
###################

def min_CAD_coins(price,payment):
    '''
    
    (number, number) ---> number
    
    paramaters must be positive, be real numbers and have two decimals and payment must be bigger or equal to the price
    
    Returns exact change to the closest fifth cent with a given ammount of coins which can be read from right to left as a toonie, loonie, quarter, dime , nickel
    
    '''
    t = cad_cashier(price,payment)
    f = t*100
    g = f//100 
    h = g//2 
    i = g-(h*2)
    j= f%100
    k= j//25
    l = j-(k*25)
    m = l//10
    n = math.trunc(round(l-(m*10)))
    o = n//5
    
    z = math.trunc(h)
    y = math.trunc(i)
    x = math.trunc(k)
    w = math.trunc(m)
    v = math.trunc(o)

    return (z,y,x,w,v)
