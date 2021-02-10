
# Create a function that takes a string as a parameter and returns a list.
# The function should remove all vowels and sort the consonants in alphabetic order, and the return the result.

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def sort_a_text(x):
    result = []
    for s in x.lower():
        if s not in vowels and s.strip(): # Cannot make it work any other way. Seems that 
            result.append(s)
    return sorted(result)


def main():
    print(sort_a_text('Pizza with pineapple'))

main()