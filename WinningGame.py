import random
#for x in range(1):
guessNum=random.randint(1,21)
#guessNum=25
#random(guessNum)


y=False
while y==False:
     x=int(input("please enter any number between 1 to 20 "))
     if x==guessNum:
          print("oh!!you win")
          break  
     elif x>guessNum:
          print("too long")
          
     elif x<guessNum:
          print("too short")

     else :
          print("invalid number")