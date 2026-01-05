# 1st Question
#WAF to print the length of a list. (list is the parameter)


cities = ["delhi","mummbai","rajkot","ahemdabad","noida"]
cricketer = ["Hitman", "king", "thala", "god"]

def len_list(list):
  print(len(list))

# len_list(cities)
# len_list(cricketer)


# 2nd Question
# WAF to print the elements of a list in a single line.(list is the parameter)

def print_list(list):
   for item in list:
      print(item, end=" ")


# print_list(cities)
# print_list(cricketer)

# 3rd Question
# WAF to find the factorial of n.(n is the parameter)
 

def calc_fact(n):
   fact = 1
   for i in range (1,n+1):
      fact *= i
   print(fact)
  
# calc_fact(5)

# 4 Question
#WAF to convert USD to INR.

def converter(usd_val):
   inr_val = usd_val * 83
   print(usd_val, "USD =" , inr_val , "INR")

# converter(20)
