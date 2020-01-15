#! /bin/python3
#  Jan 20 (PJW)

a_list = ["one","two","three"]
print(a_list)

#  Appending another elements

a_list.append("four")

#  Extending it with another lists

a_more = ["five","six"]
a_list.extend(a_more)

#  Joining the list with one space between each pair of words

a_string = " ".join(a_list)
print(a_string)

#  Splitting a string into its component words

b_string = "a string with several words"
b_list = b_string.split()
print(b_list)

#  Counting elements in a list:

n = len(b_list)
print(n)

#  Creating a sorted copy of a list

b_sort = sorted(b_list)
print(b_sort)
