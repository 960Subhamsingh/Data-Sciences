# Calculate the sum of all numbers in a list

a = [12,23,45,44,56,6]

def total(num):
    s = 0
    for i in a:
        s=s+i
    print(s)

total(a)


# def t1(l):
#     h=0
#     [h:=h+1 for i in l]
#     return h
# t1([12,3,4,5,6,7])