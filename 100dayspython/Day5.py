# student_score = [150, 50, 90, 80, 199, 70, 78, 85, 200, 201, 99, 1, 65, 42, 38]
# max_score = 0
# for score in student_score:
#     if score > max_score:
#         max_score = score
# print(max_score)
#

#
# count = 0
# for number in range(1, 101):
#     count += number
# print(count)

# <----------------------------------- fizzbuzz----------------------------------------------------------->
for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)
