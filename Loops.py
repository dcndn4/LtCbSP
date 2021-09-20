# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 07:52:41 2021

@author: CS_Knit_tinK_SC
"""

secret_word = 'olive'
print(len(secret_word), 'iterations, coming right up!')
#%%
for char in secret_word:
        print('Letter: ' + char)
        print('*')
        
#%%
s = 'garage'
total = 0

# this results in 10 because the g counts as 2 (twice), same with the a. weird.

for char in s:
    total = total + s.count(char)
    print(total)
#%%

#method 'is upper case' ==> .isupper(), returns boolean value

print('q'.isupper())
print('Q'.isupper())

#%%

title = 'The Escape'
for char in title:
    if char.isupper():
        print(char)
        
#%%

letters = 'ABC'
digits = '123'

for letter in letters:
    for digit in digits:
        print(letter + digit)
#%%

title = 'The Escape'
total = 0

for char1 in title:
    for char2 in title:
        total = total + 1

# I think result will be a total equal to twice the # of characters

print(total)

# No, duh, it's 10 * 10! That makes sense.
#%%

for swap_type in swaps:
    # Big if statement to keep track of the ball
    #maybe later!