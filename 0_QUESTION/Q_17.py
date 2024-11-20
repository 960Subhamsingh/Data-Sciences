# Check if a given number is prime

def prime(n):
    if(n<2):
        print("Not Prime number")
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            print("Mot Prime")
    print("It is Prime")


prime(12)





# Find the mean (average) of a list

# Print the multiplication table of a user-given number
# Print a star triangle pattern based on user input