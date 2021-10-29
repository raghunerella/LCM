n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
if n1>n2:
    large_number=n1
else:
    large_number=n2
while True:
    if(large_number%n1==0 and large_number%n2==0):
        LCM=large_number
        break
    large_number+=1
print(LCM)
