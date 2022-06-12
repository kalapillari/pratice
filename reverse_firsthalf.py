#reverse first half of the list
list1=[1,2,3,4,5,6,7,8,9,10]
list2=int(len(list1)/2)
print(list1[:list2-1:-1])


print("secong method")
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[4::-1]#43210
list3=list1[5:10:1]
print(list1)
print(list2)
print(list3)
list4=list2+list3
print(list4)

