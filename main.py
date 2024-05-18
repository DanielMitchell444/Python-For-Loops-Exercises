'''
Within this section, there is another important tool that we need 
to learn that is related to arrays. And that tool is for loops.
There are 2 types of loops in Python, for loops, and while loops.
We will get to while loops later, but for now, lets focus on for
loops
A for loop is used for iterating over a sequence such as lists,
strings, tuples, dictionaries, and sets. We will get to 
tuples, dictionaries, and sets later, but for now we will
be primarily focusing on strings and lists.
for loops typically loop through once through each item
of a list.
For example, lets say we have a list of fruits like so
'''

fruits = ["Apples", "Banana", "Cherry"]

'''
We can loop through the list like so
'''

for x in fruits:
    print(x)

'''
You might be asking yourself, what is x? Well, x is essentially
just each list item without the list, while fruits would be the
individual lists printed out 3 times
for example, if you print out x, you will see
Apple
banana
cherry

but if you print out fruits, you will see the list we created printed
out 3 times
'''

'''
PRACTICE:
Below this comment, i want you to create your own list and then
loop through it using a for loop. After that, i want you to
print out the list individually. Please post the code below this
comment
'''

'''
BREAK STATEMENT:
The break statement essentially stops the loop before it has
looped through all the items. For example, if we made
something like this
'''
for x in fruits:
  print(x)
  if x == "banana":
    break
  
'''
Like we learned during the conditional lessons, we are essentially
looping through the loops array, printing each individual list
item, and then checking to see if x is equal to banana, when
x does equal banana, it would essentially stop the loop
'''

'''
PRACTICE:
Below this comment, i want you to loop through the array
you created above, below the for loop, i want you to
print out each individual index, and then check to see
if a list item is equal. Then, i want you to use the break
statement
'''


'''
CONTINUE STATEMENT:
The continue stops the current iteration of the loop and
continues with the next item.
For example, if we do something like so
'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

'''
This would essentially not print banana, since
when the individual item is equal to banana, it would
continue to the next iteration.
'''


'''
RANGE FUNCTION
We can also set a for loop to only loop for a specific number of times,
that is the range function. The range function returns a sequence
of numbers, starting at 0, and increments by 1 and ends at
a specific number
for example, lets say we want to loop through 5 numbers,
we can do this like so
'''

for x in range(5):
  print(x)

'''
This would loop through x 5 times, but it would only show numebrs
up to 4, because lists start at 0.
You can also specify a range like so
'''

for y in range(2,6):
  print(x)

'''
This would not include 6, it would only show numbers 2 through 5.


PRACTICE:
Below this comment, i want you to loop through numbers using
a for loop, loop through numbers 2 through 10 and then print
out each number. Post this below this comment
'''

'''
ELSE KEYWORD:
The else keyword specifies a block of code to be executed
when the loop has ended. We can do this like so
'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")


'''
NESTED FOR LOOPS
A nested for loop is essentially a loop inside a loop.
The inner loop will be executed one time for each iteration
of the outer loop. For example, if we have something
like this.
'''

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

'''
It would essentially just print out red with every
individual list item in fruits, and go on. Its easier
to just show you the output.
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry

I will explain this better in person lol.
'''