a = int(input())
if (a%3 == 0) and (a%5 == 0) and (a%7 == 0):
  print("JugsMugsPugs")
elif (a%3 == 0) and (a%5 == 0):
  print("JugsMugs")
elif (a%3 == 0) and (a%7 == 0):
  print("JugsPugs")
elif (a%5 == 0) and (a%7 == 0):
  print("MugsPugs")
elif (a%3 == 0):
  print("Jugs")
elif (a%5 == 0):
  print("Mugs")
elif (a%7 == 0):
  print("Pugs")
else:
  print(a)
