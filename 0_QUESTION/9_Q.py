""" 
Write a  program asks for City name and Temperature and builds a dictionary using that Later on 
you can input City name and it will tell you the temperature of that City.
"""

dict = {}
n = int(input("Enter the number "))
for i in range(n):
    n1, n2 = input("Enter the city name temperature: ").split(",")
    dict[n1]= n2
print("The temperature of the city {} is {}".format(n1,n2))
