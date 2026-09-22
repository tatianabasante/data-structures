print ("Hello. Welcome to data structures class !!!")

number1 = 10
print(f"Var number1  is: {type(number1)}")
gravity = 9.8
print(f"Var gravity  is: {type(gravity)}")
numberx = 8j
print(f"Var numberx  is: {type(numberx)}")

#String Data Types

'''
This is a scope comment
'''

my_name = "Tatiana"
full_name = "Tatiana Yaqueline"
description = '''
    Hello, how's it going?
    This is amazing !!!
'''
print(f"Var my_name  is: {type(my_name)}")
print(f"Var full_name  is: {type(full_name)}")
print(f"Var description  is: {type(description)}")

week_days = []
print(f"Var week_days is: {type(week_days)}")

fruits = []
print(f"Var fruits is: {type(fruits)}")

months = ()
print(f"Var months is: {type(months)}")

#List Data Types
personal_info = ['Tatiana', 'Basante', 19, True, '3123669795', 'Pasto', ['Juli',9]]
print(personal_info)   

#Show father age
print(f"Father age is: {personal_info[2]}")    
print("Father city is: ", personal_info[5])

#Show daughter name and age
print(f"Daughter name is: {personal_info[6][0]} and age is: {personal_info[6][1]}")

#Update father age
#new_age = input("Please, type the new father age: ")
personal_info[2] = 60
print(f"Father age is: {personal_info[2]}")

#Add new information 
personal_info.append('Malala')
print(personal_info)

#Tuple
user_data = ('Benazir', 'Butto', 35, False)
print(user_data)
print(user_data[0])
new_age = 40
#user_data[2]= new_age

# Dictionaries
countries_info = {'country_name': 'Colombia', 'Capital': 'Bogota', 'Abbrev': 'CO', 'Code': 123456}
print(countries_info)
