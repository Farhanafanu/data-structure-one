
def linearsearch(list):
    element=int(input("enter element to found"))
    
    for i in range(len(list)):
        flag=0
        if i==element:
            flag=1
            break
    if flag==1:
     print("element found")
    else:
        print("element not found")
list=[1,2,3,4,5,6,7,8,9,10]
s=linearsearch(list)
