# # try:
# #     print(x)
# # except:
# #     print("An exception occured")
#
# #
# # try:
# #     print(x)
# # except NameError:
# #     print("Variable x is not defined")
# #
# # except:
# #     print("Something else went wrong")
#
#
# # try:
# #     print("Hello")
# # except:
# #     print("something went wrong")
# # else:
# #     print("Nothing went wrong")
# #
#
# # try:
# #     print(x)
# # except:
# #     print("Something went wrong")
# # finally:
# #     print("The 'try except' is finished")
#
#
# # try:
# #     f = open("demofile.txt")
# #     try:
# #         f.write("Lorum Ipsum")
# #     except:
# #         print("Something went wrong when writing to the file")
# #
# #     finally:
# #         f.close()
# # except:
# #     print("something went wrong when opening the file")
#
#
# # x = -1
# # if x < 0:
# #     raise Exception("Sorry, no numbers below zero")
# #
# # x = "hello"
# #
# # if not type(x) is int:
# #     raise TypeError("Only integers are allowed")
# #
# # try:
# #     number =  int(input("Enter a Number: "))
# #     print(f"You entered {number}")
# # except ValueError:
# #     print("That's not a valid number")
#
#
# # try:
# #     number =  int(input("Enter a number: "))
# #     result = 100/number
# #     print(f"Result:{result}")
# # except ValueError:
# #     print("Please enter a valid number!")
# # except ZeroDivisionError:
# # #     print("Cannot divide by zero")
# #
# # def read_file(filename):
# #     try:
# #         with open(filename, "r") as f:
# #             return f.read()
# #     except FileNotFoundError:
# #         return f"Error: '{filename}' not found!"
# #     except PermissionError:
# #         return f"Error: No permission to read '{filename}'"
# #     finally:
# #         print(f"Attempted to read: {filename}")
#
#
# # def safe_divide(a, b):
# #     try:
# #         return a / b
# #     except ZeroDivisionError:
# #         print("Cannot divide by zero")
# #
# #     except TypeError:
# #         print("Please enter numbers only!")
# #
# # print(safe_divide(10, 2))    # 5.0
# # print(safe_divide(10, 0))    # Cannot divide by zero!
# # print(safe_divide(10, "a"))  # Please enter numbers only!
# #
# #
# # def safe_read(filename):
# #     try:
# #         with open(filename, "r") as f:
# #             return f.read()
# #     except FileNotFoundError:
# #         return "File not found"
# #     finally:
# #         print("Read attempt complete")
# #
# #
# # print(safe_read("server.log"))
# # print(safe_read("missing.txt"))
#
# # def validate_port(port):
# #     try:
# #         port_num = int(input("Enter the port num: "))
# #     if port_num <1 or port_num> 65535:
# #         raise ValueError("Please, Enter valid value")
# #
#
#
#
# def scan_port(port):
#     try:
#         port = int(port)
#         if port < 1 or port > 65535:
#             raise ValueError("Port out of range")
#         return f"Scanning port {port}"
#     except ValueError as e:
#         print(f"Error: {e}")
#     except TypeError:
#         print("Wrong type!")
#     finally:
#         print("Scan attempt done")
#
# print(scan_port("80"))
# print(scan_port("abc"))



# x = lambda a: a+ 10
# print(x(5))

# x = lambda a,b : a* b
# print(x(5,6))
#
# def myfunc(n):
#     return lambda a: a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

numbers = [ 1,2,,3,4,5]
doubled = list(map(lambda x: x *2, numbers))