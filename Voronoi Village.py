# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 11:24:09 2021

@author: CS_Knit_tinK_SC
"""
[20, 50, 4, 19, 15, 1]
print([1, 2, 3] + [4, 5, 6])

print('one' in ['one', 'two', 'three'])
print(len(['one', 'two', 'hello']))
#%%
for value in [20, 50, 4, 19, 15, 1]:
    print(value)
# works .. list doesn't have a name or anything?!!
#%%
stringgroup = ['one', 'two', 'hello']
print(stringgroup[2])
print(stringgroup[2][1])
#%%

dish = ['h', 'e', 'l', 'l', 'o']
print(dish)
dish[0]='j'
print(dish)
dish[2] = 'x'
print(dish)
#%%
dish = ['abc', 'def', 'ghi']
dish[1] = 'zyx'
print(len(dish))
#%%
input
5
print(input)
#%%

# original data: Village = [5, 16, 0, 10, 4, 15]
Village = [0, 4, 5, 10, 15, 16]
position = []
#%%

for i in range(6):

    left = (Village[i] - Village[0])/2
    right = (Village[2] - Village[1])/2
    min_size = left + right
    print (min_size)
#%%

for i in range(6):
    left = (Village[i] - Village[i - 1])/2
    right = (Village[i + 1] - Village[i])/2
    size = left + right
    if size < min_size:
        min_size = size
