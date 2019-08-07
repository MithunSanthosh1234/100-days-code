num = int(input())
while(num%3==0 or num%5==0 or num%7==0):
  if(num%3==0):
    print("Jugs")
  if(num%5==0):
    print("Mugs")
  if(num%7==0):
    print("Pugs")
    
  break
else:
    print(num)
