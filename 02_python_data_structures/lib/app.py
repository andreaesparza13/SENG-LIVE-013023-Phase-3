# Sequence Types
    
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
# #2. ✅ Return the first pet name
print(pet_names[0])

# #3. ✅ Return all pet names beginning from the 3rd index
# # ^ Includes pet_names[3]
print(pet_names[3:])

# #4. ✅ Return all pet names before the 3rd index
# # ^ Does NOT include pet_names[3]
print(pet_names[:3])

# #5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index
print(pet_names[3:8])

# #6. ✅ Find the index of a given element => .index()
print(pet_names.index("Luke"))

#7. ✅ Reverse the original list => .reverse()
# ^ Destructive => completely reassigns the indexes of pet_names 
# pet_names.reverse()
# print(pet_names)

# ^ NOT destructive => original pet_names remains the same
print(pet_names[::-1])

#8. ✅ Return the frequency of a given element => .count()
print(pet_names.count("Luke"))

# Updating Lists
#9. ✅ Change the first pet_name to all uppercase letters => .upper()
# ^ NOT destructive
print(pet_names[0].upper())

#10. ✅ Append a new name to the list => .append()
# ^ Destructive
pet_names.append("Lady")
print(pet_names)

#11. ✅ Add a new name at a specific index => .insert()
# ^ Destructive
pet_names.insert(2, "Spider")
print(pet_names)

#12. ✅ Add two lists together => +
print([1, 2, 3] + [4, 5, 6])

#13. ✅ Remove the final element from the list => .pop()
# ^ Destructive BUT returns that removed (popped) element
pet_names.pop()
print(pet_names)

#14. ✅ Remove element by specific index => .pop()
# ^ Destructive
pet_names.pop(2)
print(pet_names)

#15. ✅ Remove a specific element by it's string => .remove()
# ^ Destructive BUT will only remove the first instance of it, not all instances if an element has duplicates
pet_names.remove("Paul")
print(pet_names)

#16. ✅ Remove all pet names from the list => .clear()
# ^ Destructive
pet_names.clear()
print(pet_names)

#Tuple
# 📚 Review:
    # List, Tuple <=> Mutable, Immutable <=> Changeable, Unchangeable
    
    # Why Are Tuples Immutable?

        # What advantages does this provide for us? In what situations
        # would this serve us?

        # Tuples are useful for representing static data (not dynamic or alterable)

#17. ✅ Create a Tuple of 10 pet ages => () 
pet_ages = (1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6, 7, 8, 9, 9, 9)

#18. ✅ Print the first pet age => []
print(pet_ages[0])

# Testing Mutability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# ! pet_ages.pop() => AttributeError: 'tuple' object has no attribute 'pop'

#20. ✅ Attempt to change the first element (should error) => []
# ! pet_ages[2] = 4 => TypeError: 'tuple' object does not support item assignment

# Tuple Methods
#21. ✅ Return the frequency of a given element => .count()
print(pet_ages.count(5))

#22. ✅ Return the index of a given element  => .index()
print(pet_ages.index(5))

#23. ✅ Create a Range 
# Note:  Ranges are primarily used in loops
# ^ This will print all the values from 0 to 19 because it does not include 20
my_range = range(20)
for num in my_range:
   print(num)

# Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}

# Dictionaries (Remind us of objects in JS formatted like json)
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
# The advantage here is that it minimizes possibility of keystroke errors
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
print(pet_info_rose['name']) # Returns "Rose"
# ! print(pet_info_rose['temperament']) => Returns "KeyError: 'temperament'"

#28. ✅ Print the pet attribute of "age" using ".get"
# get() is a built in dictionary method
# ^ Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error

print(pet_info_rose.get('name')) # Returns 'Rose'
print(pet_info_rose.get('temperament')) # Returns "None"

# Updating 
#29. ✅ Update Rose's age to 12 => []
# ^ Bracket notation will work for this but .get() will not work to update values
pet_info_rose['age'] = 12
print(pet_info_rose)

#30. ✅ Update Spot's age to 26 => .update({...})
pet_info_spot.update({'age':26})
print(pet_info_spot)

# Deleting
#31. ✅ Delete Rose's age using the "del" keyword => []
# ^ Built in 'del' is destructive
del pet_info_rose['age']
print(pet_info_rose)

#32. ✅ Delete Spot's age using ".pop"
# ^ pop() is destructive BUT the return is the value of the key:value pair which we can capture in a variable
pet_info_rose.pop('name') # Returns 12 because that's the value of age
print(pet_info_rose)

#33. ✅ Delete the last item for Rose using "popitem()"
# ^ Destructive and don't need anything in parenthesis either
pet_info_rose.popitem() # Returns a TUPLE containing 2 items: (key, value)
print(pet_info_rose)

# Loops 
# Below is a List of Dictionaries 
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#34. ✅ Loop through a range of 10 and print every number within the range
my_range_2 = range(10)
for num in my_range_2:
   print(num)

#35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
my_range_3 = range(50, 60, 2)
for num in my_range_3:
   print(num)

#36. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info:
   print(pet)

#37. ✅ Create a function that takes a list a parameter 
# The function should use a "for" loop to loop through the list and print each item 
def output_pet_names(list):
   for pet in list:
      print(pet)

# Invoke the function and pass it "pet_names" as an argument
output_pet_names(pet_info)

#38. ✅ Create a function that takes a list as a parameter
    # The function should define a variable ("counter") and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Once the loop has finished, return the final value of "counter"
def return_pet_count(list):
    counter = 0
    while (counter < len(list)):
        counter += 1
    return counter

print(return_pet_count(pet_info))

#39. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dictionaries", "name" and "age" as parameters 
        # Create an index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param 
            # and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dictionary containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'Pet not found'
def update_pet_age(list, name, age):
    i = 0
    while(i<(len(list)-1) and list[i]['name'] != name):
        i += 1
    if (list[i]['name'] == name):
        list[i]['age'] = age
        return list
    else:
        return "Pet Not Found"

# map like 
#40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# def to_upper(name):
#     name = name.upper()

# pet_names_to_upper = map(to_upper, pet_names)
# print(list(pet_names_to_upper))
new_pet_list = [pet.get('name').upper() for pet in pet_info]
print(new_pet_list)

# find like
#41. ✅ Use list comprehension to find a pet named spot
# spot = [RETURNED PET / LOOP / CONDITIONAL]
spot = [pet for pet in pet_info if pet.get("name") == 'Spot' ]
print(spot)

# filter like
#42. ✅ Use list comprehension to find all of the pets under 3 years old
# young_pets = [RETURNED PET / LOOP / CONDITIONAL]
young_pets = [pet for pet in pet_info if pet.get("age") < 2]
print(len(young_pets))

#43. ✅ Create a generator expression matching the filter above
# ^ Main Benefit => Less Memory Intensive

young_pets = (pet for pet in pet_info if pet.get("age") < 26)

# ^ Accessing Generator Object Values

# 1. Using next()
print(next(young_pets))
print(next(young_pets))
print(next(young_pets))

# 2. Using a for loop
for pet in young_pets:
    print(pet)