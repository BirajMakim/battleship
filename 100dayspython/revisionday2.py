# i = 5
# while i < 6:
#     print(i)
#     i -= 1


# i = 1 
# while i <= 100:
#     print(i)
#     i += 1


# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


# n = 3
# while n <= 30:
#     print(n)
#     n += 3


# i = 1
# while i <= 10:
#     print(3 * i)
#     i += 1

# nums = [1, 4, 9., 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1
    


# nums = (1, 4, 9., 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0
# while i < len(nums):
    
#     if nums[i] == x:
#         print("Yes the num 36 is in the tuple")
    
#     i += 1        
    

# i = 0
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue
       
#     print (i) 
#     i += 1


# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for n in nums:
#     print(n)
    
    
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]
# x = 49
# index = 0
# for n in nums:
#     if n == x:
#       print("Num 49 is found at ", index)  
#     index += 1
    



# for r in range(1, 100):
#     print(r)

# r = 100
# for r in range(100, 0, -1):
#     print(r)


# n = 3
# for m in range(1, 10):
#     print(n*m)


# n = int(input("Enter the num: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Total sum is ", sum)


# n = int(input("Enter the num: "))
# sum = 0
# i = 1
# for i in range (1, n+1):
#     sum += i
# print("Total sum is : ", sum)


# n = int(input("Enter the num: "))
# fact = 1
# for i in range (1, n+1):
#     fact *= i
# print("Total factorial: " ,fact)
    
    
    
# n = int(input("Enter the num: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
    
# print("Total factorial: " ,fact)
    
    
    
    
# <-------------------function ------------------>
# def my_function(fname):
#     print (fname + " k ")
# my_function("biraj")





# def my_function(greeting, *names):
#       for name in names:
#           print(greeting, name)

# my_function("YOM", "Emil", "Tobias", "Linus")

# list = [ 'apple', 'banana', 'cherry']
# hero = [ 'superman', 'batman', 'spiderman']

# def my_list(list):
#     print(len(list))
# my_list(list)
# my_list(hero)


# List = [ 'apple', 'banana', 'cherry']
# hero = [ 'superman', 'batman', 'spiderman']

# def my_list(list):
#     for ting in list:
#         print(ting, end= " ")

# my_list(List)
# my_list(hero)

# def factorial_cal(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact *= i
#     print(fact)
    
# factorial_cal(5)


# def money_exchange(amount):
#     indian_money = " "
#     inr = 90.16
#     dollor_inr = (amount * inr)
    
#     print(dollor_inr)
# money_exchange(4)


# def odd_even(num):
#     if num % 2 == 0:
#         print("Even num")
#     else:
#         print("Odd")
# odd_even(3)
    
    
# def factorial(n):
#     if n== 0 or n==1:
#         return 1
#     return factorial(n-1)*n
# print(factorial(5))



# def sum_natural(n):
#     if n == 0:
#         return 0
#     return sum_natural(n-1) + n
# print(sum_natural(2))


# fruits = [ "apple", "orange", "mango",]
# def print_list(my_lsit):
    
    
    
  
  
# -----concept--------------
# sum_list([1,2,3,4,5])
#  = 1 + sum_list([2,3,4,5])
#  = 1 + (2 + sum_list([3,4,5]))
#  = 1 + (2 + (3 + sum_list([4,5])))
#  = 1 + (2 + (3 + (4 + sum_list([5]))))
#  = 1 + (2 + (3 + (4 + (5 + sum_list([])))))
   
# def sum_list(number):
#     if len(number) == 0:
#         return 0
#     else:
#         return number[0] + sum_list(number[1:])
    
# mylist = [1, 2, 3, 4, 5]
# print(sum_list(mylist))
