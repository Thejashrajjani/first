import random
a=[1,2,3,4,5,6,7,8,9,0]


while True:
        mobile_number= (input("enter mobile number"))
        length= len(mobile_number)
        if length == 10:
               b= random.sample(a)
               print("your OTP is..",b)
               break
        else :
             print("enetr the valid number..")
        