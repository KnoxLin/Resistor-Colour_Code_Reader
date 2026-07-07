import math 

def colours(colour1,colour2):
    return (colour_codes[colour1.upper()],colour_codes[colour2.upper()])

def multiplier(colour):
    return 10**colour_codes[colour.upper()]

def resistorvalue(a,b,c):
    x,y = colours(a,b)
    return (x*10+y)*multiplier(c)
    

colour_codes = {"BLACK":0,
                "BROWN":1,
                "RED":2,
                "ORANGE":3,
                "YELLOW":4,
                "GREEN":5,
                "BLUE":6,
                "VIOLET":7,
                "GREY":8,
                "WHITE":9}

#print(colour_codes["BROWN"])
while True:
    try:
        c1,c2,c3= input("Enter the colours of the resistor:").split()
        value = resistorvalue(c1,c2,c3)
        print(value)
    except KeyError,ValueError:
        print("Input format was given incorrectly.")
        
    again = input("Do you want to continue? (y/n): ")
    
    if(again.lower() != 'y'):
        break;
    




