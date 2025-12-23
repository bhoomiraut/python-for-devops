
#set - collection of unique items of different data types 
#sets are unordered- items do not have a defined order
#duplicate items are not allowed

info ={} #empyt dictionary
print(type(info))  # <class 'dict'>

days = set() # empty set
print(type(days))  # <class 'set'>

info ={1} #set with one item
print(type(info))  # <class 'set'>

info = {2,3,4, 1, 5,5,4, "hi"} #set with multiple items
print(info)  #prints entire set {1, 2, 3, 4, 5} - duplicates removed


nums = [1,1,1,1,2,2,2,3,3,4,6.4,6.4,0,-1,-4]
print(nums)
nums = set(nums)  #converting list to set
print(nums)
print(type(nums))  # <class 'set'>

nums2= [1,1,1,1,2,2,5,5,3,3,2,6.2, 10.5, 0, -3, -4, -1]
print(nums2)
nums2 = list(set(nums2))  #converting list to set and back to list
print(nums2)    
print(type(nums2))  # <class 'list'>

#difference in list and set - list is ordered and allows duplicates & set is unordered and does not allow duplicates
#ex: list - ip addresses in a server log file , playlist, to-do list
#ex: set - unique ip addresses from the log file, unique users in a system, user IDs, email addresses