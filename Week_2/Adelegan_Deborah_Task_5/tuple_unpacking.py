# TASK 4: Tuple Unpacking
FName = input("What is your first name please?: ")
age = int(input("How old are you?: "))
fav_color = input("What is your favourite color?: ")
home_town = input("Where is your home town?: ")
profile = FName, age, fav_color, home_town
tuple_profile = tuple(profile)
print(f"Name: \t\t\t{FName}\nAge: \t\t\t{age}\nFavourite Color:\t{fav_color}\nHome Town:\t\t{home_town}")
