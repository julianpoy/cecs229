import math

# 1.
print('1:')
re = (sum(673, 909) % 3 == 0)

print(re)

# 2.
print('2:')
r = {2**x for x in {0,1,2,3}}

print(r)

# 3
print('3:')
r = {x * y for x in {9,2,3} for y in {4,5,8}}

print(r)

# 4
print('4:')
r = [[x,y] for x in ['A', 'B', 'C'] for y in [1,2,3]]

print(r)

# 5
# a)
print('5 - a:')
S = {-4,-2,1,2,5,0}

r = [[x, y, z] for x in S for y in S for z in S if (x + y + z) == 0]

print(r)

# b)
print('5 - b:')
r = [[x, y, z] for x in S for y in S for z in S if (x + y + z) == 0 if {x,y,z} != {0,0,0}]
print(r)
