# Write a program in Python, A library charges a fine for every book returned late. For first 5 days 
# the fine is 50 paisa, or 6-10 days fine is one rupee and above 10 days is 5 rupees. If you return the 
# book after 30 days your membership will be cancelled. Write a program to accept the number of 
# days the member is late to return the book and display the fine or the appropriate message

days = int(input("Enter the number of days :"))

if(days<=5):
    amount = 0.50*days
    print(f'Fine amount of five days : {amount}')
elif(days>=6 & days<=10):
    amount = 1*days
    print(f'fine Amount to five to ten days {amount} ')
elif(days>=11):
    amount = 5*days
    print(f'fine Amount to greate then ten days {amount}')
    if(days>30):
        print(' member ship would be cancelled.')
