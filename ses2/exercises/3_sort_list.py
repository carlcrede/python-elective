
# Create a list of strings with names in it. (l = [‘Claus’, ‘Ib’, ‘Per’])
# 1. Sort this list by using the sorted() build in function.
# 2. Sort the list in reversed order.
# 3. Sort the list on the lenght of the name.
# 4. Sort the list based on the last letter in the name.
# 5. Sort the list with the names where the letter ‘a’ is in the name first.

l = ['Claus', 'Ib', 'Per', 'Mogens', 'Albert', 'Jonas']

# 1
ex1 = sorted(l)
print(f'List sorted with sorted() {ex1}')

# 2
ex2 = sorted(l, reverse=True)
print(f'List sorted in reversed order with sorted(): {ex2}')

# 3
ex3 = sorted(l, key=len)
print(f'List sorted by lenght: {ex3}')

# 4
def reverse_word(word):
    return word[::-1]

# Note: can also be done with lambda:  key = lambda x: x[::-1]
# Every word is reversed and then used to sort - but data is not changed, since sorted() returns new list
ex4 = sorted(l, key=reverse_word)
print(f'List sorted by last letter: {ex4}')

# 5
# Not working as intended. Will sort word based by position of 'a', 
# but shorter words without an a is still sorted before longer words containing a..
ex5 = sorted(l, key = lambda x: x.split('a'))
print(f'List sorted by index of "a": {ex5}')

# Teacher's solution
"""
def a_in(s):
    if 'a' in s.lower():
        return True
    return False

sorted(names, key=a_in)
"""