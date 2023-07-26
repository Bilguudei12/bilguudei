import sys

inputNum = int(input("input integer : "))

if inputNum <=0:
     print("this is negative Num.")
     print("Program exit. ")
     sys.exit() 
else:
    if inputNum % 2== 0:
       print("Even Num")
    else:
       print("odd Num")
 
