""" 1. We are having 3 list like this Colors = [“Yellow”,”Green”,”White”,”Black”] Fruits=
[“Apple”,”Papaya”,”Mango”,”Orange”] Animals=[“Tiger”,”Lion”,”Deer”,”Zebra”]
i. Write a program that asks user to enter a Color/Fruit/Animal name and it should tell which
category belongs to , like its is a fruit or color or Animal.  """

Colors = ["Yellow","Green","White","Black"]          
Fruits= ["Apple","Papaya","Mango","Orange"] 
Animals=["Tiger","Lion","Deer","Zebra"]
name = input("Enter the name : ")

if(name in Colors):
    category = "Colors"
elif(name in Fruits):
    category = "Fruits"
elif(name in Animals):
    category = "Animals"
else:
    category = "Invalid"
print(f"Category  {category} " )