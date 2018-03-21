a=int(input())

if(((a%400==0)||(a%100!=0))&&(a%4==0)):
   print("Leap Year")
else:
   print("Not a Leap Year")
