""" 3. Write a python program that can tell you if your grade score good or not . Good Score
range is 40 to 60.i. Ask user to enter his score. ii. If it is below 40 to 60 range then print that score is low iii. If
it is above 60 then print that it is good otherwise print that it is normal """

score = int(input("Enter your score : "))
if(score<40):
    print("Not a good Score")
elif(score>60):
    print("Good Score")
else:
    print("Normal")