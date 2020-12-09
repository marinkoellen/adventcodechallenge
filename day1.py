#day 1


#Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

#Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.


#part 1
text_file = open("day1_input.txt",'r').read().split('\n')


if "" in str(text_file):
    text_file.remove("")
#convert string to int using map function
input_number_list = []

# If you do want to pass a string representation of a float to an int
# Get a value error if you pass a string representation of a float to an int

for string in text_file:
    int_update = int(float(string))
    input_number_list.append(int_update)


#Need a way to generate all combinations of 2 numbers in a list + then filter to only those that sum to 2020

from itertools import combinations

combinations_list = list(combinations(input_number_list, 2))


def check2020(values):
    return sum(values) == 2020

result = list(filter(check2020, combinations_list))
sum_result = result[0][0] + result[0][1]
multiply_result = result[0][0] * result[0][1]
print(f"The numbers {result[0][0]} and {result[0][1]} sum to {sum_result} and multiply to {multiply_result}")

combinations_list_3 = list(combinations(input_number_list, 3))
result_3 = list(filter(check2020, combinations_list_3))
sum_result = result_3[0][0] + result_3[0][1] + result_3[0][2]
multiply_result = result_3[0][0] * result_3[0][1] * result_3[0][2]
print(f"The numbers {result_3[0][0]} and {result_3[0][1]} and {result_3[0][2]} sum to {sum_result} and multiply to {multiply_result}")

