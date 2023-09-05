loop=""
while loop=="":
   loop3=False
   while not loop3:
      try:
         cost=int(input("input cost ratio (1 length per cost)"))
         if cost>0:
            loop3 = True
         else:
            print("please enter a number more than 0")
      except ValueError:
         print("please enter a number")
   loop1=False
   while not loop1:
      try:
         width =float(input("input width "))
         if width > 0:
            loop1=True
         else:
            print("enter a number more than 0")
            print()
      except ValueError:
         print("enter a number more than 0")
         print()
   loop2=False
   while not loop2:
      try:
         hight = float(input("input hight "))
         if hight > 0:
            loop2=True
         else:
            print("enter a number more than 0")
            print()
      except ValueError:
         print("enter a number more than 0")
         print()
   primiter = (2*width) + (hight*2)
   print()
   unit=input("enter mesurment symbol")
   money = input("enter monatry symbol")
   print()
   print("the cost of the perimiter is:", primiter*cost,money)
   print("the perimiter is:", primiter,unit)
   loop=input("press enter to rerun to end press any other key then enter")
print("thank you for useing this calucaluator goodbye")