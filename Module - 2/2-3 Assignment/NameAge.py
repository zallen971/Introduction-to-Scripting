from datetime import date

#get name
name = input("What is your name? ")

#get age
age = int(input("What is your age? "))

#calculate birth year
current_year = date.today().year
birth_year = current_year - age

#greetings plus birth year
print(f'Hello {name}! You were born in {birth_year}.')