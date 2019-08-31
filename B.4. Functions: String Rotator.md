## String Rotator

Write a Python function string_rotate to generate the desired pattern. The function should accept an integer as its single argument. 

Input and Output Format:
Input consists of a single integer that corresponds to n.
Assume that 0 < n <= 26. 
Refer sample output for output formatting specifications.
```
Sample Input1 : 5
Sample Output1:
ABCDE
BCDEA
CDEAB
DEABC
EABCD


Sample Input2 : 6
Sample Output2:
ABCDEF
BCDEFA
CDEFAB
DEFABC
EFABCD
FABCDE

```

## Python code:
```
def string_rotate(letter): 
  from string import ascii_uppercase 
  val = ascii_uppercase[0:letter] 
  res = val 
  for i in range(letter-1): 
    rotate = val[1:] + val[0]
    res += " " + rotate
    val = rotate
  return res

```
