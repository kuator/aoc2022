import re

def to_int(arr):
    return list(map(int, arr))

with open('input', 'r') as reader:
    string = reader.read()

calories = list(filter(
    None,
    re.split(r'\n{2,}', string),
))

calories = list(map(
    lambda c: sum(to_int(c.split())),
    calories,
))

calories = sorted(calories, reverse=True)

print(calories[0])
print(calories[0]+ calories[1]+ calories[2])
