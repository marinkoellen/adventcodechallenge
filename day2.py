
#Day 2:
#Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.


text_file = open("day2_input.txt",'r').read().split('\n')
print(len(text_file))
if "" in str(text_file):
    text_file.remove("")

print(len(text_file))

#convert each line in to a dictionary and a flag for whether the password passes the policy or not
def convert_line_to_dictionary(line):
    password_dictionary = {}
    current_password_details = line.split()
    min_max = current_password_details[0].split("-")
    password_dictionary["min"] = int(min_max[0])
    password_dictionary["max"] = int(min_max[1])
    password_dictionary["alphabet_letter"]= current_password_details[1][0]
    password_dictionary["password"] = current_password_details[2]
    char_count_in_password = password_dictionary["password"].count(password_dictionary["alphabet_letter"])
    password_dictionary["password_flag"] = password_dictionary["min"] <= char_count_in_password <= password_dictionary["max"]
    return password_dictionary

# Apply to each line in the text file
password_details_list = [convert_line_to_dictionary(password_and_policy) for password_and_policy in text_file]

# Reduce password list to only valid passwords bsaed on password_flag key
valid_passwords = [x['password'] for x in password_details_list if x['password_flag'] == True]

# Find how many valid passwords there are
print(f"There are {len(valid_passwords)} valid passwords using part 1 rules")



#Part 2:
#Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.



#Learnt that python has an exclusive or using ^
#convert each line in to a dictionary and a flag for whether the password passes the policy or not

def convert_line_to_dictionary_part2(line):
    password_dictionary = {}
    current_password_details = line.split()
    min_max = current_password_details[0].split("-")
    password_dictionary["first_pos"] = int(min_max[0])
    password_dictionary["second_pos"] = int(min_max[1])
    password_dictionary["alphabet_letter"]= current_password_details[1][0]
    password_dictionary["password"] = current_password_details[2]
    char_in_first_position = password_dictionary["password"][password_dictionary["first_pos"] - 1] == password_dictionary["alphabet_letter"]
    char_in_second_position = password_dictionary["password"][password_dictionary["second_pos"] - 1] == password_dictionary["alphabet_letter"]
    password_dictionary["password_flag"] = char_in_first_position ^ char_in_second_position
    return password_dictionary

# Apply to each line in the text file
password_details_list2 = [convert_line_to_dictionary_part2(password_and_policy) for password_and_policy in text_file]

# Reduce password list to only valid passwords based on password_flag key
valid_passwords2 = [x['password'] for x in password_details_list2 if x['password_flag'] == True]

# Find how many valid passwords there are
print(f"There are {len(valid_passwords2)} valid passwords using part 2 rules")
