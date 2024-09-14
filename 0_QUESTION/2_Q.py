""" 2. Write a program that asks user to enter two cities and it tells you if they both are in same
city or not. For example if I enter yellow and Black, it will print "Both are colors" but if I enter
yellow and Tiger it should print "They don't belong to same category """

cities = ["Patna" ,"GAYA","Jhanabad","Nadwan","punpun"]

x = input("Enter the city Name ")
y = input(" Enter the Another  city  name ")

if x in cities and y in cities:
    category = "Both are cities"
else:
    category = "both are not same city "

print(f"category : {category}")
