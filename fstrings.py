# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:35:45 2021

@author: CS_Knit_tinK_SC
"""

plays = range(10)
print('Martha plays', plays[5], 'times before money is spent')

#%%
 
num1 = 7
num2 = 82
num3 = 11
print(f'We have {num1}, {num2}, and {num3}.')

#%%

print(type(f'hello'))
print(type(f'hello {num1}'))
#%%
print(f'the sum is {num1 + num2 + num3}')
#%%
# problem # 9 in chapter 4 - Song Playlist

button = 0

#%%

songs = 'ABCDE'
songs = songs[1] + songs[2] + songs[3] + songs[4] + songs[0]
print(songs)
#%%
s = 'abcdefghijk'
print(s[4:8])

print(s)
print(s[:])
#%%
songs = 'ABCDE'
songs = songs[1:] + songs[0]
print(songs)
#%%
game = 'Lost Vikings'
print(game[2:-6])
#%%
songs = 'ABCDE'
button = 0

# %%
#while button != 4:
    # Read button
    # Read number of presses
    # Process button press
    
# skipping over input process by setting value

press = 1
timespress = 1
    
while button != 4:
    button = press
    for i in range(timespress):
        if button == 1:
            songs = songs[1:0] + songs[0]
        elif button ==2:
            songs = songs[-1:] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]
output = ''
for song in songs:
            output = output + song + ''
print(output[:-1])
    #not having input process kind of muddies this up a bit
