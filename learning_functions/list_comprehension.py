# Problem 1: Reverse a List

list1 = [1, 2, 3, 4, 5]
print ([i for i in list1[::-1]])

# Problem 2: Concatenate two List

list4 = [1, 2, 3]
list5 = ['a', 'b', 'c']

result = []
for i in range(len(list4)):
    combined = str(list4[i]) + list5[i]  #
    result.append(combined)

print(result)

list8 = [1, 2, 3]
list9 = ['a', 'b', 'c']

concatenated_lst = [str(list8[i]) + list9[i] for i in range(len(list1))]
print(concatenated_lst)


list2 = [213, 123, 454, 789]
list3 = [123, 456, 789, 993]
print([i for i in (list2 + list3)])

# Problem 3: Check if a number is prime or not

numbers = [ i for i in range(1, 4000)]
print([ num for num in numbers if not any([num % i == 0 for i in range (2, num)])])


#: Square Each Item of a List
lst = [1, 2, 3, 4, 5]

squared_lst = [x ** 2 for x in lst]
print(squared_lst)


#: Iterate Two Lists Simultaneously
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped_lst = [(x, y) for x, y in zip(list1, list2)]  # zip func to create pairs for each item
print(zipped_lst)

#Remove Empty Strings from a List
lst1 = ["ram", "", "shyam", " ", "haru", ""]

cleaned_lst1 = [x for x in lst if x.strip("")]  # Keep only non-empty strings
print(cleaned_lst1)

# Add a New Item After a Specified Item
#Extend a Nested List (isintance)

#Replace List Item with a New Value
lst = [1, 2, 3, 4, 5]
old_value = 3
new_value = 10

replaced_lst = [new_value if x == old_value else x for x in lst]
print(replaced_lst)

### **Remove All Occurrences of a Specific Item**
lst = [1, 2, 3, 2, 4, 2, 5]
item_to_remove = 2

filtered_lst = [x for x in lst if x != item_to_remove]
print(filtered_lst)
