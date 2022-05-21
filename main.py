#Question 1
"""The problem is given a number 'n', calculate its factorial. The factorial of a number 'n' is defined as follows: 
n! = n (n - 1) (n-2) .... (1) 
That is, the product of all integers from 'n' until '1'. How can we calculate this using recursion ?"""
# 5! = 5*4*3*2*1
# 4! = 4*3*2*1
# 5! = 5*fact(4)

def factorial_ (n):
  if n == 1:
    return 1
  else:
    fac_n = n*factorial_(n-1)
    return fac_n
# factorial_(5) --> 5*factorial_(4) --> 5*24 = 120
# factorial_(4) --> 4*factorial_(3) --> 4*6 = 24
# factorial_(3) --> 3*factorial_(2) --> 3*2 = 6
# factorial_(2) --> 2*factorial_(1) --> 2*1 = 2
# factorial_(1) --> 1

print(factorial_(35))

#Question 2a
"""Fibonacci Sequence is a sequence of numbers that starts with '0' and '1', and after that each number in the sequence is the sum of the two previous numbers.
'0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....'
we can write the n^{th} element of the sequence as follows:
F(n) = F(n - 1) + F(n - 2)"""
#F(4) = 0, 1, 1, 2 --> 2
#F(4) = F(3) + F(2) --> 1 + 1 = 2
#F(3) = F(2) + F(1)  --> 1 + 0 = 1
#F(2) = 1
#F(1) = 0

def fib (n):
  if n == 1:
    return 0
  elif n == 2:
    return 1
  else: 
    fib_n = fib (n-1) + fib (n-2)
    return fib_n

print(fib(10))

#Question 2b
def fact_iterative(n):
  answer = 1
  for i in range(1, n+1):
    answer *= i
  return answer

print(fact_iterative(35))

#Version 2
def fib_iterative(n):
  before_previous = 0
  previous = 1
  answer = 0
  for x in range(1, n-1):
    answer = before_previous + previous
    before_previous = previous
    previous = answer
  return answer

print(fib_iterative(10))

#Question 3a
"""Write a recursive function which takes a base and a power and computes the base^power"""
# 2^4 = 2*2*2*2
# 2^4 = 2*2^3
# 2^3 = 2*2^2
# 2^2 = 2*2^1
# 2^1 = 2

def base_power (base, power):
  if power == 0:
    return 1
  else:
    power = power - 1
    rep = base*base_power(base, power)
    print(rep)
    return rep
    
print(base_power(8, 11))

#Question 3b
"""Write a iterative function which takes a base and a power and computes the base^power"""

def base_power_2 (base, power):
  base_1 = base
  for x in range (1,power):
    base_1 *= base
    print(base_1)
  return base_1
    
print(base_power_2(8, 11))

#Question 4
"""Implement a recursive algorithm that takes a number as an input and returns how many digits it has.
(HINT: Remember that if n is an integer, n/10 will be an integer without the fractional part.) 
12, 105, 15105"""

def count_digits (number):
  if number == 0:
    return number
  else:
    number = number // 10
    return (1 + count_digits(number))

print(count_digits(151055))

#Iterrative Version 
def count_digits_2 (number):
  base_c = 0
  while not(number == 0) :
    number = number//10
    base_c += 1
  return base_c

print(count_digits_2(151))

#Question 5
"""Write a recursive program that takes a list as an input and returns the maximum in that list"""
#[2,8,3,0,1,7,9,4]
#check if 2 is greater than max of the list below
#[8,3,0,1,7,9,4]
#[3,0,1,7,9,4]
#[0,1,7,9,4]
#[1,7,9,4]
#[7,9,4]
#[9,4]
#check if 9 is greater than max of the list below (4)
#[4]

def max_list (list_1):
  if len(list_1) == 1:
    return list_1[0]
  else:
    number_1 = list_1[0]
    list_1 = list_1[1:len(list_1)]
    if number_1 > max_list(list_1):
      return number_1
    else:
      return max_list(list_1)

print(max_list([2,8,3,0,19,2]))

#Iterrative version
def max_list_2 (list_1):
  base = 0
  for x in range(len(list_1)):
    if list_1[x] > base:
      base = list_1[x]
  return base
    
print(max_list_2([2,8,3,0,1,17,9,4]))

#Question 6
"""Write a recursive function that takes a number as an input and returns the addition of its digits.
Example: add_digit(12345) --> 15"""

