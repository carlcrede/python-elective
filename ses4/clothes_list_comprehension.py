# %%
# From 2 lists, using a list comprehension, create a list containing:
# [('Black', 's'), ('Black', 'm'), ('Black', 'l'), ('Black', 'xl'), 
#  ('White', 's'), ('White', 'm'), ('White', 'l'), ('White', 'xl')]
# colors = ['Black', 'White']
# sizes = ['s', 'm', 'l', 'xl']
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']

[ (c, s) for c in colors for s in sizes ]

# %%
# If the tuple pair is in the following list, it should not be added to the comprehension generated list.
# soled_out = [('Black', 'm'), ('White', 's')]
soled_out = [('Black', 'm'), ('White', 's')]
[ (c, s) for c in colors for s in sizes if (c, s) not in soled_out ]


# %%
