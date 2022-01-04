

import random

comwin=0
userwin=0
tie=0


a=["Stone","Paper","Seizor"]



num=int(input("Enter number of playing that you want"))

while num >0:
    user1 = input("enter the choice...1.Stone,2.Paper,3.Seizor..")
    x=random.choice(a)

    if user1 == "Stone" and  x == "Paper" or user1=="Paper" and x=="Seizor" or user1=="Seizor" and x=="Stone":
      print("computer choice..",x)
      print("you lose..")
      comwin=comwin+1
      
   
    elif user1 ==x :
      print(x)
      print(user1)
      print("tie..Match")
     
    else:
      print("computer Choice..",x)
      print("you winn")
      userwin = userwin + 1

    num= num -1

  
if comwin > userwin:
     print("You lose ")
  
elif userwin > comwin:
      print("You Win the tournament..") 
       
