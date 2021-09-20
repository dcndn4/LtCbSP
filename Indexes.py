# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:23:08 2021

@author: CS_Knit_tinK_SC
"""

word = 'splore'
print(word[0])
print(word[3])
print(word[5])
where = 2
print(word[where])
print(word[where+2])
print(word[-2])
print(word[-1])
#%%
s = 'abcde'
t = s[0] + s[-5] + s[len(s)-5]

#each of these indices refer to the first item in the string
#%%

# range function generates set of integers,
# which can serve to control loops via specified integer set.

# when argument = 1 integer, the set of integers produced 
# is 0 to that integer-1.
# when argument is integer,integer, the set of integers 
# goes from the first argument to the second argument-1

# if argument has a 3rd value, that value tells the size of the steps


for num in range(5):
    print(num)
#%%
for num in range (3, 7):
    print(num)
#%%

for num in range (0, 10, 2):
    print(num)

for num in range(0, 10, 3):
    print(num)
#%%

# this statement doesn't function, because ranges by definition count up

for num in range(6, 2):
    print(num)
#%%

# in order to make range act in non-default manner, 
# have to tell it to do so by 3rd argument being negative step command


for num in range (6, 2, -1):
    print(num)
#%%
list(range(3,7))
# if working in terminal, that command would show result
# here in spyder, have to tell it to print to get result

print(list(range(3,7)))
print(list)

#%%

for i in range (10, 20):
    print('jump up and down ', i)
#%%
num = 0
while num < 5:
    print(num)
    num += 1
#%%

num = 0
while num < 10:
    print(num)
    num = num + 3
#%%

n = 3
while n > 0:
    if n == 5:
        n = -100
    print(n)
    n += 1
    #%%
x = 6
while x > 4:
    x += -1
    print(x)
#%%

i = 0
while i < 3:
    j = 8
    while j < 11:
        print(i, j)
        j += 1
    i += 1
    #%%
x = 0
y = 1
while x < 3:
    while y < 3:
        print(x,y)
        y += 1
    x += 1
#%%
x = 4
y = 10
while x <= 10 and y <= 13:
    print(x,y)
    x += 1
    y += 1