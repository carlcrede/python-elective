# Slicing exercises
#
# 1. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
# 2. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
# 3. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
# 4. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
# 5. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
# 6. ['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
# 7. ('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
# 8. 'Hello World Huston we are here' -> 'World Huston we'

s = ['Hello', 'World', 'Huston', 'we', 'are', 'here']
t = ('Hello', 'World', 'Huston', 'we', 'are', 'here')
aStr = 'Hello World Huston we are here'

# 1
ex1 = s[:-1]
print(ex1)

#2
ex2 = s[:2]
print(ex2)

#3
ex3 = s[-2:]
print(ex3)

#4
ex4 = s[-2:-1]
print(ex4)

#5
ex5 = s[::2]
print(ex5)

#6
ex6 = s[::-1]
print(ex6)

#7
ex7 = t[1:-1]
print(list(ex7))

#8
ex8 = aStr[aStr.index('World Huston we'):aStr.index('are')]
print(ex8)