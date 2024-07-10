import  random


password = " "
for i in range(20):
    i = chr(random.randint(65,90))
    password = str(password) + i
print(password)

# Upper and lower case password

password_1 = " "
for i in range(12):
    i = chr(random.randint(65, 90))
    for j in range(12):
        j = chr(random.randint(65, 90)).lower()

    password_1 = str(password_1) + j +i
print(password_1)



# The upper and lowercase password can be simplified as follows:
password = ""
for i in range(5):
    i = chr(random.randint(65, 90))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)


# The upper and lowercase password can be simplified as follows:
password = ""
for i in range(5):
    i = str(random.randrange(65, 95))
    j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)
