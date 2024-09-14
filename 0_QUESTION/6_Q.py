""" After appearing in exam 10 times you got this result,

result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]

Using for loop figure out how many times you got Pass """


result = ["Pass","Fail","Fail","Pass","Fail","Pass","Pass","Fail","Fail","Fail"]

count =0

for i in result:
    if(i== "Pass"):
        count+=1
print(count)


 
 