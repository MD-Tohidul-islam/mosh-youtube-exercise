l=[1,2,33,45,56,6,78,2,3,33,6,4,5,4,5]
new_list =[]
for i in l:
    if i  not in new_list:
        new_list.append(i)
print(sorted(new_list))
#or we can use set methode
l1=l.copy()
print(sorted(set(l1)))