
# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def sort_a_text(x):
    result = []
    for s in x.lower():
        if s not in vowels and s.strip(): # Cannot make it work any other way.
            result.append(s)
    return sorted(result)


# from solutions - smarter solutions than mine 
def sort_cons(s):
    for i in ['a', 'e', 'i', 'o', 'u', 'y', ' ']:
        s = s.lower().replace(i,'')
    
    return sorted(s)

def main():
    print('My solution: ', sort_a_text('Pizza with pineapple'))
    print("Teacher's solution: ", sort_cons('Hello World'))

main()