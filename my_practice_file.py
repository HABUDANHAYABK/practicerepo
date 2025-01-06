def formatted_name(first_name, last_name, middle_name):
    """Return my full name neatly formatted """
    if middle_name:
       full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
my_info = formatted_name(first_name='abubakar', middle_name='muhammad', last_name='danhaya')
print(my_info)

# when middle name is optional

def formatted_name(first_name, last_name, middle_name=''):
    """Return my full name neatly formatted """
    if middle_name:
       full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
my_info = formatted_name(first_name='abubakar', last_name='danhaya')
print(my_info)

# building a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_mydict(first_name, last_name):
    """Return my dictionary of personal data"""
    mydict = {'first': first_name, 'last': last_name}
    return mydict
my_bio = build_mydict('abubakar', 'danhaya')
print(my_bio)

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def build_mydict(first_name, last_name, age=None):
    """returndictionary of my personal data"""
    my_dict = {'first': first_name, 'last': last_name}
    if age:
        my_dict['age'] = age
    return my_dict

my_data = build_mydict('abubakar', 'danhaya', 26)
print(my_data)

# fuction with while loop
def formatted_name(first_name, last_name):
    """Return full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell your name")
    print("Enter 'q' to cancel at any time")
    f_name = input("Enter your first name")
    if f_name == 'q':
        break
    l_name = input("Enter your last name")
    if l_name == 'q':
        break
my_name = formatted_name(f_name, l_name)
print(my_name)

#passing a list in function

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


def greet_user(names):
    """Display simple greeting"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
         

usernames = ['abubakar', 'sani', 'mike', 'daniel', 'muhammad', 'john']
greet_user(usernames)

# Modifying a list in a function

unprinted_design = ['T-shirt', 'phone case', 'sticker']
completed_models = []
# let me use while loop to append
while unprinted_design:
    current_model = unprinted_design.pop()
    print(f"printing model: {current_model}")
    completed_models.append(current_model)
# Displaying all the models
print("\nThe following are completed models:")
for completed_model in completed_models:
    print(completed_model)