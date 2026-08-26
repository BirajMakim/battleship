

# --- ------------CSV comma separated values----------

# import csv
# with open("students.csv", "w", newline= "") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "age", "score"])
#     writer.writerow(["Biraj", 25, 98])
#     writer.writerow(["diya", 21, 91])
#     writer.writerow(["Alice", 22, 75])
#
# with open("students.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# with open("students.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["name"], row["score"])


# ---------------Pandas----------------
# import pandas as pd
# mydataset = {
#     'cars': ["BMW", "Volvo", "Ford"],
#     'passings': [3,7,2]
#
# }
# myvar = pd.DataFrame(mydataset)
# print(myvar)
#
# print(pd.__version__)
#
# import pandas as pd
# a = [1,7,2]
# myvar = pd.Series(a)
# print(myvar)
# print([0])
#
# import pandas as pd
# a = [1,7,9,10]
# myvar = pd.Series(a, index = ["x", "y", "z", "a"])
# print(myvar)
#
# print(myvar["y"])

# import pandas as pd
# calories = {"day1": 420, "day2": 380, "day3": 390}
# myvar = pd.Series(calories)
# print(myvar)
#
# import pandas as pd
# calories = {"day1": 420, "day2":380, "day3":390}
# myvar =  pd.Series(calories, index=["day1", "day2"])
# print(myvar)


# -----------DataFrames-----------



# import pandas as pd
# data = {
#     "calories": [420,380,390],
#     "duration": [50,40,45]
#
# }
# myvar = pd.DataFrame(data)
# print(myvar)
#


# import pandas as pd
# data = {
#     "calories": [420,380,390],
#     "duration": [50,40,45]
#
# }
# df = pd.DataFrame(data)
# print(df)
#
# print(df.loc[0])
# print(df.loc[[0,1]])


# import pandas as pd
# data= {
#     "calories": [420,380,390],
#     "duration":[50,40,45]
# }
# df = pd.DataFrame(data,index = ["day1", "day2", "day3"])
# print(df)
# print(df.loc["day2"])


# import pandas as pd
# df = pd.read_csv("data.csv")
# print(df)
#
# import pandas as pd
# df = pd.read_csv('data.csv')
# print(df.to_string())
# # print(df)
#
# print(pd.options.display.max_rows)


# import pandas as pd
# pd.options.display.max_rows = 9999
# df = pd.read_csv("data.csv")
# print(df)
#
# import csv
# with open("product.csv", "w", newline= "") as f:
#     write_data = csv.writer(f)
#     write_data.writerow(["name", "price", "stock"])
#     write_data.writerow(["Laptop", 1500, 10])
#     write_data.writerow(["Phone", 800, 40])
#     write_data.writerow(["Mobile charger", 100, 66])
#     write_data.writerow(["Case cover", 150, 10])
#
# with open("product.csv", "r")as f:
#     read = csv.DictReader(f)
#     for row in read:
#         print(row["name"], row["price"], row["stock"])
#
#
#
# import pandas as pd
# data = {
#     "city": ["Melbourne", "Sydney", "Brisbane", "Perth"],
#     "population": [5000000, 5300000, 2600000, 2100000],
#     "avg_temp": [15.8, 17.7, 20.5, 19.0]
# }
# df = pd.DataFrame(data)
# print(df.to_string())
# print(df[df["population"]] > 3000000)
# print(df["avg_temp"])
#
#
# import csv
# with open("sales.csv", "r")as f:
#
#
# import pandas as pd
#
# data = {
#     "name": ["Alice", "Bob", "Clara"],
#     "score": [88, 74, 92]
# }
#
# df = pd.DataFrame(data)
# print(df)                        # bug 1
# print(df[df["score"] > 80])              # bug 2
# df.to_csv("results.csv", index=True)     # bug 3 — subtle!

# import csv
# import pandas as pd
# with open("sales1.csv", "w", newline="") as f:
#     sales_write = csv.writer(f)
#     sales_write.writerow(["month", "sales", "expenses"])
#     sales_write.writerow(["January", 15000, 8000])
#     sales_write.writerow(["February", 18000, 9500])
#     sales_write.writerow((["March", 22000, 10000]))
#     sales_write.writerow(["April", 19000, 8500])
#     sales_write.writerow(["May", 25000, 11000])
#
# df = pd.read_csv("sales1.csv")
# print(df)
# df["profit"] = df["sales"] - df["expenses"]
# print(df)
# best_month = df.loc[df["profit"].idxmax(), "month"]
# print(f"Best month: {best_month}")
# print(df["sales"].mean())
# df = df.sort_values("profit", ascending = False)
# print(df)
#
# import pandas as pd
# data = {
#     "city": ["Melbourne", "Sydney", "Brisbane", "Perth"],
#     "population": [5000000, 5300000, 2600000, 2100000],
#     "avg_temp": [15.8, 17.7, 20.5, 19.0]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df["population"] > 30000 )