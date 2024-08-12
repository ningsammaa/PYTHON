list = ["Ningsamma", "Kritika", "Simran", "Aakriti"]
print(list)

#Append
list.append("Simrik")
print(list)

#Extend
fruits = ["apple", "banana", "cherry"]

list.extend(fruits)
print(list)

#insert
list.insert(0, "Sarika")
print(list)

#remove()
list.remove("Ningsamma")
print(list)

#pop
list.pop(3)
print(list)

#slice
print(list[2:4])


#reverese
list.reverse()
print(list)

#len()
print(len(list))

#min()
print(min(list))

#max
print(max(list))

list_copy = list.copy()
print(list_copy)

#index
index = list.index("Simran")
print(list)

#sort
print(sorted(list))

#clear
print(list.clear())