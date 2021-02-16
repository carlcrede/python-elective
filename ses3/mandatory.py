# Mandatory assignment for Python elective

import sys
"""
1)
Model an organisation of employees, management and board of directors in 3 sets.
Board of directors: Benny, Hans, Tine, Mille, Torben, Troels, Søren

Management: Tine, Trunte, Rane

Employees: Niels, Anna, Tine, Ole, Trunte, Bent, Rane, Allan, Stine, Claus, James, Lars

- who in the board of directors is not an employee?
- who in the board of directors is also an employee?
- how many of the management is also member of the board?
- All members of the managent also an employee
- All members of the management also in the board?
- Who is an employee, member of the management, and a member of the board?
- Who of the employee is neither a memeber or the board or management?
"""

directors = set(['Benny', 'Hans', 'Tine', 'Mille', 'Torben', 'Troels', 'Søren'])
management = set(['Tine', 'Trunte', 'Rane'])
employees = set(['Niels', 'Anna', 'Ole', 'Trunte', 'Bent', 'Rane', 'Allan', 'Stine', 'Claus', 'James', 'Lars'])

print(f'The organisation in 3 sets:\n{directors}\n{management}\n{employees}')


"""
2)
Using a list comprehension create a list of tuples from the folowing datastructure
{‘a’: ‘Alpha’, ‘b’ : ‘Beta’, ‘g’: ‘Gamma’}
"""

data = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}
l = [ (k, v) for k, v in data.items() ]
print(f'List of tuples: {l}')


"""
3)
From these 2 sets:
{'a', 'e', 'i', 'o', 'u', 'y'}

{'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

Of the 2 sets create a:

Union
Symmetric Difference
Difference
disjoint
"""

a = {'a', 'e', 'i', 'o', 'u', 'y'}
b = {'a', 'e', 'i', 'o', 'u', 'y', 'æ' ,'ø', 'å'}

# Union by operator
print(f'Union by operator: {a | b}')

# Union by method
print(f'Union by method: {a.union(b)}')


# Symmetric difference by operator
print(f'Symmetric difference by operator: {a ^ b}')

# Symmetric difference by method
print(f'Symmetric difference by method: {a.symmetric_difference(b)}')


# Difference by operator
print(f'Difference by operator: {b - a}')

# Difference by method
print(f'Difference by method: {b.difference(a)}')


# Disjoint by method - if True, the two sets have nothing in common (Disjoint), and a & b returns empty set -
# else it returns the intersection
print(f'Check if disjoint by method: {a.isdisjoint(b)}')

# Disjoint by operator
print(f'Empty set if disjoint, else intersection: {a & b}')


"""
Date Decoder.
A date of the form 8-MAR-85 includes the name of the month, which must be translated to a number.

Create a dict suitable for decoding month names to numbers.

Create a function which uses string operations to split the date into 3 items using the "-" character.

Translate the month, correct the year to include all of the digits.

The function will accept a date in the "dd-MMM-yy" format and respond with a tuple of ( y , m , d ).
"""

months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
    'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 
    'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
}

def translate_month(date):
    date = date.lower().split('-')
    day = date[0]
    month = months.get(date[1])
    year = date[2]
    return ('19' + year, month, day)
    
print(f'Date after decoding month: {translate_month("08-MAR-85")}')


# Alternative solution using sys.argv to get user input
# print(translate_month(sys.argv[1]))