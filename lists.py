my_list = []

my_list.append (10)
my_list.append(15)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)
print(my_list)

my_extended_list = my_list + [50, 60, 70]

my_list.pop()

my_list.sort()

index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)