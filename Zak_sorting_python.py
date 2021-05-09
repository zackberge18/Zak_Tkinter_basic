my_list=[5,4,3,6,7,12,3,45,6,7,1]

newlist=list()

for i in range(len(my_list)):
    newlist.append(min(my_list))
    my_list.remove(min(my_list))
print(newlist)