cars = ['audi', 'honda', 'suzuki', 'toyota']
if 'honda' in cars:
    print(f"{cars[1].title()} exist in the list")

#CGPA grading

cgpa = float(input("please enter your CGPA:"))
if cgpa >= 4.50:
    print(f"You have earned first class with CGPA of {cgpa}")
elif 3.5 <= cgpa < 4.50:
    print(f"You have earned second class upper with CGPA of {cgpa}")
elif 2.5 <= cgpa < 3.50:
    print(f"You have earned second class lower with CGPA of {cgpa}")
elif 2.0 <= cgpa < 2.5:
    print(f"You have earned third class with CGPA of {cgpa}")
elif 1.5 <= cgpa < 2.0:
    print(f"You have earned pass degree with CGPA of {cgpa}")
else:
    print(f"You have failed")

# person's stage in life

age = int(input("please enter your age:"))
if age < 2:
    print("You are a baby")
elif 2<= age < 4:
    print("You are a toddler")
elif 4 <= age < 13:
    print("You are a kid")
elif 13 <= age < 20:
    print("You are a teenager")
elif 20 <= age < 65:
    print("You are an adult")
else:
    print("You are elder")

# working with dictionaries

alient_0 = {'color': 'green', 'dress': 'hijab', 'football': 'pumer'}
print(alient_0['color'])

alient_0['points'] = 4.74
alient_0.update({'school': 'almanar', 'class': '4b'})

favorite_language = {'jane': 'python', 'musa': ' c++', 'daniel': 'c'}
favorite_language.update({'sageer': 'fotran', 'mustapha': 'java'})
del favorite_language['musa']

