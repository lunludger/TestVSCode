# Creating dictionaries

int_key_dict = {1: 'apple',
                2: 'banana',
                3: 'orange'
                }

print(int_key_dict)

# Dictionaries can also be created from a list with the dict() function
int_key_list = [(1, 'apple'), (2, 'banana'), (3, 'orange')]
int_key_dict = dict(int_key_list)

# Pattern matching where you assign certain values to certain variables
my_tuple = (3, 'orange')
key, value = my_tuple
print(key)  # prints 1
print(value)  # prints apple

# Accessing elements from a dictionary
profile_dict = {'name': 'Chris',
                'surname': 'Smith',
                'age': '28',
                'cell': '083 233 3242'
                }

print(profile_dict['surname']) # Prints out 'Smith'
print(profile_dict['name'])
print(profile_dict.get('cell'))
print(profile_dict.get('age'))

# You can also iterate over all the keys and all the values with the .keys() and .values() methods respectively
keys = profile_dict.keys()
values = profile_dict.values()

print(keys)
print(values)

# Changing elements in a dictionary
# We can add or change items using the assignment operator(=). If there is already a key present, the value gets updated. Otherwise if there
# is no key a new key-value pair is added
profile_dict['age'] = 29 # Changing value for "age"
print(profile_dict)

profile_dict['gender'] = "Male"  # adding new key-value pair
print(profile_dict)

# Dictionary membership test _
doubles = {1: 2,
           2: 4,
           3: 6,
           4: 8,
           5: 10
          }

print(8 in doubles) # Prints out True