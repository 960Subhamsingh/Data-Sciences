#  Write a Python function to print all even number from a list

list1 = [12,3,4,5,6,7,8,9,10,12,13,14,15]

def even(num):
    for i in num:
        if(i%2==0):
            print(i, end=" ")
   

even(list1)
 
def even(num1):
    l = []
    for i in num1:
        if(i%2==0):
            l.append(i)
    print(l)

even([12,3,4,5,6,7,7,8])


def add(t):
    return [i for i in t if i%2==0]

add([12,3,4,5,6,7])

