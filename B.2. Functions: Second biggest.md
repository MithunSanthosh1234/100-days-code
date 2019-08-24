## Second Largest
Write a function second_is_second_largest that will return True if the 2nd largest value is in the 2nd position. Otherwise, return False.

The function should accept three arguments. 


```
Example 
second_is_second_largest(1, 2, 3) -> True 
second_is_second_largest(11, 10, 9) -> True
second_is_second_largest(3, 3, 0) -> False 
second_is_second_largest(3, 2, 2) -> False 

```


# Python Code:

```
def second_is_second_largest(num1, num2, num3): 
  
  if(num1<num2<num3 or num1>num2>num3):
    return True
  else:
    return False
  
    
      
```
