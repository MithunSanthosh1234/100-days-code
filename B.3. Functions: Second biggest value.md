## Second Biggest Value
Write a function second_biggest_value which accepts three integers, and does the following:
returns the second biggest value among the three
returns “NA” if there are two or more equal values.

```
Example

(1, 2, 3) -> 2
(3, 1, -1) -> 1
(3, 5, -1) -> 3
(3, -1, -1) -> "NA"
```

## Python Code:

```
def second_biggest_value(num1,num2, num3): 
  if ((num1 < num2 < num3) or (num1 > num2 > num3)):
    return num2
  elif ((num2 < num1 < num3) or (num2 > num1 > num3)):
    return num1
  elif ((num2 < num3 < num1) or (num2 > num3 > num1)):
    return num3
  else:
    return 'NA'
```
