import pandas as pd

file_path = 'day_2.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

data = [list(map(int, line.split())) for line in lines]

example = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

# Create the DataFrame
df = pd.DataFrame(data)

print(df.head())

really_safe = []
safe = []

def check_safe(list):
    safe = []
    problem = []
    increasing = []
    decreasing = []
    for index, number in enumerate(list):
        if index < len(list) - 1:
            next = list[index + 1]
            if next - number in [1, 2, 3]:
                increasing.append(1)
            if number - next in [1, 2, 3]:
                decreasing.append(1)
            else:
                problem.append(1)
                

    if len(increasing) >= 1 and len(decreasing) >= 1:
        return None
    if len(increasing) == 0 and len(decreasing) == 0:
        return None
    if len(increasing) != len(list) - 1 and len(decreasing) != len(list) -1:
        return None
    really_safe.append(1)
    


rows_as_lists = df.apply(lambda row: row.dropna().tolist(), axis=1)

for row in rows_as_lists:
    check_safe(row)


# for i in example:
#     check_safe(i)
        

print(sum(really_safe))
