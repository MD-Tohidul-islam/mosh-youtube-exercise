l = [34,56,78,23,44,56,78,90,12]
print(max(l))
largest = l[0]
for i in l:
    if i > largest:
        largest = i
print(largest, ' is largest number')

