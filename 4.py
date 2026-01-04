a = 6
b = 4
c = 3
d = 2

# result = a * b ** c // d + a % b * c - a / (b - c) + d ** (a % c)

# b ** c = ?

# a * (b ** c) = ?

# (a * b ** c) // d = ?

# a % b = ?

# (a % b) * c = ?

# b - c = ?

# a / (b - c) = ?

# a % c = ?

# d ** (a % c) = ?

# result = [step3] + [step5] - [step7] + [step9]


print(b**c)
print( a * (b ** c) )
print((a * b ** c) // d)
print(a % b)
print((a % b) * c)
print(b - c)
print(a / (b - c))
print( a % c)
print(d ** (a % c) )
print(192+6-6+1)


# # ans : 
# 64
# 384
# 192
# 2
# 6
# 1
# 6.0
# 0
# 1