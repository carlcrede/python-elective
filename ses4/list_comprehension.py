#%% 
# Create a list of capital letters in the english alphabet
[ chr(x) for x in range(65, 91) ]


# %%
# Create a list of capital letter from the english aplhabet, 
# but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
[ chr(x) for x in range(65, 91) if x not in [70, 75, 80, 85] ]

# %%
# Create a list of capital letter from from the english aplhabet, 
# but exclude every second between F & O
[ chr(x) for x in range(65, 91) if x not in range(71, 79, 2) ]
