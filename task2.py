import re

parsed_list = []

with open("skychallenge_accounting_input.txt", "r") as myfile:
    data = myfile.read()
    parsed_list = [int(element) for element in re.findall(r'-?\d+', data)]


def sum_of_all_digits(tested_list):
    result = 0
    for element in tested_list:
        result += element
    return result


print(f"list of all founded digits: {parsed_list}")
print(f"final result is {sum_of_all_digits(parsed_list)}")
