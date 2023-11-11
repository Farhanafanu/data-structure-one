num1=[1,2]
num2=[3]
num3=num1+num2
print(num3)
length=len(num3)
if length%2==1:
    median=num3[length//2]
else:
    median=(num3[length//2-1]+num3[length//2])/2

print(median)
