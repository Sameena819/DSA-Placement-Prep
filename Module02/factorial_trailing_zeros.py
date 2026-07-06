n=int(input("enter the number"))
count=0
while n>0:
    n//=5
    count+=n
print(count)
