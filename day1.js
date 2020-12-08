//Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

//Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.



const input = require('fs').readFileSync('day1_input.txt', 'utf-8');


// Part 1:


// Remove line breaks and empty space and parse strings to integer
let numbers = input.split('\n').map(x => parseInt(x));


// Remove NAs - empty strings that become NAN when you use parseInt over list
const number_input_ready = numbers.filter(value => !Number.isNaN(value));



// This function has some issues, assumes that there is only 1 pair in list that equal the sum requirement - would break with more
function get_numbers(numbers_list, sum_requirement) {
    for (let i = 0; i <= numbers_list.length; i++) {
        //Each input - 2020 to find difference
        let partOneOf2020 = sum_requirement - numbers_list[i];
        let index = numbers_list.findIndex(x => x == partOneOf2020);

        if (numbers_list.filter(x => x == partOneOf2020).length == 1) {
            return [i, index]
        }
    }


}

// Function presents results:

function present_list_items(index1, index2, number_list) {
    let value1 = number_list[index1]
    let value2 = number_list[index2]
    let sum_total = value1 * value2;
    let add_total = value1 + value2;

    console.log(`The numbers ${value1} and ${value2} add to ${add_total} and their product is ${sum_total}`);
}


// Trying destrcuturing in arrays - not really important but remembered destructuring 
const [number_index_1 = 0, number_index_2 = 0] = get_numbers(number_input_ready, 2020)

present_list_items(number_index_1, number_index_2, number_input_ready)

// Part 2:

// This option prints out all combinations regardless if they are the same combo

function get_three_numbers(numbers, sum_requirement) {
    for (let i = 0; i < numbers.length; i++) {
        let first = number_input_ready[i];

        for (let j = 0; j < numbers.length; j++) {
            const second = numbers[j];

            for (let k = 0; k < numbers.length; k++) {
                const third = numbers[k];

                if ((first + second + third) === sum_requirement) {

                    console.log(`The numbers ${numbers[i]} and ${numbers[j]} and ${numbers[k]} add to ${first + second + third} and their product is: ${first * second * third}`);
                }
            }
        }
    }
}

get_three_numbers(number_input_ready, 2020)