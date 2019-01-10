
# Create a tuple named zoo that contains your favorite animals.
zoo = ('Lion', 'Polar Bear', 'Meerkat')

# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index('Meerkat'))

# Determine if an animal is in your tuple by using value in tuple.
if 'Elephant' in zoo:
    print('We have an elephant!')
else:
    print('No elephants here.')

# Create a variable for each of the animals in your tuple with this cool feature of Python.

(death_kitty, snow_teddy, desert_hole_rat) = zoo
print(death_kitty)

# Convert your tuple into a list.
zoo = list(zoo)
print(zoo)

# Use extend() to add three more animals to your zoo.
zoo.extend(['Chimpanzee', 'Cheetah', 'Ostrich'])

# Convert the list back into a tuple.
zoo = tuple(zoo)
print(zoo)