# Exam Synopsis (Template)

This synopsis should be handed in on wiseflow a few weeks before the oral exam. 

## 1. Data Structures & functions

Topics brainstorm:
- List, Tuple, Set, Dict, list comprehension, dict comprehension
- Files (read, write, context manager)
- Built-in functions (sorted, len, dir, zip, input, open, print, range, str, repr, type, )
- Funcion definitions, return values, parameters

Ideas for presentation:
1) Focus on files - I will show how to read and write textfiles in a couple of ways, and how to read a file into a list. Then I will demonstrate how to use some built-in functions on the list, eg. sorted and len. 
If there is time I will also loop through the list and demonstrate the use of range and print.

2) Focus on functions - I will show how to create a simple function definition, how to give it parameters and how to return values. Also I will give an example of how to decorate a function with a simple timer.

## 2. Pythonic OOP

Topics brainstorm:
- args, kwargs
- encapsulation, properties annotation, public variables
- inheritance
- dunder methods

Ideas for presentation:
1) Focus on the python datamodel 'dunder'/magic methods - I will give examples of how we can implement different dunder-methods such as __len__, __repr__, __str__, __add__ etc for some class.

## 3. Generators, Decorators & Context Managers

Topics brainstorm:
- decorator - how is it used? why is it good
- generator - generator expression
- idea: function that makes a list vs generator function - time it with own decorator (see ses10)
- context managers 

Ideas for presentation:
1) Focus on generator and decorator - I will make a function that returns a list of size n and a generator function that also constructs a list of size n - then I will make a timer decorator function and then decorate
the two functions to see their time difference.

## 4. Python modules and the python development environment. 

Topic brainstorm:
- installation and use of a 3rd party module (eg. requests) - pip
- freeze dependencies
- built-in modules: eg. time and random, os, subprocess, zipfile
- how to run python file, REPL
- how to use python with docker
- jupyter notebook

Presentation ideas:
1) Focus on modules - I will demonstrate how to install and use a 3rd party module (probably requests) and then I will demonstrate how to use some built-in modules (eg. time, random, os, subprocess).

2) Focus on developement environment - I will demonstrate how to run a .py file in the terminal and how to use the REPL. Then I will show how to run python in a docker container. If there is time I will also demonstrate how to run a jupyter notebook.