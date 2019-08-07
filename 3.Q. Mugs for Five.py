a = int(input())
if (a%3 == 0) and (a%5 == 0):
  print("JugsMugs")
elif (a%3 == 0):
  print("Jugs")
elif (a%5 == 0):
  print("Mugs")
else:
  print(a)
