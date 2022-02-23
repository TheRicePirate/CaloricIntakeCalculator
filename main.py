def measurements():
    print("")
    print("========================")
    print("Enter 1 to input metric system units.")
    print("Enter 2 to input imperial system units.")
    print("========================")
    print("")


def gender():
    print("")
    print("========================")
    print("Enter 1 if you are male.")
    print("Enter 2 if you are female.")
    print("========================")
    print("")


def activity_levels():
    print("")
    print("========================")
    print("Enter 1 if you are sedentary.")
    print("Enter 2 if you are lightly active.")
    print("Enter 3 if you are moderately active.")
    print("Enter 4 if you are very active.")
    print("Enter 5 if you are extra active.")
    print("========================")
    print("")


print("This calculator's default measurement system is set to metric.")
print("Enter any number other than 1 to input metric system values.")
print("============================================================")
user_measurement_system = int(input("Enter 1 to switch to the imperial system: "))

BMR_raw = 0
daily_calories = 0


if user_measurement_system == 1:
    height = float(input("Input your height in feet and inches as a decimal: "))
    weight = float(input("Input your weight in lbs: "))
    age = int(input("Input your age as a whole number: "))
    print(gender())
    user_gender = int(input("Input your gender in accordance to the list: "))
    height_converted = height*30.48
    weight_converted = weight/2.205
    if user_gender == 1:
        BMR_raw = (10*weight_converted) + (6.25*height_converted) - (5*age) + 5
    elif user_gender == 2:
        BMR_raw = (10*weight_converted) + (6.25*height_converted) - (5*age) - 161
    else:
        print("Gender selection invalid, please enter your gender's corresponding numerical value in the list.")

else:
    height = float(input("Input your height in centimetres: "))
    weight = float(input("Input your weight in kg: "))
    age = int(input("Input your age as a whole number: "))
    print(gender())
    user_gender = int(input("Input your gender in accordance to the list: "))
    if user_gender == 1:
        BMR_raw = (10*weight) + (6.25*height) - (5*age) + 5
    elif user_gender == 2:
        BMR_raw = (10*weight) + (6.25*height) - (5*age) - 161
    else:
        print("Gender invalid, please enter your corresponding gender's numerical value in the list.")

print(activity_levels())

user_activity_level = int(input("Enter your corresponding activity level: "))

if user_activity_level == 1:
    daily_calories = BMR_raw*1.2
if user_activity_level == 2:
    daily_calories = BMR_raw*1.375
if user_activity_level == 3:
    daily_calories = BMR_raw*1.55
if user_activity_level == 4:
    daily_calories = BMR_raw*1.725
if user_activity_level == 5:
    daily_calories = BMR_raw*1.9
if user_activity_level < 1 or user_activity_level > 5:
    print("Please enter a valid activity level.")

print("")
print("In order to maintain your current weight, you must consume " + str(daily_calories) + " calories daily.")
print("")
calories_per_meal = daily_calories/3
print("Optimally, you should consume " + str(calories_per_meal) + " for each of the three daily meals.")
print("")
print("Your BMR value " + str(BMR_raw))
print("")
calories_consumed = int(input("Input the quantity of calories you have consumed so far: "))
print("")
calories_remaining = daily_calories - calories_consumed
print("You must consume " + str(calories_remaining) + " more calories today to retain your current weight.")
