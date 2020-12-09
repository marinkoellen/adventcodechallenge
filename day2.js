
//Day 2:
const input = require('fs').readFileSync('day2_input.txt', 'utf-8');
// console.log(input)

// Part 1:
//Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

// Remove line breaks and empty space and parse strings to integer
let passwords = input.split('\n')


// Remove NAs - empty strings 
passwords = passwords.filter(function (e) { return e });

function password_dictionary_task1(line) {
    let password_dictionary = {}
    let password_info = line.split(" ")
    let min_max = password_info[0].split("-")
    password_dictionary["min"] = parseInt(min_max[0])
    password_dictionary["max"] = parseInt(min_max[1])
    password_dictionary["alphabet_letter"] = password_info[1][0]
    password_dictionary["password"] = password_info[2]
    const password_current = password_info[2].split('')
    const charMatches = password_current.filter(x => x == password_dictionary["alphabet_letter"]).length;
    if (charMatches >= password_dictionary["min"] && charMatches <= password_dictionary["max"]) {
        password_dictionary["password_flag"] = true;
    } else {
        password_dictionary["password_flag"] = false;

    }
    return password_dictionary
}


let password_dictionary_complete = passwords.map(password_dictionary_task1);
var passwords_valid_list = password_dictionary_complete.filter(function (password_dict) {
    return password_dict.password_flag === true;
});

console.log(`There are ${passwords_valid_list.length} valid passwords for part 1`);


// Part 2 

//Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.


function password_dictionary_task2(line) {
    let password_dictionary = {}
    let password_info = line.split(" ")
    let min_max = password_info[0].split("-")
    password_dictionary["first_pos"] = parseInt(min_max[0])
    password_dictionary["second_pos"] = parseInt(min_max[1])
    password_dictionary["alphabet_letter"] = password_info[1][0]
    password_dictionary["password"] = password_info[2]
    const password_current = password_info[2].split('')
    const isAtPositionOne = password_current[password_dictionary["first_pos"] - 1] === password_dictionary["alphabet_letter"];
    const isAtPositionTwo = password_current[password_dictionary["second_pos"] - 1] === password_dictionary["alphabet_letter"];
    // Learnt that you could add true or falses together to calculate exclusive or
    if (isAtPositionOne + isAtPositionTwo === 1) {
        password_dictionary["password_flag"] = true;
    } else {
        password_dictionary["password_flag"] = false;
    }
    return password_dictionary
}


let password_dictionary_complete2 = passwords.map(password_dictionary_task2);
var passwords_valid_list2 = password_dictionary_complete2.filter(function (password_dict) {
    return password_dict.password_flag === true;
});

console.log(`There are ${passwords_valid_list2.length} valid passwords for part 2`);

