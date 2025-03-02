#Checking for a Sublist in a List:

my_list1 = [3, 4, 5, 2, 7, 8]
sub_list1 = [2, 7]
is_found = False

for i in range(len(my_list1) - len(sub_list1) + 1):
    if my_list1[i : i + len(sub_list1)] == sub_list1:
        is_found = True
        break

print(is_found)