person = {"name": "Alex", "age": 18, "gender": "male"}
print (person ["age"])
cars = ("bmw", "Chrysler", "Lada")
cars2 = ["bmw", "Lada"]
cars2.append("honda")
hours = 25

if hours > 5 and hours <=12:
    print ("morning")
elif hours > 12 and hours <=17:
    print("day")
elif hours >= 18 and hours <= 23:
    print ("evening")
elif hours >23 and hours <=24 or hours <=5:
    print ("night")
else:
    print ("wrong time")
string = "melon, banana, apple"
def fruits(fruits_str):
    list_fruits = string.split(", ")
    return list_fruits[0], list_fruits[-1]
fruit1, fruit2 = fruits(string)
print(fruit2)