# 1.FizzBuzz

Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:
</br></br></br>
+ If i is a multiple of both 3 and 5, print FizzBuzz
+ If i is a multiple of 3(but not 5), print Fizz
+ If i is a multiple of 5(but not 3), print Buzz
+ If i is not a multiple of 3 or 5, print the value of i.<br>

__Function Description__
Complete the function FizzBuzz in the editor below.<br>

fizzBuzz has the following parametr(s):
    int n: upper limit of values to test(inclusive)
Returns: None
Prints:
    The function must print the appropriate response for each value i in the set {1,2, ... n} in ascending order, each on a separate line.
    
 __Constraints__
 * 0 < n < 2 x 10^5<br><br>
 __SAMPLE INPUT__
 ```
 STDIN    Function
-----    --------
15    →  n = 15
 ```
__SAMPLE OUTPUT__
```
1     
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```
__EXPLANATION__
> The numbers 3, 6, 9, and 12 are multiples of 3(but not 5), so print Fizz on those lines.
> The numbers 5 and 10 are multiples of 5(but not 3), so print Buzz on those lines.
> The number 15 is a multiple of both 3 and 5, so print FizzBuzz on that line.
> None of the other values are multiples of 3 or 5, so print values of i on those lines.
