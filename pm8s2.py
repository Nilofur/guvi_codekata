l=int(input())

u=int(input())

for num in range (l+1,u+1):

    sum=0
  
    t=num
   
    while t>0:

      dig=t%10
 
      sum+=dig**3
  
      t//=10

    if num==sum:
  
       print(sum)