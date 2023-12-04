# # 1. Write a program that finds the maximum value of the given list, assuming that the list
# # contains at least one element.
# # Try your program with the following array
# # 2 4 7 4 23 5 1 4 8 9
#
# lst = [2, 4, 7, 4, 23, 5, 1, 4, 8, 9]
# lst.sort()
# print(lst[-1])


# # 2. Write a program that calculates the average value of the given list.
# # Try your program with the following list
# # 4 7 1 5 11 53 12 46 84 23
# lst = [4, 7, 1, 5, 11, 53, 12, 46, 84, 23]
# sum = 0
# for nm in lst:
#     sum+=nm
# print(sum/len(lst))

# # 3. Write a program that prints the given list of integers in reverse order.
# # Try your program with the following list
# # 2 6 7 45 23 53 14 45 89 5
#
# lst = [2, 6, 7, 45, 23, 53, 14, 45, 89, 5]
# lst.reverse()
# print(lst)

# # 4. Write a program that accepts two lists of integers and prints true if each element in the first
# # list is less than the element at the same index in the second list. Your program should print
# # false if the lists are not the same length.
# def cal(l1, l2):
#     if len(l1) != len(l2):
#         print("false")
#         return
#     for i in range(0, len(l1)):
#         if l1[i] >= l2[i]:
#             print("false")
#             return
#     print("true")
# l1 = [1, 2, 3]
# l2 = [2, 3, 4]
# cal(l1, l2)

# # 5. Write a program that accepts a list of integers and two indexes and swaps the elements at
# # those indexes
# def cal(arr, i1,i2):
#     arr[i1], arr[i2] = arr[i2], arr[i1]
#     return arr
# lst = [1,2,4,3,5]
# print(cal(lst, 2,3))


# # 6. Write a program that accepts two lists of integers and prints a new list containing all
# # elements of the first list followed by all elements of the second.
# l1 = [1,2,3]
# l2 = [4,5,6]
# l3 = l1+l2
# print(l3)



# # 7. Write a program that accepts a list of integers and an integer value as its parameters and
# # prints the last index at which the value occurs in the list. The program should print –1 if the
# # value is not found. For example, in the list [74, 85, 102, 99, 101, 85, 56], the last index of the
# # value 85 is 5.
# lst = [74, 85, 56, 99, 101, 85, 56]
# indx = -1
# for i in range(0, len(lst)):
#     if lst[i] == 56:
#         indx = i
# print(indx)



# # 8. Write a program that prints the range of values in a list of integers. The range is defined as 1
# # more than the difference between the maximum and minimum values in the list. For
# # example, if a list contains the values [36, 12, 25, 19, 46, 31, 22], the program should return
# # 35. You may assume that the list has at least one element.
# lst = [36, 12, 25, 19, 46, 31, 22]
# lst.sort()
# v = lst[len(lst)-1] - lst[0] +1
# print(v)


# # 9. Write a program that accepts a list of integers, a minimum value, and a maximum value and
# # prints the count of how many elements from the list fall between the minimum and
# # maximum (inclusive). For example, in the list [14, 1, 22, 17, 36, 7, -43, 5], for minimum value
# # 4 and maximum value 17, there are four elements whose values fall between 4 and 17.
# def calc(arr, min, max):
#     count = 0
#     for nmb in arr:
#         if nmb <= max and nmb >= min:
#             count += 1
#     print(count)
# lst = [14, 1, 22, 17, 36, 7, -43, 5]
# calc(lst, 4, 17)


# # 10. Write a program that accepts a list of real numbers and prints true if the list is in sorted
# # (nondecreasing) order and false otherwise. For example, if lists named list1 and list2 store
# # [16.1, 12.3, 22.2, 14.4] and [1.5, 4.3, 7.0, 19.5, 25.1, 46.2] respectively, the program should
# # print false for list1 and true for list2 respectively. Assume the list has at least one element. A
# # one-element list is sorted.
# def calc(lst):
#     for i in range(0, len(lst)-1):
#         print(i)
#         if lst[i] > lst[i+1]:
#             print("false")
#             return
#     print("true")
# lst = [16.1, 12.3, 22.2, 14.4]
# calc(lst)
# lst = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]
# calc(lst)

