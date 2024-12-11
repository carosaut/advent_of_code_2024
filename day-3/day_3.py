import ast

# instructions = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

from day_3_data import instructions

indices = []
start = 0
substring = 'mul('

def find_indicies(string, substring):
    start = 0
    while True:
        index = string.find(substring, start)
        if index == -1: 
            break
        indices.append(index+3)
        start = index + len(substring)
    return indices

# print(find_indicies(instructions, substring))

lst_of_indicies = find_indicies(instructions, substring)


nums_to_multiply = []  
for i in lst_of_indicies:
    start = i
    next_closing_paren = instructions.index(')', start)
    lenght_of_string = next_closing_paren - start
    if lenght_of_string <= 8 and lenght_of_string >= 4:
        string_of_num = instructions[i:next_closing_paren+1]
        if ',' not in string_of_num:
            pass
        elif string_of_num.index(',',0) in [2,3,4]:
                nums_to_multiply.append(string_of_num)
        

string_to_int = [ast.literal_eval(item) for item in nums_to_multiply]

list_for_summing = []

for i in string_to_int:
    multiply_result = i[0] * i[1]
    list_for_summing.append(multiply_result)
print(sum(list_for_summing))




# print(instructions.find('mul('))

# for index, letter in instructions:
    
    
    
#     if letter == 'm':
#         second_letter = instructions[index + 1]
#         if second_letter = 'u':
#             third_letter = instructions[index + 2]
#             if 

