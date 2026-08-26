# with open("practice.txt", "w") as f:
#     f.write("Hi everyone \n we are learning File I/O \n using java \n i like programming in java")
   
# with open("practice.txt", "r") as f:
    
#     # print(f.read())
#     data = f.read()
# new_data = data.replace("python", "java")
# print(new_data)
    
  
# with open("practice.txt", "w") as f:
#     f.write(new_data) 



# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find(word)) != -1:
#         print("Found")
#     else:
#         print("Not found")




# -------------------OOP-----------------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database. .")
# s1 = Student("Biraj", 89)
# s2 = Student("Diya", 90)
# print(s1.name, s1.marks)
# print(s2.name, s2.marks)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     @staticmethod    
#     def hello():
#         print("Hello")


#     def get_average(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi",  self.name, "your avg mark is: ", sum/3)
        
# s1 = Student("Biraj Magar", [99, 87, 89])
# s1.get_average()
        
# s1.hello()   

 
 
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
        
        
#     def debit_acc(self, amount):
#         self.balance -= amount
#         print("Rs. ", amount, "Was debited")
#         print("Your totoal balance is Rs ", self.balance)
        
#     def credit(self, amount):
#         self.balance += amount
#         print("RS", amount, "was credited")
#         print("Your totoal balance is Rs ", self.balance)
        
        
#     def get_balance(self):
#         return self.balance
# a1 = Account(20000, 102100175)
# a1.debit_acc(1000)
# a1.credit(60000)






# class Car:
#     def __init__(self, type):
#         self.type = type
    
    
#     @staticmethod
#     def start():
#         print("Car is Started..")
        
        
#     @staticmethod,
#     def stop():
#         print("Car has stoped..")
# class Toyota(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()


# car1 = Toyota("Camry", "Hybrid")
# print(car1.type)
        
        
        
