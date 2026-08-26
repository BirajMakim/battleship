# fruits = ["apple", "banana", "mango"]
# print(fruits[0])
# print(fruits[-1])
# print(len(fruits))
#
#
from itertools import count


# files = ["log1.txt", "log2.txt", "log3.txt"]
# files.append("log4.txt")
# files.insert(0, "log0.txt")
# print(files)
# files.remove("log4.txt")
# files.pop()
# print(files)
# files.sort()
# print(files)
# files.reverse()
# print(files)
#
#
# print(files.count("log1.txt"))



# numbers = [1,2,3,4,5]
# # squared = []
# # for n in numbers:
# #     squared.append(n**2)
# # print(squared)
#
# # squared = [n**2 for n in numbers]
# # print(squared)
#
# even = [n for n in numbers if n % 2 ==0]
# print(even)

# devices = ["router", "switch", "firewall", "hub"]
# devices.append("access_point")
# print(devices)
#
# devices[0] = "modem"
# print(devices)
# devices.remove("hub")
# print(devices)
# devices.sort()
# print(len(devices))
#
# ip_addresses = ["192.168.1.1", "10.0.0.1", "172.16.0.1",
#                 "192.168.1.2", "8.8.8.8", "192.168.1.100"]
#
# new_ip = [p for p in ip_addresses if p.startswith("192.168")]
# print(new_ip)



# def analyse_logs(logs):
#     error_count = 0
#     info_count = 0
#     warning_count = 0
#
#     for message in logs:
#         if message.startswith("ERROR"):
#             error_count += 1
#
#         elif message.startswith("WARNING"):
#             warning_count += 1
#         elif message.startswith("INFO"):
#             info_count += 1
#
#
#
#     return {
#         "ERROR": error_count,
#         "WARNING": warning_count,
#         "INFO": info_count
#
#     }
#
# logs = [
#     "ERROR: disk full",
#     "INFO: server started",
#     "WARNING: high memory",
#     "ERROR: connection lost",
#     "INFO: backup complete",
#     "ERROR: timeout"
# ]
#
# result = analyse_logs(logs)
# print(f"Errors: {result['ERROR']}")
# print(f"Warnings: {result['WARNING']}")
# print(f"Info: {result['INFO']}")
#
# def scan_ports(ports):
#     dangerous_ports = [21, 22, 23, 3306]
#     flagged = [p for p in ports if p in dangerous_ports]
#     return flagged
#
# open_ports = [80, 22, 443, 3306, 8080]
# print(f"Flagged ports: {scan_ports(open_ports)}")