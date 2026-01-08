
### 1. Create function called sum which return sum of two numbers.

def calc_sum(a,b):
  c = a + b
  return c


print(calc_sum(10,12))


### 2. Write a function called `greet()` that prints the message:

def message():
  print("hello Raj")


message()


### 3. Write a function called square that takes one number as a parameter and returns its square.

def squre(a,b):
  squre = a**b
  return squre

print(squre(10,4))



### 4. Write a function named check_even_odd that takes a number as input and prints whether the number is Even or Odd.

def even_odd(num):
  if num % 2 == 0:
    print("It Is Even")
  else:
    print("It Is Odd")
  return 

even_odd(8)

# ### 5. Write a function called power that takes:
# > base
# > exponent (default value = 2)
# > The function should return base raised to the power of exponent.

def power(base, exponent=2):
    return base ** exponent
print(power(5))  
print(power(5, 3))  

