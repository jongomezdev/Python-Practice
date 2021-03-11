# a = input("a: ")
# b = input("b: ")

# If you have 2 cups.. one with coffee and one with milk how would you switch the contents?
# You would have to get a third cup!!!!
# c = a
# a = b
# b = c

# print("a: " + a)
# print("b: " + b)

# print(len(input('What is your name?')))

# name = input('What is your name?')

# length = len(name)

# print(length)

# time_until_midnight = "5"
# print("There are " + time_until_midnight + " hours until midnight")

# print('Welcome to the Band Name Generator!')

# city = input("What city did you grow up in?\n")

# petName = input("What is the name of your pet?\n")

# print("Your band name could be " + city + ' ' + petName)

############################################
# #Data Types
############################################

# #checks the data type
# type() 

# num_char = len(input('What is your name?'))

# # Type conversion #
# typeString = str(num_char)

# print('Your name has ' + typeString + ' characters.')


# #prints 170.5
# print(70 + float('100.5')) 
# #prints 70100
# print(str(70)+ str(100))




###########################################

# two_digit_number = input("Type a two digit number: ")


# # print(type(two_digit_number))

# firstNum = two_digit_number[0]
# secondNum = two_digit_number[1]

# ## Type Conversion ##
# result = int(firstNum) + int(secondNum)

# print(2 ** 2 )
###########################################

# 2 to the power of 2 is writtin with two asterics 


############################################ 
#BMI CALCULATOR 
############################################

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")


# bmi = int(weight) / float(height) ** 2
# bmiWhole = int(bmi) ## turns result into a whole number
# print(bmi)

############################################
# ROUNDING 
############################################

# print(round(8 / 3))
# ## Rounding to two decimal places ##
# print(round(8 / 3, 2))
# ########### Floor Division ############
# print(round(8 // 3)) #prints 2

# ##### f-string #####
# score = 500

# print(f"your score is {score}")


############################################
# TIME LEFT CALC 
############################################

# age = input("What is your current age?")

# ageNum = int(age)

# years_left = 90 - ageNum

# days_left = years_left * 365

# weeks_left = years_left * 52

# months_left = years_left * 12

# message = f"You have {days_left} days, {weeks_left} weeks and {months_left} months.. Make the most of it!"
# print(message)


############################################
# TIP CALCULATOR 
############################################

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill?"))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# # fine_amount = "{:.2f}".format(bill_per_person) get two decimal places after final calc

# print(f"Each person should pay: ${final_amount}")


############################################
# If Else Statement  ROLLERCOASTER 
############################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#   print('You can ride the rollercoaster!')
# else:
#   print('Sorry, grow a little!')

############################################
  # Nested If Else Statement 
############################################

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print('You can ride the rollercoaster!')
#   age = int(input('What is your age?'))
#   if age < 12:
#     bill = 5
#     print('Child tickets are $5')
#   elif age <= 18:
#     bill = 7
#     print('Youth tickets are $7')
#   elif age >= 45 and age <= 55: ## logical operator
#     print('Have a free ride on us')
#   else:
#     bill = 12
#     print('Adult tickets are $12')
#   photo = input('Would you like a photo? Y or N ')

#   if photo == "Y":
#     bill += 3
    
#     print(f'Your final bill is ${bill}')
# else:
#   print('Sorry, you have to be taller to get on this ride.')

############################################
  # Elif statement with BMI Calc 
############################################

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = round(weight / height ** 2)

# if bmi < 18.5:
#   print(f'Youre bmi is {bmi}, you are under weight')
# elif bmi < 25:
#   print(f'Youre bmi is {bmi}, you have a normal weight')
# elif bmi < 30:
#   print(f'Youre bmi is {bmi}, you are slightly overweight')
# elif bmi < 35:
#   print(f'Youre bmi is {bmi}, you are obeseish')
# else:
#   print(f'Youre bmi is {bmi}, you are clinically obese')


############################################
# Leap Year Calc 
############################################

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print('Leap Year')
#     else:
#       print('Not a leap year')
#   else:
#     print('Leap year!')
# else:
#   print('Not a leap year')


############################################
# Leap Year WITH OUTPUT FUNCTION 
############################################

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year) and month == 2:
#     return 29
#   return month_days[month - 1]
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

############################################
  # PYTHON PIZZA 
############################################

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
  
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#   bill += 1

# print(f"Your total is ${bill}")

############################################
# LOVE CALC 
############################################

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1 + name2

# lower_case = combined_string.lower()

# t = lower_case.count('t')
# r = lower_case.count('r')
# u = lower_case.count('u')
# e = lower_case.count('e')

# true = t + r + u + e

# l = lower_case.count('l')
# o = lower_case.count('o')
# v = lower_case.count('v')
# e = lower_case.count('e')

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):
#   print(f"Your love score is {love_score}, you mix like oil and water")
# elif (love_score >= 40) or (love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together")
# else:
#   print(f"Your score is{love_score}")

############################################
# Random numbers 
############################################

# import random ## imports the module random
# rand_int = random.randint(1, 1000) # specify a start and an end. random num is in between
# print(rand_int)

# rand_float = random.random()
# print(rand_float)

# rand = random.random() * 5
# print(rand)

# #
# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")
# #
# rand_num = random.randint(0, 1)


# if rand_num == 1:
#   print("Heads")
# else:
#   print("Tales")

############################################
# PYTHON LISTS 
############################################

# fruits = ["Cherry", "Apple", "Banana"]

