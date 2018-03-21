RV=int(input())
RM=int(input())
RK=int(input())

if(RV>RM):
   if(RV>RK):
     print(RV)
   else:
     print(RK)
elif(RM>RK):
  print(RM)
else:
  print(RK)
