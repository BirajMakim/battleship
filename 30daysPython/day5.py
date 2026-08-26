from venv import create

#-------------file handling- --------------




# f = open(r"C:\Users\biraj\OneDrive\Desktop\python\30daysPython\notes.txt", "w")
# f.write("Hello, Biraj!\n")
# f.write("This is a file")
# f.close()
#
#
# f = open("notes.txt", "r")
# content = f.read()
# print(content)

#
# with open(r"C:\Users\biraj\OneDrive\Desktop\python\30daysPython\notes.txt", "w") as f:
#     f.write ("Hello Mate!, how's going on\n")
#     f.write(" This is line 2.\n")
#
# with open(r"C:\Users\biraj\OneDrive\Desktop\python\30daysPython\notes.txt", "r") as f:
#     content =f.read()
#     print(content)



# with open(r"C:\Users\biraj\OneDrive\Desktop\python\30daysPython\logs.txt", "w") as f:
#     f.write("Hello people, how are you doing?")
#     f.write("Do you guys wants chicken curry")
#     f.close()
#
#
#
#
# with open(r"C:\Users\biraj\OneDrive\Desktop\python\30daysPython\logs.txt", "r") as f:
#     for line in f:
#         print(line.strip())

#
# import datetime
# def write_log(message):
#     with open("system.log", "a") as f:
#         f.write(f"{message}\n")
#
# write_log("Server started")
# write_log("User looged in")
# write_log("ERROR: disk full")
#
# with open("system.log", "r") as f:
#     lines = f.readlines()
#
# errors = [line.strip() for line in lines if "ERROR" in line]
# print(errors)
#
# import datetime
#
# def write_log(message):
#     timestamp = datetime.datetime.now()   # gets current date & time
#     with open("system.log", "a") as f:
#         f.write(f"[{timestamp}] {message}\n")
#
# write_log("Server started")
# write_log("ERROR: disk full")
# # ADD THIS — read and print the file
# with open("system.log", "r") as f:
#     contents = f.read()
#     print(contents)


# with open("students.txt", "w") as f:
#     f.write("Biraj - 98\n")
#     f.write("Diya - 91\n")
#     f.write("Alice - 75\n")
#     f.write("Shakti - 60\n")
#
#
# with open("students.txt", "r") as f:
#     content =f.read()
# print(content)
#
#
#
# with open("students.txt", "a") as f:
#     f.write("Bob - 74")
#
# count = 0
# with open("students.txt", "r") as f:
#     for line in f.readlines():
#         count += 1
#     print(f"The total number of students are {count}")
#
#
#
# def analyse_log_file():
#     with open("server.log", "w") as f:
#         f.write("INFO: server started\n")
#         f.write("ERROR: disk full\n")
#         f.write("WARNING: high memory\n")
#         f.write("ERROR: connection lost\n")
#         f.write("INFO: backup complete\n")
#         f.write("ERROR: timeout\n")
#
#     error_count = 0
#     info_count = 0
#     warning_count = 0
#     with open("server.log", "r") as f:
#         for line in f.readlines():
#             if line.startswith("ERROR"):
#                    error_count += 1
#             elif line.startswith("WARNING"):
#                    warning_count += 1
#             elif line.startswith("INFO"):
#                    info_count += 1
#
#
#
#     print(f"Errors: {error_count}")
#     print(f"WARNING: {warning_count}")
#     print(f"INFO: {info_count}")
#
# analyse_log_file()
#



with open("scan_report.txt", "w") as f:
    f.write("Network Scan Report\n")
    f.write("Open ports: " + str([80, 443, 22]))

with open("scan_report.txt", "r") as f:
    print(f)







