import random
from re import S
from tkinter import W

def game(comp,b):
    if(comp==b):
        return None
    elif(comp=='s'):
        if(b=='g'):
            return True
        elif(b=='w'):
            return False 
    elif(comp=='g'):
        if(b=='w'):
            return True
        elif(b=='s'):
            return False     
    elif(comp=='w'):
        if(b=='s'):
            return True
        elif(b=='g'):
            return False             

no=random.randint(1,3)

if(no==1):
    comp='w'
elif(no==2):
    comp='s'      
elif(no==3):
    comp='g'    
b=input("Enter your choice Gun(g)-Snake(s)-Water(w)")
a=game(comp,b)    
print("The Pc choose " + comp )
if(a==True):
    print("You Won !")
elif(a==None):
    print("The Match is a Tie!")
elif(a==False):
    print("Opps!You Loose")        
     