def add_digit(n):
  if n//10 == 0:
    return n
  else:
    total = n%10 + add_digit(n//10)
    return total
    
print("The result",add_digit(12345))


#Question 7
"""Write a function using recursion that takes in a string and returns a reversed copy of the string. The only
string operation you are allowed to use is string concatenation
Example: reverse('dilara') --> 'aralid'"""

def reverse(n):
  index = len(n)-1
  if 1 == len(n):
    return n
  else:
    final = n[index] + reverse(n[0:index])
    return final

print(reverse('dilara'))


#Question 8
"""Write a function using recursion to print numbers from n to 0
Example: 
count_down(10) --> 
10
9
8
7
6
5
4
3
2
1
0
count_down(-4) --> 
-4
-3
-2
-1
0"""

def count_down(n):
  print(n)
  if n == 0:
    pass #return vide
  elif n > 0:
    count_down(n-1)
  else:
    count_down(n+1)
  
(count_down(-10))

#Question 9
"""Write a recursive program that returns the summation of the elements of given list."""
lst = [1, 2, [3,4], [5,6]]
#Result should be: 21"""

def summation(lst):
  lst = [1, 2, [3,4], [5,6]]
  index = len(lst)-1
  rep = 0
  if len(lst) == 1:
    return lst
  elif len(lst[index]) == 1 :
    print(rep)
    rep += summation(lst[0:index])
    return rep
  else: 
    lst[index] = summation(lst[index])

print(summation([1, 2, [3,4], [5,6]]))

# Question 10
"""Write a recursive program to calculate the harmonic sum of a number.
Note: The harmonic sum is the sum of reciprocals of the positive integers."""
#harmonic_sum(7) --> 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7

def harmonic_sum(num):
  if num == 0:
    return num
  else: 
    rep = harmonic_sum(num-1) + 1/num
    num -= 1
    return rep

print(harmonic_sum(7))

#Question 11
"""Write a Python program to find  the greatest common divisor (gcd) of two integers."""
#gcd(12,198) --> 6
#If you dont know the concept, gcd is the greatest number that divides both numbers. For instance, 2 also divides both 12 and 198 and 3 also divides both 12 and 198. But the largest number that divides both is 6. Hence, gcd=6

def gcd_1(num, num2):
  x = num
  lstx = []
  while not(x ==1) : 
    if x/2 == x//2:
      x = x/2
      a = 2
      lstx.append(a)
    elif x/3 == x//3:
      x = x/3
      a = 3
      lstx.append(a)
    elif x/5 == x//5:
      x = x/5
      a = 5
      lstx.append(a)
    elif x/7 == x//7:
      x = x/7
      a = 7
      lstx.append(a)
    elif x/11 == x//11:
      a = 11
      lstx.append(a)
  print(lstx)
  y = num2
  lsty = []
  while not(y == 1): 
    if y/2 == y//2:
      y= y/2
      a = 2
      lsty.append(a)
    elif y/3 == y//3:
      y = y/3
      a = 3
      lsty.append(a)
    elif y/5 == y//5:
      y = y/5
      a = 5
      lsty.append(a)
    elif y/7 == y//7:
      y = y/7
      a = 7
      lsty.append(a)
    elif y/11 == y//11:
      y = y/11
      a = 11
      lsty.append(a)
  print(lstx, lsty)
  z = list(set(lstx) & set(lsty))
  total = 1
  for x in range (len(z)):
    total = z[x]* total
  return total

#Version 2
def gcd(num, num2):
  x = find(num2)
  y = find(num)
  z = list(set(x) & set(y))
  total = 1
  for x in range (len(z)):
    total = z[x]* total
  return total

def find(x): 
  lstx = []
  while not((x ==1) or (x ==0)): 
    if x/2 == x//2:
      x = x/2
      a = 2
      lstx.append(a)
    elif x/3 == x//3:
      x = x/3
      a = 3
      lstx.append(a)
    elif x/5 == x//5:
      x = x/5
      a = 5
      lstx.append(a)
    elif x/7 == x//7:
      x = x/7
      a = 7
      lstx.append(a)
    elif x/11 == x//11:
      x = x/11
      a = 11
      lstx.append(a)
  return lstx

print("test1",gcd_1( 12, 198))

print("test2",gcd(12,198))
