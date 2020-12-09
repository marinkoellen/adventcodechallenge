#Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.



text_file = open("day4_input.txt",'r').read().split('\n')
print((text_file))


codes = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

sortedPassports = []
temp = []
# Sort codes into single passports
for ind, passport_line in enumerate(text_file):
    if passport_line != '':
        temp.append(passport_line)
        # if we get to end of passport array or we get to an empty string indicating end of passport then push to sorted passports and reset temp
    if (ind == (len(text_file) -1) or  passport_line == ''):
        sortedPassports.append(temp)
        temp = []


validPassports = 0
for currentPassport in sortedPassports:
    consolidatedPassport = ' '.join(currentPassport)
    verifiedCodes = []

    for code in codes:
        if code in consolidatedPassport:
            verifiedCodes.append(code)
    
    if len(verifiedCodes) == 7:
        validPassports += 1


print(f"There are {validPassports} valid passports using part 1 rules")
