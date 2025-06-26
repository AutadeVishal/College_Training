from itertools import groupby
data = [1, 1, 2, 3, 3, 3, 2, 2, 4, 4, 5]
groups = [list(group) for key, group in groupby(data, key=lambda x: x)]
print(groups)

num=input("Type the Number")
