# Defination of a function
def greet_user():
    """Display a sinmple greeting"""
    print('Hello user')

greet_user()

def morining_greeting(username):
    '''Display morning greeting to user'''
    print("Good morining", (username).title)

morining_greeting('umar')

def product_of_two_numbers():
    """display the product of two numbers"""
    num1 = int(input("Enter a first number"))
    num2 = int(input("Enter another number"))
    product = num1 * num2
    print(f"{num1} x {num2} = {product}")

product_of_two_numbers()

# students information
def student_information(name, level, faculty):
    """Display student level and his/her faculty"""
    print(f"good day {name}")
    print(f"You are a {level} level student from faculty of {faculty.title}")

student_information('abubakar','2', 'enginering')

student_information(name='abubakar', level='2', faculty='engineering')

#personal infromation
def get_formatted_name(first_name, last_name):
    """ return full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
magician = get_formatted_name('john', 'mike')
print(magician)

def my_full_name(first_name, middle_name, surname):
    """return my full name """
    full_name = f"{first_name} {middle_name} {surname}"
    return full_name.title()
student_bio = my_full_name(first_name='abubakar', middle_name='muhammad', surname='danhaya')
print(student_bio)

#Returning to a dictionary
def build_person(first_name, last_name, age=None):
    """Returning to a dictionary"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person[age] = age
    return build_person
my_information = build_person('abubakar', 'danhaya')
print(my_information)

def my_info(first_name, last_name, city, age=None):
    """my information"""
    info = {'first': first_name, 'last': last_name, 'state': city}
    if age:
        info[age] = age
    return my_info
bio_data = my_info('abubakar', 'danhaya', 'jigawa')
print(bio_data)


# Function with while loop
def formatted_name(first_name, last_name):
    """Return formatted name neatly"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nplease tell me your name")
    print("Enter 'q' to cancel at any time")
    f_name = input("Enter your first name")
    if f_name == 'q':
        break
    l_name = input("Enter your last name")
    if l_name == 'q':
        break
my_name = formatted_name(f_name, l_name)
print(f"\nHello, {my_name}!")

    