# fruits.append("Grapes") # adds to the end of the list

# print(fruits[2]) # Prints Banana

# x = fruits.index("Cherry")
# print(x)


############################################
# Generating random choice from a list 
############################################

# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# num_of_names = len(names)

# rand_choice = random.randint(0, num_of_names -1)

# person = names[rand_choice]

# print(f"{person} is going to buy the meal today!")

############################################
# NESTED LIST 
############################################

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1]) # will print kale

# ####


# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1][horizontal - 1] = "X"

# print(f"{row1}\n{row2}\n{row3}")


############################################
# FOR LOOPS 
############################################

# fruits = ["Apple", "Peach", "Pear", "Cherry", "Strawberry"]

# for fruit in fruits: 
#   print(fruit + " pie")

############################################
# STUDENT HEIGHTS 
############################################

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = 0

# for height in student_heights:
#   total_height += height
# print(total_height)

# number_of_students = 0

# for student in student_heights:
#   number_of_students += 1
# print(number_of_students)

# average_height = round(total_height / number_of_students)
# print(average_height)

############################################
# STUDENT SCORES 
############################################

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# high_score = 0

# for score in student_scores:
#   if score > high_score:
#     high_score = score
# print(f"The highest score in the class is: {high_score}")

# # Find Lowest score using a for loop
# minimum = student_scores[0]
# for score in student_scores:
#     if minimum > score:
#        minimum = score
# print(minimum)

############################################
# RANGE METHOD 
############################################

# for number in range(1, 11):
#   print(number)
# #############
# total = 0

# for number in range(1, 101):
#    total += number
# print(total)

# total = 0

## add each even number in the range and count by set 2
# for number in range(2, 101, 2):
#   total += number
# print(total)

# flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

# for i in range(len(flavor_list)):
#   flavor = flavor_list[i]
#   print(f'{i + 1}: {flavor}')

############################################
# Enumerate 
############################################

# for i, flavor in enumerate(flavor_list, 1):
#   print(f'{i}: {flavor}')


############################################
# FIZZ BUZZ IN PYTHON!! 
############################################


# for number in range(1, 101):
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)


############################################
# DEFINING FUNCTIONS 
############################################

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

    
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#   jump()
#   number_of_hurdles -= 1

############################################
# WHILE LOOP 
############################################

# while not at_finishline():
#   run()

# while not at_goal():
#   if wall_in_front():
#       jump()
#   else:
#       move()

############################################
# Functions with inputs 
############################################

# def greet(name): ## parameter
#   print(f"Hello {name}")
#   print(f"Ciao {name}")
#   print(f"Hola {name}")
# greet("Jonathan") ## argument

############################################
# Keyword Arguments 
############################################

# def greet_with(name, location):
#   print(f"Hello {name}, what's it like in {location}?")
# greet_with(location="New York", name="Jonathan")

############################################
# PYTHON DICTIONARIES 
############################################

# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Cry": "Tears",
#   }

# print(programming_dictionary["Function"])

# programming_dictionary["Loop"] = "The action of doing something over and over again."

## Will wipe out the existing data in the dictionary
# programming_dictionary = {} 
# print(programming_dictionary)

 ### Declare a dictionary as empty and at a later state you can add to it!
# empty_dictionary = {}

# Change an existing item in the dictionary
# programming_dictionary["Bug"] = "A moth in your computer"

# Loop through dictionary and print key/value

# for key in programming_dictionary:
  # print(key)
  # print(programming_dictionary[key])

############################################
# Manipulating Dictionaries 
############################################

#   student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }


#todo-1: Create an empty dictionary called student_grades.
# student_grades = {}

# for student in student_scores: 
#   score = student_scores[student]
#   print(score)
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"

# print(student_grades)


############################################
# NESTING A DICTIONARY IN A DICTIONARY 
############################################

# travel_log = {
#   "France": {
#   "cities_visited":
#   ["Paris", "lille", "dijon"],
#   "total_visits": 12
#   },
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":5}
# }

############################################
# NESTING A DICTIONARY IN A LIST 
############################################

# travel_log = [
#   {
#     "country": "France", 
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#   },
#   {
#     "country": "Germany", 
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 5
#   },
# ]

############################################
# DICTIONARY IN LIST ACT. 92. 
############################################

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country_visited, times_visited, cities_visited):
#   new_country = {}
#   new_country["country"] = country_visited
#   new_country["visits"] = times_visited
#   new_country["cities"] = cities_visited
#   travel_log.append(new_country)


# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

############################################
# BLIND AUCTION 
############################################

# bids = {}
# bidding_finished = False

# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   # bidding_record = {"Angela": 123, "James": 321}
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

# while not bidding_finished:
#   name = input("What is your name?: ")
#   price = int(input("What is your bid?: $"))
#   bids[name] = price
#   should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
#   if should_continue == "no":
#     bidding_finished = True
#     find_highest_bidder(bids)
#   elif should_continue == "yes":
#     clear()
  
############################################
# FUNCTIONS WITH OUTPUTS 
############################################

# def format_name(f_name, l_name):
#   """Take a first and last name and format it to return the title case version of the name."""
#   if f_name == "" or l_name == "":
#     return "Please enter a valid name"

#   upper_f = f_name.title()
#   upper_l = l_name.title()
#   return f"{upper_f} {upper_l}"

# print(format_name(input("What is your first name? "), input("What is your last name? ")))


############################################
# Scoping 
############################################

i = 50
def foo():
  i = 100
  return i

foo()
print(i)
