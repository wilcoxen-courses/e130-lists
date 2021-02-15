#! /bin/python3
#  Jan 20 (PJW)

a_list = ["zero","one","two","three"]
print("\nOriginal a_list:")
print(a_list)

#  Selecting element 0 from a list

print("\nFirst element:")
print(a_list[0])

#  Appending another elements

a_list.append("four")

#  Extending it with another list

a_more = ["five","six"]
a_list.extend(a_more)

print("\nExtended a_list:")
print(a_list)

#  Selecting the second and third elements. This is confusing
#  at first because 1:3 includes element 1 but DOES NOT includes
#  element 3.

print("\nSecond and third elements:")
print(a_list[1:3])

#  Selecting elements from the beginning to the third. Note that 
#  this has the same gotcha as above: element 4 is NOT included

print("\nElements from the start through element 3:")
print(a_list[:4])

#  Selecting all elements from the second to the end of the list

print("\nElements from second to the end:")
print(a_list[1:])

#  Selecting elements backward from the end can be done with
#  a negative number followed by a colon. The negative number
#  indicates how far back from the end to start.

print("\nLast 3 elements:")
print(a_list[-3:])

#  Joining the list with one space between each pair of words

a_string = " ".join(a_list)
print("\nElements joined with spaces:")
print(a_string)

#  Splitting a string into its component words

b_string = "a string with several words"
b_list = b_string.split()
print("\nSplitting a string:")
print(b_list)

#  Counting elements in a list:

n = len(b_list)
print("\nNumber of elements in b_list is:")
print(n)

#  Creating a sorted copy of a list

c_sort = sorted(b_list)
print("\nSorted copy of b_list")
print(c_sort)
